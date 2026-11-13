# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 40,145 tps; base rate 6,022 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,664 | 17,665 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 17,664 | 17,665 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.361 | 0.342 | -5.3% (-73.6 to +63.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.21 | 1.81 | -18.4% (-167.8 to +131.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.15 | 0.151 | +0.4% (-6.2 to +7.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.243 | 0.252 | +3.7% (-46.2 to +53.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 18.0 | -8.3% (-18.9 to +2.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.365 | 0.368 | +0.7% (-6.0 to +7.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 621.8 | 626.3 | +0.7% (-6.2 to +7.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0782 | 0.0788 | +0.7% (-6.3 to +7.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.06 | 3.55 | +16.2% (+4.1 to +28.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -8.9% (-27.1 to +9.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 59, 40; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17659 / 0.5 / 20.0 / 20.0; omni 17665 / 0.3 / 18.9 / 19.1
- rep 2 (omni then native): native 17665 / 0.3 / 18.9 / 20.0; omni 17669 / 0.3 / 16.3 / 16.5
- rep 3 (native then omni): native 17667 / 0.3 / 20.0 / 20.0; omni 17661 / 0.4 / 18.9 / 19.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,614 tps; base rate 992 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,764 | 2,779 | +0.5% (-3.9 to +4.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,908 | 2,911 | +0.1% (-0.1 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 33.0 | 36.0 | +8.9% (-536.0 to +553.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 627.7 | 593.8 | -5.4% (-13.2 to +2.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.974 | 0.984 | +1.0% (-7.6 to +9.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 20.2 | 19.2 | -5.1% (-57.7 to +47.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.0 | -9.8% (-14.8 to -4.8) | GAIN |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (+4.5 to +18.8) | power given |
| host CPU busy (share of the run) | 0.361 | 0.368 | +1.9% (-4.8 to +8.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 626.1 | 637.4 | +1.8% (-4.8 to +8.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.504 | 0.51 | +1.2% (-9.6 to +12.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.874 | 1.41 | +61.1% (+40.0 to +82.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -8.8% (-13.6 to -4.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 93, 96, 87; fail-ups per arm: 4, 5, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2730 / 72.2 / 20.0 / 20.0; omni 2793 / 9.7 / 18.2 / 18.5
- rep 2 (omni then native): native 2783 / 11.7 / 19.8 / 20.0; omni 2748 / 92.5 / 18.1 / 18.4
- rep 3 (native then omni): native 2778 / 15.2 / 20.0 / 20.0; omni 2795 / 5.7 / 17.6 / 17.8

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,755 tps; base rate 263 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 770.7 | 772.2 | +0.2% (-0.9 to +1.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 772.2 | 772.5 | +0.0% (-1.0 to +1.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.27 | 2.19 | -3.5% (-21.4 to +14.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.99 | 3.18 | -60.2% (-324.9 to +204.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.27 | 1.26 | -0.2% (-1.4 to +1.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.66 | 1.43 | -13.7% (-89.2 to +61.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 18.5 | 12.5 | -32.2% (-52.2 to -12.2) | GAIN |
| server connections alive, most at once | 20.0 | 19.7 | -1.7% (-8.8 to +5.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.175 | 0.175 | -0.2% (-2.5 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 309.3 | 308.8 | -0.2% (-2.5 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.892 | 0.889 | -0.4% (-3.1 to +2.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.553 | 1.05 | +89.3% (+78.0 to +100.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 13.7 | -31.4% (-60.8 to -2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 26, 46, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 767 / 2.5 / 20.0 / 20.0; omni 769 / 2.2 / 13.5 / 13.6
- rep 2 (omni then native): native 774 / 2.2 / 15.4 / 20.0; omni 771 / 2.2 / 8.3 / 11.4
- rep 3 (native then omni): native 772 / 2.2 / 20.0 / 20.0; omni 776 / 2.2 / 15.7 / 16.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
