# Azure quota and cleanup repair — 15 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Evidence and limits

The full-control AKS run 38693801818 completed its first paired repetition. Its next two repetitions failed on Azure CPU quota. Later full-control dispatches also failed capacity checks. These are failures of the test machinery, so they give no GAIN, STEADY or LOSS reading of the service.

The source also showed three preventable hazards: resource-group cleanup returned before deletion finished; cluster-delete errors were suppressed; and separate Azure suites could compete for the same regional machine-family allowance. Multi-pool preflight counted each pool separately rather than aggregating a shared family, and included the system node only when pool and system size names matched exactly. The live owner of occupied quota has not been established.

## Correction

The capacity helper sums system and worker CPU demand by family, checks the regional allowance too, refuses unknown or insufficient allowances, and waits for occupied capacity before allocating resources. It rechecks capacity before each AKS arm. Existing named clusters are deleted synchronously and errors remain failures. Resource-group cleanup waits until the group is read back as gone. AKS machines-only, AKS full-control and ordinary large-organism workflows share a region queue. Large-organism candidate sizes are checked before VM creation.

The helper exports no inventory: operational messages contain neither quota values nor infrastructure identifiers. Existing paired-run artifacts and historical failures are retained. The engine fingerprint, workload, worker ceiling, burst, organism scales and measured duration are unchanged. No quota increase, GPU launch, Amazon launch or Google launch is introduced.

## Validation and remaining work

Regression tests cover repeated-family accounting, differently named sizes in one family, single virtual machines outside a cluster, the regional ceiling, occupied quota retries, unknown quota, deletion read back, deletion timeout and error propagation. Workflow checks verify the common queue and awaited cleanup.

Live inventory export was blocked by automatic approval review because this repository is public. No inventory workflow was launched. Local tests cannot establish who owns occupied Azure quota or prove a successful cloud rerun. The follow-up now uses private in-memory capacity checks and Azure's public retail price API. It selects only a configured two-CPU machine at or below the existing hourly price ceiling and records the selected deployment inputs and replacement run reference. It exports no quota counters, resource-group existence data, or unrelated inventory. A successful cloud rerun is still required before calling the incident resolved.

Robustness run 38729569415 was invalid because too few controller decisions landed inside the measurement window. Redis run 38725712960 and capacity run 38722001872 also have failed jobs; their numerical results must not be relabelled successful without valid reruns.

© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
