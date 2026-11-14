#!/usr/bin/env python3
"""Regenerate all three second-paper figures from the checked-in v1.4 summary data."""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "papers" / "second_paper" / "figure_data_v1_4.json"
OUT = ROOT / "papers" / "second_paper" / "figures"

def add_value_labels(ax, bars, fmt="{:.3f}"):
    for bar in bars:
        value = bar.get_height()
        ax.annotate(
            fmt.format(value),
            (bar.get_x() + bar.get_width() / 2, value),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=8,
        )

def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)

    # Figure 1: mean source-grounded quality by model and prompt.
    prompts = ["P0_reference", "P1_paraphrase", "P2_paraphrase"]
    labels = ["P0 reference", "P1 paraphrase", "P2 paraphrase"]
    models = ["0.5B", "1.5B"]
    x = np.arange(len(prompts))
    width = 0.34
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    for i, model in enumerate(models):
        values = [data["quality_by_model_and_prompt"][model][p] for p in prompts]
        bars = ax.bar(x + (i - 0.5) * width, values, width, label=f"Qwen2.5-{model}")
        add_value_labels(ax, bars)
    ax.set_title("Mean source-grounded quality by prompt and model")
    ax.set_ylabel("Mean quality score")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 1.0)
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(OUT / "quality_by_prompt_model.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # Figure 2: pairwise relation counts by model.
    relations = ["stable", "emphasis_shift", "substantive_shift", "contradiction"]
    relation_labels = ["Stable", "Emphasis shift", "Substantive shift", "Contradiction"]
    x = np.arange(len(relations))
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    for i, model in enumerate(models):
        values = [data["pairwise_relations_by_model"][model][r] for r in relations]
        bars = ax.bar(x + (i - 0.5) * width, values, width, label=f"Qwen2.5-{model}")
        for bar in bars:
            ax.annotate(
                f"{int(bar.get_height())}",
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 4),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
            )
    ax.set_title("Pairwise conclusion relation counts")
    ax.set_ylabel("Number of prompt-pair comparisons")
    ax.set_xticks(x, relation_labels, rotation=12, ha="right")
    ax.set_ylim(0, 18)
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(OUT / "pairwise_relation_counts.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # Figure 3: mean lexical overlap by source-grounded pair relation.
    rels = ["stable", "emphasis_shift", "substantive_shift"]
    rel_labels = ["Stable", "Emphasis shift", "Substantive shift"]
    means = [data["tfidf_by_relation"][r]["mean"] for r in rels]
    counts = [data["tfidf_by_relation"][r]["n"] for r in rels]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    bars = ax.bar(rel_labels, means)
    for bar, count in zip(bars, counts):
        ax.annotate(
            f"{bar.get_height():.3f} (n={count})",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax.set_title("TF-IDF similarity by conclusion relation")
    ax.set_ylabel("Mean cosine similarity")
    ax.set_ylim(0, 0.65)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    fig.text(
        0.5,
        0.01,
        "Lexical overlap only; TF-IDF similarity is not a semantic correctness measure.",
        ha="center",
        fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(OUT / "tfidf_by_conclusion_relation.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    print(f"Regenerated all three figures in {OUT}")

if __name__ == "__main__":
    main()
