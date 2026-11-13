# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -2.63 to 1.67 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0188 to 0.00709 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00108 to 0.000711 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0042 to 0.00281 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.28 | +0.8% | -0.137 to 0.217 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.54 | +0.4% | -0.016 to 0.028 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.4% | -3.18 to -2.42 | GAIN |
| memory used, mean (MB) | 57.2 | 55.3 | -3.3% | -2.28 to -1.5 | GAIN |
| keys evicted | 71,716 | 71,769 | +0.1% | -221 to 327 | shown, not judged |
| host CPU busy (share of the run) | 0.0509 | 0.0427 | -16.0% | -0.0529 to 0.0366 | EVEN, no difference beyond the noise |
| host CPU-seconds | 35.7 | 29.6 | -17.1% | -39 to 26.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.185 | 0.153 | -17.1% | -0.202 to 0.139 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,307 | +3.2% | 31.4 to 48.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -6.77e-05 to 0.00152 | EVEN, the same |
| cache hit rate | 0.845 | 0.872 | +3.2% | 0.0209 to 0.0324 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.72 | -0.2% | -0.019 to 0.0014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.0% | -0.00821 to 0.00893 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.9 | -13.9% | -0.18 to -0.111 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.2 | +5.1% | 0.277 to 6.21 | power given |
| memory used, mean (MB) | 61.3 | 63.1 | +2.9% | -0.399 to 3.92 | EVEN, no difference beyond the noise |
| keys evicted | 103,401 | 85,872 | -17.0% | -21,107 to -13,951 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.107 | -8.0% | -0.0191 to 0.000596 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 178 | -8.6% | -34.6 to 1.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.302 | -11.3% | -0.072 to -0.00523 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 31 |  | 31 to 31 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 924 | -0.2% | -2.89 to -0.738 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0235 to 0.0222 | EVEN, the same |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00211 to -0.000128 | LOSS |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0231 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | +0.1% | -0.0192 to 0.0282 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.28 | +0.2% | -0.0143 to 0.0242 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.3% | 0.301 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 60.7 | -0.1% | -0.74 to 0.631 | EVEN, no difference beyond the noise |
| keys evicted | 243,157 | 245,027 | +0.8% | -2,955 to 6,695 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.14 | +0.1% | -0.0223 to 0.0227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 234 | +0.3% | -40.6 to 42.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.56 | 0.563 | +0.5% | -0.0971 to 0.103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 15.5 to 29.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 58.7 to 81.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00699 to 0.00736 | EVEN, the same |
| cache hit rate | 0.789 | 0.836 | +5.9% | 0.0392 to 0.0545 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.62 | -0.2% | -0.0824 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.0491 to 0.0541 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.02 | -19.7% | -0.265 to -0.236 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 88.3 | +37.9% | 16.6 to 31.9 | power given |
| memory used, mean (MB) | 61.2 | 79.6 | +30.0% | 15.7 to 21 | power given |
| keys evicted | 138,110 | 107,076 | -22.5% | -37,321 to -24,749 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.11 | +10.1% | -0.0201 to 0.0403 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 196 | +11.8% | -37.6 to 79 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.328 | 0.346 | +5.5% | -0.0849 to 0.121 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 58.3 |  | 53.2 to 63.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
