# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7099, 1 copy of each organism on one clock, 337 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 5 | The four stacked, duplicates kept | 1226 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.211% (+0.210 to +0.212) | -0.016% (-0.017 to -0.015) | -0.226% (-0.227 to -0.225) | +0.250 (+0.244 to +0.255) | True |
