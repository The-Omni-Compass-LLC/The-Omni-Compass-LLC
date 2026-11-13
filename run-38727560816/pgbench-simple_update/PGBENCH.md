# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,816 tps; base rate 572 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v6 (digest df6147466ef18046, 45 files) at `63f29c3e20a5`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,633 | 1,644 | +0.7% (-3.5 to +4.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,679 | 1,680 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.88 | 7.99 | -10.0% (-102.3 to +82.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 179.6 | 159.0 | -11.5% (-165.9 to +142.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.56 | 1.56 | -0.2% (-3.7 to +3.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.7 | 6.04 | -10.0% (-142.0 to +122.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -4.0% (-5.4 to -2.5) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.347 | 0.347 | -0.1% (-4.1 to +3.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 523.7 | 522.5 | -0.2% (-4.8 to +4.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.713 | 0.707 | -0.9% (-9.2 to +7.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.86 | +82.9% (+77.0 to +88.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.3% (-4.7 to -1.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 52, 51, 64; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1639 / 7.7 / 20.0 / 20.0; omni 1645 / 8.0 / 19.2 / 19.4
- rep 2 (omni then native): native 1640 / 7.8 / 20.0 / 20.0; omni 1626 / 9.5 / 19.3 / 19.4
- rep 3 (native then omni): native 1620 / 11.1 / 20.0 / 20.0; omni 1660 / 6.5 / 19.1 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
