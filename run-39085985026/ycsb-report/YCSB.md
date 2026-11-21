# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,891 | +0.0% | -2.77 to 3.99 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,897 | +0.0% | -1.67 to 2.81 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.351 | -0.9% | -0.0342 to 0.0275 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.6 | 0.592 | -1.4% | -0.0325 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.201 | -1.4% | -0.0113 to 0.00573 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -3.19 to 4.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,806 | 61,905 | +0.2% | -368 to 566 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.177 | -5.7% | -0.0438 to 0.0224 | EVEN, no difference beyond the noise |
| host CPU-seconds | 324 | 303 | -6.5% | -86.7 to 44.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.227 | -6.5% | -0.0655 to 0.0337 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -9.44 to 6.93 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,894 | 2,893 | -0.0% | -8.49 to 6.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.414 | 0.422 | +2.1% | -0.0234 to 0.0407 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.553 | 0.562 | +1.6% | -0.00391 to 0.0219 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.219 | +0.2% | -0.00717 to 0.0082 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,512 | +0.0% | -7.54 to 8.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,598 | 77,666 | +0.1% | 9.58 to 126 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.1% | -0.0397 to 0.0402 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 110 | +0.6% | -31.1 to 32.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.206 | +0.6% | -0.0587 to 0.0612 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -1.74 to 1.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,939 | -0.0% | -1.58 to 0.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.161 | 0.154 | -4.4% | -0.0145 to 0.000453 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.316 | 0.31 | -1.7% | -0.0141 to 0.00339 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0695 | 0.0685 | -1.5% | -0.0024 to 0.000355 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | +0.0% | -2.45 to 3.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,682 | 61,723 | +0.1% | -161 to 243 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0735 | -30.2% | -0.1 to 0.0363 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 132 | -32.0% | -197 to 71.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.145 | 0.0988 | -32.0% | -0.147 to 0.0535 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,818 | 5,818 | -0.0% | -14.1 to 13.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,827 | 5,826 | -0.0% | -12.7 to 10.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.218 | -3.4% | -0.0202 to 0.00484 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.427 | 0.409 | -4.2% | -0.0354 to -0.00061 | GAIN |
| latency, mean (ms) | 0.11 | 0.109 | -1.3% | -0.0118 to 0.0088 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -5.91 to 4.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,108 | 63,102 | -0.0% | -313 to 302 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.152 | -2.3% | -0.0697 to 0.0627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 285 | 277 | -2.7% | -150 to 134 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.106 | 0.104 | -2.7% | -0.056 to 0.0503 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `8ad09824e445`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,859 | 2,811 | -1.7% | -259 to 165 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,866 | 2,820 | -1.6% | -258 to 165 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.263 | 0.271 | +3.0% | -0.0114 to 0.0274 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.415 | 0.422 | +1.8% | -0.0189 to 0.0342 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.21 | +0.5% | -0.0482 to 0.0505 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,347 | -0.2% | -46.3 to 40.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,000 | 62,927 | -0.1% | -1,046 to 899 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.176 | -5.1% | -0.0362 to 0.0173 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 318 | -6.4% | -81.3 to 37.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.247 | -4.8% | -0.0683 to 0.0436 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
