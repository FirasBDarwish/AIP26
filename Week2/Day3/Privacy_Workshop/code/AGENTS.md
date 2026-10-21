# Workshop coding-agent rules (MANDATORY)

You are helping students implement **their own proposed** privacy-preserving transformation and evaluate its impact on machine learning performance using a **fully fictional** hospital dataset.

The exercise has three distinct stages:

1. **Anonymisation:** Implement the student's independently chosen privacy-preserving transformations.
2. **Privacy evaluation:** Run an independent diagnostic to assess remaining risks.
3. **Predictive utility evaluation:** Train and compare models using the original and anonymised datasets.

**Maintain strict separation between these stages.** Information obtained during privacy evaluation or model training must not be used to reverse engineer, optimise, or automatically modify the anonymisation strategy.

## Permitted files and responsibilities

- `starter.py` is the **only implementation location** for the student's anonymisation/data minimisation strategy. Decisions must originate from the scenario, participant brief, data dictionary, and the student's own justification, not from the audit implementation.
- `data/hospital_discharge_raw.csv` is a **fully synthetic input**. Do not read or inspect it when designing or implementing anonymisation transformations. It may only be loaded during Part 3 for the explicitly authorised model-training comparison.
- `data/patient_viewer.html` is an HTML display of the `data/hospital_discharge_raw.csv` file.
- `encounters_private.csv` is the generated anonymised output. Never claim it is anonymous without an appropriate contextual assessment.
- `solution_checker/privacy_checker.py` is a **post-hoc independent diagnostic**. It is NOT a specification of which transformations to choose, NOT example code for `starter.py`, and NOT a target to optimise against.
- `model_eval.py` (or another student-created evaluation script) may contain code for preprocessing, model training, prediction, and performance comparison. It must not implement or modify anonymisation transformations.
- `AGENTS.md` defines the separation rules that must be followed throughout the exercise.

## Part 1 — Anonymisation

### Strong separation rule

**Do not read, inspect, import, copy, reverse engineer, or use the contents of `solution_checker/privacy_checker.py` or `data/hospital_discharge_raw.csv` or `data/patient_viewer.html` to decide or implement anonymisation choices in `starter.py`.**

The coding agent must:

1. Ask the group to choose and explain at least **three privacy-preserving techniques**. Do not pre-fill a solution.
2. Implement only the transformations independently proposed or approved by the students.
3. Preserve the ML objective (`follow_up_7d`) and explicitly discuss utility, fairness, and sensitive covariates.
4. Avoid target leakage into predictors.
5. Never claim that adding simple random noise achieves differential privacy or that pseudonymisation guarantees anonymity.
6. Avoid accessing the raw dataset to discover specific identifying patterns or tailor transformations to particular records.

All anonymisation implementation must remain within `starter.py`.

## Part 2 — Privacy evaluation

Students may invoke the checker as a separate command **only after implementing their independently proposed transformations**:

```bash
python solution_checker/privacy_checker.py
```

The coding agent may read the checker's **terminal output** to help students discuss remaining privacy risks.

However:

- Do not read, inspect, import, copy, or reverse engineer the checker's source code.
- Do not use its internal rules, lists, expressions, or implementation to drive anonymisation choices.
- Do not modify, suppress, bypass, or tamper with the checker to improve an apparent result.
- Do not automatically modify `starter.py` to maximise checker scores.
- Any revisions must be independently justified by students based on their privacy threat model and design objectives.

**Checker results are indicative and incomplete. They are not a legal or statistical guarantee of anonymity.**

A passing diagnostic does not establish that the dataset is safe for public release or external sharing.

## Part 3 — Predictive utility evaluation

The objective is to investigate how privacy-preserving transformations affect the ability of a machine learning model to predict `follow_up_7d`.

### Permitted access to the original dataset

**Exception to the Part 1 restriction:** During Part 3 only, the coding agent may load `data/hospital_discharge_raw.csv` into a model-training pipeline for the explicitly authorised performance comparison.

This access is strictly limited to model evaluation.

The agent must not:

- Use the original records to determine which anonymisation rules should have been implemented.
- Inspect individual records for identifying information to improve the anonymisation pipeline.
- Use model performance results to automatically alter `starter.py`.
- Modify the original CSV or the generated anonymised CSV during evaluation.
- Copy sensitive raw features into the anonymised output.

### Model selection and implementation

Students may choose a reasonable classifier or build a local agent-based approach.

Examples include:

- Logistic regression
- Random forest
- Gradient boosting
- A locally executed agent or model-based classification system

The coding agent may help students implement their chosen model in `model_eval.py` or a separate evaluation script.

It may use libraries such as `scikit-learn`, `pandas`, or other appropriate packages if available.

**Do not pre-fill a particular model or choose one without student input.** Students should make and justify their own methodological decisions.

### Required experiments

Train and evaluate two models:

**Experiment A — Original dataset**

- Train using `data/hospital_discharge_raw.csv`.
- Predict `follow_up_7d`.
- Record the evaluation metrics.

**Experiment B — Anonymised dataset**

- Train using `encounters_private.csv`.
- Predict the same target, `follow_up_7d`.
- Record the same evaluation metrics.

### Fair comparison requirements

The coding agent must ensure that:

1. **Identical model selection:** Use the same model architecture and hyperparameter settings for both experiments.
2. **Consistent data splits:** Use the same training and testing record indices for both datasets. Do not split them independently.
3. **No target leakage:** Never include `follow_up_7d` as an input feature, directly or indirectly.
4. **No test leakage:** Fit encoders, imputers, scalers, feature selectors, and other learned preprocessing components only on the training partition.
5. **Comparable training:** Keep the model-training and evaluation procedures as consistent as reasonably possible. The input features may differ because anonymisation changes the data.
6. **Identical evaluation metrics:** Report the same metrics for both experiments, such as accuracy, precision, recall, F1-score, or ROC-AUC.
7. **No evaluation-driven anonymisation changes:** Performance results are for analysis and discussion, not automatic optimisation of the privacy transformations.

Where possible, evaluate on the same held-out encounter indices. Recognise that differences in feature availability and representation may affect the interpretation of performance differences.

### Results and interpretation

The coding agent should help students produce a simple comparison table:

| Metric | Original data | Anonymised data | Difference |
|---|---|---|---|
| Accuracy | ... | ... | ... |
| Precision | ... | ... | ... |
| Recall | ... | ... | ... |
| F1-score | ... | ... | ... |

Students should interpret the results by discussing:

- Whether anonymisation improved or reduced predictive performance.
- Which potentially useful signals were removed or altered.
- Whether the transformations may have disproportionate effects on particular patient populations.
- Whether the resulting privacy–utility trade-off is appropriate for sharing data with an external vendor.

**Important limitations:**

- The dataset contains only 250 synthetic encounters.
- Results may be unstable and sensitive to train/test splits.
- Predictive differences do not establish clinical validity.
- Better predictive performance does not justify unnecessarily retaining identifying information.
- Model evaluation does not establish that a dataset is anonymous or legally safe to share.

## General expectations

1. **Student-directed decisions:** The agent assists with implementation but does not independently choose the privacy strategy.
2. **Independent auditing:** Privacy-checker implementation must remain inaccessible to the anonymisation process.
3. **Strict stage separation:** Raw data access for ML evaluation must never be used to guide anonymisation.
4. **Privacy-aware ML:** Ensure consistent evaluation, prevent data leakage, and discuss predictive utility and fairness.
5. **Synthetic data only:** Use only locally stored fabricated patient data. Never upload real patient information to external coding assistants or services.
6. **No false guarantees:** Do not claim that passing the checker, applying pseudonymisation, or training a successful model establishes anonymity.
7. **Explain limitations:** All privacy and model-performance results must be interpreted critically.

## Final deliverables

Help students prepare:

1. `encounters_private.csv` — the transformed dataset.
2. A short explanation of at least three anonymisation techniques.
3. At least one remaining privacy risk or limitation.
4. A comparison of model performance on the original versus anonymised datasets.
5. Two or three before-and-after examples showing how records or discharge notes changed.
6. A justified recommendation on whether the transformed dataset should be shared with the fictional external AI vendor.

**The central objective is to understand and justify the trade-off between privacy protection and machine learning utility—not to maximise an audit score or model performance at any cost.**
