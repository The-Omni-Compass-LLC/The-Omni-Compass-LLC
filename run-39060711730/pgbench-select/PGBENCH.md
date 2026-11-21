# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,530 tps; base rate 3,979 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,668 | 11,671 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,668 | 11,671 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.38 | +10.2% (-50.4 to +70.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.84 | 3.32 | +16.8% (-45.6 to +79.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.273 | 0.273 | +0.0% (-5.5 to +5.5) | EVEN, the same |
| latency, mean (ms) | 0.444 | 0.476 | +7.1% (-26.5 to +40.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.0 | -9.1% (-26.7 to +8.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.458 | 0.458 | -0.0% (-2.3 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 795.7 | 795.1 | -0.1% (-2.4 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.151 | -0.1% (-2.4 to +2.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.67 | 4.27 | +16.3% (+12.0 to +20.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | -9.6% (-25.3 to +6.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 30, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11666 / 1.2 / 20.0 / 20.0; omni 11672 / 1.7 / 18.9 / 19.1
- rep 2 (omni then native): native 11673 / 1.2 / 19.2 / 20.0; omni 11666 / 1.1 / 18.4 / 18.5
- rep 3 (native then omni): native 11664 / 1.3 / 20.0 / 20.0; omni 11675 / 1.3 / 16.6 / 16.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
