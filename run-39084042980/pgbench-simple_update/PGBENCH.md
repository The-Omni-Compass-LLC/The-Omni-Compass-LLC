# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,633 tps; base rate 1,145 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,104 | 3,143 | +1.2% (-2.8 to +5.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,358 | 3,358 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 162.5 | 130.1 | -20.0% (-106.7 to +66.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 642.2 | 587.3 | -8.6% (-20.6 to +3.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.711 | 0.709 | -0.2% (-9.1 to +8.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 26.2 | 22.7 | -13.5% (-55.5 to +28.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.4% (-3.6 to +0.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.354 | +0.8% (-6.0 to +7.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 598.5 | 602.6 | +0.7% (-5.9 to +7.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.429 | 0.426 | -0.6% (-10.6 to +9.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.868 | 1.4 | +60.7% (+46.6 to +74.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.8 | -1.1% (-3.0 to +0.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 46, 25; fail-ups per arm: 1, 1, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3088 / 160.8 / 20.0 / 20.0; omni 3184 / 63.2 / 19.6 / 19.7
- rep 2 (omni then native): native 3096 / 179.6 / 20.0 / 20.0; omni 3121 / 173.2 / 19.6 / 19.7
- rep 3 (native then omni): native 3128 / 147.1 / 20.0 / 20.0; omni 3124 / 153.7 / 19.9 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
