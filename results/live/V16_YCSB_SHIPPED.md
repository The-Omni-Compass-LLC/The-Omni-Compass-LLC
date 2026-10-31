# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39826088859 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39846968680 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39866167058 | `5f430c111d90` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | 2886 → 2885; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2934 → 2936; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 2921 → 2920; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,890 | 2,890 | 2890 → 2890; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2937 → 2938; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2924 → 2923; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.324 | 0.325 | 0.324 → 0.3253; raw +0.4% (95%: −5.2% to +6.1%), +0.0013 in the gauge's unit; STEADY | 0.152 → 0.1517; raw −0.2% (95%: −13.8% to +13.4%), −0.0003 in the gauge's unit; STEADY | 0.2123 → 0.2173; raw +2.4% (95%: −7.2% to +11.9%), +0.0050 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.474 | 0.474 | 0.4743 → 0.474; raw −0.1% (95%: −3.0% to +2.9%), −0.0003 in the gauge's unit; STEADY | 0.3573 → 0.3603; raw +0.8% (95%: −7.0% to +8.7%), +0.0030 in the gauge's unit; LOSS | 0.4373 → 0.442; raw +1.1% (95%: −7.0% to +9.1%), +0.0047 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.192 | 0.192 | 0.1915 → 0.1921; raw +0.3% (95%: −1.3% to +1.8%), +0.0006 in the gauge's unit; STEADY | 0.07464 → 0.07394; raw −0.9% (95%: −3.5% to +1.6%), −0.0007 in the gauge's unit; GAIN | 0.112 → 0.1127; raw +0.7% (95%: −1.4% to +2.7%), +0.0007 in the gauge's unit; LOSS | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7481 → 7481; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | 1365 → 1365; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1364 → 1364; raw ±0.0% (95%: −0.4% to +0.4%); STEADY | 1364 → 1364; raw ±0.0% (95%: −0.7% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| pages read into the cache (misses) | 62,971 | 63,263 | 6.297e+04 → 6.326e+04; raw +0.5% (95%: −1.8% to +2.7%) | 6.339e+04 → 6.343e+04; raw +0.1% (95%: −1.4% to +1.5%) | 6.345e+04 → 6.315e+04; raw −0.5% (95%: −2.7% to +1.7%) | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.216 | 0.228 → 0.2163; raw −5.1% (95%: −52.2% to +42.0%), −0.0116 in the gauge's unit; GAIN | 0.09608 → 0.09838; raw +2.4% (95%: −32.8% to +37.6%), +0.0023 in the gauge's unit; power given | 0.145 → 0.142; raw −2.1% (95%: −37.1% to +33.0%), −0.0030 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 409.8 | 383.9 | 409.8 → 383.9; raw −6.3% (95%: −67.1% to +54.5%); GAIN | 172.9 → 176.8; raw +2.3% (95%: −36.3% to +40.9%); power given | 262.7 → 255.7; raw −2.7% (95%: −44.4% to +39.0%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.288 | 0.3077 → 0.2883; raw −6.3% (95%: −67.0% to +54.4%), −0.0194 in the gauge's unit; GAIN | 0.1292 → 0.1321; raw +2.3% (95%: −36.2% to +40.8%), +0.0029 in the gauge's unit; power given | 0.1966 → 0.1914; raw −2.7% (95%: −44.4% to +39.0%), −0.0052 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,914 | 2912 → 2914; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 2940 → 2939; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2890 → 2890; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,915 | 2,917 | 2915 → 2917; raw +0.1% (95%: −0.1% to +0.2%); STEADY | 2942 → 2941; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 2893 → 2893; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.208 | 0.207 | 0.2083 → 0.207; raw −0.6% (95%: −19.2% to +17.9%), −0.0013 in the gauge's unit; GAIN | 0.1307 → 0.1317; raw +0.8% (95%: −34.8% to +36.3%), +0.0010 in the gauge's unit; LOSS | 0.304 → 0.3103; raw +2.1% (95%: −6.6% to +10.7%), +0.0063 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 0.44 | 0.444 | 0.44 → 0.4437; raw +0.8% (95%: −18.4% to +20.1%), +0.0037 in the gauge's unit; LOSS | 0.3367 → 0.333; raw −1.1% (95%: −14.0% to +11.8%), −0.0037 in the gauge's unit; GAIN | 0.493 → 0.4977; raw +0.9% (95%: −1.8% to +3.7%), +0.0047 in the gauge's unit; LOSS | **the runs disagree** |
| latency, mean (ms) | 0.11 | 0.108 | 0.1102 → 0.1082; raw −1.8% (95%: −11.4% to +7.8%), −0.0020 in the gauge's unit; GAIN | 0.06066 → 0.0603; raw −0.6% (95%: −11.7% to +10.5%), −0.0004 in the gauge's unit; GAIN | 0.1811 → 0.1831; raw +1.1% (95%: −3.7% to +6.0%), +0.0020 in the gauge's unit; LOSS | **the runs disagree** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | 7481 → 7481; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7484 → 7484; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | 1365 → 1366; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 1367 → 1366; raw −0.1% (95%: −0.3% to +0.2%); STEADY | 1366 → 1365; raw −0.1% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.04%) |
| pages read into the cache (misses) | 61,768 | 61,844 | 6.177e+04 → 6.184e+04; raw +0.1% (95%: −0.4% to +0.6%) | 6.183e+04 → 6.184e+04; raw ±0.0% (95%: −0.6% to +0.6%) | 6.182e+04 → 6.182e+04; raw ±0.0% (95%: −0.6% to +0.6%) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | 0.1452 → 0.1264; raw −13.0% (95%: −74.7% to +48.8%), −0.0188 in the gauge's unit; GAIN | 0.08827 → 0.07377; raw −16.4% (95%: −82.2% to +49.4%), −0.0145 in the gauge's unit; GAIN | 0.179 → 0.1816; raw +1.5% (95%: −8.8% to +11.7%), +0.0026 in the gauge's unit; power given | **the runs disagree** |
| host CPU-seconds | 266.7 | 227.0 | 266.7 → 227; raw −14.9% (95%: −86.3% to +56.5%); GAIN | 162.1 → 132.6; raw −18.2% (95%: −91.9% to +55.4%); GAIN | 311.2 → 316.3; raw +1.6% (95%: −9.8% to +13.1%); power given | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.17 | 0.1997 → 0.17; raw −14.9% (95%: −86.3% to +56.5%), −0.0297 in the gauge's unit; GAIN | 0.121 → 0.099; raw −18.2% (95%: −91.9% to +55.5%), −0.0220 in the gauge's unit; GAIN | 0.2337 → 0.2375; raw +1.6% (95%: −9.8% to +13.1%), +0.0038 in the gauge's unit; power given | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | 2878 → 2879; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 2939 → 2937; raw −0.1% (95%: −0.5% to +0.4%); STEADY | 2940 → 2940; raw ±0.0% (95%: −0.2% to +0.1%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,887 | 2,888 | 2887 → 2888; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 2942 → 2940; raw −0.1% (95%: −0.4% to +0.3%); STEADY | 2942 → 2942; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.468 | 0.474 | 0.468 → 0.4737; raw +1.2% (95%: −1.5% to +3.9%), +0.0057 in the gauge's unit; LOSS | 0.2473 → 0.2563; raw +3.6% (95%: −12.3% to +19.6%), +0.0090 in the gauge's unit; LOSS | 0.2283 → 0.2303; raw +0.9% (95%: −7.0% to +8.7%), +0.0020 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.644 | 0.654 | 0.644 → 0.6537; raw +1.5% (95%: −2.8% to +5.8%), +0.0097 in the gauge's unit; LOSS | 0.3797 → 0.3993; raw +5.2% (95%: −23.9% to +34.2%), +0.0197 in the gauge's unit; LOSS | 0.3547 → 0.355; raw +0.1% (95%: −7.6% to +7.8%), +0.0003 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.215 | 0.217 | 0.215 → 0.2166; raw +0.8% (95%: −0.3% to +1.8%), +0.0016 in the gauge's unit; LOSS | 0.0753 → 0.07704; raw +2.3% (95%: −30.7% to +35.3%), +0.0017 in the gauge's unit; LOSS | 0.06965 → 0.06964; raw ±0.0% (95%: −3.3% to +3.3%), ±0.0000 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,508 | 1508 → 1508; raw ±0.0% (95%: −0.3% to +0.3%); STEADY | 1518 → 1522; raw +0.3% (95%: ±0.0% to +0.6%); STEADY | 1519 → 1522; raw +0.2% (95%: −0.1% to +0.4%); STEADY | STEADY, under the floor (the three runs' mean 0.17%) |
| pages read into the cache (misses) | 77,635 | 77,725 | 7.763e+04 → 7.772e+04; raw +0.1% (95%: −0.1% to +0.3%) | 7.756e+04 → 7.767e+04; raw +0.1% (95%: −0.1% to +0.4%) | 7.771e+04 → 7.774e+04; raw ±0.0% (95%: −0.1% to +0.2%) | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.203 | 0.1681 → 0.2031; raw +20.9% (95%: −14.8% to +56.5%), +0.0351 in the gauge's unit; power given | 0.05998 → 0.08287; raw +38.2% (95%: −55.3% to +131.6%), +0.0229 in the gauge's unit; power given | 0.1134 → 0.05986; raw −47.2% (95%: −71.6% to −22.8%), −0.0535 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 114.0 | 143.5 | 114 → 143.5; raw +25.9% (95%: −19.5% to +71.4%); power given | 42.6 → 60.37; raw +41.7% (95%: −62.5% to +145.9%); power given | 85.65 → 42.7; raw −50.1% (95%: −76.7% to −23.6%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.27 | 0.2146 → 0.2702; raw +25.9% (95%: −19.6% to +71.4%), +0.0556 in the gauge's unit; power given | 0.07951 → 0.1127; raw +41.8% (95%: −62.7% to +146.3%), +0.0332 in the gauge's unit; power given | 0.1598 → 0.07969; raw −50.1% (95%: −76.7% to −23.6%), −0.0801 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,938 | 2936 → 2938; raw +0.1% (95%: ±0.0% to +0.1%); STEADY | 2897 → 2895; raw −0.1% (95%: −0.5% to +0.4%); STEADY | 2914 → 2914; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,938 | 2,940 | 2938 → 2940; raw +0.1% (95%: ±0.0% to +0.1%); STEADY | 2902 → 2899; raw −0.1% (95%: −0.4% to +0.3%); STEADY | 2917 → 2917; raw ±0.0% (95%: −0.1% to ±0.0%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.092 | 0.0923 | 0.092 → 0.09233; raw +0.4% (95%: −10.6% to +11.3%), +0.0003 in the gauge's unit; STEADY | 0.2027 → 0.206; raw +1.6% (95%: −7.6% to +10.9%), +0.0033 in the gauge's unit; LOSS | 0.175 → 0.175; raw ±0.0% (95%: −1.4% to +1.4%), ±0.0000 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.301 | 0.315 | 0.3007 → 0.315; raw +4.8% (95%: −4.3% to +13.9%), +0.0143 in the gauge's unit; LOSS | 0.3803 → 0.3803; raw ±0.0% (95%: −15.4% to +15.4%), ±0.0000 in the gauge's unit; STEADY | 0.3513 → 0.356; raw +1.3% (95%: −5.8% to +8.4%), +0.0047 in the gauge's unit; LOSS | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0566 | 0.0571 | 0.05656 → 0.05705; raw +0.9% (95%: −1.2% to +2.9%), +0.0005 in the gauge's unit; LOSS | 0.1482 → 0.152; raw +2.5% (95%: −7.0% to +12.1%), +0.0038 in the gauge's unit; LOSS | 0.1253 → 0.1255; raw +0.2% (95%: −4.1% to +4.5%), +0.0003 in the gauge's unit; STEADY | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | 1350 → 1350; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1347 → 1346; raw ±0.0% (95%: −0.3% to +0.2%); STEADY | 1349 → 1349; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 61,695 | 61,697 | 6.17e+04 → 6.17e+04; raw ±0.0% (95%: −0.2% to +0.2%) | 6.161e+04 → 6.164e+04; raw ±0.0% (95%: −0.2% to +0.2%) | 6.162e+04 → 6.165e+04; raw +0.1% (95%: −0.3% to +0.4%) | shown, not judged |
| host CPU busy (share of the run) | 0.0737 | 0.0811 | 0.07366 → 0.08113; raw +10.1% (95%: −9.4% to +29.7%), +0.0075 in the gauge's unit; power given | 0.1576 → 0.1702; raw +8.0% (95%: −14.5% to +30.5%), +0.0126 in the gauge's unit; power given | 0.1301 → 0.1293; raw −0.6% (95%: −116.5% to +115.3%), −0.0008 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 132.8 | 147.6 | 132.8 → 147.6; raw +11.1% (95%: −10.9% to +33.1%); power given | 281.4 → 307.7; raw +9.3% (95%: −19.6% to +38.3%); power given | 233.5 → 230.8; raw −1.2% (95%: −132.8% to +130.5%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.0992 | 0.11 | 0.09921 → 0.1102; raw +11.1% (95%: −10.8% to +33.0%), +0.0110 in the gauge's unit; power given | 0.211 → 0.2308; raw +9.4% (95%: −19.4% to +38.1%), +0.0197 in the gauge's unit; power given | 0.1747 → 0.1727; raw −1.1% (95%: −132.7% to +130.4%), −0.0020 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,682 | 5681 → 5682; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5752 → 5754; raw ±0.0% (95%: −0.2% to +0.3%); STEADY | 5663 → 5673; raw +0.2% (95%: −0.4% to +0.8%); STEADY | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 5,694 | 5,695 | 5694 → 5695; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5764 → 5766; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | 5675 → 5684; raw +0.2% (95%: −0.4% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 0.414 | 0.415 | 0.4143 → 0.4147; raw +0.1% (95%: −1.2% to +1.3%), +0.0003 in the gauge's unit; STEADY | 0.307 → 0.3067; raw −0.1% (95%: −1.0% to +0.8%), −0.0003 in the gauge's unit; STEADY | 0.4097 → 0.4047; raw −1.2% (95%: −6.6% to +4.2%), −0.0050 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.42%) |
| latency, 99th percentile (ms) | 0.635 | 0.641 | 0.6353 → 0.641; raw +0.9% (95%: −2.6% to +4.4%), +0.0057 in the gauge's unit; LOSS | 0.4563 → 0.4683; raw +2.6% (95%: −9.5% to +14.8%), +0.0120 in the gauge's unit; LOSS | 0.6213 → 0.6047; raw −2.7% (95%: −11.8% to +6.4%), −0.0167 in the gauge's unit; GAIN | **the runs disagree** |
| latency, mean (ms) | 0.236 | 0.236 | 0.2364 → 0.2362; raw −0.1% (95%: −0.7% to +0.6%), −0.0002 in the gauge's unit; STEADY | 0.1793 → 0.179; raw −0.2% (95%: −4.4% to +4.0%), −0.0004 in the gauge's unit; STEADY | 0.2301 → 0.2279; raw −1.0% (95%: −5.2% to +3.2%), −0.0022 in the gauge's unit; GAIN | STEADY, under the floor (the three runs' mean 0.41%) |
| failed operations | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 7482 → 7482; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,361 | 1361 → 1361; raw ±0.0% (95%: ±0.0% to +0.1%); STEADY | 1362 → 1364; raw +0.2% (95%: −0.7% to +1.1%); STEADY | 1362 → 1360; raw −0.2% (95%: −0.7% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.02%) |
| pages read into the cache (misses) | 62,753 | 62,987 | 6.275e+04 → 6.299e+04; raw +0.4% (95%: −0.8% to +1.5%) | 6.311e+04 → 6.315e+04; raw +0.1% (95%: −0.6% to +0.7%) | 6.287e+04 → 6.292e+04; raw +0.1% (95%: −1.4% to +1.6%) | shown, not judged |
| host CPU busy (share of the run) | 0.297 | 0.299 | 0.2968 → 0.2993; raw +0.9% (95%: −5.9% to +7.6%), +0.0025 in the gauge's unit; power given | 0.2273 → 0.2332; raw +2.6% (95%: −28.8% to +34.0%), +0.0059 in the gauge's unit; power given | 0.31 → 0.2906; raw −6.3% (95%: −22.1% to +9.6%), −0.0194 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 531.9 | 539.1 | 531.9 → 539.1; raw +1.4% (95%: −8.5% to +11.3%); power given | 410.7 → 425.8; raw +3.7% (95%: −37.3% to +44.6%); power given | 571.4 → 523.2; raw −8.4% (95%: −29.4% to +12.6%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.203 | 0.2007 → 0.2033; raw +1.3% (95%: −8.6% to +11.2%), +0.0026 in the gauge's unit; power given | 0.154 → 0.1596; raw +3.7% (95%: −37.4% to +44.7%), +0.0056 in the gauge's unit; power given | 0.2158 → 0.1973; raw −8.5% (95%: −29.8% to +12.7%), −0.0184 in the gauge's unit; GAIN | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 0 gauge-rows GAIN, 6 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 22 STEADY, 16 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
