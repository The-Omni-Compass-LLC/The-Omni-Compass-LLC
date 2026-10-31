# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any increase in any run is marked. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054742933 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38054746778 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38054750788 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 976, 975, 983 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 365.4 | 364.4 | -0.3% (-1.0 to +0.5) | -0.3% (-0.9 to +0.2) | -0.2% (-0.7 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 429.4 | 429.4 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,457 | 2,509 | +2.1% (-1.9 to +6.2) | +3.4% (-7.3 to +14.2) | +2.8% (+2.0 to +3.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,887 | -1.6% (-12.8 to +9.7) | +4.0% (-1.6 to +9.5) | -1.1% (-14.2 to +12.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.64 | 8.59 | -0.6% (-1.5 to +0.3) | -0.1% (-4.5 to +4.3) | -0.5% (-1.8 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 332.8 | 339.9 | +2.1% (-7.2 to +11.4) | +4.4% (-7.1 to +16.0) | +1.7% (-3.8 to +7.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,708 | 1,738 | +1.8% (-4.1 to +7.6) | +2.8% (-4.9 to +10.4) | +0.7% (-5.2 to +6.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 147.2 | 150.3 | +2.1% (-6.7 to +10.9) | +4.2% (-7.0 to +15.4) | +1.3% (-5.5 to +8.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.319 | +0.1% (-3.9 to +4.1) | -0.3% (-7.2 to +6.7) | -0.6% (-2.6 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 552.5 | 554.5 | +0.4% (-4.1 to +4.8) | -0.2% (-7.2 to +6.7) | -0.5% (-2.7 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.36 | 3.38 | +0.6% (-3.5 to +4.8) | +0.1% (-7.2 to +7.3) | -0.3% (-2.1 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 975, 975, 973 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.8 | 340.8 | +0.0% (-0.3 to +0.3) | -0.1% (-0.6 to +0.3) | +0.1% (-0.9 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 418.9 | 418.9 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,525 | 2,503 | -0.9% (-9.3 to +7.5) | +1.8% (-4.6 to +8.1) | -1.7% (-6.2 to +2.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,776 | 3,763 | -0.3% (-8.8 to +8.1) | +2.0% (-1.2 to +5.1) | -2.1% (-15.7 to +11.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 9.68 | 9.58 | -1.1% (-20.9 to +18.7) | -0.2% (-0.7 to +0.3) | -3.2% (-6.3 to -0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, mean (ms) | 382.9 | 383.9 | +0.3% (-2.8 to +3.4) | +1.2% (-0.1 to +2.5) | -1.5% (-9.3 to +6.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,650 | 1,644 | -0.3% (-4.2 to +3.5) | -0.6% (-1.1 to -0.1) | -0.6% (-9.1 to +8.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| consumer lag, mean messages waiting | 166.3 | 166.1 | -0.1% (-3.4 to +3.1) | +0.9% (-0.4 to +2.2) | -2.1% (-9.1 to +4.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.295 | 0.292 | -1.0% (-6.8 to +4.8) | -0.3% (-6.1 to +5.5) | -1.3% (-8.5 to +5.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 206.5 | 204.5 | -1.0% (-6.7 to +4.7) | -0.3% (-6.1 to +5.5) | -1.3% (-8.6 to +5.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -1.0% (-6.4 to +4.4) | -0.2% (-5.6 to +5.3) | -1.4% (-8.2 to +5.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 392, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 146.8 | 146.8 | -0.0% (-1.1 to +1.0) | -0.8% (-3.6 to +2.0) | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 172.1 | 172.1 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,328 | 2,303 | -1.0% (-11.4 to +9.3) | +5.6% (-16.7 to +27.8) | -0.6% (-6.8 to +5.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,624 | 3,548 | -2.1% (-11.9 to +7.8) | +3.6% (-4.8 to +11.9) | -2.2% (-14.7 to +10.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.5 | 11.5 | -0.1% (-0.5 to +0.3) | -0.4% (-1.6 to +0.8) | +0.0% (-0.5 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 310.4 | 309.6 | -0.3% (-11.6 to +11.1) | +7.8% (-15.9 to +31.5) | -0.6% (-6.2 to +5.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 683.7 | 665.7 | -2.6% (-10.2 to +4.9) | +5.0% (-9.1 to +19.1) | -0.2% (-2.8 to +2.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 56.5 | 56.3 | -0.4% (-9.1 to +8.4) | +6.7% (-12.6 to +26.0) | -2.0% (-7.0 to +2.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | +0.1% (-1.9 to +2.2) | -0.3% (-0.3 to -0.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.277 | 0.276 | -0.5% (-3.4 to +2.3) | -0.7% (-3.1 to +1.8) | -0.5% (-1.6 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 488.6 | 486.6 | -0.4% (-3.2 to +2.4) | -0.6% (-3.2 to +2.0) | -0.4% (-1.5 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.38 | 7.36 | -0.4% (-4.2 to +3.5) | +0.2% (-4.2 to +4.6) | -0.3% (-1.6 to +0.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,932, 1,941, 1,945 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 725.1 | 722.8 | -0.3% (-1.2 to +0.5) | -0.2% (-0.8 to +0.3) | +0.2% (-0.0 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 849.6 | 849.9 | +0.0% (-0.1 to +0.2) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,368 | 2,372 | +0.1% (-14.5 to +14.8) | +1.5% (-0.4 to +3.4) | -2.8% (-5.8 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,640 | 3,789 | +4.1% (-2.6 to +10.8) | +1.4% (-2.6 to +5.5) | -5.6% (-16.3 to +5.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.26 | 7.99 | -3.3% (-12.5 to +5.9) | -0.8% (-11.9 to +10.2) | -0.4% (-2.7 to +2.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 315.8 | 322.6 | +2.1% (-11.6 to +15.9) | +2.0% (-1.4 to +5.5) | -3.6% (-8.9 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 3,283 | 3,313 | +0.9% (-4.2 to +6.0) | +0.5% (-4.6 to +5.6) | -1.3% (-8.4 to +5.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 274.8 | 280.2 | +1.9% (-13.1 to +17.0) | +2.1% (-0.3 to +4.4) | -3.8% (-8.8 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 2.25 | +12.3% (-14.9 to +39.5) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | EVEN, no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2.67 | +33.3% (-38.4 to +105.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.336 | 0.336 | -0.1% (-9.5 to +9.2) | -0.0% (-3.8 to +3.8) | -0.5% (-3.3 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 577.0 | 577.5 | +0.1% (-9.2 to +9.4) | +0.2% (-3.9 to +4.3) | -0.3% (-2.8 to +2.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.77 | 1.77 | +0.4% (-7.9 to +8.8) | +0.5% (-4.1 to +5.0) | -0.5% (-3.1 to +2.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 6 | +200.0% (+200.0 to +200.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

**Across 3 untouched workloads: 1 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 41 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
