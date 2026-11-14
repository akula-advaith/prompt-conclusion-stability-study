# Submission readiness audit — 14 November 2026

## Overall decision

**Not yet final-submission ready.** The project has substantial evidence for G1–G3 and the core G4 paper/repository artifacts exist. The remaining issues are material: human review of AI-assisted labels, independent source/citation checks, complete first-paper packaging, provenance completion, and the five-minute demonstration.

## Gate review

| Gate | Assignment threshold | Current audit |
|---|---|---|
| G1 — Research brief | One-page gap brief, original supporting papers, focused question, pathway, compute/data feasibility | **Prepared / provisional.** Brief and plan exist. Recheck that primary sources support the gap framing and preserve “novelty not established.” |
| G2 — Baseline verification | Accessible dataset, environment check, runnable baseline, measured output, validation report | **Evidence present with limitation.** Actual baseline notebook, JSON run, comparator smoke tests and validation report are now stored. The development conclusion omitted a material qualification; it is documented, not hidden. |
| G3 — Experimental evidence | Frozen protocol, actual outputs/logs, tables/plots, deeper analysis | **Substantially complete; human validation pending.** 48 raw outputs, analysis CSVs, plots and failure cases are present. All labels/scores are AI-assisted first-pass assessments and need human review. |
| G4 — Paper and reproducibility | Paper PDF + LaTeX, GitHub repository, AI audit, 5-minute demo | **Partially complete.** Second paper source/PDF/BibTeX/figures and repository are present. AI audit is partial, first-paper PDF/figure package needs validation, human review/citation verification is open, and demo is pending. |

## Critical blockers before submission

1. **Human annotation review:** review all 48 output assessments and all 48 pairwise labels against the eight source abstracts. Record corrections in separate versioned files; never edit raw model outputs.
2. **Citation/source audit:** verify all second-paper and first-paper references at publisher/official records and check each citation supports the nearby claim. Check dataset-specific reuse/license conditions.
3. **First paper packaging:** add/verify the compiled first literature-review PDF and its referenced prompt_refinement.jpeg source figure in GitHub; run its LaTeX build.
4. **Provenance:** retain the authentic Phase III debug log and outputs; add the actual prompt/version-to-code-commit/diff mapping if available. Do not reconstruct or invent missing logs.
5. **Demonstration:** prepare and rehearse a five-minute walkthrough: research question and link to review; baseline and main notebook; dataset hash/config; actual raw outputs; two result plots and one failure case; limitations/AI provenance. Be prepared to rerun one validator or summary script.

## Repository checks to complete

- Run the README commands from a clean environment and mark anything not tested as [TEST REQUIRED].
- Confirm dataset access, attribution and licence handling from publisher records.
- Confirm dependency compatibility and clarify that CUDA/PyTorch must match the actual environment.
- Confirm first-paper PDF/figure, second-paper PDF/source/.bib/three figures and all experiment raw files are in the final branch.
- Make historical pre-main-run Phase II/III status documents clearly labelled as historical; retain the frozen v1.4 plan as a pre-collection protocol snapshot.

## Claims that are currently defensible

- The main run produced 48 generations under the recorded 8 × 3 × 2 design with pinned model revisions and greedy settings.
- The first-pass AI-assisted labels report 25 stable, 15 emphasis-shift, 8 substantive-shift and 0 contradiction pairs.
- The paper's quality and prompt-pair findings are descriptive, not statistically significant or generalizable.
- The two model conditions are from one Qwen2.5 family; this is not cross-family evidence.
- The adapted PSS-style measure is study-specific and is not a full ProSA benchmark replication.

Do not claim independent human validation, cross-family generalization, statistical significance, or a completed five-minute demonstration.
