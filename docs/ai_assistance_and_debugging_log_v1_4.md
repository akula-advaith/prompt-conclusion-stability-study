# AI Assistance and Research Provenance Log — v1.4

**Project:** Prompt Sensitivity and Stability of LLM-Generated Scientific Conclusions  
**Purpose:** Record AI assistance and the evidence available for human verification. This consolidated log is not a substitute for authentic prompts, Colab outputs, code revisions and decisions required by the instructor.

## Recorded development and debugging events

The Phase II/III development record documents environment checks, CPU-to-GPU runtime correction, dependency warnings, model-loading smoke tests, an arXiv timeout, failed structured-output attempts, prompt simplification, model revision pinning and a source-fidelity limitation in a development output.

## Main experiment and analysis update

| Activity | AI-assisted contribution | Evidence retained | Human verification / boundary |
|---|---|---|---|
| Experiment implementation | Assisted in preparing and refining the frozen v1.4 Colab notebook and validation/checkpoint logic. | Main experiment notebook | The user's actual run, not generated code, is the evidence for execution. |
| Main data collection | User executed the main notebook in Colab and supplied the resulting JSON for analysis. | Raw main-run JSON and CSV | 48 outputs across 8 abstracts, 3 prompts and 2 models; preserve raw model text unchanged. |
| Output annotation | AI assisted with first-pass quality ratings for conclusion fidelity, evidential support and scope/qualification preservation. | AI-assisted annotation CSV | These ratings are not independent human ground truth; review all records against the abstracts. |
| Pairwise comparisons | AI assisted in assigning stable, emphasis-shift, substantive-shift or contradiction labels. | Pairwise relation CSV | Review all 48 pair labels; do not describe them as independent human judgments. |
| Descriptive analysis | AI assisted in summarizing annotations, pairwise comparisons and TF-IDF lexical-overlap results. | Analysis report, CSVs and figures | TF-IDF is lexical overlap, not a semantic truth metric. Adapted PSS-style score is study-specific, not a full ProSA replication. |
| Manuscript preparation | AI assisted with organization and drafting of the second-paper text and LaTeX/figure integration. | LaTeX source, bibliography and PDF draft | Author must verify every claim, citation, figure, affiliation and limitation. |
| Repository documentation | AI assisted in organizing files and drafting README and reproducibility notes. | Repository documents and scripts | Student should inspect the structure, run validation and understand all included files. |

## Main-run configuration recorded in the raw evidence

- Dataset: `study_sources_v1_1_verified.json`, v1.1; SHA-256 `8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295`.
- 8 abstracts × 3 prompt conditions × 2 model sizes = 48 generations.
- Models: `Qwen/Qwen2.5-0.5B-Instruct` and `Qwen/Qwen2.5-1.5B-Instruct`, with pinned revisions in the raw records.
- Greedy decoding (`do_sample=false`), `max_new_tokens=100`, seed 42 recorded before each generation.
- Recorded environment: Python 3.13.16, PyTorch 2.14.1+cu130, Transformers 5.22.1, Tesla T4.

## Required final human actions

1. Review the 48 output annotations and 48 pairwise relation labels against the supplied abstracts.
2. Verify sources, DOI/URLs, licenses and manuscript references at publisher sources.
3. Confirm final numerical tables and figures match raw and derived files.
4. Add authentic prompt transcripts and code commit/diff evidence if required by the course.
5. Record actual human corrections and decisions only when they occur; do not invent examples.
6. Disclose AI assistance according to institute/course rules.

## Integrity boundary

No model training or fine-tuning was conducted. The study is a controlled comparison of prompt conditions and two model sizes within one model family. Only one greedy generation was collected per source × prompt × model condition. Annotations are AI-assisted and must be human-reviewed before final claims. No statistical-significance claim is supported by the current descriptive analysis.
