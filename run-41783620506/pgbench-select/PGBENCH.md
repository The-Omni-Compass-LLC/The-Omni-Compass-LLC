# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,316 tps; base rate 2,297 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,740 | 6,736 | -0.1% (-0.1 to +0.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 6,740 | 6,736 | -0.1% (-0.1 to +0.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.902 | 0.858 | -4.8% (-10.2 to +0.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.78 | 1.57 | -12.1% (-18.1 to -6.1) | GAIN |
| latency, median (ms) | 0.349 | 0.346 | -0.9% (-3.4 to +1.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.444 | 0.428 | -3.6% (-6.1 to -1.2) | GAIN |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.377 | 0.375 | -0.6% (-2.4 to +1.3) | STEADY, no difference beyond the noise |
| host CPU-seconds | 640.3 | 637.0 | -0.5% (-2.2 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.211 | 0.21 | -0.5% (-2.2 to +1.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.08 | 8.79 | +8.7% (+7.0 to +10.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6747 / 0.9 / 20.0 / 20.0; omni 6741 / 0.9 / 20.0 / 20.0
- rep 2 (omni then native): native 6736 / 0.9 / 20.0 / 20.0; omni 6731 / 0.8 / 20.0 / 20.0
- rep 3 (native then omni): native 6737 / 0.9 / 20.0 / 20.0; omni 6735 / 0.9 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
