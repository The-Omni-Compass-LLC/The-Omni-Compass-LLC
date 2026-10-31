# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,457 tps; base rate 1,119 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,998 | 3,091 | +3.1% (-7.7 to +13.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,274 | 3,279 | +0.2% (+0.0 to +0.3) | GAIN |
| latency, 95th percentile (ms, lag included) | 321.9 | 89.9 | -72.1% (-334.5 to +190.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,993 | 532.5 | -73.3% (-364.8 to +218.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.709 | 0.708 | -0.2% (-5.5 to +5.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 78.9 | 18.8 | -76.1% (-376.3 to +224.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 27.3 | +36.7% (+26.7 to +46.6) | power given |
| server connections alive, most at once | 20.0 | 37.7 | +88.3% (+62.5 to +114.2) | power given |
| host CPU busy (share of the run) | 0.347 | 0.353 | +1.8% (-1.2 to +4.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 594.0 | 604.1 | +1.7% (-0.9 to +4.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.44 | 0.434 | -1.4% (-9.8 to +7.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.38 | 2.94 | +23.6% (+18.8 to +28.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 27.3 | +36.5% (+26.3 to +46.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 81, 67, 61; fail-ups per arm: 0, 2, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2850 / 721.9 / 20.0 / 20.0; omni 3092 / 98.2 / 28.2 / 28.2
- rep 2 (omni then native): native 3054 / 174.7 / 20.0 / 20.0; omni 3071 / 115.2 / 27.2 / 27.1
- rep 3 (native then omni): native 3092 / 69.1 / 20.0 / 20.0; omni 3109 / 56.3 / 26.6 / 26.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
