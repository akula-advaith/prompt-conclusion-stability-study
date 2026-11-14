# Human review before submission

This package contains an AI-assisted first-pass annotation and a manuscript draft. Complete these checks before treating the results as final:

1. Review all 48 output annotations against the exact abstract. Confirm the three quality scores and their rationales.
2. Review all 48 pairwise prompt comparisons. Confirm `stable`, `emphasis_shift`, `substantive_shift`, or `contradiction` labels against the source evidence.
3. Pay particular attention to unsupported additions, omitted qualifications, and outputs flagged for two-sentence format violations. Do not edit the raw outputs; record any corrected human labels in a separate file.
4. Confirm the author name and affiliation on the manuscript title page.
5. Check each reference and DOI against the publisher record and confirm the citation is used for the claim it supports.
6. Confirm that the distinction between the study-specific adapted PSS-style score and the original ProSA benchmark is understood and retained.
7. Keep conclusions descriptive. The eight abstracts are a purposive sample, both models are from one family, and only one greedy generation was collected per condition. Do not claim statistical significance or generalize beyond this design.
8. Verify that AI assistance and AI-assisted annotations are disclosed according to the institute's current rules.

## Important provenance note
The 48 generations are outputs from the recorded Qwen model revisions and settings. Quality ratings and pairwise relation labels were produced with AI assistance and have not been independently human-validated. The manuscript must not describe those labels as human ground truth.