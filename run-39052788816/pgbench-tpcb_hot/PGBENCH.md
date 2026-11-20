# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,930 tps; base rate 289 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 844.4 | 845.4 | +0.1% (-2.5 to +2.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 849.2 | 848.1 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.09 | 4.97 | -2.4% (-30.0 to +25.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 24.3 | 15.9 | -34.4% (-254.1 to +185.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.88 | -0.3% (-1.5 to +1.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.17 | 2.88 | -9.1% (-98.3 to +80.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.3 | -7.1% (-11.3 to -3.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.236 | 0.235 | -0.2% (-1.7 to +1.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 367.4 | 366.8 | -0.2% (-1.8 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.967 | 0.964 | -0.3% (-4.3 to +3.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.77 | 1.48 | +92.6% (+86.8 to +98.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.4% (-7.7 to -3.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 21, 24, 11; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 841 / 5.2 / 20.0 / 20.0; omni 849 / 4.6 / 18.3 / 18.7
- rep 2 (omni then native): native 851 / 4.7 / 19.2 / 20.0; omni 842 / 5.2 / 18.1 / 19.1
- rep 3 (native then omni): native 841 / 5.4 / 20.0 / 20.0; omni 846 / 5.1 / 18.6 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
