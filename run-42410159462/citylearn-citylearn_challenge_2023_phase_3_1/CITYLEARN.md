# Omni-Compass on top of CityLearn's own controller

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn 3.2.0 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.0875 an hour, reading the coming hour from the same hour of the past 7 days, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, read by the one key: a fall is a GAIN; a rise in energy not served or time uncomfortable is a LOSS, a rise in any other score (a resource spent or held) is power given. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 0 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery) | native | omni | Change | Reading (this run) |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1117 | 2.1117 | +0.00% | STEADY |
| electricity bought (`electricity_consumption_total`) | 2.1912 | 2.1912 | +0.00% | STEADY |
| carbon (`carbon_emissions_total`) | 2.1971 | 2.1971 | +0.00% | STEADY |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5367 | +0.00% | STEADY |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2344 | +0.00% | STEADY |
| ramping (swings hour to hour) (`ramping_average`) | 0.9721 | 0.9721 | +0.00% | STEADY |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6461 | 0.6461 | +0.00% | STEADY |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7297 | 0.7297 | +0.00% | STEADY |
| distance from zero net energy (`zero_net_energy`) | 2.2517 | 2.2517 | +0.00% | STEADY |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0154 | +0.00% | STEADY |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9828 | +0.00% | STEADY |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts where it fell | Districts where it rose | Mean change | A rise reads |
|---|---:|---:|---:|---|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% | power given |
| electricity bought | 0 of 1 | 0 of 1 | +0.00% | power given |
| carbon | 0 of 1 | 0 of 1 | +0.00% | power given |
| daily peak draw | 0 of 1 | 0 of 1 | +0.00% | power given |
| highest peak | 0 of 1 | 0 of 1 | +0.00% | power given |
| ramping (swings hour to hour) | 0 of 1 | 0 of 1 | +0.00% | power given |
| daily load unevenness | 0 of 1 | 0 of 1 | +0.00% | power given |
| monthly load unevenness | 0 of 1 | 0 of 1 | +0.00% | power given |
| distance from zero net energy | 0 of 1 | 0 of 1 | +0.00% | power given |
| energy not served | 0 of 1 | 0 of 1 | +0.00% | LOSS |
| time uncomfortable | 0 of 1 | 0 of 1 | +0.00% | LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
