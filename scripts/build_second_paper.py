#!/usr/bin/env python3
"""Build the missing TF-IDF figure required by the second-paper LaTeX source."""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "analysis" / "relation_similarity_summary_v1_4.csv"
OUTPUT = ROOT / "papers" / "second_paper" / "figures" / "tfidf_by_conclusion_relation.png"

ORDER = ["stable", "emphasis_shift", "substantive_shift"]
LABELS = {
    "stable": "Stable",
    "emphasis_shift": "Emphasis shift",
    "substantive_shift": "Substantive shift",
}

def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8-sig") as stream:
        rows = {row["relation"]: row for row in csv.DictReader(stream)}

    missing = [name for name in ORDER if name not in rows]
    if missing:
        raise SystemExit(f"Missing expected relation rows in {SOURCE}: {missing}")

    means = [float(rows[name]["mean_tfidf_cosine"]) for name in ORDER]
    counts = [int(rows[name]["pair_count"]) for name in ORDER]
    labels = [LABELS[name] for name in ORDER]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    bars = ax.bar(labels, means)
    ax.set_title("TF-IDF similarity by conclusion relation")
    ax.set_ylabel("Mean cosine similarity")
    ax.set_ylim(0, 0.65)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    for bar, value, count in zip(bars, means, counts):
        ax.annotate(
            f"{value:.3f} (n={count})",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    fig.text(
        0.5,
        0.01,
        "Lexical overlap only; TF-IDF similarity is not a semantic correctness measure.",
        ha="center",
        fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(OUTPUT, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    main()
