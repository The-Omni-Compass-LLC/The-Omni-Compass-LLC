# Six organisms, 100 runs, 10x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7099, 10 copies of each organism on one clock, 1940 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 6 | The whole tower, every muscle once | 6560 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.216% (+0.215 to +0.216) | -0.012% (-0.012 to -0.012) | -0.227% (-0.228 to -0.227) | +0.188 (+0.186 to +0.190) | True |
