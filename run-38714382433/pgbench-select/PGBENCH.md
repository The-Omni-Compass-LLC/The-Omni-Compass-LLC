# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,312 tps; base rate 2,447 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,176 | 7,171 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,176 | 7,171 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.39 | 1.59 | +14.2% (+3.0 to +25.5) | LOSS |
| latency, 99th percentile (ms) | 4.08 | 4.84 | +18.6% (-1.1 to +38.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.372 | 0.376 | +1.1% (-0.1 to +2.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.565 | 0.624 | +10.4% (-2.8 to +23.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.4 | -11.7% (-19.9 to -3.5) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.324 | 0.329 | +1.5% (-0.5 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 479.2 | 487.2 | +1.7% (-0.8 to +4.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.148 | 0.151 | +1.7% (-0.8 to +4.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.65 | 3.47 | +30.5% (+29.8 to +31.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.5 | -7.7% (-19.4 to +4.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 37, 27, 21; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7176 / 1.5 / 20.0 / 20.0; omni 7169 / 1.8 / 17.0 / 17.4
- rep 2 (omni then native): native 7171 / 1.3 / 19.2 / 20.0; omni 7174 / 1.5 / 16.9 / 19.0
- rep 3 (native then omni): native 7181 / 1.4 / 20.0 / 20.0; omni 7171 / 1.5 / 18.3 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
