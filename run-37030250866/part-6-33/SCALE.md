# Six organisms, 25 runs, 100x size

Evidence class **S** (models). Commit `7ab396540564`, seeds 7000-7024, 100 copies of each organism on one clock, 5507 s on 4 workers. Native: each organism's own controllers. Omni: the bowl law on every muscle (`realms/bowl_arm.py`). Harness `tools/run_scale.py`.

Band first (the founder's rule): no win unless the time over the service line is no higher than native's (violations, mean over runs, at or under 0 pp).

| # | Organism | Muscles | Label | Band first | Work per energy | Work | Energy | Violations (pp) | Knobs handed back |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 6 | The whole tower, every muscle once | 65600 | **SUPERIOR WITHIN GUARDRAILS** | NOT held | +0.211% (+0.211 to +0.211) | -0.012% (-0.012 to -0.012) | -0.222% (-0.223 to -0.222) | +0.190 (+0.189 to +0.191) | True |
