# INE Replication

This folder contains the active replication attempt for INE's published projected mortality tables.

## Main script

- `ine_methodology_replication.py`
- `ine_methodology_replication_walkthrough.ipynb`

Run it with:

```bash
python code/replication/ine_methodology_replication.py
```

## What it does

1. Reads observed mortality information from the fresh INE mortality-table workbook `27153`.
2. Uses the current INE published benchmarks `36774` and `36775` for validation.
3. Builds projected `qx`, projected `ax`, and life-table `e0` for men and women.
4. Produces two replication variants:
   - `baseline`
   - `male_high_age_adjusted`

## Readable companion

If you want a more approachable entry point, open:

- `ine_methodology_replication_walkthrough.ipynb`

The notebook follows the same workflow as the script, but in a more narrative order.

## Key input files

- `input/demographic_inputs/fresh_downloads/ine_27153_mortality_tables_functions.xlsx`
- `input/demographic_inputs/fresh_downloads/ine_31912_male_2023_total_deaths_by_age.csv`
- `input/demographic_inputs/fresh_downloads/ine_56934_male_july_2023_population_by_age.csv`
- `input/demographic_inputs/ine_replication/MLT_UN2011_130_1y_complete.xlsx`
- `input/published_benchmarks/fresh_downloads/36774.xlsx`
- `input/published_benchmarks/fresh_downloads/36775.xlsx`

## Raw-source note

The full INE raw download `ine_31912_full.csv` is not tracked in GitHub because it exceeds GitHub's file-size limit.
If needed, the compact tracked inputs can be regenerated from the raw downloads with:

```bash
python code/preprocessing/build_ine_2023_start_profile_inputs.py
```

## Main output

- `output/mortality_projection/final/ine_replication_2024_2073/ine_replication_validation_2024_2073.xlsx`

This workbook is the main place to review:

- overall fit metrics
- benchmark comparisons by sex and year
- life-expectancy validation
- the side-by-side comparison between the baseline and the optional male high-age adjustment
