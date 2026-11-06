# Omni v6: capacity repair and complete non-GPU rerun campaign

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v6 stood on main from 15 to 16 October; Omni v7 (`docs/OMNI_V7.md`) stood from 16 to 17 October, and since 17 October the
engine that stands is Omni v8 (`docs/OMNI_V8.md`, the founder's order). This page and v6's four three-run tables (`results/live/V6_*.md`) stay as that engine's record, read beside no other engine's.

The engine combines the unchanged v5 muscle law and 1,107-muscle catalog with the v6 shared-host Kubernetes capacity repair.
The controller samples Linux host CPU occupancy, counts kind's shared host once, refuses extra replica capacity when that
host is busy or unmeasured, and rechecks a previously enlarged replica ceiling. This is a versioned evaluation engine;
it does not establish that every workload gains. Every result retains its own engine fingerprint and evidence class.

The source of the capacity repair is branch `codex/v6-kind-headroom-repair`, commit `3bda41a00fab81052551be99e618a523b5c61347`.
The damaged Markdown manuals on that branch are not imported. The existing intact manuals remain the starting point.
The zero-valued machines-only flag repair is retained: `1` selects machines-only; `0`, empty and unset retain full wiring.

## Campaign

`scripts/benchmark_campaign.json` records this request. A successful `verify` run for the release commit marked
`[all-nongpu]` starts the grid automatically; an unsuccessful release verification launches no campaign.
`scripts/reruns.txt` lists every single-benchmark variant;
the grid conductor releases A, B and C gradually alongside every organism at 1, 10, 100 and 1,000 copies and nested 1, 10, 100 and
1,000 runs on free GitHub runners. The v6 dispatch manifest lives under `results/grid_v6`; v5 receipts remain historical. Each job prints its
engine fingerprint and source commit. A queued, failed or unavailable test is not a completed measurement.

The queue covers Kubernetes baseline/full/levers/observe, fairness, faults, batch and trace loads, KEDA, CruiseKube,
Goldilocks, fixed capacity, scale control-plane checks, both muscle catalogs, all seven organisms (the spine the seventh since
16 October, `docs/THE_SPINE.md`) and their live-cluster
grid, Redis, Kafka, PostgreSQL, MySQL, MongoDB, MuJoCo, pandapower, CityLearn, drone swarms, robustness, Linux CPU-governor
checks, the Azure full-control burst and the larger Azure organism machine. Linux cpufreq/RAPL execution requires a host
that exposes the interfaces; a hosted VM capability refusal remains visible as unavailable hardware.

The Azure burst is `1 4 1 6 1 9`, three paired repetitions, 600 measured seconds per arm, 100 seconds per load stage.
Full wiring enables HPA control, pod CPU limits and the existing power model. It does not create host RAPL, clock control
or physical power meters on managed Azure VMs.

Free GitHub Kubernetes, Linux, swarm and organism/model workloads may use 1,000 copies and 1,000 runs.
Paid cloud and GPU organism scales remain 1, 10 and 100, with at most 100 repetitions.
The conductor lists cells that exceed free runner memory/time as pending runner capacity; it never rents a cloud
machine for them. The 1,000-copy planning estimates are extrapolations, not completed measurements.

## Prepared, not launched

Google/GKE and Amazon/EKS retain their deployment scripts and use the new shared engine on a future manual launch.
Their workflows, cloud-organism, gpu-bench and lambda-gpu are excluded from this campaign. No GPU machine is rented by it.
`scripts/gpu_campaign_profiles.json` defines one physical card and eight physical cards, with all seven organisms at scales
1, 10 and 100 and 100 paired repetitions per scale. Reports show nested 1/10/100 run prefixes. These are model copies around real hardware; only these three organism scales are permitted.

The profiles are operational through the existing `HIL_SCALES` and `HIL_REPS_BY_SCALE` environment variables. Existing
wall-clock budgets still apply: a stage that cannot finish within its budget must be reported incomplete.

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
