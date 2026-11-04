# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,633 tps; base rate 395 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,155 | 1,157 | +0.2% (-1.0 to +1.3) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 1,159 | 1,158 | -0.1% (-0.5 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.48 | 2.35 | -5.2% (-12.4 to +2.1) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.95 | 4.14 | -58.4% (-281.1 to +164.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.16 | 1.16 | -0.5% (-2.2 to +1.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.69 | 1.41 | -16.4% (-63.2 to +30.4) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.2 | +0.8% (-2.8 to +4.5) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (-38.5 to +61.9) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.239 | 0.237 | -0.5% (-2.4 to +1.3) | STEADY, no difference beyond the noise |
| host CPU-seconds | 420.0 | 417.7 | -0.5% (-2.3 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.808 | 0.802 | -0.7% (-1.7 to +0.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.46 | 1.94 | +33.0% (+30.3 to +35.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.2 | +0.9% (-2.8 to +4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 8; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1151 / 2.5 / 20.0 / 20.0; omni 1158 / 2.3 / 20.0 / 20.0
- rep 2 (omni then native): native 1158 / 2.4 / 20.0 / 20.0; omni 1154 / 2.3 / 20.0 / 20.0
- rep 3 (native then omni): native 1156 / 2.5 / 20.0 / 20.0; omni 1159 / 2.4 / 20.5 / 20.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
