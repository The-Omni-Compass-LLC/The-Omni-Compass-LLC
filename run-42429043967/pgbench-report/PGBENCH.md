# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,010 tps; base rate 2,401 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,042 | 7,046 | +0.0% (-0.0 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 7,042 | 7,046 | +0.0% (-0.0 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.864 | 0.879 | +1.7% (-14.2 to +17.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.72 | 1.68 | -2.7% (-54.6 to +49.2) | STEADY, no difference beyond the noise |
| latency, median (ms) | 0.341 | 0.344 | +0.8% (-3.2 to +4.8) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.43 | 0.433 | +0.6% (-11.0 to +12.2) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.378 | 0.381 | +0.7% (-2.3 to +3.7) | STEADY, no difference beyond the noise |
| host CPU-seconds | 642.5 | 646.8 | +0.7% (-2.3 to +3.6) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.204 | +0.6% (-2.3 to +3.6) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.15 | 8.82 | +8.2% (+6.3 to +10.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7042 / 0.9 / 20.0 / 20.0; omni 7044 / 0.9 / 20.0 / 20.0
- rep 2 (omni then native): native 7044 / 0.8 / 20.0 / 20.0; omni 7046 / 0.9 / 20.0 / 20.0
- rep 3 (native then omni): native 7041 / 0.8 / 20.0 / 20.0; omni 7047 / 0.8 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,910 tps; base rate 1,037 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,909 | 2,935 | +0.9% (-0.3 to +2.2) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 3,037 | 3,038 | +0.0% (-0.3 to +0.4) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 21.5 | 4.16 | -80.7% (-323.0 to +161.6) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 547.9 | 431.5 | -21.3% (-40.6 to -1.9) | GAIN |
| latency, median (ms) | 0.935 | 0.953 | +1.9% (-0.2 to +3.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 16.3 | 12.1 | -25.5% (-52.6 to +1.7) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 26.8 | +34.2% (+24.7 to +43.7) | power given |
| server connections alive, most at once | 20.0 | 37.3 | +86.7% (+55.4 to +117.9) | power given |
| host CPU busy (share of the run) | 0.36 | 0.37 | +3.0% (+1.2 to +4.7) | power given |
| host CPU-seconds | 634.6 | 652.5 | +2.8% (+1.1 to +4.6) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.485 | 0.494 | +1.9% (+0.6 to +3.2) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.4 | 2.91 | +21.1% (+17.9 to +24.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 26.8 | +34.1% (+24.6 to +43.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 63, 60, 73; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2890 / 44.9 / 20.0 / 20.0; omni 2934 / 3.7 / 26.2 / 26.2
- rep 2 (omni then native): native 2921 / 6.2 / 20.0 / 20.0; omni 2940 / 4.6 / 26.6 / 26.5
- rep 3 (native then omni): native 2914 / 13.5 / 20.0 / 20.0; omni 2931 / 4.1 / 27.7 / 27.7

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,908 tps; base rate 286 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `25130545f054`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 840.0 | 838.5 | -0.2% (-0.5 to +0.1) | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 840.0 | 838.6 | -0.2% (-0.5 to +0.1) | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.57 | 4.46 | -2.4% (-17.2 to +12.4) | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.4 | 11.3 | -0.3% (-27.6 to +27.0) | STEADY, no difference beyond the noise |
| latency, median (ms) | 1.71 | 1.71 | +0.1% (-2.7 to +2.9) | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.23 | 2.22 | -0.4% (-8.0 to +7.1) | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.288 | 0.288 | +0.2% (-3.2 to +3.5) | STEADY, no difference beyond the noise |
| host CPU-seconds | 496.5 | 497.2 | +0.2% (-3.2 to +3.5) | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.31 | 1.32 | +0.3% (-3.3 to +3.9) | STEADY, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.45 | 2.07 | +43.2% (+36.3 to +50.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 842 / 4.9 / 20.0 / 20.0; omni 841 / 4.4 / 20.0 / 20.0
- rep 2 (omni then native): native 840 / 4.7 / 20.0 / 20.0; omni 837 / 4.7 / 20.0 / 20.0
- rep 3 (native then omni): native 838 / 4.2 / 20.0 / 20.0; omni 838 / 4.3 / 20.0 / 20.0

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
