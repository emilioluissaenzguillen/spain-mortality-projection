# Spain Mortality Projection

This repository is being cleaned into two clear stages:

1. Replicate INE's mortality projection methodology as faithfully as possible.
2. Extend the projection to `2100` using UN-based assumptions for Spain.

## Current status

The active completed stage is the INE replication for the current release:

- horizon: `2024-2073`
- benchmark qx table: `36774`
- benchmark life-expectancy table: `36775`

The active replication script is:

- `code/replication/ine_methodology_replication.py`
- `code/replication/ine_methodology_replication_walkthrough.ipynb`

The extension stage currently lives under:

- `code/extension_2100`
- `code/extension_2100/extension_2100_walkthrough.ipynb`
- `code/extension_2100/un_extension_2100.py`

To rerun the active workflow:

```bash
pip install -r requirements.txt
python code/replication/ine_methodology_replication.py
```

## Repository layout

- `code`
  Active scripts and notes.
- `input`
  Source data used by the active workflow.
- `reference`
  Methodology PDFs, INE replies, and supporting reading.
- `output`
  Generated workbooks and tables.
- `old`
  Safety backup. Kept outside the active workflow.

## Recommended reading order

1. `code/README.md`
2. `code/replication/ine_methodology_replication_walkthrough.ipynb`
3. `code/replication/README.md`
4. `reference/INE/mortality_projection_note.md`
5. `code/replication/ine_methodology_replication.py`

## Main outputs

- `output/mortality_projection/final/ine_replication_2024_2073/ine_replication_validation_2024_2073.xlsx`

This workbook contains:

- the baseline replication
- the optional `male_high_age_adjusted` variant
- direct comparisons against INE `36774` and `36775`

INE later confirmed by email that the remaining small discrepancies in the `2024-2073` replication are expected to come from the provisional internal deaths file and provisional `1 July 2023` population inputs used to build the official starting table for `2023`. So the residual gap should be interpreted as an input-data limitation of the public replication, not as evidence of a missing unpublished adjustment in the method.

## Repo notes

- Input filenames keep their original downloaded names where possible.
- The main workflow is now Python-based and documented in English.
- Old exploratory code has been removed from the active path to keep the repo easier to follow.
- `old/` and generated `output/` files are ignored in Git so the uploaded repo stays focused on source material.
- Oversized raw downloads are replaced by smaller tracked extracts when the active workflow only needs a narrow subset.
