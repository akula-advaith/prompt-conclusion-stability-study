# Submission readiness audit — 14 November 2026

## Overall decision

**The project is substantially assembled, but it is not yet final-submission ready.** The core research path, two papers, notebooks, 48-output run, analysis files and GitHub repository are present. The remaining work is mainly human validation, provenance, a clean reproduction check and the required demonstration.

## Gate review

| Gate | Instructor's requirement | Current position |
|---|---|---|
| G1 — Research brief | One-page gap brief, original supporting papers, focused question, pathway, data/compute feasibility | **Prepared.** The G1 brief and frozen plan are present. Keep novelty qualified; independently verify the source claims before submission. |
| G2 — Baseline verification | Accessible data, environment test, runnable baseline, measured output, validation report | **Substantial evidence with a limitation.** The development baseline and GPU environment were run and checked. The development output omitted the source's call for larger, fully powered trials; this is recorded as a fidelity failure. |
| G3 — Experimental evidence | Frozen protocol, genuine outputs/logs, tables/plots and one deeper analysis | **Main run complete; assessment review pending.** 48 raw generations, analysis files, three result plots, pairwise comparison and qualitative failure cases are present. The 48 output scores and 48 pairwise labels are AI-assisted first-pass assessments. |
| G4 — Paper and reproducibility | Final PDF + LaTeX + bibliography + figures, GitHub, AI audit and five-minute demonstration | **Partially complete.** Both papers and their source/bibliography files are in GitHub. Provenance is partial, clean-environment reproduction is not yet demonstrated, human review is open, and the five-minute demo is pending. |

## Confirmed deliverables

1. **First paper:** literature-review PDF, LaTeX source, BibTeX bibliography and embedded TikZ diagram are in `papers/literature_review/`. Its latest GitHub Actions compile completed successfully.
2. **Second paper:** PDF, LaTeX source, `.bib`, verified `.bbl`, three figures and human-review checklist are in `papers/second_paper/`.
3. **Experiment:** 8 abstracts × 3 prompt conditions × 2 pinned Qwen2.5 models = 48 raw generations. The exact prompts, source text, model revisions, seed, decoding settings and runtime are in the raw JSON.
4. **Analysis:** 48 AI-assisted output assessments and 48 AI-assisted pairwise labels. Counts are 25 stable, 15 emphasis shifts, 8 substantive shifts and 0 contradictions. These are not independent human judgments.
5. **Repository:** original project structure plus numbered handoff folders `03_Code_and_Notebooks`, `04_Dataset_and_Results` and `05_Research_Documentation`.

## Remaining work before submission

1. **Human annotation review:** read all 48 generated conclusions beside their source abstracts. Then review all 48 prompt-pair labels. Record corrections in a separate, versioned human-review file; never edit the raw model outputs.
2. **Source and citation audit:** verify every paper reference at its primary publisher or official record and check that it supports the nearby claim. The eight PLOS source records used in the experiment have had their title/DOI metadata checked against publisher pages, but that is not a full claim-to-citation audit for both papers. Recheck reuse and attribution terms before redistribution.
3. **AI provenance:** keep the authentic development/debugging log and add the actual prompt/version-to-code-commit/diff mapping if available. Do not reconstruct or invent missing records.
4. **Clean reproduction check:** clone the repository into a fresh environment, follow the README commands, run the validator and summary-rebuild script, and record any dependency or GPU setup steps that need adjustment. The current notebooks have been checked as files; that is not the same as a second-student reproduction.
5. **Five-minute demonstration:** prepare and rehearse a walkthrough covering the review-to-gap link, research question, baseline validation, main notebook, frozen dataset/hash, 48 outputs, two result plots, one source-fidelity failure, limitations and AI provenance. Be ready to rerun one validator or analysis command.

## Repository automation note

The latest first-paper workflow completed successfully. The latest second-paper workflow successfully regenerated the figures and compiled the manuscript, but its final push was rejected because the first- and second-paper workflows attempted to publish at the same time. This was a repository automation race, not a LaTeX compile failure. Both workflows now share a concurrency group and rebase generated commits onto the latest `main` before pushing. The already committed second-paper PDF remains present in `papers/second_paper/`.

## Defensible claims

- The main run produced 48 generations under the recorded 8 × 3 × 2 design, with pinned model revisions and greedy decoding.
- The first-pass AI-assisted labels report 25 stable, 15 emphasis-shift, 8 substantive-shift and 0 contradiction pairs.
- Findings are descriptive; the design does not establish statistical significance.
- Both models are from the Qwen2.5 family; the data do not support cross-family generalization or a general model-size claim.
- The adapted PSS-style value is study-specific and is not a full ProSA benchmark replication.
- Human-independent validation of the annotations and completion of the five-minute demonstration must not be claimed until performed.
