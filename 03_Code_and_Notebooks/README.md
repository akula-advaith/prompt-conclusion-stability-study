# 03 — Code and Notebooks

This folder contains the two Colab notebooks and the utility scripts used for the prompt-conclusion stability experiment.

## Files

- 01_phase_iii_baseline_validation.ipynb — development-stage baseline/environment validation notebook. Its baseline result is documented in the Phase III report under 05_Research_Documentation.
- 02_main_experiment_v1_4.ipynb — frozen v1.4 notebook used for the main experiment (8 sources × 3 prompt conditions × 2 models = 48 generations).
- validate_experiment_outputs.py — checks the frozen dataset hash and the completeness/metadata of the recorded 48-output JSON. It does not judge scientific correctness.
- rebuild_descriptive_summaries.py — rebuilds descriptive CSV aggregates from the supplied AI-assisted annotation and pairwise-label CSVs. It does not recreate the annotations or TF-IDF values.
- requirements.txt — Python dependencies recorded for the main-run workflow. PyTorch/CUDA may need to be installed separately to match the Colab GPU runtime.

## Validate the archived experiment files

Run from the project root:

\`\`\`bash
python 03_Code_and_Notebooks/validate_experiment_outputs.py \\
  --data 04_Dataset_and_Results/study_sources_v1_1_verified.json \\
  --outputs 04_Dataset_and_Results/main_experiment_raw_outputs_v1_4.json
\`\`\`

A successful result confirms file/hash integrity and expected source × prompt × model coverage. It is not a scientific review of the generated conclusions.

## Rebuild descriptive summary CSVs

\`\`\`bash
python 03_Code_and_Notebooks/rebuild_descriptive_summaries.py \\
  --annotations 04_Dataset_and_Results/annotations_ai_assisted.csv \\
  --pairs 04_Dataset_and_Results/pairwise_conclusion_relations.csv \\
  --outdir 04_Dataset_and_Results/rebuilt
\`\`\`

The rebuilt directory is created when this command is run. Preserve the original CSVs and raw JSON unchanged.

## Running the notebooks

Open a notebook in Google Colab, select a compatible GPU runtime where required, and run cells in order. The recorded main run used a Tesla T4, Python 3.13.16, PyTorch 2.14.1+cu130 and Transformers 5.22.1. Runtime packages and GPU availability can change, so verify the live environment before reproducing a run. Do not overwrite the archived raw outputs; preserve any new run separately and record its settings.

**Research-integrity note:** annotations_ai_assisted.csv and pairwise_conclusion_relations.csv contain AI-assisted first-pass assessments. They are not independent human ground truth and should be checked against the source abstracts before final submission.
