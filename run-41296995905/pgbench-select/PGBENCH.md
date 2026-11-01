# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,700 tps; base rate 2,355 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,903 | 6,907 | +0.1% (-0.1 to +0.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 6,903 | 6,907 | +0.1% (-0.1 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.896 | 0.908 | +1.3% (-13.0 to +15.7) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.71 | 1.82 | +6.2% (-33.5 to +45.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.346 | 0.346 | +0.0% (-1.9 to +1.9) | STEADY, the same |
| latency, mean (ms) | 0.437 | 0.443 | +1.2% (-9.0 to +11.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.381 | 0.382 | +0.3% (-1.1 to +1.6) | STEADY, no difference beyond the noise |
| host CPU-seconds | 646.1 | 648.1 | +0.3% (-1.0 to +1.7) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.208 | 0.209 | +0.3% (-1.2 to +1.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.19 | 8.97 | +9.6% (+5.6 to +13.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6906 / 0.9 / 20.0 / 20.0; omni 6906 / 0.9 / 20.0 / 20.0
- rep 2 (omni then native): native 6905 / 0.9 / 20.0 / 20.0; omni 6913 / 0.9 / 20.0 / 20.0
- rep 3 (native then omni): native 6899 / 0.9 / 20.0 / 20.0; omni 6902 / 0.9 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
