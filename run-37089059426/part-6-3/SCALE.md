# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7099, 1 copy of each organism on one clock, 172 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 6 | The whole tower, every muscle once | 656 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.194% (+0.193 to +0.195) | -0.000% (-0.000 to +0.000) | -0.194% (-0.194 to -0.193) | -0.009 (-0.010 to -0.007) | True |
