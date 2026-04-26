# Input Data

Input filenames keep their original downloaded names where possible.

## Active replication inputs

### Observed mortality inputs

- `demographic_inputs/fresh_downloads/ine_27153_mortality_tables_functions.xlsx`
  Official INE mortality tables and life-table functions.
- `demographic_inputs/fresh_downloads/ine_31912_male_2023_total_deaths_by_age.csv`
  Compact deaths extract used by the active male high-age starting-profile adjustment.
- `demographic_inputs/fresh_downloads/ine_56934_male_july_2023_population_by_age.csv`
  Compact population extract used by the active male high-age starting-profile adjustment.

### Model life tables

- `demographic_inputs/ine_replication/MLT_UN2011_130_1y_complete.xlsx`
  Model life tables used for the INE replication horizon.

### Published INE benchmarks

- `published_benchmarks/fresh_downloads/36774.xlsx`
  INE projected mortality `qx` by age and sex for `2024-2073`.
- `published_benchmarks/fresh_downloads/36775.xlsx`
  INE projected life expectancy by age and sex for `2024-2073`.

## Inputs reserved for the later 2100 extension

- `demographic_inputs/un_extension/MLT_UN2011_130_1y_complete.xlsx`
  Model life-table workbook reserved for the longer-horizon extension.
- `demographic_inputs/un_extension/wpp2019_life_expectancy_at_birth_male.xlsx`
  UN life-expectancy source kept for the future male extension workflow.
- `demographic_inputs/un_extension/wpp2019_life_expectancy_at_birth_female.xlsx`
  UN life-expectancy source kept for the future female extension workflow.

## Note

The active repo workflow currently centers on the INE replication stage.
The `2100` extension inputs are kept separate on purpose so the two stages do not get mixed.
Older exploratory and unrelated working files were removed from the active repo structure because they are already preserved in `old/`.
Very large raw source downloads can be kept locally and reduced to smaller tracked extracts for the active repo.
