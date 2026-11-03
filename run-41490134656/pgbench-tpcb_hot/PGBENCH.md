# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,700 tps; base rate 255 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `5d3560eacaa2`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 725.0 | 733.3 | +1.1% (-5.2 to +7.5) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 746.5 | 747.0 | +0.1% (-0.9 to +1.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.56 | 1.71 | -77.3% (-366.8 to +212.2) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,202 | 166.5 | -86.1% (-494.5 to +322.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.727 | 0.738 | +1.6% (-1.8 to +5.0) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 30.2 | 7.2 | -76.1% (-467.0 to +314.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.7 | +3.7% (-1.6 to +9.0) | STEADY, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 30.7 | +53.3% (-4.0 to +110.7) | STEADY, no difference beyond the noise |
| host CPU busy (share of the run) | 0.107 | 0.11 | +2.3% (-4.0 to +8.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 188.5 | 192.7 | +2.2% (-4.2 to +8.7) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.578 | 0.584 | +1.1% (-11.4 to +13.7) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.782 | 1.24 | +58.0% (+51.4 to +64.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.7 | +3.7% (-1.6 to +9.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 8, 7, 20; fail-ups per arm: 1, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 723 / 4.3 / 20.0 / 20.0; omni 721 / 2.2 / 20.4 / 20.4
- rep 2 (omni then native): native 738 / 1.3 / 20.0 / 20.0; omni 734 / 1.7 / 20.7 / 20.7
- rep 3 (native then omni): native 714 / 17.1 / 20.0 / 20.0; omni 744 / 1.2 / 21.2 / 21.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
