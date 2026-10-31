# The store gate: the data stores' wires, standing against candidate, on their own archived seconds

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class S, our own model: every omni arm's archived audit seconds (the V16 three-run tables' runs), replayed decision by decision through the standing wires (the runners at `0364382a54`) and the candidates (this checkout), each with its own verdict fed the recorded cost samples and its own knob. Open-loop: the inputs are those the standing wire's knob produced, so the gate says what each wire decides on the same seconds, never what a store would then have done. Each arm is one pair; the reading is the mean change over the arms, its 95% interval and the word by the gauge's aim (`tools/model_gate.py` `reading`, `tools/readings.py`). A reading here shows whether a change shows promise before a real run; it is never a benchmark result.

## pgbench: 26 omni arms

Runs (branch `raw`, `run-<id>/`): A 39842347137, B 39851575564, C 39860251731; each workload's three repetitions a run.

The candidate waits thirty seconds after adding a server before it gives one back (five before): fewer give-backs that the next seconds undo, each a server closed and a new one opened.

The standing wire's replay reproduces its own recorded knob in 97.4% of the seconds (the lowest arm 32.2%). Not read, the standing replay reproducing under 95% of its own record: select run C rep-3 (32.2%) (at the second it leaves its record, a verdict step reads the other way on the recorded seconds, which the audit rounds: t to 0.01 s, the cost to 1e-9).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 19.13 | 19.21 | =0.4% STEADY |
| writes (the knob's moves) | 31.12 | 24.58 | +21.0% GAIN |
| seconds below native | 242.42 | 217.85 | shown |
| seconds below native while short (waiting, missing, lagging) | 19.31 | 16.85 | +12.7% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| select | 8 | 18.1 → 18.3: +0.8% power given | 31.1 → 21.1: +32.1% GAIN | 344.5 → 304.0: shown | 20.9 → 16.6: +20.4% GAIN |
| simple_update | 9 | 19.7 → 19.8: =0.3% STEADY | 36.2 → 31.0: +14.4% GAIN | 188.7 → 171.1: shown | 21.8 → 20.7: +5.1% GAIN, inside the arms' noise |
| tpcb_hot | 9 | 19.4 → 19.4: =0.2% STEADY | 26.0 → 21.2: +18.4% GAIN | 205.4 → 188.0: shown | 15.4 → 13.2: +14.4% GAIN |

## kafka: 27 omni arms

Runs (branch `raw`, `run-<id>/`): A 39821402572, B 39840024618, C 39860244280; each workload's three repetitions a run.

The candidate starts no give-back trial on the seconds before the producer starts, when nothing was consumed (the standing wire's trial gave a consumer back at 8 s and failed up at 11 s in every arm: two rebalances), and hands a consumer above the operator's count back once the service is calm with no more waiting than one poll round, thirty seconds after the change (the standing wire's idle test and empty backlog never held: the third consumer stayed to the end of the arm).

The standing wire's replay reproduces its own recorded knob in 100.0% of the seconds (the lowest arm 100.0%).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 2.02 | 2.00 | +0.6% GAIN, inside the arms' noise |
| writes (the knob's moves) | 2.07 | 0.15 | +92.9% GAIN |
| seconds below native | 3.00 | 0.00 | shown |
| seconds below native while short (waiting, missing, lagging) | 0.89 | 0.00 | +100.0% GAIN |
| seconds above native, calm with nothing waiting | 12.52 | 2.11 | +83.1% GAIN, inside the arms' noise |
| writes in the first 15 s (rebalances) | 2.00 | 0.00 | +100.0% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) | seconds above native, calm with nothing waiting | writes in the first 15 s (rebalances) |
|---|---:|---|---|---|---|---|---|
| burst | 9 | 2.0 → 2.0: +0.8% power given | 2.0 → 0.0: +100.0% GAIN | 3.0 → 0.0: shown | 0.8 → 0.0: +100.0% GAIN | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 2.0 → 0.0: +100.0% GAIN |
| heavy | 9 | 2.0 → 2.0: =0.3% STEADY | 2.0 → 0.0: +100.0% GAIN | 3.0 → 0.0: shown | 0.9 → 0.0: +100.0% GAIN | 0.0 → 0.0: =0.00 a arm STEADY (identical) (the standing wire's mean is 0) | 2.0 → 0.0: +100.0% GAIN |
| light | 9 | 2.1 → 2.0: +3.0% GAIN, inside the arms' noise | 2.2 → 0.4: +80.0% GAIN | 3.0 → 0.0: shown | 1.0 → 0.0: +100.0% GAIN | 37.6 → 6.3: +83.1% GAIN, inside the arms' noise | 2.0 → 0.0: +100.0% GAIN |

## ycsb: 36 omni arms

Runs (branch `raw`, `run-<id>/`): A 39823811507, B 39842363997, C 39862241743; each workload's three repetitions a run.

The candidate holds more cache. Below native it hands a notch back each second while the cache misses 1% or more (the seconds below native while short fall), and its full (WiredTiger's own 80%, or evicting) opens the grow path on seconds that were slow, missing and evicting, which the standing wire read as 'slow with room to spare' at 90%: spend trials above native, power given, allowed by the verdict on the recorded cost samples, which in an open-loop replay never show what the larger cache would have bought. The writes rise with the hand-backs and the spends: wear, power given.

The standing wire's replay reproduces its own recorded knob in 100.0% of the seconds (the lowest arm 99.3%).

| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |
|---|---:|---:|---|
| setting, mean (the knob held) | 502.79 | 528.79 | +5.2% power given |
| writes (the knob's moves) | 3.56 | 6.28 | +76.6% power given |
| seconds below native | 54.44 | 19.78 | shown |
| seconds below native while short (waiting, missing, lagging) | 38.86 | 2.19 | +94.4% GAIN |

By workload:

| Workload | Arms | setting, mean (the knob held) | writes (the knob's moves) | seconds below native | seconds below native while short (waiting, missing, lagging) |
|---|---:|---|---|---|---|
| b | 9 | 507.3 → 522.8: +3.1% power given, inside the arms' noise | 2.7 → 3.6: +33.3% power given | 33.1 → 13.2: shown | 20.0 → 1.4: +92.8% GAIN |
| burst | 9 | 501.9 → 514.6: +2.5% power given | 4.2 → 8.2: +94.7% power given | 29.1 → 21.0: shown | 11.9 → 3.2: +72.9% GAIN |
| c | 9 | 494.5 → 529.0: +7.0% power given | 3.3 → 5.4: +63.3% power given | 122.4 → 18.8: shown | 106.3 → 2.0: +98.1% GAIN, inside the arms' noise |
| f | 9 | 507.4 → 548.8: +8.2% power given | 4.0 → 7.9: +97.2% power given | 33.1 → 26.1: shown | 17.2 → 2.1: +87.7% GAIN |

## sysbench: the reading itself

The candidate reads sysbench's own statements (its account, its prepared statements counted); the standing reading counted the four plain statement names for every account. The archived seconds hold only the standing reading's counter, so the candidate's decisions on its own reading cannot be replayed from these files: a short real run's files are the model's input for them. Both counters where the raw files hold them (the statements the standing reading counted were the harness's own monitoring SELECTs, so of the workload it saw none):

| Workload | Arms | Statements a second the standing reading counted (the harness's own SELECTs) | Statements a second sysbench sent (reads and writes: what the candidate counts) | The standing count as a share of the workload's |
|---|---:|---:|---:|---:|
| read_only | 9 | 4.2 | 4,198 | 0.10% |
| read_write | 9 | 4.1 | 3,599 | 0.11% |
| update_index | 9 | 4.1 | 999 | 0.41% |
| burst | 9 | 4.1 | 4,180 | 0.10% |

## Redis: the rule unchanged

The ceiling's rule is the same in both wires: on 9,728 archived seconds the two decide differently in 0. The CPU apart (redis-server, the application, the brain, the sampler) is a new gauge, read only by runs that record it.

## The gate's verdict

No LOSS: no judged gauge (time below native while short) rose on any wire or workload.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
