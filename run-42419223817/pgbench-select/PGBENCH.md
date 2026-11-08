# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 35,765 tps; base rate 5,365 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 15,732 | 15,615 | -0.7% (-2.5 to +1.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 15,732 | 15,732 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.31 | 1.46 | +11.5% (-8.1 to +31.1) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.69 | 37.9 | +925.5% (-1120.2 to +2971.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.216 | 0.216 | +0.2% (-1.2 to +1.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.393 | 1.07 | +172.3% (-210.5 to +555.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.3 | +1.3% (-1.5 to +4.0) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 23.3 | +16.7% (-19.2 to +52.5) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.445 | 0.445 | +0.1% (-0.4 to +0.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 792.3 | 794.0 | +0.2% (-0.3 to +0.7) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.112 | 0.113 | +1.0% (-0.4 to +2.4) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 14.5 | 15.3 | +5.5% (+3.8 to +7.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.3 | +1.3% (-1.5 to +4.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 0, 6; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 15736 / 1.5 / 20.0 / 20.0; omni 15587 / 1.6 / 20.4 / 20.4
- rep 2 (omni then native): native 15726 / 1.3 / 20.0 / 20.0; omni 15734 / 1.4 / 20.0 / 20.0
- rep 3 (native then omni): native 15734 / 1.1 / 20.0 / 20.0; omni 15524 / 1.4 / 20.4 / 20.4

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
