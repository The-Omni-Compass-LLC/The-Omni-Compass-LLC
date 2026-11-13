# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,943 tps; base rate 891 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `afbac134f8a1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,465 | 2,483 | +0.7% (-6.7 to +8.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,610 | 2,610 | -0.0% (-0.7 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 67.8 | 70.0 | +3.2% (-608.4 to +614.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 631.8 | 575.0 | -9.0% (-52.3 to +34.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.19 | 1.19 | +0.2% (-4.2 to +4.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.8 | 19.9 | -9.1% (-128.8 to +110.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.1 | -8.6% (-16.0 to -1.2) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.407 | 0.409 | +0.5% (-1.5 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 704.0 | 707.1 | +0.4% (-1.7 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.635 | 0.633 | -0.3% (-7.1 to +6.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.05 | 1.65 | +58.1% (+50.6 to +65.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.4 | -7.9% (-15.2 to -0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 60, 71, 81; fail-ups per arm: 3, 4, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2427 / 105.8 / 20.0 / 20.0; omni 2503 / 5.7 / 18.9 / 19.1
- rep 2 (omni then native): native 2501 / 4.9 / 19.6 / 20.0; omni 2437 / 199.7 / 17.8 / 18.3
- rep 3 (native then omni): native 2468 / 92.8 / 20.0 / 20.0; omni 2510 / 4.6 / 17.7 / 17.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
