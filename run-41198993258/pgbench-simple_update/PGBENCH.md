# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
