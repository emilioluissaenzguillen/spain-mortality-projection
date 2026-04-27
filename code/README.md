# Code

The repository is organized around two stages.

## Stage 1: INE replication

This is the active implemented stage.

- `replication/ine_methodology_replication.py`
  Main script for the `2024-2073` INE replication.
- `replication/ine_methodology_replication_walkthrough.ipynb`
  Readable notebook companion that walks through the same workflow step by step.
- `replication/README.md`
  Short guide to the active script, inputs, and outputs.
- `preprocessing/build_ine_2023_start_profile_inputs.py`
  Helper extractor that reduces the raw `31912` and `56934` downloads to the compact inputs used by the active replication.

The `preprocessing/` folder is intentionally small and only contains helper scripts that prepare raw source files for the active workflow.

The main script now produces:

- the `baseline` replication
- the optional `male_high_age_adjusted` variant

in the same validation workbook.

Run it with:

```bash
python code/replication/ine_methodology_replication.py
```

## Stage 2: Extension to 2100

- `extension_2100/README.md`
- `extension_2100/extension_2100_walkthrough.ipynb`
- `extension_2100/un_extension_2100.py`

This folder now contains the first implementation step:
extend the validated INE-style workflow to `2100` using UN-based assumptions for Spain.

## Principle

The repo should stay easy to read:

- first reproduce INE as transparently as possible
- then add the `2100` extension as a separate layer
- do not mix the two workflows in the same undocumented script
