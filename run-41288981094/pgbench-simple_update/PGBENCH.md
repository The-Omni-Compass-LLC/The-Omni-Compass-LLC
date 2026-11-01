# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,895 tps; base rate 584 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,683 | 1,683 | -0.1% (-0.9 to +0.8) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,712 | 1,714 | +0.1% (-0.2 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.77 | 4.97 | +4.3% (-9.0 to +17.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 133.1 | 132.6 | -0.3% (-46.2 to +45.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.37 | 1.36 | -0.6% (-4.1 to +2.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.45 | 4.52 | +1.6% (-30.8 to +33.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.6 | +17.9% (+7.2 to +28.6) | power given |
| server connections alive, most at once | 20.0 | 34.3 | +71.7% (+43.0 to +100.4) | power given |
| host CPU busy (share of the run) | 0.404 | 0.403 | -0.2% (-2.6 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 691.7 | 690.4 | -0.2% (-2.6 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.913 | 0.912 | -0.1% (-1.7 to +1.4) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.41 | 3.18 | +32.1% (+27.6 to +36.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.7 | +18.5% (+9.9 to +27.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 31, 39; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1686 / 4.8 / 20.0 / 20.0; omni 1678 / 5.0 / 22.7 / 23.1
- rep 2 (omni then native): native 1681 / 4.8 / 20.0 / 20.0; omni 1683 / 5.3 / 23.6 / 23.6
- rep 3 (native then omni): native 1683 / 4.7 / 20.0 / 20.0; omni 1686 / 4.6 / 24.4 / 24.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
