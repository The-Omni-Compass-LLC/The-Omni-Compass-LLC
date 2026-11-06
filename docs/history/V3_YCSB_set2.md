# YCSB on MongoDB, a database's operator-set cache size: the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37858512907 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 37858515717 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 37858519010 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | -0.0% (-0.2 to +0.1) | -0.1% (-0.4 to +0.1) | -0.0% (-1.2 to +1.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,888 | 2,886 | -0.1% (-0.2 to +0.1) | -0.2% (-0.4 to +0.1) | -0.1% (-1.3 to +1.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.333 | 0.334 | +0.3% (-1.7 to +2.3) | +2.0% (-2.5 to +6.5) | +0.7% (-0.7 to +2.0) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.486 | 0.482 | -0.9% (-3.3 to +1.5) | +1.5% (-3.9 to +6.9) | -1.6% (-4.8 to +1.6) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.188 | 0.186 | -1.1% (-6.4 to +4.2) | +2.2% (-3.9 to +8.3) | +0.9% (-1.6 to +3.5) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 388.9 | -24.0% (-24.2 to -23.9) | -20.0% (-36.9 to -3.1) | -22.1% (-30.3 to -14.0) | **confirmed better** |
| bytes in the cache, mean (MB) | 415.0 | 317.7 | -23.4% (-25.1 to -21.8) | -19.3% (-36.1 to -2.4) | -21.2% (-29.2 to -13.2) | **confirmed better** |
| pages read into the cache (misses) | 464,294 | 577,605 | +24.4% (+16.3 to +32.5) | +24.3% (+7.2 to +41.5) | +25.5% (+13.9 to +37.1) | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.218 | -5.0% (-18.6 to +8.6) | +7.0% (-7.8 to +21.8) | -1.0% (-15.0 to +13.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 283.2 | 264.4 | -6.6% (-25.6 to +12.3) | +8.8% (-10.4 to +28.0) | -1.7% (-20.6 to +17.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.321 | 0.299 | -6.6% (-25.6 to +12.4) | +8.9% (-10.3 to +28.0) | -1.8% (-21.7 to +18.2) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +3 (-1.3 to +7.3) | +2.67 (-0.202 to +5.54) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,856 | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | +0.0% (-0.4 to +0.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,864 | 2,862 | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.0) | -0.0% (-0.3 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.406 | 0.406 | -0.1% (-1.5 to +1.3) | +1.1% (-0.7 to +2.9) | -1.3% (-3.6 to +0.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.568 | 0.565 | -0.5% (-7.1 to +6.0) | -0.3% (-11.7 to +11.1) | -5.2% (-13.0 to +2.6) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.213 | 0.215 | +1.1% (-1.3 to +3.6) | +2.1% (-2.6 to +6.7) | -2.4% (-8.9 to +4.1) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 368.8 | -28.0% (-45.1 to -10.8) | -35.9% (-35.9 to -35.9) | -28.0% (-45.1 to -10.9) | **confirmed better** |
| bytes in the cache, mean (MB) | 414.8 | 301.8 | -27.2% (-45.6 to -8.9) | -36.2% (-39.2 to -33.1) | -27.3% (-44.1 to -10.5) | **confirmed better** |
| pages read into the cache (misses) | 488,743 | 613,152 | +25.5% (+5.5 to +45.4) | +32.3% (+19.1 to +45.5) | +23.5% (-2.7 to +49.6) | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.213 | +1.0% (-16.9 to +18.8) | +0.9% (-58.7 to +60.5) | -2.4% (-55.1 to +50.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 240.5 | 242.1 | +0.7% (-21.4 to +22.7) | +0.5% (-68.1 to +69.1) | -2.5% (-62.8 to +57.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.275 | +0.7% (-21.4 to +22.7) | +0.5% (-68.1 to +69.0) | -2.5% (-62.6 to +57.5) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.33 | +2.33 (+0.899 to +3.77) | +3 (+3 to +3) | +2.33 (+0.899 to +3.77) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,611 | 2,737 | +4.8% (-14.3 to +23.9) | -0.0% (-0.3 to +0.3) | +0.0% (-0.2 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,625 | 2,747 | +4.6% (-13.9 to +23.2) | -0.0% (-0.3 to +0.3) | +0.0% (-0.1 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.347 | 0.346 | -0.2% (-9.3 to +8.9) | +0.1% (-2.0 to +2.1) | +0.2% (-0.8 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.629 | 0.549 | -12.7% (-52.1 to +26.8) | -0.8% (-6.7 to +5.1) | -0.3% (-4.5 to +3.9) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.252 | 0.231 | -8.2% (-35.8 to +19.3) | +1.4% (-2.2 to +4.9) | +1.1% (-2.8 to +5.0) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 404.5 | -21.0% (-24.1 to -17.9) | -22.4% (-22.7 to -22.1) | -26.2% (-42.1 to -10.3) | **confirmed better** |
| bytes in the cache, mean (MB) | 387.0 | 305.1 | -21.2% (-28.9 to -13.5) | -21.5% (-23.2 to -19.8) | -26.6% (-44.3 to -8.9) | **confirmed better** |
| pages read into the cache (misses) | 178,538 | 200,667 | +12.4% (-25.9 to +50.6) | +21.6% (+12.9 to +30.3) | +21.9% (+10.4 to +33.4) | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.183 | +7.0% (-49.4 to +63.4) | +3.6% (-30.5 to +37.7) | -11.9% (-35.4 to +11.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 83.7 | 89.7 | +7.2% (-58.8 to +73.2) | +4.3% (-38.1 to +46.7) | -15.0% (-44.1 to +14.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.268 | +3.0% (-48.9 to +54.9) | +4.3% (-38.1 to +46.7) | -15.0% (-44.2 to +14.2) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.33 | +2.33 (+0.899 to +3.77) | +2 (+2 to +2) | +2.33 (+0.899 to +3.77) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,898 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,902 | 2,900 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.278 | 0.281 | +0.8% (-6.9 to +8.5) | +0.6% (-0.4 to +1.6) | -0.1% (-0.7 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.426 | 0.425 | -0.2% (-2.8 to +2.3) | +0.5% (-2.7 to +3.8) | +0.2% (-2.0 to +2.3) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.107 | 0.11 | +2.3% (+0.9 to +3.8) | +2.3% (+1.7 to +2.8) | +1.1% (-1.5 to +3.6) | no difference beyond the noise (1 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 389.1 | -24.0% (-24.1 to -23.9) | -24.0% (-24.1 to -23.9) | -24.0% (-24.0 to -24.0) | **confirmed better** |
| bytes in the cache, mean (MB) | 416.3 | 319.7 | -23.2% (-25.5 to -21.0) | -22.8% (-24.4 to -21.3) | -22.3% (-24.4 to -20.2) | **confirmed better** |
| pages read into the cache (misses) | 466,300 | 583,886 | +25.2% (+12.0 to +38.5) | +29.6% (+22.5 to +36.6) | +28.5% (+1.5 to +55.6) | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.146 | +1.5% (-39.8 to +42.8) | +7.6% (-28.3 to +43.4) | -4.3% (-28.7 to +20.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 176.1 | 178.6 | +1.4% (-46.9 to +49.7) | +8.8% (-36.6 to +54.2) | -5.9% (-36.6 to +24.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.201 | +1.4% (-46.9 to +49.7) | +8.8% (-36.6 to +54.2) | -5.9% (-36.5 to +24.7) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +2 (+2 to +2) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,656 | 5,601 | -1.0% (-4.2 to +2.3) | -0.2% (-1.6 to +1.2) | -0.1% (-0.5 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,675 | 5,618 | -1.0% (-4.1 to +2.1) | -0.2% (-1.6 to +1.2) | -0.2% (-0.6 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.344 | 0.347 | +0.8% (-2.9 to +4.5) | +0.9% (-2.5 to +4.3) | -0.6% (-1.7 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.55 | 0.546 | -0.8% (-9.2 to +7.5) | -0.4% (-4.7 to +3.9) | -3.5% (-11.0 to +4.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.211 | 0.214 | +1.7% (-2.3 to +5.7) | +0.5% (-2.9 to +4.0) | +0.2% (-5.9 to +6.3) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 327.9 | -35.9% (-36.4 to -35.5) | -28.0% (-45.1 to -10.8) | -36.1% (-36.4 to -35.7) | **confirmed better** |
| bytes in the cache, mean (MB) | 412.9 | 265.7 | -35.6% (-37.3 to -34.0) | -28.0% (-45.1 to -10.8) | -36.2% (-36.3 to -36.0) | **confirmed better** |
| pages read into the cache (misses) | 472,245 | 674,851 | +42.9% (+31.1 to +54.8) | +35.3% (+8.9 to +61.8) | +43.8% (+38.3 to +49.4) | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.275 | +2.6% (-10.4 to +15.6) | +1.3% (-2.4 to +4.9) | +2.1% (-37.3 to +41.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 325.7 | 336.8 | +3.4% (-16.0 to +22.9) | +0.9% (-4.3 to +6.0) | +2.0% (-45.4 to +49.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.194 | +4.4% (-11.8 to +20.6) | +0.9% (-2.8 to +4.6) | +2.0% (-45.2 to +49.3) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3 | +3 (+3 to +3) | +2.33 (+0.899 to +3.77) | +3 (+3 to +3) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 8 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
