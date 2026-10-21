"""Student implementation area. This is intentionally NOT an anonymisation solution.

Run: python starter.py
Then: python solution_checker/privacy_checker.py

Only synthetic fabricated records are used. Do not import the checker here.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT_PATH = ROOT / 'data' / 'hospital_discharge_raw.csv'
OUTPUT_PATH = ROOT / 'encounters_private.csv'


def transform(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Implement and justify YOUR group's privacy transformations here.

    Consider: feature minimisation, narrative management, quasi-identifiers,
    household features, location detail, cross-record identifiability.

    Important: This skeleton intentionally has NO privacy protections yet.
    Returning the rows unchanged is an unsafe baseline for illustration only.
    """
    # TODO: decide release audience, required ML features and acceptable risk.
    # TODO: implement at least three techniques of your choice.
    # TODO: make a documented decision about discharge_note.
    # TODO: assess usefulness of retained fields for follow_up_7d.
    return rows


def main() -> None:
    with INPUT_PATH.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    protected = transform(rows)
    if not protected:
        raise ValueError('Transformation produced no records.')
    fields = list(protected[0].keys())
    if any(set(row) != set(fields) for row in protected):
        raise ValueError('All output records must have the same fields.')
    with OUTPUT_PATH.open('w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        writer.writerows(protected)
    print(f'Wrote {len(protected)} rows to {OUTPUT_PATH.name}.')
    print('WARNING: the provided baseline is NOT anonymised. Implement transform() before sharing.')


if __name__ == '__main__':
    main()
