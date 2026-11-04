# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,480 tps; base rate 972 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,745 | 2,760 | +0.6% (-0.7 to +1.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,850 | 2,850 | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 10.1 | 1.9 | -81.2% (-407.6 to +245.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 506.2 | 407.7 | -19.5% (-39.3 to +0.3) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.628 | 0.628 | +0.1% (-7.0 to +7.1) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 14.0 | 10.9 | -21.7% (-48.7 to +5.3) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 25.1 | +25.3% (+19.7 to +30.9) | power given |
| server connections alive, most at once | 20.0 | 37.0 | +85.0% (+72.6 to +97.4) | power given |
| host CPU busy (share of the run) | 0.289 | 0.29 | +0.3% (-6.2 to +6.8) | STEADY, no difference beyond the noise |
| host CPU-seconds | 495.3 | 496.3 | +0.2% (-5.9 to +6.3) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.401 | 0.4 | -0.4% (-6.2 to +5.5) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.04 | 2.54 | +24.2% (+16.4 to +31.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 25.0 | +25.2% (+19.4 to +31.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 47, 60, 34; fail-ups per arm: 1, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2726 / 25.4 / 20.0 / 20.0; omni 2757 / 1.9 / 24.6 / 24.6
- rep 2 (omni then native): native 2754 / 2.3 / 20.0 / 20.0; omni 2765 / 1.9 / 25.5 / 25.5
- rep 3 (native then omni): native 2755 / 2.5 / 20.0 / 20.0; omni 2758 / 1.9 / 25.1 / 25.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
