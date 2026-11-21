# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,494 tps; base rate 374 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,094 | 1,095 | +0.1% (-0.5 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,097 | 1,096 | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.13 | 2.93 | -6.3% (-38.6 to +26.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.3 | 5.75 | -44.1% (-258.3 to +170.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.32 | 1.32 | -0.6% (-4.0 to +2.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.83 | 1.65 | -9.7% (-71.7 to +52.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 17.8 | -8.2% (-12.9 to -3.5) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.246 | 0.245 | -0.2% (-2.8 to +2.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 430.7 | 429.7 | -0.2% (-2.7 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.875 | 0.872 | -0.3% (-3.2 to +2.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.64 | 1.15 | +80.1% (+69.6 to +90.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.5 | -7.3% (-9.1 to -5.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 25, 18; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1092 / 3.5 / 20.0 / 20.0; omni 1096 / 2.9 / 18.2 / 18.6
- rep 2 (omni then native): native 1096 / 3.0 / 18.3 / 20.0; omni 1095 / 3.0 / 17.1 / 18.4
- rep 3 (native then omni): native 1094 / 2.9 / 20.0 / 20.0; omni 1095 / 3.0 / 18.2 / 18.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
