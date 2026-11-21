# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,530 tps; base rate 3,979 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,668 | 11,671 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,668 | 11,671 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.38 | +10.2% (-50.4 to +70.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.84 | 3.32 | +16.8% (-45.6 to +79.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.273 | 0.273 | +0.0% (-5.5 to +5.5) | EVEN, the same |
| latency, mean (ms) | 0.444 | 0.476 | +7.1% (-26.5 to +40.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.0 | -9.1% (-26.7 to +8.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.458 | 0.458 | -0.0% (-2.3 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 795.7 | 795.1 | -0.1% (-2.4 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.151 | -0.1% (-2.4 to +2.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.67 | 4.27 | +16.3% (+12.0 to +20.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | -9.6% (-25.3 to +6.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 30, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11666 / 1.2 / 20.0 / 20.0; omni 11672 / 1.7 / 18.9 / 19.1
- rep 2 (omni then native): native 11673 / 1.2 / 19.2 / 20.0; omni 11666 / 1.1 / 18.4 / 18.5
- rep 3 (native then omni): native 11664 / 1.3 / 20.0 / 20.0; omni 11675 / 1.3 / 16.6 / 16.7

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,818 tps; base rate 873 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,354 | 2,360 | +0.3% (-3.0 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,556 | 2,557 | +0.0% (-0.8 to +0.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 301.0 | 362.1 | +20.3% (-58.8 to +99.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 930.4 | 951.4 | +2.3% (-25.8 to +30.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.18 | 1.17 | -0.7% (-1.8 to +0.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 40.4 | 43.0 | +6.4% (-39.8 to +52.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | -3.0% (-8.2 to +2.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.391 | 0.392 | +0.3% (-1.3 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 676.8 | 678.9 | +0.3% (-1.2 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.639 | 0.639 | +0.0% (-3.0 to +3.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.6 | +58.0% (+51.2 to +64.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.6% (-7.8 to +2.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 42, 41; fail-ups per arm: 4, 6, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2316 / 331.6 / 20.0 / 20.0; omni 2350 / 435.3 / 19.8 / 19.8
- rep 2 (omni then native): native 2353 / 356.4 / 20.0 / 20.0; omni 2365 / 307.8 / 19.0 / 19.0
- rep 3 (native then omni): native 2392 / 215.0 / 20.0 / 20.0; omni 2365 / 343.2 / 19.4 / 19.6

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,424 tps; base rate 364 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 719.6 | 734.4 | +2.1% (-55.3 to +59.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,048 | 1,049 | +0.1% (-4.5 to +4.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,036 | 2,394 | +17.6% (-69.0 to +104.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3,305 | 3,351 | +1.4% (-73.8 to +76.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 7.96 | 5.15 | -35.4% (-479.2 to +408.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 357.4 | 319.7 | -10.5% (-82.2 to +61.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-0.4 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.262 | 0.261 | -0.4% (-5.7 to +4.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 457.4 | 455.6 | -0.4% (-6.4 to +5.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.49 | 1.41 | -5.6% (-65.0 to +53.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.646 | 1.21 | +87.6% (+79.4 to +95.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-0.5 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 24, 2; fail-ups per arm: 6, 4, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 963 / 131.0 / 20.0 / 20.0; omni 833 / 349.8 / 20.0 / 20.0
- rep 2 (omni then native): native 576 / 2680.2 / 20.0 / 20.0; omni 772 / 3807.7 / 20.0 / 19.9
- rep 3 (native then omni): native 620 / 3295.5 / 20.0 / 20.0; omni 598 / 3024.5 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
