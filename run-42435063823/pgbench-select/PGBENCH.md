# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,538 tps; base rate 2,481 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,276 | 7,276 | -0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 7,276 | 7,276 | -0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.11 | 1.13 | +2.3% (-10.0 to +14.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.78 | 2.98 | +7.1% (-21.9 to +36.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.353 | 0.354 | +0.3% (-1.1 to +1.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.489 | 0.498 | +1.7% (-6.7 to +10.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.399 | 0.4 | +0.4% (-0.5 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 676.9 | 679.8 | +0.4% (-0.5 to +1.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.207 | 0.208 | +0.4% (-0.4 to +1.2) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.42 | 9.19 | +9.2% (+3.9 to +14.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7281 / 1.2 / 20.0 / 20.0; omni 7277 / 1.2 / 20.0 / 20.0
- rep 2 (omni then native): native 7275 / 1.1 / 20.0 / 20.0; omni 7277 / 1.2 / 20.0 / 20.0
- rep 3 (native then omni): native 7273 / 1.1 / 20.0 / 20.0; omni 7274 / 1.1 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
