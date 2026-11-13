# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7099, 1 copy of each organism on one clock, 70 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 345 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.094% (+0.091 to +0.097) | +0.000% (-0.000 to +0.001) | -0.093% (-0.096 to -0.091) | -0.015 (-0.017 to -0.013) | True |
