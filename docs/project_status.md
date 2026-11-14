# Project status snapshot — 14 November 2026

This file is the current status index. Historical Phase II/III planning and baseline-validation documents remain in the repository to preserve the development trail; their pre-main-run wording should not be mistaken for the status of the November 10 main experiment.

| Work item | Status | Evidence / next action |
|---|---|---|
| G1 research brief | Prepared | See the G1 research brief in the project documentation package. |
| Phase II experiment plan | Frozen v1.4 | `docs/phase_ii_experiment_plan_v1_4.md`; retain as the protocol frozen before main collection. |
| Phase III baseline validation | Completed with a documented source-fidelity limitation | `docs/Phase_III_Baseline_Validation_Report_v1_4.md`; earlier reports are retained as historical evidence. |
| Main experiment | Executed | 48 records in `results/raw/main_experiment_raw_outputs_v1_4.json`; run the validator to check integrity. |
| Results and analysis | First-pass outputs prepared | `results/analysis/`; AI-assisted annotations and pair labels still require human review against the original abstracts. |
| Second paper | Draft prepared | `papers/second_paper/`; complete the human review checklist and citation audit before submission. |
| Literature-review paper | Source and manuscript retained | `papers/literature_review/`. |
| Repository reproducibility | Core source, notebook, data, code and analysis are present | Run the validation and summary-rebuild scripts from the repository root. |
| AI provenance | Consolidated working log retained | `docs/ai_assistance_and_debugging_log_v1_4.md`; supplement with authentic prompts or code diffs if the instructor requires them. |
| Five-minute demo | Pending | Prepare a walkthrough of the research question, notebook, results, limitations and provenance. |

## Scope reminders

- The study uses eight purposively selected abstracts; they are not a representative sample of scientific literature.
- Both evaluated models belong to the Qwen2.5 family; this is a within-family size comparison.
- One greedy generation was collected per source × prompt × model condition.
- AI-assisted scores and pairwise labels are not independent human ground truth.
- The PSS-style quantity is a study-specific adaptation inspired by ProSA/PSS, not a full replication of the original benchmark.
- The three outputs flagged by the one-sentence heuristic were retained unchanged.
