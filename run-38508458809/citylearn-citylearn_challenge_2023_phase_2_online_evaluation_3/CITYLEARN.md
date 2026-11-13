# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, every row's aim is lower. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1288 | 2.1352 | +0.30% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2124 | 2.2087 | -0.17% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2112 | -0.18% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.3931 | -1.54% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9474 | 0.9990 | +5.45% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6834 | 0.6680 | -2.26% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2403 | 2.2389 | -0.06% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0047 | +9.80% | higher: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9878 | -0.01% | lower: less time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.30% |
| electricity bought | 1 of 1 | 0 of 1 | -0.17% |
| carbon | 1 of 1 | 0 of 1 | -0.18% |
| daily peak draw | 1 of 1 | 0 of 1 | -1.54% |
| highest peak | 1 of 1 | 0 of 1 | -3.49% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +5.45% |
| daily load unevenness | 1 of 1 | 0 of 1 | -2.26% |
| monthly load unevenness | 1 of 1 | 0 of 1 | -1.88% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.06% |
| energy not served | 0 of 1 | 1 of 1 | +9.80% |
| time uncomfortable | 1 of 1 | 0 of 1 | -0.01% |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
