# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,272 tps; base rate 1,091 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,040 | 3,054 | +0.5% (-1.0 to +1.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,200 | 3,198 | -0.0% (-0.4 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 49.4 | 31.4 | -36.5% (-138.2 to +65.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 581.3 | 522.5 | -10.1% (-24.9 to +4.7) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.636 | 0.653 | +2.6% (-0.4 to +5.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 18.9 | 16.6 | -12.3% (-34.2 to +9.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 26.1 | +30.6% (+16.6 to +44.7) | power given |
| server connections alive, most at once | 20.0 | 36.7 | +83.3% (+76.2 to +90.5) | power given |
| host CPU busy (share of the run) | 0.319 | 0.329 | +3.1% (-0.4 to +6.6) | STEADY, no difference beyond the noise |
| host CPU-seconds | 545.8 | 562.5 | +3.1% (-0.3 to +6.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.399 | 0.409 | +2.6% (+0.5 to +4.6) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.21 | 2.77 | +25.4% (+17.7 to +33.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 26.1 | +30.4% (+16.2 to +44.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 56, 44; fail-ups per arm: 1, 2, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3013 / 77.3 / 20.0 / 20.0; omni 3048 / 38.2 / 26.5 / 26.4
- rep 2 (omni then native): native 3075 / 8.8 / 20.0 / 20.0; omni 3078 / 10.2 / 27.1 / 27.0
- rep 3 (native then omni): native 3032 / 62.2 / 20.0 / 20.0; omni 3037 / 45.7 / 24.9 / 24.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
