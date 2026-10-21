# Workshop coding-agent rules (MANDATORY)

You are helping students implement **their own proposed** privacy-preserving transformation for a **fully fictional** hospital CSV.

## Permitted files and responsibilities
- `starter.py` is the **only implementation location** for the student's anonymisation/data minimisation strategy. The student's decisions must originate from the scenario, participant brief, data dictionary and their own justification, not from the audit implementation.
- `data/hospital_discharge_raw.csv` is a **synthetic input**. Read it to understand fields and test code. Never edit it.
- `encounters_private.csv` is generated output. Never claim it is anonymous without an appropriate contextual assessment.
- `solution_checker/privacy_checker.py` is a **post-hoc independent diagnostic**. It is NOT a specification of which transformations to choose, NOT example code for `starter.py`, and NOT a target to optimise against.

## Strong separation rule
**Do not read, inspect, import, copy, reverse engineer or use the contents of `solution_checker/privacy_checker.py` to decide or implement anonymisation choices in `starter.py`.**

Students may invoke it as a separate command **only after** implementing their independently proposed transformations:

`python solution_checker/privacy_checker.py`

Read its **terminal output** to discuss remaining risk, then independently justify any revisions. Do not use its internal rules, lists, expressions or implementation to drive code. Do not modify, suppress, bypass, or tamper with the checker to improve an apparent result.

## Expectations
1. Ask the group to choose and explain at least three privacy techniques; **do not pre-fill a solution**.
2. Treat unstructured notes as a source of direct and indirect identifying details, not merely phone numbers or names.
3. Preserve the ML objective (`follow_up_7d`) and explicitly discuss utility/fairness and sensitive covariates.
4. Avoid leakage from the target into predictors. Do not claim naive noise achieves differential privacy or that pseudonyms guarantee anonymity.
5. Use only local fabricated data. **Do not upload actual patient information to external assistants.**
6. Always explain that checker results are indicative, incomplete and **not a legal or statistical anonymity guarantee**.
