# sysbench on MySQL, a database's operator-set buffer pool: the A/B/C confirmation

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2,048] MB in chunks of 128 MB, holding the server's own mean statement latency at 40% of the 0.6 ms statement line (`docs/MYSQL_PREREGISTRATION.md`). sysbench's published OLTP workloads ask for rows from a set of tables that steps through the pool and past it, the same transactions in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Errors: any increase in any run is WORSE. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 37858501997 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| B | 37858505059 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |
| C | 37858509109 | `310cf31838e7` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 5 |

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,923 | 2,921 | -0.1% (-0.4 to +0.3) | +0.1% (-0.2 to +0.3) | +0.1% (-0.1 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 2,930 | 2,929 | -0.0% (-0.6 to +0.5) | +0.1% (-0.3 to +0.5) | +0.0% (-0.2 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 2,930 | 2,929 | -0.0% (-0.6 to +0.5) | +0.1% (-0.3 to +0.5) | +0.0% (-0.2 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.365 | 0.363 | -0.5% (-2.9 to +1.8) | +0.5% (-12.5 to +13.6) | -4.2% (-18.9 to +10.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.467 | 0.464 | -0.6% (-7.4 to +6.1) | +1.8% (-11.9 to +15.5) | -4.4% (-23.9 to +15.1) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.201 | 0.203 | +0.8% (-0.6 to +2.3) | +1.1% (-12.0 to +14.1) | -2.9% (-18.0 to +12.1) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 625.9 | +22.2% (-84.0 to +128.5) | -11.6% (-47.6 to +24.3) | +12.2% (-74.1 to +98.6) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 462.1 | 528.1 | +14.3% (-75.8 to +104.4) | -10.4% (-47.5 to +26.6) | +7.9% (-61.5 to +77.3) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 262,586 | 219,665 | -16.3% (-139.0 to +106.3) | +17.6% (-43.8 to +79.0) | -7.6% (-98.9 to +83.7) | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | -0.1% (-6.7 to +6.5) | +2.6% (-20.4 to +25.6) | -5.0% (-30.7 to +20.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 114.9 | 114.8 | -0.1% (-7.4 to +7.2) | +2.8% (-20.5 to +26.0) | -5.0% (-30.9 to +20.8) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.128 | 0.128 | -0.0% (-7.6 to +7.6) | +2.7% (-20.3 to +25.8) | -5.1% (-31.1 to +21.0) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 | +8.33 (+0.744 to +15.9) | +5.67 (+2.8 to +8.54) | +8 (+1.43 to +14.6) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 6 1 8 1 6 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291.7 | 293.2 | +0.5% (-1.9 to +2.9) | -0.5% (-2.1 to +1.0) | -0.6% (-1.7 to +0.6) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 292.4 | 293.6 | +0.4% (-1.4 to +2.2) | -0.5% (-2.0 to +1.0) | -0.6% (-1.6 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,679 | 4,698 | +0.4% (-1.4 to +2.2) | -0.5% (-2.0 to +1.0) | -0.6% (-1.6 to +0.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.32 | 3.12 | -6.3% (-19.2 to +6.6) | +0.0% (-9.0 to +9.1) | -5.3% (-5.8 to -4.7) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 4.57 | 4.44 | -2.9% (-16.3 to +10.5) | -1.2% (-6.3 to +3.9) | -8.1% (-14.5 to -1.6) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.42 | 1.36 | -4.6% (-10.8 to +1.7) | +1.7% (-0.3 to +3.7) | -0.8% (-5.6 to +4.0) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 223.7 | -56.3% (-56.9 to -55.7) | -54.9% (-59.8 to -50.0) | -48.9% (-72.6 to -25.2) | **confirmed better** |
| pages holding data, mean (MB) | 438.8 | 188.1 | -57.1% (-57.9 to -56.4) | -55.7% (-61.3 to -50.1) | -51.5% (-67.2 to -35.7) | **confirmed better** |
| pages read from disk into the pool (misses) | 169,531 | 301,649 | +77.9% (+75.7 to +80.1) | +76.0% (+53.4 to +98.7) | +63.1% (+33.7 to +92.6) | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0992 | -1.1% (-11.7 to +9.5) | +1.5% (+0.2 to +2.9) | +0.3% (-4.9 to +5.4) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 40.4 | 40.0 | -1.0% (-12.0 to +10.0) | +1.6% (+0.3 to +2.9) | +0.2% (-5.2 to +5.5) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.33 | -1.6% (-10.3 to +7.1) | +2.1% (+1.5 to +2.7) | +0.8% (-4.3 to +5.9) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 3 | +3 (+3 to +3) | +3.67 (+0.798 to +6.54) | +4.33 (+1.46 to +7.2) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered; the transaction line 8.4 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293.8 | 291.9 | -0.6% (-2.3 to +1.1) | -0.2% (-0.6 to +0.1) | +0.3% (-0.7 to +1.4) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 293.8 | 292.1 | -0.6% (-2.3 to +1.1) | -0.2% (-0.6 to +0.1) | +0.3% (-0.7 to +1.4) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 4,701 | 4,674 | -0.6% (-2.3 to +1.1) | -0.2% (-0.6 to +0.1) | +0.3% (-0.7 to +1.4) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 3.66 | 3.59 | -1.8% (-1.9 to -1.7) | -0.6% (-3.3 to +2.0) | -2.4% (-4.8 to +0.1) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 4.85 | 4.82 | -0.6% (-7.5 to +6.2) | -1.2% (-3.8 to +1.4) | -1.2% (-3.8 to +1.4) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.75 | 2.73 | -0.7% (-2.4 to +1.0) | -0.6% (-3.6 to +2.3) | -0.9% (-2.7 to +0.9) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 517.1 | +1.0% (-77.2 to +79.2) | -24.7% (-96.3 to +46.8) | +0.8% (-36.2 to +37.8) | no difference beyond the noise (3 of 3 runs) |
| pages holding data, mean (MB) | 461.8 | 464.3 | +0.5% (-72.9 to +74.0) | -26.9% (-89.7 to +35.8) | -0.7% (-34.4 to +33.0) | no difference beyond the noise (3 of 3 runs) |
| pages read from disk into the pool (misses) | 456,915 | 531,776 | +16.4% (-112.8 to +145.6) | +74.8% (-32.9 to +182.4) | +13.0% (-38.2 to +64.2) | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.219 | -1.2% (-1.4 to -1.0) | -0.6% (-3.8 to +2.6) | +0.1% (-4.5 to +4.7) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 265.7 | 262.5 | -1.2% (-1.4 to -1.0) | -0.6% (-3.9 to +2.6) | +0.2% (-4.7 to +5.1) | no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.93 | -0.6% (-2.4 to +1.3) | -0.4% (-3.3 to +2.6) | -0.1% (-4.4 to +4.2) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 | +13.7 (-0.89 to +28.2) | +8 (-4.42 to +20.4) | +15 (+10.7 to +19.3) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered; the transaction line 10.8 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188.1 | 191.7 | +1.9% (+0.1 to +3.6) | -4.3% (-20.6 to +12.0) | +1.8% (-61.7 to +65.2) | no difference beyond the noise (2 of 3 runs) |
| throughput (transactions a second) | 193.9 | 194.5 | +0.4% (-1.3 to +2.1) | +0.6% (-1.4 to +2.6) | +0.6% (-0.9 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 3,877 | 3,891 | +0.4% (-1.3 to +2.1) | +0.6% (-1.4 to +2.6) | +0.6% (-0.9 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 9.22 | 8.04 | -12.9% (-25.3 to -0.5) | -23.8% (-77.3 to +29.7) | +1.7% (-144.0 to +147.5) | no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 14.4 | 12.0 | -16.4% (-44.3 to +11.5) | -39.8% (-96.3 to +16.6) | +23.1% (-101.6 to +147.9) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 5.83 | 5.26 | -9.7% (-24.0 to +4.6) | -19.0% (-53.8 to +15.8) | +11.0% (-159.8 to +181.8) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 814.2 | +59.0% (+37.4 to +80.6) | +62.3% (+42.9 to +81.6) | +62.6% (-2.2 to +127.4) | no difference beyond the noise (1 of 3 runs) |
| pages holding data, mean (MB) | 460.6 | 698.8 | +51.7% (+34.3 to +69.1) | +46.8% (+12.8 to +80.8) | +43.7% (+18.6 to +68.9) | **confirmed WORSE** |
| pages read from disk into the pool (misses) | 430,621 | 200,534 | -53.4% (-64.7 to -42.2) | -44.0% (-89.6 to +1.6) | -39.8% (-68.6 to -10.9) | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.202 | -5.6% (-7.0 to -4.3) | -4.6% (-7.9 to -1.2) | -4.1% (-7.7 to -0.4) | **confirmed better** |
| host CPU-seconds | 231.2 | 218.0 | -5.7% (-7.2 to -4.2) | -4.5% (-7.4 to -1.7) | -4.2% (-7.0 to -1.3) | **confirmed better** |
| host CPU-seconds per 1,000 transactions inside the line | 3.99 | 3.7 | -7.4% (-10.0 to -4.8) | -0.0% (-13.8 to +13.7) | -3.9% (-57.9 to +50.0) | no difference beyond the noise (2 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 22.3 | +22.3 (+17.2 to +27.5) | +21.7 (+16.5 to +26.8) | +19.7 (+15.9 to +23.5) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered; the transaction line 0.6 ms, 3 paired repetitions a run

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; 6 tables of 1,000,000 rows, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s; the operator's pool 512 MB, the cover 128 to 2,048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.73 | 1.53 | -11.6% (-96.9 to +73.8) | -100.0% (-530.3 to +330.3) | +6.4% (-114.3 to +127.1) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 974.6 | 974.9 | +0.0% (-0.6 to +0.6) | -0.1% (-0.8 to +0.6) | -1.2% (-18.4 to +15.9) | no difference beyond the noise (3 of 3 runs) |
| queries a second | 974.6 | 974.9 | +0.0% (-0.6 to +0.6) | -0.1% (-0.8 to +0.6) | -1.2% (-18.4 to +15.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 1.89 | 1.92 | +1.6% (-10.5 to +13.7) | +0.4% (-18.3 to +19.0) | -0.4% (-280.6 to +279.9) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 4.55 | 5.29 | +16.1% (+0.6 to +31.6) | +5.2% (-38.8 to +49.2) | +5.5% (-234.7 to +245.7) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 1.18 | 1.2 | +2.0% (-3.5 to +7.4) | +3.3% (-26.0 to +32.7) | -14.8% (-195.3 to +165.7) | no difference beyond the noise (3 of 3 runs) |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| buffer pool held, mean (MB; the knob, the resource) | 512.0 | 577.0 | +12.7% (+2.7 to +22.7) | -4.3% (-6.2 to -2.5) | -11.7% (-69.6 to +46.3) | **the runs disagree** |
| pages holding data, mean (MB) | 449.7 | 476.0 | +5.9% (-9.3 to +21.0) | -9.1% (-15.7 to -2.5) | -19.7% (-59.9 to +20.5) | no difference beyond the noise (2 of 3 runs) |
| pages read from disk into the pool (misses) | 138,999 | 142,763 | +2.7% (-8.8 to +14.2) | +18.1% (+7.3 to +28.8) | +28.7% (-31.5 to +88.9) | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.147 | -1.0% (-22.1 to +20.1) | -1.2% (-16.0 to +13.6) | -1.9% (-25.5 to +21.7) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 153.1 | 151.8 | -0.9% (-21.6 to +19.9) | -1.2% (-16.0 to +13.6) | -1.3% (-23.8 to +21.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 324.6 | 349.0 | +7.5% (-71.1 to +86.2) | -1.2% (-16.0 to +13.6) | -5.8% (-88.4 to +76.8) | no difference beyond the noise (3 of 3 runs) |
| buffer pool size changes written (the knob's moves) | 0 | 22.7 | +22.7 (+19.8 to +25.5) | +17.7 (+16.2 to +19.1) | +16.3 (-0.208 to +32.9) | shown, not judged |

The buffer pool handed back to the operator's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 4 gauge-rows confirmed better, 1 confirmed worse, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
