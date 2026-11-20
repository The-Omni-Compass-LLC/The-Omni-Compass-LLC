# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,629 tps; base rate 994 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,690 | 2,786 | +3.6% (-5.6 to +12.7) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,913 | 2,914 | +0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 243.3 | 34.2 | -85.9% (-428.9 to +257.0) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,091 | 385.2 | -64.7% (-317.7 to +188.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.703 | 0.684 | -2.8% (-19.7 to +14.1) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 42.8 | 12.1 | -71.8% (-342.9 to +199.4) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 25.9 | +29.7% (+18.2 to +41.2) | power given |
| server connections alive, most at once | 20.0 | 35.7 | +78.3% (+59.4 to +97.3) | power given |
| host CPU busy (share of the run) | 0.329 | 0.32 | -2.9% (-20.1 to +14.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 564.4 | 547.1 | -3.1% (-20.1 to +14.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.467 | 0.437 | -6.4% (-25.4 to +12.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.15 | 2.68 | +24.2% (+19.6 to +28.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.9 | +29.6% (+17.9 to +41.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 61, 74, 34; fail-ups per arm: 0, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2623 / 601.7 / 20.0 / 20.0; omni 2823 / 5.7 / 26.8 / 26.8
- rep 2 (omni then native): native 2660 / 115.8 / 20.0 / 20.0; omni 2745 / 76.2 / 26.1 / 26.1
- rep 3 (native then omni): native 2786 / 12.4 / 20.0 / 20.0; omni 2788 / 20.7 / 24.9 / 24.9

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
