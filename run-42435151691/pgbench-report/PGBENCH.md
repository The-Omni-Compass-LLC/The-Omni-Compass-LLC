# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,712 tps; base rate 2,357 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,915 | 6,912 | -0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 6,915 | 6,912 | -0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.901 | 0.897 | -0.5% (-6.5 to +5.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.74 | 1.69 | -3.2% (-22.8 to +16.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.344 | 0.345 | +0.1% (-0.3 to +0.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.441 | 0.435 | -1.4% (-8.6 to +5.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.38 | 0.38 | +0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise |
| host CPU-seconds | 645.1 | 645.0 | -0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.207 | 0.207 | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.15 | 8.85 | +8.7% (+6.2 to +11.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6920 / 0.9 / 20.0 / 20.0; omni 6910 / 0.9 / 20.0 / 20.0
- rep 2 (omni then native): native 6914 / 0.9 / 20.0 / 20.0; omni 6912 / 0.9 / 20.0 / 20.0
- rep 3 (native then omni): native 6910 / 0.9 / 20.0 / 20.0; omni 6916 / 0.9 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,427 tps; base rate 1,114 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,103 | 3,074 | -0.9% (-4.3 to +2.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,262 | 3,265 | +0.1% (-0.4 to +0.6) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 46.3 | 76.6 | +65.4% (-121.3 to +252.1) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 529.2 | 525.0 | -0.8% (-14.1 to +12.6) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.651 | 0.664 | +2.0% (-4.3 to +8.4) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 16.6 | 19.0 | +14.4% (-27.4 to +56.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 28.3 | +41.3% (+25.5 to +57.1) | power given |
| server connections alive, most at once | 20.0 | 37.0 | +85.0% (+85.0 to +85.0) | power given |
| host CPU busy (share of the run) | 0.328 | 0.334 | +1.9% (-1.3 to +5.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 560.7 | 571.2 | +1.9% (-1.2 to +4.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.402 | 0.413 | +2.8% (-1.4 to +7.0) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.27 | 2.85 | +25.3% (+18.9 to +31.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 28.2 | +41.2% (+25.5 to +56.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 88, 80, 74; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3100 / 45.8 / 20.0 / 20.0; omni 3101 / 55.5 / 29.2 / 29.1
- rep 2 (omni then native): native 3105 / 46.2 / 20.0 / 20.0; omni 3027 / 116.6 / 28.8 / 28.7
- rep 3 (native then omni): native 3104 / 46.9 / 20.0 / 20.0; omni 3095 / 57.6 / 26.8 / 26.8

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,931 tps; base rate 290 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `bf9868379271`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 850.7 | 848.8 | -0.2% (-0.6 to +0.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 850.7 | 850.0 | -0.1% (-0.5 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.26 | 4.31 | +1.3% (-4.1 to +6.7) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.17 | 8.78 | +7.3% (-28.1 to +42.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.76 | 1.76 | +0.2% (-0.3 to +0.6) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.18 | 2.31 | +6.0% (-19.3 to +31.3) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.2 | +0.9% (-2.8 to +4.5) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (-38.5 to +61.9) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.296 | 0.297 | +0.2% (-0.1 to +0.5) | STEADY, no difference beyond the noise |
| host CPU-seconds | 510.1 | 511.1 | +0.2% (-0.2 to +0.6) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.34 | +0.4% (+0.1 to +0.8) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.46 | 2.11 | +44.7% (+42.3 to +47.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.2 | +0.9% (-2.8 to +4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 8, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 852 / 4.3 / 20.0 / 20.0; omni 849 / 4.4 / 20.5 / 20.5
- rep 2 (omni then native): native 850 / 4.3 / 20.0 / 20.0; omni 848 / 4.2 / 20.0 / 20.0
- rep 3 (native then omni): native 850 / 4.2 / 20.0 / 20.0; omni 850 / 4.3 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
