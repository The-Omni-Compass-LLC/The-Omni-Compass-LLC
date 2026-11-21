# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `13f22e8141c4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,903 | +0.0% | -2.26 to 3.23 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,907 | +0.0% | -3.34 to 4.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.317 | -1.1% | -0.00992 to 0.00259 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.549 | 0.538 | -1.9% | -0.0155 to -0.00516 | GAIN |
| latency, mean (ms) | 0.126 | 0.125 | -0.8% | -0.00228 to 0.000272 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.1% | -1.58 to 0.195 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,819 | 61,816 | -0.0% | -416 to 411 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.165 | +9.1% | -0.0292 to 0.0565 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 303 | +10.8% | -61.9 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.228 | +10.8% | -0.0465 to 0.091 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `13f22e8141c4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -15 to 15.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -11.1 to 11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.424 | +0.0% | -0.028 to 0.028 | EVEN, the same |
| latency, 99th percentile (ms) | 0.618 | 0.615 | -0.5% | -0.0903 to 0.0843 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.223 | -0.2% | -0.0115 to 0.0104 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,510 | 1,512 | +0.1% | -10.9 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,585 | 77,694 | +0.1% | -202 to 420 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.184 | +8.7% | -0.0844 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 126 | +9.8% | -71.6 to 94 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.237 | +9.8% | -0.134 to 0.176 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `13f22e8141c4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% | -13.5 to 8.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,933 | -0.1% | -11.1 to 6.32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.205 | +4.1% | -0.0178 to 0.0338 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.324 | 0.336 | +3.7% | -0.0317 to 0.0557 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0753 | 0.0773 | +2.7% | -0.00784 to 0.0118 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,351 | 1,350 | -0.1% | -3.15 to 1.18 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,709 | 61,645 | -0.1% | -151 to 23 | shown, not judged |
| host CPU busy (share of the run) | 0.0969 | 0.0823 | -15.0% | -0.0808 to 0.0517 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 147 | -16.8% | -162 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.132 | 0.11 | -16.8% | -0.121 to 0.0766 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `13f22e8141c4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,815 | 5,820 | +0.1% | -7.39 to 17 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,824 | 5,829 | +0.1% | -8.88 to 18.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.219 | 0.219 | +0.0% | -0.0108 to 0.0108 | EVEN, the same |
| latency, 99th percentile (ms) | 0.424 | 0.424 | +0.2% | -0.0045 to 0.00584 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.111 | 0.11 | -0.5% | -0.00242 to 0.0013 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,366 | +0.2% | -3.34 to 9.78 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,180 | 63,290 | +0.2% | -243 to 462 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.14 | +1.1% | -0.0234 to 0.0264 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 252 | +1.3% | -51.1 to 57.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0928 | 0.094 | +1.3% | -0.0191 to 0.0215 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `13f22e8141c4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,891 | +0.0% | -2.4 to 4.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,897 | +0.0% | -2.72 to 4.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.342 | +1.2% | -0.000303 to 0.0083 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.529 | +0.6% | -0.00197 to 0.00797 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.211 | +0.8% | -0.00684 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,364 | +0.1% | -1.63 to 5.64 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,872 | 63,168 | +0.5% | -524 to 1,116 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.206 | +3.5% | -0.101 to 0.115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 354 | +4.2% | -214 to 243 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.266 | +4.2% | -0.161 to 0.182 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
