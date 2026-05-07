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

## Interpretation of the current fit

The current replication follows the published methodology closely and matches the official tables reasonably well, especially for women and for the later years of the horizon.

INE later confirmed by email that the remaining residual differences are expected because the official starting table for `2023` was built from provisional internal deaths and provisional population inputs that are not exactly the same as the values currently published.

So:

- the `baseline` result should be read as the methodology-faithful public-data replication
- the optional `male_high_age_adjusted` result should be read only as an empirical proxy for the remaining male high-age starting-point gap

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

The main remaining mismatch is concentrated in the first projected male years at very high ages, which is consistent with the later INE clarification on the provisional `2023` starting inputs.
