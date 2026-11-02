# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
