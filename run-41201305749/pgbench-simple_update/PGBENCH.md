# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,896 tps; base rate 584 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,680 | 1,685 | +0.3% (-2.8 to +3.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,714 | 1,713 | -0.1% (-0.2 to -0.0) | LOSS |
| latency, 95th percentile (ms, lag included) | 7.02 | 6.27 | -10.7% (-67.2 to +45.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 142.7 | 121.6 | -14.8% (-230.5 to +201.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.46 | 1.46 | -0.6% (-1.7 to +0.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.43 | 4.58 | -15.6% (-134.9 to +103.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 23.5 | +17.7% (+8.4 to +27.0) | power given |
| server connections alive, most at once | 20.0 | 35.7 | +78.3% (+49.6 to +107.0) | power given |
| host CPU busy (share of the run) | 0.414 | 0.414 | -0.1% (-0.8 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 709.6 | 708.8 | -0.1% (-1.0 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.939 | 0.935 | -0.4% (-4.3 to +3.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.41 | 3.21 | +33.2% (+28.5 to +37.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.5 | +17.7% (+8.5 to +27.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 31, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1696 / 5.9 / 20.0 / 20.0; omni 1682 / 6.4 / 22.9 / 22.9
- rep 2 (omni then native): native 1678 / 6.6 / 20.0 / 20.0; omni 1679 / 6.5 / 23.4 / 23.4
- rep 3 (native then omni): native 1667 / 8.5 / 20.0 / 20.0; omni 1694 / 5.9 / 24.4 / 24.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
