# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38935442398 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| B | 38947622681 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |
| C | 38957537624 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,194 | +1.1% (+0.6 to +1.6) | +0.8% (+0.4 to +1.1) | +1.2% (+1.1 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, the same |
| cache hit rate | 0.789 | 0.797 | +1.0% (+0.4 to +1.7) | +0.8% (+0.4 to +1.1) | +1.2% (+1.1 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% (-0.3 to +0.4) | -0.0% (-0.3 to +0.2) | -0.1% (-0.7 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.29 | 5.28 | -0.1% (-1.3 to +1.1) | +0.1% (-0.3 to +0.4) | -0.0% (-0.4 to +0.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.18 | 1.13 | -4.0% (-5.8 to -2.3) | -2.3% (-3.5 to -1.1) | -4.2% (-5.3 to -3.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.7 | +2.7% (+1.5 to +3.8) | +1.7% (+0.2 to +3.2) | +2.8% (+2.4 to +3.1) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% (+1.3 to +2.7) | +1.3% (-0.4 to +2.9) | +2.1% (+1.8 to +2.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| keys evicted | 138,150 | 133,510 | -3.4% (-5.8 to -0.9) | -2.1% (-3.8 to -0.5) | -4.1% (-4.6 to -3.6) | shown, not judged |
| host CPU busy (share of the run) | 0.0645 | 0.0558 | -13.4% (-65.0 to +38.2) | -0.6% (-59.0 to +57.9) | -6.6% (-38.7 to +25.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 113.8 | 97.7 | -14.2% (-69.0 to +40.6) | -0.4% (-66.0 to +65.2) | -7.3% (-43.1 to +28.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.182 | -15.1% (-69.8 to +39.5) | -1.1% (-66.5 to +64.2) | -8.4% (-44.2 to +27.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+16 to +26) | +19.3 (+13.1 to +25.6) | +23 (+23 to +23) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run B: acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% (-0.1 to -0.0) | -0.1% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.1 to -0.0) | -0.1% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% (-0.1 to +0.2) | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% (-0.0 to +0.4) | +0.0% (-0.1 to +0.1) | +0.1% (-0.0 to +0.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% (+0.3 to +0.8) | +0.3% (-0.5 to +1.0) | +0.1% (-0.1 to +0.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.5 | -4.0% (-7.0 to -0.9) | -2.5% (-2.7 to -2.3) | -2.3% (-2.5 to -2.0) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 55.5 | -2.9% (-6.3 to +0.6) | -1.2% (-1.6 to -0.8) | -0.9% (-1.1 to -0.7) | STEADY, no difference beyond the noise (1 of 3 runs) |
| keys evicted | 71,737 | 71,873 | +0.2% (+0.1 to +0.2) | +0.2% (-0.3 to +0.7) | -0.1% (-0.4 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.128 | -2.2% (-45.7 to +41.3) | +13.8% (-86.6 to +114.2) | -1.7% (-37.6 to +34.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 87.7 | 85.5 | -2.5% (-52.1 to +47.1) | +15.1% (-95.8 to +126.0) | -2.1% (-42.7 to +38.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.442 | -2.4% (-52.1 to +47.2) | +15.2% (-95.7 to +126.0) | -2.1% (-42.8 to +38.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 8.67 | +8.67 (+2.93 to +14.4) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% (+1.3 to +1.9) | +1.0% (+0.6 to +1.4) | +1.4% (+0.1 to +2.8) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, the same |
| cache hit rate | 0.845 | 0.859 | +1.6% (+1.5 to +1.7) | +1.0% (+0.6 to +1.4) | +1.4% (+0.0 to +2.8) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.49 | 5.49 | -0.0% (-0.4 to +0.4) | -0.1% (-0.1 to +0.0) | -0.1% (-0.5 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.1% (-0.1 to +0.3) | +0.1% (+0.0 to +0.1) | +0.1% (-0.1 to +0.2) | STEADY, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 0.955 | 0.887 | -7.1% (-8.9 to -5.4) | -4.3% (-6.0 to -2.6) | -6.4% (-12.9 to +0.0) | STEADY, no difference beyond the noise (1 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.5% (+0.4 to +4.6) | -1.1% (-3.7 to +1.5) | +1.0% (-4.7 to +6.7) | STEADY, no difference beyond the noise (2 of 3 runs) |
| memory used, mean (MB) | 61.3 | 62.1 | +1.3% (+0.7 to +2.0) | -2.6% (-4.7 to -0.5) | +0.4% (-5.4 to +6.1) | **the runs disagree** |
| keys evicted | 103,115 | 94,196 | -8.6% (-9.3 to -8.0) | -5.2% (-7.9 to -2.4) | -7.6% (-15.5 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.105 | +5.5% (-69.1 to +80.1) | -0.5% (-35.5 to +34.5) | +8.4% (-39.9 to +56.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 175.6 | 186.1 | +6.0% (-76.4 to +88.3) | -0.4% (-39.9 to +39.2) | +9.8% (-45.7 to +65.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.321 | +4.3% (-77.6 to +86.2) | -1.4% (-40.9 to +38.1) | +8.2% (-45.5 to +61.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 21.7 | +21.7 (+15.9 to +27.4) | +31 (+22.4 to +39.6) | +22.7 (+13.3 to +32.1) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run B: acting: 56 to 72 (16 trials, 2 allowed, 1 refused); acting: 48 to 72 (13 trials, 3 allowed, 2 refused); acting: 48 to 72 (15 trials, 3 allowed, 1 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 3 refused); acting: 56 to 72 (11 trials, 2 allowed, 3 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.4 | 937.3 | +1.3% (+1.1 to +1.5) | +1.2% (+1.1 to +1.3) | +1.3% (+0.8 to +1.8) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.1 to +1.5) | +1.2% (+1.2 to +1.3) | +1.3% (+1.0 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% (-0.3 to +0.3) | -0.0% (-0.1 to +0.1) | -0.1% (-1.5 to +1.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% (-0.0 to +0.3) | +0.1% (-0.1 to +0.3) | +0.0% (-30.9 to +31.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.27 | 2.22 | -1.9% (-2.4 to -1.3) | -1.8% (-1.8 to -1.7) | -2.3% (-6.9 to +2.4) | STEADY, no difference beyond the noise (1 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.3 | +2.0% (+1.5 to +2.6) | +2.1% (+1.8 to +2.5) | +2.2% (+1.5 to +2.9) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% (+1.0 to +2.7) | +2.0% (+1.8 to +2.3) | +1.8% (+1.5 to +2.0) | **power given in all three of our runs** |
| keys evicted | 243,232 | 237,910 | -2.2% (-7.5 to +3.2) | -2.9% (-4.9 to -1.0) | -1.3% (-2.7 to +0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.6% (-21.5 to +20.2) | +0.9% (-20.0 to +21.9) | -1.9% (-16.0 to +12.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 242.6 | 241.3 | -0.6% (-25.3 to +24.1) | +1.2% (-22.6 to +25.1) | -1.8% (-18.0 to +14.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.572 | -1.8% (-26.2 to +22.5) | +0.0% (-23.5 to +23.5) | -3.1% (-19.2 to +13.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 14.7 | +14.7 (+7.49 to +21.8) | +13.3 (+3.93 to +22.7) | +15.3 (+7.74 to +22.9) | shown, not judged |

The ceiling handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 80 (11 trials, 3 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 5 gauge-rows GAIN in all three of our runs, 0 LOSS, 2 power given, 28 STEADY, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
