# Research Decisions Log — Phase II/III v1.3

## D08 — Narrow output to one central conclusion sentence

- **Observation:** The first modular prompt requested a central conclusion and two key findings; the 0.5B baseline returned only the conclusion. A JSON retry produced code fences and placeholder findings. A second retry again failed to provide both fields.
- **Decision status:** Proposed in v1.3 as a protocol revision before main-data collection; must be confirmed against instructor expectations before the main run.
- **Rationale:** The core research question is conclusion stability. Requiring extra finding bullets introduces output-format compliance as a confound.
- **Evidence:** `phase3_baseline_validation_output.json`, `phase3_baseline_validation_retry.json`, `phase3_baseline_validation_retry2.json`, and `phase3_single_conclusion_baseline.json`.
- **Consequence:** Replace the old three-field output specification with one central-conclusion sentence only. Re-score neither pilot as main data; keep all pilots excluded from the main dataset.

## D09 — Pin model revisions

- **0.5B model:** `Qwen/Qwen2.5-0.5B-Instruct`, SHA `7ae557604adf67be50417f59c2c2f167def9a775`.
- **1.5B model:** `Qwen/Qwen2.5-1.5B-Instruct`, SHA `989aa7980e4cf806f80c7fef2b1adb7bc71aa306`.
- **Rationale:** A named model can move; the exact immutable commit should be recorded in run metadata.
- **Evidence:** User-provided Colab outputs from the model smoke test and revision lookup.

## D10 — Keep the study comparative, not a full ProSA replication

- **Decision:** Use a controlled comparative study (assignment Pathway B). The study compares prompts and two Qwen model sizes on fixed source abstracts. Implement an adapted pairwise difference score inspired by ProSA/PSS and compare it with TF-IDF, while explicitly documenting that neither is a full replication of ProSA's original benchmarks.
- **Rationale:** The task/domain, dataset, source-grounded rubric and model conditions differ from ProSA's original benchmark.
- **Status:** Metric calculation tests are included in the v1.3 notebook but still require an actual successful run in Colab.

## D11 — Pin dataset integrity

- **Dataset:** `study_sources_v1_1_verified.json`, version `v1.1`, 8 abstracts.
- **SHA-256:** `8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295`.
- **Decision:** Verify this hash in the modular notebook before inference and record it with the run.

## D12 — Do not treat model smoke tests as research findings

- **Decision:** Exclude all development-only source outputs, including the ProSA abstract and STEM intervention abstract, from main results.
- **Rationale:** They were used to debug environment, prompting and output-format behavior; the sample is not the prespecified eight-source main dataset.

## Historical next action at the v1.3 checkpoint (superseded on 10 November 2026)

This was the next action at the 29 October 2026 checkpoint. It was subsequently completed; the retained run output is results/baseline/phase3_baseline_validation_v1_3.json. It is kept here as historical decision-log context, not as the current next action.

## D13 — Operational baseline status after v1.3 JSON

- **Evidence:** `phase3_baseline_validation_v1_3.json` records successful GPU availability, dataset hash/schema checks, prompt assembly checks, a pinned 0.5B model revision, a non-empty one-sentence development output, and passing unit tests for the adapted pairwise score and TF-IDF calculation.
- **Assessment:** Mark the software pipeline as operationally validated for the development case. The generated conclusion omitted the source's recommendation for larger, fully powered trials; keep that as a source-fidelity limitation and do not repeatedly tune prompts to eliminate it.
- **Boundary:** The eight-source, 48-output main experiment has not been run; no main-study results are claimed.

## D14 — Freeze protocol v1.4 before main collection

- **Decision:** Use the one-sentence central-conclusion task with P0/P1/P2 and identical common constraints. Keep two Qwen2.5 size conditions at pinned revisions, seed 42, greedy decoding, max_new_tokens=100 and one generation per source/prompt/model.
- **Rationale:** Pilot failures of multi-field output formatting showed that asking for key-findings bullets added avoidable format failures unrelated to the main research question. The one-sentence outcome better matches the research question and is frozen before any main-data collection.
- **Status:** Frozen for the planned main run, subject to instructor-required changes being logged before collection.

## D15 — Bound TF-IDF numerical output

- **Evidence:** Unit test for identical strings returned `1.0000000000000007`, which is numerically 1 within floating-point tolerance.
- **Decision:** Clamp values exported in final result tables to [0,1] and use tolerance-based assertions. This is numerical hygiene and does not change the interpretation of cosine similarity.

## D16 — Main experiment executed under frozen v1.4 protocol

- **Date:** 10 November 2026.
- **Evidence:** results/raw/main_experiment_raw_outputs_v1_4.json and its CSV export; 48 records covering 8 sources × 3 prompt conditions × 2 pinned Qwen2.5 model sizes.
- **Protocol:** Greedy decoding, max_new_tokens=100, seed 42 recorded, one generation per source/prompt/model, exact dataset hash and model revisions recorded.
- **Decision:** Keep the raw JSON unmodified and separate all development/pilot outputs from the main run.
- **Status:** Main data collection completed. Integrity checks pass; scientific output assessments remain subject to human review.

## D17 — Treat output assessment as an AI-assisted first pass

- **Evidence:** results/analysis/annotations_ai_assisted.csv (48 output assessments) and results/analysis/pairwise_conclusion_relations.csv (48 pair comparisons).
- **Decision:** Report these as AI-assisted source-grounded assessments, not independent human ground truth.
- **Required human action:** Review all 48 output annotations and 48 pair labels against the original abstracts. Keep human corrections in separately versioned files and do not edit raw outputs.
- **Status:** Human review remains open as of 14 November 2026.
