# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,932 tps; base rate 290 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 849.7 | 849.9 | +0.0% (-0.9 to +1.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 849.8 | 849.9 | +0.0% (-1.0 to +1.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.14 | 4.12 | -0.5% (-15.6 to +14.7) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.21 | 8.03 | -2.2% (-41.2 to +36.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.72 | 1.72 | +0.1% (-1.3 to +1.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.13 | -0.2% (-9.1 to +8.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.292 | 0.293 | +0.2% (-2.4 to +2.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 503.2 | 504.4 | +0.2% (-2.4 to +2.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.32 | 1.32 | +0.2% (-1.7 to +2.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.47 | 2.12 | +44.6% (+42.3 to +46.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 853 / 4.3 / 20.0 / 20.0; omni 850 / 4.0 / 20.0 / 20.0
- rep 2 (omni then native): native 848 / 4.2 / 20.0 / 20.0; omni 848 / 4.2 / 20.0 / 20.0
- rep 3 (native then omni): native 848 / 3.9 / 20.0 / 20.0; omni 852 / 4.1 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
