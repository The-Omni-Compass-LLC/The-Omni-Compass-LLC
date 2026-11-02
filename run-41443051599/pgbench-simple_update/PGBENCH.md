# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,680 tps; base rate 852 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `19cdd5c920e3`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,388 | 2,411 | +1.0% (-0.4 to +2.4) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,499 | 2,499 | -0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 27.4 | 7.87 | -71.2% (-237.0 to +94.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 444.9 | 425.5 | -4.4% (-65.8 to +57.1) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.994 | 1.02 | +2.7% (-8.0 to +13.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 13.9 | 11.8 | -14.7% (-59.3 to +30.0) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 24.3 | +21.5% (+9.7 to +33.4) | power given |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+67.6 to +92.4) | power given |
| host CPU busy (share of the run) | 0.36 | 0.37 | +2.8% (-5.4 to +11.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 630.4 | 647.9 | +2.8% (-5.5 to +11.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.587 | 0.597 | +1.8% (-7.1 to +10.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.7 | 3.31 | +22.7% (+18.6 to +26.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.3 | +21.6% (+9.6 to +33.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 37, 54; fail-ups per arm: 0, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2374 / 48.8 / 20.0 / 20.0; omni 2412 / 10.5 / 24.7 / 24.7
- rep 2 (omni then native): native 2404 / 8.7 / 20.0 / 20.0; omni 2416 / 6.9 / 23.2 / 23.2
- rep 3 (native then omni): native 2387 / 24.5 / 20.0 / 20.0; omni 2406 / 6.2 / 25.0 / 25.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
