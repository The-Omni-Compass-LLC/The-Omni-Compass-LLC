# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,824 tps; base rate 274 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `43a27376d80b`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 802.5 | 802.4 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 802.8 | 802.6 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.58 | 6.02 | +7.8% (-19.0 to +34.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 14.7 | +12.0% (-50.5 to +74.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.9 | 1.9 | +0.4% (-2.0 to +2.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.57 | 2.64 | +2.7% (-14.5 to +19.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.6 | -11.2% (-24.0 to +1.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.221 | 0.223 | +0.9% (-3.4 to +5.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 346.0 | 349.3 | +0.9% (-3.5 to +5.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.958 | 0.967 | +0.9% (-3.2 to +5.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.756 | 1.49 | +97.6% (+95.4 to +99.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.5% (-23.4 to +6.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 27, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 804 / 5.9 / 20.0 / 20.0; omni 802 / 5.8 / 16.6 / 16.9
- rep 2 (omni then native): native 803 / 5.5 / 19.4 / 20.0; omni 803 / 6.5 / 17.5 / 19.0
- rep 3 (native then omni): native 801 / 5.4 / 20.0 / 20.0; omni 802 / 5.7 / 18.6 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
