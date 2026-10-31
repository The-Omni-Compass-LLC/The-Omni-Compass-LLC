# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38933440763 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| B | 38945586160 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| C | 38955596458 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% (+0.5 to +1.0) | +0.9% (+0.5 to +1.4) | +1.1% (+0.9 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.79 | 0.796 | +0.8% (+0.5 to +1.0) | +0.9% (+0.4 to +1.5) | +1.2% (+1.0 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% (-0.0 to +0.0) | +0.0% (-0.3 to +0.3) | +0.0% (-0.4 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.72 | 5.73 | +0.1% (-0.0 to +0.1) | +1.0% (-1.6 to +3.7) | +0.1% (-0.8 to +0.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.31 | 1.28 | -2.4% (-3.5 to -1.2) | -2.9% (-4.8 to -1.0) | -3.8% (-5.7 to -1.9) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.1 | +1.8% (+0.7 to +2.9) | +2.1% (+0.1 to +4.1) | +2.6% (+1.5 to +3.7) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.0 | +1.4% (+0.8 to +2.0) | +1.6% (+0.0 to +3.2) | +2.0% (+1.4 to +2.6) | **power given in all three of our runs** |
| keys evicted | 138,020 | 134,806 | -2.3% (-3.4 to -1.3) | -3.2% (-5.7 to -0.7) | -3.9% (-4.4 to -3.3) | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.134 | -2.1% (-52.5 to +48.2) | +5.4% (-14.6 to +25.5) | +21.5% (-2.0 to +45.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 240.6 | 234.2 | -2.7% (-60.1 to +54.8) | +6.5% (-16.5 to +29.4) | +23.0% (-1.3 to +47.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.436 | -3.4% (-60.9 to +54.1) | +5.5% (-17.5 to +28.5) | +21.6% (-2.9 to +46.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 17.7 | +17.7 (+10.1 to +25.3) | +19 (+10.4 to +27.6) | +22.3 (+19.5 to +25.2) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); left native (11 trials, 0 allowed, 0 refused); run C: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (15 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% (-0.1 to -0.0) | -0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.1) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.1 to -0.0) | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.71 | 5.71 | +0.0% (-0.3 to +0.4) | +0.0% (-0.1 to +0.2) | -0.1% (-0.3 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% (-0.0 to +0.3) | +0.2% (+0.1 to +0.3) | +0.1% (-0.1 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.72 | 1.72 | +0.3% (-0.1 to +0.8) | +0.2% (-0.7 to +1.1) | +0.2% (-1.3 to +1.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.5 | -2.3% (-2.6 to -2.1) | -2.5% (-2.9 to -2.0) | -2.5% (-3.0 to -2.1) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% (-1.2 to -0.8) | -1.2% (-1.7 to -0.7) | -1.3% (-1.7 to -0.8) | **GAIN in all three of our runs** |
| keys evicted | 71,672 | 71,802 | +0.2% (+0.0 to +0.3) | +0.0% (-0.6 to +0.6) | +0.0% (-0.1 to +0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.129 | +9.1% (-8.6 to +26.9) | +22.3% (-2.5 to +47.2) | +19.0% (-22.0 to +60.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 79.0 | 86.9 | +10.0% (-9.9 to +30.0) | +25.3% (-0.1 to +50.7) | +20.9% (-24.5 to +66.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.407 | 0.449 | +10.1% (-9.9 to +30.1) | +25.3% (-0.2 to +50.9) | +21.0% (-24.3 to +66.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% (+1.3 to +1.8) | +1.4% (+0.6 to +2.2) | +1.7% (+1.5 to +1.9) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.845 | 0.858 | +1.5% (+1.3 to +1.8) | +1.4% (+0.6 to +2.2) | +1.7% (+1.6 to +1.8) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% (-0.4 to +0.1) | -0.1% (-0.3 to +0.1) | -0.3% (-0.8 to +0.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.82 | 5.82 | -0.0% (-0.2 to +0.1) | -0.1% (-0.7 to +0.5) | -0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.06 | 0.985 | -6.6% (-7.7 to -5.5) | -6.8% (-10.0 to -3.6) | -7.9% (-9.5 to -6.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.2 | +1.8% (+0.4 to +3.3) | +1.0% (-1.2 to +3.1) | +1.6% (+0.2 to +3.0) | STEADY, no difference beyond the noise (1 of 3 runs) |
| memory used, mean (MB) | 61.3 | 62.0 | +1.1% (-0.5 to +2.6) | +0.3% (-1.8 to +2.5) | +1.1% (-0.1 to +2.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| keys evicted | 103,442 | 94,973 | -8.2% (-9.6 to -6.8) | -7.5% (-11.9 to -3.1) | -9.1% (-9.9 to -8.3) | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.12 | +0.2% (-32.8 to +33.3) | -8.1% (-61.2 to +45.0) | +11.2% (+3.8 to +18.5) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 200.4 | 201.4 | +0.5% (-37.7 to +38.7) | -8.2% (-64.0 to +47.5) | +12.7% (+4.1 to +21.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.352 | 0.348 | -1.0% (-39.0 to +37.0) | -9.5% (-64.1 to +45.1) | +10.8% (+2.7 to +18.9) | STEADY, no difference beyond the noise (2 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 21.7 | +21.7 (+18.8 to +24.5) | +21.7 (+18.8 to +24.5) | +22.3 (+19.5 to +25.2) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); left native (12 trials, 0 allowed, 1 refused); run B: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); left native (13 trials, 0 allowed, 2 refused); left native (13 trials, 0 allowed, 2 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 1 refused); left native (12 trials, 0 allowed, 2 refused); left native (13 trials, 0 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 937.4 | +1.3% (+1.1 to +1.4) | +1.4% (+1.2 to +1.6) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.4) | +1.4% (+1.2 to +1.6) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% (-0.1 to +0.1) | +0.1% (-0.1 to +0.2) | -0.0% (-0.6 to +0.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% (+0.1 to +0.3) | +0.3% (+0.2 to +0.3) | +0.0% (-0.3 to +0.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| latency, mean (ms) | 2.26 | 2.22 | -1.8% (-2.1 to -1.5) | -1.9% (-2.2 to -1.6) | -2.0% (-2.5 to -1.4) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.3% (+2.0 to +2.6) | +2.4% (+1.9 to +2.9) | +2.4% (+2.2 to +2.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.5 to +2.4) | +1.8% (+1.4 to +2.2) | +2.1% (+2.1 to +2.1) | **power given in all three of our runs** |
| keys evicted | 243,233 | 236,824 | -2.6% (-6.3 to +1.0) | -1.5% (-3.5 to +0.6) | -3.4% (-3.7 to -3.2) | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.142 | +5.8% (-18.0 to +29.6) | +0.5% (-10.0 to +10.9) | +2.8% (-23.1 to +28.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 222.9 | 237.7 | +6.6% (-20.7 to +33.9) | +0.7% (-11.8 to +13.1) | +3.2% (-25.9 to +32.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.535 | 0.563 | +5.3% (-21.8 to +32.4) | -0.7% (-12.9 to +11.5) | +1.9% (-27.3 to +31.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 14.0 | +14 (+9.7 to +18.3) | +15.7 (+14.2 to +17.1) | +13.7 (+10.8 to +16.5) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run B: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN in all three of our runs, 0 LOSS, 2 power given, 26 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
