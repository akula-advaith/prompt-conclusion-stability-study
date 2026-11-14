# Assignment requirement-to-evidence map

This map is aligned to the instructor's 11-page “AI Tools for Research” assignment. Status reflects the repository on 14 November 2026; it does not imply that pending human checks or the demonstration are complete.

| Assignment requirement | Project evidence | Status / note |
|---|---|---|
| Connect the second study to the completed literature review | papers/literature_review/, docs/G1_research_brief.pdf, second-paper Introduction/Related Work | Prepared; the G1 brief is still provisional and the first-paper PDF/figure packaging must be complete. Verify source claims and references before submission. |
| Formulate testable research questions and success criteria | docs/phase_ii_experiment_plan_v1_4.md, papers/second_paper/second_research_paper.tex | Prepared. RQ1 covers source fidelity/conclusion stability; RQ2 compares lexical overlap with source-grounded relations. |
| Select accessible data and meaningful comparators | data/, frozen plan | Prepared: 8 publisher-linked abstracts, 3 prompt conditions and 2 Qwen2.5 sizes. The two models are within one family; this is a constrained comparative design, not cross-family evidence. |
| Freeze a fair protocol | docs/phase_ii_experiment_plan_v1_4.md, configs/main_experiment_v1_4.json, main notebook | Frozen v1.4. There is no train/test split because the study performs inference only and no model training; this is explicitly justified. |
| Configure environment and validate baseline | notebooks/01_phase_iii_baseline_validation.ipynb, results/baseline/, Phase III report and comparator assessment | Development baseline executed on a Tesla T4; pinned model and data checks plus metric tests recorded. A source-fidelity omission and failed output-format attempts are retained. |
| Use AI-assisted coding/debugging with actual evidence | docs/ai_assistance_log_v1_3.md, docs/ai_assistance_and_debugging_log_v1_4.md, Colab notebooks, baseline JSONs | Authentic development/debugging cases now linked. A complete prompt-to-code commit/diff ledger for every AI-assisted change is still not available. |
| Execute the main experiment and save outputs | notebooks/02_main_experiment_v1_4.ipynb, results/raw/ | Complete: 48 raw generations across 8 × 3 × 2; raw JSON retained. |
| Evaluate with predefined metrics and fair conditions | results/analysis/, scripts/validate_experiment_outputs.py, scripts/rebuild_descriptive_summaries.py | First-pass analysis present. Output and pairwise labels are AI-assisted; independent human review is pending. |
| Conduct deeper analysis and report limitations | analysis report, pairwise/TF-IDF summaries, failure cases, manuscript limitations | Complete as an exploratory first pass: prompt sensitivity, TF-IDF disagreement/overlap, source-fidelity failures and threats to validity are discussed. |
| Submit second research paper PDF, LaTeX, .bib and figures | papers/second_paper/ | Files and build workflow are present; the PDF builds. Draft is not submission-final until human annotation review, citation checks and author details are confirmed. |
| Provide a complete, reproducible GitHub repository | root README, data/, notebooks/, scripts/, configs/, results/, papers/, dependency files | Core package present. Verify first-paper PDF/build assets, and test reproduction commands in a clean environment before submission. |
| AI audit / research provenance | docs/ai_assistance_log_v1_3.md, docs/ai_assistance_and_debugging_log_v1_4.md, docs/research_decisions_v1_4.md | Partial: authentic debugging events and known failures are recorded. Add a more complete prompt/version-to-code-commit/diff and human-verification ledger if available. |
| Five-minute demonstration | Not yet included | Pending. Prepare and rehearse a code-and-results walkthrough, and be ready to rerun/defend one component. |

## Current overall position

G1–G3 have substantial supporting evidence. G4 is only partially complete: the second-paper draft, buildable LaTeX package and repository are present, but human assessment review, final source/citation verification, provenance completion, first-paper package validation and the five-minute demonstration remain open. Do not describe the submission as final until those checks are completed.
