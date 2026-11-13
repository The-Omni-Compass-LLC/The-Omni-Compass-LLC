# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,559 tps; base rate 5,934 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,403 | 17,405 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 17,403 | 17,406 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.373 | 0.622 | +66.9% (-220.4 to +354.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.9 | 3.91 | +105.5% (-211.4 to +422.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.153 | 0.156 | +2.0% (-3.7 to +7.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.341 | +45.2% (-55.3 to +145.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 16.6 | -15.4% (-37.3 to +6.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.37 | 0.377 | +2.0% (-4.1 to +8.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 629.8 | 642.3 | +2.0% (-4.3 to +8.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0804 | 0.082 | +2.0% (-4.2 to +8.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.14 | 3.73 | +19.0% (+11.0 to +27.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.1 | -14.6% (-38.2 to +8.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 42, 79, 47; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17403 / 0.4 / 20.0 / 20.0; omni 17410 / 0.4 / 17.7 / 17.9
- rep 2 (omni then native): native 17410 / 0.4 / 18.9 / 20.0; omni 17399 / 0.4 / 13.9 / 14.9
- rep 3 (native then omni): native 17397 / 0.3 / 20.0 / 20.0; omni 17407 / 1.1 / 18.2 / 18.4

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,842 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,645 | 1,649 | +0.2% (-3.0 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,690 | 1,690 | +0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.16 | 7.98 | +11.5% (-52.6 to +75.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 199.9 | 187.5 | -6.2% (-68.7 to +56.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.54 | 1.57 | +1.8% (-0.4 to +4.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.8 | 6.54 | -3.8% (-78.5 to +70.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.4% (-6.5 to -2.2) | GAIN |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.343 | 0.35 | +2.0% (-0.4 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 516.3 | 528.5 | +2.4% (-0.6 to +5.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.697 | 0.712 | +2.2% (-3.6 to +7.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.86 | +81.6% (+79.1 to +84.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -3.1% (-5.0 to -1.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 51, 52, 51; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1652 / 7.2 / 20.0 / 20.0; omni 1637 / 9.6 / 19.3 / 19.5
- rep 2 (omni then native): native 1649 / 6.6 / 20.0 / 20.0; omni 1648 / 7.8 / 19.2 / 19.4
- rep 3 (native then omni): native 1634 / 7.7 / 20.0 / 20.0; omni 1661 / 6.5 / 18.9 / 19.2

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,824 tps; base rate 274 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 802.5 | 802.4 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 802.8 | 802.6 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.58 | 6.02 | +7.8% (-19.0 to +34.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 14.7 | +12.0% (-50.5 to +74.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.9 | 1.9 | +0.4% (-2.0 to +2.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.57 | 2.64 | +2.7% (-14.5 to +19.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.6 | -11.2% (-24.0 to +1.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.221 | 0.223 | +0.9% (-3.4 to +5.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 346.0 | 349.3 | +0.9% (-3.5 to +5.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.958 | 0.967 | +0.9% (-3.2 to +5.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.756 | 1.49 | +97.6% (+95.4 to +99.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.5% (-23.4 to +6.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 27, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 804 / 5.9 / 20.0 / 20.0; omni 802 / 5.8 / 16.6 / 16.9
- rep 2 (omni then native): native 803 / 5.5 / 19.4 / 20.0; omni 803 / 6.5 / 17.5 / 19.0
- rep 3 (native then omni): native 801 / 5.4 / 20.0 / 20.0; omni 802 / 5.7 / 18.6 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
