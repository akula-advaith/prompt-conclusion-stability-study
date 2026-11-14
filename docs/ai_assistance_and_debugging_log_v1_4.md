# AI Assistance and Research Provenance Log — v1.4

**Project:** Prompt Sensitivity and Stability of LLM-Generated Scientific Conclusions  
**Purpose:** Record the role of AI assistance and the evidence available for human verification. This is a consolidated working log, not a substitute for retaining the actual prompts, Colab outputs, code revisions and decisions required by the instructor.

## Recorded development and debugging events

The detailed Phase II/III development record is preserved in `docs/phase_ii_iii_status_pre_main_run.md` and in the baseline validation report. The authentic events recorded there include environment checks, CPU-to-GPU runtime correction, dependency warnings, model-loading smoke tests, an arXiv timeout, failed structured-output attempts, prompt simplification, model revision pinning and a source-fidelity limitation in the development output.

## Main experiment and analysis update

| Activity | AI-assisted contribution | Evidence retained | Human verification / boundary |
|---|---|---|---|
| Experiment implementation | Assisted in preparing and refining the frozen v1.4 Colab experiment notebook and its validation/checkpoint logic. | `notebooks/02_main_experiment_v1_4.ipynb` | The notebook's actual run must be distinguished from generated code; the raw output file is the evidence of the user-executed run. |
| Main data collection | The user executed the main notebook in Colab and provided the resulting JSON for analysis. | `results/raw/main_experiment_raw_outputs_v1_4.json` | 48 outputs are recorded across 8 abstracts, 3 prompts and 2 models. Raw model text is retained unchanged. |
| Output annotation | AI assisted with source-grounded first-pass quality ratings for conclusion fidelity, evidential support and scope/qualification preservation. | `results/analysis/annotations_ai_assisted.csv` | These scores are AI-assisted judgments, not independent human ground truth. Review all 48 records against the source abstracts. |
| Pairwise comparisons | AI assisted in assigning stable, emphasis-shift, substantive-shift or contradiction labels to prompt pairs. | `results/analysis/pairwise_conclusion_relations.csv` | Review all 48 pair labels. Do not describe them as independent human judgments. |
| Descriptive analysis | AI assisted in summarizing the annotations, pairwise comparisons and TF-IDF lexical-overlap results. | `results/analysis/analysis_report_v1_4.md`, CSV files and figures | Re-check the reported summaries against the CSVs. TF-IDF is lexical overlap, not a semantic truth metric. The adapted PSS-style score is study-specific, not a full ProSA replication. |
| Manuscript preparation | AI assisted in organizing and drafting the second-paper text and preparing LaTeX/figure integration from the documented protocol and results. | `papers/second_paper/second_research_paper.tex` and PDF | Human author must verify every claim, citation, figure, affiliation and limitation before submission. |
| Repository documentation | AI assisted in organizing the project files and drafting the README, reproduction notes and provenance record. | Repository documentation and scripts | The student should inspect the structure, run the validation script and understand all included files. |

## Main-run configuration recorded in the raw evidence

- Dataset: `study_sources_v1_1_verified.json`, version v1.1; SHA-256 `8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295`.
- 8 scientific abstracts × 3 prompt conditions × 2 model sizes = 48 generations.
- Models: `Qwen/Qwen2.5-0.5B-Instruct` and `Qwen/Qwen2.5-1.5B-Instruct`, with pinned revisions recorded in each raw record.
- Greedy decoding (`do_sample=false`), `max_new_tokens=100`, seed 42 recorded before each generation.
- Recorded main-run environment: Python 3.13.16, PyTorch 2.14.1+cu130, Transformers 5.22.1, Tesla T4.

## Required final human actions

1. Review the 48 output annotations and 48 pairwise relation labels against the supplied abstracts.
2. Verify the sources, DOI/URLs, licenses and all manuscript references at their publishers.
3. Confirm all final numerical tables and figures match the provided raw/derived files.
4. Replace this consolidated summary with, or supplement it by, the authentic prompt transcript and code commit/diff records required by the course if those are separately required.
5. Record actual human corrections and decisions only when they occur; do not invent examples.
6. Disclose AI assistance according to current institute/course rules.

## Integrity boundary

No model training or fine-tuning was conducted. The study is a controlled comparison of prompt conditions and two model sizes within one model family. Only one greedy generation was collected per source × prompt × model condition. The annotations are AI-assisted and must be human-reviewed before final claims. No statistical-significance claim is supported by the current descriptive analysis.

## Authentic development-log linkage

The earlier, contemporaneous Phase II/III log is retained at docs/ai_assistance_log_v1_3.md. It records actual observed environment outputs, failed multi-field and JSON output attempts, a network timeout, the unpinned comparator revision issue, a pinned comparator test, and the source-qualification omission. The accompanying raw development JSON files are stored in results/baseline/.

The v1.3 log predates the 10 November main run; it is a historical development record. This v1.4 log records later main-run and analysis assistance separately. Neither log substitutes for a complete prompt-by-prompt source-control diff ledger. Any further provenance entries must be based on authentic prompts, outputs and commits, not reconstructed or invented.
