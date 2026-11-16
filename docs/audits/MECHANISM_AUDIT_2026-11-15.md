# The mechanism before the lock: every order, its code, its proof, and what is open (15 November 2026)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

The founder's question of 15 November: "is the mechanism right? Is OmniCompass tuned ... so that we can lock it all and run it all
one way through, all on top of native." Native by itself is on record; what is read here is Omni-Compass on top of native. The
answer, from the records below: **not yet**. The candidate omni-v27 carries every order of 14 and 15 November and reads, in our
own models, pods waiting below native's at every beat; on omni-v26, the engine that stood until omni-v27 landed the same day, the real tables still hold 231 rows
that read LOSS against native, and omni-v27 has not yet run on real machines. The lock comes after omni-v27's runs on GitHub's
own machines read the ledger again, every remaining LOSS row root-caused, and only then the clouds and the chips.

## 1. The orders of 14 and 15 November, each against the code

| Order (the founder's words) | Where it is in the code | Its proof | State |
|---|---|---|---|
| Pods waiting may never be worse than native; "if it's worse, then it's supposed to result to native" | `omni_controller/controller.py`: `_replica_room` (R1, place before asking), `_withdraw_waiting` (R2, R3), called by the decision and by the fast check | `tests/test_place_before_asking.py`; the model gate, section 3 | built in omni-v27, gated in our models, not run on real machines |
| "If it's scaling up, it should be looking forward 3 steps", not by the history | `LOOK_AHEAD_BEATS`, `_slope`, `_horizon_s`; omni-v19's largest-rise-ever memory removed | `tests/test_place_before_asking.py` (ahead) | built in omni-v27 |
| Locked into the cloud's own rules | the machine lever opens and parks machines that exist (`scripts/kind_nodepool.sh`), never past the pool; a new machine is the cloud autoscaler's, for a pod that waits; the look-ahead never nearer than a machine's delivery, measured from the governor's own orders (`_delivered`) | the cloud model plays by the same rule (`tools/model_gate.py`, `CloudSim`) | built; see section 2 for what the cloud's law means |
| What Omni-Compass cannot make better stays native | R3 (native's own count while pods wait); the immune hand-back (omni-v19, omni-v21); the card governor writes nothing where the card already stands at its top on native | the model gate; the A100 tables (every gauge STEADY, no write) | in place |
| One whole new version with all of it, in one shot | omni-v27 = place before asking + the forward look + the stand-ins + the conveyance owed (held on `v27-convey-study` since 7 November) + the C++ twin of the look-ahead | `docs/OMNI_V27.md`; `results/model_gate/V27_VS_V26.md` | landed on 15 November |
| One full final benchmark, every receipt through one engine | `tools/the_benchmark.py` → `results/THE_BENCHMARK.md`: every scenario on the engine that stands, its receipt, its state, and every paid scenario waiting with its switch | `tests/test_the_benchmark.py`; verify checks it on every push | built |
| No chip and no cloud until the mechanism is right | `scripts/azure_queue.txt`, `amazon_queue.txt`, `google_queue.txt`: `switch=off` | on main since 15 November (commit `adfc923b1d2`) | done |
| The small chip runs on Amazon: one card at 1, 10 and 100 copies; the eight-card machine not now | `.github/workflows/aws-gpu.yml`, `scripts/aws_gpu.sh` | `tests/test_archive_sweep.py`, the legal and workflow checks | wired, not pushed; held by the order above |
| Every chip its own benchmark, and all combined | `tools/chips_board.py` → `results/CHIPS_BOARD.md` | `tests/test_chips_board.py` | built, not pushed |
| Every engine version recorded as a benchmark | `tools/engine_ladder.py` → `results/ENGINE_LADDER.md` | `tests/test_engine_ladder.py` | built, not pushed |
| Every organism three ways, the jump generator and Monte Carlo wired in | `scripts/reruns.txt`: "kubernetes by itself", the 1,107 muscles and seven organisms, the orchestra, Omni-Compass's own orchestrator's three arms, the core's Monte Carlo; `engine-runs.yml` every night | `tests/test_release_campaign.py` | the orchestra, the orchestrator and Monte Carlo added, not pushed |
| The website in line with the record | `docs/WEBSITE_CLAIMS.md` (the site's lines of 14 November, each against the record); `results/SITE_NUMBERS.json` (the cloud's arms C and D from the newest Azure table, its work per dollar) | `tools/claims_check.py`; `tests/test_site_numbers.py` | written; the site's own builder applies it |
| The beat | omni-v24's factory beat per place: 10 s on site, 60 s through a cloud | `results/model_gate/V24_VS_V23.md` | unchanged |

## 2. The cloud's law, and what it means for every rule above

In every cloud this repository runs (Azure's AKS; Google's GKE and Amazon's EKS wired the same way), Omni-Compass's machine
lever opens and parks machines that already exist; it never makes one. A new machine is made by the cloud's own autoscaler, and
that autoscaler makes one only for a pod that is waiting. So in a cloud, **asking for a machine is making a pod wait**:

- omni-v26 let the pods its lower target asked for wait, so the cloud made machines for them: faster, a larger bill, and pods
  waiting three to four times native's (the Azure work meter, `results/live/V26_AKS_WORK_METER.md`: work per dollar GAIN in all
  three of our runs, pods with no machine LOSS in all three).
- omni-v27 never lets a pod it asked for wait: it asks only where a machine in service can place the pod, and withdraws its own
  waiting pods to native's count at once. The cloud then makes no machine for Omni-Compass's pods; the bill does not rise for
  them, and the speed Omni-Compass adds is the room on the machines that exist.

The one mechanism that lets Omni-Compass have a machine made ahead of the demand without a real pod waiting is the one
Kubernetes itself provides for it: a placeholder of the lowest priority, sized for the demand looked ahead, which the cloud's
autoscaler makes a machine for and which any real pod displaces at once. Built the same day, on the founder's words ("What makes
the thing stronger? We don't want to make pods scale up when we can't give it to them"): the stand-ins (`docs/OMNI_V27.md`,
section 4; `deploy/kind/omni-headroom.yaml`; `tests/test_standins.py`), through a cloud only, at the max, sized for the rise held at
every one of the last three beats and the pods held back beyond the free and parked room. A first form that projected the
least-squares line through the last three beats read, in the cloud model, pods waiting near none and the alert minutes down, for
22% to 86% more machine-hours than omni-v26: a single jump in the load was projected again as a climb, and the cloud made machines
the demand never used. It was replaced before the gate by the rise held at every beat, which asks nothing for a jump already taken
or a reading's wobble.

## 3. What omni-v27 reads in our own models (class S, never proof)

`results/model_gate/V27_VS_V26.md`, seeds 1 to 8, twelve models. Each change is the mean over the seeds against the arm named.

| Model | Pods waiting against native | against omni-v26 | 95th percentile against native | against omni-v26 | Alert minutes against native | against omni-v26 |
|---|---|---|---|---|---|---|
| the cloud, a decision every 60 s (its factory beat) | GAIN, down 9.2% | GAIN, down 19.5% | GAIN, down 6.2% | LOSS, up 2.6% | GAIN, down 21.6% | LOSS, up 1.2% |
| the cloud, every 15 s | GAIN, down 20.8% | GAIN, down 50.0% | GAIN, down 20.5% | LOSS, up 7.2% | GAIN, down 70.0% | LOSS, up 60.0% |
| the cloud, machines blinking out | GAIN, down 9.5% | GAIN, down 19.8% | GAIN, down 5.0% | LOSS, up 3.8% | GAIN, down 17.4% | LOSS, up 6.7% |
| on site, every 10 s (its factory beat) | STEADY (none waits in either) | STEADY | GAIN, down 29.3% | LOSS, up 0.6% | GAIN, down 86.0% | LOSS, up 36.4% |

The machines read the same as omni-v26's or fewer (down 0.2% to 3.5% in the cloud; identical on site). The autoscaler's scale-up
time reads LOSS against native in the cloud at 60 s (up 1.1%, about two seconds an hour) and at 15 s STEADY: the pods now come as
the machines land, in steps. The conveyance, the card and the verdict models read omni-v26's numbers. Against omni-v26 the speed
and alert rows read LOSS: omni-v26's reserve, the largest rise ever seen held from then on, kept room for the model's repeating
load steps; the forward look holds none while the demand is flat, and meets a step as native does. By the rule of 15 October a
version lands only with no LOSS against the engine that stands; this one lands only on the founder's word.

## 4. The real record on the engine that stands, and what omni-v27 answers

`docs/LOSS_LEDGER.md`: on omni-v26, 231 rows read LOSS against native, in 43 tables; 168 carry their cause, 63 do not.

| Cause, as the ledger writes it | Rows | What answers it |
|---|---:|---|
| the conveyance's cycle on the shared host (a raise, then a hand-back, then a raise), with the web target's remaining writes and the governor's own processor at the 10 s beat | 146 | omni-v27's conveyance owed (steps sized to the band, half given back at a time, no raise into processor another workload is owed): Koordinator's replay, the cycle down 60.6% (`results/model_gate/V27_KOORD_CONVEY.md`, class S) |
| the web target's remaining writes, measured beside the row | 21 | omni-v26's hold; not yet to none |
| the governor's own processor at 10 s | 1 | not answered: the beat's own cost |
| not yet written | 63 | among them the Azure burst set (`V26_AKS_FULL_BURST`: pods with no machine and the response times), the data stores' work rows (sysbench as shipped, YCSB, pgbench) and pods waiting on several rigs; omni-v27's pod rules answer the pods waiting; the data stores' rows are their own wires' |

## 5. The verdict, and the road to the lock

**Not ready to lock.** What is right: every order of 14 and 15 November is in the code of omni-v27, with its test, and the models
read pods waiting below native's at every beat. What is open:

1. omni-v27 lands with the stand-ins (the founder's words of 15 November: decide by what makes the mechanism stronger, never a
   pod scaled up that cannot be given a machine); its model gate against omni-v26 is in `results/model_gate/V27_VS_V26.md`;
2. omni-v27's own runs on GitHub's free machines (every Kubernetes rig, the seven organisms three ways, the data stores), read by
   the one key, every LOSS row against native root-caused, before anything is locked;
3. the 63 rows without a cause, each read from its runs' own files;
4. the scale-up time against native (up 1.1% in the cloud model at 60 s);
5. the cloud: the stand-ins (section 2) read on real machines, in the clouds' own runs, on the founder's word;
6. then the clouds and the chips, each on the founder's word, with its price and its cap.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
