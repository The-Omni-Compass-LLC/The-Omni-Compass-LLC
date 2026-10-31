# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39470845655 | `ac0eeaef8ecc` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39475514914 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39477842603 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning

> not in every run: C lack it.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,913 | 2915 → 2913; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2897 → 2895; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 2899 → 2896; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 2,918 | 2,916 | 2918 → 2916; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2901 → 2899; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 2902 → 2899; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 0.268 | 0.267 | 0.2683 → 0.2673; raw −0.4% (95%: −4.6% to +3.9%), −0.0010 in the gauge's unit; STEADY | 0.3273 → 0.325; raw −0.7% (95%: −12.5% to +11.1%), −0.0023 in the gauge's unit; GAIN | 0.3073 → 0.3163; raw +2.9% (95%: −6.4% to +12.3%), +0.0090 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 0.44 | 0.434 | 0.4403 → 0.4337; raw −1.5% (95%: −5.5% to +2.4%), −0.0067 in the gauge's unit; GAIN | 0.487 → 0.4867; raw −0.1% (95%: −2.4% to +2.2%), −0.0003 in the gauge's unit; STEADY | 0.4387 → 0.451; raw +2.8% (95%: −7.5% to +13.1%), +0.0123 in the gauge's unit; LOSS | **the runs disagree** |
| latency, mean (ms) | 0.119 | 0.119 | 0.1185 → 0.1186; raw ±0.0% (95%: −5.8% to +5.9%), +0.0001 in the gauge's unit; STEADY | 0.2007 → 0.1978; raw −1.4% (95%: −6.9% to +4.1%), −0.0028 in the gauge's unit; GAIN | 0.1812 → 0.1836; raw +1.4% (95%: −0.1% to +2.8%), +0.0025 in the gauge's unit; LOSS | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.5 | 512 → 508.5; raw −0.7% (95%: −1.2% to −0.1%); GAIN | 512 → 509; raw −0.6% (95%: −1.0% to −0.2%); GAIN | 512 → 508.6; raw −0.7% (95%: −0.8% to −0.6%); GAIN | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 416.4 | 414.7 | 416.4 → 414.7; raw −0.4% (95%: −3.1% to +2.2%); STEADY | 419 → 416.4; raw −0.6% (95%: −1.8% to +0.5%); GAIN | 415.6 → 415.1; raw −0.1% (95%: −1.0% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.39%) |
| pages read into the cache (misses) | 701,051 | 711,588 | 7.011e+05 → 7.116e+05; raw +1.5% (95%: −24.2% to +27.2%) | 7.155e+05 → 7.036e+05; raw −1.7% (95%: −10.4% to +7.1%) | 6.873e+05 → 7.014e+05; raw +2.1% (95%: −10.0% to +14.1%) | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.146 | 0.1381 → 0.1461; raw +5.8% (95%: −50.5% to +62.1%), +0.0080 in the gauge's unit; power given | 0.2027 → 0.1773; raw −12.5% (95%: −28.9% to +3.8%), −0.0254 in the gauge's unit; GAIN | 0.2114 → 0.2004; raw −5.2% (95%: −33.5% to +23.0%), −0.0110 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 250.1 | 266.5 | 250.1 → 266.5; raw +6.6% (95%: −58.6% to +71.7%); power given | 354.9 → 302.3; raw −14.8% (95%: −32.9% to +3.2%); GAIN | 384.3 → 356.9; raw −7.1% (95%: −43.0% to +28.7%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.2 | 0.1873 → 0.1996; raw +6.6% (95%: −58.6% to +71.7%), +0.0123 in the gauge's unit; power given | 0.2663 → 0.2269; raw −14.8% (95%: −32.9% to +3.3%), −0.0394 in the gauge's unit; GAIN | 0.2882 → 0.2677; raw −7.1% (95%: −42.9% to +28.7%), −0.0205 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3 | 0 → 3; raw +3.0000 in the gauge's unit (95%: +0.5157 to +5.4843) | 0 → 3.333; raw +3.3333 in the gauge's unit (95%: +0.4647 to +6.2020) | 0 → 4; raw +4.0000 in the gauge's unit (95%: +4.0000 to +4.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,899 | 2899 → 2899; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 2888 → 2887; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 2897 → 2897; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,905 | 2,906 | 2905 → 2906; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2897 → 2896; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2902 → 2900; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.426 | 0.432 | 0.4263 → 0.4323; raw +1.4% (95%: −8.5% to +11.3%), +0.0060 in the gauge's unit; LOSS | 0.4327 → 0.4337; raw +0.2% (95%: −1.8% to +2.2%), +0.0010 in the gauge's unit; STEADY | 0.362 → 0.3633; raw +0.4% (95%: −0.4% to +1.2%), +0.0013 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.622 | 0.634 | 0.622 → 0.634; raw +1.9% (95%: −5.8% to +9.6%), +0.0120 in the gauge's unit; LOSS | 0.6267 → 0.627; raw +0.1% (95%: −6.4% to +6.5%), +0.0003 in the gauge's unit; STEADY | 0.486 → 0.4813; raw −1.0% (95%: −8.2% to +6.3%), −0.0047 in the gauge's unit; GAIN | **the runs disagree** |
| latency, mean (ms) | 0.162 | 0.163 | 0.1617 → 0.163; raw +0.8% (95%: −7.0% to +8.6%), +0.0013 in the gauge's unit; LOSS | 0.2221 → 0.2233; raw +0.6% (95%: −1.4% to +2.5%), +0.0013 in the gauge's unit; LOSS | 0.2002 → 0.1963; raw −1.9% (95%: −10.8% to +7.0%), −0.0039 in the gauge's unit; GAIN | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 496.8 | 512 → 496.8; raw −3.0% (95%: −3.8% to −2.1%); GAIN | 512 → 480.4; raw −6.2% (95%: −14.1% to +1.8%); GAIN | 512 → 502.8; raw −1.8% (95%: −2.7% to −0.9%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 406.4 | 393.2 | 406.4 → 393.2; raw −3.2% (95%: −5.4% to −1.1%); GAIN | 402.3 → 380; raw −5.6% (95%: −15.7% to +4.6%); GAIN | 404.9 → 398.3; raw −1.6% (95%: −3.7% to +0.5%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 261,304 | 276,274 | 2.613e+05 → 2.763e+05; raw +5.7% (95%: −16.9% to +28.3%) | 2.66e+05 → 2.874e+05; raw +8.1% (95%: −12.4% to +28.5%) | 2.63e+05 → 2.639e+05; raw +0.4% (95%: −2.7% to +3.4%) | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.191 | 0.1732 → 0.1906; raw +10.1% (95%: −7.2% to +27.4%), +0.0175 in the gauge's unit; power given | 0.1928 → 0.1533; raw −20.5% (95%: −36.0% to −5.0%), −0.0395 in the gauge's unit; GAIN | 0.219 → 0.1982; raw −9.5% (95%: −46.5% to +27.6%), −0.0208 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 127.1 | 142.8 | 127.1 → 142.8; raw +12.4% (95%: −6.9% to +31.7%); power given | 133.8 → 101.4; raw −24.2% (95%: −41.2% to −7.3%); GAIN | 160.4 → 141.3; raw −11.9% (95%: −57.8% to +33.9%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.268 | 0.239 → 0.2683; raw +12.3% (95%: −7.2% to +31.8%), +0.0294 in the gauge's unit; power given | 0.2517 → 0.1907; raw −24.2% (95%: −41.2% to −7.3%), −0.0610 in the gauge's unit; GAIN | 0.3009 → 0.2649; raw −12.0% (95%: −57.8% to +33.8%), −0.0360 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.33 | 0 → 4.333; raw +4.3333 in the gauge's unit (95%: +1.4647 to +7.2020) | 0 → 4.667; raw +4.6667 in the gauge's unit (95%: +3.2323 to +6.1010) | 0 → 4; raw +4.0000 in the gauge's unit (95%: +4.0000 to +4.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## c

> not in every run: B lack it.

## f

> not in every run: B lack it.

**Across 2 untouched workloads: 3 gauge-rows GAIN, 1 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 7 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
