# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,818 tps; base rate 873 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,354 | 2,360 | +0.3% (-3.0 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,556 | 2,557 | +0.0% (-0.8 to +0.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 301.0 | 362.1 | +20.3% (-58.8 to +99.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 930.4 | 951.4 | +2.3% (-25.8 to +30.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.18 | 1.17 | -0.7% (-1.8 to +0.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 40.4 | 43.0 | +6.4% (-39.8 to +52.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | -3.0% (-8.2 to +2.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.391 | 0.392 | +0.3% (-1.3 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 676.8 | 678.9 | +0.3% (-1.2 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.639 | 0.639 | +0.0% (-3.0 to +3.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.6 | +58.0% (+51.2 to +64.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.6% (-7.8 to +2.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 42, 41; fail-ups per arm: 4, 6, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2316 / 331.6 / 20.0 / 20.0; omni 2350 / 435.3 / 19.8 / 19.8
- rep 2 (omni then native): native 2353 / 356.4 / 20.0 / 20.0; omni 2365 / 307.8 / 19.0 / 19.0
- rep 3 (native then omni): native 2392 / 215.0 / 20.0 / 20.0; omni 2365 / 343.2 / 19.4 / 19.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
