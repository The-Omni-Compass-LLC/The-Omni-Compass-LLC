# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,077 tps; base rate 5,862 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,187 | 17,197 | +0.1% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 17,187 | 17,197 | +0.1% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.41 | 0.434 | +5.8% (-44.0 to +55.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.35 | 4.16 | +24.5% (-37.7 to +86.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.154 | 0.154 | +0.2% (-6.3 to +6.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.31 | 0.333 | +7.3% (-35.2 to +49.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.3% (-16.3 to +1.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.369 | 0.369 | +0.0% (-6.1 to +6.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 630.1 | 629.9 | -0.0% (-6.1 to +6.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0815 | 0.0814 | -0.1% (-6.2 to +6.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.03 | 3.63 | +20.0% (+11.5 to +28.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.4 | -8.1% (-14.6 to -1.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 52, 62, 63; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17184 / 0.4 / 20.0 / 20.0; omni 17199 / 0.3 / 18.8 / 19.0
- rep 2 (omni then native): native 17188 / 0.4 / 18.6 / 20.0; omni 17194 / 0.4 / 17.8 / 18.1
- rep 3 (native then omni): native 17187 / 0.5 / 20.0 / 20.0; omni 17197 / 0.6 / 17.8 / 18.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
