# Six organisms, 10 runs, 100x size

Evidence class **S** (models). Commit `70a03bc96839`, seeds 7000-7009, 100 copies of each organism on one clock, 590 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 4 | Distribution / Specialized | 33700 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.242% (+0.240 to +0.244) | -0.016% (-0.017 to -0.015) | -0.257% (-0.260 to -0.255) | +0.258 (+0.254 to +0.263) | True |
