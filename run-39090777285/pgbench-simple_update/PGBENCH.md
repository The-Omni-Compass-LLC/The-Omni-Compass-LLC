# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,842 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8e3f058da83e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,640 | 1,626 | -0.8% (-7.8 to +6.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,690 | 1,690 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 9.71 | 49.4 | +408.3% (-1377.4 to +2194.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 209.6 | 332.4 | +58.6% (-304.4 to +421.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.58 | 1.57 | -0.7% (-3.7 to +2.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.46 | 12.3 | +65.4% (-290.8 to +421.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.2% (-4.3 to -0.2) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.351 | -0.4% (-2.7 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 531.6 | 529.1 | -0.5% (-3.2 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.72 | 0.724 | +0.4% (-9.4 to +10.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.83 | +77.2% (+72.0 to +82.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.6% (-3.4 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 44, 22; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1647 / 11.1 / 20.0 / 20.0; omni 1585 / 131.4 / 19.7 / 19.8
- rep 2 (omni then native): native 1637 / 9.5 / 20.0 / 20.0; omni 1627 / 10.2 / 19.4 / 19.5
- rep 3 (native then omni): native 1636 / 8.5 / 20.0 / 20.0; omni 1666 / 6.5 / 19.6 / 19.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
