# The Kafka consumer group in our own model, closed loop

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S (our own model, never a benchmark result). The standing wire is `tools/run_kafka.py` at `29370eec0b`; the objective resource; seeds 201 to 208, every arm on the same seeds; notches of 20 s. Built by `tools/kafka_model.py` from the omni-v21 runs' own files (see its header).

## burst

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 346.2 | 346.2 | 403.4 | STEADY, under the floor (0.00%), +0.0% | GAIN, +16.5% | GAIN, +16.5% |
| end-to-end latency, 95th percentile (ms) | 1,764.5 | 1,764.5 | 645.8 | STEADY, under the floor (0.00%), +0.0% | GAIN, -63.4% | GAIN, -63.4% |
| end-to-end latency, 99th percentile (ms) | 2,183.3 | 2,183.3 | 1,583.3 | STEADY, under the floor (0.00%), +0.0% | GAIN (inside the seeds spread), -27.5% | GAIN (inside the seeds spread), -27.5% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 298.1 | 298.1 | 120.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, -59.6% | GAIN, -59.6% |
| consumer lag, most messages waiting at once | 1,100.0 | 1,100.0 | 1,437.5 | STEADY, under the floor (0.00%), +0.0% | LOSS (inside the seeds spread), +30.6% | LOSS (inside the seeds spread), +30.6% |
| consumer lag, mean messages waiting | 97.6 | 97.6 | 26.9 | STEADY, under the floor (0.00%), +0.0% | GAIN, -72.5% | GAIN, -72.5% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.4 | STEADY, under the floor (0.00%), +0.0% | power given, +69.1% | power given, +69.1% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 1.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 15.5 | 15.5 | 1.4

## light

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 730.3 | 730.3 | 836.6 | STEADY, under the floor (0.00%), +0.0% | GAIN, +14.6% | GAIN, +14.6% |
| end-to-end latency, 95th percentile (ms) | 1,669.8 | 1,669.8 | 51.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -96.9% | GAIN, -96.9% |
| end-to-end latency, 99th percentile (ms) | 2,132.3 | 2,132.3 | 1,001.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -53.0% | GAIN, -53.0% |
| end-to-end latency, median (ms) | 51.0 | 51.0 | 51.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 249.7 | 249.7 | 75.7 | STEADY, under the floor (0.00%), +0.0% | GAIN, -69.7% | GAIN, -69.7% |
| consumer lag, most messages waiting at once | 2,150.1 | 2,150.1 | 2,054.5 | STEADY, under the floor (0.00%), +0.0% | GAIN (inside the seeds spread), -4.4% | GAIN (inside the seeds spread), -4.4% |
| consumer lag, mean messages waiting | 164.9 | 164.9 | 20.2 | STEADY, under the floor (0.00%), +0.0% | GAIN, -87.7% | GAIN, -87.7% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.1 | STEADY, under the floor (0.00%), +0.0% | power given, +53.1% | power given, +53.1% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 33.1 | 33.1 | 3.8

## heavy

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 148.0 | 142.0 | 169.1 | LOSS, -4.1% | GAIN, +14.2% | GAIN, +19.1% |
| end-to-end latency, 95th percentile (ms) | 1,580.0 | 1,823.8 | 55.0 | LOSS, +15.4% | GAIN, -96.5% | GAIN, -97.0% |
| end-to-end latency, 99th percentile (ms) | 2,036.3 | 2,936.3 | 998.8 | LOSS, +44.0% | GAIN, -50.9% | GAIN, -62.2% |
| end-to-end latency, median (ms) | 55.0 | 55.0 | 55.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 240.2 | 319.8 | 79.7 | LOSS, +33.0% | GAIN, -66.8% | GAIN, -74.1% |
| consumer lag, most messages waiting at once | 419.1 | 727.2 | 414.5 | LOSS, +73.3% | GAIN (inside the seeds spread), -1.1% | GAIN (inside the seeds spread), -31.7% |
| consumer lag, mean messages waiting | 31.1 | 44.3 | 4.1 | LOSS, +42.5% | GAIN, -86.9% | GAIN, -90.1% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.1 | power given (inside the seeds spread), +1.3% | power given, +53.1% | power given, +51.2% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 2.0 | 3.0 | no value, +0.0% | no value, +0.0% | power given, +50.0% |
| seconds over the line, mean | 30.8 | 38.0 | 3.8

## tuning

| Gauge | native | standing | candidate | native against standing | native against candidate | standing against candidate |
|---|---:|---:|---:|---|---|---|
| work inside the response line (messages a second handled within the line) | 368.4 | 368.4 | 421.9 | STEADY, under the floor (0.00%), +0.0% | GAIN, +14.5% | GAIN, +14.5% |
| end-to-end latency, 95th percentile (ms) | 1,652.0 | 1,652.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -96.9% | GAIN, -96.9% |
| end-to-end latency, 99th percentile (ms) | 2,120.8 | 2,120.8 | 1,002.0 | STEADY, under the floor (0.00%), +0.0% | GAIN, -52.7% | GAIN, -52.7% |
| end-to-end latency, median (ms) | 52.0 | 52.0 | 52.0 | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% | STEADY, under the floor (0.00%), +0.0% |
| end-to-end latency, mean (ms) | 248.7 | 248.7 | 76.7 | STEADY, under the floor (0.00%), +0.0% | GAIN, -69.1% | GAIN, -69.1% |
| consumer lag, most messages waiting at once | 1,078.9 | 1,078.9 | 1,035.9 | STEADY, under the floor (0.00%), +0.0% | GAIN (inside the seeds spread), -4.0% | GAIN (inside the seeds spread), -4.0% |
| consumer lag, mean messages waiting | 82.4 | 82.4 | 10.2 | STEADY, under the floor (0.00%), +0.0% | GAIN, -87.6% | GAIN, -87.6% |
| consumers running, mean (the resources held) | 2.0 | 2.0 | 3.1 | STEADY, under the floor (0.00%), +0.0% | power given, +53.1% | power given, +53.1% |
| consumer changes written (each a rebalance of the whole group) | 0.0 | 0.0 | 3.0 | STEADY, the same, +0.0% | no value, +0.0% | no value, +0.0% |
| seconds over the line, mean | 32.8 | 32.8 | 3.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
