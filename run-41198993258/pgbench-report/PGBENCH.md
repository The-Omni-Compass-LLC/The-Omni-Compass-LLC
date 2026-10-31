# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 33,499 tps; base rate 5,025 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 14,734 | 14,735 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 14,734 | 14,735 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.722 | 0.698 | -3.3% (-14.3 to +7.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.34 | 2.25 | -3.9% (-7.1 to -0.6) | GAIN |
| latency, median (ms) | 0.213 | 0.213 | -0.2% (-1.9 to +1.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.315 | 0.31 | -1.5% (-5.1 to +2.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.427 | 0.426 | -0.1% (-1.1 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 760.1 | 759.9 | -0.0% (-1.0 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.115 | 0.115 | -0.0% (-1.0 to +0.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 13.6 | 14.3 | +5.7% (+1.4 to +10.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 14741 / 0.7 / 20.0 / 20.0; omni 14737 / 0.7 / 20.0 / 20.0
- rep 2 (omni then native): native 14728 / 0.8 / 20.0 / 20.0; omni 14736 / 0.8 / 20.0 / 20.0
- rep 3 (native then omni): native 14733 / 0.7 / 20.0 / 20.0; omni 14732 / 0.6 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,849 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,663 | 1,665 | +0.1% (-2.9 to +3.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,693 | 1,691 | -0.1% (-0.7 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.7 | 5.72 | +0.4% (-30.1 to +30.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 128.3 | 110.0 | -14.3% (-195.6 to +167.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.45 | 1.45 | +0.5% (-0.1 to +1.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.73 | 4.33 | -8.5% (-98.7 to +81.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 23.4 | +17.2% (+7.5 to +26.9) | power given |
| server connections alive, most at once | 20.0 | 34.3 | +71.7% (+43.0 to +100.4) | power given |
| host CPU busy (share of the run) | 0.409 | 0.411 | +0.4% (-0.3 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 701.0 | 703.5 | +0.4% (-0.2 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.937 | 0.939 | +0.2% (-2.5 to +3.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.41 | 3.15 | +31.0% (+29.9 to +32.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.4 | +17.2% (+7.4 to +26.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 30, 36, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1675 / 5.6 / 20.0 / 20.0; omni 1658 / 6.3 / 23.0 / 22.9
- rep 2 (omni then native): native 1661 / 5.8 / 20.0 / 20.0; omni 1662 / 5.8 / 24.3 / 24.3
- rep 3 (native then omni): native 1652 / 5.8 / 20.0 / 20.0; omni 1675 / 5.1 / 23.0 / 23.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,959 tps; base rate 294 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 860.9 | 862.1 | +0.1% (-0.3 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 861.2 | 862.4 | +0.1% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.66 | 5.27 | -6.8% (-22.9 to +9.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.1 | 12.0 | -20.2% (-71.4 to +31.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.87 | 1.86 | -0.7% (-6.9 to +5.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.6 | 2.48 | -4.3% (-19.7 to +11.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.314 | 0.312 | -0.4% (-5.3 to +4.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 539.8 | 537.7 | -0.4% (-5.3 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.39 | 1.39 | -0.5% (-5.3 to +4.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.52 | 2.2 | +44.7% (+42.7 to +46.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 863 / 5.5 / 20.0 / 20.0; omni 864 / 5.4 / 20.0 / 20.0
- rep 2 (omni then native): native 862 / 6.2 / 20.0 / 20.0; omni 862 / 5.4 / 20.0 / 20.0
- rep 3 (native then omni): native 858 / 5.3 / 20.0 / 20.0; omni 861 / 5.1 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
