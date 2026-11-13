# Omni-Compass on top of CityLearn's own controller

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## baeda_3dem: 4 buildings, 2,928 hours

Omni-Compass moved the commands in 2,606 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.3109 | 1.3109 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.3784 | 1.3784 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 1.0854 | 1.0854 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 0.8848 | 0.8848 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.1344 | 1.1344 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7120 | 0.7120 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.6930 | 0.6930 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 1.4067 | 1.4067 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +0.00% | same |
| time uncomfortable (`discomfort_proportion`) | 0.8142 | 0.8142 | +0.00% | same |

## citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 720 hours

Omni-Compass moved the commands in 625 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8431 | 1.8496 | +0.35% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.9002 | 1.8951 | -0.27% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.8899 | 1.8866 | -0.17% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.3288 | 1.3074 | -1.61% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9236 | 0.9813 | +6.24% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7080 | 0.6878 | -2.86% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8341 | 0.8347 | +0.07% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.9420 | 1.9408 | -0.06% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0175 | 0.0185 | +5.96% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9466 | 0.9477 | +0.12% | WORSE: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1270 | 2.1342 | +0.34% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2130 | 2.2098 | -0.15% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2157 | 2.2122 | -0.16% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4144 | 1.3954 | -1.34% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | better: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9463 | 0.9989 | +5.56% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6825 | 0.6685 | -2.05% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7542 | -1.88% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2387 | 2.2371 | -0.07% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0048 | 0.0051 | +5.50% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9889 | 0.9891 | +0.02% | WORSE: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1257 | 2.1326 | +0.32% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2118 | 2.2078 | -0.18% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2146 | 2.2109 | -0.17% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4122 | 1.3937 | -1.30% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | better: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9456 | 0.9986 | +5.60% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6831 | 0.6718 | -1.67% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2484 | 2.2468 | -0.07% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0070 | 0.0075 | +6.25% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9863 | 0.9877 | +0.15% | WORSE: more time uncomfortable |

## citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1288 | 2.1352 | +0.30% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.2124 | 2.2087 | -0.17% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.2152 | 2.2112 | -0.18% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.4148 | 1.3931 | -1.54% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2188 | 1.1763 | -3.49% | better: less highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9474 | 0.9990 | +5.45% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6834 | 0.6680 | -2.26% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7687 | 0.7543 | -1.88% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2403 | 2.2389 | -0.06% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0043 | 0.0047 | +9.80% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9879 | 0.9878 | -0.01% | better: less time uncomfortable |

## citylearn_challenge_2023_phase_3_1: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1117 | 2.1171 | +0.26% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1912 | 2.1889 | -0.10% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1970 | 2.1941 | -0.13% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5367 | 1.5029 | -2.20% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9721 | 1.0159 | +4.51% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6461 | 0.6205 | -3.96% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7298 | 0.7212 | -1.18% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2516 | 2.2511 | -0.02% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0154 | 0.0157 | +1.97% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9828 | 0.9830 | +0.02% | WORSE: more time uncomfortable |

## citylearn_challenge_2023_phase_3_2: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1119 | 2.1159 | +0.19% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1877 | 2.1856 | -0.10% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1918 | 2.1891 | -0.12% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5404 | 1.5068 | -2.18% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9763 | 1.0241 | +4.89% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6467 | 0.6199 | -4.14% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7316 | 0.7278 | -0.53% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2432 | 2.2440 | +0.04% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0130 | 0.0136 | +4.14% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9875 | 0.9884 | +0.09% | WORSE: more time uncomfortable |

## citylearn_challenge_2023_phase_3_3: 6 buildings, 2,208 hours

Omni-Compass moved the commands in 1,964 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 2.1116 | 2.1170 | +0.26% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 2.1890 | 2.1876 | -0.07% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 2.1930 | 2.1912 | -0.08% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.5391 | 1.4997 | -2.56% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.2344 | 1.2657 | +2.53% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 0.9799 | 1.0269 | +4.79% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.6520 | 0.6215 | -4.68% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.7288 | 0.7218 | -0.96% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 2.2353 | 2.2351 | -0.01% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0109 | 0.0111 | +2.22% | WORSE: more energy not served |
| time uncomfortable (`discomfort_proportion`) | 0.9844 | 0.9844 | +0.01% | WORSE: more time uncomfortable |

## quebec_neighborhood_with_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 1,914 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |
| time uncomfortable (`discomfort_proportion`) | 0.8161 | 0.8186 | +0.30% | WORSE: more time uncomfortable |

## quebec_neighborhood_without_demand_response_set_points: 20 buildings, 2,160 hours

Omni-Compass moved the commands in 1,914 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8136 | 1.8136 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 2.3217 | 2.3217 | +0.00% | same |
| carbon (`carbon_emissions_total`) | 1.0000 | 1.0000 | +0.00% | same |
| daily peak draw (`daily_peak_average`) | 2.1682 | 2.1682 | +0.00% | same |
| highest peak (`all_time_peak_average`) | 1.0938 | 1.0938 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 1.9513 | 1.9513 | +0.00% | same |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.8058 | 0.8058 | +0.00% | same |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.4781 | 0.4781 | +0.00% | same |
| distance from zero net energy (`zero_net_energy`) | 2.3289 | 2.3289 | +0.00% | same |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |
| time uncomfortable (`discomfort_proportion`) | 0.8119 | 0.8126 | +0.09% | WORSE: more time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 10 | 7 of 10 | +0.20% |
| electricity bought | 7 of 10 | 0 of 10 | -0.10% |
| carbon | 7 of 10 | 0 of 10 | -0.10% |
| daily peak draw | 7 of 10 | 0 of 10 | -1.27% |
| highest peak | 3 of 10 | 3 of 10 | -0.29% |
| ramping (swings hour to hour) | 0 of 10 | 7 of 10 | +3.70% |
| daily load unevenness | 7 of 10 | 0 of 10 | -2.16% |
| monthly load unevenness | 6 of 10 | 1 of 10 | -0.82% |
| distance from zero net energy | 6 of 10 | 1 of 10 | -0.03% |
| energy not served | 0 of 8 | 7 of 8 | +4.48% |
| time uncomfortable | 1 of 10 | 8 of 10 | +0.08% |
