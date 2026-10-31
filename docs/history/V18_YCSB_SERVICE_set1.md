# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **STEADY, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40105166483 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40106352563 | `1aa4ebd3855c` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40109893975 | `00f7839c8b98` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,931 | -0.0% (-0.2 to +0.1) | -0.1% (-0.3 to +0.2) | +0.0% (-0.3 to +0.4) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | +0.0% (-0.4 to +0.4) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.157 | 0.162 | +3.0% (-3.4 to +9.3) | +8.6% (+3.7 to +13.4) | +0.7% (-6.2 to +7.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.371 | 0.38 | +2.4% (-4.3 to +9.1) | +4.2% (-0.2 to +8.6) | +0.3% (-10.6 to +11.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0835 | 0.0831 | -0.5% (-11.7 to +10.8) | +2.0% (-4.9 to +9.0) | +1.2% (-6.6 to +8.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.5 | -0.9% (-1.4 to -0.3) | -0.7% (-1.2 to -0.3) | -1.2% (-2.7 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 419.0 | 417.0 | -0.5% (-1.3 to +0.3) | -0.3% (-1.1 to +0.5) | -0.9% (-2.0 to +0.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 680,563 | 692,262 | +1.7% (-2.5 to +5.9) | -0.7% (-5.6 to +4.2) | +0.4% (-3.5 to +4.3) | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.112 | -10.6% (-51.0 to +29.7) | +6.9% (-79.4 to +93.2) | -0.1% (-11.5 to +11.4) | **the runs disagree** |
| host CPU-seconds | 227.7 | 201.5 | -11.5% (-56.2 to +33.2) | +7.2% (-88.9 to +103.2) | -0.7% (-13.3 to +11.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.151 | -11.5% (-56.3 to +33.3) | +7.2% (-88.9 to +103.3) | -0.8% (-13.7 to +12.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.33 (+0.465 to +6.2) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.0) | -0.0% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 0.318 | 0.321 | +1.2% (-1.4 to +3.7) | -0.3% (-5.3 to +4.7) | +1.7% (-43.0 to +46.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.578 | 0.568 | -1.8% (-5.1 to +1.4) | +0.2% (-7.0 to +7.4) | +3.6% (-15.7 to +23.0) | **the runs disagree** |
| latency, mean (ms) | 0.196 | 0.197 | +0.1% (-1.7 to +1.9) | +0.1% (-2.8 to +3.0) | +0.9% (-15.3 to +17.1) | STEADY, under the floor (the three runs' mean 0.36%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.7 | -0.8% (-1.4 to -0.3) | -0.6% (-1.2 to -0.1) | -0.7% (-1.3 to -0.0) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 415.7 | 415.5 | -0.0% (-1.4 to +1.3) | -0.2% (-3.2 to +2.8) | -0.2% (-3.0 to +2.6) | STEADY, under the floor (the three runs' mean 0.16%) |
| pages read into the cache (misses) | 690,444 | 688,640 | -0.3% (-7.5 to +6.9) | +1.9% (-19.9 to +23.7) | -1.3% (-7.4 to +4.7) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.199 | -3.5% (-43.1 to +36.1) | -2.3% (-38.1 to +33.5) | +20.7% (-41.4 to +82.8) | **the runs disagree** |
| host CPU-seconds | 365.3 | 348.2 | -4.7% (-55.2 to +45.8) | -2.7% (-46.4 to +41.0) | +22.7% (-45.5 to +90.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.274 | 0.262 | -4.7% (-55.3 to +45.8) | -2.7% (-46.5 to +41.1) | +22.7% (-45.3 to +90.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+2.23 to +5.1) | +3 (+0.516 to +5.48) | +3.33 (+0.465 to +6.2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,935 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.1% (-0.4 to +0.6) | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (operations a second) | 2,938 | 2,938 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.1% (-0.4 to +0.6) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.234 | 0.239 | +2.3% (-1.0 to +5.5) | +0.2% (-4.4 to +4.8) | -0.2% (-1.1 to +0.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.406 | 0.415 | +2.1% (-7.9 to +12.0) | +1.1% (-2.7 to +4.9) | -0.7% (-3.2 to +1.8) | **the runs disagree** |
| latency, mean (ms) | 0.08 | 0.0813 | +1.6% (-0.9 to +4.2) | +0.3% (-2.5 to +3.2) | -0.2% (-3.2 to +2.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 504.4 | -1.5% (-2.5 to -0.5) | -1.5% (-1.7 to -1.3) | -2.6% (-5.0 to -0.1) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 407.7 | 401.4 | -1.6% (-4.7 to +1.6) | +0.4% (-2.9 to +3.6) | -1.6% (-5.6 to +2.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 263,170 | 275,392 | +4.6% (-2.1 to +11.4) | +2.8% (-5.5 to +11.1) | +8.2% (+5.4 to +11.0) | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0824 | -25.3% (-154.7 to +104.1) | -13.9% (-45.8 to +18.0) | -6.4% (-41.6 to +28.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 82.4 | 59.5 | -27.9% (-168.4 to +112.7) | -17.7% (-58.2 to +22.7) | -7.9% (-51.7 to +36.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.111 | -27.9% (-168.3 to +112.6) | -17.7% (-58.2 to +22.7) | -8.0% (-51.5 to +35.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+0.465 to +6.2) | +4 (+4 to +4) | +4.67 (+3.23 to +6.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,909 | -0.0% (-0.5 to +0.4) | -0.1% (-0.1 to -0.0) | +0.0% (-0.2 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,914 | 2,913 | -0.0% (-0.5 to +0.4) | -0.1% (-0.1 to +0.0) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.187 | 0.19 | +1.6% (+0.3 to +2.9) | +0.4% (-0.4 to +1.1) | -8.7% (-40.3 to +22.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.359 | 0.362 | +0.8% (-2.3 to +4.0) | +0.2% (-4.6 to +5.0) | -5.2% (-21.9 to +11.5) | **the runs disagree** |
| latency, mean (ms) | 0.136 | 0.138 | +0.8% (-6.2 to +7.8) | -0.3% (-2.9 to +2.3) | -4.9% (-19.9 to +10.1) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 510.2 | -0.4% (-0.5 to -0.2) | -0.4% (-0.5 to -0.3) | -0.4% (-0.5 to -0.3) | STEADY, under the floor (the three runs' mean 0.39%) |
| bytes in the cache, mean (MB) | 418.9 | 419.3 | +0.1% (-2.8 to +3.0) | +0.3% (-1.0 to +1.7) | -0.0% (-3.3 to +3.2) | STEADY, under the floor (the three runs' mean 0.13%) |
| pages read into the cache (misses) | 680,367 | 739,183 | +8.6% (-3.8 to +21.1) | +1.1% (-11.3 to +13.4) | -3.0% (-28.9 to +22.9) | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.149 | -4.2% (-31.3 to +22.8) | -11.6% (-69.8 to +46.6) | +6.8% (-18.0 to +31.6) | **the runs disagree** |
| host CPU-seconds | 281.2 | 266.4 | -5.3% (-36.4 to +25.9) | -13.4% (-82.2 to +55.3) | +7.6% (-18.9 to +34.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.199 | -5.3% (-36.4 to +25.8) | -13.5% (-82.2 to +55.3) | +7.6% (-18.9 to +34.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +2 (+2 to +2) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,665 | 5,673 | +0.2% (-0.7 to +1.0) | -0.1% (-0.4 to +0.1) | -0.1% (-0.3 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (operations a second) | 5,683 | 5,691 | +0.1% (-0.7 to +1.0) | -0.2% (-0.4 to +0.1) | -0.1% (-0.4 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.437 | 0.436 | -0.4% (-2.5 to +1.8) | +0.7% (-2.3 to +3.8) | -0.2% (-18.4 to +18.0) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 0.673 | 0.668 | -0.7% (-3.4 to +2.0) | +0.2% (-2.5 to +2.8) | -0.3% (-9.5 to +8.9) | STEADY, under the floor (the three runs' mean 0.26%) |
| latency, mean (ms) | 0.25 | 0.249 | -0.4% (-3.5 to +2.8) | +0.4% (-2.9 to +3.7) | -0.8% (-8.5 to +6.9) | STEADY, under the floor (the three runs' mean 0.24%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 505.2 | -1.3% (-4.0 to +1.3) | -0.6% (-1.2 to -0.0) | -2.0% (-4.0 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 416.1 | 412.0 | -1.0% (-3.3 to +1.3) | -0.3% (-0.3 to -0.2) | -1.5% (-3.3 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 682,202 | 692,171 | +1.5% (-0.6 to +3.5) | +0.6% (-0.7 to +1.8) | +3.6% (-0.8 to +8.1) | shown, not judged |
| host CPU busy (share of the run) | 0.333 | 0.329 | -1.3% (-5.6 to +3.1) | +0.4% (-2.8 to +3.6) | +4.3% (-44.2 to +52.8) | **the runs disagree** |
| host CPU-seconds | 604.5 | 593.1 | -1.9% (-7.8 to +4.0) | +0.5% (-3.1 to +4.2) | +5.5% (-50.1 to +61.1) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.224 | -2.1% (-7.8 to +3.6) | +0.6% (-3.0 to +4.1) | +5.5% (-50.3 to +61.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused).

**Across 4 untouched workloads: 8 gauge-rows GAIN, 3 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 19 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
