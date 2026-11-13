# Six organisms, 100 runs, 10x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7099, 10 copies of each organism on one clock, 826 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 2620 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.086% (+0.085 to +0.088) | -0.001% (-0.001 to -0.000) | -0.087% (-0.088 to -0.086) | -0.008 (-0.009 to -0.006) | True |
