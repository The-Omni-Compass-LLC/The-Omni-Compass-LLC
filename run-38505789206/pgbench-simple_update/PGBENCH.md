# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,614 tps; base rate 992 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `89958aaa9496`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,764 | 2,779 | +0.5% (-3.9 to +4.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,908 | 2,911 | +0.1% (-0.1 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 33.0 | 36.0 | +8.9% (-536.0 to +553.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 627.7 | 593.8 | -5.4% (-13.2 to +2.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.974 | 0.984 | +1.0% (-7.6 to +9.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 20.2 | 19.2 | -5.1% (-57.7 to +47.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.0 | -9.8% (-14.8 to -4.8) | GAIN |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (+4.5 to +18.8) | power given |
| host CPU busy (share of the run) | 0.361 | 0.368 | +1.9% (-4.8 to +8.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 626.1 | 637.4 | +1.8% (-4.8 to +8.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.504 | 0.51 | +1.2% (-9.6 to +12.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.874 | 1.41 | +61.1% (+40.0 to +82.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -8.8% (-13.6 to -4.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 93, 96, 87; fail-ups per arm: 4, 5, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2730 / 72.2 / 20.0 / 20.0; omni 2793 / 9.7 / 18.2 / 18.5
- rep 2 (omni then native): native 2783 / 11.7 / 19.8 / 20.0; omni 2748 / 92.5 / 18.1 / 18.4
- rep 3 (native then omni): native 2778 / 15.2 / 20.0 / 20.0; omni 2795 / 5.7 / 17.6 / 17.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
