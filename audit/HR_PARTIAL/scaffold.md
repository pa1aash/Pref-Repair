# Scaffold — revealed-preference-repair-llm-4f6896

> PRIVATE PLANNING DOCUMENT. Must not appear anywhere in the final report.

## User Prompt (VERBATIM — gospel)

Has any published or preprinted work proposed an inference-time or training-time
intervention that CORRECTS, PROJECTS, REPAIRS, or otherwise ENFORCES revealed-preference
consistency (GARP/WARP/SARP compliance, or minimal-perturbation restoration of
rationalizability) on the choices or outputs of an LLM-based or AI agent — as opposed to
merely measuring or scoring such consistency? Separately: has the relationship between
enforced choice-coherence and downstream decision-quality or task performance been
empirically tested for LLM agents, in either direction? Cover the economics literature
(Afriat/Varian/Houtman-Maks efficiency and repair methods) and the ML/alignment literature
(coherence theorems, Bradley-Terry/RLHF consistency violations, Nash learning from human
feedback) as two related but distinct search fronts.

## Run config

- vault_tag: `revealed-preference-repair-llm-4f6896`
- query_file_path: `research/query-revealed-preference-repair-llm-4f6896.md`
- modality: **collect → synthesize** (primary: collect; see rationale)
- vault: this project directory (scoped, 0 prior notes at run start)

## Modality classification rationale

The query has two halves with different modalities.

Half one — "has any work proposed an intervention that corrects/projects/repairs/enforces
revealed-preference consistency on an LLM agent" — is an **occupancy question**. It is
answered by enumerative coverage: the deliverable is a defensible census of what exists,
per-work, with named fields (mechanism, training-time vs inference-time, axiom system,
whether it repairs or merely measures). That is **collect**.

Half two — "has the relationship between enforced choice-coherence and downstream decision
quality been empirically tested, in either direction" — cannot be answered by enumeration
alone, because the relevant evidence is scattered across two literatures that do not cite
each other and use incompatible vocabulary. Deciding whether the question is open requires a
**defended thesis**: that is **synthesize**.

Primary label: **collect**, with a synthesize obligation on the second half. Drafting style
should be per-work enumerative for half one and argued-with-evidence-chains for half two.

## Two search fronts (binding, from the query)

1. **Economics front** — Afriat / Varian / Houtman–Maks efficiency and repair methods,
   GARP/WARP/SARP, CCEI, money-pump index, budget-set demand data.
2. **ML/alignment front** — coherence theorems, Bradley–Terry / RLHF consistency violations,
   Nash learning from human feedback, von Neumann winner, reward-model intransitivity.

These are related but distinct and must be covered separately, not merged.

## Prior findings this run must not re-derive (from this session's Phase C/E work)

These are already established in this repository and are inputs, not open questions:

- The arXiv legacy full-text index is **partial** and includes bibliographies; a zero from it
  is weak evidence of absence. See `audit/INSTRUMENT_CALIBRATION.md`.
- **Chadwick, Kahng & Kipper (HAR 2025)**, "Dutch books and money pumps" — an inference-time
  rationality layer that repairs LLM preference intransitivity and probabilistic incoherence,
  with a faithfulness constraint. NOT on arXiv. Already found and read.
- **Andrews, arXiv:2608.05015** — training-time penalty, theory only, no experiments.
- **Aguiar & Kashaev, arXiv:2603.23993** — training-time GARP intervention (fine-tuning on
  GARP-consistent synthetic data).
- **Zhang et al., arXiv:2602.19041** "Back to Blackwell" — accepts cycles, technical-necessity
  grounds, not a normative argument against enforcement.
- The RePEc family (EconPapers, IDEAS) is **not headlessly searchable** — a standing gap.

The run's value-add is: (a) find what these missed, especially in the ML/alignment front and
outside arXiv, and (b) settle half two.

## Wrapper requirements

- Save path: `research/notes/final_report_revealed-preference-repair-llm-4f6896.md` (pipeline default; no external wrapper).
- Citation format: inline links to primary sources, arXiv IDs where they exist, venue named
  for non-arXiv work.
- Terminal sections: none mandated beyond the pipeline's own.
- Constraint inherited from the calling session: **headless retrieval only**. No browser.

## Tier rationale

_Filled in after step 1._

## Tier rationale

**`full` / `argumentative` / `inline`.** The query is research-grade and contested: it asks for a
defensible occupancy census across two literatures that use incompatible vocabulary and do not cite
each other, and then asks a second question ("has the coherence↔quality link been tested, in either
direction") whose answer requires weighing scattered and partial evidence rather than looking
something up. It carries fourteen sub-questions, an explicit two-front structure, and an explicit
demand that near-misses be distinguished from hits. A `light` run would produce a list of papers and
miss the thing that matters — whether the near-neighbours already occupy the ground. Tiering up is
also the safer error here: this run's output feeds a novelty judgement, and a false "nothing exists"
is the most expensive mistake available.

`inline` citations rather than the wikilink default because the report is an audit artefact that has
to be readable outside this vault by a reviewer who cannot resolve `[[note-id]]` links.
