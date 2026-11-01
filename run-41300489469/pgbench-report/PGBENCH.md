# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,202 tps; base rate 5,880 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,244 | 17,245 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 17,244 | 17,245 | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.735 | 0.706 | -4.0% (-33.5 to +25.5) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.6 | 2.3 | -11.7% (-42.6 to +19.1) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.189 | 0.19 | +0.4% (-1.2 to +1.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.3 | 0.289 | -3.9% (-17.7 to +9.9) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.427 | 0.427 | -0.0% (-0.9 to +0.9) | STEADY, no difference beyond the noise |
| host CPU-seconds | 761.6 | 761.5 | -0.0% (-1.0 to +1.0) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0981 | 0.0981 | -0.0% (-0.9 to +0.9) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 13.6 | 14.2 | +4.7% (+2.9 to +6.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17250 / 0.8 / 20.0 / 20.0; omni 17240 / 0.7 / 20.0 / 20.0
- rep 2 (omni then native): native 17242 / 0.8 / 20.0 / 20.0; omni 17247 / 0.7 / 20.0 / 20.0
- rep 3 (native then omni): native 17241 / 0.6 / 20.0 / 20.0; omni 17247 / 0.7 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,646 tps; base rate 1,147 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,195 | 3,221 | +0.8% (-1.9 to +3.6) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,360 | 3,365 | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 33.2 | 15.5 | -53.3% (-342.9 to +236.3) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 581.2 | 536.0 | -7.8% (-47.4 to +31.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.601 | 0.601 | +0.0% (-1.4 to +1.4) | STEADY, the same |
| latency, mean (ms) | 18.8 | 16.3 | -13.0% (-66.0 to +40.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 26.3 | +31.3% (+14.2 to +48.3) | power given |
| server connections alive, most at once | 20.0 | 36.7 | +83.3% (+64.4 to +102.3) | power given |
| host CPU busy (share of the run) | 0.318 | 0.32 | +0.7% (+0.2 to +1.2) | power given |
| host CPU-seconds | 542.7 | 546.4 | +0.7% (+0.3 to +1.1) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.378 | 0.377 | -0.2% (-2.6 to +2.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.19 | 2.65 | +20.7% (+10.8 to +30.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 26.2 | +31.0% (+14.1 to +48.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 77, 56, 61; fail-ups per arm: 0, 1, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3149 / 79.9 / 20.0 / 20.0; omni 3213 / 18.2 / 27.8 / 27.8
- rep 2 (omni then native): native 3218 / 10.2 / 20.0 / 20.0; omni 3238 / 7.9 / 25.5 / 25.4
- rep 3 (native then omni): native 3218 / 9.5 / 20.0 / 20.0; omni 3212 / 20.4 / 25.5 / 25.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,912 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v23 (digest c96ea4105d8747db, 65 files) at `6cc9379757a7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 839.8 | 841.9 | +0.3% (-0.4 to +0.9) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 839.8 | 842.0 | +0.3% (-0.4 to +0.9) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.99 | 5 | +0.1% (-2.5 to +2.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.4 | 10.2 | -1.6% (-5.9 to +2.8) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.77 | 1.77 | +0.0% (-0.7 to +0.8) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.32 | 2.32 | -0.3% (-1.6 to +1.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.294 | 0.295 | +0.2% (-0.7 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds | 507.3 | 508.3 | +0.2% (-0.8 to +1.2) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.34 | 1.34 | -0.1% (-0.4 to +0.3) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.46 | 2.12 | +45.3% (+40.0 to +50.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 840 / 5.1 / 20.0 / 20.0; omni 840 / 5.1 / 20.0 / 20.0
- rep 2 (omni then native): native 840 / 4.9 / 20.0 / 20.0; omni 844 / 5.0 / 20.0 / 20.0
- rep 3 (native then omni): native 840 / 4.9 / 20.0 / 20.0; omni 841 / 4.9 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
