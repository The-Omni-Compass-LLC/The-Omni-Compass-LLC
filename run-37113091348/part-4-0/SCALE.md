# Six organisms, 10 runs, 1000x size

Evidence class **S** (models). Commit `9cef8d3a4284`, seeds 7000-7009, 1000 copies of each organism on one clock, 5499 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 4 | Distribution / Specialized | 337000 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.084% (+0.083 to +0.084) | -0.000% (-0.000 to -0.000) | -0.084% (-0.084 to -0.083) | -0.016 (-0.016 to -0.016) | True |
