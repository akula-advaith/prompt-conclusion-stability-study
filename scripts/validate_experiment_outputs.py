#!/usr/bin/env python3
"""Validate the frozen dataset and the recorded v1.4 main-run output file."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

EXPECTED_HASH = "8c2bc1018ee04dc216c55c389ba296c1ad8138566063b1add827ed06d8393295"
EXPECTED_SOURCES = {f"S{i:02d}" for i in range(1, 9)}
EXPECTED_PROMPTS = {"P0_reference", "P1_paraphrase", "P2_paraphrase"}
EXPECTED_MODELS = {
    "Qwen/Qwen2.5-0.5B-Instruct",
    "Qwen/Qwen2.5-1.5B-Instruct",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, default=Path("data/study_sources_v1_1_verified.json"))
    ap.add_argument("--outputs", type=Path, default=Path("results/raw/main_experiment_raw_outputs_v1_4.json"))
    args = ap.parse_args()
    errors = []
    if not args.data.is_file(): errors.append(f"Dataset not found: {args.data}")
    if not args.outputs.is_file(): errors.append(f"Raw output JSON not found: {args.outputs}")
    if errors:
        print("VALIDATION FAILED")
        print("\n".join(f"- {e}" for e in errors))
        return 1

    actual_hash = sha256(args.data)
    print(f"Dataset SHA-256: {actual_hash}")
    if actual_hash != EXPECTED_HASH:
        errors.append("Dataset SHA-256 does not match frozen v1.1 hash.")

    dataset = json.loads(args.data.read_text(encoding="utf-8"))
    dataset_records = dataset.get("sources", dataset.get("records", [])) if isinstance(dataset, dict) else dataset
    if not isinstance(dataset_records, list):
        errors.append("Could not locate a list of dataset source records.")
        dataset_records = []
    dataset_ids = {r.get("source_id", r.get("id")) for r in dataset_records if isinstance(r, dict)}
    print(f"Dataset records: {len(dataset_records)}; unique source IDs: {len(dataset_ids)}")

    raw = json.loads(args.outputs.read_text(encoding="utf-8"))
    records = raw.get("records", []) if isinstance(raw, dict) else []
    print(f"Raw output records: {len(records)} (expected 48)")
    if len(records) != 48: errors.append(f"Expected 48 records, found {len(records)}.")

    combos = []
    empty = []
    missing_revision = []
    for i, r in enumerate(records):
        combo = (r.get("source_id"), r.get("prompt_id"), r.get("model_id"))
        combos.append(combo)
        if not str(r.get("raw_output", "")).strip(): empty.append(i)
        if not r.get("model_revision_sha"): missing_revision.append(i)
    unique_combos = set(combos)
    print(f"Unique source × prompt × model combinations: {len(unique_combos)}")
    if len(unique_combos) != 48: errors.append("Output combinations contain duplicates or missing combinations.")
    if empty: errors.append(f"Empty outputs at record indexes: {empty}")
    if missing_revision: errors.append(f"Missing model revision SHA at record indexes: {missing_revision}")

    used_sources = {c[0] for c in combos}
    used_prompts = {c[1] for c in combos}
    used_models = {c[2] for c in combos}
    if used_sources != EXPECTED_SOURCES: errors.append(f"Unexpected source IDs: {sorted(used_sources)}")
    if used_prompts != EXPECTED_PROMPTS: errors.append(f"Unexpected prompt IDs: {sorted(used_prompts)}")
    if used_models != EXPECTED_MODELS: errors.append(f"Unexpected models: {sorted(used_models)}")
    if dataset_ids and used_sources != dataset_ids: errors.append("Source IDs in raw outputs do not match the dataset.")

    print(f"Empty outputs: {len(empty)}")
    print(f"Missing model revisions: {len(missing_revision)}")
    if errors:
        print("\nVALIDATION FAILED")
        for e in errors: print(f"- {e}")
        return 1
    print("\nVALIDATION PASSED: file integrity and expected experiment coverage checks passed.")
    print("Note: this script validates file/schema coverage; it does not judge scientific correctness of model outputs.")
    return 0

if __name__ == "__main__":
    sys.exit(main())