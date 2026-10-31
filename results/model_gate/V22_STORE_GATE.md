# The store gate: the data stores' wires, standing against candidate, on their own archived seconds

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S, our own model: every omni arm's archived audit seconds (the V21 three-run tables' runs), replayed decision by decision through the standing wires (the runners at `29370eec0b`) and the candidates (this checkout), each with its own verdict fed the recorded cost samples and its own knob. Open-loop: the inputs are those the standing wire's knob produced, so the gate says what each wire decides on the same seconds, never what a store would then have done. Each arm is one pair; the reading is the mean change over the arms, its 95% interval and the word by the gauge's aim (`tools/model_gate.py` `reading`, `tools/readings.py`). A reading here shows whether a change shows promise before a real run; it is never a benchmark result.

## pgbench: 26 omni arms

Runs (branch `raw`, `run-<id>/`): A 40258014810, B 40281459100, C 40400963499; each workload's three repetitions a run.

omni-v22, the max: a server added while clients wait is never clamped by an allowance, and the pool is never taken below the pooler's own setting (the standing wire's calm give-back took it below, inside the allowance, and the queue line added the servers back when the load rose): the seconds below native fall to none, the servers held rise, power given.

The standing wire's replay reproduces its own recorded knob in 99.0% of the seconds (the lowest arm 75.1%). Not read, the standing replay reproducing under 95% of its own record: simple_update run B rep-3 (75.1%) (at the second it leaves its record, a verdict step reads the other way on the recorded seconds, which the audit rounds: t to 0.01 s, the cost to 1e-9).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 19.27 | 24.70 | +28.2% power given |
| writes (the knob's moves) | 18.42 | 23.73 | +28.8% power given, inside the arms' noise |
| seconds below native | 223.46 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 7.54 | 0.00 | +100.0% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| select | 9 | 18.9 → 20.0: +5.8% power given | 13.9 → 0.0: +100.0% GAIN | 275.6 → 0.0: shown | 4.0 → 0.0: +100.0% GAIN |
| simple_update | 8 | 19.8 → 31.2: +58.0% power given | 24.5 → 54.1: +120.9% power given | 155.2 → 0.0: shown | 11.9 → 0.0: +100.0% GAIN |
| tpcb_hot | 9 | 19.2 → 23.6: +23.1% power given, inside the arms' noise | 17.6 → 20.4: +16.5% power given, inside the arms' noise | 232.0 → 0.0: shown | 7.2 → 0.0: +100.0% GAIN |

## kafka: 27 omni arms

Runs (branch `raw`, `run-<id>/`): A 40256717947, B 40279909158, C 40400868003; each workload's three repetitions a run.

omni-v22, the max: the group's twin (each partition's arrivals placed on the members by the range assignor) and the reflex, never clamped by an allowance, with a hold that hands a consumer back only to a count that carries the last minute's peak. omni-v21's audits carry no arrivals, so in this replay the twin reads none and the reflex adds consumers from the compass's own wanting; the closed-loop model, which carries them, shows the twin at work (tools/kafka_model.py).

The standing wire's replay reproduces its own recorded knob in 100.0% of the seconds (the lowest arm 99.3%).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 2.10 | 4.85 | +130.6% power given |
| writes (the knob's moves) | 2.37 | 6.00 | +153.1% power given |
| seconds below native | 0.00 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 0.00 | 0.00 | =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |
| seconds above native, calm with nothing waiting | 31.44 | 120.33 | +282.7% power given |
| writes in the first 15 s (rebalances) | 0.00 | 0.00 | =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) | seconds above native, calm with nothing waiting | writes in the first 15 s (rebalances) |
|---|---:|---|---|---|---|---|---|
| burst | 9 | 2.0 → 4.5: +126.3% power given | 0.0 → 6.0: +6.00 a arm power given (the standing wire's mean is 0) | 0.0 → 0.0: shown | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 0.0 → 49.7: +49.67 a arm power given (the standing wire's mean is 0) | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |
| heavy | 9 | 2.1 → 5.0: +138.6% power given | 2.4 → 6.0: +145.5% power given | 0.0 → 0.0: shown | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 32.2 → 155.8: +383.4% power given | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |
| light | 9 | 2.2 → 5.0: +126.8% power given | 4.7 → 6.0: +28.6% power given, inside the arms' noise | 0.0 → 0.0: shown | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 62.1 → 155.6: +150.4% power given | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |

## ycsb: 36 omni arms

Runs (branch `raw`, `run-<id>/`): A 40259304209, B 40281469940, C 40401042132; each workload's three repetitions a run.

omni-v22, the max: the cache never below the operator's (the seconds below native fall to none), and memory spent only where WiredTiger's own account (its time reading pages from disk for the application's threads) says the misses cost the reads and the host has a notch to spare. omni-v21's audits carry neither account, so in this replay the candidate holds at native and writes nothing: the first run on omni-v22 reads them.

The standing wire's replay reproduces its own recorded knob in 100.0% of the seconds (the lowest arm 99.7%).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 520.60 | 512.00 | +1.7% GAIN |
| writes (the knob's moves) | 5.64 | 0.00 | +100.0% GAIN |
| seconds below native | 12.50 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 2.11 | 0.00 | +100.0% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| b | 9 | 510.7 → 512.0: =0.3% STEADY | 3.3 → 0.0: +100.0% GAIN | 8.9 → 0.0: shown | 1.6 → 0.0: +100.0% GAIN |
| burst | 9 | 517.3 → 512.0: +1.0% GAIN, inside the arms' noise | 6.8 → 0.0: +100.0% GAIN | 11.4 → 0.0: shown | 2.7 → 0.0: +100.0% GAIN |
| c | 9 | 515.8 → 512.0: +0.7% GAIN, inside the arms' noise | 3.6 → 0.0: +100.0% GAIN | 14.2 → 0.0: shown | 1.4 → 0.0: +100.0% GAIN |
| f | 9 | 538.6 → 512.0: +4.9% GAIN, inside the arms' noise | 8.9 → 0.0: +100.0% GAIN | 15.4 → 0.0: shown | 2.8 → 0.0: +100.0% GAIN |

## sysbench: 33 omni arms

Runs (branch `raw`, `run-<id>/`): A 40258018856, B 40281464587, C 40401032384; each workload's three repetitions a run.

omni-v22, the max: the pool never below the operator's (the seconds below native fall to none), and memory spent only where the server's own account (the performance schema's timer on the data files' reads) says the misses cost the statements and the host has a chunk to spare. omni-v21's audits carry neither account, so in this replay the candidate holds at native and writes nothing: the first run on omni-v22 reads them; the memory the tune-down gave back is the tune-down's (dial save).

The standing wire's replay reproduces its own recorded knob in 98.0% of the seconds (the lowest arm 51.7%). Not read, the standing replay reproducing under 95% of its own record: burst run C rep-1 (85.6%); burst run C rep-3 (91.3%); read_only run A rep-2 (51.7%) (at the second it leaves its record, a verdict step reads the other way on the recorded seconds, which the audit rounds: t to 0.01 s, the cost to 1e-9).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 479.77 | 512.00 | +6.7% power given |
| writes (the knob's moves) | 7.45 | 0.00 | +100.0% GAIN |
| seconds below native | 97.85 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 65.39 | 0.00 | +100.0% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| burst | 7 | 440.1 → 512.0: +16.3% power given | 6.3 → 0.0: +100.0% GAIN | 83.3 → 0.0: shown | 30.7 → 0.0: +100.0% GAIN |
| read_only | 8 | 418.1 → 512.0: +22.5% power given | 8.6 → 0.0: +100.0% GAIN | 242.0 → 0.0: shown | 200.8 → 0.0: +100.0% GAIN |
| read_write | 9 | 533.2 → 512.0: +4.0% GAIN, inside the arms' noise | 14.8 → 0.0: +100.0% GAIN | 78.9 → 0.0: shown | 37.4 → 0.0: +100.0% GAIN |
| update_index | 9 | 512.0 → 512.0: =0.0% STEADY (identical) | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 0.0 → 0.0: shown | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |

## redis: 27 omni arms

Runs (branch `raw`, `run-<id>/`): A 40254205224, B 40276907808, C 40400989005; each workload's three repetitions a run.

omni-v22, the max: misses with the cache full go through unclamped (the standing wire's allowance refused them in 4,426 of the 4,581 seconds over the line) where the application's own split says they cost the service and the host has a notch to spare, and the ceiling is never handed back below the working set's floor nor below the operator's. omni-v21's audits carry neither the split nor the host's memory, so in this replay the candidate holds at native; the closed-loop model, which carries both, shows what the larger cache buys (tools/redis_model.py).

The standing wire's replay reproduces its own recorded knob in 100.0% of the seconds (the lowest arm 100.0%).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 64.20 | 64.00 | =0.3% STEADY |
| writes (the knob's moves) | 12.30 | 0.00 | +100.0% GAIN |
| seconds below native | 36.63 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 1.52 | 0.00 | +100.0% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| burst | 9 | 62.7 → 64.0: +2.0% power given | 4.7 → 0.0: +100.0% GAIN | 26.6 → 0.0: shown | 1.3 → 0.0: +100.0% GAIN |
| large | 9 | 64.8 → 64.0: +1.3% GAIN | 21.4 → 0.0: +100.0% GAIN | 62.2 → 0.0: shown | 3.2 → 0.0: +100.0% GAIN |
| small | 9 | 65.0 → 64.0: +1.6% GAIN | 10.8 → 0.0: +100.0% GAIN | 21.1 → 0.0: shown | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) |

## sysbench: the reading itself

The candidate reads sysbench's own statements (its account, its prepared statements counted); the standing reading counted the four plain statement names for every account. The archived seconds hold only the standing reading's counter, so the candidate's decisions on its own reading cannot be replayed from these files: a short real run's files are the model's input for them. Both counters where the raw files hold them (the statements the standing reading counted were the harness's own monitoring SELECTs, so of the workload it saw none):

| Workload | Arms | Statements a second the standing reading counted (the harness's own SELECTs) | Statements a second sysbench sent (reads and writes: what the candidate counts) | The standing count as a share of the workload's |
|---|---:|---:|---:|---:|
| read_only | 9 | 4401.7 | 4,202 | 104.76% |
| read_write | 9 | 3732.8 | 3,598 | 103.75% |
| update_index | 9 | 973.7 | 993 | 98.01% |
| burst | 9 | 4360.4 | 4,198 | 103.87% |

## Redis: the rule unchanged

The ceiling's rule is the same in both wires: on 8,658 archived seconds the two decide differently in 0. The CPU apart (redis-server, the application, the brain, the sampler) is a new gauge, read only by runs that record it.

## The gate's verdict

No LOSS: no judged gauge (time below native while short) rose on any wire or workload.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
