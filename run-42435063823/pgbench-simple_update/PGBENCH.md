# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,924 tps; base rate 589 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,696 | 1,702 | +0.4% (-1.3 to +2.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,724 | 1,726 | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.13 | 5.04 | -1.6% (-32.2 to +29.0) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 119.9 | 99.6 | -16.9% (-150.2 to +116.4) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.43 | 1.42 | -0.2% (-1.1 to +0.8) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.49 | 3.91 | -13.0% (-70.6 to +44.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 22.7 | +13.7% (-0.4 to +27.8) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 31.3 | +56.7% (+20.8 to +92.5) | power given |
| host CPU busy (share of the run) | 0.409 | 0.41 | +0.2% (-0.0 to +0.3) | STEADY, no difference beyond the noise |
| host CPU-seconds | 701.3 | 702.1 | +0.1% (-0.2 to +0.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.919 | 0.916 | -0.2% (-2.2 to +1.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.19 | +30.6% (+25.8 to +35.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.9 | +14.3% (+2.5 to +26.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 40, 31; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1709 / 4.7 / 20.0 / 20.0; omni 1706 / 5.0 / 21.5 / 21.8
- rep 2 (omni then native): native 1694 / 5.0 / 20.0 / 20.0; omni 1696 / 5.4 / 23.7 / 23.7
- rep 3 (native then omni): native 1686 / 5.6 / 20.0 / 20.0; omni 1705 / 4.8 / 23.0 / 23.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
