# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,427 tps; base rate 1,114 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,103 | 3,074 | -0.9% (-4.3 to +2.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,262 | 3,265 | +0.1% (-0.4 to +0.6) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 46.3 | 76.6 | +65.4% (-121.3 to +252.1) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 529.2 | 525.0 | -0.8% (-14.1 to +12.6) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.651 | 0.664 | +2.0% (-4.3 to +8.4) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 16.6 | 19.0 | +14.4% (-27.4 to +56.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 28.3 | +41.3% (+25.5 to +57.1) | power given |
| server connections alive, most at once | 20.0 | 37.0 | +85.0% (+85.0 to +85.0) | power given |
| host CPU busy (share of the run) | 0.328 | 0.334 | +1.9% (-1.3 to +5.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 560.7 | 571.2 | +1.9% (-1.2 to +4.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.402 | 0.413 | +2.8% (-1.4 to +7.0) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.27 | 2.85 | +25.3% (+18.9 to +31.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 28.2 | +41.2% (+25.5 to +56.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 88, 80, 74; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3100 / 45.8 / 20.0 / 20.0; omni 3101 / 55.5 / 29.2 / 29.1
- rep 2 (omni then native): native 3105 / 46.2 / 20.0 / 20.0; omni 3027 / 116.6 / 28.8 / 28.7
- rep 3 (native then omni): native 3104 / 46.9 / 20.0 / 20.0; omni 3095 / 57.6 / 26.8 / 26.8

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
