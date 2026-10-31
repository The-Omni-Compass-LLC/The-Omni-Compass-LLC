# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39383000915 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39414286889 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39463721089 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 2 |

## tuning

> not in every run: C lack it.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,929 | 2,928 | 2929 → 2928; raw −0.1% (95%: −0.1% to ±0.0%); STEADY | 2910 → 2910; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2933 → 2932; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,931 | 2,930 | 2931 → 2930; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 2913 → 2914; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2935 → 2934; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.245 | 0.25 | 0.2453 → 0.25; raw +1.9% (95%: +0.7% to +3.1%), +0.0047 in the gauge's unit; LOSS | 0.286 → 0.2927; raw +2.3% (95%: −5.0% to +9.6%), +0.0067 in the gauge's unit; LOSS | 0.229 → 0.228; raw −0.4% (95%: −2.6% to +1.7%), −0.0010 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.391 | 0.396 | 0.391 → 0.396; raw +1.3% (95%: −1.5% to +4.0%), +0.0050 in the gauge's unit; LOSS | 0.4953 → 0.4943; raw −0.2% (95%: −0.7% to +0.3%), −0.0010 in the gauge's unit; STEADY | 0.3773 → 0.3767; raw −0.2% (95%: −4.8% to +4.4%), −0.0007 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.30%) |
| latency, mean (ms) | 0.0854 | 0.0878 | 0.08544 → 0.08784; raw +2.8% (95%: −0.9% to +6.5%), +0.0024 in the gauge's unit; LOSS | 0.1182 → 0.1186; raw +0.3% (95%: −1.3% to +1.8%), +0.0003 in the gauge's unit; STEADY | 0.0814 → 0.08079; raw −0.8% (95%: −2.6% to +1.1%), −0.0006 in the gauge's unit; GAIN | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,367 | 1366 → 1367; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 1364 → 1365; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 1367 → 1366; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| pages read into the cache (misses) | 61,784 | 61,887 | 6.178e+04 → 6.189e+04; raw +0.2% (95%: −0.2% to +0.5%) | 6.178e+04 → 6.185e+04; raw +0.1% (95%: −0.3% to +0.5%) | 6.181e+04 → 6.186e+04; raw +0.1% (95%: −0.6% to +0.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0988 | 0.101 → 0.09884; raw −2.2% (95%: −15.2% to +10.9%), −0.0022 in the gauge's unit; GAIN | 0.1603 → 0.14; raw −12.7% (95%: −25.4% to ±0.0%), −0.0203 in the gauge's unit; GAIN | 0.1046 → 0.08772; raw −16.1% (95%: −54.1% to +21.8%), −0.0169 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 182.5 | 177.5 | 182.5 → 177.5; raw −2.7% (95%: −17.6% to +12.1%); GAIN | 297.3 → 253.5; raw −14.8% (95%: −30.0% to +0.5%); GAIN | 191.1 → 157.3; raw −17.7% (95%: −58.5% to +23.2%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.136 | 0.133 | 0.1364 → 0.1327; raw −2.7% (95%: −17.6% to +12.2%), −0.0037 in the gauge's unit; GAIN | 0.2228 → 0.1899; raw −14.8% (95%: −30.0% to +0.5%), −0.0329 in the gauge's unit; GAIN | 0.1427 → 0.1175; raw −17.6% (95%: −58.6% to +23.3%), −0.0252 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst

> not in every run: C lack it.

## c

> not in every run: B lack it.

## f

> not in every run: B, C lack it.

**Across 1 untouched workloads: 3 gauge-rows GAIN, 1 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 6 STEADY, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
