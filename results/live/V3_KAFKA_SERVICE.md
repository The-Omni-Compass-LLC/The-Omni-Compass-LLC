# Kafka, a consumer group's operator-set size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Apache Kafka as shipped (one broker, a topic of 8 partitions) with the consumer group at the operator's count is native; omni is the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line (`docs/KAFKA_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Lost messages: any increase in any run is marked. The tuning workload is shown and not counted. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner, the compass's own cost included; no energy is claimed beyond them.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38054804459 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| B | 38054808912 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |
| C | 38054812962 | `ca745467845c` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 4 |

## tuning: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Native capacity with the operator's 2 consumers, per run: 975, 973, 974 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 366.1 | 365.3 | -0.2% (-0.7 to +0.2) | +0.0% (-0.5 to +0.5) | +0.0% (-1.0 to +1.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 428.9 | 428.9 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,342 | 2,413 | +3.1% (-2.6 to +8.7) | -0.4% (-9.2 to +8.3) | -2.5% (-12.8 to +7.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,696 | 3,672 | -0.6% (-10.0 to +8.7) | -0.9% (-7.1 to +5.3) | -1.9% (-7.8 to +3.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 8.57 | 8.6 | +0.3% (-1.1 to +1.6) | -0.3% (-0.8 to +0.3) | -1.2% (-4.9 to +2.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 315.2 | 323.1 | +2.5% (-3.8 to +8.9) | -0.4% (-6.0 to +5.1) | -1.5% (-12.8 to +9.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,669 | 1,709 | +2.4% (-3.0 to +7.9) | -0.1% (-1.4 to +1.1) | -1.7% (-5.1 to +1.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 139.5 | 142.7 | +2.3% (-5.3 to +9.9) | -0.8% (-4.8 to +3.2) | -1.9% (-12.8 to +9.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.314 | 0.313 | -0.5% (-3.2 to +2.2) | +0.0% (-4.0 to +4.0) | -2.3% (-8.1 to +3.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 546.5 | 543.2 | -0.6% (-2.9 to +1.7) | +0.3% (-3.7 to +4.4) | -2.2% (-7.0 to +2.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.32 | 3.3 | -0.4% (-2.6 to +1.8) | +0.3% (-4.2 to +4.8) | -2.2% (-6.4 to +2.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## burst: 2.0 ms of work a message, 256 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 976, 976, 974 messages a second; steps 1 6 1 8 1 6 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 340.6 | 340.8 | +0.1% (-1.4 to +1.6) | -0.0% (-0.2 to +0.2) | -0.5% (-1.6 to +0.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 419.5 | 419.5 | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (2 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,551 | 2,540 | -0.4% (-2.3 to +1.4) | -1.2% (-7.8 to +5.4) | +0.5% (-7.4 to +8.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,984 | 3,770 | -5.4% (-11.8 to +1.1) | -4.5% (-19.9 to +10.9) | +7.0% (-9.8 to +23.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 9.49 | 9.36 | -1.4% (-5.7 to +2.9) | -2.5% (-6.9 to +1.9) | -3.8% (-9.1 to +1.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 394.8 | 389.3 | -1.4% (-8.4 to +5.6) | +0.2% (-1.1 to +1.4) | +2.6% (-4.3 to +9.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 1,715 | 1,673 | -2.5% (-9.5 to +4.6) | -0.5% (-6.2 to +5.2) | +0.9% (-5.1 to +7.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 171.6 | 168.4 | -1.9% (-7.7 to +3.9) | +0.1% (-1.0 to +1.3) | +1.9% (-4.5 to +8.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.98 | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | -0.8% (-0.8 to -0.8) | **GAIN in all three of our runs** |
| consumers running, most at once | 2 | 2 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, the same |
| host CPU busy (share of the run) | 0.294 | 0.292 | -0.9% (-6.6 to +4.7) | -1.1% (-6.7 to +4.5) | -1.0% (-8.4 to +6.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 205.9 | 204.2 | -0.8% (-6.4 to +4.7) | -1.1% (-6.6 to +4.5) | -0.9% (-8.3 to +6.6) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 3.35 | 3.32 | -0.9% (-6.3 to +4.4) | -1.1% (-6.9 to +4.7) | -0.3% (-8.4 to +7.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## heavy: 5.0 ms of work a message, 1024 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 391, 393, 393 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147.2 | 147.0 | -0.1% (-0.7 to +0.4) | -0.1% (-0.3 to +0.1) | -0.0% (-0.9 to +0.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 171.8 | 171.8 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,185 | 2,144 | -1.9% (-8.7 to +4.9) | -0.8% (-1.9 to +0.3) | +0.5% (-4.4 to +5.3) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,389 | 3,466 | +2.3% (-2.6 to +7.1) | +2.9% (-5.6 to +11.5) | -0.4% (-19.1 to +18.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 11.1 | 11.1 | +0.1% (-0.8 to +1.0) | -0.5% (-1.3 to +0.3) | -0.2% (-0.9 to +0.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 284.7 | 288.2 | +1.3% (-7.0 to +9.5) | +0.5% (-1.8 to +2.9) | -0.3% (-9.3 to +8.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, most messages waiting at once | 648.3 | 644.0 | -0.7% (-2.6 to +1.3) | -0.6% (-5.0 to +3.7) | +0.2% (-3.3 to +3.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 51.9 | 52.4 | +1.2% (-4.2 to +6.5) | +1.2% (-1.0 to +3.4) | -1.1% (-8.9 to +6.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% (-0.6 to +0.1) | -0.3% (-0.3 to -0.3) | -0.3% (-0.3 to -0.3) | STEADY, no difference beyond the noise (1 of 3 runs) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.266 | 0.266 | -0.2% (-2.2 to +1.8) | -1.5% (-5.8 to +2.8) | -1.3% (-5.7 to +3.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 477.8 | 476.9 | -0.2% (-2.1 to +1.8) | -1.5% (-5.7 to +2.8) | -1.2% (-5.7 to +3.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 7.21 | 7.21 | -0.1% (-2.2 to +2.1) | -1.4% (-5.7 to +3.0) | -1.2% (-5.5 to +3.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +100.0% (+100.0 to +100.0) | +100.0% (+100.0 to +100.0) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## light: 1.0 ms of work a message, 128 B; line 500 ms, 3 paired repetitions a run

Native capacity with the operator's 2 consumers, per run: 1,949, 1,946, 1,917 messages a second; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 730.1 | 771.4 | +5.7% (-19.6 to +30.9) | -0.0% (-0.2 to +0.1) | +0.4% (-1.9 to +2.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| throughput (messages a second consumed) | 857.3 | 857.3 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 95th percentile (ms) | 2,455 | 1,736 | -29.3% (-176.1 to +117.5) | -1.7% (-4.5 to +1.0) | -9.0% (-62.1 to +44.2) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, 99th percentile (ms) | 3,754 | 2,608 | -30.5% (-171.0 to +110.0) | +0.1% (-1.0 to +1.1) | -10.1% (-47.7 to +27.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, median (ms) | 7.42 | 7.13 | -3.9% (-24.5 to +16.7) | -1.4% (-4.8 to +1.9) | -3.2% (-12.1 to +5.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| end-to-end latency, mean (ms) | 330.0 | 233.2 | -29.3% (-173.8 to +115.2) | -0.9% (-1.4 to -0.4) | -8.8% (-54.9 to +37.3) | STEADY, no difference beyond the noise (2 of 3 runs) |
| consumer lag, most messages waiting at once | 3,369 | 2,353 | -30.2% (-164.7 to +104.4) | -0.3% (-2.9 to +2.2) | -8.6% (-48.6 to +31.5) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer lag, mean messages waiting | 288.2 | 203.9 | -29.3% (-172.3 to +113.8) | -1.2% (-1.7 to -0.6) | -8.6% (-53.7 to +36.4) | STEADY, no difference beyond the noise (2 of 3 runs) |
| messages produced and never consumed | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| consumers running, mean (the resources held) | 2 | 2.17 | +8.5% (-29.6 to +46.6) | +6.0% (-21.2 to +33.1) | +6.5% (-22.9 to +35.8) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumers running, most at once | 2 | 2.33 | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | +16.7% (-55.1 to +88.4) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.313 | 0.315 | +0.6% (-2.6 to +3.9) | -0.1% (-3.7 to +3.5) | +0.4% (-11.2 to +11.9) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 558.0 | 561.8 | +0.7% (-2.9 to +4.3) | -0.0% (-3.8 to +3.8) | +0.9% (-10.9 to +12.7) | STEADY, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 messages inside the line | 1.7 | 1.63 | -4.3% (-23.4 to +14.8) | -0.0% (-3.8 to +3.8) | +0.5% (-11.1 to +12.1) | STEADY, no difference beyond the noise (3 of 3 runs) |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% (-10.1 to +276.8) | +133.3% (-10.1 to +276.8) | +166.7% (-120.2 to +453.5) | shown, not judged |

The consumer count handed back to the operator's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 2 to 3 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run B: acting: 2 to 3 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 2 to 3 (3 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 1 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 41 STEADY, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
