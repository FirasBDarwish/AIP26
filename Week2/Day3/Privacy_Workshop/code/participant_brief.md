# Participant brief — Privacy vs AI utility

**Scenario.** A fictional hospital will share one CSV with an external AI vendor to prototype a classifier for **priority care-coordinator review within seven days of discharge** (`follow_up_7d`). The vendor does **not** need patient identities. Your task is to preserve sufficient predictive context with defensible privacy safeguards, not to make autonomous medical decisions.

## Time-boxed lab — 35 minutes

**5 min — Decisions.** Decide which fields you would drop, retain, or transform. Explain why household composition, housing stability, language, location, rare occupations, medications, and clinical notes might be useful **and** hazardous. Choose at least **three** approaches.

**20 min — Vibe coding.** Implement your choices in `starter.py`, outputting `encounters_private.csv`. You may ask an AI coding assistant for suggestions and code, but instruct it to follow `AGENTS.md`. Pay special attention to privacy signals hidden in `discharge_note` beyond standard names/phone numbers.

**10 min — Audit and discuss.** Only *after* implementation, run `python solution_checker/privacy_checker.py`. Inspect output and manually read 3–5 random transformed notes. Explain remaining risks, information lost and what safeguards your recipient would need.

## Technique menu (pick based on the threat model)

| Technique | Example / limitation |
|---|---|
| Data minimisation | Drop contact data, unnecessary details; retains least needed for task |
| Text redaction | Mask names, addresses, dates and *contextual* clues; simple regex misses indirect identifiers |
| Pseudonymisation | Substitute stable identifiers but preserve linkability; **not anonymisation** |
| Generalisation | Convert exact age to bands; coarsen regions and dates; may reduce utility |
| Suppression | Withhold rare categories or small-group values; can skew data |
| k-anonymity | Make selected quasi-identifier groups size >= k; depends on QI definition and doesn't stop attribute inference |
| Perturbation | Small random noise to numeric fields; **not differential privacy** |
| Differential privacy | Requires calibrated mechanism and privacy budget; optional advanced discussion, not required to implement |
| Synthetic data | Artificial samples may still leak training data; these records are already entirely synthetic for teaching |

## Questions (you choose, justify and code)

1. Which household/social details actually help predict review needs? Is retaining exact numbers of children necessary? Could the number itself identify somebody?
2. If two patients share a diagnosis, but one has unstable housing and the other lives alone with no caregiver, what minimum information would be useful?
3. Does removing names alone prevent linkage of rare occupation + neighborhood + family size + discharge date? What if these facts occur only in the narrative?
4. Should the vendor get a full redacted note, a clinically focused summary, extracted structured features, or no narrative? What errors would an automated assistant make?
5. How does your choice change for internal controlled access vs contracted vendor vs public release?
6. Are your transformations fair to patients with unusual housing, a rare language or high care needs? Might suppression disproportionately erase the most vulnerable?
7. What can the checker **not** detect? What additional contextual review would be required?

## Deliverables for the 15-minute share-out

- Your `encounters_private.csv` and a short explanation of **three chosen techniques**.
- One example of a subtle identifying combination or report fragment you handled.
- One residual privacy risk and one lost or retained ML signal.
- One sentence: Would you approve this dataset for the hypothetical vendor? On what conditions?

All examples are fictitious. Never input real sensitive patient records into a public coding assistant without authorisation and suitable controls.
