# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40235697056 | `5ce458c7e7d2` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40254205224 | `babd7a2ceac0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40276907808 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% (+0.5 to +1.7) | +1.2% (+0.9 to +1.5) | +0.7% (+0.1 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.798 | +1.1% (+0.6 to +1.5) | +1.2% (+1.1 to +1.3) | +0.7% (+0.1 to +1.2) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% (-0.8 to +0.7) | -0.0% (-0.2 to +0.2) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.1% (-1.7 to +1.6) | +0.2% (-0.4 to +0.8) | +0.0% (-0.4 to +0.5) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 1.17 | 1.13 | -3.9% (-5.9 to -2.0) | -3.8% (-5.7 to -1.9) | -2.2% (-5.1 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.7 | +2.6% (+1.5 to +3.7) | +3.2% (+1.9 to +4.5) | +1.4% (+0.8 to +2.1) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% (+0.9 to +3.0) | +2.4% (+1.4 to +3.5) | +1.2% (+0.8 to +1.6) | **power given in all three of our runs** |
| keys evicted | 138,152 | 133,247 | -3.6% (-5.3 to -1.8) | -4.1% (-4.5 to -3.6) | -2.0% (-4.1 to +0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.064 | 0.0581 | -9.2% (-37.5 to +19.1) | +4.9% (-57.0 to +66.8) | -7.1% (-34.1 to +19.8) | **the runs disagree** |
| host CPU-seconds | 113.2 | 102.1 | -9.8% (-39.8 to +20.1) | +5.0% (-60.5 to +70.4) | -7.9% (-38.1 to +22.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.213 | 0.19 | -10.8% (-41.0 to +19.4) | +3.7% (-61.8 to +69.3) | -8.6% (-39.2 to +22.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 22.3 | +22.3 (+19.5 to +25.2) | +22.3 (+19.5 to +25.2) | +16.3 (+8.74 to +23.9) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124.0 | 123.2 | -0.6% (-11.9 to +10.7) | +1.4% (-3.5 to +6.2) | -0.9% (-2.9 to +1.1) | **the runs disagree** |
| the server's own CPU-seconds (redis-server) | 17.3 | 17.2 | -0.6% (-15.7 to +14.6) | +0.5% (-1.9 to +2.9) | +0.5% (-0.1 to +1.0) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106.5 | 105.3 | -1.2% (-11.9 to +9.5) | +1.0% (-4.6 to +6.6) | -1.4% (-3.6 to +0.7) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.576 | +0.576 (+0.51 to +0.641) | +0.563 (+0.433 to +0.694) | +0.935 (+0.877 to +0.994) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.124 | -3.1% (-20.4 to +14.2) | -2.7% (-16.2 to +10.8) | -1.7% (-7.5 to +4.1) | shown, not judged |
| host CPU-seconds without steal | 113.2 | 102.1 | -9.8% (-39.8 to +20.1) | +5.0% (-60.5 to +70.4) | -7.9% (-38.1 to +22.3) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% (-0.3 to +0.1) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.3 to +0.2) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.0% (-0.1 to +0.2) | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% (-0.1 to +0.5) | +0.0% (-0.1 to +0.1) | +0.1% (-0.3 to +0.4) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% (+0.2 to +0.7) | +0.1% (-0.5 to +0.7) | +0.2% (-0.7 to +1.1) | STEADY, under the floor (the three runs' mean 0.25%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.3 | -2.6% (-2.9 to -2.4) | -2.2% (-2.4 to -1.9) | -2.4% (-3.1 to -1.7) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% (-1.5 to -0.9) | -0.7% (-1.0 to -0.4) | -1.0% (-1.7 to -0.2) | **GAIN in all three of our runs** |
| keys evicted | 71,738 | 72,379 | +0.9% (+0.3 to +1.5) | +0.9% (+0.7 to +1.1) | +0.9% (+0.9 to +0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.135 | -5.9% (-37.1 to +25.3) | -2.3% (-42.3 to +37.8) | -10.7% (-68.3 to +46.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 96.3 | 90.0 | -6.5% (-41.4 to +28.3) | -2.2% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.497 | 0.465 | -6.5% (-41.6 to +28.6) | -2.1% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123.2 | 123.3 | +0.1% (-1.6 to +1.8) | +0.1% (-0.8 to +1.1) | +0.4% (-2.5 to +3.2) | STEADY, under the floor (the three runs' mean 0.18%) |
| the server's own CPU-seconds (redis-server) | 15.4 | 15.3 | -0.8% (-3.5 to +2.0) | +0.7% (-0.0 to +1.4) | +0.6% (-3.9 to +5.2) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107.7 | 107.6 | -0.2% (-1.6 to +1.3) | -0.4% (-1.5 to +0.8) | -0.1% (-3.0 to +2.8) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.394 | +0.394 (+0.356 to +0.431) | +0.283 (+0.238 to +0.329) | +0.301 (+0.274 to +0.328) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0957 | 0.0947 | -1.1% (-7.4 to +5.2) | -2.9% (-5.0 to -0.9) | -0.3% (-1.0 to +0.5) | shown, not judged |
| host CPU-seconds without steal | 96.3 | 90.0 | -6.5% (-41.4 to +28.3) | -2.2% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,282 | +1.2% (+0.0 to +2.4) | +1.4% (+0.5 to +2.3) | +1.7% (+1.6 to +1.9) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.855 | +1.2% (+0.0 to +2.4) | +1.4% (+0.5 to +2.3) | +1.7% (+1.6 to +1.9) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% (-0.4 to +0.2) | -0.3% (-0.5 to +0.0) | -0.1% (-0.3 to +0.1) | STEADY, under the floor (the three runs' mean 0.17%) |
| latency, 99th percentile (ms) | 5.83 | 5.83 | +0.0% (-0.4 to +0.5) | -0.0% (-0.3 to +0.2) | +0.1% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 1.06 | 1.01 | -5.1% (-9.7 to -0.6) | -6.7% (-10.3 to -3.2) | -7.8% (-8.5 to -7.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.9 | +1.4% (-1.0 to +3.8) | +0.8% (-1.1 to +2.7) | +1.4% (-1.0 to +3.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% (-0.3 to +1.7) | +0.5% (-1.4 to +2.4) | +1.0% (-0.8 to +2.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| keys evicted | 103,556 | 96,760 | -6.6% (-13.1 to +0.0) | -7.6% (-12.4 to -2.8) | -9.3% (-10.1 to -8.6) | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.118 | -5.2% (-33.3 to +22.8) | -11.2% (-24.8 to +2.4) | +16.6% (-5.6 to +38.7) | **the runs disagree** |
| host CPU-seconds | 207.6 | 195.6 | -5.7% (-37.9 to +26.4) | -12.1% (-26.5 to +2.3) | +18.9% (-6.0 to +43.7) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.339 | -6.9% (-38.4 to +24.7) | -13.4% (-27.0 to +0.3) | +16.8% (-7.5 to +41.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+12.4 to +29.6) | +21 (+16 to +26) | +22.3 (+19.5 to +25.2) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288.0 | 286.8 | -0.4% (-2.6 to +1.7) | -1.0% (-1.2 to -0.9) | -0.1% (-2.4 to +2.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (redis-server) | 38.4 | 38.3 | -0.1% (-5.1 to +4.8) | -1.1% (-3.6 to +1.5) | -0.2% (-1.2 to +0.7) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249.4 | 247.2 | -0.9% (-2.7 to +1.0) | -1.5% (-1.7 to -1.2) | -0.5% (-3.0 to +1.9) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.986 | +0.986 (+0.916 to +1.06) | +0.698 (+0.66 to +0.735) | +0.757 (+0.738 to +0.776) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.242 | 0.237 | -1.9% (-7.3 to +3.4) | -2.8% (-6.0 to +0.5) | -0.6% (-5.7 to +4.4) | shown, not judged |
| host CPU-seconds without steal | 207.6 | 195.6 | -5.7% (-37.9 to +26.4) | -12.1% (-26.5 to +2.3) | +18.9% (-6.0 to +43.7) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run B: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); left native (11 trials, 0 allowed, 2 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.9 | 937.7 | +1.3% (+1.1 to +1.4) | +1.0% (-0.7 to +2.7) | +1.3% (+1.1 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.618 | 0.625 | +1.3% (+1.1 to +1.4) | +1.0% (-0.7 to +2.7) | +1.3% (+1.1 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.0% (-0.0 to +0.1) | +0.0% (-0.2 to +0.3) | +0.0% (-0.0 to +0.1) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.56 | 5.57 | +0.1% (+0.1 to +0.1) | +0.2% (-0.3 to +0.6) | +0.2% (+0.1 to +0.3) | STEADY, under the floor (the three runs' mean 0.16%) |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% (-2.4 to -1.4) | -1.4% (-3.4 to +0.7) | -1.7% (-2.0 to -1.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+1.4 to +3.0) | +1.8% (-0.4 to +4.1) | +2.2% (+2.1 to +2.3) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% (+1.6 to +2.4) | +1.3% (-0.3 to +3.0) | +1.9% (+1.3 to +2.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 243,043 | 236,704 | -2.6% (-6.1 to +0.9) | -0.8% (-1.8 to +0.2) | -2.6% (-6.1 to +0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.105 | -2.4% (-53.9 to +49.0) | +1.0% (-17.5 to +19.6) | +9.7% (-3.0 to +22.4) | **the runs disagree** |
| host CPU-seconds | 188.6 | 183.5 | -2.7% (-60.3 to +54.8) | +1.2% (-21.4 to +23.8) | +11.4% (-3.6 to +26.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.435 | -4.0% (-61.1 to +53.2) | +0.3% (-23.8 to +24.3) | +10.1% (-5.1 to +25.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 14.0 | +14 (+11.5 to +16.5) | +15.3 (+12.5 to +18.2) | +14 (+9.7 to +18.3) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 204.2 | 204.6 | +0.2% (-0.7 to +1.1) | +0.3% (-2.4 to +3.0) | +0.3% (-0.3 to +1.0) | STEADY, under the floor (the three runs' mean 0.26%) |
| the server's own CPU-seconds (redis-server) | 24.6 | 24.4 | -0.6% (-0.8 to -0.5) | +1.2% (-2.8 to +5.2) | -0.3% (-3.3 to +2.8) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179.5 | 179.3 | -0.1% (-1.0 to +0.9) | -0.2% (-2.7 to +2.4) | +0.1% (-1.1 to +1.2) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.702 | +0.702 (+0.642 to +0.761) | +0.943 (+0.899 to +0.986) | +0.924 (+0.818 to +1.03) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.163 | 0.159 | -2.1% (-3.4 to -0.7) | -1.8% (-16.1 to +12.5) | -1.0% (-4.5 to +2.6) | shown, not judged |
| host CPU-seconds without steal | 188.6 | 183.5 | -2.7% (-60.3 to +54.8) | +1.2% (-21.4 to +23.8) | +11.4% (-3.6 to +26.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run B: acting: 64 to 80 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); left native (9 trials, 0 allowed, 1 refused); run C: acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 12 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 6 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
