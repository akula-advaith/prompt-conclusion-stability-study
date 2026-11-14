# Main Experiment Analysis — Protocol v1.4

**Research topic:** Prompt sensitivity and stability of LLM-generated scientific conclusions
**Input:** `main_experiment_raw_outputs_v1_4.json` (uploaded raw outputs; retained unchanged in this package)
**Assessment status:** AI-assisted, source-grounded annotations; not independent human ground truth.

## 1. Run integrity and completion

| Check | Observed result |
|---|---:|
| Protocol version | 1.4 |
| Dataset version | v1.1 |
| Dataset SHA-256 matches frozen v1.1 value | True |
| Raw output records | 48 / 48 |
| Unique source × prompt × model combinations | 48 / 48 |
| Duplicate combinations | 0 |
| Empty outputs | 0 |
| Possible truncations | 0 |
| One-sentence format pass (heuristic) | 45 / 48 (93.8%) |
| Runtime | Python 3.13.16; PyTorch 2.14.1+cu130; Transformers 5.22.1; Tesla T4 |

Both model conditions used the expected pinned revisions:

- Qwen2.5-0.5B-Instruct: `7ae557604adf67be50417f59c2c2f167def9a775`
- Qwen2.5-1.5B-Instruct: `989aa7980e4cf806f80c7fef2b1adb7bc71aa306`

Generation used greedy decoding (`do_sample=false`), a 100-token maximum and seed 42 set before each generation. The recorded raw run started at 2026-11-10 12:42:30 UTC and finished/checkpointed at 12:44:42 UTC.

**Format exceptions:** three outputs contained two sentences despite the one-sentence instruction: S03 / 0.5B / P0; S02 / 1.5B / P0; and S02 / 1.5B / P2. They are retained unchanged and flagged in `annotations_ai_assisted.csv`.

## 2. Evaluation method

Each of the 48 outputs was assessed against the abstract supplied in the same record. Three dimensions were rated on the protocol's 0, 0.5, 1 scale:

1. Central-conclusion fidelity.
2. Evidential support and avoidance of unsupported assertions.
3. Preservation of scope and qualifications.

The overall output-quality score is the arithmetic mean of these three dimensions. The 24 source/model groups each have three unordered prompt pairs, giving 48 pairwise comparisons. Each pair was assigned one of the frozen labels: `stable`, `emphasis_shift`, `substantive_shift`, or `contradiction`.

The adapted PSS-style value is the mean absolute difference between the three output-quality scores within each source/model group. It is a study-specific descriptive adaptation inspired by ProSA/PSS, not a replication of the original benchmark. TF-IDF cosine uses lowercase word unigrams and bigrams and is interpreted only as lexical overlap.

All ratings and pair labels in this report are AI-assisted judgments by the assistant. They are source-grounded and accompanied by rationales, but they are not independent human annotations. Treat the numbers as an initial annotation pass pending human review.

## 3. Main descriptive results

### 3.1 Source-grounded output quality

| Model | Mean quality (0–1) | Median | Outputs scoring ≥0.8 |
|---|---:|---:|---:|
| Qwen2.5-0.5B | 0.618 | 0.667 | 33.3% |
| Qwen2.5-1.5B | 0.757 | 0.833 | 62.5% |

The 1.5B condition had a higher mean source-grounded quality score than the 0.5B condition in this run (0.757 versus 0.618). This is a descriptive comparison between two model sizes from the same Qwen2.5 family; it does not establish a general model-size effect.

Across all 48 outputs, the average dimension scores were:

- Central-conclusion fidelity: **0.844**
- Evidential support: **0.719**
- Scope and qualification fidelity: **0.500**

The lowest average dimension was preservation of scope and qualifications. This is consistent with several outputs retaining the broad conclusion while omitting limitations, exceptions, or study-specific qualifiers.

### 3.2 Quality by prompt condition

| Model | P0 reference | P1 paraphrase | P2 paraphrase |
|---|---:|---:|---:|
| Qwen2.5-0.5B | 0.458 | 0.687 | 0.708 |
| Qwen2.5-1.5B | 0.729 | 0.792 | 0.750 |

In this sample, P0 had the lowest mean quality for both models. P1 and P2 scored higher on average. This is an observed pattern across eight abstracts, not evidence that one wording is universally superior; the sample is small and purposively selected.

![Output quality by prompt and model](quality_by_prompt_model.png)

### 3.3 Pairwise conclusion relations

| Model | Stable | Emphasis shift | Substantive shift | Contradiction |
|---|---:|---:|---:|---:|
| Qwen2.5-0.5B | 10 | 6 | 8 | 0 |
| Qwen2.5-1.5B | 15 | 9 | 0 | 0 |

Across all 48 pairs: **25 stable (52.1%), 15 emphasis shifts (31.2%), 8 substantive shifts (16.7%), and 0 contradictions**.

The eight substantive shifts occurred in the 0.5B condition in this annotation pass. The 1.5B outputs were classified as stable or emphasis shifts only. No explicit contradiction was identified. This does not imply all outputs were fully faithful: some stable groups contained the same unsupported claim across prompts.

![Pairwise conclusion relation counts](pairwise_relation_counts.png)

Pair labels by prompt comparison:

| Prompt comparison | Stable | Emphasis shift | Substantive shift |
|---|---:|---:|---:|
| P0 vs P1 | 7 | 6 | 3 |
| P0 vs P2 | 7 | 5 | 4 |
| P1 vs P2 | 11 | 4 | 1 |

P1 versus P2 had 11 stable pairs and 1 substantive shift, while P0 versus P1 had 7 stable and 3 substantive shifts; P0 versus P2 had 7 stable and 4 substantive shifts. This pattern suggests the two paraphrases were more similar to each other in their substantive conclusions than either was to the reference wording in this dataset.

### 3.4 Adapted PSS-style score and lexical similarity

| Model | Mean adapted PSS-style score | Mean TF-IDF cosine |
|---|---:|---:|
| Qwen2.5-0.5B | 0.2083 | 0.4540 |
| Qwen2.5-1.5B | 0.0972 | 0.4400 |

The lower adapted PSS-style score for the 1.5B condition (0.0972 versus 0.2083) indicates less variation in the three rubric-based quality scores across prompt pairs in this sample. It is not a measure of truth or correctness.

Mean TF-IDF cosine similarity by pair label:

| Pair label | Pair count | Mean TF-IDF cosine | Mean absolute quality-score difference |
|---|---:|---:|---:|
| emphasis_shift | 15 | 0.406 | 0.189 |
| stable | 25 | 0.503 | 0.040 |
| substantive_shift | 8 | 0.350 | 0.437 |

Stable pairs had higher average lexical overlap than substantive-shift pairs, but the values are not a semantic ground truth. TF-IDF should remain a lexical comparator rather than being interpreted as an evaluator of conclusion correctness.

![TF-IDF similarity by pairwise conclusion relation](tfidf_by_conclusion_relation.png)

## 4. Qualitative failure cases

- **S02 / 0.5B / P0:** the output introduced extinction risk and named mammals/reptiles as especially vulnerable. The abstract instead reports projected reductions in species richness, with birds and plants most affected. This is a material source-fidelity error.
- **S03 / 0.5B / P0:** the output added Maharashtra and Gujarat as states with smaller gains, although the abstract's comparison is among Madhya Pradesh, Uttar Pradesh and Karnataka. This is an unsupported addition.
- **S05 / P0 for both models:** the output described handwashing before and after meals. The abstract distinguishes handwashing before eating from after defecation. This is a small wording error with a substantive measurement distinction.
- **S06 / 0.5B / P0:** the output characterized the intervention's outcomes as inconclusive overall. The abstract reports statistically significant differences for six of nineteen outcomes, with small standardized effects, while one particular stages-of-change conclusion remains inconclusive.
- **S04 / both models:** outputs associated the achievement gain with use of an online platform. The abstract says the platform facilitated the experiment; it does not clearly establish that the platform itself caused or was necessary for the peer-assessment effect.
- **S08 / 1.5B / P0:** the output says accuracy can be reduced without compromising generalization. The abstract reports cross-language generalization of the models, but does not directly establish this as a consequence of removing leaky features.

## 5. Interpretation for the research question

Within this controlled run, changing the opening task wording was associated with differences in the generated one-sentence conclusions. Most prompt pairs were judged stable or differed mainly in emphasis, but 8 of 48 pairs were judged to contain a substantive shift. The difference was concentrated in the 0.5B condition under the current source-grounded annotation.

The results also show why lexical similarity alone is insufficient: it measures overlap in words and phrases, while the substantive comparison depends on whether the same evidence-based conclusion, scope and qualifications are retained. Some outputs had high overlap but shared the same unsupported addition; conversely, wording differences can occur without changing the underlying conclusion.

## 6. Limitations and reporting cautions

1. The dataset contains only eight purposively selected abstracts and is not representative of scientific literature.
2. Abstract-only evidence can omit detail present in full papers.
3. The two models are different sizes within one family, not independent model families.
4. Only one greedy generation was run per source × prompt × model; stochastic run-to-run variability was not estimated.
5. The annotations and relation labels are AI-assisted, not independently validated human ground truth. A human review of the 48 output ratings and 48 pair labels is recommended before final submission.
6. The adapted PSS-style score is not the official ProSA benchmark or full replication.
7. These descriptive results do not support statistical-significance claims or broad causal generalization.

## 7. Files in this package

- `main_experiment_raw_outputs_v1_4.json`: original raw run preserved unchanged.
- `annotations_ai_assisted.csv`: output-level ratings, sentence-format flags and rationales.
- `pairwise_conclusion_relations.csv`: 48 pair classifications, adapted-score differences and TF-IDF similarities.
- `source_model_stability_metrics.csv`: source/model-level adapted PSS-style scores and relation counts.
- `quality_by_model_and_prompt.csv`: prompt-wise quality dimension summaries.
- `relation_similarity_summary.csv`: lexical similarity by pairwise relation.
- Three PNG figures for the paper/report.

**Suggested next step:** review the flagged AI-assisted annotations, then write the Results and Discussion sections from these verified descriptive summaries.