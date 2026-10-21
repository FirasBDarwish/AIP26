# Student package — Medical Data Privacy Exercise

**Your job:** Prepare a privacy-preserving version of fictional hospital discharge data for an external AI vendor developing a prototype that predicts `follow_up_7d` (priority care-coordinator review within seven days).

Your goal is to balance **patient privacy** with the **predictive utility of the data**. This is not a medical decision tool.

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

## Discussion questions — Prepare for the 15-minute share-out
Be ready to present your transformed dataset and discuss the following four questions:
1. What were your main anonymisation decisions?
Which information did you remove, retain, or transform, and why? Explain at least three techniques you implemented and how you balanced privacy against predictive utility.

2. What privacy risks or limitations remain?
Identify at least one way a patient could still potentially be identified, even after your transformations. Consider combinations of attributes, information hidden in clinical notes, and limitations of your anonymisation techniques or the privacy checker.

3. What potentially useful ML signals did you lose?
Identify at least one piece of information that could have helped predict follow_up_7d but was removed or altered for privacy reasons. How might its removal affect prediction quality or fairness for particular patient groups?

4. How did your transformations change the data?
Present 2–3 examples of original versus transformed records or discharge notes. Highlight what sensitive information was removed or generalised, what clinically relevant information was preserved, and any remaining concerns.

5. **Final decision**: Would you approve sharing your transformed dataset with the external AI vendor? Under what conditions?


## Data cautions
Patients, addresses, workplaces, dates, phone numbers, relationships and sensitive narrative details are fabricated; cities/neighbourhoods are fictional. Some patterns are intentionally repeated, and a real attacker could know external facts that this audit cannot know.

The fabricated labels have no clinical validity. Avoid training an actual clinical model from this toy dataset.

Never input real sensitive patient records into a public coding assistant without authorisation and suitable controls.