# Omni-Compass on top of CityLearn's own controller

CityLearn (see each district file) (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## ca_alameda_county_neighborhood: not run to the end

- native: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.
- omni: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.

## citylearn_challenge_2022_phase_all_demand_response: not run to the end

- native: ValueError: RBC controllers require interface='flat'.
- omni: ValueError: RBC controllers require interface='flat'.

## citylearn_challenge_2022_phase_all_plus_evs: not run to the end

- native: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1
- omni: ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1

## citylearn_challenge_2022_phase_all_robustness: not run to the end

- native: ValueError: RBC controllers require interface='flat'.
- omni: ValueError: RBC controllers require interface='flat'.

## citylearn_three_phase_dynamic_assets_only_demo: not run to the end

- native: ValueError: RBC controllers require interface='flat'.
- omni: ValueError: RBC controllers require interface='flat'.

## citylearn_three_phase_dynamic_topology_demo: not run to the end

- native: ValueError: RBC controllers require interface='flat'.
- omni: ValueError: RBC controllers require interface='flat'.

## citylearn_three_phase_electrical_service_demo: not run to the end

- native: ValueError: RBC controllers require interface='flat'.
- omni: ValueError: RBC controllers require interface='flat'.

## tx_travis_county_neighborhood: not run to the end

- native: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.
- omni: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.

## vt_chittenden_county_neighborhood: not run to the end

- native: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.
- omni: ModuleNotFoundError: PySAM is required for PV sizing but is not installed.

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
