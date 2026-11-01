# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,646 tps; base rate 1,147 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,195 | 3,221 | +0.8% (-1.9 to +3.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,360 | 3,365 | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 33.2 | 15.5 | -53.3% (-342.9 to +236.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 581.2 | 536.0 | -7.8% (-47.4 to +31.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.601 | 0.601 | +0.0% (-1.4 to +1.4) | STEADY, the same |
| latency, mean (ms) | 18.8 | 16.3 | -13.0% (-66.0 to +40.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 26.3 | +31.3% (+14.2 to +48.3) | power given |
| server connections alive, most at once | 20.0 | 36.7 | +83.3% (+64.4 to +102.3) | power given |
| host CPU busy (share of the run) | 0.318 | 0.32 | +0.7% (+0.2 to +1.2) | power given |
| host CPU-seconds | 542.7 | 546.4 | +0.7% (+0.3 to +1.1) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.378 | 0.377 | -0.2% (-2.6 to +2.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.19 | 2.65 | +20.7% (+10.8 to +30.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 26.2 | +31.0% (+14.1 to +48.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 77, 56, 61; fail-ups per arm: 0, 1, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3149 / 79.9 / 20.0 / 20.0; omni 3213 / 18.2 / 27.8 / 27.8
- rep 2 (omni then native): native 3218 / 10.2 / 20.0 / 20.0; omni 3238 / 7.9 / 25.5 / 25.4
- rep 3 (native then omni): native 3218 / 9.5 / 20.0 / 20.0; omni 3212 / 20.4 / 25.5 / 25.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
