"""CCEI, GARP and Bronars power for two-good budget-set data.

Guards against the trap in docs/METHOD_NOTE_Q6.md: with discrete prices an exact budget tie
lets a naive bisection report CCEI = 1.0 while GARP is violated, because the supremum is never
attained and bisection only ever tests strictly interior points. The design fix is continuous
prices plus budget exhaustion; the implementation fix is `exact_tie_count`, which reports how
many ordered pairs sit on an exact tie so a false 1.0 can be detected rather than trusted.
"""
from __future__ import annotations
import numpy as np


def revealed_matrix(p: np.ndarray, x: np.ndarray, e: float = 1.0) -> np.ndarray:
    """R0[i, j] = True iff bundle i is directly revealed preferred to j at efficiency e.

    e * (p_i . x_i) >= p_i . x_j
    """
    exp_own = np.einsum("ij,ij->i", p, x)          # p_i . x_i
    cross = p @ x.T                                # cross[i, j] = p_i . x_j
    return (e * exp_own[:, None]) >= cross - 1e-12


def strict_matrix(p: np.ndarray, x: np.ndarray, e: float = 1.0) -> np.ndarray:
    exp_own = np.einsum("ij,ij->i", p, x)
    cross = p @ x.T
    return (e * exp_own[:, None]) > cross + 1e-12


def exact_tie_count(p: np.ndarray, x: np.ndarray, tol: float = 1e-9) -> int:
    """Ordered pairs (i, j), i != j, with p_i.x_i == p_i.x_j — the Lemma-1 trap condition."""
    exp_own = np.einsum("ij,ij->i", p, x)
    cross = p @ x.T
    d = np.abs(exp_own[:, None] - cross)
    np.fill_diagonal(d, np.inf)
    return int((d < tol).sum())


def _closure(m: np.ndarray) -> np.ndarray:
    """Transitive closure by Warshall."""
    r = m.copy()
    n = r.shape[0]
    for k in range(n):
        r |= r[:, k][:, None] & r[k, :][None, :]
    return r


def garp_holds(p: np.ndarray, x: np.ndarray, e: float = 1.0) -> bool:
    """GARP at efficiency e: no i R j (transitively) with j P0 i strictly."""
    R = _closure(revealed_matrix(p, x, e))
    P = strict_matrix(p, x, e)
    return not (R & P.T).any()


def ccei(p: np.ndarray, x: np.ndarray, tol: float = 1e-6) -> float:
    """Afriat's Critical Cost Efficiency Index by bisection on e."""
    if garp_holds(p, x, 1.0):
        return 1.0
    lo, hi = 0.0, 1.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if garp_holds(p, x, mid):
            lo = mid
        else:
            hi = mid
    return lo


def bronars(p: np.ndarray, incomes: np.ndarray, n: int = 2000, seed: int = 0):
    """Bronars power: fraction of uniform-random agents violating GARP on these budget sets.

    Depends only on prices and incomes — computable before any model is queried.
    Returns (power, mean simulated CCEI).
    """
    rng = np.random.default_rng(seed)
    T, K = p.shape
    viol = 0
    cs = np.empty(n)
    for r in range(n):
        w = rng.dirichlet(np.ones(K), size=T)      # uniform on the budget hyperplane
        xr = w * incomes[:, None] / p
        ok = garp_holds(p, xr, 1.0)
        viol += (not ok)
        cs[r] = 1.0 if ok else ccei(p, xr)
    return viol / n, float(cs.mean())


def predictive_success(pass_rate: float, power: float) -> float:
    """Selten's m = pass rate - (1 - power)."""
    return pass_rate - (1.0 - power)
