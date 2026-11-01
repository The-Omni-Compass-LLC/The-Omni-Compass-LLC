# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,263 tps; base rate 340 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 639.6 | 535.6 | -16.3% (-106.3 to +73.8) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 963.1 | 949.1 | -1.5% (-23.3 to +20.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3,368 | 3,939 | +16.9% (-552.0 to +585.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5,043 | 5,674 | +12.5% (-341.8 to +366.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 11.3 | 28.9 | +155.5% (-940.9 to +1251.8) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 640.8 | 612.3 | -4.4% (-509.0 to +500.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 21.7 | +8.7% (-3.9 to +21.3) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 35.0 | +75.0% (+9.3 to +140.7) | power given |
| host CPU busy (share of the run) | 0.24 | 0.249 | +4.0% (-8.2 to +16.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 420.8 | 439.1 | +4.3% (-7.2 to +15.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.86 | +22.7% (-80.2 to +125.6) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.24 | 1.86 | +50.7% (+35.7 to +65.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 21.0 | +4.8% (-4.3 to +14.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 50, 56, 24; fail-ups per arm: 21, 21, 11.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 472 / 8308.2 / 20.0 / 20.0; omni 612 / 662.9 / 21.1 / 20.7
- rep 2 (omni then native): native 703 / 816.1 / 20.0 / 20.0; omni 571 / 2514.0 / 22.9 / 21.8
- rep 3 (native then omni): native 744 / 980.2 / 20.0 / 20.0; omni 423 / 8638.9 / 21.2 / 20.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
