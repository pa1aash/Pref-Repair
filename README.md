# Pref-Repair

Revealed-preference consistency **repair** for LLM agents.

The literature on economic rationality in language models is a measurement literature: it
scores agents against the revealed-preference axioms (GARP / WARP / SARP) and reports how
often they are violated. This project asks the constructive question instead — given a
choice sequence that violates GARP, can an inference-time layer project it onto the nearest
rationalizable sequence at bounded utility cost, and does doing so make the agent a *better*
decision-maker or merely a more consistent one?

## Status

Early. This repository currently holds the planning brief, a characterisation of its claims,
and the audit trail behind them. No experiment code, no projection implementation, and no
model calls have been made yet.

## Layout

| Path | Contents |
|---|---|
| `docs/` | Planning brief (read-only input), claim ledger, venue notes, decision log |
| `audit/` | Instrument calibration, reference ledger, kill-check verdicts |
| `src/` | Implementation (empty) |
| `results/` | Experiment outputs (empty) |
| `paper/` | Manuscript sources (empty) |
| `scripts/` | Repository tooling |

## Target

NeurIPS 2026 EconML workshop.

## Environment

Python 3.13.12 (pinned in `.python-version`); `pip install -r requirements.txt`.
The LP and MILP formulations run on SciPy's HiGHS backend — CPU only, no accelerator needed.

## License

MIT. See `LICENSE`.
