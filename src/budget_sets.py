"""Fixed budget sets for the pilot. Continuous prices, per docs/METHOD_NOTE_Q6.md."""
import numpy as np

def make(T=25, seed=20260826):
    """E3's generator with full float precision (NOT rounded to 2dp).

    M, N ~ U[0.1, 1.0] i.i.d., rejected unless max(M, N) >= 0.5.
    Commodity prices p = 1/M, 1/N; income normalised to 100.
    """
    rng = np.random.default_rng(seed)
    MN = []
    while len(MN) < T:
        m, n = rng.uniform(0.1, 1.0, 2)
        if max(m, n) >= 0.5:
            MN.append((m, n))
    MN = np.array(MN)
    p = 1.0 / MN
    inc = np.full(T, 100.0)
    return MN, p, inc
