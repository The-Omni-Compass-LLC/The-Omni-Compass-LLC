# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40236918458 | `23c7e8eb27be` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40259304209 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40281469940 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,873 | -0.1% (-0.6 to +0.4) | -0.1% (-0.2 to +0.1) | -0.1% (-0.7 to +0.4) | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (operations a second) | 2,886 | 2,883 | -0.1% (-0.6 to +0.4) | -0.1% (-0.2 to +0.1) | -0.1% (-0.7 to +0.5) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 0.361 | 0.363 | +0.6% (-0.6 to +1.7) | +0.5% (-1.2 to +2.2) | +0.0% (-3.1 to +3.1) | STEADY, under the floor (the three runs' mean 0.35%) |
| latency, 99th percentile (ms) | 0.578 | 0.582 | +0.7% (-3.8 to +5.2) | +0.8% (-0.6 to +2.3) | -0.3% (-4.9 to +4.2) | STEADY, under the floor (the three runs' mean 0.40%) |
| latency, mean (ms) | 0.221 | 0.221 | +0.2% (-0.5 to +0.9) | +0.5% (-1.4 to +2.3) | -0.5% (-1.9 to +0.8) | STEADY, under the floor (the three runs' mean 0.04%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 529.9 | +3.5% (-2.5 to +9.5) | +4.5% (-6.2 to +15.2) | +7.2% (-8.2 to +22.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 417.4 | 431.9 | +3.5% (-2.2 to +9.2) | +4.3% (-6.1 to +14.7) | +7.0% (-7.6 to +21.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 678,119 | 663,562 | -2.1% (-5.6 to +1.3) | -3.4% (-13.0 to +6.1) | -5.2% (-19.9 to +9.6) | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.272 | +8.3% (-3.4 to +20.1) | +3.6% (-24.3 to +31.5) | +0.4% (-34.0 to +34.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 439.0 | 488.0 | +11.2% (-4.3 to +26.7) | +4.8% (-33.6 to +43.1) | +0.5% (-44.1 to +45.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.331 | 0.368 | +11.3% (-3.8 to +26.3) | +4.8% (-33.5 to +43.2) | +0.6% (-44.4 to +45.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 9 | +9 (+6.52 to +11.5) | +11.7 (+7.87 to +15.5) | +11 (+8.52 to +13.5) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275.2 | 276.5 | +0.5% (-1.1 to +2.0) | +0.9% (+0.2 to +1.7) | -0.1% (-1.6 to +1.4) | STEADY, under the floor (the three runs' mean 0.43%) |
| the server's own CPU-seconds (mongod) | 272.6 | 273.3 | +0.2% (-1.3 to +1.8) | +0.7% (-0.1 to +1.4) | -0.3% (-1.9 to +1.2) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.24 | +24.1% (+16.6 to +31.5) | +25.8% (+23.0 to +28.5) | +22.2% (+16.4 to +28.0) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 439.0 | 488.0 | +11.2% (-4.3 to +26.7) | +4.8% (-33.6 to +43.1) | +0.5% (-44.1 to +45.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 576 (5 trials, 1 allowed, 0 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 2 refused); run B: acting: 512 to 640 (8 trials, 2 allowed, 1 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); run C: acting: 512 to 640 (7 trials, 2 allowed, 0 refused); acting: 512 to 640 (6 trials, 2 allowed, 0 refused); left native (7 trials, 0 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.334 | 0.332 | -0.7% (-2.6 to +1.2) | +1.5% (-2.0 to +4.9) | +2.3% (-6.7 to +11.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.588 | 0.582 | -1.1% (-2.3 to +0.1) | +1.2% (-1.8 to +4.3) | +2.4% (-4.5 to +9.3) | **the runs disagree** |
| latency, mean (ms) | 0.2 | 0.199 | -0.6% (-5.7 to +4.4) | +0.7% (-1.8 to +3.2) | +1.4% (-3.4 to +6.3) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 510.2 | -0.4% (-0.4 to -0.3) | -0.3% (-0.4 to -0.3) | -0.3% (-0.4 to -0.2) | STEADY, under the floor (the three runs' mean 0.33%) |
| bytes in the cache, mean (MB) | 417.0 | 415.8 | -0.3% (-0.8 to +0.2) | +0.2% (-0.6 to +1.0) | +0.5% (-1.2 to +2.1) | STEADY, under the floor (the three runs' mean 0.12%) |
| pages read into the cache (misses) | 712,186 | 673,332 | -5.5% (-17.3 to +6.4) | +2.8% (-19.2 to +24.7) | +5.6% (-5.6 to +16.8) | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.182 | -14.5% (-24.2 to -4.9) | -2.5% (-17.6 to +12.7) | -1.6% (-38.9 to +35.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 377.1 | 310.0 | -17.8% (-29.8 to -5.8) | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.284 | 0.233 | -17.8% (-29.8 to -5.8) | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +2.67 (-0.202 to +5.54) | +2 (+2 to +2) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199.3 | 198.6 | -0.4% (-7.9 to +7.2) | +1.3% (-1.9 to +4.6) | +2.0% (-3.5 to +7.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 196.8 | 195.5 | -0.7% (-8.3 to +7.0) | +1.1% (-2.2 to +4.4) | +1.8% (-3.9 to +7.5) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.11 | +23.3% (+17.9 to +28.7) | +21.7% (+17.3 to +26.1) | +23.8% (+16.6 to +31.0) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 377.1 | 310.0 | -17.8% (-29.8 to -5.8) | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% (-0.3 to +0.1) | -0.0% (-0.2 to +0.1) | +0.1% (-0.4 to +0.7) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,938 | 2,935 | -0.1% (-0.3 to +0.1) | -0.0% (-0.1 to +0.1) | +0.1% (-0.4 to +0.7) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.257 | 0.266 | +3.8% (-6.9 to +14.4) | +0.2% (-2.9 to +3.2) | +5.4% (-7.8 to +18.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.425 | 0.445 | +4.9% (+1.0 to +8.8) | +0.4% (-4.4 to +5.2) | +2.5% (-0.4 to +5.5) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 0.0832 | 0.0883 | +6.2% (+4.4 to +7.9) | -0.2% (-2.3 to +1.9) | -4.0% (-10.7 to +2.7) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 506.1 | -1.2% (-2.2 to -0.1) | +0.6% (-3.3 to +4.5) | +2.9% (-9.2 to +15.0) | **the runs disagree** |
| bytes in the cache, mean (MB) | 406.3 | 406.8 | +0.1% (-1.0 to +1.3) | +0.8% (-4.5 to +6.1) | +4.2% (-6.8 to +15.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 271,839 | 274,828 | +1.1% (-10.3 to +12.5) | +6.1% (+1.3 to +10.8) | -0.3% (-14.2 to +13.6) | shown, not judged |
| host CPU busy (share of the run) | 0.081 | 0.1 | +23.6% (-97.2 to +144.4) | -14.6% (-46.2 to +17.1) | -9.0% (-74.5 to +56.4) | **the runs disagree** |
| host CPU-seconds | 58.2 | 73.5 | +26.3% (-107.3 to +159.9) | -17.7% (-57.0 to +21.6) | -10.6% (-86.3 to +65.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.109 | 0.137 | +26.4% (-107.2 to +160.0) | -17.7% (-56.9 to +21.6) | -10.6% (-86.3 to +65.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.67 | +4.67 (-2.92 to +12.3) | +7.33 (+4.46 to +10.2) | +7 (+0.427 to +13.6) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 26.4 | 28.0 | +6.1% (-7.2 to +19.4) | -0.0% (-3.4 to +3.4) | +1.0% (-2.2 to +4.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 25.7 | 27.1 | +5.3% (-8.6 to +19.1) | -0.3% (-3.6 to +3.1) | +0.7% (-2.4 to +3.8) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.67 | 0.924 | +37.9% (+24.3 to +51.5) | +21.2% (+12.6 to +29.9) | +20.0% (+12.3 to +27.6) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 58.2 | 73.5 | +26.3% (-107.3 to +159.9) | -17.7% (-57.0 to +21.7) | -10.6% (-86.3 to +65.2) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run C: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,889 | -0.0% (-0.1 to +0.1) | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.1) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% (-0.1 to +0.1) | +0.0% (-0.0 to +0.1) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.309 | 0.308 | -0.2% (-1.4 to +1.0) | -0.3% (-2.0 to +1.3) | -0.9% (-3.5 to +1.7) | STEADY, under the floor (the three runs' mean 0.47%) |
| latency, 99th percentile (ms) | 0.489 | 0.488 | -0.1% (-4.2 to +4.0) | +0.0% (-1.3 to +1.3) | -0.9% (-3.6 to +1.8) | STEADY, under the floor (the three runs' mean 0.31%) |
| latency, mean (ms) | 0.19 | 0.189 | -0.2% (-1.4 to +1.1) | +0.6% (-2.2 to +3.4) | -0.6% (-5.9 to +4.7) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 517.1 | +1.0% (-6.9 to +8.9) | -0.4% (-0.8 to -0.1) | -0.6% (-1.3 to +0.1) | **the runs disagree** |
| bytes in the cache, mean (MB) | 418.4 | 422.0 | +0.9% (-5.9 to +7.6) | +0.3% (-0.7 to +1.2) | -0.3% (-2.1 to +1.6) | STEADY, under the floor (the three runs' mean 0.29%) |
| pages read into the cache (misses) | 687,996 | 663,759 | -3.5% (-32.7 to +25.6) | +5.2% (-14.8 to +25.1) | +1.8% (-12.6 to +16.2) | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.182 | -0.2% (-28.0 to +27.6) | -3.8% (-18.2 to +10.6) | -3.1% (-24.4 to +18.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 316.6 | 315.7 | -0.3% (-34.4 to +33.8) | -4.7% (-23.2 to +13.8) | -3.6% (-28.6 to +21.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.238 | 0.237 | -0.3% (-34.4 to +33.8) | -4.7% (-23.2 to +13.7) | -3.6% (-28.7 to +21.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 5 | +5 (-2.45 to +12.5) | +2.67 (-0.202 to +5.54) | +4.33 (-0.838 to +9.5) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186.4 | 186.3 | -0.0% (-0.9 to +0.9) | +1.1% (-2.5 to +4.8) | +0.2% (-7.9 to +8.4) | STEADY, under the floor (the three runs' mean 0.44%) |
| the server's own CPU-seconds (mongod) | 184.0 | 183.4 | -0.3% (-1.2 to +0.5) | +0.9% (-2.9 to +4.6) | -0.1% (-8.3 to +8.1) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.38 | 2.89 | +21.1% (+15.9 to +26.4) | +19.9% (+17.1 to +22.8) | +22.9% (+18.8 to +26.9) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 316.6 | 315.7 | -0.3% (-34.4 to +33.8) | -4.7% (-23.2 to +13.8) | -3.6% (-28.6 to +21.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,686 | 5,691 | +0.1% (-0.3 to +0.5) | +0.1% (-0.3 to +0.6) | -0.1% (-0.4 to +0.2) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (operations a second) | 5,700 | 5,705 | +0.1% (-0.3 to +0.5) | +0.2% (-0.3 to +0.6) | -0.1% (-0.4 to +0.2) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.411 | 0.41 | -0.2% (-1.5 to +1.0) | -0.7% (-3.0 to +1.6) | +4.5% (-16.8 to +25.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.599 | 0.595 | -0.6% (-1.6 to +0.3) | +0.2% (-1.8 to +2.1) | +1.4% (-8.3 to +11.1) | **the runs disagree** |
| latency, mean (ms) | 0.231 | 0.231 | -0.3% (-1.3 to +0.6) | -0.9% (-4.0 to +2.3) | +2.6% (-8.7 to +13.9) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 533.7 | +4.2% (-6.2 to +14.7) | +5.5% (-7.1 to +18.0) | +2.6% (-11.1 to +16.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 417.0 | 434.6 | +4.2% (-6.2 to +14.6) | +5.4% (-6.9 to +17.6) | +2.8% (-9.5 to +15.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 691,520 | 664,630 | -3.9% (-12.4 to +4.6) | -3.7% (-16.0 to +8.6) | -0.8% (-12.2 to +10.6) | shown, not judged |
| host CPU busy (share of the run) | 0.311 | 0.311 | -0.3% (-3.3 to +2.8) | -1.4% (-11.8 to +9.0) | +17.2% (-29.8 to +64.3) | **the runs disagree** |
| host CPU-seconds | 565.2 | 562.5 | -0.5% (-4.8 to +3.9) | -1.9% (-16.4 to +12.5) | +19.5% (-33.1 to +72.0) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.213 | 0.212 | -0.5% (-4.8 to +3.7) | -2.0% (-16.8 to +12.7) | +19.6% (-33.1 to +72.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 11.0 | +11 (+8.52 to +13.5) | +11 (+6.03 to +16) | +6.67 (+3.8 to +9.54) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 346.4 | 346.4 | +0.0% (-0.8 to +0.8) | -0.7% (-4.1 to +2.7) | +4.1% (-12.0 to +20.2) | **the runs disagree** |
| the server's own CPU-seconds (mongod) | 342.1 | 341.5 | -0.2% (-1.1 to +0.7) | -0.9% (-4.2 to +2.5) | +3.7% (-12.5 to +19.9) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.31 | 4.92 | +14.1% (+6.0 to +22.2) | +12.9% (+1.9 to +23.8) | +24.3% (+10.7 to +38.0) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 565.2 | 562.5 | -0.5% (-4.8 to +3.9) | -1.9% (-16.4 to +12.5) | +19.5% (-33.1 to +72.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 640 (6 trials, 2 allowed, 0 refused); acting: 512 to 576 (7 trials, 1 allowed, 1 refused); left native (6 trials, 0 allowed, 2 refused); run B: left native (5 trials, 0 allowed, 2 refused); acting: 512 to 640 (9 trials, 2 allowed, 1 refused); acting: 512 to 640 (6 trials, 2 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused).

**Across 4 untouched workloads: 6 gauge-rows GAIN, 2 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 STEADY, 17 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
