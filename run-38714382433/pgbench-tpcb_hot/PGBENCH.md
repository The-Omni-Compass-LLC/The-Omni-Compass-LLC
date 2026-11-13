# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,614 tps; base rate 392 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,094 | 1,114 | +1.9% (-16.0 to +19.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,150 | 1,144 | -0.6% (-3.0 to +1.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 831.2 | 2.92 | -99.6% (-528.9 to +329.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,411 | 233.5 | -83.4% (-476.6 to +309.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.831 | 0.821 | -1.2% (-12.3 to +9.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 84.1 | 10.8 | -87.2% (-491.9 to +317.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 16.8 | -14.8% (-27.7 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.179 | 0.177 | -1.5% (-13.6 to +10.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 311.7 | 307.1 | -1.5% (-13.5 to +10.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.636 | 0.613 | -3.7% (-34.2 to +26.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.555 | 1.1 | +98.3% (+83.8 to +112.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.2 | -13.9% (-25.7 to -2.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 72, 71, 73; fail-ups per arm: 0, 0, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1133 / 2.0 / 20.0 / 20.0; omni 1121 / 1.8 / 16.0 / 16.6
- rep 2 (omni then native): native 1016 / 2489.6 / 19.2 / 20.0; omni 1126 / 3.0 / 16.5 / 16.7
- rep 3 (native then omni): native 1133 / 1.9 / 20.0 / 20.0; omni 1096 / 4.0 / 18.0 / 18.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
