# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150495654 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39160201436 | `773cd59cfdd2` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39169863638 | `2b4c11e3aee0` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,865 | 2,843 | 2865 → 2843; raw −0.8% (95%: −7.1% to +5.6%); LOSS | 2772 → 2789; raw +0.6% (95%: −6.9% to +8.1%); GAIN | 2895 → 2895; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | **the runs disagree** |
| throughput (operations a second) | 2,874 | 2,851 | 2874 → 2851; raw −0.8% (95%: −7.1% to +5.5%); LOSS | 2781 → 2797; raw +0.6% (95%: −6.9% to +8.1%); GAIN | 2899 → 2900; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | **the runs disagree** |
| latency, 95th percentile (ms) | 0.267 | 0.266 | 0.2673 → 0.2657; raw −0.6% (95%: −3.9% to +2.6%), −0.0017 in the gauge's unit; GAIN | 0.2803 → 0.2763; raw −1.4% (95%: −8.3% to +5.5%), −0.0040 in the gauge's unit; GAIN | 0.3143 → 0.3143; raw ±0.0% (95%: −1.4% to +1.4%), ±0.0000 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.43 | 0.428 | 0.4303 → 0.428; raw −0.5% (95%: −2.6% to +1.5%), −0.0023 in the gauge's unit; GAIN | 0.457 → 0.452; raw −1.1% (95%: −4.0% to +1.8%), −0.0050 in the gauge's unit; GAIN | 0.4543 → 0.455; raw +0.1% (95%: −1.0% to +1.3%), +0.0007 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.50%) |
| latency, mean (ms) | 0.214 | 0.209 | 0.2137 → 0.2092; raw −2.1% (95%: −18.2% to +14.0%), −0.0045 in the gauge's unit; GAIN | 0.2281 → 0.2216; raw −2.9% (95%: −13.9% to +8.1%), −0.0065 in the gauge's unit; GAIN | 0.1943 → 0.1951; raw +0.4% (95%: −0.9% to +1.7%), +0.0008 in the gauge's unit; STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,338 | 1350 → 1338; raw −0.8% (95%: −5.2% to +3.5%); GAIN | 1337 → 1327; raw −0.7% (95%: −8.1% to +6.7%); GAIN | 1363 → 1365; raw +0.1% (95%: −0.3% to +0.5%); STEADY | STEADY, under the floor (the three runs' mean 0.47%) |
| pages read into the cache (misses) | 63,011 | 62,028 | 6.301e+04 → 6.203e+04; raw −1.6% (95%: −8.8% to +5.7%) | 6.253e+04 → 6.186e+04; raw −1.1% (95%: −12.1% to +10.0%) | 6.289e+04 → 6.321e+04; raw +0.5% (95%: −0.3% to +1.3%) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.174 | 0.1722 → 0.1741; raw +1.1% (95%: −53.3% to +55.5%), +0.0019 in the gauge's unit; power given | 0.1782 → 0.1683; raw −5.5% (95%: −61.8% to +50.7%), −0.0099 in the gauge's unit; GAIN | 0.2272 → 0.2336; raw +2.8% (95%: −16.1% to +21.8%), +0.0064 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 310.9 | 315.7 | 310.9 → 315.7; raw +1.5% (95%: −63.3% to +66.4%); power given | 325.9 → 304.1; raw −6.7% (95%: −71.4% to +58.1%); GAIN | 409.7 → 422.7; raw +3.2% (95%: −21.3% to +27.6%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.242 | 0.2368 → 0.2415; raw +2.0% (95%: −62.0% to +65.9%), +0.0047 in the gauge's unit; power given | 0.2563 → 0.237; raw −7.5% (95%: −67.9% to +52.8%), −0.0193 in the gauge's unit; GAIN | 0.3074 → 0.3172; raw +3.2% (95%: −21.3% to +27.6%), +0.0098 in the gauge's unit; power given | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | 2895 → 2894; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 2893 → 2894; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2910 → 2911; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,899 | 2,899 | 2899 → 2899; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 2898 → 2898; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2916 → 2917; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.337 | 0.343 | 0.337 → 0.3427; raw +1.7% (95%: −8.6% to +12.0%), +0.0057 in the gauge's unit; LOSS | 0.338 → 0.3333; raw −1.4% (95%: −10.2% to +7.4%), −0.0047 in the gauge's unit; GAIN | 0.257 → 0.2617; raw +1.8% (95%: −9.7% to +13.3%), +0.0047 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 0.517 | 0.521 | 0.5173 → 0.521; raw +0.7% (95%: −1.5% to +2.9%), +0.0037 in the gauge's unit; LOSS | 0.4933 → 0.4903; raw −0.6% (95%: −7.2% to +5.9%), −0.0030 in the gauge's unit; GAIN | 0.4143 → 0.414; raw −0.1% (95%: −3.5% to +3.3%), −0.0003 in the gauge's unit; STEADY | **the runs disagree** |
| latency, mean (ms) | 0.195 | 0.197 | 0.1948 → 0.1971; raw +1.2% (95%: −3.3% to +5.7%), +0.0023 in the gauge's unit; LOSS | 0.1971 → 0.1956; raw −0.8% (95%: −5.5% to +4.0%), −0.0015 in the gauge's unit; GAIN | 0.1784 → 0.1802; raw +1.0% (95%: −8.0% to +9.9%), +0.0018 in the gauge's unit; LOSS | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | 1365 → 1366; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1365 → 1365; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 1362 → 1361; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| pages read into the cache (misses) | 61,772 | 61,888 | 6.177e+04 → 6.189e+04; raw +0.2% (95%: −0.3% to +0.6%) | 6.179e+04 → 6.185e+04; raw +0.1% (95%: −0.3% to +0.5%) | 6.18e+04 → 6.184e+04; raw +0.1% (95%: −0.4% to +0.6%) | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.185 | 0.1794 → 0.1848; raw +3.0% (95%: −5.0% to +11.1%), +0.0054 in the gauge's unit; power given | 0.1788 → 0.1722; raw −3.7% (95%: −31.5% to +24.1%), −0.0066 in the gauge's unit; GAIN | 0.1544 → 0.1414; raw −8.4% (95%: −72.0% to +55.1%), −0.0130 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 308.0 | 318.2 | 308 → 318.2; raw +3.3% (95%: −7.7% to +14.4%); power given | 304.3 → 291.1; raw −4.3% (95%: −36.7% to +28.0%); GAIN | 280.9 → 252.6; raw −10.1% (95%: −83.2% to +63.1%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.239 | 0.2313 → 0.239; raw +3.4% (95%: −7.7% to +14.4%), +0.0078 in the gauge's unit; power given | 0.2286 → 0.2186; raw −4.3% (95%: −36.8% to +28.1%), −0.0099 in the gauge's unit; GAIN | 0.2107 → 0.1894; raw −10.1% (95%: −83.2% to +63.0%), −0.0213 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | 2885 → 2884; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 2922 → 2922; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 2894 → 2903; raw +0.3% (95%: −0.4% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (operations a second) | 2,893 | 2,893 | 2893 → 2893; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2925 → 2925; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 2900 → 2909; raw +0.3% (95%: −0.3% to +1.0%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 0.505 | 0.504 | 0.505 → 0.5043; raw −0.1% (95%: −2.8% to +2.6%), −0.0007 in the gauge's unit; STEADY | 0.3643 → 0.3667; raw +0.6% (95%: −5.1% to +6.4%), +0.0023 in the gauge's unit; LOSS | 0.328 → 0.3313; raw +1.0% (95%: −4.0% to +6.1%), +0.0033 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.667 | 0.665 | 0.6673 → 0.665; raw −0.3% (95%: −8.7% to +8.0%), −0.0023 in the gauge's unit; STEADY | 0.5177 → 0.5283; raw +2.1% (95%: −6.3% to +10.4%), +0.0107 in the gauge's unit; LOSS | 0.4383 → 0.4637; raw +5.8% (95%: −11.1% to +22.6%), +0.0253 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.225 | 0.228 | 0.225 → 0.2275; raw +1.1% (95%: −2.7% to +4.9%), +0.0025 in the gauge's unit; LOSS | 0.1325 → 0.1337; raw +0.9% (95%: −5.0% to +6.7%), +0.0012 in the gauge's unit; LOSS | 0.175 → 0.1745; raw −0.2% (95%: −17.5% to +17.0%), −0.0004 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,506 | 1,507 | 1506 → 1507; raw +0.1% (95%: −0.5% to +0.7%); STEADY | 1517 → 1517; raw ±0.0% (95%: −0.4% to +0.3%); STEADY | 1508 → 1509; raw +0.1% (95%: −1.1% to +1.2%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| pages read into the cache (misses) | 77,632 | 77,724 | 7.763e+04 → 7.772e+04; raw +0.1% (95%: −0.2% to +0.4%) | 7.761e+04 → 7.767e+04; raw +0.1% (95%: −0.4% to +0.5%) | 7.75e+04 → 7.768e+04; raw +0.2% (95%: −0.2% to +0.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.197 | 0.1897 → 0.1974; raw +4.1% (95%: −34.2% to +42.3%), +0.0077 in the gauge's unit; power given | 0.1234 → 0.1044; raw −15.4% (95%: −116.1% to +85.3%), −0.0190 in the gauge's unit; GAIN | 0.1466 → 0.148; raw +0.9% (95%: −43.4% to +45.3%), +0.0014 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 131.7 | 137.8 | 131.7 → 137.8; raw +4.6% (95%: −42.4% to +51.7%); power given | 90.68 → 75.51; raw −16.7% (95%: −127.5% to +94.1%); GAIN | 105 → 106.2; raw +1.1% (95%: −51.3% to +53.5%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.259 | 0.2479 → 0.2594; raw +4.6% (95%: −42.1% to +51.4%), +0.0115 in the gauge's unit; power given | 0.17 → 0.1416; raw −16.7% (95%: −127.7% to +94.3%), −0.0284 in the gauge's unit; GAIN | 0.1978 → 0.1995; raw +0.8% (95%: −51.1% to +52.8%), +0.0017 in the gauge's unit; power given | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,897 | 2898 → 2897; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2933 → 2934; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 2934 → 2933; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,902 | 2,901 | 2902 → 2901; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 2935 → 2936; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 2936 → 2935; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.301 | 0.302 | 0.3013 → 0.3023; raw +0.3% (95%: −2.6% to +3.3%), +0.0010 in the gauge's unit; STEADY | 0.2023 → 0.201; raw −0.7% (95%: −6.7% to +5.4%), −0.0013 in the gauge's unit; GAIN | 0.2197 → 0.2217; raw +0.9% (95%: −2.1% to +3.9%), +0.0020 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 0.512 | 0.514 | 0.5123 → 0.5137; raw +0.3% (95%: −4.1% to +4.6%), +0.0013 in the gauge's unit; STEADY | 0.348 → 0.341; raw −2.0% (95%: −7.6% to +3.6%), −0.0070 in the gauge's unit; GAIN | 0.398 → 0.4007; raw +0.7% (95%: −3.6% to +4.9%), +0.0027 in the gauge's unit; LOSS | **the runs disagree** |
| latency, mean (ms) | 0.187 | 0.189 | 0.1872 → 0.1895; raw +1.2% (95%: −3.2% to +5.6%), +0.0022 in the gauge's unit; LOSS | 0.07484 → 0.07483; raw ±0.0% (95%: −5.9% to +5.9%), ±0.0000 in the gauge's unit; STEADY | 0.1054 → 0.1057; raw +0.3% (95%: −1.6% to +2.3%), +0.0003 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | 1348 → 1349; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 1350 → 1349; raw −0.1% (95%: −0.2% to +0.1%); STEADY | 1350 → 1349; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| pages read into the cache (misses) | 61,636 | 61,673 | 6.164e+04 → 6.167e+04; raw +0.1% (95%: −0.2% to +0.3%) | 6.163e+04 → 6.163e+04; raw ±0.0% (95%: −0.2% to +0.2%) | 6.169e+04 → 6.166e+04; raw −0.1% (95%: −0.3% to +0.2%) | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | 0.1645 → 0.1657; raw +0.7% (95%: −18.2% to +19.6%), +0.0012 in the gauge's unit; power given | 0.1076 → 0.09644; raw −10.3% (95%: −34.2% to +13.5%), −0.0111 in the gauge's unit; GAIN | 0.1285 → 0.1151; raw −10.4% (95%: −97.7% to +76.8%), −0.0134 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 280.8 | 283.1 | 280.8 → 283.1; raw +0.8% (95%: −21.9% to +23.5%); power given | 198.7 → 175.9; raw −11.5% (95%: −37.1% to +14.2%); GAIN | 239.6 → 211.1; raw −11.9% (95%: −110.9% to +87.1%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.213 | 0.2108 → 0.2125; raw +0.8% (95%: −21.9% to +23.6%), +0.0018 in the gauge's unit; power given | 0.1484 → 0.1314; raw −11.5% (95%: −37.2% to +14.2%), −0.0170 in the gauge's unit; GAIN | 0.179 → 0.1577; raw −11.9% (95%: −110.9% to +87.1%), −0.0213 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,605 | 5,582 | 5605 → 5582; raw −0.4% (95%: −1.8% to +1.0%); STEADY | 5707 → 5708; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 5738 → 5740; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.12%) |
| throughput (operations a second) | 5,620 | 5,598 | 5620 → 5598; raw −0.4% (95%: −1.8% to +1.0%); STEADY | 5720 → 5721; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 5748 → 5751; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, 95th percentile (ms) | 0.462 | 0.464 | 0.4617 → 0.4643; raw +0.6% (95%: −1.8% to +3.0%), +0.0027 in the gauge's unit; LOSS | 0.437 → 0.4387; raw +0.4% (95%: −0.5% to +1.2%), +0.0017 in the gauge's unit; STEADY | 0.359 → 0.3603; raw +0.4% (95%: −0.7% to +1.4%), +0.0013 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.44%) |
| latency, 99th percentile (ms) | 0.679 | 0.691 | 0.6793 → 0.691; raw +1.7% (95%: −2.6% to +6.0%), +0.0117 in the gauge's unit; LOSS | 0.6883 → 0.6877; raw −0.1% (95%: −1.0% to +0.8%), −0.0007 in the gauge's unit; STEADY | 0.5703 → 0.574; raw +0.6% (95%: −1.8% to +3.1%), +0.0037 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.269 | 0.27 | 0.2689 → 0.2701; raw +0.4% (95%: −1.6% to +2.5%), +0.0012 in the gauge's unit; STEADY | 0.2475 → 0.2478; raw +0.2% (95%: −0.7% to +1.0%), +0.0004 in the gauge's unit; STEADY | 0.1958 → 0.1969; raw +0.5% (95%: −0.3% to +1.4%), +0.0011 in the gauge's unit; LOSS | STEADY, under the floor (the three runs' mean 0.38%) |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,354 | 1,354 | 1354 → 1354; raw ±0.0% (95%: −0.5% to +0.4%); STEADY | 1361 → 1360; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 1364 → 1364; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| pages read into the cache (misses) | 62,550 | 62,641 | 6.255e+04 → 6.264e+04; raw +0.1% (95%: −1.3% to +1.6%) | 6.299e+04 → 6.286e+04; raw −0.2% (95%: −0.9% to +0.5%) | 6.289e+04 → 6.303e+04; raw +0.2% (95%: −0.3% to +0.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.298 | 0.304 | 0.2977 → 0.304; raw +2.1% (95%: −7.7% to +11.9%), +0.0062 in the gauge's unit; power given | 0.2543 → 0.2575; raw +1.2% (95%: −0.4% to +2.9%), +0.0031 in the gauge's unit; power given | 0.251 → 0.2668; raw +6.3% (95%: −3.4% to +16.0%), +0.0158 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 505.9 | 517.0 | 505.9 → 517; raw +2.2% (95%: −9.2% to +13.6%); power given | 427.8 → 434.1; raw +1.5% (95%: −0.1% to +3.1%); power given | 454 → 491.9; raw +8.4% (95%: −5.8% to +22.5%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.193 | 0.198 | 0.1933 → 0.1983; raw +2.6% (95%: −10.0% to +15.2%), +0.0050 in the gauge's unit; power given | 0.1611 → 0.1636; raw +1.5% (95%: −0.1% to +3.1%), +0.0024 in the gauge's unit; power given | 0.1707 → 0.1849; raw +8.3% (95%: −5.8% to +22.5%), +0.0142 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 0 gauge-rows GAIN, 5 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 22 STEADY, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
