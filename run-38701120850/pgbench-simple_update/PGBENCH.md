# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,697 tps; base rate 855 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,446 | 2,433 | -0.5% (-2.3 to +1.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,509 | 2,501 | -0.3% (-0.4 to -0.2) | LOSS |
| latency, 95th percentile (ms, lag included) | 4.97 | 5.16 | +3.9% (-13.4 to +21.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 177.3 | 199.0 | +12.3% (-28.6 to +53.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.08 | 1.09 | +0.6% (-0.4 to +1.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.58 | 6.31 | +13.0% (-53.9 to +79.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.3 | -8.5% (-19.4 to +2.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.43 | 0.431 | +0.1% (-0.2 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 745.6 | 746.7 | +0.1% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.677 | 0.682 | +0.7% (-1.6 to +3.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.1 | 1.74 | +58.0% (+53.8 to +62.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.1% (-18.7 to +4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 58, 51, 72; fail-ups per arm: 0, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2458 / 5.2 / 20.0 / 20.0; omni 2433 / 5.6 / 18.6 / 18.9
- rep 2 (omni then native): native 2442 / 4.8 / 20.0 / 20.0; omni 2421 / 5.2 / 19.0 / 19.3
- rep 3 (native then omni): native 2438 / 4.9 / 20.0 / 20.0; omni 2445 / 4.7 / 17.3 / 17.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
