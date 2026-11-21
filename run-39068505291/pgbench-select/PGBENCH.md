# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,601 tps; base rate 2,490 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,298 | 7,300 | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,298 | 7,300 | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.51 | 1.3 | -14.0% (-17.4 to -10.7) | GAIN |
| latency, 99th percentile (ms) | 4.55 | 3.82 | -16.1% (-32.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.373 | 0.368 | -1.3% (-3.3 to +0.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.6 | 0.557 | -7.1% (-10.4 to -3.8) | GAIN |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.1% (-9.8 to -4.5) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.328 | 0.322 | -1.9% (-4.2 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 483.4 | 473.3 | -2.1% (-4.9 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.144 | -2.1% (-4.9 to +0.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.65 | 3.31 | +24.9% (+19.6 to +30.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.6% (-6.3 to -5.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 11, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7299 / 1.6 / 20.0 / 20.0; omni 7301 / 1.3 / 18.5 / 18.8
- rep 2 (omni then native): native 7296 / 1.4 / 18.4 / 20.0; omni 7298 / 1.2 / 17.2 / 18.8
- rep 3 (native then omni): native 7298 / 1.5 / 20.0 / 20.0; omni 7302 / 1.3 / 18.5 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
