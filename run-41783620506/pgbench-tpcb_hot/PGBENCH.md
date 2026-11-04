# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,148 tps; base rate 472 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,380 | 1,383 | +0.2% (-1.2 to +1.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,384 | 1,384 | +0.0% (-0.7 to +0.8) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.87 | 1.81 | -3.4% (-32.5 to +25.8) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.0 | 8.05 | -27.2% (-108.0 to +53.6) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.796 | 0.791 | -0.6% (-8.4 to +7.2) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.14 | -14.7% (-60.4 to +31.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.5 | +2.3% (-3.6 to +8.2) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 24.3 | +21.7% (-25.4 to +68.7) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.206 | 0.206 | +0.0% (-9.2 to +9.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 356.9 | 356.9 | +0.0% (-9.0 to +9.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.575 | 0.573 | -0.2% (-8.7 to +8.2) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.22 | 1.69 | +38.5% (+36.1 to +40.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.5 | +2.3% (-3.6 to +8.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 7, 15; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1372 / 2.0 / 20.0 / 20.0; omni 1384 / 1.9 / 20.0 / 20.0
- rep 2 (omni then native): native 1384 / 1.9 / 20.0 / 20.0; omni 1386 / 1.7 / 20.4 / 20.4
- rep 3 (native then omni): native 1384 / 1.7 / 20.0 / 20.0; omni 1380 / 1.9 / 20.9 / 20.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
