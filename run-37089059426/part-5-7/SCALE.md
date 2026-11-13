# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7099, 1 copy of each organism on one clock, 139 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 5 | The four stacked, duplicates kept | 1226 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.154% (+0.153 to +0.155) | -0.000% (-0.000 to +0.000) | -0.154% (-0.155 to -0.153) | -0.024 (-0.026 to -0.023) | True |
