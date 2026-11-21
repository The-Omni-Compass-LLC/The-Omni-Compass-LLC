# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,424 tps; base rate 364 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 719.6 | 734.4 | +2.1% (-55.3 to +59.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,048 | 1,049 | +0.1% (-4.5 to +4.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,036 | 2,394 | +17.6% (-69.0 to +104.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3,305 | 3,351 | +1.4% (-73.8 to +76.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 7.96 | 5.15 | -35.4% (-479.2 to +408.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 357.4 | 319.7 | -10.5% (-82.2 to +61.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-0.4 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.262 | 0.261 | -0.4% (-5.7 to +4.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 457.4 | 455.6 | -0.4% (-6.4 to +5.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.49 | 1.41 | -5.6% (-65.0 to +53.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.646 | 1.21 | +87.6% (+79.4 to +95.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-0.5 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 24, 2; fail-ups per arm: 6, 4, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 963 / 131.0 / 20.0 / 20.0; omni 833 / 349.8 / 20.0 / 20.0
- rep 2 (omni then native): native 576 / 2680.2 / 20.0 / 20.0; omni 772 / 3807.7 / 20.0 / 19.9
- rep 3 (native then omni): native 620 / 3295.5 / 20.0 / 20.0; omni 598 / 3024.5 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
