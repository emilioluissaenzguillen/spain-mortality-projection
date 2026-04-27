# Extension to 2100

This folder is reserved for the second stage of the project.

## Goal

Start from the validated INE-style replication and extend the projection to `2100` using UN-based assumptions for Spain.

## Rule

Keep this stage separate from the INE replication:

- do not overwrite the replication baseline
- do not mix INE validation logic with the `2100` extension logic

## Expected future contents

- one main extension script
- one readable walkthrough notebook
- a short note describing the UN assumptions used
- outputs stored separately from the INE replication outputs
- inputs drawn from `input/demographic_inputs/un_extension`

## Current files

- `un_extension_2100.py`
- `extension_2100_walkthrough.ipynb`
- `un_annualization_note.md`

## Current approach

The first implementation keeps the current INE-style replication unchanged through `2073` and then:

- reads the UN Spain life-expectancy path for men and women
- treats the quinquennial UN values as knots at `2075, 2080, ..., 2100`
- annualizes the target path by linear interpolation between those knots
- extends `qx` and `ax` from the replicated `2073` endpoint to a `2100` horizon profile using the same interpolation mechanics as the replication workflow

## Main outputs

- `output/mortality_projection/final/extension_2100/un_extension_validation_2074_2100.xlsx`

This workbook shows the annualized UN target path and the resulting life-table `e0` from the extension.

## Important note

The conversion from UN quinquennial values to annual targets is a modelling choice.
See:

- `un_annualization_note.md`
