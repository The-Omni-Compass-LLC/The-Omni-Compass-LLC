# Six organisms, 100 runs, 10x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7099, 10 copies of each organism on one clock, 866 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 2 | Physics / Robotics / Autonomous | 2620 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.217% (+0.215 to +0.218) | -0.016% (-0.016 to -0.015) | -0.232% (-0.233 to -0.230) | +0.246 (+0.243 to +0.250) | True |
