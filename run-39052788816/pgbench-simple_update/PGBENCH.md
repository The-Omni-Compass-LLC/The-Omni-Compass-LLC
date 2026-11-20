# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,845 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,643 | 1,647 | +0.3% (-2.4 to +3.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,689 | 1,691 | +0.1% (-0.0 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.72 | 8.91 | +2.1% (-111.6 to +115.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 197.7 | 175.8 | -11.1% (-85.6 to +63.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.54 | 1.54 | +0.5% (+0.1 to +0.9) | LOSS |
| latency, mean (ms) | 6.78 | 6.46 | -4.8% (-93.0 to +83.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.5% (-8.8 to +3.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.349 | 0.351 | +0.6% (-0.5 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 526.5 | 530.3 | +0.7% (-0.9 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.712 | 0.715 | +0.5% (-3.6 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.84 | +79.4% (+69.4 to +89.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -1.8% (-7.8 to +4.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 30, 57; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1647 / 9.9 / 20.0 / 20.0; omni 1656 / 7.4 / 20.0 / 20.2
- rep 2 (omni then native): native 1643 / 7.4 / 20.0 / 20.0; omni 1628 / 12.2 / 19.5 / 19.6
- rep 3 (native then omni): native 1638 / 8.9 / 20.0 / 20.0; omni 1658 / 7.2 / 19.0 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
