# Student package — Medical Data Privacy Exercise

**Your job:** Prepare a privacy-preserving version of fictional hospital discharge data for an external AI vendor developing a prototype that predicts `follow_up_7d` (priority care-coordinator review within seven days).

Your goal is to balance **patient privacy** with the **predictive utility of the data**. This is not a medical decision tool.

You will also train a machine learning model on both the original and anonymised datasets to investigate how your privacy-preserving transformations affect predictive performance.


## Run

```bash
python starter.py # to anonmyise the data
python solution_checker/privacy_checker.py # to check the quality of anonymization/security
```

`starter.py` initially **copies raw rows unchanged**; this is deliberately unsafe. Modify `transform()` yourself. The audit is an independent diagnostic only: read `AGENTS.md` before using an AI coding assistant. Python 3 standard library only; no installation needed.

## Contents

- `data/hospital_discharge_raw.csv` — **one CSV**, 250 fully synthetic encounter records including free-text `discharge_note`.
- `starter.py` — editable implementation area, no built-in solution.
- `solution_checker/privacy_checker.py` — runnable post-transformation diagnostic; not an anonymisation recipe.
- `AGENTS.md` — coding-agent separation rules.
- `data_dictionary.md` — all 33 fields.

## Sections

### Part 1 — Anonymise the dataset

Examine the dataset and decide which fields to retain, remove, or transform.

Apply at least three privacy-preserving techniques of your choice, considering both structured attributes and sensitive information hidden within clinical notes.

Modify `starter.py` to produce encounters_private.csv.

### Part 2 — Evaluate privacy

Run the privacy checker:

```
python solution_checker/privacy_checker.py
```

Inspect its findings and manually examine several transformed records.

Consider what the checker might miss and whether your transformed dataset is appropriate to share externally.

### Part 3 — Evaluate predictive utility

Train a machine learning classifier of your choice to predict follow_up_7d.

Your task is to compare two experiments:

* Experiment A — Original data: Train your model using the original hospital discharge dataset.
* Experiment B — Anonymised data: Train the same model using your anonymised dataset.

You may use any reasonable classifier, such as logistic regression, random forest, gradient boosting, or a local agent if you want to try to set it up.

Important considerations:

* Use the same model type, evaluation records, and train/test split for both experiments.
* Keep the preprocessing and training procedure as consistent as possible.
* Evaluate both models using suitable classification metrics, such as accuracy, F1-score, precision, recall, or ROC-AUC.
* Do not use follow_up_7d as an input feature.
* Ensure that information from the test set does not leak into training. Fit learned preprocessing steps on training data only.

Think about: Does greater privacy necessarily mean worse predictive performance? Which transformations have the largest impact, and why?

Because the dataset contains only 250 fictional records, treat performance differences as illustrative rather than clinically meaningful.

## Discussion questions — Prepare for the 15-minute share-out
Be ready to present your transformed dataset and discuss the following questions:

1. What were your main anonymisation decisions?

Which information did you remove, retain, or transform, and why? Explain at least three techniques you implemented and how you balanced privacy against predictive utility.

2. What privacy risks or limitations remain?

Identify at least one way a patient could still potentially be identified, even after your transformations. Consider combinations of attributes, information hidden in clinical notes, and limitations of your anonymisation techniques or the privacy checker.

3. How did anonymisation affect predictive performance?

Compare the performance of your model trained on the original dataset versus the anonymised dataset.

* Which model performed better, and by how much?
* What potentially useful ML signals were lost or altered during anonymisation?
* Could removing certain attributes disproportionately affect predictions for particular patient groups?

4. How did your transformations change the data?

Present 2–3 examples of original versus transformed records or discharge notes. Highlight what sensitive information was removed or generalised, what clinically relevant information was preserved, and any remaining concerns.

5. Final decision

Would you approve sharing your transformed dataset with the external AI vendor? Under what conditions? Consider both the residual privacy risks and the predictive performance of your model.


## Data cautions
Patients, addresses, workplaces, dates, phone numbers, relationships and sensitive narrative details are fabricated; cities/neighbourhoods are fictional. Some patterns are intentionally repeated, and a real attacker could know external facts that this audit cannot know.

The fabricated labels have no clinical validity. Avoid training an actual clinical model from this toy dataset.

Never input real sensitive patient records into a public coding assistant without authorisation and suitable controls.