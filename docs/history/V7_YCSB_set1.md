# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38935435045 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| B | 38947615453 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |
| C | 38957530830 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,902 | -0.1% (-1.0 to +0.8) | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,915 | 2,912 | -0.1% (-0.9 to +0.7) | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.279 | 0.28 | +0.5% (-1.4 to +2.3) | -0.5% (-2.5 to +1.5) | +0.3% (-2.0 to +2.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.462 | 0.456 | -1.4% (-7.1 to +4.2) | -0.1% (-3.1 to +3.0) | -1.0% (-2.7 to +0.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.194 | 0.195 | +0.6% (-9.8 to +10.9) | -0.0% (-5.6 to +5.5) | -0.7% (-8.1 to +6.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.5 | -0.7% (-0.9 to -0.5) | -1.2% (-2.9 to +0.6) | -1.2% (-3.2 to +0.8) | STEADY, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 417.4 | 413.4 | -0.9% (-2.5 to +0.6) | -0.8% (-2.7 to +1.1) | -0.8% (-3.1 to +1.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 679,673 | 679,772 | +0.0% (-1.1 to +1.2) | +0.6% (-2.9 to +4.1) | +1.8% (-2.3 to +5.9) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.185 | +7.4% (-25.7 to +40.5) | -1.6% (-8.4 to +5.2) | -1.2% (-52.5 to +50.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 303.2 | 329.7 | +8.7% (-30.8 to +48.2) | -2.0% (-10.3 to +6.2) | -1.9% (-60.5 to +56.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.248 | +8.8% (-30.1 to +47.7) | -2.0% (-10.3 to +6.2) | -2.0% (-60.6 to +56.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% (-0.1 to -0.0) | -0.1% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% (-0.1 to -0.0) | -0.1% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.6% (-1.1 to +4.2) | -0.1% (-4.6 to +4.4) | +0.5% (-7.1 to +8.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.483 | 0.492 | +2.0% (-4.6 to +8.6) | +0.7% (-2.1 to +3.5) | +0.5% (-1.2 to +2.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.197 | 0.202 | +2.5% (-1.6 to +6.7) | +1.4% (-1.0 to +3.8) | +1.4% (-1.9 to +4.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 503.2 | -1.7% (-4.4 to +0.9) | -5.2% (-21.0 to +10.6) | -1.0% (-1.3 to -0.7) | STEADY, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 418.5 | 411.3 | -1.7% (-5.2 to +1.7) | -4.8% (-19.7 to +10.0) | -1.5% (-3.9 to +0.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 697,708 | 688,177 | -1.4% (-21.8 to +19.1) | +3.4% (-15.2 to +22.1) | +0.6% (-11.3 to +12.6) | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.189 | +6.3% (-28.7 to +41.2) | -2.6% (-58.7 to +53.4) | +2.9% (-39.7 to +45.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 303.9 | 324.8 | +6.9% (-35.1 to +48.9) | -3.0% (-70.3 to +64.3) | +3.1% (-48.0 to +54.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.244 | +6.9% (-35.1 to +48.9) | -3.0% (-70.2 to +64.2) | +3.1% (-48.0 to +54.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.33 (+1.9 to +4.77) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,889 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to -0.0) | -3.3% (-11.5 to +5.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | -3.2% (-11.6 to +5.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.5 | 0.498 | -0.3% (-0.6 to +0.0) | -0.2% (-1.1 to +0.7) | +1.4% (-2.4 to +5.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.636 | 0.637 | +0.1% (-1.4 to +1.5) | +0.0% (-3.1 to +3.1) | +3.8% (-0.6 to +8.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.228 | 0.228 | -0.1% (-2.2 to +2.1) | -0.4% (-4.4 to +3.5) | +4.4% (+0.6 to +8.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 503.6 | -1.6% (-2.6 to -0.7) | -2.9% (-5.8 to -0.1) | -1.6% (-6.6 to +3.5) | STEADY, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 401.6 | 399.8 | -0.4% (-4.2 to +3.3) | -3.4% (-6.7 to -0.2) | -0.3% (-5.6 to +5.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 264,592 | 272,124 | +2.8% (-1.7 to +7.4) | +1.0% (-8.7 to +10.7) | -7.6% (-26.1 to +10.9) | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.147 | -12.0% (-46.4 to +22.4) | -0.8% (-115.6 to +114.0) | -2.3% (-42.7 to +38.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 112.8 | 96.9 | -14.1% (-54.2 to +26.0) | -2.9% (-131.4 to +125.7) | -3.2% (-48.9 to +42.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.182 | -14.1% (-54.3 to +26.2) | -2.9% (-131.5 to +125.7) | +0.4% (-37.4 to +38.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.33 (+1.9 to +4.77) | +5.67 (+4.23 to +7.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (3 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% (-0.2 to +0.1) | -0.2% (-0.6 to +0.2) | -0.0% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% (-0.2 to +0.1) | -0.2% (-0.4 to +0.1) | -0.0% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.32 | 0.319 | -0.4% (-2.4 to +1.5) | +10.0% (-9.7 to +29.6) | -1.1% (-9.6 to +7.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.491 | 0.488 | -0.5% (-2.6 to +1.6) | +10.2% (-13.3 to +33.8) | -1.1% (-5.3 to +3.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.201 | 0.202 | +0.2% (-1.1 to +1.6) | +12.4% (-10.7 to +35.5) | -0.7% (-7.4 to +5.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.2 | -0.7% (-2.1 to +0.6) | -1.4% (-4.2 to +1.4) | -4.3% (-21.3 to +12.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| bytes in the cache, mean (MB) | 418.0 | 418.8 | +0.2% (-0.9 to +1.2) | -1.1% (-5.3 to +3.0) | -3.0% (-20.8 to +14.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 684,013 | 704,742 | +3.0% (-25.3 to +31.3) | -0.7% (-18.1 to +16.8) | +6.4% (-24.7 to +37.5) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.17 | -1.5% (-12.6 to +9.6) | +44.1% (-8.7 to +97.0) | +8.4% (+0.4 to +16.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 291.7 | 285.7 | -2.0% (-14.8 to +10.7) | +48.8% (-6.7 to +104.2) | +10.4% (+1.9 to +19.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.215 | -2.0% (-14.9 to +10.8) | +48.9% (-6.9 to +104.8) | +10.4% (+1.8 to +19.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +3 (+0.516 to +5.48) | +2.33 (+0.899 to +3.77) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,741 | 5,740 | -0.0% (-0.3 to +0.2) | -0.0% (-0.3 to +0.3) | +0.1% (-0.4 to +0.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,761 | 5,760 | -0.0% (-0.2 to +0.2) | -0.0% (-0.3 to +0.3) | +0.1% (-0.4 to +0.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.356 | 0.357 | +0.4% (-3.1 to +3.9) | +0.1% (-1.3 to +1.5) | +0.8% (-2.0 to +3.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.656 | 0.655 | -0.2% (-4.2 to +3.9) | +0.0% (-0.4 to +0.4) | +0.4% (-0.5 to +1.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.171 | 0.171 | +0.3% (-2.8 to +3.4) | -0.2% (-1.9 to +1.5) | +0.6% (-2.2 to +3.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 500.8 | -2.2% (-8.2 to +3.8) | -1.1% (-1.3 to -0.9) | -1.7% (-4.6 to +1.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 416.2 | 409.1 | -1.7% (-7.2 to +3.8) | -0.7% (-1.3 to -0.0) | -1.1% (-3.7 to +1.5) | STEADY, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 692,812 | 706,764 | +2.0% (-4.6 to +8.6) | -0.2% (-1.7 to +1.3) | +2.9% (+0.5 to +5.3) | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.237 | +1.9% (-11.4 to +15.1) | -1.2% (-13.3 to +10.9) | +1.3% (-4.6 to +7.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 419.2 | 429.7 | +2.5% (-13.5 to +18.6) | -1.6% (-18.3 to +15.2) | +1.4% (-6.6 to +9.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.158 | 0.162 | +2.5% (-13.9 to +18.8) | -1.6% (-18.1 to +14.8) | +1.2% (-6.4 to +8.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 44 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
