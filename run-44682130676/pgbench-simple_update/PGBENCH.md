# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,585 tps; base rate 988 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,795 | 2,804 | +0.3% (-2.2 to +2.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,894 | 2,897 | +0.1% (-0.2 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.93 | 3.06 | -61.4% (-386.2 to +263.4) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 445.0 | 411.6 | -7.5% (-68.2 to +53.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.648 | 0.651 | +0.6% (-5.2 to +6.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 12.2 | 11.0 | -10.3% (-85.9 to +65.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 25.6 | +27.8% (+13.9 to +41.7) | power given |
| server connections alive, most at once | 20.0 | 36.7 | +83.3% (+52.1 to +114.6) | power given |
| host CPU busy (share of the run) | 0.3 | 0.303 | +1.2% (-3.0 to +5.3) | STEADY, no difference beyond the noise |
| host CPU-seconds | 513.4 | 518.7 | +1.0% (-2.9 to +5.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.408 | 0.411 | +0.7% (-4.7 to +6.0) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.07 | 2.61 | +26.2% (+20.7 to +31.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.6 | +27.8% (+13.9 to +41.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 66, 43, 52; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2768 / 19.4 / 20.0 / 20.0; omni 2810 / 2.6 / 26.7 / 26.7
- rep 2 (omni then native): native 2802 / 2.2 / 20.0 / 20.0; omni 2798 / 4.5 / 24.4 / 24.4
- rep 3 (native then omni): native 2814 / 2.2 / 20.0 / 20.0; omni 2805 / 2.0 / 25.6 / 25.6

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
