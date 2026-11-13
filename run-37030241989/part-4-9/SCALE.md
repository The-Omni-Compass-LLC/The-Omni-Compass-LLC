# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7099, 1 copy of each organism on one clock, 74 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 4 | Distribution / Specialized | 337 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.243% (+0.237 to +0.248) | -0.018% (-0.020 to -0.016) | -0.260% (-0.265 to -0.255) | +0.246 (+0.236 to +0.255) | True |
