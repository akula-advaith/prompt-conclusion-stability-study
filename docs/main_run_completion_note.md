# Main experiment completion note — v1.4

The main experiment was executed after the earlier Phase II/III planning and validation snapshots had been written.

- Main-run date recorded in project artifacts: 10 November 2026.
- Dataset: 8 scientific abstracts, dataset v1.1.
- Prompt conditions: P0 reference, P1 paraphrase, P2 paraphrase.
- Models: Qwen2.5-0.5B-Instruct and Qwen2.5-1.5B-Instruct.
- Generation design: 8 × 3 × 2 = 48 outputs; greedy decoding; `max_new_tokens=100`; seed 42 recorded.
- Raw results: `results/raw/main_experiment_raw_outputs_v1_4.json` and its CSV export.
- First-pass analysis: `results/analysis/`.

The first-pass relation counts are 25 stable, 15 emphasis shifts, 8 substantive shifts and 0 contradictions across 48 prompt pairs. Mean output-quality scores were 0.618 for the 0.5B model and 0.757 for the 1.5B model. These are descriptive outputs of AI-assisted annotations, not independent human ground truth. The eight-abstract purposive sample, one generation per condition and single model family limit generalization. Review annotations and pair labels before presenting final findings.

Historical Phase II/III snapshots that state the main experiment had not yet run remain valid records of the earlier checkpoint. They should not be mistaken for the current project status.
