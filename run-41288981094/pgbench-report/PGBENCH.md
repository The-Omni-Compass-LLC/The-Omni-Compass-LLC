# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 37,629 tps; base rate 5,644 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,552 | 16,550 | -0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 16,552 | 16,550 | -0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.309 | 0.293 | -5.2% (-31.1 to +20.7) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.81 | 1.12 | -38.1% (-288.1 to +211.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.146 | 0.145 | -0.7% (-4.1 to +2.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.203 | -10.8% (-91.9 to +70.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.343 | 0.34 | -0.9% (-6.0 to +4.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 591.3 | 585.5 | -1.0% (-6.2 to +4.3) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0794 | 0.0786 | -1.0% (-6.1 to +4.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.99 | 10.5 | +5.2% (-1.0 to +11.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16550 / 0.3 / 20.0 / 20.0; omni 16541 / 0.3 / 20.0 / 20.0
- rep 2 (omni then native): native 16557 / 0.3 / 20.0 / 20.0; omni 16551 / 0.3 / 20.0 / 20.0
- rep 3 (native then omni): native 16548 / 0.3 / 20.0 / 20.0; omni 16559 / 0.3 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,895 tps; base rate 584 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,683 | 1,683 | -0.1% (-0.9 to +0.8) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,712 | 1,714 | +0.1% (-0.2 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.77 | 4.97 | +4.3% (-9.0 to +17.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 133.1 | 132.6 | -0.3% (-46.2 to +45.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.37 | 1.36 | -0.6% (-4.1 to +2.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.45 | 4.52 | +1.6% (-30.8 to +33.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.6 | +17.9% (+7.2 to +28.6) | power given |
| server connections alive, most at once | 20.0 | 34.3 | +71.7% (+43.0 to +100.4) | power given |
| host CPU busy (share of the run) | 0.404 | 0.403 | -0.2% (-2.6 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 691.7 | 690.4 | -0.2% (-2.6 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.913 | 0.912 | -0.1% (-1.7 to +1.4) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.41 | 3.18 | +32.1% (+27.6 to +36.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.7 | +18.5% (+9.9 to +27.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 31, 39; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1686 / 4.8 / 20.0 / 20.0; omni 1678 / 5.0 / 22.7 / 23.1
- rep 2 (omni then native): native 1681 / 4.8 / 20.0 / 20.0; omni 1683 / 5.3 / 23.6 / 23.6
- rep 3 (native then omni): native 1683 / 4.7 / 20.0 / 20.0; omni 1686 / 4.6 / 24.4 / 24.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,963 tps; base rate 294 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `507f8c2251ae`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 861.3 | 863.1 | +0.2% (-0.9 to +1.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 863.2 | 864.7 | +0.2% (-0.4 to +0.7) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.53 | 5.78 | -11.6% (-34.4 to +11.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 21.3 | 18.2 | -14.6% (-28.4 to -0.8) | GAIN |
| latency, median (ms) | 1.85 | 1.83 | -0.9% (-5.6 to +3.8) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.92 | 2.69 | -7.8% (-24.9 to +9.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | +0.7% (-2.4 to +3.8) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-33.0 to +53.0) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.312 | 0.31 | -0.8% (-4.8 to +3.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 537.2 | 532.9 | -0.8% (-4.6 to +3.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.39 | 1.37 | -1.0% (-5.5 to +3.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.52 | 2.18 | +44.2% (+35.9 to +52.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.7% (-2.4 to +3.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 7, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 861 / 4.5 / 20.0 / 20.0; omni 865 / 4.4 / 20.0 / 20.0
- rep 2 (omni then native): native 860 / 7.3 / 20.0 / 20.0; omni 864 / 6.5 / 20.4 / 20.4
- rep 3 (native then omni): native 862 / 7.8 / 20.0 / 20.0; omni 860 / 6.4 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
