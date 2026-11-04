# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,457 tps; base rate 819 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `05092772357b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,362 | 2,353 | -0.4% (-1.5 to +0.8) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,401 | 2,400 | -0.0% (-0.2 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.27 | 5.1 | +19.4% (-15.5 to +54.4) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 116.7 | 157.0 | +34.6% (-57.0 to +126.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.09 | 1.11 | +1.7% (-3.9 to +7.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 4.08 | 4.8 | +17.6% (-30.3 to +65.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 24.3 | +21.6% (+8.7 to +34.6) | power given |
| server connections alive, most at once | 20.0 | 33.7 | +68.3% (+61.2 to +75.5) | power given |
| host CPU busy (share of the run) | 0.43 | 0.436 | +1.2% (-1.9 to +4.4) | STEADY, no difference beyond the noise |
| host CPU-seconds | 756.1 | 765.4 | +1.2% (-1.8 to +4.3) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.712 | 0.723 | +1.6% (-1.9 to +5.1) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.02 | 3.64 | +20.3% (+18.8 to +21.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.4 | +21.9% (+8.7 to +35.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 48, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2367 / 3.6 / 20.0 / 20.0; omni 2349 / 5.0 / 24.9 / 25.0
- rep 2 (omni then native): native 2347 / 4.3 / 20.0 / 20.0; omni 2350 / 5.3 / 25.0 / 25.0
- rep 3 (native then omni): native 2371 / 4.9 / 20.0 / 20.0; omni 2360 / 5.1 / 23.1 / 23.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
