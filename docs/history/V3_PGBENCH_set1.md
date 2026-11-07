# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Superseded on 2026-10-09.** This is the table of the first counted set (runs 37435740735, 37435751322, 37435761371, on amendment 1 of `docs/POSTGRES_PREREGISTRATION.md`). Its host-CPU cost was later measured and traced to the harness's own `psql` launches, and its median-latency cost to the pool shrunk into a queue (amendment 2); the second counted set on the amended harness replaced it in `results/live/V3_PGBENCH.md`. Kept whole, every row; nothing below is current.


PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any increase in any run is WORSE. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37435740735 | `bf26c1cebd84` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 37435751322 | `bf26c1cebd84` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 37435761371 | `bf26c1cebd84` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 16,366, 37,847, 16,293 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,199 | 6,795 | -5.6% (-20.2 to +9.0) | -0.5% (-1.4 to +0.4) | -6.3% (-22.5 to +9.8) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 7,199 | 7,181 | -0.2% (-1.2 to +0.7) | -0.0% (-0.2 to +0.1) | -0.1% (-0.3 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 2.66 | 142.9 | +5266.7% (-12868.4 to +23401.7) | +1374.5% (-341.7 to +3090.8) | +3429.2% (-7499.6 to +14357.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 13.0 | 300.3 | +2206.5% (-4663.9 to +9076.9) | +741.9% (-272.4 to +1756.3) | +1077.8% (-1464.1 to +3619.7) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.38 | 0.445 | +17.3% (+13.1 to +21.5) | +8.0% (+1.5 to +14.4) | +19.1% (+17.0 to +21.2) | **confirmed WORSE** |
| latency, mean (ms) | 0.878 | 17.1 | +1850.0% (-3999.5 to +7699.5) | +384.2% (-100.7 to +869.1) | +1479.5% (-2981.3 to +5940.4) | no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 7.51 | -61.1% (-71.2 to -51.1) | -63.0% (-66.5 to -59.4) | -62.3% (-78.3 to -46.3) | **confirmed better** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-22.9 to +39.6) | +3.3% (-22.5 to +29.2) | +6.7% (-22.0 to +35.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.352 | 0.435 | +23.5% (+22.6 to +24.5) | +13.4% (+8.8 to +18.1) | +22.9% (+19.1 to +26.6) | **confirmed WORSE** |
| host CPU-seconds | 350.7 | 445.8 | +27.1% (+26.0 to +28.3) | +13.7% (+8.7 to +18.7) | +26.3% (+21.6 to +30.9) | **confirmed WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.162 | 0.219 | +35.0% (+13.5 to +56.6) | +14.3% (+8.5 to +20.1) | +35.3% (+11.3 to +59.2) | **confirmed WORSE** |
| pool size, mean (the knob) | 20.0 | 7.58 | -62.1% (-65.1 to -59.1) | -63.5% (-71.8 to -55.1) | -63.8% (-69.7 to -58.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 4,446, 3,711, 3,787 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 997.4 | 1,252 | +25.6% (-78.9 to +130.0) | -5.4% (-13.0 to +2.3) | -12.5% (-21.7 to -3.4) | no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 1,858 | 1,907 | +2.6% (-5.2 to +10.4) | +0.1% (-0.9 to +1.1) | -0.5% (-1.4 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 3,122 | 1,249 | -60.0% (-139.7 to +19.7) | +634.5% (-523.6 to +1792.7) | +1390.9% (+233.9 to +2547.8) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 5,405 | 2,292 | -57.6% (-154.3 to +39.1) | +63.4% (-126.0 to +252.9) | +199.7% (+15.4 to +383.9) | no difference beyond the noise (2 of 3 runs) |
| latency, median (ms) | 36.4 | 18.4 | -49.4% (-439.6 to +340.9) | +20.7% (+16.8 to +24.6) | +25.8% (+22.4 to +29.2) | no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 564.7 | 246.2 | -56.4% (-189.0 to +76.2) | +144.9% (-93.8 to +383.6) | +434.6% (+18.7 to +850.6) | no difference beyond the noise (2 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 22.4 | +12.2% (+9.0 to +15.4) | -35.1% (-55.1 to -15.2) | -34.1% (-42.3 to -25.8) | **the runs disagree** |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+67.6 to +92.4) | +68.3% (+61.2 to +75.5) | +75.0% (+62.6 to +87.4) | **confirmed WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.365 | +18.7% (+10.9 to +26.5) | +24.6% (+22.2 to +27.0) | +23.6% (+19.1 to +28.1) | **confirmed WORSE** |
| host CPU-seconds | 360.6 | 425.7 | +18.0% (+11.6 to +24.5) | +28.0% (+24.9 to +31.1) | +27.1% (+22.1 to +32.2) | **confirmed WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.22 | 1.18 | -3.3% (-92.2 to +85.6) | +35.4% (+20.4 to +50.4) | +45.4% (+38.3 to +52.5) | no difference beyond the noise (1 of 3 runs) |
| pool size, mean (the knob) | 20.0 | 21.4 | +7.1% (+1.0 to +13.2) | -36.8% (-53.3 to -20.3) | -37.4% (-44.5 to -30.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,769, 1,907, 2,926 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,217 | 1,182 | -2.9% (-8.2 to +2.5) | -3.4% (-6.0 to -0.8) | -1.6% (-5.4 to +2.2) | no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 1,217 | 1,219 | +0.1% (-0.3 to +0.6) | +0.1% (-0.6 to +0.8) | -0.1% (-1.6 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 3.6 | 29.4 | +715.2% (-364.8 to +1795.3) | +442.7% (+134.6 to +750.9) | +409.2% (-659.7 to +1478.1) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 10.8 | 107.6 | +898.7% (-445.0 to +2242.4) | +145.1% (-73.8 to +364.0) | +235.9% (-209.3 to +681.0) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.3 | 1.49 | +15.2% (+7.8 to +22.5) | +23.2% (+13.5 to +32.9) | +3.8% (+0.1 to +7.5) | **confirmed WORSE** |
| latency, mean (ms) | 1.78 | 6.29 | +253.6% (-101.0 to +608.1) | +141.6% (+41.0 to +242.3) | +238.4% (-346.4 to +823.1) | no difference beyond the noise (2 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.4 | 5.97 | -69.2% (-92.2 to -46.3) | -71.5% (-86.3 to -56.8) | -69.3% (-98.4 to -40.2) | **confirmed better** |
| server connections alive, most at once | 20.0 | 29.0 | +45.0% (-52.0 to +142.0) | +15.0% (-17.9 to +47.9) | +18.3% (+11.2 to +25.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.313 | 0.359 | +14.7% (+12.8 to +16.6) | +24.2% (+20.6 to +27.9) | +14.6% (+8.3 to +20.9) | **confirmed WORSE** |
| host CPU-seconds | 364.3 | 418.0 | +14.8% (+12.7 to +16.8) | +25.1% (+21.5 to +28.7) | +14.6% (+8.0 to +21.2) | **confirmed WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.998 | 1.18 | +18.2% (+10.5 to +25.9) | +29.5% (+22.3 to +36.7) | +16.5% (+5.2 to +27.9) | **confirmed WORSE** |
| pool size, mean (the knob) | 20.0 | 6.07 | -69.6% (-83.2 to -56.0) | -72.4% (-77.2 to -67.5) | -68.8% (-96.6 to -41.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

**Across 3 workloads: 2 gauge-rows confirmed better, 11 confirmed worse, 1 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
