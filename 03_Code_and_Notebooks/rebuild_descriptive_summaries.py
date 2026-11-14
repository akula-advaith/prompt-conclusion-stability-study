#!/usr/bin/env python3
"""Rebuild descriptive summary CSVs from the supplied AI-assisted annotations.

This script aggregates existing annotations. It does not create or validate the
scientific judgments, pairwise labels, or TF-IDF similarity values.
"""
from __future__ import annotations
import argparse, csv
from collections import defaultdict, Counter
from pathlib import Path

def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(row, key):
    try: return float(row[key])
    except (KeyError, TypeError, ValueError): raise ValueError(f"Invalid numeric value in column {key!r}: {row.get(key)!r}")

def write_csv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--annotations", type=Path, default=Path("results/analysis/annotations_ai_assisted.csv"))
    ap.add_argument("--pairs", type=Path, default=Path("results/analysis/pairwise_conclusion_relations.csv"))
    ap.add_argument("--outdir", type=Path, default=Path("results/rebuilt"))
    args=ap.parse_args()
    annotations=read_csv(args.annotations); pairs=read_csv(args.pairs)
    if not annotations or not pairs: raise SystemExit("Input annotation/pairwise CSV is empty.")
    grouped=defaultdict(list)
    for r in annotations: grouped[(r["model_size"],r["prompt_id"])].append(r)
    out=[]
    for (model,prompt), rows in sorted(grouped.items()):
        out.append({
            "model_size":model,"prompt_id":prompt,"n":len(rows),
            "mean_total_quality":f"{sum(num(r,'overall_quality_score') for r in rows)/len(rows):.3f}",
            "mean_conclusion_fidelity":f"{sum(num(r,'central_conclusion_fidelity') for r in rows)/len(rows):.3f}",
            "mean_evidential_support":f"{sum(num(r,'evidential_support') for r in rows)/len(rows):.3f}",
            "mean_scope_fidelity":f"{sum(num(r,'scope_qualification_fidelity') for r in rows)/len(rows):.3f}",
            "one_sentence_pass_rate":f"{sum(str(r.get('format_compliant_one_sentence','')).lower()=='true' for r in rows)/len(rows):.3f}"
        })
    write_csv(args.outdir/"quality_by_model_and_prompt_rebuilt.csv",list(out[0]),out)

    rel=defaultdict(Counter)
    for r in pairs: rel[r["model_size"]][r["relation"]]+=1
    rows=[]
    for model, counts in sorted(rel.items()):
        rows.append({"model_size":model,**{k:counts.get(k,0) for k in ["stable","emphasis_shift","substantive_shift","contradiction"]}})
    write_csv(args.outdir/"pairwise_relation_counts_by_model_rebuilt.csv",list(rows[0]),rows)
    print(f"Read {len(annotations)} annotations and {len(pairs)} pairwise labels.")
    print(f"Wrote rebuilt descriptive summaries to: {args.outdir}")
    print("Reminder: these are aggregates of AI-assisted labels, not independent human assessments.")

if __name__=="__main__": main()