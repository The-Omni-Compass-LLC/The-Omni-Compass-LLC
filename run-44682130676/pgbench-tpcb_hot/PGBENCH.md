# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,013 tps; base rate 302 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `fe3cbb497940`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 830.9 | 850.6 | +2.4% (-4.2 to +8.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 885.4 | 883.9 | -0.2% (-0.3 to -0.1) | LOSS |
| latency, 95th percentile (ms, lag included) | 126.9 | 38.0 | -70.0% (-332.4 to +192.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 367.2 | 251.5 | -31.5% (-128.0 to +65.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.14 | 1.12 | -1.6% (-3.3 to +0.2) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 18.7 | 10.2 | -45.7% (-212.0 to +120.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 21.0 | +5.0% (-2.2 to +12.2) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 29.7 | +48.3% (+1.3 to +95.4) | power given |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.8% (-1.9 to +0.3) | STEADY, no difference beyond the noise |
| host CPU-seconds | 360.3 | 357.3 | -0.8% (-1.9 to +0.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.965 | 0.934 | -3.2% (-11.4 to +4.9) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.17 | 1.75 | +49.2% (+43.9 to +54.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 21.0 | +4.9% (-2.2 to +12.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 28, 15; fail-ups per arm: 7, 5, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 786 / 313.4 / 20.0 / 20.0; omni 831 / 69.9 / 20.7 / 20.6
- rep 2 (omni then native): native 837 / 58.9 / 20.0 / 20.0; omni 845 / 40.7 / 21.7 / 21.6
- rep 3 (native then omni): native 870 / 8.5 / 20.0 / 20.0; omni 876 / 3.5 / 20.6 / 20.6

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
