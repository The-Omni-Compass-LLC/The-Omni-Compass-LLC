# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 37,629 tps; base rate 5,644 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,552 | 16,550 | -0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 16,552 | 16,550 | -0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.309 | 0.293 | -5.2% (-31.1 to +20.7) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.81 | 1.12 | -38.1% (-288.1 to +211.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.146 | 0.145 | -0.7% (-4.1 to +2.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.203 | -10.8% (-91.9 to +70.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.343 | 0.34 | -0.9% (-6.0 to +4.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 591.3 | 585.5 | -1.0% (-6.2 to +4.3) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0794 | 0.0786 | -1.0% (-6.1 to +4.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.99 | 10.5 | +5.2% (-1.0 to +11.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16550 / 0.3 / 20.0 / 20.0; omni 16541 / 0.3 / 20.0 / 20.0
- rep 2 (omni then native): native 16557 / 0.3 / 20.0 / 20.0; omni 16551 / 0.3 / 20.0 / 20.0
- rep 3 (native then omni): native 16548 / 0.3 / 20.0 / 20.0; omni 16559 / 0.3 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
