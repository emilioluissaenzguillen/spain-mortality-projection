# UN Annualization Note

The UN inputs used for the `2100` extension are published in quinquennial form:

- `2020-2025`
- `2025-2030`
- ...
- `2095-2100`

According to the WPP2019 methodological notes, a label such as `2020-2025` refers to the full period from `1 July 2020` to `30 June 2025`, not to a single point at the end of `2025`.

## Why annualization is needed

The INE-style replication works year by year, so the UN period values must be converted into an annual target path before extending `qx` and `ax` from `2074` to `2100`.

## Plausible annualization choices

There is no unique annualization rule implied directly by the workbook itself. At least three reasonable interpretations exist:

1. `stepwise period mapping`
   Assign the same UN value to every year inside the period.

2. `midpoint mapping`
   Treat each quinquennial value as centered at the middle of the period and interpolate between midpoints.

3. `period-end knot mapping`
   Treat each quinquennial value as a knot at the period end year `2075, 2080, ..., 2100` and interpolate annually between those knots.

## Current repo choice

The current extension implementation uses `period-end knot mapping`.

This choice was made because the extension starts from the validated INE replication endpoint at `2073`:

- replicated male `e0` in `2073`: about `86.0`
- replicated female `e0` in `2073`: about `90.0`

The first available UN quinquennial values after that are:

- male `2070-2075`: `87.19`
- female `2070-2075`: `92.50`

If we interpret those UN values more literally as midpoint-type annual targets, the implied targets just after `2073` are much higher:

- midpoint-style male target for `2074`: about `87.358`
- midpoint-style female target for `2074`: about `92.668`

That would create a much sharper break from the replicated `2073` baseline.

By contrast, the current rule gives:

- current male target for `2074`: about `86.595`
- current female target for `2074`: about `91.250`

So the current mapping is more conservative and smoother as a bridge from the INE endpoint to the UN-driven extension.

## Interpretation

The current rule should be read as a `bridge assumption`, not as the only possible interpretation of the UN quinquennial tables.

It is useful because it:

- preserves continuity with the validated INE replication through `2073`
- keeps the annual extension simple and transparent
- avoids a very abrupt jump immediately after `2073`

But it should also be remembered that:

- the UN source values are period values
- another annualization rule could be defended
- any future refinement of the `2100` extension should revisit this choice explicitly
