# Omni-Compass on top of CityLearn's own controller

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, the aim is lower for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2022_phase_1 (the tuning district: not counted in the counted run): 5 buildings, 8,760 hours

Omni-Compass moved the commands in 7,859 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1158 | 0.9982 | -10.54% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.2275 | 1.0094 | -17.77% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1804 | 1.0072 | -14.67% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1417 | 1.0061 | -11.88% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0142 | 1.0000 | -1.40% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.1562 | 1.1052 | -4.41% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.9892 | 0.9863 | -0.29% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9900 | 0.9926 | +0.26% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1369 | 1.0625 | -6.55% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
