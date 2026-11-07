# The governor's own cost at 1, 10, 100 and 1,000 copies

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Omni-Compass's own CPU: the seconds its process and every command it ran spent on the CPU over the measured window, as a share of one core, from the `overhead` record every omni arm's audit carries (`omni_controller/controller.py`, written at exit), with the host's core count beside it. Native runs no governor: its cost is zero by construction. The organisms are the six with the real cluster inside (`tools/run_kil.py`); the governor's cost is the cost of governing the real cluster, which does not grow with the organism around it. Each run is shown under the engine its commit carries, and nothing is read across engines (`docs/ROBUSTNESS_PREREGISTRATION.md`, scenario 3). Shown, not judged.

## Run 37501769448 (`33b15ebb41ed`, omni-v3 (digest b53d05449ee04c4b, 40 files))

| Organism | Copies | Repetitions | Omni's own CPU (cores), mean | As a share of the host's cores | CPU seconds, mean | Window (s), mean |
|---|---:|---:|---:|---:|---:|---:|
| compute_ai_cloud | 10 | 5 | 0.0111 | 0.28% of 4 | 10.4 | 940 |
| distribution_specialized | 10 | 5 | 0.0099 | 0.25% of 4 | 9.2 | 926 |
| energy_facility_industrial | 10 | 5 | 0.0110 | 0.28% of 4 | 10.4 | 939 |
| physics_robotics_autonomous | 10 | 5 | 0.0102 | 0.26% of 4 | 9.6 | 930 |
| stack | 10 | 5 | 0.0107 | 0.27% of 4 | 10.3 | 961 |
| tower | 10 | 5 | 0.0111 | 0.28% of 4 | 10.3 | 928 |
| compute_ai_cloud | 100 | 5 | 0.0094 | 0.24% of 4 | 13.7 | 1448 |
| distribution_specialized | 100 | 5 | 0.0089 | 0.22% of 4 | 12.8 | 1432 |
| energy_facility_industrial | 100 | 5 | 0.0097 | 0.24% of 4 | 14.4 | 1481 |
| physics_robotics_autonomous | 100 | 5 | 0.0092 | 0.23% of 4 | 13.2 | 1439 |
| stack | 100 | 5 | 0.0091 | 0.23% of 4 | 15.9 | 1741 |
| tower | 100 | 5 | 0.0095 | 0.24% of 4 | 14.7 | 1540 |

## Run 37359815637 (`a004a8f9194d`, omni-v1 (37 of 38 files, all v1 bytes; not yet in this commit: tools/run_pandapower.py))

| Organism | Copies | Repetitions | Omni's own CPU (cores), mean | As a share of the host's cores | CPU seconds, mean | Window (s), mean |
|---|---:|---:|---:|---:|---:|---:|
| compute_ai_cloud | 1 | 5 | 0.0108 | 0.27% of 4 | 10.1 | 930 |
| distribution_specialized | 1 | 5 | 0.0101 | 0.25% of 4 | 9.3 | 922 |
| energy_facility_industrial | 1 | 5 | 0.0116 | 0.29% of 4 | 10.6 | 919 |
| physics_robotics_autonomous | 1 | 5 | 0.0114 | 0.29% of 4 | 10.6 | 926 |
| stack | 1 | 5 | 0.0093 | 0.23% of 4 | 8.6 | 923 |
| tower | 1 | 5 | 0.0115 | 0.29% of 4 | 10.8 | 935 |
| compute_ai_cloud | 10 | 5 | 0.0110 | 0.28% of 4 | 10.3 | 937 |
| distribution_specialized | 10 | 5 | 0.0109 | 0.27% of 4 | 10.2 | 935 |
| energy_facility_industrial | 10 | 5 | 0.0105 | 0.26% of 4 | 9.8 | 927 |
| physics_robotics_autonomous | 10 | 5 | 0.0104 | 0.26% of 4 | 9.7 | 932 |
| stack | 10 | 5 | 0.0087 | 0.22% of 4 | 8.0 | 922 |
| tower | 10 | 5 | 0.0105 | 0.26% of 4 | 9.8 | 938 |
| compute_ai_cloud | 100 | 5 | 0.0097 | 0.24% of 4 | 14.2 | 1460 |
| distribution_specialized | 100 | 5 | 0.0087 | 0.22% of 4 | 12.7 | 1438 |
| energy_facility_industrial | 100 | 5 | 0.0096 | 0.24% of 4 | 13.9 | 1449 |
| physics_robotics_autonomous | 100 | 5 | 0.0094 | 0.24% of 4 | 13.5 | 1428 |
| stack | 100 | 5 | 0.0091 | 0.23% of 4 | 14.1 | 1539 |
| tower | 100 | 5 | 0.0092 | 0.23% of 4 | 13.6 | 1468 |
| compute_ai_cloud | 1,000 | 3 | 0.0074 | 0.18% of 4 | 22.8 | 3054 |
| distribution_specialized | 1,000 | 3 | 0.0083 | 0.21% of 4 | 27.1 | 3236 |
| energy_facility_industrial | 1,000 | 3 | 0.0087 | 0.22% of 4 | 31.2 | 3557 |
| physics_robotics_autonomous | 1,000 | 3 | 0.0079 | 0.20% of 4 | 27.1 | 3373 |
| stack | 1,000 | 3 | 0.0090 | 0.22% of 4 | 28.8 | 3190 |
| tower | 1,000 | 3 | 0.0084 | 0.21% of 4 | 29.4 | 3499 |

## Run 37359820055 (`a004a8f9194d`, omni-v1 (37 of 38 files, all v1 bytes; not yet in this commit: tools/run_pandapower.py))

| Organism | Copies | Repetitions | Omni's own CPU (cores), mean | As a share of the host's cores | CPU seconds, mean | Window (s), mean |
|---|---:|---:|---:|---:|---:|---:|
| tower | 1,000 | 3 | 0.0125 | 0.16% of 8 | 36.1 | 2892 |

## Run 37575930111 (`f162ce8d74e8`, omni-v1 (digest ccc7fbdf8b312ed7, 38 files))

| Organism | Copies | Repetitions | Omni's own CPU (cores), mean | As a share of the host's cores | CPU seconds, mean | Window (s), mean |
|---|---:|---:|---:|---:|---:|---:|
| stack | 1,000 | 3 | 0.0064 | 0.08% of 8 | 18.3 | 2863 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
