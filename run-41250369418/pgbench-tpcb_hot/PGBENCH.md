# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,089 tps; base rate 163 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `a73ae3e52895`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 366.1 | 380.7 | +4.0% (-29.2 to +37.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 478.5 | 477.6 | -0.2% (-1.8 to +1.5) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 347.2 | 434.0 | +25.0% (-337.9 to +387.8) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 730.0 | 1,090 | +49.4% (-349.2 to +447.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.21 | 1.14 | -5.7% (-32.8 to +21.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 59.8 | 71.4 | +19.4% (-305.6 to +344.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.3 | +1.4% (-1.0 to +3.7) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 28.0 | +40.0% (+27.6 to +52.4) | power given |
| host CPU busy (share of the run) | 0.116 | 0.115 | -0.9% (-8.8 to +7.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 205.9 | 203.9 | -0.9% (-9.0 to +7.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.26 | 1.2 | -4.7% (-43.9 to +34.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.817 | 1.36 | +66.5% (+65.0 to +67.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.2 | +0.9% (-1.5 to +3.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 8, 22; fail-ups per arm: 8, 4, 11.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 362 / 339.2 / 20.0 / 20.0; omni 412 / 181.7 / 20.5 / 20.4
- rep 2 (omni then native): native 395 / 204.9 / 20.0 / 20.0; omni 354 / 874.7 / 20.2 / 20.0
- rep 3 (native then omni): native 341 / 497.6 / 20.0 / 20.0; omni 376 / 245.6 / 20.2 / 20.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
