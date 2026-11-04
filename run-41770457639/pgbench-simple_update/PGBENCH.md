# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,806 tps; base rate 571 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,643 | 1,649 | +0.4% (-1.5 to +2.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,674 | 1,674 | +0.0% (-0.2 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.91 | 4.97 | +1.3% (-1.8 to +4.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 134.1 | 101.9 | -24.0% (-134.9 to +86.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.39 | 1.4 | +0.5% (-0.3 to +1.4) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.56 | 4.01 | -12.1% (-70.3 to +46.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.4 | +17.1% (+13.0 to +21.2) | power given |
| server connections alive, most at once | 20.0 | 34.7 | +73.3% (+47.5 to +99.2) | power given |
| host CPU busy (share of the run) | 0.4 | 0.401 | +0.4% (-0.3 to +1.1) | STEADY, no difference beyond the noise |
| host CPU-seconds | 684.7 | 687.7 | +0.4% (-0.3 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.926 | 0.927 | +0.1% (-1.2 to +1.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.44 | 3.2 | +31.0% (+29.5 to +32.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.4 | +17.1% (+13.0 to +21.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 30, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1651 / 4.8 / 20.0 / 20.0; omni 1646 / 4.8 / 23.7 / 23.7
- rep 2 (omni then native): native 1641 / 5.2 / 20.0 / 20.0; omni 1645 / 5.3 / 23.4 / 23.4
- rep 3 (native then omni): native 1638 / 4.8 / 20.0 / 20.0; omni 1657 / 4.8 / 23.1 / 23.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
