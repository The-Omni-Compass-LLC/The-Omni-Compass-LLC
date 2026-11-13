# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7099, 1 copy of each organism on one clock, 59 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 262 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.228% (+0.222 to +0.234) | -0.015% (-0.016 to -0.013) | -0.242% (-0.248 to -0.237) | +0.237 (+0.224 to +0.251) | True |
