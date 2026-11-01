# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,989 tps; base rate 748 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,395 | 1,734 | +24.3% (-67.9 to +116.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,123 | 2,190 | +3.2% (-11.6 to +18.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3,189 | 452.3 | -85.8% (-394.2 to +222.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,202 | 1,376 | -67.2% (-396.5 to +262.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 14.1 | 1.24 | -91.2% (-488.0 to +305.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 632.9 | 80.7 | -87.3% (-423.5 to +249.0) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 28.1 | +40.4% (+28.9 to +51.9) | power given |
| server connections alive, most at once | 20.0 | 37.7 | +88.3% (+62.5 to +114.2) | power given |
| host CPU busy (share of the run) | 0.329 | 0.349 | +5.9% (-13.4 to +25.1) | STEADY, no difference beyond the noise |
| host CPU-seconds | 576.0 | 607.0 | +5.4% (-11.4 to +22.1) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.95 | 0.785 | -17.3% (-88.0 to +53.4) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.2 | 2.92 | +32.6% (+20.0 to +45.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 27.8 | +38.9% (+24.5 to +53.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 44, 65; fail-ups per arm: 10, 7, 14.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1015 / 7444.5 / 20.0 / 20.0; omni 1854 / 217.9 / 28.2 / 28.1
- rep 2 (omni then native): native 1486 / 1469.3 / 20.0 / 20.0; omni 1858 / 237.3 / 28.9 / 28.8
- rep 3 (native then omni): native 1684 / 653.6 / 20.0 / 20.0; omni 1489 / 901.8 / 27.1 / 26.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
