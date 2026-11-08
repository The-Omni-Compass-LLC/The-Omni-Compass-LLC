# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,847 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,667 | 1,661 | -0.4% (-0.9 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,692 | 1,692 | -0.0% (-0.5 to +0.5) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.07 | 5.12 | +1.0% (-15.4 to +17.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 96.7 | 137.1 | +41.8% (-50.0 to +133.6) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.37 | 1.38 | +0.7% (-2.2 to +3.6) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.02 | 4.54 | +13.0% (-25.1 to +51.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.7 | +18.3% (+13.5 to +23.1) | power given |
| server connections alive, most at once | 20.0 | 35.3 | +76.7% (+50.8 to +102.5) | power given |
| host CPU busy (share of the run) | 0.399 | 0.401 | +0.6% (-0.9 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 683.4 | 687.5 | +0.6% (-0.9 to +2.1) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.911 | 0.92 | +1.0% (-0.7 to +2.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.41 | 3.15 | +30.6% (+25.4 to +35.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.8 | +18.8% (+13.7 to +24.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 41, 39, 37; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1670 / 5.1 / 20.0 / 20.0; omni 1660 / 5.1 / 24.0 / 24.0
- rep 2 (omni then native): native 1660 / 5.4 / 20.0 / 20.0; omni 1657 / 5.2 / 23.8 / 24.0
- rep 3 (native then omni): native 1672 / 4.6 / 20.0 / 20.0; omni 1665 / 5.1 / 23.2 / 23.3

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
