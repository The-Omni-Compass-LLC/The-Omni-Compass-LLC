# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,043 tps; base rate 2,406 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,061 | 7,058 | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 7,061 | 7,058 | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.994 | 0.956 | -3.8% (-11.4 to +3.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.11 | 1.99 | -5.9% (-19.2 to +7.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.349 | 0.346 | -0.8% (-1.9 to +0.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.46 | 0.45 | -2.1% (-5.6 to +1.3) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.389 | 0.387 | -0.6% (-1.7 to +0.4) | STEADY, no difference beyond the noise |
| host CPU-seconds | 661.0 | 656.7 | -0.7% (-1.8 to +0.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.208 | 0.207 | -0.6% (-1.8 to +0.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.31 | 9.03 | +8.7% (+3.0 to +14.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7062 / 1.0 / 20.0 / 20.0; omni 7057 / 0.9 / 20.0 / 20.0
- rep 2 (omni then native): native 7064 / 1.0 / 20.0 / 20.0; omni 7060 / 1.0 / 20.0 / 20.0
- rep 3 (native then omni): native 7057 / 0.9 / 20.0 / 20.0; omni 7057 / 0.9 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,006 tps; base rate 601 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,735 | 1,739 | +0.2% (-1.1 to +1.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,763 | 1,764 | +0.1% (-0.2 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.56 | 6.48 | -1.2% (-37.1 to +34.8) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 104.9 | 85.2 | -18.8% (-141.5 to +103.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.36 | 1.37 | +0.7% (-1.0 to +2.5) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.27 | 3.84 | -10.1% (-60.9 to +40.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 23.7 | +18.7% (+10.1 to +27.4) | power given |
| server connections alive, most at once | 20.0 | 33.7 | +68.3% (+54.0 to +82.7) | power given |
| host CPU busy (share of the run) | 0.403 | 0.406 | +0.7% (+0.0 to +1.3) | power given |
| host CPU-seconds | 690.9 | 695.3 | +0.6% (-0.2 to +1.5) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.885 | 0.888 | +0.4% (-1.4 to +2.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.51 | 3.28 | +30.9% (+27.7 to +34.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 23.8 | +18.8% (+10.1 to +27.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 30, 40, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1744 / 6.8 / 20.0 / 20.0; omni 1743 / 6.1 / 23.0 / 23.0
- rep 2 (omni then native): native 1732 / 6.4 / 20.0 / 20.0; omni 1731 / 7.4 / 23.9 / 23.9
- rep 3 (native then omni): native 1728 / 6.5 / 20.0 / 20.0; omni 1743 / 5.9 / 24.4 / 24.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,262 tps; base rate 339 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 994.4 | 995.0 | +0.1% (-0.2 to +0.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 995.0 | 995.7 | +0.1% (-0.3 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.47 | 3.69 | -17.4% (-81.2 to +46.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.4 | 8.06 | -35.0% (-160.5 to +90.5) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.49 | -0.6% (-9.9 to +8.7) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.11 | 1.95 | -7.7% (-48.1 to +32.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | +0.7% (-2.4 to +3.8) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-33.0 to +53.0) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.309 | 0.308 | -0.5% (-7.6 to +6.5) | STEADY, no difference beyond the noise |
| host CPU-seconds | 536.6 | 533.7 | -0.5% (-7.5 to +6.4) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.2 | 1.19 | -0.6% (-7.7 to +6.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.68 | 2.39 | +42.7% (+34.6 to +50.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.7% (-2.4 to +3.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 7; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 994 / 5.9 / 20.0 / 20.0; omni 996 / 3.8 / 20.0 / 20.0
- rep 2 (omni then native): native 994 / 4.1 / 20.0 / 20.0; omni 995 / 3.8 / 20.0 / 20.0
- rep 3 (native then omni): native 995 / 3.5 / 20.0 / 20.0; omni 995 / 3.5 / 20.4 / 20.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
