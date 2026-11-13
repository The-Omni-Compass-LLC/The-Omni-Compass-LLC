# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 38,103 tps; base rate 5,715 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,764 | 16,759 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 16,764 | 16,759 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.325 | 0.589 | +81.2% (-207.7 to +370.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.839 | 4.59 | +447.6% (-777.4 to +1672.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.155 | 0.159 | +2.6% (-5.9 to +11.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.338 | +71.0% (-104.1 to +246.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.7 | -10.2% (-18.9 to -1.4) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.359 | 0.371 | +3.3% (-6.0 to +12.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 609.0 | 630.2 | +3.5% (-6.0 to +13.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0807 | 0.0836 | +3.5% (-6.0 to +13.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.02 | 3.64 | +20.4% (+6.1 to +34.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -9.9% (-20.6 to +0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 36, 60, 57; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16765 / 0.3 / 20.0 / 20.0; omni 16757 / 0.4 / 18.6 / 19.0
- rep 2 (omni then native): native 16767 / 0.3 / 19.0 / 20.0; omni 16764 / 1.0 / 17.1 / 17.4
- rep 3 (native then omni): native 16761 / 0.3 / 20.0 / 20.0; omni 16754 / 0.4 / 17.3 / 17.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,492 tps; base rate 824 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,816 | 1,960 | +7.9% (-44.1 to +60.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,404 | 2,395 | -0.4% (-4.4 to +3.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,067 | 1,061 | -0.5% (-343.6 to +342.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,627 | 1,934 | +18.9% (-249.8 to +287.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.23 | 1.1 | -10.4% (-63.8 to +43.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 140.8 | 128.9 | -8.5% (-306.3 to +289.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.8 | -0.7% (-4.7 to +3.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.379 | 0.38 | +0.4% (-5.5 to +6.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 655.2 | 655.6 | +0.1% (-4.3 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.81 | 0.747 | -7.8% (-54.3 to +38.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.944 | 1.63 | +72.6% (+59.6 to +85.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.7% (-4.6 to +3.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 79, 56, 81; fail-ups per arm: 10, 3, 6.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1904 / 579.7 / 20.0 / 20.0; omni 1983 / 434.6 / 20.2 / 20.2
- rep 2 (omni then native): native 1978 / 675.4 / 20.0 / 20.0; omni 1778 / 2207.8 / 19.7 / 19.8
- rep 3 (native then omni): native 1566 / 1945.7 / 20.0 / 20.0; omni 2119 / 541.5 / 19.6 / 19.6

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,867 tps; base rate 280 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `5c97b928096a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 821.0 | 821.8 | +0.1% (-0.8 to +1.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 821.0 | 821.8 | +0.1% (-0.8 to +1.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.85 | 4.91 | +1.3% (-23.5 to +26.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.2 | 10.9 | +7.1% (-67.5 to +81.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.9 | 1.89 | -0.4% (-3.8 to +2.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.41 | 2.43 | +0.8% (-15.0 to +16.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 18.3 | -7.5% (-12.3 to -2.7) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.23 | 0.23 | -0.2% (-5.5 to +5.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 359.3 | 358.7 | -0.2% (-5.7 to +5.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.973 | 0.97 | -0.3% (-5.2 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.765 | 1.52 | +98.9% (+87.6 to +110.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -6.0% (-9.9 to -2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 25, 27, 29; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 822 / 5.1 / 20.0 / 20.0; omni 821 / 4.7 / 18.4 / 19.0
- rep 2 (omni then native): native 822 / 4.8 / 19.5 / 20.0; omni 821 / 4.9 / 18.4 / 19.0
- rep 3 (native then omni): native 819 / 4.6 / 20.0 / 20.0; omni 824 / 5.1 / 18.2 / 18.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
