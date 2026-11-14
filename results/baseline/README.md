# Phase III baseline validation evidence

These files preserve the actual development-stage Colab outputs used to validate the software pipeline before the main v1.4 data collection.

**Important separation:** every file in this folder is development/pilot evidence and is excluded from the eight-source, 48-generation main dataset. Do not mix pilot outputs into main results.

## Files

- phase3_baseline_validation_v1_3.json — final Phase III development checkpoint: runtime, GPU, dataset hash/schema checks, prompt assembly, pinned 0.5B model output, and unit-test values.
- phase3_baseline_validation_output.json — original multi-field prompt attempt; only the conclusion field was returned.
- phase3_baseline_validation_retry.json — structured JSON retry; Markdown fences/placeholders made parsing fail.
- phase3_baseline_validation_retry2.json — second three-line retry; schema still failed and output included an unsupported control-group comparison.
- phase3_single_conclusion_baseline.json — three single-conclusion prompts using the 0.5B development model.
- phase3_pinned_baseline_validation.json — three prompt conditions with the revision-pinned 1.5B development comparator; P2 returned two sentences.
- phase3_comparator_15b_baseline_unpinned.json — earlier comparator smoke test with a null model revision; retained as a reproducibility failure, superseded by the pinned test.

## Interpretation

The final v1.3 checkpoint confirms an operational environment, dataset/hash validation, prompt assembly and metric unit tests. It is not proof that every scientific output is correct. The baseline report documents the main source-fidelity limitation: the development conclusion omitted the source's call for larger, fully powered trials. These development runs are not main-study evidence.

Run outputs are retained as captured. Do not edit them; add any later interpretation to a separate versioned note.
