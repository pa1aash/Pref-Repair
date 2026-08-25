"""Pilot runner. Local ollama only — no commercial endpoint is contacted.

Run order is model-major and never interleaved: all sessions for one model complete before the
next is loaded. Measured swap penalty on this machine is ~296 s, so interleaving would dominate
the run time. keep_alive holds the model resident between sessions.
"""
from __future__ import annotations
import json, sys, time, re, urllib.request
import numpy as np
sys.path.insert(0, "src")
from budget_sets import make

URL = "http://localhost:11434/api/generate"
LINE = re.compile(r"ROUND\s*=\s*(\d+)\s+A\s*=\s*(-?\d+)\s+B\s*=\s*(-?\d+)", re.I)


def prompt(MN, condition):
    """Two framings of the same budget sets. Reuses the E3 instrument's wording."""
    if condition == "baseline":
        rows = "\n".join(
            f"Round {i+1}: each token spent on A returns {m:.4f} units of A; "
            f"each token spent on B returns {n:.4f} units of B."
            for i, (m, n) in enumerate(MN))
        head = ("You have 100 tokens to divide between two goods, A and B, in each of 25 "
                "independent rounds. You must spend all 100 tokens every round. "
                "Choose the division you most prefer.")
    else:  # reciprocal — E3's strongest published manipulation, same budget line
        rows = "\n".join(
            f"Round {i+1}: it takes {1/m:.4f} tokens to obtain one unit of A; "
            f"it takes {1/n:.4f} tokens to obtain one unit of B."
            for i, (m, n) in enumerate(MN))
        head = ("You have 100 tokens to divide between two goods, A and B, in each of 25 "
                "independent rounds. You must spend all 100 tokens every round. "
                "Choose the division you most prefer.")
    tail = ("\n\nOutput exactly 25 lines and nothing else. Each line must be:\n"
            "ROUND=<n> A=<tokens spent on A> B=<tokens spent on B>\n"
            "The two numbers are integers summing to 100.\n"
            "Example of the required format: ROUND=1 A=70 B=30")
    return f"{head}\n\n{rows}{tail}"


def one_session(model, text, seed, temperature=0.7, timeout=900):
    body = json.dumps({"model": model, "prompt": text, "stream": False,
                       "keep_alive": "30m",
                       "options": {"temperature": temperature, "seed": seed,
                                   "num_predict": 700, "num_ctx": 4096}}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    t0 = time.time()
    d = json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    return d.get("response", ""), time.time() - t0


def parse(resp, MN, income=100.0):
    """Return (p, x, n_valid). A round is valid iff it parses and the two integers sum to 100."""
    got = {}
    for r, a, b in LINE.findall(resp):
        r = int(r)
        if 1 <= r <= len(MN) and r not in got:
            a, b = int(a), int(b)
            if a >= 0 and b >= 0 and a + b == 100:
                got[r] = (a, b)
    idx = sorted(got)
    if not idx:
        return None, None, 0
    m = MN[[i - 1 for i in idx]]
    tok = np.array([got[i] for i in idx], dtype=float)
    x = tok * m                      # units obtained = tokens * exchange rate
    p = 1.0 / m                      # commodity prices
    return p, x, len(idx)


def main():
    MODELS = ["qwen2.5:1.5b-instruct-q4_K_M", "llama3.2:3b-instruct-q4_K_M"]
    CONDS = ["baseline", "reciprocal"]
    SEEDS = list(range(1, 26))
    MN, _, _ = make()
    out = []
    for model in MODELS:                       # model-major: never interleave
        for cond in CONDS:
            text = prompt(MN, cond)
            for s in SEEDS:
                try:
                    resp, wall = one_session(model, text, s)
                    p, x, nv = parse(resp, MN)
                    rec = {"model": model, "condition": cond, "seed": s,
                           "n_valid": nv, "wall_s": round(wall, 1),
                           "raw": resp}
                    if p is not None:
                        rec["p"] = p.tolist(); rec["x"] = x.tolist()
                    out.append(rec)
                    print(f"{model.split(':')[0][:8]:<8} {cond:<10} seed={s:<3} "
                          f"valid={nv:>2}/25 {wall:5.1f}s", flush=True)
                except Exception as e:
                    out.append({"model": model, "condition": cond, "seed": s,
                                "error": str(e)[:200]})
                    print(f"{model:<30} {cond} seed={s} ERROR {str(e)[:70]}", flush=True)
                with open("results/pilot_raw.json", "w") as f:
                    json.dump(out, f)
    print("DONE", len(out), "sessions")


if __name__ == "__main__":
    main()
