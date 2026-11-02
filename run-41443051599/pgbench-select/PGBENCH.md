# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,845 tps; base rate 2,377 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,972 | 6,967 | -0.1% (-0.2 to +0.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 6,972 | 6,967 | -0.1% (-0.2 to +0.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.945 | 0.965 | +2.1% (-6.6 to +10.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.97 | 1.99 | +1.4% (-24.3 to +27.1) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.347 | 0.348 | +0.3% (-1.1 to +1.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.451 | 0.455 | +0.8% (-6.3 to +7.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.385 | 0.386 | +0.2% (-0.1 to +0.5) | STEADY, no difference beyond the noise |
| host CPU-seconds | 654.2 | 655.6 | +0.2% (-0.1 to +0.5) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.209 | 0.209 | +0.3% (-0.1 to +0.6) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.14 | 8.91 | +9.5% (+6.0 to +12.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6977 / 0.9 / 20.0 / 20.0; omni 6970 / 1.0 / 20.0 / 20.0
- rep 2 (omni then native): native 6969 / 1.0 / 20.0 / 20.0; omni 6966 / 0.9 / 20.0 / 20.0
- rep 3 (native then omni): native 6970 / 1.0 / 20.0 / 20.0; omni 6965 / 1.0 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
