# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,977 tps; base rate 446 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 994.2 | 1,028 | +3.4% (-2.7 to +9.4) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,306 | 1,305 | -0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 424.0 | 410.1 | -3.3% (-72.2 to +65.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,001 | 1,008 | +0.7% (-185.7 to +187.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.03 | 0.99 | -3.9% (-30.9 to +23.0) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 72.5 | 66.9 | -7.8% (-100.9 to +85.3) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 26.3 | +31.5% (+21.5 to +41.4) | power given |
| server connections alive, most at once | 20.0 | 36.7 | +83.3% (+64.4 to +102.3) | power given |
| host CPU busy (share of the run) | 0.204 | 0.206 | +0.9% (-1.0 to +2.9) | STEADY, no difference beyond the noise |
| host CPU-seconds | 357.8 | 360.8 | +0.8% (-0.9 to +2.5) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.8 | 0.78 | -2.5% (-7.6 to +2.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.52 | 2.13 | +40.3% (+37.8 to +42.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.8 | +29.0% (+20.1 to +37.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 59, 46, 54; fail-ups per arm: 22, 12, 14.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1026 / 420.8 / 20.0 / 20.0; omni 1053 / 541.7 / 27.2 / 26.5
- rep 2 (omni then native): native 987 / 367.9 / 20.0 / 20.0; omni 1000 / 272.3 / 25.9 / 25.7
- rep 3 (native then omni): native 969 / 483.3 / 20.0 / 20.0; omni 1030 / 416.3 / 25.7 / 25.1

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
