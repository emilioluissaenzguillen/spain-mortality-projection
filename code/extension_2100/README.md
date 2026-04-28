# Extension to 2100

This folder contains the active second stage of the project.

## Goal

Start from the validated INE-style replication and extend the mortality projection to `2100` using UN-based assumptions for Spain.

## Main files

- `un_extension_2100.py`
- `extension_2100_walkthrough.ipynb`
- `un_annualization_note.md`

Run it with:

```bash
python code/extension_2100/un_extension_2100.py
```

## Workflow

The extension script:

1. loads the validated INE-style replication baseline through `2073`
2. reads the UN Spain life-expectancy paths for men and women
3. annualizes the UN quinquennial values for `2074-2100`
4. derives `2100` horizon `qx` and `ax` profiles from the model life tables
5. extends annual `qx`, `ax`, and life-table `e0` from `2074` to `2100`

## Key inputs

- `input/demographic_inputs/un_extension/wpp2019_life_expectancy_at_birth_male.xlsx`
- `input/demographic_inputs/un_extension/wpp2019_life_expectancy_at_birth_female.xlsx`
- `code/replication/ine_methodology_replication.py`

## Comparison logic

This stage does not validate against published INE tables after `2073`.

- Up to `2073`, the baseline is the validated INE replication.
- From `2074` to `2100`, the extension compares the generated life-table `e0` against the annualized UN target path.

## Main output

- `output/mortality_projection/final/extension_2100/un_extension_validation_2074_2100.xlsx`

This workbook is the main place to review:

- the annualized UN target path
- the resulting life-table `e0`
- the gap between the extension output and the annualized UN target

## Important note

The conversion from UN quinquennial values to annual targets is a modelling choice.
See:

- `un_annualization_note.md`
