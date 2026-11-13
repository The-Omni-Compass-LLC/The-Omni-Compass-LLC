# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,970 tps; base rate 295 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 864.4 | 865.5 | +0.1% (-0.5 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 864.9 | 866.2 | +0.1% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.63 | 4.87 | +5.1% (-9.9 to +20.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 15.3 | +20.2% (-31.9 to +72.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.78 | 1.78 | -0.3% (-2.1 to +1.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.4 | 2.47 | +2.7% (-6.9 to +12.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 17.9 | -10.1% (-27.1 to +7.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.221 | 0.22 | -0.2% (-2.0 to +1.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 342.9 | 342.3 | -0.2% (-2.1 to +1.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.882 | 0.879 | -0.3% (-2.5 to +1.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.75 | 1.48 | +98.0% (+87.3 to +108.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -8.8% (-25.9 to +8.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 41, 36, 56; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 866 / 4.5 / 20.0 / 20.0; omni 865 / 4.9 / 18.7 / 19.0
- rep 2 (omni then native): native 864 / 4.6 / 19.6 / 20.0; omni 866 / 5.0 / 18.5 / 19.1
- rep 3 (native then omni): native 863 / 4.7 / 20.0 / 20.0; omni 866 / 4.6 / 16.4 / 16.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
