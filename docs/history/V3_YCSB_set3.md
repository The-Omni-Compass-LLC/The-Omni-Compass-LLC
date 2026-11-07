# YCSB on MongoDB, a database's operator-set cache size: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013343689 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 38013348512 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 38013353044 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% (-0.2 to +0.0) | -0.0% (-0.9 to +0.9) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% (-0.2 to +0.1) | -0.0% (-0.9 to +0.8) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.316 | 0.319 | +1.1% (-3.4 to +5.5) | +1.1% (-4.8 to +7.0) | -0.6% (-4.4 to +3.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.54 | 0.549 | +1.8% (-0.5 to +4.1) | -0.6% (-4.6 to +3.5) | -1.1% (-4.2 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.149 | 0.148 | -0.1% (-1.0 to +0.8) | +2.0% (-3.1 to +7.2) | -1.0% (-5.0 to +2.9) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 466.6 | -8.9% (-23.4 to +5.7) | -12.6% (-14.5 to -10.8) | -10.5% (-17.7 to -3.4) | no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 417.5 | 382.6 | -8.4% (-22.0 to +5.3) | -12.2% (-14.0 to -10.3) | -9.8% (-17.4 to -2.3) | no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 682,918 | 738,387 | +8.1% (-8.1 to +24.4) | +12.8% (+11.2 to +14.3) | +11.0% (+5.2 to +16.8) | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.206 | +6.5% (-28.6 to +41.6) | -0.5% (-9.5 to +8.5) | -1.1% (-21.8 to +19.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 355.3 | 384.7 | +8.3% (-36.7 to +53.3) | -1.4% (-12.6 to +9.8) | -1.4% (-26.2 to +23.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.289 | +8.3% (-36.7 to +53.3) | -1.5% (-12.3 to +9.4) | -1.4% (-26.4 to +23.6) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (+1.23 to +4.1) | +2.67 (+1.23 to +4.1) | +3.67 (+0.798 to +6.54) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); run C: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% (-0.1 to -0.0) | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.0) | no difference beyond the noise (1 of 3 runs) |
| throughput (operations a second) | 2,899 | 2,898 | -0.1% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.0) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.343 | 0.341 | -0.5% (-8.9 to +7.9) | +2.1% (-2.5 to +6.7) | +2.8% (-2.3 to +7.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.508 | 0.511 | +0.6% (-1.1 to +2.3) | +1.5% (-0.4 to +3.4) | +0.4% (-2.8 to +3.5) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.203 | 0.204 | +0.2% (-2.7 to +3.0) | +0.3% (-3.7 to +4.4) | +1.5% (-4.3 to +7.3) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 466.0 | -9.0% (-27.0 to +9.0) | -8.3% (-24.4 to +7.7) | -12.2% (-12.4 to -12.0) | no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 419.4 | 381.9 | -8.9% (-24.4 to +6.5) | -7.5% (-23.0 to +7.9) | -12.0% (-12.8 to -11.2) | no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 732,882 | 736,004 | +0.4% (-21.5 to +22.4) | +10.8% (-14.4 to +36.0) | +4.8% (-15.8 to +25.3) | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.19 | -3.2% (-16.0 to +9.6) | +12.9% (-4.1 to +30.0) | -7.8% (-74.2 to +58.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 339.4 | 325.8 | -4.0% (-18.9 to +10.8) | +16.0% (-4.1 to +36.0) | -9.7% (-87.8 to +68.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.245 | -4.0% (-18.8 to +10.8) | +16.0% (-4.0 to +36.0) | -9.7% (-87.8 to +68.4) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (+1.23 to +4.1) | +2.67 (+1.23 to +4.1) | +2.67 (+1.23 to +4.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,804 | 2,686 | -4.2% (-16.2 to +7.7) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to -0.0) | no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,815 | 2,698 | -4.1% (-16.0 to +7.7) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to -0.0) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.344 | 0.351 | +2.1% (-3.0 to +7.3) | +0.2% (-2.6 to +3.1) | +0.5% (-0.8 to +1.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.529 | 0.572 | +8.2% (-5.7 to +22.1) | -0.4% (-2.8 to +2.1) | +0.2% (-0.5 to +0.8) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.226 | 0.25 | +10.9% (-14.9 to +36.7) | +0.2% (-0.9 to +1.2) | +1.0% (+0.4 to +1.7) | no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 455.0 | -11.1% (-29.6 to +7.3) | -9.5% (-18.6 to -0.4) | -14.8% (-22.4 to -7.2) | no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 397.2 | 353.2 | -11.1% (-25.7 to +3.5) | -10.2% (-17.8 to -2.5) | -15.2% (-24.2 to -6.2) | no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 260,725 | 238,666 | -8.5% (-25.9 to +9.0) | +6.6% (-3.2 to +16.5) | +7.6% (-11.4 to +26.7) | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.141 | +0.6% (-66.0 to +67.3) | -8.8% (-60.0 to +42.4) | -9.5% (-104.7 to +85.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 100.6 | 102.0 | +1.4% (-76.2 to +79.0) | -11.2% (-73.7 to +51.3) | -12.7% (-121.9 to +96.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.207 | +5.8% (-60.6 to +72.3) | -11.2% (-73.7 to +51.3) | -12.7% (-121.9 to +96.5) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (+1.23 to +4.1) | +3.67 (+2.23 to +5.1) | +3 (-1.3 to +7.3) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (3 trials, 2 allowed, 1 refused); acting: 384 to 512 (3 trials, 2 allowed, 1 refused); run C: acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% (-0.1 to -0.1) | -0.0% (-0.2 to +0.2) | -0.1% (-0.6 to +0.5) | no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,899 | 2,896 | -0.1% (-0.1 to -0.1) | -0.0% (-0.2 to +0.1) | -0.1% (-0.6 to +0.5) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.342 | 0.345 | +0.9% (-2.9 to +4.7) | -1.0% (-4.1 to +2.1) | +1.2% (-4.9 to +7.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.517 | 0.518 | +0.1% (-4.0 to +4.2) | -0.8% (-2.1 to +0.5) | +0.4% (-4.4 to +5.2) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.204 | 0.205 | +0.6% (-0.5 to +1.7) | +5.2% (-9.9 to +20.4) | -1.0% (-16.4 to +14.5) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 485.9 | -5.1% (-20.4 to +10.2) | -4.3% (-21.3 to +12.7) | -12.7% (-15.8 to -9.5) | no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 416.3 | 399.3 | -4.1% (-18.9 to +10.8) | -4.8% (-20.5 to +11.0) | -12.2% (-18.3 to -6.2) | no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 721,790 | 715,451 | -0.9% (-23.8 to +22.1) | +3.7% (-15.1 to +22.4) | +13.9% (-5.1 to +32.8) | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.176 | -1.8% (-24.3 to +20.7) | +12.1% (-47.7 to +72.0) | +0.1% (-55.8 to +56.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 306.0 | 297.8 | -2.7% (-29.7 to +24.3) | +14.4% (-55.5 to +84.3) | -0.6% (-66.5 to +65.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.224 | -2.7% (-29.7 to +24.3) | +14.3% (-55.6 to +84.3) | -0.6% (-66.7 to +65.4) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (-0.128 to +7.46) | +3 (+0.516 to +5.48) | +1.33 (-0.101 to +2.77) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run C: acting: 448 to 512 (1 trials, 1 allowed, 0 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,688 | 5,678 | -0.2% (-1.1 to +0.7) | -0.1% (-0.3 to +0.1) | -1.3% (-6.9 to +4.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,705 | 5,696 | -0.2% (-1.1 to +0.7) | -0.1% (-0.4 to +0.2) | -1.3% (-6.8 to +4.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.439 | 0.443 | +0.9% (-3.1 to +4.9) | +0.2% (-2.0 to +2.4) | +0.3% (-0.4 to +1.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.664 | 0.673 | +1.3% (-7.0 to +9.6) | +0.5% (-2.4 to +3.4) | +1.1% (-1.6 to +3.7) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.255 | 0.257 | +0.9% (-3.1 to +4.9) | +0.8% (-4.5 to +6.1) | +4.0% (+0.1 to +7.8) | no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 446.7 | -12.8% (-15.2 to -10.3) | -13.4% (-15.8 to -10.9) | -3.3% (-5.3 to -1.3) | **confirmed better** |
| bytes in the cache, mean (MB) | 417.3 | 365.3 | -12.4% (-15.2 to -9.7) | -12.7% (-15.0 to -10.4) | -3.6% (-5.5 to -1.7) | **confirmed better** |
| pages read into the cache (misses) | 679,207 | 773,228 | +13.8% (+11.8 to +15.9) | +12.6% (+9.0 to +16.2) | +2.2% (-8.7 to +13.0) | shown, not judged |
| host CPU busy (share of the run) | 0.284 | 0.285 | +0.2% (-3.1 to +3.4) | +2.6% (-14.5 to +19.6) | +3.8% (-10.8 to +18.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 481.2 | 481.6 | +0.1% (-5.7 to +5.9) | +2.9% (-18.5 to +24.3) | +4.9% (-14.4 to +24.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.182 | 0.182 | +0.2% (-4.7 to +5.0) | +2.9% (-18.6 to +24.4) | +6.5% (-16.4 to +29.5) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (+1.23 to +4.1) | +2.33 (+0.899 to +3.77) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 384 to 512 (3 trials, 2 allowed, 0 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 0 refused); acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 384 to 512 (3 trials, 2 allowed, 0 refused).

**Across 4 untouched workloads: 2 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
