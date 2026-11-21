# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,859 tps; base rate 279 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 817.3 | 816.3 | -0.1% (-0.5 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 817.6 | 816.9 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.03 | 5.25 | +4.4% (-16.0 to +24.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.5 | 14.0 | +33.9% (-119.0 to +186.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.95 | 1.93 | -1.0% (-1.5 to -0.5) | GAIN |
| latency, mean (ms) | 2.51 | 2.6 | +3.5% (-21.5 to +28.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.3% (-9.7 to -5.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.235 | 0.231 | -1.5% (-3.5 to +0.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 366.7 | 361.4 | -1.5% (-3.8 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.997 | 0.984 | -1.3% (-4.0 to +1.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.77 | 1.48 | +92.5% (+84.4 to +100.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-6.2 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 22, 24; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 818 / 4.9 / 20.0 / 20.0; omni 818 / 4.8 / 18.5 / 18.9
- rep 2 (omni then native): native 816 / 4.9 / 18.5 / 20.0; omni 814 / 5.0 / 17.3 / 18.8
- rep 3 (native then omni): native 818 / 5.3 / 20.0 / 20.0; omni 816 / 6.0 / 18.4 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
