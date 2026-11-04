# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,810 tps; base rate 2,371 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,955 | 6,953 | -0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 6,955 | 6,953 | -0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.949 | 0.928 | -2.2% (-7.6 to +3.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.93 | 1.81 | -6.1% (-24.3 to +12.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.348 | 0.345 | -0.8% (-2.8 to +1.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.448 | 0.441 | -1.6% (-4.6 to +1.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.384 | 0.382 | -0.6% (-2.1 to +0.9) | STEADY, no difference beyond the noise |
| host CPU-seconds | 652.9 | 649.4 | -0.5% (-2.0 to +0.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.209 | 0.208 | -0.5% (-1.7 to +0.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.19 | 8.9 | +8.8% (+7.1 to +10.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6954 / 1.0 / 20.0 / 20.0; omni 6961 / 1.0 / 20.0 / 20.0
- rep 2 (omni then native): native 6957 / 0.9 / 20.0 / 20.0; omni 6954 / 0.9 / 20.0 / 20.0
- rep 3 (native then omni): native 6954 / 0.9 / 20.0 / 20.0; omni 6945 / 0.9 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,562 tps; base rate 984 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,688 | 2,775 | +3.2% (-3.1 to +9.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,885 | 2,886 | +0.0% (-0.4 to +0.5) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 186.1 | 14.9 | -92.0% (-288.8 to +104.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,098 | 364.7 | -82.6% (-263.7 to +98.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.683 | 0.667 | -2.4% (-6.5 to +1.6) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 60.2 | 11.0 | -81.7% (-260.1 to +96.6) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 27.2 | +36.0% (+23.4 to +48.6) | power given |
| server connections alive, most at once | 20.0 | 38.0 | +90.0% (+68.5 to +111.5) | power given |
| host CPU busy (share of the run) | 0.311 | 0.308 | -0.9% (-5.4 to +3.6) | STEADY, no difference beyond the noise |
| host CPU-seconds | 532.9 | 527.3 | -1.0% (-6.0 to +3.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.441 | 0.422 | -4.2% (-15.2 to +6.9) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.13 | 2.65 | +24.5% (+19.9 to +29.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 27.2 | +36.1% (+23.5 to +48.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 69, 62, 69; fail-ups per arm: 0, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2639 / 284.9 / 20.0 / 20.0; omni 2767 / 23.7 / 26.7 / 26.7
- rep 2 (omni then native): native 2662 / 258.2 / 20.0 / 20.0; omni 2786 / 7.0 / 26.6 / 26.5
- rep 3 (native then omni): native 2764 / 15.1 / 20.0 / 20.0; omni 2771 / 14.1 / 28.4 / 28.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,166 tps; base rate 325 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 952.1 | 951.2 | -0.1% (-0.8 to +0.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 952.2 | 951.6 | -0.1% (-0.7 to +0.6) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.31 | 3.32 | +0.3% (-7.9 to +8.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.78 | -0.1% (-41.7 to +41.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.46 | 1.45 | -0.8% (-1.9 to +0.4) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.8 | 1.82 | +0.8% (-15.0 to +16.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.295 | 0.293 | -0.5% (-1.5 to +0.6) | STEADY, no difference beyond the noise |
| host CPU-seconds | 511.9 | 509.4 | -0.5% (-1.5 to +0.6) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.19 | 1.19 | -0.4% (-1.6 to +0.8) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.6 | 2.3 | +44.0% (+40.9 to +47.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 953 / 3.2 / 20.0 / 20.0; omni 950 / 3.2 / 20.0 / 20.0
- rep 2 (omni then native): native 949 / 3.3 / 20.0 / 20.0; omni 951 / 3.4 / 20.0 / 20.0
- rep 3 (native then omni): native 955 / 3.4 / 20.0 / 20.0; omni 952 / 3.3 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
