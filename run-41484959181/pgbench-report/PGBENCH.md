# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 36,539 tps; base rate 5,481 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,075 | 16,075 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 16,075 | 16,075 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.283 | 0.294 | +3.8% (-0.6 to +8.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.926 | 1.08 | +16.5% (+12.2 to +20.8) | LOSS |
| latency, median (ms) | 0.144 | 0.145 | +0.9% (-1.1 to +2.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.203 | +8.2% (+3.3 to +13.1) | LOSS |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.33 | 0.334 | +1.1% (+0.7 to +1.4) | power given |
| host CPU-seconds | 569.9 | 576.0 | +1.1% (+0.7 to +1.4) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.0788 | 0.0796 | +1.1% (+0.6 to +1.5) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.74 | 10.4 | +6.5% (+4.3 to +8.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16079 / 0.3 / 20.0 / 20.0; omni 16075 / 0.3 / 20.0 / 20.0
- rep 2 (omni then native): native 16069 / 0.3 / 20.0 / 20.0; omni 16065 / 0.3 / 20.0 / 20.0
- rep 3 (native then omni): native 16076 / 0.3 / 20.0 / 20.0; omni 16086 / 0.3 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,871 tps; base rate 581 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,672 | 1,670 | -0.1% (-1.7 to +1.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,701 | 1,703 | +0.1% (-0.6 to +0.7) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.01 | 6.11 | +1.6% (-14.7 to +17.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 131.2 | 147.5 | +12.4% (-145.4 to +170.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.46 | 1.45 | -0.9% (-2.8 to +1.1) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.73 | 4.98 | +5.3% (-79.0 to +89.6) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 24.1 | +20.3% (+19.6 to +21.0) | power given |
| server connections alive, most at once | 20.0 | 35.7 | +78.3% (+49.6 to +107.0) | power given |
| host CPU busy (share of the run) | 0.417 | 0.416 | -0.2% (-1.6 to +1.1) | STEADY, no difference beyond the noise |
| host CPU-seconds | 713.9 | 712.3 | -0.2% (-1.6 to +1.1) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.949 | 0.948 | -0.1% (-2.7 to +2.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.46 | 3.23 | +31.6% (+28.0 to +35.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.2 | +20.9% (+18.9 to +23.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 43, 40, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1681 / 6.3 / 20.0 / 20.0; omni 1669 / 6.7 / 24.0 / 24.4
- rep 2 (omni then native): native 1664 / 6.0 / 20.0 / 20.0; omni 1673 / 6.2 / 24.0 / 24.0
- rep 3 (native then omni): native 1671 / 5.8 / 20.0 / 20.0; omni 1669 / 5.4 / 24.1 / 24.1

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,956 tps; base rate 293 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 859.9 | 859.9 | +0.0% (-0.5 to +0.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 859.9 | 860.0 | +0.0% (-0.4 to +0.5) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.83 | 4.94 | +2.3% (-10.6 to +15.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 10.7 | +5.9% (-32.4 to +44.1) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.79 | 1.81 | +0.7% (-1.0 to +2.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.33 | 2.37 | +2.0% (-5.1 to +9.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.301 | 0.303 | +0.7% (+0.1 to +1.3) | power given |
| host CPU-seconds | 518.8 | 522.2 | +0.6% (+0.1 to +1.2) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.35 | +0.6% (-0.3 to +1.6) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.49 | 2.17 | +45.5% (+42.2 to +48.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 860 / 4.8 / 20.0 / 20.0; omni 859 / 5.2 / 20.0 / 20.0
- rep 2 (omni then native): native 861 / 5.0 / 20.0 / 20.0; omni 860 / 5.0 / 20.0 / 20.0
- rep 3 (native then omni): native 859 / 4.7 / 20.0 / 20.0; omni 861 / 4.6 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
