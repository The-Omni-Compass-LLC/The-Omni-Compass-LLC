# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,901 tps; base rate 585 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,685 | 1,687 | +0.1% (-1.2 to +1.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,715 | 1,715 | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.28 | 5.48 | +3.9% (-19.8 to +27.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 134.5 | 111.5 | -17.1% (-117.0 to +82.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.42 | 1.42 | +0.2% (-1.0 to +1.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.73 | 4.31 | -8.9% (-59.2 to +41.4) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.6 | +18.2% (+6.9 to +29.6) | power given |
| server connections alive, most at once | 20.0 | 34.3 | +71.7% (+43.0 to +100.4) | power given |
| host CPU busy (share of the run) | 0.411 | 0.413 | +0.4% (-0.1 to +1.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 703.4 | 706.4 | +0.4% (-0.1 to +1.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.928 | 0.93 | +0.3% (-1.6 to +2.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.47 | 3.24 | +31.4% (+24.2 to +38.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.6 | +18.2% (+6.8 to +29.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 38, 40; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1692 / 4.9 / 20.0 / 20.0; omni 1686 / 5.4 / 22.7 / 22.7
- rep 2 (omni then native): native 1680 / 5.6 / 20.0 / 20.0; omni 1681 / 6.1 / 24.5 / 24.5
- rep 3 (native then omni): native 1683 / 5.3 / 20.0 / 20.0; omni 1695 / 4.9 / 23.7 / 23.7

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
