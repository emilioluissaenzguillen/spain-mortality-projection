# INE Mortality Projection Note

This note summarizes the main methodological clarifications found in the INE reply documents in `reference/INE/emails`.

## Main idea

The INE correspondence confirms that the published mortality projection is built by interpolating yearly mortality-rate series, not by projecting directly by cohort.

## 2024-2073 update

The official INE methodology for the `2024-2073` release keeps the same overall structure, but with important updates:

1. The mortality projection is now anchored to the `2024-2073` national hypotheses.
2. The life-expectancy regression ends in `2023`, not `2019`.
3. The pandemic years `2020` and `2021` are excluded from that regression.
4. INE explicitly states that the effect of COVID-19 is removed from this edition.
5. The expert horizon targets for `2073` are `86.0` years for men and `90.0` years for women.
6. The projected `qx` for `2073` is still obtained by interpolation between Coale-Demeny model life tables, East for men and West for women.
7. The methodology note says the projected age profiles avoid carrying forward the pandemic shock and refers again to the twice-smoothed `2019` `qx` and `ax` profiles as the age-pattern starting point.

## What the emails clarify

1. Interpolation is by year, not by cohort.
   The projected `qx` series for each year is constructed year by year.

2. The first target is the `qx` series for the final horizon year.
   In the official INE setup, that horizon year is 2069.

3. The logit regression is estimated using life expectancy at birth from the INE mortality tables.
   The emails confirm that the relevant series is the observed Spanish life expectancy at birth for 1991-2019 from the INE mortality-table publication.

4. The asymptotes are chosen to fit the horizon-year life expectancy.
   INE explains that `e0_max` is chosen so that the projected life expectancy at birth for the final horizon matches the expert target, and `e0_min` is chosen as the value giving the best fit together with that maximum.

5. For the official 2020-2069 projection, the final-horizon `qx` is obtained from model life tables.
   INE explains that the projected `qx` for the last year is obtained by linear interpolation between adjacent Ansley Coale / Paul Demeny model tables.

6. The intermediate years are interpolated between smoothed 2019 `qx` and the final-horizon `qx`.
   INE explains that the yearly `qx` series for 2020-2068 is obtained by linear interpolation between:
   - the projected `qx` for the final horizon year
   - the 2019 `qx` series smoothed twice with 5-term moving averages across years, not across ages

7. The same idea applies to `ax`.
   The public methodology states that the average years lived in the last year of life, `ax`, is also obtained for the final horizon from the model tables and interpolated year by year from the smoothed 2019 `ax` profile.

8. The national life table closes at age 100+.
   INE's mortality-table methodology uses `q100+ = 1`, then computes `Lx = l_{x+1} + ax * dx` and `e0 = Tx / lx`.

9. The smoothing is done across years.
   The emails explicitly clarify that the moving-average smoothing is applied using neighboring calendar years, not neighboring ages.

10. To extend the projection beyond 2069, the same methodology should be repeated with a new horizon.
   INE’s guidance was not to simply attach model-table values after 2069, but rather to set a longer projection horizon, choose new asymptotes, obtain the horizon-year `qx`, and then interpolate the intermediate years again.

11. The published 2020 results include a one-year COVID shock.
   The INE release for the 2020-2070 population projections states that:
   - excess mortality observed up to July 2020 was taken into account
   - mortality is assumed to be affected only during 2020
   - 2021 is projected with normal mortality again

   This is important when validating the published 2020 `qx` and `e0` values. A clean replication of the baseline interpolation mechanics can match 2021 onward extremely well while still missing part of the special 2020 shock if that one-off adjustment is not modelled separately.

## Specific values mentioned by INE

### Men

- Expert target life expectancy at birth for 2069: `85.8`
- Official asymptotes used by INE: `e0_max = 86.5`, `e0_min = 60`
- Interpolation coefficient for 2069: `0.824744`

This coefficient implies interpolation between the model-table levels corresponding to life expectancy `85` and `86`.

### Women

- Expert target life expectancy at birth for 2069: `90.01`
- Official asymptotes used by INE: `e0_max = 90.9`, `e0_min = 60`
- Interpolation coefficient for 2069: `0.009292`

This coefficient implies interpolation between the model-table levels corresponding to life expectancy `90` and `91`.

## Why your results can differ slightly

One INE reply explains that small decimal differences can appear because the original official exercise used provisional 2019 results at the time, while later replications may use final 2019 values.

## Files behind this note

- `reference/INE/emails/ine_reply_ref_183752.docx`
- `reference/INE/emails/ine_reply_ref_184116.docx`
- `reference/INE/emails/ine_reply_ref_184306.docx`
- `reference/INE/emails/ine_reply_ref_186580.docx`
- `https://ine.es/en/metodologia/t20/meto_propob_2024_2074_en.pdf`
