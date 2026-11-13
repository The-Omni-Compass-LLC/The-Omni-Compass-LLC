# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,842 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,645 | 1,649 | +0.2% (-3.0 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,690 | 1,690 | +0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.16 | 7.98 | +11.5% (-52.6 to +75.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 199.9 | 187.5 | -6.2% (-68.7 to +56.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.54 | 1.57 | +1.8% (-0.4 to +4.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.8 | 6.54 | -3.8% (-78.5 to +70.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.4% (-6.5 to -2.2) | GAIN |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.343 | 0.35 | +2.0% (-0.4 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 516.3 | 528.5 | +2.4% (-0.6 to +5.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.697 | 0.712 | +2.2% (-3.6 to +7.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.86 | +81.6% (+79.1 to +84.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -3.1% (-5.0 to -1.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 51, 52, 51; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1652 / 7.2 / 20.0 / 20.0; omni 1637 / 9.6 / 19.3 / 19.5
- rep 2 (omni then native): native 1649 / 6.6 / 20.0 / 20.0; omni 1648 / 7.8 / 19.2 / 19.4
- rep 3 (native then omni): native 1634 / 7.7 / 20.0 / 20.0; omni 1661 / 6.5 / 18.9 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
