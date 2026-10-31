# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,042 tps; base rate 2,406 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,056 | 7,059 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,056 | 7,059 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.04 | 1.06 | +2.4% (-12.5 to +17.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.37 | 2.53 | +6.5% (-31.2 to +44.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.351 | 0.353 | +0.7% (-2.0 to +3.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.471 | 0.49 | +3.9% (-14.7 to +22.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.39 | 0.393 | +0.7% (-1.1 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 662.2 | 667.2 | +0.8% (-1.0 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.209 | 0.21 | +0.7% (-1.2 to +2.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.25 | 9 | +9.1% (+5.5 to +12.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7061 / 1.1 / 20.0 / 20.0; omni 7054 / 1.1 / 20.0 / 20.0
- rep 2 (omni then native): native 7060 / 1.0 / 20.0 / 20.0; omni 7066 / 1.1 / 20.0 / 20.0
- rep 3 (native then omni): native 7049 / 1.0 / 20.0 / 20.0; omni 7057 / 1.0 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
