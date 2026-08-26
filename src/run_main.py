"""Main experiment runner, per docs/MAIN_EXPERIMENT_PROTOCOL.md.

Local ollama only. Model-major, never interleaved (section 1's correctness requirement, not just
an optimisation -- a crash was observed this session when two models were held resident at once).

N=30 independent replicates per condition. Fresh, independently-drawn budget sets per (model,
condition, replicate) -- not the pilot's single fixed set. Capped 3-attempt retry protocol per
section 6: same budget set, fresh generation seed, up to 3 attempts; all attempts logged; a slot
failing all 3 is a residual discard, not silently dropped.

Conditions: baseline + reciprocal at both models; multiturn (format manipulation, section 3.1) at
qwen2.5:1.5b only.
"""
from __future__ import annotations
import json, sys, time, re, urllib.request
import numpy as np
sys.path.insert(0, "src")
from budget_sets import make as make_budget_set

URL = "http://localhost:11434/api/generate"
LINE = re.compile(r"ROUND\s*=\s*(\d+)\s+A\s*=\s*(-?\d+)\s+B\s*=\s*(-?\d+)", re.I)
LINE_ONE = re.compile(r"A\s*=\s*(-?\d+)\s+B\s*=\s*(-?\d+)", re.I)

N = 30
QWEN = "qwen2.5:1.5b-instruct-q4_K_M"
LLAMA = "llama3.2:3b-instruct-q4_K_M"
DESIGN = {
    QWEN: ["baseline", "reciprocal", "multiturn"],
    LLAMA: ["baseline", "reciprocal"],
}
COND_OFFSET = {"baseline": 0, "reciprocal": 1, "multiturn": 2}
MODEL_OFFSET = {QWEN: 0, LLAMA: 200_000}
OUT_PATH = "results/main_raw.json"


def budget_seed(model, condition, r):
    return 30_000_000 + MODEL_OFFSET[model] + COND_OFFSET[condition] * 1_000_000 + r


def gen_seed(r, attempt):
    return r + 1000 * (attempt - 1)


def one_call(model, text, seed, temperature=0.7, timeout=180, num_predict=700, num_ctx=4096):
    body = json.dumps({"model": model, "prompt": text, "stream": False,
                        "keep_alive": "30m",
                        "options": {"temperature": temperature, "seed": seed,
                                    "num_predict": num_predict, "num_ctx": num_ctx}}).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    t0 = time.time()
    d = json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    return d.get("response", ""), time.time() - t0


def prompt_single_turn(MN, condition):
    """baseline / reciprocal -- unchanged wording from src/run_pilot.py."""
    if condition == "baseline":
        rows = "\n".join(
            f"Round {i+1}: each token spent on A returns {m:.4f} units of A; "
            f"each token spent on B returns {n:.4f} units of B."
            for i, (m, n) in enumerate(MN))
    else:  # reciprocal
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


def prompt_multiturn_round(MN, round_idx, history_lines):
    m, n = MN[round_idx - 1]
    head = ("You are dividing 100 tokens between two goods, A and B, across 25 independent "
            "rounds, one round at a time. You must spend all 100 tokens every round. Choose "
            "the division you most prefer for THIS round only.")
    cur = (f"Round {round_idx} of 25: each token spent on A returns {m:.4f} units of A; "
           f"each token spent on B returns {n:.4f} units of B.")
    tail = ("\n\nRespond with exactly one line and nothing else:\nA=<tokens spent on A> "
            "B=<tokens spent on B>\nThe two numbers are integers summing to 100.\n"
            "Example: A=70 B=30")
    parts = [head]
    if history_lines:
        parts.append("Your choices in previous rounds:\n" + "\n".join(history_lines))
    parts.append(cur + tail)
    return "\n\n".join(parts)


def parse_single_turn(resp, MN):
    got = {}
    for r, a, b in LINE.findall(resp):
        r = int(r)
        if 1 <= r <= len(MN) and r not in got:
            a, b = int(a), int(b)
            if a >= 0 and b >= 0 and a + b == 100:
                got[r] = (a, b)
    return got


def run_single_turn_attempt(model, MN, condition, seed):
    text = prompt_single_turn(MN, condition)
    resp, wall = one_call(model, text, seed)
    got = parse_single_turn(resp, MN)
    return got, resp, wall


def run_multiturn_attempt(model, MN, seed):
    got = {}
    history_lines = []
    raw_parts = []
    wall_total = 0.0
    for i in range(1, len(MN) + 1):
        text = prompt_multiturn_round(MN, i, history_lines)
        resp, wall = one_call(model, text, seed + i, num_predict=16, num_ctx=4096)
        wall_total += wall
        raw_parts.append(f"[round {i}] {resp.strip()}")
        m = LINE_ONE.search(resp)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a >= 0 and b >= 0 and a + b == 100:
                got[i] = (a, b)
                history_lines.append(f"Round {i}: A={a} B={b}")
            else:
                history_lines.append(f"Round {i}: (invalid response, skipped)")
        else:
            history_lines.append(f"Round {i}: (invalid response, skipped)")
    return got, "\n".join(raw_parts), wall_total


def build_record(got, MN, model, condition, r, attempt, seed, wall, raw):
    idx = sorted(got)
    rec = {"model": model, "condition": condition, "replicate": r, "attempt": attempt,
           "seed": seed, "n_valid": len(idx), "wall_s": round(wall, 1), "raw": raw}
    if idx:
        m = MN[[i - 1 for i in idx]]
        tok = np.array([got[i] for i in idx], dtype=float)
        x = tok * m
        p = 1.0 / m
        rec["p"] = p.tolist()
        rec["x"] = x.tolist()
    return rec


def run_slot(model, condition, r, out):
    bset_seed = budget_seed(model, condition, r)
    MN, _, _ = make_budget_set(seed=bset_seed)
    for attempt in (1, 2, 3):
        s = gen_seed(r, attempt)
        try:
            if condition == "multiturn":
                got, raw, wall = run_multiturn_attempt(model, MN, s)
            else:
                got, raw, wall = run_single_turn_attempt(model, MN, condition, s)
            rec = build_record(got, MN, model, condition, r, attempt, s, wall, raw)
            rec["budget_seed"] = bset_seed
            out.append(rec)
            status = "OK" if rec["n_valid"] >= 20 else "FAIL"
            print(f"{model.split(':')[0][:8]:<8} {condition:<10} r={r:<3} attempt={attempt} "
                  f"valid={rec['n_valid']:>2}/25 {wall:6.1f}s {status}", flush=True)
            with open(OUT_PATH, "w") as f:
                json.dump(out, f)
            if rec["n_valid"] >= 20:
                return
        except Exception as e:
            rec = {"model": model, "condition": condition, "replicate": r, "attempt": attempt,
                   "seed": s, "budget_seed": bset_seed, "error": str(e)[:300]}
            out.append(rec)
            print(f"{model:<30} {condition} r={r} attempt={attempt} ERROR {str(e)[:80]}", flush=True)
            with open(OUT_PATH, "w") as f:
                json.dump(out, f)
    print(f"  -> residual discard: {model} {condition} r={r} after 3 attempts", flush=True)


def main():
    out = []
    for model, conditions in DESIGN.items():   # model-major, never interleaved
        for condition in conditions:
            for r in range(1, N + 1):
                run_slot(model, condition, r, out)
    print("DONE", len(out), "attempt-records logged")


if __name__ == "__main__":
    main()
