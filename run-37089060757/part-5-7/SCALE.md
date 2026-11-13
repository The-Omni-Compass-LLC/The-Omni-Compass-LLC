# Six organisms, 100 runs, 10x size

Evidence class **S** (models). Commit `e0294a584531`, seeds 7000-7099, 10 copies of each organism on one clock, 3056 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 5 | The four stacked, duplicates kept | 12260 | **SUPERIOR WITHIN GUARDRAILS** | held | +0.156% (+0.156 to +0.156) | -0.000% (-0.000 to +0.000) | -0.156% (-0.156 to -0.156) | -0.023 (-0.023 to -0.022) | True |
