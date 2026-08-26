"""Exogenous payoff, per docs/MAIN_EXPERIMENT_PROTOCOL.md section 5.

A fixed, pre-registered, equal-weight Cobb-Douglas valuation, never fit to any agent's choices.
The optimal bundle at each budget line is closed-form and depends only on (p, income) -- never
on the agent's own x or x_tilde -- which is what makes this exogenous rather than a rationalising
fit to the observed data.
"""
from __future__ import annotations
import numpy as np


def cd_optimal_bundle(p: np.ndarray, incomes: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """Closed-form Cobb-Douglas demand x*_k = alpha_k * I / p_k, fixed weights, no fitting."""
    T, K = p.shape
    if K != 2:
        raise ValueError("fixed 0.5/0.5 weights assume K=2; generalise before using K != 2")
    weights = np.array([alpha, 1.0 - alpha])
    return (weights[None, :] * incomes[:, None]) / p


def payoff(x: np.ndarray, p: np.ndarray, incomes: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """Per-observation efficiency ratio U_exo(x) / U_exo(x*) in (0, 1]."""
    x_star = cd_optimal_bundle(p, incomes, alpha)
    u_x = np.prod(np.clip(x, 1e-12, None) ** np.array([alpha, 1 - alpha]), axis=1)
    u_star = np.prod(x_star ** np.array([alpha, 1 - alpha]), axis=1)
    return u_x / u_star


def mean_payoff(x: np.ndarray, p: np.ndarray, incomes: np.ndarray, alpha: float = 0.5) -> float:
    return float(payoff(x, p, incomes, alpha).mean())
