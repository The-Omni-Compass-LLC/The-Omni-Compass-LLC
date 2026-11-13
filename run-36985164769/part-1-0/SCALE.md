# Six organisms, 100 runs, 1x size

Evidence class **S** (models). Commit `792aece5eb1b`, seeds 7000-7099, 1 copy of each organism on one clock, 72 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | Compute / AI / Cloud | 345 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.304% (+0.298 to +0.311) | -0.018% (-0.020 to -0.016) | -0.321% (-0.328 to -0.315) | +0.263 (+0.252 to +0.273) | True |
