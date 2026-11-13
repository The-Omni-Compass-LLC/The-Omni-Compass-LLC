# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,299 tps; base rate 495 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 8d4f91f0dabbc9fd, 43 files) at `3132004c90de`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,446 | 1,436 | -0.7% (-1.8 to +0.4) | no difference beyond the noise |
| throughput (transactions a second) | 1,450 | 1,449 | -0.1% (-0.7 to +0.5) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.48 | 1.83 | +23.0% (-24.4 to +70.5) | no difference beyond the noise |
| latency, 99th percentile (ms) | 15.3 | 42.3 | +176.1% (-70.7 to +422.8) | no difference beyond the noise |
| latency, median (ms) | 0.749 | 0.753 | +0.5% (-1.3 to +2.3) | no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.98 | +53.4% (-8.4 to +115.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 16.3 | -18.4% (-34.9 to -1.8) | better |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-12.3 to +25.6) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.197 | 0.199 | +0.9% (-0.7 to +2.5) | no difference beyond the noise |
| host CPU-seconds | 227.0 | 229.1 | +0.9% (-0.9 to +2.7) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.523 | 0.532 | +1.6% (-1.0 to +4.1) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.339 | 0.628 | +85.2% (+76.5 to +94.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.6 | -16.8% (-33.7 to +0.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 42, 54, 49; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1442 / 1.6 / 20.0 / 20.0; omni 1433 / 1.7 / 16.2 / 16.6
- rep 2 (omni then native): native 1451 / 1.4 / 19.9 / 20.0; omni 1434 / 2.1 / 17.6 / 18.0
- rep 3 (native then omni): native 1446 / 1.5 / 20.0 / 20.0; omni 1441 / 1.6 / 15.1 / 15.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
