# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,981 tps; base rate 597 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,718 | 1,717 | -0.0% (-0.4 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,752 | 1,749 | -0.2% (-0.7 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.99 | 5.84 | -2.5% (-18.8 to +13.8) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 160.7 | 131.7 | -18.1% (-50.9 to +14.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.42 | 1.42 | +0.1% (-0.8 to +1.0) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 5.23 | 4.76 | -9.1% (-23.7 to +5.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.9 | +19.4% (+7.1 to +31.7) | power given |
| server connections alive, most at once | 20.0 | 34.0 | +70.0% (+37.1 to +102.9) | power given |
| host CPU busy (share of the run) | 0.415 | 0.415 | +0.0% (-0.8 to +0.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 709.5 | 709.6 | +0.0% (-0.8 to +0.8) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.918 | 0.918 | +0.0% (-1.0 to +1.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.5 | 3.27 | +30.8% (+30.4 to +31.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.0 | +20.0% (+8.4 to +31.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 42, 31, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1713 / 6.7 / 20.0 / 20.0; omni 1713 / 6.2 / 23.4 / 23.7
- rep 2 (omni then native): native 1726 / 5.4 / 20.0 / 20.0; omni 1728 / 5.2 / 23.2 / 23.2
- rep 3 (native then omni): native 1714 / 5.9 / 20.0 / 20.0; omni 1711 / 6.2 / 25.0 / 25.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
