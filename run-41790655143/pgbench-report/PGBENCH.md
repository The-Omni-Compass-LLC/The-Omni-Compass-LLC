# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 23,832 tps; base rate 3,575 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 10,483 | 10,484 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 10,485 | 10,485 | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.6 | 0.58 | -3.3% (-16.8 to +10.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.37 | 1.16 | -15.2% (-65.5 to +35.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.234 | 0.234 | -0.1% (-0.8 to +0.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.327 | 0.297 | -9.3% (-49.6 to +31.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.389 | 0.389 | -0.1% (-1.3 to +1.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 676.4 | 675.3 | -0.2% (-1.4 to +1.1) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | -0.2% (-1.4 to +1.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.19 | 9.78 | +6.4% (+3.9 to +8.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 10482 / 0.6 / 20.0 / 20.0; omni 10483 / 0.6 / 20.0 / 20.0
- rep 2 (omni then native): native 10476 / 0.6 / 20.0 / 20.0; omni 10482 / 0.6 / 20.0 / 20.0
- rep 3 (native then omni): native 10489 / 0.6 / 20.0 / 20.0; omni 10488 / 0.6 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,081 tps; base rate 912 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,584 | 2,602 | +0.7% (-0.2 to +1.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,673 | 2,669 | -0.2% (-0.4 to +0.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.35 | 1.97 | -41.1% (-51.5 to -30.6) | GAIN |
| latency, 99th percentile (ms) | 458.7 | 304.6 | -33.6% (-59.3 to -7.9) | GAIN |
| latency, median (ms) | 0.665 | 0.659 | -0.9% (-5.4 to +3.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 12.2 | 7.9 | -35.5% (-60.3 to -10.7) | GAIN |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 25.2 | +25.9% (+17.5 to +34.3) | power given |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+58.5 to +101.5) | power given |
| host CPU busy (share of the run) | 0.292 | 0.292 | +0.1% (-5.5 to +5.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 499.6 | 500.3 | +0.1% (-5.6 to +5.8) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.43 | 0.427 | -0.6% (-6.4 to +5.2) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.01 | 2.56 | +27.0% (+22.6 to +31.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.2 | +25.8% (+17.3 to +34.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 51, 54, 48; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2592 / 3.6 / 20.0 / 20.0; omni 2605 / 2.1 / 24.9 / 24.9
- rep 2 (omni then native): native 2583 / 3.2 / 20.0 / 20.0; omni 2612 / 1.9 / 24.7 / 24.7
- rep 3 (native then omni): native 2576 / 3.2 / 20.0 / 20.0; omni 2589 / 2.0 / 25.9 / 25.9

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,058 tps; base rate 309 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 817.3 | 855.1 | +4.6% (-47.6 to +56.8) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 901.9 | 905.5 | +0.4% (-0.8 to +1.6) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 252.8 | 160.9 | -36.4% (-625.8 to +553.1) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 430.2 | 463.9 | +7.8% (-637.8 to +653.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.17 | 1.14 | -2.7% (-20.0 to +14.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 35.5 | 24.8 | -30.1% (-588.1 to +527.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 21.6 | +7.9% (-7.4 to +23.2) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 32.3 | +61.7% (+11.5 to +111.9) | power given |
| host CPU busy (share of the run) | 0.211 | 0.21 | -0.4% (-10.6 to +9.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 368.6 | 366.5 | -0.6% (-11.7 to +10.6) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.02 | 0.958 | -6.1% (-71.3 to +59.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.2 | 1.78 | +48.9% (+46.6 to +51.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 21.5 | +7.3% (-8.6 to +23.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 25, 9, 41; fail-ups per arm: 8, 0, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 889 / 12.2 / 20.0 / 20.0; omni 775 / 471.3 / 21.2 / 20.9
- rep 2 (omni then native): native 681 / 733.4 / 20.0 / 20.0; omni 905 / 2.5 / 20.6 / 20.6
- rep 3 (native then omni): native 882 / 12.8 / 20.0 / 20.0; omni 885 / 8.8 / 23.0 / 22.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
