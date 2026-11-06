# Omni-Compass on top of CityLearn's own controller

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the compass law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, the aim is lower for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2020_climate_zone_1: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,827 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0269 | 1.0264 | -0.05% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0086 | 1.0089 | +0.03% | higher: more carbon |
| daily peak draw (`daily_peak_average`) | 1.0240 | 1.1419 | +11.51% | higher: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.8778 | 1.0535 | +20.02% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2513 | 1.6443 | +31.40% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0534 | 1.1616 | +10.27% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9784 | 1.0967 | +12.09% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0092 | 1.0133 | +0.40% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -57.04% | lower: less energy not served |

## citylearn_challenge_2020_climate_zone_2: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,834 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0495 | 1.0415 | -0.76% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0293 | 1.0240 | -0.52% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0700 | 1.1525 | +7.70% | higher: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.7823 | 0.9732 | +24.40% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2416 | 1.5746 | +26.82% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0746 | 1.1336 | +5.49% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9642 | 1.0684 | +10.81% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0148 | 1.0213 | +0.64% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -55.25% | lower: less energy not served |

## citylearn_challenge_2020_climate_zone_3: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,836 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0302 | 1.0281 | -0.21% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0110 | 1.0101 | -0.09% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0407 | 1.1527 | +10.77% | higher: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.7778 | 0.9961 | +28.08% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2660 | 1.6226 | +28.16% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0711 | 1.1677 | +9.02% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9709 | 1.0811 | +11.35% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0066 | 1.0117 | +0.51% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -49.02% | same |

## citylearn_challenge_2020_climate_zone_4: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,843 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0582 | 1.0527 | -0.51% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0377 | 1.0338 | -0.38% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1351 | 1.2190 | +7.40% | higher: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.8131 | 0.9924 | +22.05% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2964 | 1.6012 | +23.51% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.1605 | 1.2161 | +4.78% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9833 | 1.0754 | +9.38% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0259 | 1.0368 | +1.07% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -57.27% | lower: less energy not served |

## citylearn_challenge_2021: 9 buildings, 35,040 hours

Omni-Compass moved the commands in 31,363 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0358 | 1.0327 | -0.30% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0173 | 1.0183 | +0.09% | higher: more carbon |
| daily peak draw (`daily_peak_average`) | 1.1463 | 1.2094 | +5.50% | higher: more daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0570 | 1.1672 | +10.43% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2989 | 1.6920 | +30.26% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.1975 | 1.2352 | +3.15% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 1.0641 | 1.1725 | +10.19% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0190 | 1.0202 | +0.12% | higher: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -55.92% | lower: less energy not served |

## citylearn_challenge_2022_phase_2: 5 buildings, 8,760 hours

Omni-Compass moved the commands in 7,855 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1080 | 0.9880 | -10.83% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.2124 | 1.0078 | -16.87% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1665 | 1.0021 | -14.09% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1124 | 0.9764 | -12.23% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 0.9983 | 1.0000 | +0.17% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.1231 | 1.0785 | -3.97% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.9787 | 0.9888 | +1.03% | higher: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9828 | 0.9895 | +0.68% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1970 | 1.0921 | -8.77% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## citylearn_challenge_2022_phase_3: 7 buildings, 8,760 hours

Omni-Compass moved the commands in 7,854 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0848 | 1.0395 | -4.17% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1573 | 1.0544 | -8.89% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1155 | 1.0414 | -6.65% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0973 | 0.9770 | -10.96% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 0.9942 | 0.9987 | +0.45% | higher: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.1814 | 1.2213 | +3.37% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0176 | 0.9684 | -4.83% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9838 | 0.9784 | -0.55% | lower: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0809 | 1.0454 | -3.28% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## citylearn_challenge_2022_phase_all: 17 buildings, 8,760 hours

Omni-Compass moved the commands in 7,851 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1007 | 1.0060 | -8.61% | lower: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1941 | 1.0187 | -14.69% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1496 | 1.0128 | -11.90% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1392 | 0.9802 | -13.95% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0272 | 0.9991 | -2.73% | lower: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2223 | 1.1351 | -7.13% | lower: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0084 | 0.9792 | -2.89% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9892 | 0.9903 | +0.11% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1315 | 1.0623 | -6.11% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## citylearn_challenge_2023_phase_1: 3 buildings, 720 hours

Omni-Compass moved the commands in 625 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; the aim is lower) | native | omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8368 | 1.8430 | +0.34% | higher: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.8916 | 1.8892 | -0.13% | lower: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.8808 | 1.8659 | -0.79% | lower: less carbon |
| daily peak draw (`daily_peak_average`) | 1.3043 | 1.2441 | -4.61% | lower: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9318 | 1.1678 | +25.33% | higher: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7120 | 0.6557 | -7.92% | lower: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8333 | 0.8337 | +0.06% | higher: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.9008 | 1.8984 | -0.13% | lower: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +36.30% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9600 | 0.9485 | -1.19% | lower: less time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts lower | Districts higher | Mean change |
|---|---:|---:|---:|
| electricity bill | 3 of 9 | 1 of 9 | -2.59% |
| electricity bought | 9 of 9 | 0 of 9 | -4.71% |
| carbon | 7 of 9 | 2 of 9 | -3.81% |
| daily peak draw | 4 of 9 | 5 of 9 | +0.12% |
| highest peak | 1 of 9 | 7 of 9 | +11.43% |
| ramping (swings hour to hour) | 2 of 9 | 7 of 9 | +17.53% |
| daily load unevenness | 3 of 9 | 6 of 9 | +2.01% |
| monthly load unevenness | 1 of 9 | 8 of 9 | +6.01% |
| distance from zero net energy | 4 of 9 | 5 of 9 | -1.73% |
| energy not served | 4 of 6 | 0 of 6 | -39.70% |
| time uncomfortable | 1 of 1 | 0 of 1 | -1.19% |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
