# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39379923601 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| B | 39410594381 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39459241206 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,932, 16,034, 39,368 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7,008 | 7,009 | 7008 → 7009; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7054 → 7054; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 1.732e+04 → 1.728e+04; raw −0.2% (95%: −1.1% to +0.7%); STEADY | STEADY, under the floor (the three runs' mean 0.06%) |
| throughput (transactions a second) | 7,008 | 7,009 | 7008 → 7009; raw ±0.0% (95%: −0.1% to +0.1%); STEADY | 7054 → 7056; raw ±0.0% (95%: −0.1% to +0.2%); STEADY | 1.732e+04 → 1.731e+04; raw ±0.0% (95%: −0.2% to +0.2%); STEADY | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 1.1 | 1.09 | 1.097 → 1.088; raw −0.9% (95%: −31.2% to +29.5%); GAIN | 0.8487 → 0.85; raw +0.2% (95%: −6.8% to +7.1%), +0.0013 in the gauge's unit; STEADY | 0.2507 → 0.2647; raw +5.6% (95%: −4.9% to +16.1%), +0.0140 in the gauge's unit; LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 2.97 | 2.59 | 2.966 → 2.589; raw −12.7% (95%: −78.6% to +53.2%); GAIN | 1.757 → 1.787; raw +1.7% (95%: −49.7% to +53.2%); LOSS | 0.4867 → 1.342; raw +175.8% (95%: −341.1% to +692.7%), +0.8557 in the gauge's unit; LOSS | **the runs disagree** |
| latency, median (ms) | 0.363 | 0.363 | 0.363 → 0.3633; raw +0.1% (95%: −3.7% to +3.9%), +0.0003 in the gauge's unit; STEADY | 0.3297 → 0.3293; raw −0.1% (95%: −1.7% to +1.5%), −0.0003 in the gauge's unit; STEADY | 0.1393 → 0.1403; raw +0.7% (95%: −1.1% to +2.5%), +0.0010 in the gauge's unit; LOSS | STEADY, under the floor (the three runs' mean 0.24%) |
| latency, mean (ms) | 0.504 | 0.496 | 0.5036 → 0.4956; raw −1.6% (95%: −19.2% to +16.1%), −0.0080 in the gauge's unit; GAIN | 0.4274 → 0.468; raw +9.5% (95%: −45.4% to +64.5%), +0.0407 in the gauge's unit; LOSS | 0.1662 → 0.404; raw +143.2% (95%: −359.8% to +646.1%), +0.2379 in the gauge's unit; LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | 19.5 → 18.08; raw −7.3% (95%: −10.5% to −4.2%); GAIN | 19.71 → 18.34; raw −7.0% (95%: −12.5% to −1.4%); GAIN | 19.89 → 18.05; raw −9.2% (95%: −21.3% to +2.8%); GAIN | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 20.0 | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | STEADY, the same |
| host CPU busy (share of the run) | 0.306 | 0.306 | 0.3057 → 0.3064; raw +0.2% (95%: −6.5% to +7.0%), +0.0007 in the gauge's unit; STEADY | 0.3721 → 0.3724; raw +0.1% (95%: −0.6% to +0.8%), +0.0003 in the gauge's unit; STEADY | 0.3365 → 0.3385; raw +0.6% (95%: −3.4% to +4.5%), +0.0019 in the gauge's unit; power given | STEADY, under the floor (the three runs' mean 0.30%) |
| host CPU-seconds | 449.9 | 451.0 | 449.9 → 451; raw +0.2% (95%: −7.7% to +8.2%); STEADY | 625.3 → 626.2; raw +0.1% (95%: −0.6% to +0.9%); STEADY | 569.7 → 573.2; raw +0.6% (95%: −3.3% to +4.5%); power given | STEADY, under the floor (the three runs' mean 0.33%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | 0.1427 → 0.143; raw +0.2% (95%: −7.6% to +8.0%), +0.0003 in the gauge's unit; STEADY | 0.197 → 0.1973; raw +0.1% (95%: −0.7% to +1.0%), +0.0003 in the gauge's unit; STEADY | 0.0731 → 0.07369; raw +0.8% (95%: −2.2% to +3.9%), +0.0006 in the gauge's unit; power given | STEADY, under the floor (the three runs' mean 0.40%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.5 | 3.22 | 2.497 → 3.222; raw +29.0% (95%: +20.3% to +37.7%) | 2.497 → 3.205; raw +28.4% (95%: +23.7% to +33.0%) | 2.964 → 3.439; raw +16.0% (95%: +11.0% to +21.0%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | 20 → 18.82; raw −5.9% (95%: −8.6% to −3.2%) | 20 → 18.82; raw −5.9% (95%: −7.9% to −3.8%) | 20 → 18.26; raw −8.7% (95%: −19.9% to +2.5%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); run B: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 18 to 20 (7 trials, 2 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,855, 3,143, 4,024 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,649 | 1,643 | 1649 → 1643; raw −0.3% (95%: −3.9% to +3.2%); STEADY | 988.2 → 1040; raw +5.2% (95%: −4.4% to +14.8%); GAIN | 1723 → 1712; raw −0.6% (95%: −5.0% to +3.7%); LOSS | **the runs disagree** |
| throughput (transactions a second) | 1,697 | 1,696 | 1697 → 1696; raw −0.1% (95%: −0.8% to +0.7%); STEADY | 1377 → 1380; raw +0.3% (95%: −1.6% to +2.2%); STEADY | 1772 → 1771; raw −0.1% (95%: −0.4% to +0.3%); STEADY | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 7.62 | 10.2 | 7.622 → 10.19; raw +33.7% (95%: −195.4% to +262.8%); LOSS | 633 → 405.9; raw −35.9% (95%: −37.8% to −34.0%); GAIN | 6.866 → 23.94; raw +248.7% (95%: −834.8% to +1332.2%); LOSS | **the runs disagree** |
| latency, 99th percentile (ms) | 203.6 | 229.2 | 203.6 → 229.2; raw +12.6% (95%: −55.0% to +80.1%); LOSS | 1293 → 1166; raw −9.9% (95%: −36.4% to +16.7%); GAIN | 195.6 → 224.8; raw +14.9% (95%: −65.6% to +95.5%); LOSS | **the runs disagree** |
| latency, median (ms) | 1.54 | 1.53 | 1.538 → 1.535; raw −0.2% (95%: −5.3% to +5.0%); STEADY | 1.201 → 1.09; raw −9.2% (95%: −29.7% to +11.3%); GAIN | 1.457 → 1.47; raw +0.9% (95%: −1.4% to +3.2%); LOSS | **the runs disagree** |
| latency, mean (ms) | 7.08 | 8.05 | 7.082 → 8.046; raw +13.6% (95%: −97.8% to +125.1%); LOSS | 104.9 → 75.71; raw −27.8% (95%: −35.4% to −20.2%); GAIN | 6.616 → 8.064; raw +21.9% (95%: −106.8% to +150.6%); LOSS | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | 20 → 19.52; raw −2.4% (95%: −5.1% to +0.2%); GAIN | 20 → 20.26; raw +1.3% (95%: −1.6% to +4.1%); power given | 20 → 19.09; raw −4.5% (95%: −8.3% to −0.7%); GAIN | **the runs disagree** |
| server connections alive, most at once | 20.0 | 21.7 | 20 → 21.67; raw +8.3% (95%: +1.2% to +15.5%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.347 | 0.347 | 0.3468 → 0.3465; raw −0.1% (95%: −6.1% to +6.0%), −0.0002 in the gauge's unit; STEADY | 0.2205 → 0.2247; raw +1.9% (95%: −5.9% to +9.7%), +0.0042 in the gauge's unit; power given | 0.4252 → 0.4285; raw +0.8% (95%: ±0.0% to +1.6%), +0.0034 in the gauge's unit; power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 521.7 | 521.5 | 521.7 → 521.5; raw ±0.0% (95%: −7.0% to +6.9%); STEADY | 387.5 → 394.4; raw +1.8% (95%: −5.9% to +9.5%); power given | 725.4 → 731.4; raw +0.8% (95%: ±0.0% to +1.7%); power given | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.703 | 0.705 | 0.7032 → 0.7054; raw +0.3% (95%: −9.1% to +9.7%), +0.0022 in the gauge's unit; STEADY | 0.8722 → 0.8452; raw −3.1% (95%: −10.1% to +3.9%), −0.0270 in the gauge's unit; GAIN | 0.9355 → 0.9496; raw +1.5% (95%: −3.6% to +6.6%), +0.0141 in the gauge's unit; power given | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.8 | 1.028 → 1.802; raw +75.3% (95%: +65.1% to +85.5%) | 0.7055 → 1.307; raw +85.2% (95%: +68.4% to +102.0%), +0.6012 in the gauge's unit | 1.042 → 1.833; raw +76.0% (95%: +73.6% to +78.3%) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | 20 → 19.71; raw −1.4% (95%: −4.1% to +1.2%) | 20 → 20.23; raw +1.2% (95%: −1.5% to +3.9%) | 20 → 19.34; raw −3.3% (95%: −7.2% to +0.5%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (13 trials, 2 allowed, 5 refused); acting: 20 to 21 (11 trials, 1 allowed, 3 refused); acting: 19 to 20 (10 trials, 1 allowed, 7 refused); run B: left native (24 trials, 0 allowed, 0 refused); acting: 20 to 21 (24 trials, 1 allowed, 0 refused); acting: 20 to 21 (21 trials, 1 allowed, 1 refused); run C: acting: 19 to 21 (14 trials, 2 allowed, 7 refused); acting: 19 to 20 (12 trials, 1 allowed, 7 refused); acting: 17 to 20 (13 trials, 3 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,519, 2,771, 1,635 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 688.7 | 655.3 | 688.7 → 655.3; raw −4.9% (95%: −34.0% to +24.3%); LOSS | 1219 → 1219; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 413.7 → 466; raw +12.6% (95%: −8.5% to +33.8%); GAIN | **the runs disagree** |
| throughput (transactions a second) | 1,061 | 1,058 | 1061 → 1058; raw −0.3% (95%: −13.0% to +12.5%); STEADY | 1219 → 1219; raw ±0.0% (95%: −0.6% to +0.7%); STEADY | 709.5 → 717.1; raw +1.1% (95%: −2.3% to +4.5%); GAIN | STEADY, under the floor (the three runs' mean 0.28%) |
| latency, 95th percentile (ms, lag included) | 3,366 | 4,090 | 3366 → 4090; raw +21.5% (95%: −173.5% to +216.5%); LOSS | 3.486 → 3.415; raw −2.0% (95%: −35.1% to +31.0%); GAIN | 1999 → 779.4; raw −61.0% (95%: −322.0% to +200.0%); GAIN | **the runs disagree** |
| latency, 99th percentile (ms) | 4,497 | 5,767 | 4497 → 5767; raw +28.2% (95%: −134.5% to +191.0%); LOSS | 9.32 → 7.879; raw −15.5% (95%: −126.7% to +95.7%); GAIN | 2917 → 1351; raw −53.7% (95%: −270.9% to +163.5%); GAIN | **the runs disagree** |
| latency, median (ms) | 4.36 | 26.6 | 4.357 → 26.59; raw +510.3% (95%: −1668.3% to +2688.8%); LOSS | 1.316 → 1.324; raw +0.6% (95%: −6.0% to +7.3%); LOSS | 20.35 → 3.155; raw −84.5% (95%: −214.2% to +45.3%); GAIN | **the runs disagree** |
| latency, mean (ms) | 620.1 | 660.7 | 620.1 → 660.7; raw +6.5% (95%: −177.3% to +190.4%); LOSS | 1.754 → 1.71; raw −2.5% (95%: −28.2% to +23.2%); GAIN | 277.2 → 131.6; raw −52.5% (95%: −246.7% to +141.7%); GAIN | **the runs disagree** |
| failed transactions | 0 | 0 | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | 0 → 0; raw ±0.0000 in the gauge's unit (95%: ±0.0000 to ±0.0000) | STEADY, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | 20 → 20.09; raw +0.5% (95%: −1.6% to +2.5%); STEADY | 19.54 → 18.13; raw −7.2% (95%: −15.4% to +0.9%); GAIN | 20 → 20.01; raw +0.1% (95%: −0.1% to +0.2%); STEADY | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | 20 → 21.33; raw +6.7% (95%: −0.5% to +13.8%); power given | 20 → 20; raw ±0.0% (95%: ±0.0% to ±0.0%); STEADY | 20 → 20.67; raw +3.3% (95%: −3.8% to +10.5%); power given | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU busy (share of the run) | 0.265 | 0.266 | 0.2646 → 0.2663; raw +0.7% (95%: −11.7% to +13.0%), +0.0017 in the gauge's unit; power given | 0.311 → 0.3124; raw +0.5% (95%: −5.1% to +6.1%), +0.0015 in the gauge's unit; STEADY | 0.1621 → 0.16; raw −1.3% (95%: −9.0% to +6.5%), −0.0021 in the gauge's unit; GAIN | **the runs disagree** |
| host CPU-seconds | 461.5 | 464.8 | 461.5 → 464.8; raw +0.7% (95%: −11.2% to +12.7%); power given | 546.4 → 548.9; raw +0.4% (95%: −5.2% to +6.1%); STEADY | 276.9 → 272.4; raw −1.6% (95%: −9.4% to +6.2%); GAIN | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.66 | 1.521 → 1.66; raw +9.1% (95%: −28.2% to +46.5%); power given | 0.9963 → 1; raw +0.4% (95%: −4.9% to +5.7%), +0.0040 in the gauge's unit; STEADY | 1.494 → 1.3; raw −13.0% (95%: −30.6% to +4.6%); GAIN | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.645 | 1.22 | 0.6448 → 1.218; raw +88.9% (95%: +72.4% to +105.4%), +0.5732 in the gauge's unit | 0.7352 → 1.283; raw +74.6% (95%: +72.9% to +76.3%), +0.5483 in the gauge's unit | 0.5761 → 1.134; raw +96.9% (95%: +89.3% to +104.5%), +0.5583 in the gauge's unit | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | 20 → 20.08; raw +0.4% (95%: −1.3% to +2.1%) | 20 → 18.6; raw −7.0% (95%: −8.7% to −5.3%) | 20 → 20.02; raw +0.1% (95%: −0.1% to +0.3%) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 20 to 21 (23 trials, 1 allowed, 1 refused); left native (22 trials, 0 allowed, 0 refused); left native (30 trials, 0 allowed, 0 refused); run B: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 14 to 20 (9 trials, 6 allowed, 3 refused); run C: left native (23 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 0 refused); left native (25 trials, 0 allowed, 0 refused).

**Across 3 workloads: 2 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 12 STEADY, 18 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
