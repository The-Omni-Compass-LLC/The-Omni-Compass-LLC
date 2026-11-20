# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,651 tps; base rate 2,498 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,322 | 7,324 | +0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 7,322 | 7,324 | +0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.03 | 1.06 | +2.4% (-2.6 to +7.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.4 | 2.61 | +8.8% (-19.7 to +37.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.345 | 0.348 | +0.8% (-0.1 to +1.6) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.468 | 0.48 | +2.5% (-4.2 to +9.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.395 | 0.398 | +0.8% (-0.1 to +1.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 671.5 | 676.7 | +0.8% (-0.2 to +1.8) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.204 | 0.205 | +0.7% (-0.1 to +1.6) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.58 | 9.3 | +8.4% (+2.8 to +14.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7325 / 1.0 / 20.0 / 20.0; omni 7327 / 1.0 / 20.0 / 20.0
- rep 2 (omni then native): native 7323 / 1.1 / 20.0 / 20.0; omni 7319 / 1.1 / 20.0 / 20.0
- rep 3 (native then omni): native 7318 / 1.0 / 20.0 / 20.0; omni 7326 / 1.1 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
