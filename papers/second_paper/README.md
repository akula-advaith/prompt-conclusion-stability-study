# Second research paper package — Protocol v1.4

This package contains a LaTeX draft of the second paper, the verified BibTeX source list, three result figures, and the experiment evidence files used to draft the results.

## Files
- `second_research_paper.tex`: ACM-style manuscript draft.
- `second_paper_references.bib`: BibTeX entries for the eight abstracts and methodological/background sources.
- `figures/`: figures generated from the experiment analysis.
- `results/`: raw experiment JSON, AI-assisted annotations, pairwise relation labels, and summary CSV/JSON files.

## Compile
Run `latexmk -pdf second_research_paper.tex` in a TeX Live environment with `acmart` installed.

## Important research-integrity note
The 48 generations are genuine outputs from the uploaded experiment JSON. The 48 output-level ratings and 48 pairwise relation labels were produced through AI-assisted source-grounded assessment, not independent human annotation. They require human review before final submission. No statistical-significance claims are made. The adapted PSS-style value is a study-specific descriptive adaptation inspired by ProSA/PSS, not a reproduction of the official benchmark.

## Run configuration recorded in the raw JSON
- Dataset: `study_sources_v1_1_verified.json`, v1.1, SHA-256 `8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295`
- 8 abstracts × 3 prompt conditions × 2 models = 48 outputs
- Greedy decoding, `max_new_tokens=100`, seed 42 recorded
- Qwen2.5-0.5B-Instruct and Qwen2.5-1.5B-Instruct, pinned revisions in manuscript and raw JSON
- Colab Tesla T4; Python 3.13.16; PyTorch 2.14.1+cu130; Transformers 5.22.1
