# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any increase in any run is marked. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054777807 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 38054782696 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 38054787517 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,882 | -0.2% (-0.8 to +0.4) | -1.1% (-10.1 to +7.8) | -0.1% (-0.9 to +0.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,898 | 2,891 | -0.2% (-0.9 to +0.4) | -1.2% (-9.9 to +7.6) | -0.1% (-0.9 to +0.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.366 | 0.365 | -0.3% (-0.3 to -0.3) | +2.1% (-3.2 to +7.3) | +0.8% (+0.1 to +1.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.613 | 0.61 | -0.5% (-2.7 to +1.8) | +2.2% (-7.0 to +11.5) | -0.2% (-0.5 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.224 | 0.225 | +0.2% (-0.9 to +1.4) | +1.4% (-29.2 to +32.0) | +1.4% (-0.3 to +3.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 449.2 | -12.3% (-12.7 to -11.9) | -9.3% (-24.7 to +6.1) | -12.2% (-12.2 to -12.2) | STEADY, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 417.4 | 368.6 | -11.7% (-12.1 to -11.2) | -8.6% (-21.3 to +4.2) | -11.5% (-11.7 to -11.4) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 677,075 | 759,667 | +12.2% (+8.3 to +16.1) | +6.6% (-12.0 to +25.1) | +12.9% (+8.1 to +17.7) | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.239 | +3.6% (-29.3 to +36.5) | -2.9% (-30.9 to +25.2) | -2.0% (-24.0 to +20.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 399.5 | 417.1 | +4.4% (-39.2 to +48.0) | -3.9% (-37.5 to +29.8) | -3.2% (-30.9 to +24.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.314 | +4.6% (-39.6 to +48.8) | -2.7% (-28.5 to +23.1) | -3.1% (-31.0 to +24.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+0.798 to +6.54) | +2.67 (+1.23 to +4.1) | +3 (+3 to +3) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (4 trials, 1 allowed, 2 refused); run B: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% (-0.1 to +0.0) | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.218 | 0.219 | +0.5% (-20.4 to +21.3) | -1.7% (-7.1 to +3.8) | -3.4% (-27.0 to +20.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.352 | 0.357 | +1.5% (-14.5 to +17.6) | +0.1% (-6.5 to +6.6) | -4.5% (-23.8 to +14.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.083 | 0.0839 | +1.1% (-3.1 to +5.3) | -1.1% (-4.0 to +1.8) | -1.7% (-10.3 to +6.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 444.9 | -13.1% (-15.6 to -10.6) | -12.1% (-12.4 to -11.9) | -8.6% (-26.7 to +9.5) | STEADY, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 419.9 | 366.1 | -12.8% (-18.9 to -6.8) | -12.5% (-14.0 to -11.0) | -9.0% (-24.7 to +6.8) | STEADY, no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 694,101 | 794,493 | +14.5% (-6.8 to +35.7) | +3.1% (-2.2 to +8.4) | +6.5% (-22.5 to +35.5) | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.125 | +10.8% (-15.2 to +36.8) | -9.4% (-39.0 to +20.2) | +9.1% (-17.1 to +35.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 206.5 | 232.1 | +12.4% (-18.1 to +42.9) | -11.0% (-46.5 to +24.5) | +10.3% (-19.1 to +39.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.173 | +12.4% (-18.1 to +42.9) | -11.0% (-46.4 to +24.4) | +10.3% (-19.2 to +39.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 1.67 | +1.67 (+0.232 to +3.1) | +2.67 (+1.23 to +4.1) | +1.67 (+0.232 to +3.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: acting: 448 to 512 (1 trials, 1 allowed, 0 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,889 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.0) | -0.0% (-0.1 to -0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,897 | 2,895 | -0.0% (-0.1 to +0.1) | -0.1% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.423 | 0.43 | +1.7% (+0.5 to +2.8) | +0.5% (-0.1 to +1.1) | +1.4% (-1.2 to +4.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.559 | 0.565 | +1.2% (+0.2 to +2.2) | +2.6% (+0.5 to +4.6) | +1.2% (-4.5 to +6.8) | STEADY, no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 0.219 | 0.223 | +1.4% (-1.6 to +4.5) | -0.1% (-3.2 to +3.0) | +0.8% (-0.6 to +2.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 451.9 | -11.7% (-11.8 to -11.6) | -12.5% (-14.9 to -10.2) | -10.0% (-16.3 to -3.7) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 407.6 | 354.9 | -12.9% (-15.0 to -10.9) | -13.4% (-15.7 to -11.1) | -10.0% (-14.1 to -5.9) | **GAIN in all three of our runs** |
| pages read into the cache (misses) | 275,598 | 299,411 | +8.6% (-10.0 to +27.3) | +8.0% (-3.1 to +19.0) | +4.5% (-29.3 to +38.3) | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.172 | -5.5% (-38.1 to +27.1) | -1.2% (-31.7 to +29.3) | -2.1% (-117.6 to +113.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 124.7 | 115.8 | -7.2% (-44.7 to +30.4) | -1.2% (-38.2 to +35.7) | -3.0% (-136.0 to +130.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.234 | 0.218 | -7.1% (-44.8 to +30.5) | -1.2% (-38.2 to +35.8) | -3.0% (-136.0 to +130.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3 | +3 (+3 to +3) | +4 (+1.52 to +6.48) | +3 (-1.97 to +7.97) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run B: acting: 384 to 512 (3 trials, 2 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.1% (-0.1 to -0.0) | -0.0% (-7.2 to +7.2) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% (-0.1 to -0.0) | -0.0% (-7.1 to +7.1) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.308 | 0.31 | +0.9% (-0.1 to +1.8) | +1.9% (+0.7 to +3.1) | +0.1% (-5.8 to +6.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.478 | 0.48 | +0.3% (-1.5 to +2.2) | +1.1% (-2.2 to +4.5) | +0.1% (-0.7 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.195 | 0.198 | +1.5% (-1.5 to +4.5) | +8.5% (-9.9 to +26.8) | +0.2% (-5.4 to +5.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 464.6 | -9.3% (-20.8 to +2.3) | -5.0% (-20.6 to +10.7) | -5.0% (-24.3 to +14.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| bytes in the cache, mean (MB) | 417.3 | 383.8 | -8.0% (-21.1 to +5.1) | -5.0% (-20.7 to +10.7) | -4.4% (-20.9 to +12.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 691,164 | 787,717 | +14.0% (-1.6 to +29.5) | +1.3% (-22.6 to +25.3) | +4.1% (-24.6 to +32.8) | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.17 | +2.8% (-33.4 to +39.0) | -6.1% (-49.9 to +37.8) | +7.1% (-11.8 to +26.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 280.1 | 288.4 | +2.9% (-41.3 to +47.2) | -7.0% (-57.3 to +43.3) | +8.6% (-13.0 to +30.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.216 | +2.9% (-41.3 to +47.2) | -7.0% (-54.5 to +40.5) | +8.6% (-13.0 to +30.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (-2.3 to +6.3) | +3.67 (+2.23 to +5.1) | +2.33 (+0.899 to +3.77) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (3 trials, 2 allowed, 1 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,696 | 5,697 | +0.0% (-0.5 to +0.5) | -0.0% (-0.2 to +0.1) | -0.2% (-0.5 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,711 | 5,711 | +0.0% (-0.5 to +0.5) | -0.0% (-0.2 to +0.1) | -0.1% (-0.5 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.437 | 0.433 | -1.1% (-4.8 to +2.7) | +0.6% (-1.6 to +2.7) | -0.8% (-2.9 to +1.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.635 | 0.629 | -1.0% (-3.0 to +1.0) | -0.1% (-1.2 to +1.1) | -0.6% (-1.3 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.254 | 0.251 | -1.2% (-5.3 to +2.9) | +0.8% (+0.2 to +1.3) | -1.0% (-3.5 to +1.5) | STEADY, no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 443.9 | -13.3% (-15.7 to -10.9) | -14.7% (-20.0 to -9.4) | -12.8% (-15.2 to -10.3) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 417.2 | 363.7 | -12.8% (-14.3 to -11.3) | -14.2% (-19.5 to -8.9) | -12.1% (-14.1 to -10.2) | **GAIN in all three of our runs** |
| pages read into the cache (misses) | 677,539 | 785,502 | +15.9% (+11.3 to +20.6) | +16.8% (+11.4 to +22.3) | +14.7% (+11.9 to +17.5) | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% (-7.0 to +6.1) | -0.3% (-20.8 to +20.2) | -0.7% (-8.8 to +7.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 472.9 | 470.9 | -0.4% (-9.6 to +8.7) | -0.7% (-26.8 to +25.4) | -0.7% (-11.5 to +10.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.178 | -0.5% (-10.1 to +9.1) | -0.7% (-26.7 to +25.3) | -0.6% (-11.1 to +10.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.33 | +2.33 (+0.899 to +3.77) | +2.33 (+0.899 to +3.77) | +2.67 (+1.23 to +4.1) | shown, not judged |

The cache size handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused); run B: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 384 to 512 (3 trials, 2 allowed, 0 refused); run C: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 384 to 512 (2 trials, 2 allowed, 0 refused).

**Across 4 untouched workloads: 4 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 40 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
