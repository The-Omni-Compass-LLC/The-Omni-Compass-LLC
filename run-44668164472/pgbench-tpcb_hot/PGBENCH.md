# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,612 tps; base rate 392 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,078 | 1,113 | +3.3% (-5.7 to +12.4) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,138 | 1,148 | +0.9% (-2.4 to +4.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 577.7 | 22.1 | -96.2% (-480.5 to +288.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,977 | 215.1 | -92.8% (-366.8 to +181.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.843 | 0.851 | +0.9% (-5.7 to +7.6) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 124.3 | 7.99 | -93.6% (-418.2 to +231.0) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.9 | +19.5% (+2.4 to +36.6) | power given |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+80.0 to +80.0) | power given |
| host CPU busy (share of the run) | 0.175 | 0.179 | +2.0% (-3.7 to +7.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 305.0 | 310.8 | +1.9% (-3.7 to +7.5) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.629 | 0.62 | -1.4% (-5.9 to +3.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.04 | 1.55 | +49.7% (+43.7 to +55.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.9 | +19.4% (+2.6 to +36.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 59, 30, 32; fail-ups per arm: 3, 1, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1066 / 111.8 / 20.0 / 20.0; omni 1094 / 38.6 / 25.4 / 25.3
- rep 2 (omni then native): native 1126 / 17.8 / 20.0 / 20.0; omni 1126 / 11.1 / 22.7 / 22.6
- rep 3 (native then omni): native 1041 / 1603.4 / 20.0 / 20.0; omni 1120 / 16.6 / 23.7 / 23.7

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
