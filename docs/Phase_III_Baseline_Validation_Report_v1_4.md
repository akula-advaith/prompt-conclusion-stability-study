# Phase III — Baseline Validation Report v1.4

**Status: Operational baseline validation passed with a documented source-fidelity limitation.**  
**Scope:** Phase III Prompts 08–11; development-only checks. The main experiment has not been run.

## 1. Environment verification (Prompt 08)

The v1.3 Colab execution recorded Python `3.13.16`; PyTorch `2.11.0+cu130`; Transformers `5.20.2`; Accelerate `1.15.0`; Hugging Face Hub `1.33.0`; CUDA available; Tesla T4 GPU. Core imports and model generation succeeded.

## 2. Dataset and prompt builder checks (Prompt 09)

The v1.3 notebook verified:

- Dataset version `v1.1`, with SHA-256 `8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295` matching the expected hash.
- Eight source records, all required fields present, unique IDs and unique abstracts.
- Three prompt conditions assembled successfully; source text was preserved and common instructions were identical across conditions.
- The development run records a pinned baseline model: `Qwen/Qwen2.5-0.5B-Instruct`, SHA `7ae557604adf67be50417f59c2c2f167def9a775`.

## 3. Baseline inference result and source-fidelity review (Prompt 10)

Development source: “An AI-based intervention for improving undergraduate STEM learning,” PLOS ONE, DOI `10.1371/journal.pone.0288844`. This development-only source is excluded from the eight-item main dataset.

The model returned a non-empty, non-truncated one-sentence conclusion and passed the notebook's one-sentence format heuristic:

> The central conclusion of this scientific abstract is that just-in-time interventions have shown a statistically significant increase in the proportion of students achieving a passing grade in an undergraduate STEM course, indicating their potential and promise as a tool for enhancing STEM learning.

**Content assessment:** Mostly supported but incomplete. It reflects the reported statistically significant increase and the study's potential promise, and it does not invent a percentage. However, it omits a material qualification in the abstract: the authors call for larger, fully powered randomized controlled trials. Record this as a source-fidelity omission in the development evidence. It is not a main-study result.

This omission does not mean the inference code failed. It demonstrates why preservation of source qualifications is part of the outcome being evaluated. Do not keep changing prompts until development output looks ideal; retain this case as a documented failure and freeze the prompt conditions before main collection.

## 4. Metric implementation checks

Unit tests in the notebook passed:

- Pairwise mean absolute score difference: known value `0.26666666666666666` for scores `[0.8, 0.6, 1.0]`.
- Equal-score case returns `0.0`.
- Endpoint case `[0.0, 1.0]` returns `1.0`.
- Too-few-score case raises `ValueError`.
- TF-IDF identical texts return approximately `1.0`; unrelated text has lower similarity.

The identical-text TF-IDF test emitted `1.0000000000000007` due to floating-point rounding. Clamp reported cosine values to `[0,1]` or use tolerance in assertions. The pairwise score is a study-specific adaptation inspired by ProSA/PSS; these unit tests do not claim reproduction of ProSA's full benchmark or official results.

## 5. Actual debugging evidence (Prompt 11)

1. A package-install cell reported dependency conflicts involving `huggingface_hub`, Gradio and Diffusers. Core imports and inference later succeeded; unrelated dependencies were not changed without an actual failure.
2. The arXiv API request timed out during a pilot. A supplied abstract was used instead; source text and link were recorded.
3. Prompts requesting a central conclusion plus two key findings produced incomplete outputs. A JSON retry returned Markdown fences and placeholder findings. The output task was revised to one central-conclusion sentence before main collection.
4. The 0.5B development output omitted the recommendation for larger, fully powered trials. This was recorded as a source-fidelity limitation rather than repeatedly tuning against the development source.
5. An earlier unpinned 1.5B record had a null model revision; the resolved SHA is `989aa7980e4cf806f80c7fef2b1adb7bc71aa306`. Future runs must record the SHA.
6. Library versions changed across exploratory sessions. Do not combine outputs from different environments as though they were one controlled run.

## 6. Gate interpretation

- **Prompt 08 — Environment:** passed for the recorded Colab run.
- **Prompt 09 — Baseline coding:** passed for tested modules: data validation, prompt assembly, pinned model inference, metadata capture and metric unit tests.
- **Prompt 10 — Baseline validation:** operational pass with a source-fidelity omission recorded. The implementation runs under a pinned revision; the response is imperfect, and this is an observable model-quality limitation.
- **Prompt 11 — Debugging:** genuine issues and corrections documented. Preserve failed outputs and changes in the AI assistance log.

## 7. Remaining boundary

This report completes the development baseline-validation checkpoint for the assigned Phase III work. It does **not** claim that the 48-output main experiment has run, does not contain main-study findings, and does not complete later paper-writing or reproduction gates. If the instructor specifically requires a multi-condition integration test for Prompt 10, run the frozen builder across all three prompt IDs on the development-only source and preserve all outputs before the main run.