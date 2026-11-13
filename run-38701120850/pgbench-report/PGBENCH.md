# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,863 tps; base rate 2,379 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,979 | 6,982 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 6,979 | 6,982 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.16 | 1.11 | -3.5% (-18.6 to +11.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.03 | 2.86 | -5.6% (-80.5 to +69.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.37 | 0.367 | -0.6% (-2.0 to +0.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.521 | 0.506 | -2.9% (-20.4 to +14.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.7 | -5.7% (-7.5 to -4.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.313 | 0.311 | -0.6% (-2.6 to +1.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 462.8 | 459.5 | -0.7% (-3.0 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.146 | -0.8% (-3.1 to +1.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.34 | +29.5% (+27.1 to +31.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.7% (-4.9 to -4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 27, 33; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6977 / 1.2 / 20.0 / 20.0; omni 6980 / 1.1 / 18.9 / 19.1
- rep 2 (omni then native): native 6976 / 1.1 / 19.6 / 20.0; omni 6985 / 1.1 / 18.6 / 19.0
- rep 3 (native then omni): native 6982 / 1.2 / 20.0 / 20.0; omni 6981 / 1.2 / 18.7 / 19.1

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,697 tps; base rate 855 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,446 | 2,433 | -0.5% (-2.3 to +1.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,509 | 2,501 | -0.3% (-0.4 to -0.2) | LOSS |
| latency, 95th percentile (ms, lag included) | 4.97 | 5.16 | +3.9% (-13.4 to +21.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 177.3 | 199.0 | +12.3% (-28.6 to +53.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.08 | 1.09 | +0.6% (-0.4 to +1.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.58 | 6.31 | +13.0% (-53.9 to +79.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.3 | -8.5% (-19.4 to +2.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.43 | 0.431 | +0.1% (-0.2 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 745.6 | 746.7 | +0.1% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.677 | 0.682 | +0.7% (-1.6 to +3.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.1 | 1.74 | +58.0% (+53.8 to +62.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.1% (-18.7 to +4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 58, 51, 72; fail-ups per arm: 0, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2458 / 5.2 / 20.0 / 20.0; omni 2433 / 5.6 / 18.6 / 18.9
- rep 2 (omni then native): native 2442 / 4.8 / 20.0 / 20.0; omni 2421 / 5.2 / 19.0 / 19.3
- rep 3 (native then omni): native 2438 / 4.9 / 20.0 / 20.0; omni 2445 / 4.7 / 17.3 / 17.5

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,916 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 841.9 | 842.8 | +0.1% (+0.1 to +0.1) | GAIN |
| throughput (transactions a second) | 842.1 | 842.9 | +0.1% (+0.1 to +0.1) | GAIN |
| latency, 95th percentile (ms, lag included) | 5.06 | 5.02 | -0.7% (-8.9 to +7.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.8 | 11.5 | -2.8% (-50.8 to +45.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.9 | 1.9 | -0.1% (-1.6 to +1.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.48 | 2.47 | -0.7% (-6.2 to +4.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.5 | -11.3% (-17.5 to -5.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.239 | 0.239 | -0.1% (-0.8 to +0.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 373.0 | 372.4 | -0.2% (-0.7 to +0.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.985 | 0.982 | -0.3% (-0.8 to +0.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.768 | 1.52 | +97.4% (+94.3 to +100.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.1% (-15.6 to +1.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 26, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 842 / 5.2 / 20.0 / 20.0; omni 843 / 5.1 / 17.4 / 17.8
- rep 2 (omni then native): native 842 / 4.9 / 19.2 / 20.0; omni 843 / 4.8 / 16.8 / 19.0
- rep 3 (native then omni): native 842 / 5.0 / 20.0 / 20.0; omni 843 / 5.2 / 18.3 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
