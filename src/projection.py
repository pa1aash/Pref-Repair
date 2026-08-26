"""Minimal-perturbation GARP projection, per docs/METHOD_NOTE_Q3.md's recommended formulation.

Multiplier-free ordinal characterisation (Demuynck & Rehbeck 2023, Theorem 2). No Afriat
multipliers, no bilinear terms, no outer search over orderings. Solved as a single MILP on
scipy's HiGHS backend. Every returned x-tilde is verified independently via ccei.garp_holds
(Warshall closure) before being trusted -- a solver optimality report is never trusted alone.
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from ccei import garp_holds


def _cobb_douglas_warm_start(p: np.ndarray, x: np.ndarray, incomes: np.ndarray) -> np.ndarray:
    """Share-fitted Cobb-Douglas demand at the observed (p, I) -- feasible by construction,
    gives the solver an incumbent and a free sanity ceiling on the true minimum."""
    shares = (p * x) / incomes[:, None]          # expenditure share per good, per observation
    mean_share = shares.mean(axis=0)
    mean_share = mean_share / mean_share.sum()
    return (mean_share[None, :] * incomes[:, None]) / p


def project(p: np.ndarray, x: np.ndarray, incomes: np.ndarray, gamma: float | None = None,
            time_limit: float = 30.0):
    """Return (x_tilde, dose_L1, dose_Linf, solve_info).

    p, x: (T, K) prices and observed bundles. incomes: (T,) budget-exhaustion levels (p_t . x_t).
    gamma: strict-preference margin, expenditure units. Defaults to 1e-4 * min(incomes), per
    the method note's recommendation.
    """
    T, K = p.shape
    if garp_holds(p, x, 1.0):
        return x.copy(), 0.0, 0.0, {"status": "already_garp_consistent", "gap": 0.0}

    if gamma is None:
        gamma = 1e-4 * incomes.min()

    # --- variable layout ---
    # x_tilde: T*K continuous >= 0
    # u:       T continuous in [0, 1]
    # U_{t,v}: T*(T-1) binary, indexed by ordered pairs t != v
    pairs = [(t, v) for t in range(T) for v in range(T) if t != v]
    n_pairs = len(pairs)
    pair_idx = {tv: i for i, tv in enumerate(pairs)}

    n_x = T * K
    n_u = T
    n_U = n_pairs
    n_vars = n_x + n_u + n_U

    def x_idx(t, k):
        return t * K + k

    def u_idx(t):
        return n_x + t

    def U_idx(t, v):
        return n_x + n_u + pair_idx[(t, v)]

    alpha = incomes.max() + 1.0          # big-M, valid a priori under budget exhaustion (eq. 5)
    eps = 1.0 / (2 * T)                  # 0 < eps < 1/T

    rows, cols, vals, lb_list, ub_list = [], [], [], [], []
    row = 0

    def add_row(coeffs, lo, hi):
        nonlocal row
        for c, v in coeffs:
            rows.append(row); cols.append(c); vals.append(v)
        lb_list.append(lo); ub_list.append(hi)
        row += 1

    for (t, v) in pairs:
        # (1) u_t - u_v <= -eps + 2*U_{t,v}
        add_row([(u_idx(t), 1.0), (u_idx(v), -1.0), (U_idx(t, v), -2.0)], -np.inf, -eps)
        # (2) U_{t,v} - 1 <= u_t - u_v   =>   u_t - u_v - U_{t,v} >= -1
        add_row([(u_idx(t), 1.0), (u_idx(v), -1.0), (U_idx(t, v), -1.0)], -1.0, np.inf)
        # (3) p_t.x_tilde_t - p_t.x_tilde_v <= -gamma + alpha*U_{t,v}
        coeffs = [(x_idx(t, k), p[t, k]) for k in range(K)] + [(x_idx(v, k), -p[t, k]) for k in range(K)]
        coeffs.append((U_idx(t, v), -alpha))
        add_row(coeffs, -np.inf, -gamma)
        # (4) alpha*(U_{v,t} - 1) <= p_t.x_tilde_v - p_t.x_tilde_t
        #     => p_t.x_tilde_v - p_t.x_tilde_t - alpha*U_{v,t} >= -alpha
        coeffs = [(x_idx(v, k), p[t, k]) for k in range(K)] + [(x_idx(t, k), -p[t, k]) for k in range(K)]
        coeffs.append((U_idx(v, t), -alpha))
        add_row(coeffs, -alpha, np.inf)

    # (5) budget exhaustion, equality: p_t . x_tilde_t = I_t
    for t in range(T):
        coeffs = [(x_idx(t, k), p[t, k]) for k in range(K)]
        add_row(coeffs, incomes[t], incomes[t])

    A = np.zeros((row, n_vars))
    for r, c, v in zip(rows, cols, vals):
        A[r, c] = v
    lin_con = LinearConstraint(A, lb_list, ub_list)

    # --- objective: L1 via auxiliary d_{t,k} >= |x_t,k - x_tilde_t,k| ---
    n_d = T * K
    n_vars_full = n_vars + n_d

    def d_idx(t, k):
        return n_vars + t * K + k

    rows2, cols2, vals2, lb2, ub2 = [], [], [], [], []
    row2 = 0
    for t in range(T):
        for k in range(K):
            # x_tilde_t,k - d_t,k <= x_t,k
            rows2 += [row2, row2]; cols2 += [x_idx(t, k), d_idx(t, k)]; vals2 += [1.0, -1.0]
            lb2.append(-np.inf); ub2.append(x[t, k]); row2 += 1
            # x_t,k - x_tilde_t,k - d_t,k <= 0
            rows2 += [row2, row2]; cols2 += [x_idx(t, k), d_idx(t, k)]; vals2 += [-1.0, -1.0]
            lb2.append(-np.inf); ub2.append(-x[t, k]); row2 += 1

    A2full = np.zeros((row2, n_vars_full))
    Afull_top = np.hstack([A, np.zeros((A.shape[0], n_d))])
    for r, c, v in zip(rows2, cols2, vals2):
        A2full[r, c] = v
    A_all = np.vstack([Afull_top, A2full])
    lb_all = lb_list + lb2
    ub_all = ub_list + ub2
    lin_con_full = LinearConstraint(A_all, lb_all, ub_all)

    c_obj = np.zeros(n_vars_full)
    c_obj[n_vars:n_vars + n_d] = 1.0

    lb_vars = np.concatenate([np.zeros(n_x), np.zeros(n_u), np.zeros(n_U), np.zeros(n_d)])
    ub_vars = np.concatenate([np.full(n_x, np.inf), np.ones(n_u), np.ones(n_U), np.full(n_d, np.inf)])
    bounds = Bounds(lb_vars, ub_vars)
    integrality = np.concatenate([np.zeros(n_x), np.zeros(n_u), np.ones(n_U), np.zeros(n_d)])

    # warm start from Cobb-Douglas demand (feasibility only -- scipy.milp has no incumbent hook,
    # so this is used solely as a sanity ceiling on the reported distance, per the method note)
    x_cd = _cobb_douglas_warm_start(p, x, incomes)
    ceiling_dose = float(np.abs(x - x_cd).sum())

    res = milp(c_obj, constraints=[lin_con_full], bounds=bounds, integrality=integrality,
               options={"time_limit": time_limit})

    if not res.success:
        return None, None, None, {"status": "solve_failed", "message": res.message,
                                    "cd_ceiling_dose": ceiling_dose}

    x_tilde = res.x[:n_x].reshape(T, K)
    dose_l1 = float(res.x[n_vars:n_vars + n_d].sum())
    dose_linf = float(np.abs(x - x_tilde).max())

    verified = garp_holds(p, x_tilde, 1.0)
    gap = getattr(res, "mip_gap", None)

    return x_tilde, dose_l1, dose_linf, {
        "status": "solved", "verified_garp_consistent": bool(verified),
        "mip_gap": gap, "gamma": gamma, "cd_ceiling_dose": ceiling_dose,
        "solver_message": res.message,
    }
