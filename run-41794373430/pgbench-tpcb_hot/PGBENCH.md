# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,945 tps; base rate 442 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,294 | 1,294 | +0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,296 | 1,296 | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.65 | 1.77 | +7.3% (-5.9 to +20.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.74 | 7.3 | +8.3% (-72.8 to +89.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.791 | 0.8 | +1.1% (-4.9 to +7.2) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.16 | +1.9% (-13.1 to +16.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.5 | +2.5% (-4.2 to +9.3) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 26.0 | +30.0% (-44.5 to +104.5) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.193 | 0.197 | +1.7% (-3.3 to +6.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 334.9 | 340.7 | +1.7% (-3.2 to +6.7) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.575 | 0.585 | +1.7% (-2.9 to +6.4) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.17 | 1.66 | +41.5% (+37.1 to +46.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.5 | +2.5% (-4.2 to +9.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 14, 7, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1290 / 1.8 / 20.0 / 20.0; omni 1292 / 1.9 / 21.1 / 21.1
- rep 2 (omni then native): native 1297 / 1.6 / 20.0 / 20.0; omni 1296 / 1.7 / 20.4 / 20.4
- rep 3 (native then omni): native 1296 / 1.5 / 20.0 / 20.0; omni 1295 / 1.7 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
