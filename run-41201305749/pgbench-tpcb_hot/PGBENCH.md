# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,666 tps; base rate 250 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 552.4 | 502.7 | -9.0% (-13.8 to -4.2) | LOSS |
| throughput (transactions a second) | 732.6 | 724.1 | -1.2% (-4.8 to +2.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 809.2 | 1,858 | +129.6% (-574.3 to +833.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,557 | 3,523 | +126.3% (-333.2 to +585.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 2.94 | 6.33 | +115.4% (-359.5 to +590.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 117.8 | 310.1 | +163.4% (-505.0 to +831.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.9 | +4.7% (-3.6 to +13.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 34.0 | +70.0% (-11.5 to +151.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.177 | 0.179 | +1.5% (-8.8 to +11.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 310.8 | 315.9 | +1.7% (-8.6 to +11.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.28 | 1.43 | +11.8% (+5.3 to +18.3) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.04 | 1.61 | +54.4% (+46.8 to +61.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.7 | +3.3% (-2.6 to +9.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 16, 31, 37; fail-ups per arm: 8, 14, 15.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 452 / 695.5 / 20.0 / 20.0; omni 399 / 4310.6 / 20.2 / 20.1
- rep 2 (omni then native): native 594 / 359.1 / 20.0 / 20.0; omni 556 / 686.4 / 21.5 / 21.0
- rep 3 (native then omni): native 612 / 1372.9 / 20.0 / 20.0; omni 553 / 576.5 / 21.2 / 20.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
