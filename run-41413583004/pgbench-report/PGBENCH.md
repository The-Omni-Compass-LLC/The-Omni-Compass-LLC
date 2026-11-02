# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 23,339 tps; base rate 3,501 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 10,268 | 10,269 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 10,268 | 10,269 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.595 | 0.588 | -1.2% (-18.6 to +16.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.29 | 1.15 | -10.7% (-98.9 to +77.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.254 | 0.254 | +0.0% (-1.0 to +1.0) | STEADY, the same |
| latency, mean (ms) | 0.315 | 0.312 | -1.1% (-22.7 to +20.6) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.391 | 0.39 | -0.3% (-2.4 to +1.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 667.5 | 664.3 | -0.5% (-4.1 to +3.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.144 | -0.5% (-4.1 to +3.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.22 | 9.85 | +6.8% (+3.5 to +10.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 10271 / 0.6 / 20.0 / 20.0; omni 10269 / 0.6 / 20.0 / 20.0
- rep 2 (omni then native): native 10273 / 0.6 / 20.0 / 20.0; omni 10270 / 0.6 / 20.0 / 20.0
- rep 3 (native then omni): native 10260 / 0.6 / 20.0 / 20.0; omni 10267 / 0.6 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,568 tps; base rate 985 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,787 | 2,796 | +0.3% (-1.3 to +1.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,886 | 2,887 | +0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.7 | 3.5 | -47.7% (-285.6 to +190.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 453.2 | 389.0 | -14.2% (-56.0 to +27.6) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.665 | 0.673 | +1.3% (-2.8 to +5.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 12.3 | 10.6 | -14.5% (-70.0 to +41.0) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 25.3 | +26.6% (+18.7 to +34.5) | power given |
| server connections alive, most at once | 20.0 | 37.0 | +85.0% (+85.0 to +85.0) | power given |
| host CPU busy (share of the run) | 0.307 | 0.312 | +1.6% (-2.7 to +6.0) | STEADY, no difference beyond the noise |
| host CPU-seconds | 526.6 | 534.9 | +1.6% (-2.8 to +5.9) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.42 | 0.425 | +1.3% (-2.8 to +5.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.13 | 2.67 | +25.1% (+17.2 to +32.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.3 | +26.5% (+18.3 to +34.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 49, 32, 48; fail-ups per arm: 0, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2766 / 13.8 / 20.0 / 20.0; omni 2793 / 3.2 / 25.4 / 25.4
- rep 2 (omni then native): native 2792 / 3.4 / 20.0 / 20.0; omni 2801 / 3.4 / 24.6 / 24.6
- rep 3 (native then omni): native 2803 / 2.9 / 20.0 / 20.0; omni 2793 / 3.9 / 25.9 / 25.9

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,007 tps; base rate 301 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `abbf5f0857b3`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 882.2 | 883.1 | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 882.2 | 883.1 | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.32 | 4.46 | +3.3% (-4.5 to +11.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.08 | 10.0 | +10.5% (-9.4 to +30.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.71 | 1.72 | +0.3% (-0.5 to +1.1) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.17 | 2.22 | +2.4% (-2.0 to +6.8) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.303 | 0.303 | +0.2% (-0.3 to +0.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 521.1 | 522.4 | +0.2% (-0.3 to +0.7) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.31 | 1.31 | +0.1% (-0.5 to +0.8) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.5 | 2.14 | +43.2% (+42.3 to +44.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 882 / 4.4 / 20.0 / 20.0; omni 884 / 4.4 / 20.0 / 20.0
- rep 2 (omni then native): native 881 / 4.4 / 20.0 / 20.0; omni 882 / 4.5 / 20.0 / 20.0
- rep 3 (native then omni): native 883 / 4.2 / 20.0 / 20.0; omni 884 / 4.5 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
