# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,863 tps; base rate 2,379 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,979 | 6,982 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 6,979 | 6,982 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.16 | 1.11 | -3.5% (-18.6 to +11.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.03 | 2.86 | -5.6% (-80.5 to +69.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.37 | 0.367 | -0.6% (-2.0 to +0.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.521 | 0.506 | -2.9% (-20.4 to +14.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.7 | -5.7% (-7.5 to -4.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.313 | 0.311 | -0.6% (-2.6 to +1.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 462.8 | 459.5 | -0.7% (-3.0 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.146 | -0.8% (-3.1 to +1.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.34 | +29.5% (+27.1 to +31.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.7% (-4.9 to -4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 27, 33; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6977 / 1.2 / 20.0 / 20.0; omni 6980 / 1.1 / 18.9 / 19.1
- rep 2 (omni then native): native 6976 / 1.1 / 19.6 / 20.0; omni 6985 / 1.1 / 18.6 / 19.0
- rep 3 (native then omni): native 6982 / 1.2 / 20.0 / 20.0; omni 6981 / 1.2 / 18.7 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
