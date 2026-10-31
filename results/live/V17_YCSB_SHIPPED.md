# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40008048292 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| B | 40024485005 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| C | 40038808111 | `d02c7052ae50` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | 2904 → 2903; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2938 → 2938; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2881 → 2881; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,909 | 2,909 | 2909 → 2909; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2941 → 2941; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2886 → 2886; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.317 | 0.318 | 0.3167 → 0.3183; raw +0.5% (95%: −2.4% to +3.5%), +0.0017 in the gauge's unit; LOSS | 0.1293 → 0.1363; raw +5.4% (95%: −6.3% to +17.1%), +0.0070 in the gauge's unit; LOSS | 0.3383 → 0.346; raw +2.3% (95%: −1.2% to +5.7%), +0.0077 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.541 | 0.537 | 0.541 → 0.5373; raw −0.7% (95%: −3.4% to +2.0%), −0.0037 in the gauge's unit; GAIN | 0.3377 → 0.3497; raw +3.6% (95%: −0.9% to +8.0%), +0.0120 in the gauge's unit; LOSS | 0.529 → 0.5313; raw +0.4% (95%: −0.9% to +1.8%), +0.0023 in the gauge's unit; STEADY | **the runs disagree** |
| latency, mean (ms) | 0.143 | 0.142 | 0.1428 → 0.1418; raw −0.7% (95%: −1.3% to −0.1%), −0.0010 in the gauge's unit; GAIN | 0.07143 → 0.07238; raw +1.3% (95%: −7.4% to +10.0%), +0.0009 in the gauge's unit; LOSS | 0.2047 → 0.2056; raw +0.4% (95%: −1.5% to +2.3%), +0.0009 in the gauge's unit; STEADY | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | 7481 → 7481; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | 1362 → 1363; raw ±0.0% (95%: −0.3% to +0.4%); STEADY | 1363 → 1363; raw ±0.0% (95%: −0.5% to +0.5%); STEADY | 1364 → 1363; raw −0.1% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 63,122 | 63,014 | 6.312e+04 → 6.301e+04; raw −0.2% (95%: −1.3% to +1.0%) | 6.339e+04 → 6.322e+04; raw −0.3% (95%: −0.7% to +0.2%) | 6.314e+04 → 6.346e+04; raw +0.5% (95%: −1.6% to +2.6%) | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.172 | 0.1748 → 0.1717; raw −1.8% (95%: −9.6% to +6.1%), −0.0031 in the gauge's unit; GAIN | 0.08881 → 0.1051; raw +18.4% (95%: −70.3% to +107.1%), +0.0163 in the gauge's unit; power given | 0.24 → 0.2135; raw −11.0% (95%: −37.9% to +15.9%), −0.0264 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 316.2 | 309.9 | 316.2 → 309.9; raw −2.0% (95%: −11.1% to +7.2%); GAIN | 159.7 → 191.6; raw +20.0% (95%: −79.2% to +119.2%); power given | 428.4 → 366.6; raw −14.4% (95%: −49.4% to +20.6%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.233 | 0.2372 → 0.2326; raw −1.9% (95%: −11.1% to +7.2%), −0.0046 in the gauge's unit; GAIN | 0.1192 → 0.1431; raw +20.0% (95%: −79.3% to +119.3%), +0.0239 in the gauge's unit; power given | 0.3222 → 0.2757; raw −14.4% (95%: −49.3% to +20.5%), −0.0465 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,873 | 2910 → 2873; raw −1.3% (95%: −6.6% to +4.1%); LOSS | 2908 → 2909; raw +0.1% (95%: −0.3% to +0.4%); STEADY | 2884 → 2885; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.39%) |
| throughput (operations a second) | 2,915 | 2,879 | 2915 → 2879; raw −1.2% (95%: −6.5% to +4.0%); LOSS | 2912 → 2914; raw +0.1% (95%: −0.3% to +0.4%); STEADY | 2888 → 2889; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.38%) |
| latency, 95th percentile (ms) | 0.199 | 0.204 | 0.1987 → 0.2037; raw +2.5% (95%: −4.1% to +9.1%), +0.0050 in the gauge's unit; LOSS | 0.1993 → 0.2053; raw +3.0% (95%: +1.8% to +4.3%), +0.0060 in the gauge's unit; LOSS | 0.3327 → 0.333; raw +0.1% (95%: −8.9% to +9.1%), +0.0003 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.379 | 0.389 | 0.3787 → 0.389; raw +2.7% (95%: −3.5% to +8.9%), +0.0103 in the gauge's unit; LOSS | 0.3917 → 0.4023; raw +2.7% (95%: −3.6% to +9.1%), +0.0107 in the gauge's unit; LOSS | 0.5053 → 0.507; raw +0.3% (95%: −3.7% to +4.3%), +0.0017 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.145 | 0.153 | 0.145 → 0.1535; raw +5.9% (95%: −18.4% to +30.2%), +0.0085 in the gauge's unit; LOSS | 0.1452 → 0.1419; raw −2.3% (95%: −19.9% to +15.3%), −0.0033 in the gauge's unit; GAIN | 0.1912 → 0.1923; raw +0.6% (95%: −3.1% to +4.2%), +0.0011 in the gauge's unit; LOSS | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,361 | 1366 → 1361; raw −0.4% (95%: −1.5% to +0.7%); STEADY | 1363 → 1365; raw +0.1% (95%: −0.9% to +1.2%); STEADY | 1365 → 1366; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| pages read into the cache (misses) | 61,806 | 61,852 | 6.181e+04 → 6.185e+04; raw +0.1% (95%: −0.5% to +0.6%) | 6.18e+04 → 6.186e+04; raw +0.1% (95%: ±0.0% to +0.2%) | 6.181e+04 → 6.189e+04; raw +0.1% (95%: −0.6% to +0.8%) | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.153 | 0.1418 → 0.1528; raw +7.8% (95%: −24.2% to +39.8%), +0.0110 in the gauge's unit; power given | 0.1409 → 0.1645; raw +16.8% (95%: −15.4% to +48.9%), +0.0236 in the gauge's unit; power given | 0.2093 → 0.2011; raw −3.9% (95%: −12.6% to +4.8%), −0.0082 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 252.8 | 276.6 | 252.8 → 276.6; raw +9.4% (95%: −28.2% to +47.1%); power given | 250.8 → 301; raw +20.0% (95%: −17.8% to +57.8%); power given | 371 → 352.5; raw −5.0% (95%: −17.2% to +7.3%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.21 | 0.1893 → 0.2096; raw +10.7% (95%: −26.2% to +47.5%), +0.0202 in the gauge's unit; power given | 0.1878 → 0.2254; raw +20.0% (95%: −17.6% to +57.6%), +0.0375 in the gauge's unit; power given | 0.2789 → 0.2649; raw −5.0% (95%: −17.2% to +7.2%), −0.0139 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,878 | 2880 → 2878; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | 2884 → 2884; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2901 → 2894; raw −0.2% (95%: −0.5% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 2,886 | 2,885 | 2886 → 2885; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2890 → 2889; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2913 → 2908; raw −0.1% (95%: −0.5% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 0.424 | 0.43 | 0.4243 → 0.43; raw +1.3% (95%: −8.2% to +10.9%), +0.0057 in the gauge's unit; LOSS | 0.5057 → 0.5067; raw +0.2% (95%: −2.4% to +2.8%), +0.0010 in the gauge's unit; STEADY | 0.3087 → 0.3197; raw +3.6% (95%: −7.8% to +14.9%), +0.0110 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.582 | 0.597 | 0.5823 → 0.597; raw +2.5% (95%: −7.7% to +12.8%), +0.0147 in the gauge's unit; LOSS | 0.6317 → 0.6293; raw −0.4% (95%: −3.7% to +3.0%), −0.0023 in the gauge's unit; STEADY | 0.477 → 0.5083; raw +6.6% (95%: −1.3% to +14.4%), +0.0313 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.212 | 0.214 | 0.2117 → 0.2137; raw +1.0% (95%: −7.7% to +9.6%), +0.0020 in the gauge's unit; LOSS | 0.2155 → 0.2146; raw −0.4% (95%: −3.2% to +2.4%), −0.0009 in the gauge's unit; STEADY | 0.1627 → 0.1757; raw +8.0% (95%: −9.7% to +25.6%), +0.0129 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,511 | 1512 → 1511; raw −0.1% (95%: −0.3% to +0.2%); STEADY | 1506 → 1505; raw −0.1% (95%: −0.4% to +0.3%); STEADY | 1514 → 1505; raw −0.6% (95%: −2.1% to +0.9%); GAIN | STEADY, under the floor (the three runs' mean 0.23%) |
| pages read into the cache (misses) | 77,615 | 77,649 | 7.761e+04 → 7.765e+04; raw ±0.0% (95%: −0.1% to +0.2%) | 7.758e+04 → 7.76e+04; raw ±0.0% (95%: −0.3% to +0.4%) | 7.767e+04 → 7.772e+04; raw +0.1% (95%: −0.6% to +0.8%) | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.215 | 0.2154 → 0.2149; raw −0.2% (95%: −25.2% to +24.8%), −0.0004 in the gauge's unit; STEADY | 0.1883 → 0.2107; raw +11.9% (95%: −47.7% to +71.5%), +0.0224 in the gauge's unit; power given | 0.1445 → 0.1633; raw +13.0% (95%: −35.2% to +61.2%), +0.0188 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 154.3 | 153.0 | 154.3 → 153; raw −0.8% (95%: −33.6% to +31.9%); GAIN | 132.7 → 151.5; raw +14.2% (95%: −59.9% to +88.3%); power given | 103.4 → 119.4; raw +15.5% (95%: −43.9% to +74.9%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.288 | 0.2903 → 0.288; raw −0.8% (95%: −33.4% to +31.8%), −0.0023 in the gauge's unit; GAIN | 0.2496 → 0.2849; raw +14.1% (95%: −60.0% to +88.2%), +0.0353 in the gauge's unit; power given | 0.1941 → 0.2245; raw +15.6% (95%: −43.7% to +75.0%), +0.0303 in the gauge's unit; power given | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,940 | 2943 → 2940; raw −0.1% (95%: −0.2% to ±0.0%); STEADY | 2885 → 2885; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | 2885 → 2885; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,945 | 2,942 | 2945 → 2942; raw −0.1% (95%: −0.1% to −0.1%); STEADY | 2890 → 2889; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2891 → 2891; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 0.075 | 0.0873 | 0.075 → 0.08733; raw +16.4% (95%: −28.5% to +61.4%), +0.0123 in the gauge's unit; LOSS | 0.306 → 0.303; raw −1.0% (95%: −1.8% to −0.2%), −0.0030 in the gauge's unit; GAIN | 0.2963 → 0.3013; raw +1.7% (95%: −5.9% to +9.2%), +0.0050 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 0.258 | 0.278 | 0.2583 → 0.2783; raw +7.7% (95%: −20.2% to +35.7%), +0.0200 in the gauge's unit; LOSS | 0.521 → 0.5193; raw −0.3% (95%: −1.9% to +1.2%), −0.0017 in the gauge's unit; STEADY | 0.58 → 0.5807; raw +0.1% (95%: −3.5% to +3.7%), +0.0007 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0497 | 0.0535 | 0.04971 → 0.05355; raw +7.7% (95%: −12.2% to +27.7%), +0.0038 in the gauge's unit; LOSS | 0.1859 → 0.1864; raw +0.2% (95%: −2.3% to +2.8%), +0.0005 in the gauge's unit; STEADY | 0.1855 → 0.1868; raw +0.7% (95%: −1.6% to +3.0%), +0.0013 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | 1350 → 1350; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1348 → 1349; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1348 → 1348; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 61,661 | 61,666 | 6.166e+04 → 6.167e+04; raw ±0.0% (95%: −0.3% to +0.3%) | 6.166e+04 → 6.167e+04; raw ±0.0% (95%: −0.2% to +0.3%) | 6.167e+04 → 6.164e+04; raw −0.1% (95%: −0.3% to +0.2%) | shown, not judged |
| host CPU busy (share of the run) | 0.079 | 0.0673 | 0.07903 → 0.06726; raw −14.9% (95%: −76.3% to +46.5%), −0.0118 in the gauge's unit; GAIN | 0.196 → 0.1979; raw +1.0% (95%: −59.0% to +61.1%), +0.0020 in the gauge's unit; power given | 0.1778 → 0.1706; raw −4.1% (95%: −15.6% to +7.4%), −0.0073 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 145.3 | 121.0 | 145.3 → 121; raw −16.7% (95%: −82.0% to +48.6%); GAIN | 347.6 → 350.7; raw +0.9% (95%: −75.5% to +77.3%); power given | 309 → 293.2; raw −5.1% (95%: −18.7% to +8.4%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.108 | 0.0904 | 0.1084 → 0.09037; raw −16.6% (95%: −82.0% to +48.7%), −0.0180 in the gauge's unit; GAIN | 0.2612 → 0.2636; raw +0.9% (95%: −75.5% to +77.3%), +0.0024 in the gauge's unit; power given | 0.2323 → 0.2204; raw −5.1% (95%: −18.6% to +8.3%), −0.0119 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7483 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,729 | 5725 → 5729; raw +0.1% (95%: −0.2% to +0.3%); STEADY | 5670 → 5529; raw −2.5% (95%: −4.1% to −0.9%); LOSS | 5754 → 5758; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (operations a second) | 5,740 | 5,742 | 5740 → 5742; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 5683 → 5544; raw −2.4% (95%: −3.9% to −1.0%); LOSS | 5767 → 5771; raw +0.1% (95%: ±0.0% to +0.2%); STEADY | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 95th percentile (ms) | 0.372 | 0.37 | 0.3717 → 0.3697; raw −0.5% (95%: −6.2% to +5.2%), −0.0020 in the gauge's unit; GAIN | 0.309 → 0.3093; raw +0.1% (95%: −4.6% to +4.8%), +0.0003 in the gauge's unit; STEADY | 0.3303 → 0.3313; raw +0.3% (95%: −1.0% to +1.6%), +0.0010 in the gauge's unit; STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 0.645 | 0.637 | 0.6453 → 0.6367; raw −1.3% (95%: −7.2% to +4.6%), −0.0087 in the gauge's unit; GAIN | 0.467 → 0.492; raw +5.4% (95%: −10.5% to +21.2%), +0.0250 in the gauge's unit; LOSS | 0.5987 → 0.6003; raw +0.3% (95%: −1.8% to +2.4%), +0.0017 in the gauge's unit; STEADY | **the runs disagree** |
| latency, mean (ms) | 0.191 | 0.191 | 0.1911 → 0.1908; raw −0.2% (95%: −5.1% to +4.8%), −0.0003 in the gauge's unit; STEADY | 0.1902 → 0.1978; raw +4.0% (95%: +0.9% to +7.1%), +0.0076 in the gauge's unit; LOSS | 0.1562 → 0.1551; raw −0.7% (95%: −3.3% to +1.9%), −0.0011 in the gauge's unit; GAIN | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,483 | 7,483 | 7483 → 7483; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7481 → 7481; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | 1363 → 1362; raw ±0.0% (95%: −0.6% to +0.5%); STEADY | 1355 → 1352; raw −0.2% (95%: −1.2% to +0.8%); STEADY | 1362 → 1361; raw −0.1% (95%: −0.4% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.11%) |
| pages read into the cache (misses) | 62,970 | 62,955 | 6.297e+04 → 6.296e+04; raw ±0.0% (95%: −2.1% to +2.1%) | 6.302e+04 → 6.303e+04; raw ±0.0% (95%: −0.9% to +0.9%) | 6.301e+04 → 6.314e+04; raw +0.2% (95%: −1.5% to +1.9%) | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.248 | 0.2538 → 0.2477; raw −2.4% (95%: −4.5% to −0.4%), −0.0061 in the gauge's unit; GAIN | 0.2342 → 0.2159; raw −7.8% (95%: −31.6% to +16.0%), −0.0183 in the gauge's unit; GAIN | 0.2312 → 0.2197; raw −5.0% (95%: −9.3% to −0.6%), −0.0115 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 467.4 | 451.9 | 467.4 → 451.9; raw −3.3% (95%: −6.1% to −0.5%); GAIN | 429 → 388.5; raw −9.4% (95%: −37.8% to +18.9%); GAIN | 430.2 → 402.7; raw −6.4% (95%: −12.0% to −0.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.17 | 0.176 → 0.1701; raw −3.4% (95%: −6.3% to −0.5%), −0.0059 in the gauge's unit; GAIN | 0.1633 → 0.1515; raw −7.2% (95%: −36.8% to +22.4%), −0.0118 in the gauge's unit; GAIN | 0.1615 → 0.1511; raw −6.4% (95%: −11.9% to −0.9%), −0.0104 in the gauge's unit; GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 3 gauge-rows GAIN, 9 LOSS, 1 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 19 STEADY, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
