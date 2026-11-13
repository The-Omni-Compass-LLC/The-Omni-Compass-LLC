# Six organisms, 10 runs, 1000x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7009, 1000 copies of each organism on one clock, 12881 s on 2 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 262000 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.085% (+0.085 to +0.086) | -0.000% (-0.001 to -0.000) | -0.086% (-0.086 to -0.085) | -0.008 (-0.008 to -0.007) | True |
