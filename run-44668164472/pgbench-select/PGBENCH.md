# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,549 tps; base rate 3,982 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,676 | 11,599 | -0.7% (-3.7 to +2.4) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 11,676 | 11,680 | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.49 | 1.59 | +7.1% (-25.6 to +39.9) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.43 | 40.7 | +1086.2% (-3605.5 to +5778.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.282 | 0.282 | +0.2% (-1.8 to +2.3) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.484 | 1.33 | +174.9% (-582.5 to +932.3) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | +0.6% (-2.1 to +3.4) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-27.5 to +44.2) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.467 | 0.468 | +0.2% (-1.8 to +2.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 831.2 | 832.8 | +0.2% (-1.9 to +2.3) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.158 | 0.16 | +0.9% (-0.1 to +1.9) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 12.8 | 13.4 | +4.6% (+2.3 to +6.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.6% (-2.1 to +3.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11669 / 1.6 / 20.0 / 20.0; omni 11427 / 1.9 / 20.4 / 20.4
- rep 2 (omni then native): native 11682 / 1.4 / 20.0 / 20.0; omni 11694 / 1.5 / 20.0 / 20.0
- rep 3 (native then omni): native 11677 / 1.4 / 20.0 / 20.0; omni 11675 / 1.3 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
