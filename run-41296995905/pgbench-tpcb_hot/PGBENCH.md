# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,017 tps; base rate 303 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 886.6 | 886.6 | -0.0% (-1.0 to +1.0) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 886.8 | 886.7 | -0.0% (-1.0 to +0.9) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.2 | 4.77 | -8.4% (-29.0 to +12.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.7 | 10.6 | -16.7% (-46.3 to +12.9) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.78 | 1.78 | -0.2% (-3.5 to +3.1) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.41 | 2.29 | -4.8% (-14.1 to +4.5) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.308 | 0.308 | -0.2% (-3.5 to +3.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 530.1 | 529.1 | -0.2% (-3.6 to +3.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.33 | -0.2% (-2.7 to +2.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.53 | 2.2 | +43.5% (+38.8 to +48.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 886 / 4.6 / 20.0 / 20.0; omni 888 / 4.5 / 20.0 / 20.0
- rep 2 (omni then native): native 889 / 5.1 / 20.0 / 20.0; omni 885 / 4.8 / 20.0 / 20.0
- rep 3 (native then omni): native 885 / 5.9 / 20.0 / 20.0; omni 887 / 5.0 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
