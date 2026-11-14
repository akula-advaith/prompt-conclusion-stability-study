# Evidence ledger — v1.4 (14 November 2026)

This file uses the assignment's three evidence labels: VERIFIED, INFERRED and UNKNOWN. “Verified” means checked against a primary source file or an actual execution artifact available in this project; it does not imply independent peer review.

## VERIFIED — source or execution evidence available

- The first literature-review manuscript and its LaTeX/BibTeX sources are in papers/literature_review/source/.
- The final Phase III v1.3 development JSON records Python 3.13.16, PyTorch 2.11.0+cu130, Transformers 5.20.2, Accelerate 1.15.0, Hub 1.33.0 and a Tesla T4. It records dataset v1.1 hash/schema checks, prompt-assembly checks and unit tests. Its model output omitted the source's recommendation for larger, fully powered trials.
- Phase III failure evidence is preserved in results/baseline/: initial multi-field output, two failed format/schema retries, single-conclusion pilot, unpinned comparator smoke test, revision-pinned comparator and final v1.3 validation JSON. All are development-only and excluded from the main sample.
- The main run JSON records 48 outputs for 8 abstracts × 3 prompts × 2 pinned Qwen2.5 revisions, greedy decoding, seed 42 and max 100 new tokens. The output validator checks dataset hash, expected coverage, empty outputs and model revision metadata.
- The main-run runtime recorded in raw evidence is Python 3.13.16, PyTorch 2.14.1+cu130, Transformers 5.22.1 and Tesla T4.
- The first-pass analysis files contain 48 output-level AI-assisted assessments and 48 pairwise relation labels. The reported totals (25 stable, 15 emphasis shifts, 8 substantive shifts, 0 contradictions) and model/prompt quality aggregates are traceable to the CSVs.
- The second paper PDF, LaTeX source, BibTeX file, verified BBL file, three figures and a successful GitHub Actions build are in papers/second_paper/.

## INFERRED — plausible interpretation, not guaranteed by the design

- P0/P1/P2 are intended to preserve the same task meaning. Perfect semantic equivalence cannot be guaranteed; the paper lists this as a threat to validity.
- The higher average quality and lower adapted score observed for the 1.5B model suggest a difference within this tested Qwen2.5 setup, not a general parameter-size effect.
- TF-IDF can help flag lexical-overlap patterns, but it cannot determine whether a scientific conclusion is true or source-faithful.

## UNKNOWN — evidence still missing

- Whether all 48 AI-assisted quality judgments and all 48 pairwise labels would be confirmed by an independent human annotator.
- Inter-annotator agreement; no second annotator is recorded.
- Stochastic run-to-run variation; only one greedy generation exists for each condition.
- Whether results generalize to other model families, larger/representative source sets, full-text evidence or hosted models.
- Whether every cited source and license has been independently rechecked by the student immediately before submission.
- Complete prompt/version-to-code-commit/diff provenance for every AI-assisted code change.
- Successful reproduction by a second student in a fresh environment.
- Completion of the five-minute demonstration and technical viva rehearsal.

## Integrity boundary

Do not move items from INFERRED or UNKNOWN to VERIFIED without new source checks, authentic execution output, or documented human review. Do not alter the raw main-run JSON. Store human corrections to labels in separate versioned files.
