# YCSB on MongoDB, a database's operator-set cache size: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Superseded on 2026-10-09.** This is the table of the first counted set (runs 37727968670, 37727976107, 37727983746, on the first give-back gate of `docs/YCSB_PREREGISTRATION.md`, "no page evicted in the last second"). Its audits showed every burst and c arm giving half the cache back before its first eviction (amendment 1); the second counted set on the amended gate replaced it in `results/live/V3_YCSB.md`. Kept whole, every row; nothing below is current.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37727968670 | `7ee471b4098e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 37727976107 | `7ee471b4098e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 37727983746 | `7ee471b4098e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,833 | 2,841 | +0.3% (-1.4 to +2.0) | -0.1% (-0.3 to +0.1) | +0.1% (-0.0 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,847 | 2,854 | +0.2% (-1.4 to +1.9) | -0.0% (-0.2 to +0.2) | +0.1% (+0.0 to +0.1) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.488 | 0.485 | -0.6% (-3.3 to +2.1) | +2.8% (-3.9 to +9.5) | +1.2% (-2.9 to +5.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.693 | 0.679 | -2.0% (-8.5 to +4.6) | +5.0% (-3.7 to +13.7) | +1.0% (-0.8 to +2.8) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.241 | 0.239 | -0.8% (-5.1 to +3.4) | +2.4% (+0.1 to +4.6) | +1.9% (-0.2 to +4.0) | no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 435.6 | -14.9% (-21.1 to -8.8) | -15.3% (-27.7 to -3.0) | -12.5% (-12.5 to -12.5) | **confirmed better** |
| bytes in the cache, mean (MB) | 415.6 | 357.0 | -14.1% (-19.6 to -8.6) | -14.4% (-26.1 to -2.7) | -11.7% (-12.3 to -11.1) | **confirmed better** |
| pages read into the cache (misses) | 458,716 | 533,512 | +16.3% (+5.1 to +27.5) | +16.5% (+1.2 to +31.8) | +10.0% (+8.8 to +11.2) | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.258 | +0.7% (-34.4 to +35.8) | +3.2% (-11.6 to +18.0) | +2.7% (-56.9 to +62.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 292.7 | 295.7 | +1.0% (-44.4 to +46.4) | +3.5% (-16.1 to +23.2) | +3.3% (-70.9 to +77.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.335 | 0.337 | +0.7% (-43.2 to +44.5) | +3.6% (-16.0 to +23.2) | +3.3% (-70.9 to +77.5) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 1.67 | +1.67 (+0.232 to +3.1) | +1.67 (-1.2 to +4.54) | +1 (+1 to +1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,726 | 2,757 | +1.1% (-1.2 to +3.5) | -0.1% (-0.2 to +0.1) | +0.0% (-0.1 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,735 | 2,765 | +1.1% (-1.2 to +3.4) | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.308 | 0.312 | +1.4% (-0.6 to +3.4) | +0.4% (-2.2 to +3.0) | -1.1% (-3.6 to +1.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.477 | 0.48 | +0.5% (-4.0 to +5.0) | +0.8% (-2.7 to +4.2) | -1.4% (-5.0 to +2.3) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.241 | 0.235 | -2.6% (-11.8 to +6.5) | +4.2% (+0.7 to +7.7) | +0.5% (-5.1 to +6.1) | no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 376.6 | -26.5% (-62.0 to +9.1) | -49.0% (-51.1 to -46.8) | -49.5% (-49.5 to -49.5) | no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 412.2 | 309.6 | -24.9% (-61.4 to +11.6) | -47.6% (-49.5 to -45.7) | -48.7% (-51.5 to -45.9) | no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 479,449 | 586,126 | +22.2% (-2.0 to +46.5) | +50.6% (+42.9 to +58.3) | +46.5% (+43.8 to +49.2) | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.181 | -0.9% (-27.7 to +25.9) | +9.2% (-1.5 to +19.8) | -3.8% (-41.1 to +33.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 224.7 | 220.5 | -1.8% (-32.9 to +29.2) | +11.1% (-4.4 to +26.6) | -5.0% (-50.4 to +40.4) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.26 | -2.8% (-32.0 to +26.4) | +11.1% (-4.3 to +26.6) | -5.0% (-50.4 to +40.3) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 5 | +5 (+5 to +5) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,852 | 2,849 | -0.1% (-0.3 to +0.1) | -0.1% (-0.4 to +0.1) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,861 | 2,859 | -0.1% (-0.2 to +0.1) | -0.1% (-0.4 to +0.2) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.457 | 0.458 | +0.1% (-2.6 to +2.9) | +1.6% (-1.0 to +4.1) | +0.7% (-0.4 to +1.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.669 | 0.67 | +0.1% (-6.7 to +7.0) | +1.5% (-2.7 to +5.7) | +0.3% (-1.1 to +1.8) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.241 | 0.246 | +2.2% (+0.8 to +3.6) | +2.7% (+0.8 to +4.7) | +3.7% (+2.3 to +5.0) | **confirmed WORSE** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 262.7 | -48.7% (-48.7 to -48.7) | -41.8% (-71.3 to -12.3) | -40.6% (-75.1 to -6.1) | **confirmed better** |
| bytes in the cache, mean (MB) | 398.6 | 210.3 | -47.2% (-50.9 to -43.6) | -40.0% (-70.9 to -9.1) | -38.6% (-74.6 to -2.7) | **confirmed better** |
| pages read into the cache (misses) | 175,012 | 277,156 | +58.4% (+50.8 to +66.0) | +50.0% (+13.0 to +87.0) | +45.5% (-7.2 to +98.1) | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.196 | -3.5% (-28.8 to +21.9) | +4.8% (-41.3 to +50.9) | +16.4% (-11.0 to +43.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 91.3 | 87.0 | -4.7% (-35.5 to +26.1) | +5.1% (-52.5 to +62.6) | +20.6% (-15.6 to +56.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.247 | -4.7% (-35.3 to +26.0) | +5.1% (-52.4 to +62.5) | +20.7% (-15.6 to +57.0) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4.33 (+2.9 to +5.77) | +4.67 (+1.8 to +7.54) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% (-0.1 to -0.0) | -0.1% (-0.2 to +0.0) | +0.0% (-0.6 to +0.7) | no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to -0.0) | +0.0% (-0.6 to +0.6) | no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.357 | 0.359 | +0.6% (-2.5 to +3.6) | +1.1% (-0.4 to +2.5) | -0.2% (-5.0 to +4.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.537 | 0.536 | -0.2% (-0.6 to +0.3) | +0.9% (-2.6 to +4.5) | -0.3% (-8.9 to +8.3) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.127 | 0.133 | +4.9% (+3.4 to +6.5) | +4.4% (-2.9 to +11.7) | +3.2% (-4.7 to +11.1) | no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 258.8 | -49.4% (-49.5 to -49.4) | -49.6% (-49.6 to -49.5) | -49.5% (-49.5 to -49.5) | **confirmed better** |
| bytes in the cache, mean (MB) | 415.5 | 216.2 | -48.0% (-51.2 to -44.7) | -48.1% (-50.2 to -46.0) | -48.0% (-50.4 to -45.5) | **confirmed better** |
| pages read into the cache (misses) | 468,164 | 727,442 | +55.4% (+43.3 to +67.4) | +52.9% (+29.9 to +75.9) | +57.7% (+46.2 to +69.2) | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.185 | +13.1% (-5.3 to +31.4) | +11.0% (-18.0 to +40.0) | +10.7% (-2.7 to +24.1) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 199.8 | 229.2 | +14.7% (-7.6 to +37.1) | +11.6% (-19.8 to +43.1) | +12.8% (-3.7 to +29.3) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.259 | +14.7% (-7.7 to +37.1) | +11.7% (-19.9 to +43.2) | +12.8% (-3.6 to +29.2) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,767 | 5,769 | +0.0% (-0.2 to +0.2) | -0.3% (-1.5 to +0.9) | -2.7% (-9.8 to +4.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,781 | 5,781 | +0.0% (-0.2 to +0.2) | -0.3% (-1.5 to +0.8) | -2.7% (-9.7 to +4.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.255 | 0.259 | +1.4% (-2.5 to +5.4) | +1.0% (+0.2 to +1.8) | +0.6% (-0.1 to +1.4) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.434 | 0.435 | +0.4% (-4.6 to +5.4) | -0.7% (-3.2 to +1.7) | -0.1% (-7.2 to +7.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.118 | 0.117 | -0.7% (-5.2 to +3.8) | +1.0% (-0.4 to +2.3) | +4.5% (-3.3 to +12.3) | no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 448.2 | -12.5% (-12.5 to -12.5) | -36.8% (-51.3 to -22.3) | -25.9% (-30.4 to -21.4) | **confirmed better** |
| bytes in the cache, mean (MB) | 415.2 | 369.5 | -11.0% (-11.5 to -10.5) | -36.6% (-51.8 to -21.4) | -24.4% (-28.5 to -20.3) | **confirmed better** |
| pages read into the cache (misses) | 465,847 | 531,465 | +14.1% (+8.4 to +19.8) | +48.5% (+27.8 to +69.2) | +25.3% (+1.7 to +49.0) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.161 | -6.3% (-32.7 to +20.1) | -0.6% (-4.3 to +3.2) | -7.5% (-11.9 to -3.2) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 210.4 | 193.9 | -7.8% (-39.2 to +23.5) | -0.9% (-5.8 to +4.1) | -9.1% (-13.7 to -4.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.109 | -7.9% (-39.3 to +23.5) | -0.7% (-5.3 to +4.0) | -6.6% (-14.4 to +1.1) | no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 1 | +1 (+1 to +1) | +4 (+4 to +4) | +2.67 (-0.202 to +5.54) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 6 gauge-rows confirmed better, 1 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
