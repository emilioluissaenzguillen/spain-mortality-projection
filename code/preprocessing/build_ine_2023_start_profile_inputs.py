from __future__ import annotations

from pathlib import Path
import csv
import re


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = PROJECT_ROOT / "input" / "demographic_inputs" / "fresh_downloads"

RAW_POPULATION_FILE = INPUT_DIR / "ine_56934_full.csv"
RAW_DEATHS_FILE = INPUT_DIR / "ine_31912_full.csv"

OUTPUT_POPULATION_FILE = INPUT_DIR / "ine_56934_male_july_2023_population_by_age.csv"
OUTPUT_DEATHS_FILE = INPUT_DIR / "ine_31912_male_2023_total_deaths_by_age.csv"


def parse_number(text: str) -> float:
    return float(text.replace(".", "").replace(",", "."))


def parse_age(label: str) -> int | None:
    if "Menos de 1" in label:
        return 0
    if "100" in label:
        return 100
    match = re.search(r"\d+", label)
    if match is None:
        return None
    return int(match.group())


def build_population_extract() -> None:
    rows: list[dict[str, float | int]] = []
    with RAW_POPULATION_FILE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        for row in reader:
            if row["Sexo"] != "Hombres" or row["Periodo"] != "1 de julio de 2023":
                continue
            age = parse_age(row["Edad simple"])
            if age is None:
                continue
            rows.append({"Age": age, "Population": parse_number(row["Total"])})

    rows.sort(key=lambda row: int(row["Age"]))
    with OUTPUT_POPULATION_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Age", "Population"])
        writer.writeheader()
        writer.writerows(rows)


def build_deaths_extract() -> None:
    rows: list[dict[str, float | int]] = []
    with RAW_DEATHS_FILE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        for row in reader:
            if row["Nacional y provincias"] != "Total Nacional":
                continue
            if row["Sexo"] != "Hombres" or row["Mes del fallecimiento"] != "Total" or row["Periodo"] != "2023":
                continue
            age = parse_age(row["Edad"])
            if age is None:
                continue
            rows.append({"Age": age, "Deaths": parse_number(row["Total"])})

    rows.sort(key=lambda row: int(row["Age"]))
    with OUTPUT_DEATHS_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Age", "Deaths"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not RAW_POPULATION_FILE.exists():
        raise FileNotFoundError(f"Missing raw population file: {RAW_POPULATION_FILE}")
    if not RAW_DEATHS_FILE.exists():
        raise FileNotFoundError(f"Missing raw deaths file: {RAW_DEATHS_FILE}")

    build_population_extract()
    build_deaths_extract()
    print(OUTPUT_POPULATION_FILE)
    print(OUTPUT_DEATHS_FILE)


if __name__ == "__main__":
    main()
