# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `792aece5eb1b`, seeds 7000-7099, 1 copy of each organism on one clock, 3200 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 262 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.224% (+0.217 to +0.230) | -0.016% (-0.018 to -0.014) | -0.239% (-0.245 to -0.233) | +0.246 (+0.235 to +0.258) | True |
