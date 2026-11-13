# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `792aece5eb1b`, seeds 7000-7099, 1 copy of each organism on one clock, 1952 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 6 | The whole tower, every muscle once | 656 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.223% (+0.221 to +0.224) | -0.012% (-0.013 to -0.011) | -0.234% (-0.236 to -0.233) | +0.194 (+0.187 to +0.200) | True |
