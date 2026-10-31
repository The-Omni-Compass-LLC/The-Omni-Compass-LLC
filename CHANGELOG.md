# Changelog

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## 2026-10-31: the cloud at the max; no hard rule; the factory beat read again
- **The cloud's rule of 14 October is struck** (the founder's words of 31 October: "Why is there any hard rule written ...
  Whatever the math does and falls out is whatever happens ... when it falls out wrong, the tuning is wrong"; "make the cloud
  the best it can be with Omni-Compass in it, as well as on site"). Every cloud set runs the whole engine at the max, every
  muscle, on top of the cloud's own autoscaler, and the bill is judged beside the work by the one key, never ruled: every cloud
  workflow's dial defaults to `max` and sets no machines-only switch (`aks-metered`, `aks-metered-full`, `gke-metered`,
  `eks-metered`, `byoc-metered`), every `scripts/*_queue.txt` entry reads `dial=max` with the replica room read live, the rig
  wires the same muscles on every platform (`scripts/kind_bench.sh`, `OMNI_MACHINES_ONLY` and `GIVE_BACK_ONLY` gone), the cloud
  install file passes the max (`deploy/install/omni-compass-cloud.yaml`), the model gate's cloud setting is the max
  (`tools/model_gate.py`, `tools/orchestrators_arm.py`, `tools/heartbeat_sweep.py`), and `tests/test_cloud_at_the_max.py`
  holds it (the machines-only test removed). The governor's `--give-back-only` flag, an engine file, leaves with the
  next version. Preregistered before any set at the max: `docs/K8S_COMPASS_PREREGISTRATION.md` (the amendment of 31 October),
  `docs/PACE_PREREGISTRATION.md` (amendment 5), `docs/WHOLE_SYSTEM_PREREGISTRATION.md`. The sets that ran under the struck rule
  (omni-v18's and omni-v21's Azure steady sets) stand as the tune-down's record.
- **The factory beat is read again on the engine that stands** (`docs/PACE_PREREGISTRATION.md`, amendment 4, the pick rule
  written before the run): on omni-v17's ladder 10 s read strongest on the service against 60 s (the kind setting: the minutes
  over the line down 18.4%, pods waiting down 9.9%, machine-hours down 1.4%; 20 s: 14.7%, 6.8%, 0.8%), a reading of an engine
  that no longer stands, so the pick is made on omni-v23's ladder; 60 s, set on 22 October for the reads of the cluster, is one
  setting of the dial like every other.

## 2026-10-31: omni-v23 stands: Omni direct keeps every muscle Omni-Compass cannot be
- **omni-v23** (`OMNI_V23.json`, fingerprint `c96ea4105d8747db`, 65 files; `docs/OMNI_V23.md`): omni-v22 with one guard in the
  Kubernetes governor's pod muscle of its own, on the founder's order of 31 October ("any muscle that we don't have, Omni-Compass
  cannot be it: it has to be there, if that's Kubernetes or whatever"). A write of a workload's own scale that the cluster refuses is
  recorded and the decision goes on; at three refusals in a row the knob goes back to native's own pod autoscaler, made from the
  operator's target and range recorded on the workload, and the muscle leaves the workload to it: the organism never runs with a
  knob nobody moves. 64 of 65 files are omni-v22's bytes; the model gate against omni-v22 (`results/model_gate/V23_VS_V22.md`) read
  identical on every gauge, no LOSS; `tests/test_own_replicas.py` (`HandBack`) proves the guard. Every benchmark runs again on it
  from 16:30 UTC.
- **The arm by itself, found void since 24 October** (`docs/SOLO_PREREGISTRATION.md`, amendments 1 and 2): the kind rig's identity
  never granted the scale subresource the pod muscle writes, so every solo arm's pod writes were refused, 15 of 15 decisions a
  window, while the machines and conveyance wrote as always; from 29 October the rig's own end read of the removed autoscaler ended
  the arm with exit 1. The identity gains the grant (and `create` on autoscalers for omni-v23's hand-back), the preflight proves the
  writes by name, the solo arm's end record is the workload's own, a window with a failed decision or a hand-back is refused as a
  result of that arm; `tests/test_kind_rig_rbac.py`. omni-v21's three runs and omni-v22's two of the entry are read in no table; the
  entry runs again, A, B and C, behind the campaign.
- **Orders of 31 October** (CLAUDE.md): Omni direct keeps every muscle Omni-Compass cannot be; every fix pushed, the website
  following main, the live engine defensible in line.

## 2026-10-30: omni-v22 stands: the data stores' wires at the max, through each store's own account of a miss
- **The hand-back lands** (`omni_controller/controller.py`, `omni_controller/muscles.py`, in omni-v22): every step of the Kubernetes
  governor's hand-back is tried 5 times against a transient failure of the cluster's API, each muscle on its own, and what did not
  land is raised and audited. Six-kube run 41044680505, repetition 346: one 500 from the API on the autoscaler list at the reset ended
  the whole hand-back on its first read, the conveyed CPU limits and the replica range stayed behind, and the arm was marked
  invalid; that is the failure the founder saw in GitHub's mail. `tests/test_restore_retry.py`.
- **omni-v22** (`OMNI_V22.json`, fingerprint `0e23a0bc561b900a`, 65 files; `docs/OMNI_V22.md`): omni-v21 with the five data stores'
  wires brought to the max, the founder's order of 30 October ("bring to a solid A mechanism"). What a wire's own rule asks goes
  through unclamped, up to the operator's cover, never below native; memory is spent only where the store's own account (MySQL's
  performance schema timer on the data files' reads, WiredTiger's page-read time for the application's threads, the Redis
  application's own split) says the misses are at least the one key's floor of the service's time, and only while the host keeps
  its 5% cushion; a hand-back never goes below the working set's floor; Kafka's group has a twin of its arrivals and a reflex;
  PostgreSQL's pool is never taken below the pooler's own setting. `OMNI_DIAL=save` keeps omni-v21's loop on every wire;
  `tools/store_brain.py` and `tools/knob_verdict.py` join the fingerprint. The store gate (every candidate on omni-v21's archived
  seconds), the Redis closed-loop model and the Kafka closed-loop model at the counted 30 s read no LOSS (class S); the Kafka model
  at 20 s a notch reads one LOSS row (the burst's peak queue, inside the seeds' spread), on the next version's list.
- **The root-cause page's correction** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`): the morning's reading that a MySQL or MongoDB miss
  cost the statement nothing is withdrawn; the server's own meter, read on a machine of our own, puts the misses at 3% to 32% of a
  statement's time (a tuning-bench reading, class L on that host). A slope of latency on miss share was tried as the price and is not
  used anywhere: it reads the host's noise as a price.
- **The audit of 30 October** (`docs/AUDIT_2026-10-30.md`): the six-kube evidence races fixed at their cause (`tools/bench_integrity.py`),
  the A100 card and A10 stacks three-run tables, the GPU rig's readiness barrier (amendment 15), the two load-sensitive tests fixed
  at their cause, the secret-names check, the LOSS ledger's causes for the stores.

## 2026-10-26: the live benchmark engine on omni-v21; the scoring contract audited; the documents by reader

- **The live benchmark engine rebuilt on omni-v21** (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`): main's twelve omni-v21 data-store
  tables merged in; the page names omni-v21 as the engine that stands in its prose, its manual and its appraisal (the appraisal's
  engine paragraph had still described omni-v17). The page's redline reflex is omni-v21's immune rule ported line for line
  (`omnicompass/immune.py`): over the line three decisions, stuck unless relieved by 5%, native's twin stronger by 5%, a hold of 10
  decisions doubling to 160; every one of its numbers a knob on the mechanism panel (nothing written into the rule), the factory
  numbers the engine's own. Wide tables scroll inside their own box on a phone.
- **The scoring contract, metric by metric** (`tools/audit_export.py`, `docs/audit/BENCHMARK_DISCREPANCIES.csv`,
  `docs/audit/STATISTICAL_VALIDATION.md`): every gauge of every three-run table with native and Omni-Compass in each run, the raw
  change with its true sign, the aim, the word, its class (GAIN, LOSS, power given, STEADY exactly the same, under the 0.5% floor,
  statistically inconclusive, the runs disagree), the confidence, the practical significance and the stability, each apart; an
  independent classifier sharing no code with the key reads 9,424 rows alike and none otherwise; 857 rows cannot be recomputed from
  the committed tables (101 standing, printed to two decimals), listed as a traceability gap.
- **The live benchmark engine's acceptance in a real browser** (`tools/live_engine_acceptance.py`,
  `docs/audit/LIVE_ENGINE_ACCEPTANCE.md`): 13 of 13 checks pass, among them the three shapes as drawn, the reflex on the engine's
  numbers acting under a surge, the kill switch and a phone's width.
- **The release gates** (`docs/audit/RELEASE_GATE_REPORT.md`): each marked by what ran; security, the mathematical referee report,
  the control-safety audit and a clean-room reproduction not yet run, so no grade is declared.
- **The documents by reader** (`README.md`, `docs/README.md`): the board, the CFO, the CTO, engineering, security and IP, the
  referee and the live benchmark engine's evaluator, each with what to read first and the evidence after it, and the hierarchy of
  evidence and claims (the draft pull request #19's navigation, every link checked, STEADY for STEADY).
- **Derived reports in the one format**: STEADY read STEADY in every file main's merge brought it back into; the index and the
  benefit sheet print a size beside its word without a sign, the raw change apart.

## 2026-10-25 (evening): omni-v21 stands: the immune system knows itself, knob by knob

- **omni-v21** (`OMNI_V21.json`, fingerprint `b658f05d43c1e602`, `docs/OMNI_V21.md`): omni-v20 with the immune system's
  self-knowledge, the founder's order of 25 October: a knob redlining past its line that Omni-Compass cannot bring back goes to
  native where native's twin reads it lower, and stays where native is not stronger. In the Python (`omnicompass/immune.py`) and
  its C++ twin (`cpp/src/immune.cpp`, sealed), carried through the nervous system in both (`native_hold`), wired into the
  Kubernetes governor; omni-v19's immune rules carried onto omni-v20. The model gate against omni-v20: no LOSS in any model.
- **The live-engine chat's work on main** (omni-v20, the data stores' wires, the twenty scenarios, the live engine and manuals),
  merged on the founder's order, its own branch's faults fixed on the way; main's verify brought back to green.

## 2026-10-25: omni-v20, the data stores' wires fixed at their causes

- **omni-v20** (`OMNI_V20.json`, digest `1df07f8e36a97985`, 62 files; `docs/OMNI_V20.md`), landed under the founder's words of 25
  October ("Fix, fix, fix") and the standing order that every fault found is fixed and lands as the next version. omni-v19 with five
  wires changed: sysbench reads its own workload (prepared statements counted, as its own account); Kafka hands a consumer back above
  the operator's count on calm and starts with no double rebalance; YCSB grows its cache back below native while it misses, full at
  80% or evicting, `serverStatus` read lean; YCSB and Redis record the stack's CPU apart; pgbench resets and checkpoints every arm and
  logs the runner's stalls. The store gate (`results/model_gate/STORE_GATE.md`) read no LOSS. The causes:
  `docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md`. Every benchmark runs again on it.
- **The injection grid** (`tools/injection_grid.py`, `results/injection_grid/`): the Python's batch of 500 injections through every
  organism and the fourteen governors, 1 to 500 runs by 1 to 500 organisms stacked, read per muscle; on the live engine in section 4b.
  Omni-Compass's LOSS cells: none; the governors' own LOSS cells against native: 37, shown as theirs.
- **The consensus audit of 24 October** (`docs/engine/CONSENSUS_AUDIT_2026-10-24.md`): five seats, overall B; the first round of the
  majors fixed on the live engine.

## 2026-10-24 (late afternoon): omni-v19, Omni-Compass by itself, a pod muscle of its own; the two engines named omni-v18 reconciled

- **omni-v19** (`OMNI_V19.json`, digest `36ee67284c035235`, 62 files; `docs/OMNI_V19.md`), landed under the founder's order of 23
  October (three arms: native; Omni-Compass and native; Omni-Compass by itself) and the standing order that every change lands as
  the next version, told, not asked. omni-v18 (Omni direct in the fingerprint) with a pod muscle of its own (`--own-replicas`): for a
  workload the operator names and no autoscaler governs, the Kubernetes governor sets the replicas itself through the workload's own
  scale, at the target the compass moves, reconciled every 15 s on the fast checks, never below the operator's count at the max, the
  operator's count handed back by the reset; and the models' arm by itself (`realms/harness.py`, `realms/plants.py`). 59 of its 62
  files are omni-v18's bytes.
- **Two engines had one name.** The change was first landed on the live engine's branch on 24 October, 01:30 UTC, as that branch's
  own omni-v18 (digest `22486290b19349eb`, 55 files, on omni-v17), while main's omni-v18 (digest `1cb92edb64c4391d`) stood. By the
  standing rules (one number, one engine; nothing read across engines) that engine never stood on main and none of its records is read
  as main's omni-v18; its three engine files are applied onto main's omni-v18 and land as omni-v19, gated again against main's
  omni-v18. The code's comments that named the branch's numbers name omni-v19; every rule is the branch's. Main's omni-v18 files and
  records are untouched.
- **The model gate against omni-v18** (`results/model_gate/V19_VS_V18.md`, every model, 8 seeds): every gauge of all 11 models identical,
  seed for seed (95 rows and the verdict), the numbers the branch's own gate against omni-v17 read; no LOSS against omni-v18. The
  rows against native that read LOSS are omni-v18's and omni-v17's, unchanged, each on the next version's list. In the models, the
  native and max arms read byte-identical on both engines (806 readings on the development seeds 7101 and 7102: 67 muscles under
  their own load, the climb and the line, and one body of 60 muscles). **By itself** (`results/model_gate/SOLO_V19.md`, class S) against native on the same
  machines: the 95th percentile GAIN (down 19.4%), the minutes over the response line GAIN (down 64.9%), machines and energy STEADY;
  against omni-v18 by itself, arm by arm (`results/model_gate/SOLO_V19_VS_V18.md`): native and Omni-Compass and native identical, by
  itself the 95th percentile GAIN (down 100.0%) and the minutes over the line GAIN (down 99.3%), omni-v18 having no pod muscle.
- **Brought with it** (the arm by itself, and only that): `tests/test_own_replicas.py` (11 tests); the kind rig's `ARM=solo`
  (`scripts/kind_bench.sh`, `fleet/capture/kube_capture.sh`, `tests/test_robust_restart.py`) and its readings (`tools/confirm_abc.py`,
  `tools/live_reps.py`); the organisms runner's third arm (`tools/run_realms_v5.py`); the solo study (`tools/solo_study.py`, its arm
  table corrected to the setting it runs: no Cluster Autoscaler, 12 machines in every arm); and `kubernetes by itself` in
  `scripts/reruns.txt`, written before the omni-v19 campaign opened (the queue 192, `tests/test_release_campaign.py`).
- Every place that names the engine that stands says omni-v19 (`tools/land_engine.py v19 --since 2026-10-24T16:54:55Z`): the fingerprint, the
  version list, the conductor's campaign, the grid manifest and workflows, the package 0.19.0, the root list, the release group;
  the words by hand: the version page, README, CLAUDE.md, the Operator's Manual, the state of play, this changelog, the live
  engine's engine mark (its prose stays omni-v18's until the page is rebuilt).
## 2026-10-24 (night): every change of 0.5% or more is a change

- **The key** (`tools/readings.py` `three_run_reading`, the founder's order of 24 October): the change is the mean of the three
  runs' changes in percent of native; from 0.5% up it reads GAIN, LOSS or power given by what the gauge is for, "in all three of
  our runs" where every run moved the same way clear of zero, otherwise "by the mean of our three runs" with the count of runs
  beyond the noise. STEADY is kept for a mean under 0.5% or no change at all; runs that moved 0.5% or more in opposite directions
  disagree; a count that must never rise has no floor. Each run's own number in a kind table wears that run's own word, and an
  interval turns with its number where the word turns the number's sign.
- **Every table read again from its own data** (`tools/reread.py`, idempotent, checked by `verify.py`): 4,037 readings in 194
  tables; the numbers are the runs' own, only the words were read again, and each table says so under its title. The kind,
  stack and three-arm writers read by the same rule from now on; the deterministic simulators (CityLearn, pandapower, MuJoCo, the
  swarms) put a mean under 0.5% at STEADY, under the floor.
- **What moved**: the index's headline reads GAIN, up 3.4% (up 4.3% before); the LOSS ledger holds 331 rows read LOSS across their
  three runs (160 against Omni-Compass's own native, 284 of all of them on omni-v12, none on omni-v18, whose three runs have not
  landed); the real knobs' verdicts read 4 write, 21 the operator's choice, 1 watch (9, 5 and 12 before).
- **The model gate and the live engine read by the same floor**: the gate's mean change across its seeds from 0.5% up reads by its
  aim, with whether it stands beyond the seeds' noise beside it; the live engine's own key (`threeRun`, `pairedReading`) the same,
  each run's number wearing its own word, and how firmly a word stands printed beside it.

## 2026-10-24 (evening): no table stands on two engines; every LOSS row on one page

- **Ten three-run tables held two engines**: `V17_KAFKA`, `V17_KAFKA_SERVICE`, `V17_PGBENCH`, `V17_REDIS`, `V17_REDIS_SERVICE`,
  `V17_REDIS_SHIPPED`, `V17_SYSBENCH`, `V17_SYSBENCH_SHIPPED`, `V17_YCSB` and `V17_YCSB_SHIPPED` carry runs A and B on omni-v17 and
  run C on omni-v18. Each printed its own warning, and the index, the benefit sheet and every page that picks a benchmark's newest
  table still counted it. `tools/readings.py` `landed`, the one rule those pages read, now refuses a table whose runs ran on two
  engines; each of those benchmarks stands on its newest table on one engine (omni-v16 for most) until its three runs on the
  engine that stands land. The index's headline moves from GAIN, up 4.6%, to GAIN, up 4.3%.
- **The campaign counted runs of the engine before**: omni-v18's campaign was opened at 21:19 UTC on 23 October, when the engine
  landed on its working branch; it reached main at 02:51 UTC on 24 October. The runs started between ran omni-v17's commits and
  counted as omni-v18's. The conductor now counts a run in the campaign only when its own commit carries the standing engine's
  fingerprint file (`scripts/dispatch_grid.py` `on_engine`), and the campaign's start reads 02:51 UTC on 24 October
  (`tests/test_release_campaign.py`).
- **The LOSS ledger** (`docs/LOSS_LEDGER.md`, `tools/loss_ledger.py`, checked by `verify.py`): every row that reads LOSS in all
  three runs, in every benchmark's newest table, placed by what its two arms are. Against Omni-Compass's own native, the readings
  do no harm is judged by: 7 rows, all on omni-v12, each with its cause where one is written. In place of an orchestrator (the four
  ways' VS): 14. Without Omni-Compass in one arm, or two changes at once (ORCH, BOTH): 89.

## 2026-10-24 (afternoon): the conductor ticks again on omni-v18

- **Why no benchmark started from 07:05 UTC**: the conductor (`grid.yml`) and the grid's own jobs (`six`, `six-kube`, both
  pools) and the capacity test fetch only some folders, and none of their lists named `omni_orchestrator/`, which omni-v18 took
  into the fingerprint. Their engine receipt (`tools/omni_version.py`) read every fingerprinted file from the folder, met one
  that was not there and stopped. The conductor of 02:32 UTC had started on a commit its receipt still read whole and ticked
  for five hours (the omni-v18 campaign's B and C reruns, Azure's steady set); every successor from 07:05 failed in seconds.
- **The fix, in the one place every workflow shares**: the version tool reads a file a partial checkout left out from the
  index, where git keeps it; only such a file, so a file deleted by hand from a full checkout still fails
  (`tests/test_omni_version.py`, failing on the old tool). Not an engine change: the tool is outside the fingerprint, and
  every version reads as before.
- **No more chain of failed conductors**: a conductor started its successor whenever it was not cancelled, so each failed one
  started the next, about one every 15 seconds, over 1,600 runs and none ticking. Now only a conductor that ran its whole round
  of ticks starts the next; one that fails earlier starts none, and the three-hourly schedule restarts the chain
  (`tests/test_release_campaign.py`).

## 2026-10-24: Google and Amazon kept in, wired as Azure is, not yet run; the GPU's first card

- **Google and Amazon stay, at Azure's wiring, shown as not yet run** (the founder's words: "you leave the Google and Amazon runs
  in everywhere and just show it not ran yet, because someday, some way, I'm going to have it run ... code it to wire it the same
  way that the Azure is running"). Earlier the same day he had ordered both taken out; the removal was built here and never
  pushed, and is undone whole: every workflow, script, queue, setup page, check, manual chapter, live page monitor and page
  mention stands again. Both queues read `switch=off` (Amazon's account cannot leave its Free plan before its credit is spent or
  it is six months old; Google's key has not been stored whole), so the conductor starts no set and no hourly check for them; every
  page and monitor reads them "not yet run", and they start on his word once the key or the plan is in.
- **The GPU run on Lambda, its first card** (`lambda-gpu.yml`, `scripts/lambda_gpu.py`, `scripts/lambda_gpu_watch.sh`): the key
  stored with its line breaks lost is mended before it is read, Lambda's key is found by its public half (not by its name), and
  where the stored key is not whole the run makes its own key for itself and removes it after. The first real run (an A10) rented
  and stopped at once: the code was shipped without its git record, which the run reads; the tree now goes with it, the token
  stripped. Its watch would have kept the idle card to the deadline (a run cancelled by hand keeps watching, so no give-back is
  lost): the watch now gives the card back as soon as the test stops before its last line, and the new test `giveback` gives back
  every machine whose name starts as given (omni- names only, never one launched by hand), in its own queue. The A10 went back
  after about 15 minutes. The A100 run that followed (40079645681) had its card up in four minutes, then its start step waited
  on one connection to the card until the launch job's 60-minute limit cut it off; its watch took over with the card. Since
  then every machine carries the run's number at the end of its name (-r<run id>) and both give-backs find it by that number,
  so a launch job cut off before it hands the machine's id on still gets its machine back; the launch job's limit is 90 minutes.
  The watch's "is the run alive?" asked pgrep for the scripts' names through ssh's own shell, whose command line holds the same
  names, so it always read "running" and its stopped-run rule could never fire; the names are bracketed now (proved both ways),
  every step the start makes to the machine is bounded in time, and the start says whether the run is under way. The A100 run
  of the morning still carries the old watch: its card goes back when its run ends or at its deadline (18:12 UTC, $18 at most).
- **main's verify on GitHub**: a cloud key test handed the program the runner's own GITHUB_ENV, so on GitHub (never on a
  laptop) the program wrote its masked hand-off and the test failed; the tests now hand it an environment without the runner's
  env files (proved both ways).

## 2026-10-24: the clouds' keys read to the letter of their shape

- **Azure runs; Amazon off** (06:17 UTC): with the four boxes filled, Azure's check passed (the key, the login, the subscription and,
  after the allowance request of `azure-quota.yml`, the processor allowance), and the conductor started the steady set by itself.
  Amazon told the founder its Free plan cannot be raised to the Paid plan before the $100 credit is spent or the account is six
  months old, so scripts/amazon_queue.txt reads `switch=off`: no hourly check fails there and nothing starts until his word.
- **Azure's login in four boxes, one value each** (the founder pasting the portal's numbers one at a time): the Azure sets and
  Azure's $0 check sign in with `AZURE_CREDENTIALS` when it holds the whole block, or else with the block built from four boxes,
  each holding one value as the portal shows it: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID` (the boxes the
  sign-in without a password already reads) and `AZURE_CLIENT_SECRET` (or the password's value alone in `AZURE_CREDENTIALS`).
  `tools/cloud_key_check.py azure` builds it, masks it and hands it to the login as `env.AZ_CREDS`; every failure names the box
  and what is wrong with its shape (an empty box, an ID where the password goes, the Secret ID copied for the Value), never a
  character of it. All nine logins with a password read it (`tests/test_cloud_check.py`); `docs/AZURE_SETUP.md` section 7a
  gives the clicks.

- **What the Azure box holds, named** (the founder's order: "if they don't run, you better dig in ... and find out why. So I can
  fix them"): Azure's own login still works (the steady set started on 19 October signed in at its repetition 99, 02:46 UTC on 24
  October, and carries the key it started with), while every new run reads 88 characters in `AZURE_CREDENTIALS`, the size of a
  storage account's access key, not the block. `tools/cloud_key_check.py` now names that form, text pasted before the `{`, and
  the outline of any other stored text (its lines, and whether it holds spaces, a web address or quotation marks), never a
  character of it; `docs/AZURE_SETUP.md` section 7 makes the new block under a new name (`omni-compass-github-2`), so the login a
  running set still uses is never replaced under it, and the check's message points there. The sign-in without a password was
  refused again at 03:27 UTC (`AADSTS700213`: no trust rule in Azure names this repository as GitHub presents it; section 8).

## 2026-10-23 (night): omni-v18, Omni direct in the engine; the three arms on the live engine

- **omni-v18 lands** (`OMNI_V18.json`, digest `1cb92edb64c4391d`, 62 files; `docs/OMNI_V18.md`) on the founder's orders of the
  evening ("Native is Kubernetes on the muscles. Omni on native is Omni on top of Kubernetes on top of the muscles. And then Omni
  direct is simply Omni on top of the muscles, no Kubernetes"; "It should be not 17 anymore, it should be 18"): omni-v17 with
  Omni direct taken into the engine. The seven files of Omni-Compass's own orchestrator that hold its rules (`omni_orchestrator/`:
  the brain, the control plane, the room rule, the hand, the walls, the front, the package) are fingerprinted like every other
  wire (`tools/omni_version.py`, `ORCHESTRATOR_WIRES`; a version declared before omni-v18 is read without them, so every earlier
  commit keeps its version); 55 of the 62 files are omni-v17's bytes. The model gate against omni-v17
  (`results/model_gate/V18_VS_V17.md`, every model on seeds 1 to 8): every gauge identical, 95 rows, no LOSS; Omni direct's own gate
  is its showing (no LOSS in any of the three pairs after the trial-hold fix). Landed by `tools/land_engine.py` (the campaign
  from 21:19 UTC, the grid's manifest `results/grid_v18/`, package 0.18.0); the words on the README, CLAUDE.md, the state of play,
  the three manuals, the appraisal and the omni-v17 page.
- **The three arms' three runs** on GitHub's machines (runs 40023524338, 40023529155, 40023534013; `results/orchestrator/V18_THREE_ARMS_ABC.md`, `tools/orchestrator_abc.py`): Omni on native against native work GAIN in all three (up 5.2% to 7.4%) and the 95th percentile GAIN in all three (down 7.5% to 12.1%), Omni direct against native work GAIN in all three (up 5.7% to 9.4%) and the 95th percentile GAIN in all three (down 9.8% to 15.7%), machines STEADY, the units power given or STEADY, and Omni direct against Omni on native STEADY on every gauge; no LOSS in any pair in any run (`results/orchestrator/V18_THREE_ARMS_ABC.md`).
- **The live engine shows the three arms** (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, section 1k "Omni direct: the three arms,
  native, Omni on native and Omni direct"): four monitors (work, the 95th percentile, units, machines, each step) registered on
  the wall with their lights (the 95th percentile against the service's line, the units against the service's most, the machines
  against the fleet; work aims up and has no line), arm buttons, a step slider that replays the run, the readings of every pair by
  the one key and each arm's totals. The record is the showing's own files gathered by `tools/orchestrator_record.py` into
  `results/orchestrator/`, read by the page's builder (`docs/engine/build_live_engine.py`, the record `direct`). The page's builder
  stamps omni-v18 and rebuilds every record on it.
- **The three runs on the live engine** (section 1k): under the quick form's tables, the full form's A, B and C from one commit,
  each pair and gauge with each run's word and the one rule's reading of the three (the record `results/orchestrator/V18_THREE_ARMS_ABC.json`);
  the page's words realigned to omni-v18, and the Live Engine Manual's section 7.5 and Appendix A row for `#s-direct`.
- **Omni direct ready on a rented cloud machine** (the founder's order: "update the new Azures ... the new direct ... everything in Azure,
  clouds, all the clouds ... when we get ready, we're going to run that too"): the test `direct` on the one-machine buttons
  (`big-organism-detached.yml` on Azure, `cloud-organism.yml` on Google and Amazon, `scripts/organism_detached.sh`) runs the three
  arms' full form `reps` times on one rented 8-processor machine and brings every run's files back; a dry run (the default) shows the
  price and rents nothing; nothing starts it but a hand on the button.
- **Azure: the second way in written down** (`docs/AZURE_SETUP.md`, section 8): the password-free sign-in the inventory uses was refused
  by Azure (`AADSTS700213`) because GitHub presents this repository by its ID numbers; the one trust rule that makes it work, click by
  click. The benchmark sets keep the key of section 3 (a password-free sign-in lasts about an hour, one repetition about 70 minutes, and
  a lapsed sign-in at the end could leave machines billing).
- **The GPU runs on Lambda start from `gpu-omni-v18`** (`docs/LAMBDA_SETUP.md`).
## 2026-10-24 (late night, the live engine): the Monte Carlo 500, the Python and the C++ linked; your own system through it

- **The linked run** (the founder's words: "Monte Carlo 500 Runge-Kutta, my C++ and Python linked together, ran through as a
  button"): `cpp/tools/core_runs.cpp` (new, `oc_core_runs`) runs the Python's draws (`tools/core_runs.py` writes them, the injection)
  through the sealed C++ twin of the core (`cpp/src/core.cpp`) in the Python's own loop, four ways; on 500 runs every U of every run
  is the Python's to the last bit (2,000 of 2,000 run-ways, largest difference 0), one digest. One button in the control panel and on
  monitor 4 stands the three side by side, the Python's, the C++'s and this page's run now, and reads ALL THREE THE SAME. The
  thirteenth twin of the seal (`tools/seal.py`); `verify.py` runs the C++ against the Python on every push
  (`tests/test_cpp_core_runs_parity.py`).
- **Your own system** (the founder's words: "if somebody wanted to theoretically hook up their own system and hook this to their
  stack and run their own system through it, is wired into that other button, which is the simulation that's done within the
  GitHub"): a system is a stack written as ranges of the core's six states and 22 parameters (`systems/README.md`, numbers only, never
  run as code); the panel checks it, runs it in the page, downloads it, and sends it to GitHub, where the new workflow
  `.github/workflows/monte-carlo.yml` runs it through the Python and the C++, checks the page's port on it, and commits the record. The
  example (`systems/example_heavy_swing.json`, not any real stack): Omni-Compass on top certified 500 of 500, native alone 237, the
  same digest from the Python, the C++ and the page. Class S.

## 2026-10-24 (night, the live engine): the switchboard, the reports, the Python's runs again; the page on omni-v18

- **The Python's Monte Carlo, a monitor** (the founder's words: "the Python's Monte Carlo, our 4K Runge-Kutta, 20-step macro, 10-step
  micro in each macro ... how long in steps that OmniCompass gets it into the basin and holds it there and certifies the count"):
  monitor 4 (section 1f, `#mcPanel`) draws the engine's core (`omnicompass/core.py`) over 500 runs, each from step 0, every run's U
  across the 20 macro steps of 10 RK4 micro steps, native (the plant alone, u = 0) beside Omni-Compass on top (toward the nearest
  basin, the far basin, or with the double well off), the basins at ±1, and the macro step each run was conveyed (5 in a row) and
  certified (10 in a row). It opens on the Python's own 500 (`benchmarks/core_evidence.py`, seed 223387268; its counts are the
  record's: 500 and 500 on top, 476 and 427 native alone). A set drawn on the page runs through its own port of the core, line for
  line; `tools/core_runs.py` (new) runs the same set in the Python from the jump generator and writes one digest, `--verify` holds
  the page's port to it (500 runs, four ways: 2,000 lines identical), and the engine-runs workflow writes the Python's record of every
  base it runs (`results/core_runs/`, first record base 1369407155). Class S.
- **The Python's jump generator: one switch in the control panel** (the founder's words: "some button that allows them to activate
  the Python's jump generator ... running it again and again and again ... when the button's not on, it's in some other form of
  running"): ON, set after set of 500 (or 100, or 1,000) from one base after another, each run in the browser through the engine's
  runs and through the core's Monte Carlo, each with its digest beside the Python's where the Python has run the base; OFF, the
  page's standing mode, its records played, written under the switch in plain words.
- **The lights as a traffic signal** (the founder's order: "underneath the monitor's number on the left side ... the green, yellow,
  red vertical stop sign order"): on every monitor's badge and every wall tile the three lamps stand under the number as a traffic
  signal stands: red on top as an octagon, yellow in the middle, green at the bottom (the founder's correction of the same night: "The
  red is on the top, the green is on the bottom"); the signal opens the light's reason like its button.

- **The switchboard** (the founder's words: "knobs, buttons that allow you to switch amongst all the different organisms ... direct,
  native, Omni on native ... 1, 10, 100 ... A, B, and C runs ... 5 seconds ... 45 ... 120 seconds in the heartbeat"): one row of
  knobs in the control panel, the arm, the organism, the copies, the runs, the run letter and the beat, each reaching every monitor
  that carries that variation through its own setter and naming the monitors it moved; the grid marks the chosen square.
- **The reports** (the founder's words: "physical buttons that shows these reports in some form of PDF ... engineers and software
  CTOs ... boards and all the CFOs"): the engineer's, the CTO's, the board's and the CFO's, each written from the page's records when
  pressed, opened for print or a PDF and downloaded, the notice first and last, every reading by the one key with the word's sign,
  every number with its engine and its run.
- **The Python's runs again** (the founder's words: "the Python is a 500 run mechanism, and running it again runs another 500"):
  "Run another 500" and "Run three more sets" beside "Run a new set here"; every set run on the page is listed with its digest and
  checked against every set the Python has run (the build now lists them all, `build_live_engine.py`, `eruns["sets"]`).
- **The page on omni-v18**: its records rebuilt on the engine that stands, its words realigned (the engine, the third arm's engine).
  The Live Engine Manual reads the switchboard, the reports and the Python's buttons in 4.0.

## 2026-10-24 (night): omni-v18, Omni-Compass by itself, a pod muscle of its own

- **omni-v18** (`OMNI_V18.json`, digest `22486290b19349eb`, 55 files; `docs/OMNI_V18.md`), landed under the founder's order of 23
  October (three arms: native; Omni-Compass and native; Omni-Compass by itself) and the standing order that every change lands as
  the next version, told, not asked. omni-v17 with a pod muscle of its own (`--own-replicas`): for a workload the operator names and
  no autoscaler governs, the governor sets the replicas itself through the workload's own scale, at the target the compass moves,
  reconciled every 15 s on the fast checks, never below the operator's count at the max; and the models' arm by itself
  (`realms/harness.py`, `realms/plants.py`). 52 of its 55 files are omni-v17's bytes.
- **The model gate against omni-v17** (`results/model_gate/V18_VS_V17.md`, every model, 8 seeds): every gauge of all 11 models identical,
  because nothing moves unless a workload is named. **By itself** (results/model_gate/SOLO_V18.md (the by-itself arm, removed), class S) against native on the
  same machines: the 95th percentile +19.4% GAIN, the minutes over the response line +64.9% GAIN, machines and energy STEADY.
- **The fault found before it landed**: rebuilt on omni-v17's 60 s beat, the first candidate moved pods once a minute and read the
  minutes over the line LOSS against native (26.4 to 34.8 a day); the muscle now keeps the pod autoscaler's 15 s pace between
  decisions (two unit tests). `tools/solo_study.py` writes its closing words from the engine it reads.
- Every place that names the engine that stands says omni-v18 (`tools/land_engine.py v18`); omni-v17's page in its past tense.

## 2026-10-23 (night, the live engine): Omni-Compass direct on the page, section 5g; the orchestrator merged; the phone page fits its width

- **Section 5g, Omni-Compass direct: the organism with no orchestrator, the three arms** (the founder's order of 23 October:
  "Omnidirect is simply Omni on top of the muscles, no Kubernetes ... written in code ... put into the GitHub"). The orchestrator's
  branch (`omni_orchestrator/`, `tools/orchestrator_show.py`, `.github/workflows/orchestrator.yml`, `docs/OMNI_ORCHESTRATOR.md`)
  is merged into the live engine's branch, and the page plays back every showing GitHub ran from its own files on the branch
  raw (`docs/engine/build_live_engine.py` `direct()`, the record `direct`): each arm's requests answered a second, its 95th
  percentile, its units and its machines on, 5 s at a time, read the way the showing reads them; the arms' own totals; the
  showing's readings by the one key, the number beside the word in the word's sign and every interval in its gauge's unit.
  Knobs: the showing, the gauge, the arms drawn. Native is amber, Omni-Compass and native blue, Omni-Compass direct violet
  (`--direct`), dashed. Its light reads the showing's readings (red on a LOSS, every row kept) and says it is one run of each
  arm, class L. Monitor 39 (`dirCv`) in `docs/engine/monitors.json`, every later monitor one number up; the orchestrator
  exports no Prometheus series yet, and its Grafana panel says so. Like the ledger, the record is a reading of what GitHub has
  archived, with its own read time, and a check does not rebuild it. The Live Engine Manual reads it in 11.5.
- **Every monitor's light is a button in green, yellow and red, with native's side and Omni-Compass's side apart** (the founder's
  words: "Every monitor is to have a red and green button as red is alert ... green has got to be good"; then "they're supposed to be
  a yellow too. Yellow would mean it's even ... all the reds are theoretically native"). Green: working inside its lines, or no line
  to cross. Yellow: heading for its line (within 3% of it, or its slope crossing it within three readings), or STEADY on a record. Red:
  over its line, or a LOSS row in its record. The nineteen monitors that draw the organism's two sides carry two lights in one button,
  native's and Omni-Compass's, each read from its own side, and between them the reading now, Omni-Compass against native on the
  same load by the key (GAIN green, STEADY yellow, LOSS red, by whether the gauge helps or hurts, never by its sign); before, one moment
  of the organism lit all nineteen at once from Omni-Compass's side alone. Every wall tile carries three lamps in its corner, green
  round, yellow a diamond, red an octagon, the lit one moving with the reading; the Grafana wall's panels carry the same three colours
  as thresholds where the line is a number on their series. A click opens each side's reason and, on a red or yellow one, the way back to the factory tune; the
  wall's corner dots and summary line use the same colours and name the monitors whose native side is red. Read over one model day of
  the page's organism (240 decisions, class S): native over its line in 173 decisions (350 muscle-decisions), Omni-Compass on top in
  147 (272, 22% fewer), never over where native holds; the climb loads the fixed muscles past what they can carry.
- **The phone page fits its width.** The lights' summary bar above the wall held a list of monitor numbers that did not wrap,
  so at 390 px the page scrolled 513 px sideways; it wraps now, and nothing on the page is wider than the screen.

## 2026-10-23 (evening, the live engine): the sign explained where every number sits; a light on every monitor; one button back to the factory tune; the third arm named

- **The sign, explained where the number sits** (the founder's words: "you cannot just put minus 29 gain or down 29% and then say
  gain ... you need to now explain that wherever things are"). Every word and every coloured size the live engine writes carries its
  reason on hover (`SIGN_WHY`, `whyOf`, `whyPass`): what the word means, why the number wears the word's sign, and where the page
  knows the gauge (`runWord`), what rose or fell against native. The key (section iv) carries one paragraph, "How to read a number
  beside a word", with the four cases spelled out; the Live Engine Manual's key says the same.
- **A light on every monitor, leading the line** (the founder's words: "every monitor needs to have a light in it ... that could tell
  when something is redlining ... gauging a couple percentage before"). Each monitor carries a light beside its number and in its
  wall tile's corner (`LAMP`, `lampRead`, `lampSweep`): green inside its lines; amber before the line, when the gauge is within 3%
  of it or when its own slope over the last readings, carried three readings ahead, crosses it; red over it; grey, and said so, where
  there is no line to watch. The light reads the series its monitor draws: the live engine's muscles against their lines, a cluster
  replay's 95th percentile against the 200 ms line and its pods waiting, the heart's decision time against half its beat, the CPU
  host's busy share against 75%, the card's draw against its power limit, the page's own frames against 1.5 frames, a record's judged
  rows (a LOSS row lights red and stays). Above the wall one line counts the lights, names the monitors heading for a line or over
  one, and prints the engine's own last entry on its side; the three-reading projection is the light's own.
- **Back to the factory tune, one button** (the founder's words: "there has to be a main button that puts it back ... once buttons
  are touched"). On the console under the kill switch, on the dock, above the wall and in every monitor's knobs: every knob of the
  page returns to the main engine as it ships (`factoryTune`): the max, Omni-Compass ON, demand ×1, noise σ 0, sense delay +0, no
  fault held, every muscle driven, speed 1×, running, no frame load, the heartbeat monitor on the factory's 60 s; it says what it put
  back. Native alone stays the kill switch.
- **The three arms, named** (the founder's order: "the one that said Omni before is going to have to add the word and native"). The
  title chips, every table head and every lane on the page read native, Omni-Compass and native, and Omni-Compass by itself; the key
  and the whole organism (section 3) say what the third arm is (`docs/SOLO_PREREGISTRATION.md`) and that its column appears from its
  first run on GitHub's machines, nothing written for it before.
- **The beats the ladder had not read, 20, 40, 45 and 50 s, read on the side** (the founder's words: "I think 45 you didn't try"),
  in our own models on omni-v17, eight seeds, both settings, and folded into the ladder's record (`results/model_gate/V17_LADDER.md`,
  the page's section 1j; class S). Against the main engine's 60 s in the kind benchmark's setting the minutes over the line read GAIN
  at 20 s (+14.7%) and at 40 s (+13.2%), STEADY at 45 s (=9.0%) and 50 s (=5.8%); every other gauge STEADY; the reads a day and the
  governor's own processor power given (+5% reads at 40 s, +22% at 20 s). In the cloud's setting every gauge reads STEADY against 60 s at
  every beat. Against native the rows are the ladder's: pods waiting for a place LOSS at every beat in the kind setting (the
  engine's, on the next version's list), the 95th percentile and the minutes over the line GAIN. By the key, 60 s is not the beat that
  reads best on the service: 20 s and 40 s read GAIN against it with no LOSS, their cost power given; the factory beat is the next
  version's decision, through the model gate (the order of 23 October).
- The page was opened headless at 1280 and 390 px after the change: no console error; the lights, the tooltips and the factory
  button respond. The Live Engine Manual carries the lights (4.1), the button (18.1) and the sign (the key); its appendix is rebuilt.

## 2026-10-23 (evening): Omni-Compass's own orchestrator with the engine's mechanisms in its brain; the three arms; the room's two walls

- **Omni-Compass by itself, the organism run without Kubernetes** (`omni_orchestrator/`, `docs/OMNI_ORCHESTRATOR.md`; the
  founder's order of 23 October: "Build it in your chat before you"). Built from scratch on Python's standard library and the
  compass law, no orchestrator's code in it: the walls (the kernel's control groups, version 2 and 1), the machine's hand, the
  front, the room rule, the brain, the control plane with its journal and kill switch, the checked workload, the clients.
  The yardstick it is read against is Kubernetes' published autoscaling rule, written by us. Three arms, always together (the
  founder's order of the same evening): **native** (the rule on the muscles), **Omni on native** (Omni on top of the rule, the
  engine's strict form as on the kind rigs: the rule's units never fewer, Omni's reflex, conveyance, packing and machines on
  top; brain `omni_native`) and **Omni direct** (Omni alone on the muscles; brain `omni`); every pair read by the one key,
  paired by step (`tools/orchestrator_show.py`, `.github/workflows/orchestrator.yml`).
- **The brain's win is the engine's own mechanisms.** The first showings read LOSS, then STEADY: Omni held the yardstick's count
  with the same walls, and the response time was the unit's own paper quota (no request ever waited in line). Four mechanisms,
  all the engine's, went into the brain: conveyance (each unit's CPU wall set to the room its machine can spare under 75%,
  journaled, written to the hand, read back from `cpu.max`; omni-v7 and omni-v13's rule), the reflex (work in line adds units
  in the beat), the yardstick twin read as Kubernetes would (busy capped at the request) and the fold under the verdict
  (`omnicompass/verdict.py`, a unit fewer than the twin tried on the service's own response times under the same traffic, kept
  only where it reads no LOSS within 2%; a trial whose arrivals move 15% is abandoned; work in line hands a step back). The
  full form (18 steps of 25 s, one run of each arm, class L), Omni direct against native, by the one key: **work GAIN, up 4.7%
  a step; the 95th percentile GAIN, down 9.9%; units GAIN, a cut, down 10.3%; machines STEADY, down 1.7%**; 0 failed, 0 wrong
  in 20,452 requests; the batch job 16 of 16 beside the service; the drills (a unit killed, a machine lost and repaired, the
  control plane killed and started again, the kill switch) 3,308 requests, 0 failed. One run of each arm, not yet the
  three-run reading; the referee grades (`docs/OMNI_ORCHESTRATOR_GRADES.md`): B overall, not production.
- **The three arms' first showing found a fault, fixed in the brain.** Quick form, one run each: Omni direct against Omni on
  native read work LOSS (down 5.2%). Every trial the verdict began was abandoned by the traffic gate (the clients step every
  15 s), yet each held a unit below the twin while it ran, and one trial counted its step from a twin the traffic had since
  raised. Now a trial the traffic abandons holds the next off for 6 beats, doubled in a row up to the recheck (24 beats), cleared
  by a trial judged to its end (`omni_orchestrator/control.py`), and a phase counts its step from the higher of the twin it found
  and the twin now (`omni_orchestrator/brain.py`); two unit tests. After the fix, the same quick form: Omni on native against
  native, work GAIN (up 8.3%); Omni direct against native, work GAIN (up 9.1%); Omni direct against Omni on native, the 95th
  percentile GAIN (down 13.2%), units GAIN, a cut (down 9.5%); no LOSS in any pair; nothing failed. The workflow's room rule
  defaults to the engine's busy rule, as the showing and the page do.
- **The room, written** (`docs/THE_ROOM.md`, `docs/THE_ROOM_TABLE.md`, `tools/room_table.py`): the founder's law that a muscle
  with no gain is at its limit and a LOSS is never the muscle's; the catalog read by it (527 GAIN, 421 at their limit, 159 the
  same as native, 0 LOSS); the two walls found on 23 October (the processor core, wired by the busy rule; the unit's paper
  quota, moved by conveyance); the unit count's own edge in mathematics (Erlang's C, the square-root law against Kubernetes'
  2a: no room at this rig's load, near half at a company's scale).
- **The orders of 23 October** in `CLAUDE.md` (both arms to the best; the brain finds the win; where a LOSS may ever be seen; the
  word before the sign; every tool to strengthen the engine) and `DISCLOSURES.md` section 3 (the factory tune is published only
  where it reads no LOSS; the live engine's knobs are where a LOSS is meant to be seen). The engine's fingerprint does not move:
  the orchestrator is its own files beside omni-v17.

## 2026-10-23 (afternoon): omni-v17, the heartbeat a dial; the main engine at 60 s

- **omni-v17 lands** (`OMNI_V17.json`, digest `7c937d09e4031cc7`, 55 files; `docs/OMNI_V17.md`) on the founder's order of the afternoon,
  once he had read the reads of the cluster a day in the pace study (about 86,000 at 5 s against 39,700 at 60 s): the heartbeat
  is a dial ("5, 15, 30, 60, 75, 90, 120 ... Heartbeat scaled in its monitors. And you're going to set OmniCompass is main
  engine"). The main engine takes its full decision every 60 s (`--interval 60`, the parser's default in
  `omni_controller/controller.py`, the one engine file changed; 54 of 55 are omni-v16's bytes); any beat from 5 to 120 s can be
  set, the fast checks every 5 s at every beat. Every rig, install file and cloud run starts it at 60 s (`OMNI_INTERVAL` in
  `scripts/kind_bench.sh`, `kind_paired.sh`, `kind_robust.sh`, `kind_levers.sh`, `kind_full.sh`, `kind_pilot.sh`,
  `deploy/install/*.yaml`, `deploy/controller.yaml`).
- **A fault the dial's ladder found, fixed before landing**: at 90 and 120 s the cruise rule's wait (120 s) rounded to one
  decision (`max(1, round(120 / period))`), so one reading with a pod waiting put every machine in service; in the kind setting
  the first reading held 17% and 21% more machine-hours than at 60 s, the minutes over the line 72% fewer. The cruise wait is
  now never fewer than two readings (`max(2, ...)` when derived from seconds; a hand-set `--cruise-after` stands), so nothing
  at 80 s or faster moves (`tests/test_pace_clocks.py`, which fails on the unfixed rule). Corrected, the kind benchmark's setting reads at 90 s, against 60 s, the machine-hours down 1.7%, STEADY, the minutes over the line down 4.7%, STEADY, the pods waiting down 12.1%, STEADY, the 95th percentile down 0.2%, STEADY; at 120 s the machine-hours down 2.1%, STEADY, the minutes over the line down 3.7%, STEADY, the pods waiting down 29.6%, GAIN; machines parked over the eight days 190 and 119 against 329 at 60 s.
- **Every beat beside native, in our models** (`results/model_gate/V17_LADDER.md`, `tools/beat_ladder.py`, class S): Every beat reads the cluster from about 86,400 times a day at 5 s to 37,400 at 120 s (39,700 at the main engine's 60 s), for 5.5 to 1.6 s of Omni's own processor an hour. In the kind benchmark's setting every beat reads the minutes over the line GAIN against native (down 12.0% at the main engine's 60 s, down 28.2% at its most), for machine-hours and energy given; the rows that read LOSS against native are in the kind setting pods waiting for a place at 5, 10, 15, 30, 60, 75, 90 and 120 s (up 175% to 317%); and in the cloud's pods waiting for a place at 5, 15 and 30 s (up 102% to 127%), the 95th percentile at 15 and 30 s (up 0.5% and 0.4%), the minutes over the line at 15 s (up 2.3%): the engine's, on the next version's list.
- **What the slower main engine gives up against 15 s**, disclosed: in the kind benchmark's setting 23.75 minutes over the line a
  day at 60 s against 20.25 at 15 s (up 17.3%, LOSS against 15 s by the key; still 12.0% fewer than native's 27.0, GAIN); in the
  cloud's setting 2.6% more energy per core-hour (power given). Against native the pods waiting for a place read LOSS at every
  beat, the main engine's included: the engine's, on the next version's list (`docs/CHANGE_CONTROL.md`).
- **The model gate against omni-v16** (`results/model_gate/V17_VS_V16.md`): Every model that sets its own period reads identical to omni-v16 on every gauge and every seed (9 models and the verdict); as shipped, omni-v17 at its 60 s against omni-v16 at its 15 s, every gauge reads STEADY; no LOSS against omni-v16.
- **The monitors scale with the beat**: the exporter serves `omni_heartbeat_seconds` (the median spacing of the last eleven
  decisions, `tools/omni_exporter.py`); the governor's Grafana screen shows the beat and counts the time since the last decision
  in beats (`deploy/grafana/omni-compass.json`, eighteen panels); the staleness alert fires after three beats at any setting
  (`deploy/prometheus/omni-compass-rules.yaml`: 180 s at 60 s, 45 s at 15 s, 360 s at 120 s); the control panel carries the dial
  as a button (`POST /v1/beat`, 5 to 120 s, one console button a stop; `tools/omni_control.py`, `omni_control_beat_seconds`);
  the live engine page carries "The heartbeat dial" (section 1j, every beat beside native from the ladder), read by the Live Engine
  Manual (section 7.4); the receipts record each arm's beat and a three-run table names the beat its compass arm ran at
  (`tools/live_reps.py`, `tools/confirm_abc.py`).
- **The real runs**: `docs/PACE_PREREGISTRATION.md`, amendment 3, written before any omni-v17 run: eight arms in every repetition
  (native; Omni-Compass at 60 s; and at 5, 15, 30, 75, 90 and 120 s), three runs of 10 repetitions on GitHub's own machines, each
  beat read against native and against 60 s; a repetition's job may run four hours. The Kubernetes preregistration takes its
  amendment of the same day (`docs/K8S_COMPASS_PREREGISTRATION.md`). Every benchmark runs again on omni-v17
  (`scripts/reruns.txt`, the campaign from 17:00 UTC on 23 October); omni-v16's runs stand as its record.
- **One tuned engine, and a tuning bench** (the founder's order of the night of 22 October): every benchmark is the main
  engine at its one factory tune; the live engine page is a live tuning engine, whose every knob, button and monitor turns in
  real time (native alone, Omni-Compass on top, or both), and what it shows at any other setting is the engine's range, never a
  benchmark result; turning any knob can change every metric in any direction, as on any engine. Written into `DISCLOSURES.md`
  section 3, the README, the live page's first box (`#tuningBench`) and all three manuals. The factory tune is chosen by a
  declared rule, formalized in `docs/THE_TUNE.md` and the Owner's Manual section 4.4 and coded in `tools/tune_study.py`
  (`tests/test_tune_study.py`): admissible tunes harm no gauge against native (in a cloud, no rise in the bill); the factory tune stands when no admissible tune searched dominates it; searched on development seeds, read again on untouched ones,
  landed only through the model gate; the claim is non-dominance among the tunes searched, never a global optimum. The first
  search (the beat from 15 to 120 s and the compass's balance point, both settings, seeds 101 to 108) runs in our models and is
  read on its own page in `results/model_gate/` when it finishes. The model's worker passes any governor argument through (`--ctl`).
- **Two findings of the live-engine session, on the next version's list** (`docs/CHANGE_CONTROL.md`, not yet reproduced here):
  the brain's dwell restated in seconds at the fast beats, and the cloud's floor check and warm reserve under `--give-back-only`.
- **Next**: each beat's own combination of the other knobs, in the model first, on development seeds (the founder's words: "you
  might need to click and change and turn certain things to achieve a more optimal state with a different combination of
  buttons"); a combination that reads GAIN with no LOSS at its beat lands as the next version.

## 2026-10-23 (midday): the visual seat's last six closed; main's omni-v16 tables on the page

- **Six monitors that printed over themselves on a phone** (the visual referee's V5 to V10, `docs/engine/CONSENSUS_AUDIT_2026-10-22.md`),
  each fixed in its own drawing and rendered again at 390 and 1280 px:
  - the cluster monitors (5a, 5e): the pods sit inside their machine's box, and a box past what it holds writes its count;
  - the CPU host (5f): the "awaiting its machine" stamp takes its own line under the lane heads;
  - the ring (6a): on a small ring the six gauges are ticks alone and the centre's words fit the circle, OFF in red with the switch off;
  - the seven organisms (4): the three loads stack as three bands;
  - the Azure bill (5a): a narrow bar carries its engine alone, and the reading line names the set, its pairs and its bill;
  - GitHub's runs (1i): one workflow a row, its name above its bar.
- **Main's omni-v16 tables** (Kafka, PostgreSQL's pooler, Redis, MySQL, MongoDB, each as shipped and as a service, landed on main by
  the conductor) are merged into this branch, and the live engine's records are rebuilt from the merged tree: every one of the 39 new
  runs played back from its raw files, each file matching its run's SHA-256 list.
- **The model gate keeps its two engines apart again.** A change of 22 October put the gate's own checkout first on Python's path, so
  a worker meant for the engine that stands imported the candidate's engine; the gate's own check refused it at once (the engine
  imported from the wrong checkout). The gate's checkout is last on the path again, as it was, and only the gate's own process
  formats a reading.
- **Omni-Compass by itself, preregistered** (the founder's order of 23 October; `docs/SOLO_PREREGISTRATION.md`): a third arm beside
  native and Omni-Compass and native, with each muscle's own native controller switched off and Omni-Compass the only controller
  moving the knob. The page says what it switches off and what stays (Kubernetes' scheduler and kubelet), where it is the same arm
  (every service whose native is a setting; every actuator native's own loop drives), that the cloud waits for the founder's word,
  and what is run once the next engine version carries a pod muscle of its own. The model gate takes two settings for it (kind's
  static pool, and by itself on it), read by `tools/solo_study.py`.
- **The sign rule on the benefit sheet and the state of play.** Their one number now wears its own word's sign, as every three-run
  table does: GAIN '+', LOSS '−', STEADY '=', power given '+'. The Redis row's one number read '-0.1% power given'; it reads '+0.1%
  power given'. The modelled organisms' line says each change in its verb ('misses down 0.145 pp', 'power given +0.011%', or
  'energy cut' where the energy fell). The raw values in the result files are unchanged.

## 2026-10-23 (morning): the consensus audit of 22 October, its majors closed; the sweep's table carries the notice

- **The audit** (`docs/engine/CONSENSUS_AUDIT_2026-10-22.md`; the seats' reports line for line in `docs/engine/audit_2026-10-22/`): five
  referee seats read the live engine on omni-v16, one dimension each, none reading another's report first: the mathematics and the
  readings **B**, the underwriting **B−**, the editing **B+**, the structure **B**, the visual layout as rendered **B** (desktop A−, phone
  B−); consensus **B**, no blocker named, 33 distinct majors (38 as counted). Every number the seats traced equals its record, and the
  page renders with no console error and no sideways scroll at either width; what held it at B is what it said about the record and six
  of its drawings at a phone's width. 23 majors are closed below, 3 in part (two wait on the founder's decision on the page's order), 1
  in its sentence, and the six phone overprints (V5 to V10) go in the next push. The grades are the referees' grades of the page they
  read; the next audit grades the page again.
- **The numbers first.** The verdict's keep rates (8c) no longer take a minus from the word before them: the page's word walker signs
  only a number that follows a bare word. An interval that includes zero prints as it lies, whatever the word (`byWordRange`). Failed
  requests read by the key's never-more rule in section 3 and in 5a alike, any rise in a run a LOSS, and both panels say so. The benefit
  board and its tally take each benchmark's newest table whatever its engine, each row naming it, with the Omni index printed beside
  them as a second reading of the same tables and no written explanation of any gap. Every realms word takes the key's floor. The
  start-wait sentence counts Omni-Compass's own tables only.
- **The words that contradicted the record or the key.** The key's own sentence on the sign in iv and in 4 (the number beside a word
  carries the word's sign: GAIN +, LOSS −, STEADY =, power given +), every size and interval printed through the formatters where it is
  made, the Ask panel's rule the same. The title page: every live view runs on omni-v16 and the recorded models name their own engines;
  the tables prove the factory tune of the engine each names (`DISCLOSURES.md` section 3 and both manuals: every published result is the
  factory tune of the engine its table names); the runs played back from raw files are told apart from the tables read as the repository
  holds them; "found in its own models before any real run". The spine is the organism's; power given is blue in section 2 and in
  monitor 11's registry text; a stack is bought two ways and the composition read four; the disclosures name the build's engine; 5f
  states what the chip receipts will measure and no result; 1g names a knob only where the recorded cause is the governor's; 1d answers
  a LOSS row only from the same setting's tables.
- **The structure.** A part head for 10; every contents entry is its heading's text, held by `tests/test_live_toc.py`; the quick-start
  guide under 6a; the registry in the page's order with each monitor's number; iii and iv fold to a lead paragraph each (18,231 visible
  characters before the wall with the folds closed, against 32,277 open); the Omni index is the first line of the executive summary. The
  structure seat's proposed order (the wall first) and its cost, and the cheaper cut of the front matter, stand in the audit for the
  founder's decision.
- **The visual seat's first four.** The title page's two lede paragraphs each take their own row (they printed over each other on the
  first screen); power given wears its own class in the prose, blue, and blue on the market map, the quote board and the legends; the
  last places the sign rule missed (1g's cells, iv's ranges, 5f's cells, the quote board, the radar) print the word's sign on every
  number; the phase planes stack on a phone.
- **Every reader of a three-run table reads both signs.** The tables written before the sign rule carry the gauge's raw direction and
  those after it the word's (STEADY with "="): the live engine's exporter and cell formatters read "=" and both directions, and the
  trading floor draws every judged row in its word's direction whichever way its table was written; the benefit sheet, the index and
  the wiring verdicts read the tables' JSON, never their cells. `tools/confirm_abc.py` keeps the tables' interval shape ("(+33.3 to
  +66.7)"), and its test asserts the word's sign for GAIN, LOSS and STEADY.
- **The referees' reports keep the words of their day.** `tools/layout_check.py` reads `docs/engine/audit_*/` as it reads the history
  and the receipts: a report quotes the page it read.
- **The sweep's table** (`results/model_gate/HEARTBEAT_SWEEP.md`) carries the notice under its title and at its end, written by the tool
  (`tools/heartbeat_sweep.py`), as every model-gate page does. The Live Engine Manual names the audit; all three PDFs are rebuilt; the
  release manifest is regenerated.

## 2026-10-22 (evening, the live engine): the heartbeat sweep on the wall, every beat from 5 to 120 s; main's omni-v16 merged

- **The number beside a word carries the word's sign** (the founder's words of the same night: "If it's a gain, it should be a plus 73
  with the word gain ... that word gain can never have a minus beside the word gain"; the key's rule of 20 October). The heartbeat
  monitor had printed the gauge's raw direction ("−73% GAIN"). The key's formatter (`tools/readings.py` `by_word`, `interval_by_word`)
  now prints every number beside a word with the word's sign (GAIN +, LOSS −, STEADY =, power given +) in the three-run tables,
  the receipts, the model gate, the heartbeat sweep and the live engine's trading floor, index, verdict and heartbeat monitor;
  tables already written stand as the record of their day.
- **The founder's order** ("5, 15, 30, 60 ... Then give me 75 90 And after 90, I want 120 ... Heartbeat sweeps. With buttons in
  my monitor canvas dashboard of that wired mechanism of the heartbeat ... somebody might want to tune it to be something
  different"). The live engine's new monitor, *The heartbeat sweep: every beat the governor can run at* (`beatCv`, section 5c,
  after the heart), has a button for:
  - each beat (5, 10, 15, 20, 30, 60, 75, 90 and 120 s);
  - each setting (on-site, the governor sizing the pool; in the cloud, the machines alone);
  - each engine (omni-v16, the engine that stands; omni-v15, the one before it);
  - each zero line (native, or the same engine at 15 s or at 60 s);
  - each gauge.

  Its tiles give the chosen beat whole. Each gauge's change shows with its 95% interval and its word, together with the engine's
  own processor time, cluster reads and writes a day, and the fast check's rescues (the machines added only after a pod already
  waited). The chart gives the chosen gauge at every beat, and a cursor reads the beats in turn. The registry, the Grafana wall
  (61 panels), the builder's record (`beatsweep`) and the Live Engine Manual (section 12.4) carry it.
- **The record** (`results/model_gate/HEARTBEAT_SWEEP.md` and `.json`, our own model, class S). It is written by
  `tools/heartbeat_sweep.py --table` from its runs (`results/model_gate/HEARTBEAT_SWEEP_RUNS.jsonl`), and
  `tests/test_heartbeat_sweep.py` writes it again from them byte for byte. Its design:
  - Eight seeds of a day at each beat, paired with native and read by the model gate's rule.
  - The sweep carries its own cloud plant, so every engine runs on the same one.
  - A run counts the fast check's rescues from its own audit.

  **What it reads.** On omni-v16 (our own model, class S): on-site every beat reads GAIN against native in pods waiting (GAIN +83.5%
  at 5 to 15 s, +72.9% at 60 s, +57.0% at 120 s), at 5 to 15 s with about 3% more machine-hours (power given +2.9%); a beat slower
  than 60 s waits more than the factory's 15 s (86% to 160% more, LOSS at 90 s) for at most 0.4 points fewer machines than 60 s,
  and the fast check's rescues rise from none at 15 s to 3 a day at 120 s. In the cloud, the machines alone, 5 to 15 s cut the
  machine-hours 1.5% to 1.8% (GAIN) with pods waiting +15% to +17% (LOSS, the engine's, on the next version's list, as
  omni-v16's own pace study found); from 20 s to 120 s the waiting reads STEADY and the cut 0.7% to 1.4%. omni-v15, its rules
  counted in beats, reads the same at 60 s and slower, and in the cloud at 5 to 15 s waits more (+20.5% to +22.2%, LOSS).
- **Main's omni-v16 merged** (digest `5c5502f12b1c0ce4`, landed on main by another session on the founder's words). This branch
  had built the same order in parallel without seeing it. Main's engine is taken whole, and the parallel build's own files are
  reset to main's or removed. Its findings were handed to the work on the next version, through its model gate:
  - the fleet law's dwell restated in seconds;
  - the cloud's order for machines already deleted;
  - the closure law's warm reserve.

  The live page, its builder, its registry and the Live Engine Manual keep this branch's work, with main's version words carried
  in.

## 2026-10-22 (afternoon): the Azure sets back on; the conductor starts runs again; the levers rig at the brain's minutes

- **The founder's answer.** Asked whether the person whose Azure account the login bills agreed to its use, he answered "Yes yes
  yes". The Azure queue's switch, off while the question stood, is on again (`scripts/azure_queue.txt`): the four sets (the
  steady set, the bursts `1 4 1 6 1 9` and `1 6 1 8 1 6`, the real day on 1 to 9; A, then B, then C) on omni-v16, at the tune-down
  with native's cap, each only after Azure's own $0 check passes. The engine, the harness and every other queue are unchanged.
- **The conductor had started nothing since omni-v15's push** (00:45 UTC on 22 October; the last runs it started, at 00:31 UTC,
  were omni-v14's grid). On GitHub it fingerprinted the fetched commit with its own copy of the version tool's scope, written
  before omni-v15 took eight wires (the data stores' five runners, the swarm, MuJoCo, the CPU power runner) into the fingerprint, so
  every commit of omni-v15 and omni-v16 matched no version and each tick said "this checkout runs unknown ... nothing started".
  omni-v15's campaign started no run, and omni-v16's none until this push. The conductor now runs the fetched commit's own
  version tool with that commit's own fingerprints (`scripts/dispatch_grid.py`, `engine`): it reads omni-v16 on main, where its
  old copy read unknown, and a tick that began before an engine landed still reads the fetched commit. The test
  (`tests/test_release_campaign.py`) builds a commit from this checkout's engine, late wires and all, and fails the old code.
  The running conductor fetches its newest code at every tick, so the grid, the reruns and the clouds start within 15 minutes of
  the push. It did: at 13:50 UTC it started the first six reruns (A of the core benchmark, the Kubernetes baseline, full
  controls, levers, observe-only check and CruiseKube), the first grid runs and both cloud checks.
- **The levers check, on the rig omni-v16 left behind.** Its first omni-v16 run (Kubernetes levers A) failed three of its 19
  checks: rightsize never changed the CPU request, and coldstart never parked the idle worker in either idle phase; batch pace,
  containment, cooling and every hand-back passed. The rig ran three, two and three decisions of 5 s per phase. Under omni-v14 each decision was a
  minute of the brain's whatever the period; under omni-v16 every clock counts seconds, so the phases gave the brain 15, 10 and
  15 s, and the two levers that give back wait for the brain's calm, its authority to contract (calm at least 0.5), which comes
  about a minute after it starts on an idle reading. The engine's own brain read on that reading: calm 0.59, 0.82, 0.89 after
  decisions of 60 s (the passing omni-v14 run's cooling setpoints say the same, 23.3, 25.4, 26.0 °C), 0.00, 0.00, 0.08 after
  three of 5 s (the failed run's), 0.59 at the fourth decision of 15 s. A rig fault, not the engine's: in a deployment the
  authority comes after the same minute it took at omni-v15's 60 s. The rig now runs at the default 15 s for the 3, 2 and 3
  minutes its checks were written for, the idle time before cold start in seconds (`scripts/kind_levers.sh`,
  `--coldstart-idle-s 120`); `tests/test_pace_clocks.py` holds both the rig's phases and the minute the authority waits for. The
  failed A stands as the old rig's record; the first block's B and C run on the corrected rig, and a new block runs the levers
  check again, A, B and C (`scripts/reruns.txt`, added 14:30 UTC). Every other rig that runs the governor counts its phases in
  seconds at 15 s, or reads no lever's authority within a few decisions (the scale test records its decisions and hand-back).

## 2026-10-22: omni-v16, the heartbeat at 15 s; every clock of the Kubernetes governor in seconds

- **omni-v16 lands** (`OMNI_V16.json`, digest `5c5502f12b1c0ce4`, 55 files; `docs/OMNI_V16.md`) on two words of the founder's of 22
  October: "Go", on the plan put to him that night (every clock of the governor in seconds, the decision pace read at 60, 15, 10 and
  5 s in our own models, three runs at each pace on GitHub's own machines), and, once the models had read, "15 sec all over heart beat
  fix update code". Who set the 60 s: the first harness, on 26 September, with no reason recorded; native's pod autoscaler checks
  every 15 s. Through omni-v15 several rules still counted decisions, so a shorter period also changed what they meant.
- **The heartbeat is 15 s**: the governor's full decision comes every 15 s by default and its fast checks every 5 s (`--interval 15`,
  `--floor-interval 5`, `omni_controller/controller.py`), in every rig (`scripts/kind_bench.sh`'s `OMNI_INTERVAL`, `kind_paired.sh`,
  `kind_robust.sh`, `kind_full.sh`, `kind_pilot.sh`), every install file (`deploy/install/omni-compass.yaml`,
  `omni-compass-cloud.yaml`, `deploy/controller.yaml`), every cloud set (started through `kind_bench.sh`) and the alert rules'
  staleness bound (three intervals, 45 s). Each run writes its period beside its files (`omni_interval.txt`); the robustness receipts
  read each run at its own and its decision time from the audit's own `decision_ms` (`tools/live_reps.py`); the tables of the runs
  before it are read as they were. A longer period is not a larger cushion: each muscle's cushion is set in seconds by its own
  climb, wobble and reaction time, and a longer period only leaves the governor blind longer (the founder's question of the same
  night, answered in `docs/OMNI_V16.md`).
- **What moved, and nothing else** (every gain, guard, preset and muscle is omni-v15's; 50 of the 55 files are omni-v15's bytes): the
  brain's own minute (`omnicompass/adapter.py` `period_s`: the reading's weight 1 − (1 − 0.339)^k a step with k = period / 60 s, its
  inner time, its dwell and waits, and the machines it adds or removes over the last minute's steps; its C++ twin
  `cpp/src/governor.cpp` identically, equal to the Python at 60, 15, 10 and 5 s and sealed again); the compass's damping, critical
  at the minute, and its smoothing; the edge's window, narrowing, forgetting and wobble per minute (`omnicompass/edge.py` `pace`);
  the additions past the scheduling floor, one step a minute; a command's minute to land; the host's busy share over a minute
  (`omni_controller/capacity.py`); the heat law's minute, one batch job a minute and a quiet deployment's 180 idle seconds
  (`omni_controller/muscles.py`, `--coldstart-idle-s`); the coast per raise; the conveyance every 15 s whichever check falls due
  (`--convey-every-s`; omni-v15 never conveyed at a decision every 5 s); and a loop that keeps its own schedule, a missed slot
  skipped and written in the audit (`behind_s`), never run in a burst (`omni_controller/controller.py`; `tests/test_pace_clocks.py`,
  `tests/test_loop_schedule.py`).
- **Read before it was pushed** (the model gate, class S, `results/model_gate/V16_VS_V15.md`, eight seeds, every model): at 60 s it makes
  exactly omni-v15's decisions (4,578 audit records, none different; every gauge of every model identical); at 15 s every gauge reads
  STEADY against omni-v15 at 15 s and the machines parked fall from 4,212 to 1,782; as shipped (model `cluster_shipped`, omni-v16 at
  its 15 s default against omni-v15 at its 60 s) every gauge reads STEADY: no LOSS. Against native, omni-v16 at 15 s reads two LOSS
  rows in the cloud's setting, the pods waiting for a place (+121.6%) and the 95th percentile (+0.36%), which omni-v15 at 60 s reads
  STEADY only by the seeds' spread (+209.8%, +0.63%).
- **The pace** (`results/model_gate/V16_PACE.md`, omni-v16 alone, a plant that moves every 5 s): against 60 s, no LOSS at any pace in
  either setting; at 15 s the alert minutes fall 14.7% in the kind benchmark's setting (18.4% at 10 and 5 s) and energy per core-hour
  2.6% in the cloud's (GAIN), every other reading STEADY; Omni's own processor 2.7 s an hour at 15 s (1.6 to 1.7 at 60 s, 5.5 at 5 s).
  Against native the pods waiting for a place read LOSS at every pace, the old 60 s default included (in the kind setting about four
  times native's; in the cloud's about twice), and in the cloud's setting at 15 s the 95th percentile (+0.47%) and the alert minutes
  (+2.31%), which read STEADY at 60 s only by the seeds' spread (+0.49%, +1.85%): the engine's, on the next version's list
  (`docs/CHANGE_CONTROL.md`).
- **The real runs** (`docs/PACE_PREREGISTRATION.md`, amendment 2, on main): workflow `benchmark-reps`, five arms in every repetition
  (native; Omni-Compass on top at its heartbeat of 15 s; the same deciding every 60, 10 and 5 s), the reruns' steady scenario, three
  runs of 10 repetitions on GitHub's own machines at no cost. They read the heartbeat the founder set; a LOSS at 15 s there is
  root-caused and fixed in the next version.
- **Found on the way and fixed**: the seal's engine-runs twin differs from the Python by one rounding step (3.3 × 10⁻¹⁶ in 65 of 100
  runs) under Python 3.11 and matches it to the bit under 3.12, whose compensated `sum` the C++ follows: the seal is written under
  3.12, as GitHub runs it (the base commit reads the same, so it was never this version's). The kind rig loads busybox from the
  runner's own copy (a repetition's arms had failed Docker Hub's pull after 300 s), keeps the pre-pull's evidence when it fails,
  records the host's free memory every 5 s, and the runner's own agent is kept out of the kernel's memory killer's reach (a
  repetition had lost its runner 64 minutes in). Two tests written for one decision a minute (`tests/test_convey.py`,
  `tests/test_muscles_levers.py`) now name the 60 s and 15 s they were written at.
- **Azure held**: the Azure queue's switch is off (`scripts/azure_queue.txt`) until the founder confirms that the account the
  Azure login bills agreed to it (he said the login in use may be another person's account; a key bills only its own account).
  Google and Amazon stay behind their own $0 checks, as before.
- Every benchmark runs again on omni-v16 from 07:30 UTC on 22 October (the conductor started none of its runs, and none of omni-v15's,
  until its engine check was fixed that afternoon: the entry above).

## 2026-10-22 (night): Azure behind its own $0 check; every Azure login reads the key's shape first

- **The fault.** For a while on the night of 21 October the stored `AZURE_CREDENTIALS` held a text that is not the JSON block
  Azure's login takes (`docs/AZURE_SETUP.md`, section 3): the scheduled collect of the detached big organisms failed at the login
  at 23:37 UTC (run 39694622506); by 00:00 UTC the block was whole again (the omni-v11 steady set's 56th repetition, run
  39236324280, logged in at 00:00:41). Azure's sets had no check before them: a set that fails at the login counts as started,
  so an Azure set started inside such a window would have spent its A, B or C on it, which the founder's order of 18 October
  forbids. And Azure's own login step, refusing the text, quoted its first characters on the run's page, a public page.
- **The fix.** The conductor starts an Azure set only after Azure's newest $0 check passed, as Google's and Amazon's
  (`scripts/dispatch_grid.py`, `CHECKS`); `cloud-check azure` (`.github/workflows/cloud-check.yml`) reads the key's shape
  (`tools/cloud_key_check.py azure`: the four fields Azure's login reads, never a character of the key; a client secret's value
  alone, an identifier alone, a piece, a cut, each named), logs in, reads the subscription's state and runs the sets' pre-flight
  (`scripts/azure_capacity.py preflight`: the machine offered and every allowance able to hold the fleet; capacity another run
  holds now is no refusal; nothing waits, nothing is built). Every Azure login in every workflow now has the shape check
  before it, skipped exactly when the login is (`tests/test_cloud_check.py` fails a push that leaves one without it). The
  detached start job's checkout carried `scripts/` only while its receipt step, added on 15 October, reads
  `tools/omni_version.py` and the engine: its next start would have failed there; it now checks out the tree but the raw runs.
- **What the founder does**: nothing now; the key is whole again. If it is ever stored in another form, the check names it at no
  cost and `docs/AZURE_SETUP.md`, section 7 (the Operator's Manual's appendix F) gives the steps, click by click.

## 2026-10-21 (night): the consensus audit's nineteen majors closed

The five referees' consensus audit (`docs/engine/CONSENSUS_AUDIT_2026-10-21.md`, consensus A−, no blocker) named nineteen majors,
every one a sentence, a count or a drawing. Each is closed here, in the page, its exporter, its builder and the three manuals:

- **The counts.** The executive summary counts the tables of Omni-Compass against its native (55) apart from the orchestrators' own
  cost (30 four-ways tables in which Omni-Compass is in neither arm or on the other side), and says which engines the tables stand
  on. The 0.5% floor of 20 October reads every judged word (GAIN, LOSS and power given), in the tables, the models' live judges, the
  cloud's tally and the exporter (`docs/engine/export_scenarios.py`, from `tools/readings.py SIZE_FLOOR`). A model gauge with one
  value a run has no interval: the Linux host's pod start wait and 95th percentile are shown, not judged. The appraisal's counts
  (`docs/engine/APPRAISAL.md`) are written by the build from the records at every run (`write_appraisal`), and `--check` fails a
  stale one; its stale sentences now point at them.
- **The mechanism's words.** Section 10 names both laws: the engine's default allocation law, which the page's brain runs, and the
  fleet law the shipped controller runs (its trace in 5e shows ρ* between 0.79 and 0.83). Section iii and the three manuals say what
  the mechanism does: every give-back is tried in its own paired trial; a raise is held inside the muscle's bounds and judged by the
  three-run tables; and do no harm is the aim, with every LOSS row kept, its cause found and the test run again. The builder, its
  workflow, the appraisal and the manual say what the build does with a new engine (it stamps it and rebuilds every record; `--check`
  fails a page whose engine differs), where they had said it "refuses".
- **The LOSS rows' causes.** The two LOSS rows of Omni-Compass against its native that had no cause page (job turnaround under
  Armada on the organism alone; alert minutes under Open Cluster Management) have one: `docs/LOSS_ROWS_UNDER_INVESTIGATION.md`, each
  row's reading, what is known, what is suspected and not yet shown, and what decides it.
- **The words.** The back matter is vi (it read iv); power given is blue everywhere, written once in the key; the organisms are the
  seven and the orchestra the eighth, the whole stack a composition with two arms; the governors run four ways in every repetition;
  LOSS rows are raised in 1d and answered in 1g; our own model is a model, never a simulator; the factory tune is `DISCLOSURES.md`
  section 3; the awaited GPU run is omni-v13's; the benefit board takes omni-v5 and later (three omni-v3 rows go to the road); the
  poster's caption says the ® and "registered 2026" are the artwork's words and the company's statement of record is "filed".
- **The drawing.** The wall keeps every monitor's own shape (letterboxed, never stretched) and draws any monitor not yet drawn
  before it copies it; no canvas type under 11 px; the red of LOSS is legible as text (AA); on a phone a native/Omni-Compass pair
  stacks, native above, at full width; the nested three-run tables stay inside their cell; captions and badges at the page's floor.

## 2026-10-21 (evening): omni-v15, the power cap's request through the line's own clear time; every wire in the fingerprint

- **omni-v15 lands** (`OMNI_V15.json`, digest `0a53cdd7a558f803`, 55 files; `docs/OMNI_V15.md`), under the founder's standing order that
  every fault found is fixed and lands as the next version, told, not asked, and his word of 21 October ("push, push, push on GitHub,
  update, enhanced engine"). The fault, from the next version's list (`docs/CHANGE_CONTROL.md`): on the omni-v11 long run the brain's
  request for the power cap switched between the start limit and the trim at 126 of 350 decisions and turned back at 123 of them, at
  the one threshold on the queue and the state. The fix: the brain (`omnicompass/adapter.py`) trims to demand only while the response
  line has been clean for the governor's own clear time, the flag the Kubernetes governor already declared for its muscles
  (`--slo-clear-s`, 180 s) and the card governor applied outside the brain (3 decisions; it now hands the brain the flag). A breach, or
  a line not yet clean, releases the request in the same decision; no constant is added to the law. On the run's own decisions, kept
  as a fixture with the audits' SHA-256 (`tests/fixtures/robust_long_39173420146_decisions.json`), the recorded request is omni-v14's
  rule decision for decision and the gate leaves 35 moves, 32 reversals and 28% of the travel (`tests/test_cap_band.py`). The C++ twin
  (`cpp/src/governor.cpp`, `Observation.slo_clean`) carries the same rule, proven equal on an observation stream that now carries the
  flag (`tests/test_cpp_governor_parity.py`; `cpp/tools/run_governor.cpp` reads the column when present; `cpp/tools/engine_runs.cpp`
  passes the injection's flag to the brain); the seal is rewritten. A dwell with a glide (three calm decisions, then 0.05 a decision)
  was built first and refused by the model gate: seven small moves for one on the model cluster (149 against 38 in a day on one seed), 25
  limit writes for 16 on the model card at the same travel and 0.17% more energy; it is not in omni-v15.

- **Every wire in the fingerprint** (`tools/omni_version.py`): the data stores' runners (`tools/run_redis.py`, `run_kafka.py`,
  `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py`), `run_swarm.py`, `run_mujoco.py` and `run_cpu_power.py` are inside the scope,
  their bytes as they stood, so no rule can change without the version changing (the gap `docs/CHANGE_CONTROL.md` named since
  omni-v12). A version declared before them is read without those eight wires and only those (any other file its list does
  not name still makes the tree a different engine), and the tool prints a version's own digest and file count.

- **The model gate reads the request's wear and the card** (`tools/model_gate.py`): the cluster models now read the brain's request for
  the power cap over the day (its moves, reversals and travel; wear, a resource held: a fall is a cut, a rise power given), and two
  card models run each checkout's GPU governor on the modelled card of `tools/gpu_physics_sim.py`, written into the gate so both
  engines meet one model (the card whose voltage falls with its clock, and the card near its voltage floor): requests served and not
  served, the 95th and 99th percentiles, energy, peak temperature, and the limit's writes, moves, reversals and travel.
  `results/model_gate/V15_VS_V14.md` is omni-v15's reading against omni-v14 on eight seeds.

- **The kill test reads the 300 s after the kill** (`tools/live_reps.py`, `ROBUST_AFTER_KILL_S`; `tests/test_robust.py`), declared
  before omni-v15's runs in `docs/ROBUSTNESS_PREREGISTRATION.md` ("On omni-v15"): the one tail rise of the omni-v11 kill test came 140
  to 190 s after the kill, past the 120 s window. The omni-v11 kill table stands as read.

- **Every page on omni-v15**: the README, the state of play, `CLAUDE.md`, the three manuals and their PDFs, the live engine page
  (`data-engine`, its words; its records rebuilt by its workflow), the appraisal, the receipts, the limitations, the Lambda and
  whole-system pages, the change-control record and the mechanism-of-action page (the cap rule); `docs/OMNI_V14.md` says when it
  stood. Every benchmark runs again on omni-v15 (`scripts/reruns.txt`, the grid and the cloud sets restarted from 02:30 UTC on
  22 October, a little after the push, so no run started by omni-v14's conductor is counted in its campaign; none started: the
  conductor read omni-v15's commits as no engine until 22 October, afternoon); the GPU's run on Lambda starts from
  `gpu-omni-v15`, one exact commit.

- **The preregistration's lock on the brain, amended on record** (`results/LOCK_AMENDMENTS.json`): `omnicompass/adapter.py` is one
  of the files the first preregistration locks by SHA-256. Its omni-v15 change is recorded with the exact old and new hashes and the
  new program fingerprint; the stack simulator and its benchmark hand the brain no clear flag, so every decision there reads the line
  clean and takes omni-v14's branch, and `verify.py` re-runs the preregistered held-out seeds and the fleet's held-out runs with the
  amended file, which reproduce unchanged. The mechanism's identity (`results/MECHANISM_IDENTITY.json`) is recorded again: its
  observation map, authority law and actuator parts carry the clear flag.

- **The engine's coverage, measured on omni-v15's files** (`docs/ENGINE_COVERAGE.md`): 71% of 9,685 statements run under the
  tests, where omni-v14's read 82% of 6,579. No test was lost: the files that stood before omni-v15 read 82% as they did, and the
  eight runners it took into the fingerprint hold 3,106 statements, 49% run under the unit tests, because each is run whole by
  its own benchmark on GitHub. The page says so itself (`tools/engine_coverage.py`).

## 2026-10-21 (late afternoon): the problem and Omni-Compass's solution at the head of the front matter; every tile of the wall titled

- **The problem and Omni-Compass's solution** (the founder's order of 21 October: "in the beginning we have to state in front
  matter the problem and omnicompasses solution, what the whole tech world is facing, and how omnicompass addresses it"). A new
  first section of the front matter in the live engine page (section iii, `#s-problem`, after the title page; the executive
  summary and key become iv, the contents v, the back matter vi and vii) and in all three manuals (the first chapter after the
  contents), and in short in the README: what the whole industry faces (the International Energy Agency's 415 TWh for the
  world's data centres in 2024 and about 945 TWh by 2030; Lawrence Berkeley National Laboratory's 4.4% of US electricity in 2023
  and 6.7% to 12% by 2028; Cast AI's 8% processor and 20% memory use across the Kubernetes clusters it measured in 2025;
  Flexera's 29% of cloud infrastructure and platform spend wasted, its respondents' own estimate; the Kubernetes autoscaler's
  15-second sync and 5-minute scale-down window), the four costs of loops tuned alone (reaction latency, static
  over-provisioning, uncoordinated coupling, the gaps closed by hand), Omni-Compass's solution, a table of how it addresses each
  cost and how each is judged, what it does not do and how it is held to account. The outside figures are quoted for scale,
  each source named: their authors' own, none measured or checked by us, none a result of Omni-Compass. The Owner's and the
  Operator's Introductions no longer repeat the problem and open on the idea (The Idea and the Promise; The Idea and What This
  Manual Covers). The Live Engine Manual's chapter 2 and Appendix A carry the page's new numbering; Appendix L names the title
  page ii (it had printed iii, the executive summary's number) and reads the section's prose.
- **The printed books' section numbers.** All three PDFs printed every section of every chapter under a number shifted from
  the book's own: the Operator's Manual's 1.1 (Always on top of a native controller) was printed 1.6, and in the Live Engine
  Manual all 176 numbered headings were off, while every reference in the text kept the right number, so "section 4.1" led
  to no heading of that number. The book builder numbers every heading once to learn the labels and again to print them, and
  the second pass counted on from the first; it now starts each chapter again from its first section
  (`docs/book/build_book.py`). `docs/book/nav_check.py` now reads every numbered heading of the PDF against the number the
  book's one-file text gives it and fails a book where one differs. The three manuals rebuilt.
- **A table with tall rows no longer prints its header twice on one page.** Split at a row's end, the rest of such a table
  was started lower on the same page under its header again; the book builder now splits the tall row inside it when a
  row's end would leave more than four lines of the page empty (`BookTable`, `docs/book/build_book.py`). The new section's
  table has three columns, so no word in it is broken across a line.
- **The wall's tile titles in capital letters** (the founder's order of 21 October, evening); the wall's words and the Live Engine
  Manual (4.1) say so.
- **The owner's two illustrations beside the title, both live** (the founder's order of 21 October, evening): the stacks
  Omni-Compass sits on top of as he pictures them on top, the unified control authority under it, in one stack in the title page's
  right column (under the title on a phone). Over each the engine draws its own marks and nothing of the picture's own: a ring at
  every decision of the live engine; on the rose two hands, native's (amber, the longer) and Omni-Compass's (blue), each at the
  mean place of that side's muscles in their bands, calm at north, the line at south; on the control core a glow that grows with
  the settings Omni-Compass wrote in that decision; under each, that decision's counts; OFF at the master switch, Omni-Compass's
  marks take native's colour. Each caption says it is an illustration, not a result, that the marks in it belong to their owners
  with no endorsement stated or implied, and the repository's legal line stays "filed in the USA". The Live Engine Manual (2.1)
  says so; the overlays carry no id, so the monitors keep their numbers.
- **Every tile of the monitor wall carries its title** (the founder's order of 21 October: "every monitor in the wall ... its title
  alongside its number in its top"): at the top of each tile its number and its title, what the monitor shows, wrapped to two lines
  on a desktop and four on a phone, never cut short, and under them its section and its state (live, replay, from the records, a
  model, or awaiting its run); the monitor's picture under its head. The wall's own words and the Live Engine Manual (4.1) say so.
- **The notice at the foot of every page of the three manuals** printed the word simulation with a small s, against the founder's
  wording of 20 October (Simulation, as the LICENSE writes it): the book builder had split the line in two pieces, so the
  notice check never read it whole. One piece now, a capital S, and the Operator's, the Owner's and the Live Engine Manual rebuilt.

## 2026-10-21 (afternoon): every monitor moving and wired, its code to its Python to its C++; every dashboard on its section

- **Every monitor moves** (the founder's order of 21 October: "I don't see some grids, charts, diagrams moving with real time"). A
  photograph of every monitor 2.5 s apart had found 17 that did not change: records with nothing to scan, lines that took one point
  a decision too small to see. Now a ring opens at the head of every live line as each decision lands, with the line's newest
  value printed beside it (the scoreboard strip, the console, the controller's strip, the chip and the host, the official run, the
  clouds' modelled lanes, the brain's wells and its bath, the first mode); every record monitor has a reading cursor that walks it
  one row a decision and names the row it holds (GitHub's runs, the seven organisms, all 1,107 muscles, the grid, the Azure sets,
  the orchestrators' road, the whole organism's pieces); every GitHub reading prints its age, counted every second; the modes mark
  each decision's own motion on every bar; and the proof monitor checks the Python's set again without end, one run about twice a
  second, the run boxed on all three lanes. The same photograph now finds all 60 moving.
- **Every monitor's wiring** under it and in the monitor list (`docs/engine/monitors.json`, `wire`): the page's own code, the Python
  it ports or reads, the C++ twin or why there is none, the checks that hold them equal, each file linked at the build's commit, and
  how it moves. `tests/test_live_monitors.py` holds every name to the page's script and every file to the repository. The registry's
  words were read against every canvas and corrected where they named something else (the body parts on the band, the brain's S
  and B, the pipeline, the heart, the candles, the heat map, the bars, the telemetry strip, the controller's strip, the strip, the
  console, the organisms); the tensor lab's six monitors and the cloud setting's two now say replay, as they play records.
- **The motion meter**: the page photographs every monitor in view once a second, as the viewer sees it, and says on its badge and
  in its row of the list whether it moved; a monitor off screen rests and keeps what it did when last in view. Scrolled once top to
  bottom: 60 of 60 seen, 60 moving.
- **The scale-out grid's monitor** drew the newest grid file, omni-v5's, whose squares are all empty; it now draws the engine that
  stands' own campaign as GitHub runs it (each square's runs started and measured), the road on its button.
- **Two closing tags**: one too many after the register's panel ended section 4 early and left the scale-out grid and every section
  from 5 on outside the page's frame (full width on a wide screen, no section of their own for the grid's badge); one missing after
  the benefit board nested the next three panels inside it. Both repaired; a test now walks every section's tags.
- **Every dashboard on its section**: the Grafana wall carries a row for each section of the page, its panels under it, numbered as
  the page numbers its monitors, each describing its wiring. A canvas text that fits is drawn whole, its ellipsis only where it is cut.
- **The official-run playback, lined up with the Python's scorer** (`docs/engine/export_runs.py`). The page scores every repetition with
  the repository's own scorer (`tools/live_reps.py`) and checks it against the run's own summary; for the three governors that run a
  group of two clusters (Armada, Karmada, Open Cluster Management) it disagreed by 51% to 68%: the scorer was handed the repetition's
  files laid flat, so a member cluster's capture overwrote the group's own and the page counted one cluster's machines, node-hours,
  energy and writes. Every file now keeps its place in the folder: every run agrees to about 1e-16. And each of a governor's five
  four-ways tables had replayed the same two arms (the orchestrator as shipped and Omni-Compass on top of it); each now plays its
  own two arms, named on the lanes, the candles, the heat map and the repetition's table, with Omni-Compass's colour only on an arm
  that carries it.

## 2026-10-21 (midday): the trading floor; the Grafana wall in the page's order; the owner's illustration

- **The trading floor** on the benefit board (the founder's order of 21 October, after a broker's wall of screens): every three-run
  table on the page as a market map (a squarified treemap grouped by stack, each tile's area the gauges its table judged and its
  colour its reading, an orchestrator's own cost grey and dashed) and as a quote board (a quote a table: its ticker and engine, the
  gauge that moved most, that gauge in runs A, B and C as a candle of its 95% interval and value, its rows counted by word, a tape
  of every headline), two registered monitors with their record on pointing; a reading cursor walks the map. Every figure is the
  table's own. The monitors after them are numbered two higher: the numbers stay the order of appearance.
- **The Grafana wall in the page's order** (`docs/engine/export_grafana.py`): its panels had been numbered in the registry's order
  (its panel 2 was the page's monitor 4); every panel now carries its monitor's number on the page and the panels run left to right.
- **The owner's illustration** beside the title on a desktop and under it on a phone (`docs/book/plates/unified_control_authority.webp`,
  kept with the plates), captioned as an illustration, not a result.

## 2026-10-21: the Python's 500 runs through the C++ harness to the last bit; the verdict in C++; section 10b on the live engine

- **The poster on the live engine's title page** (the founder's order of 21 October): the owner's poster of the Omni-Compass, the
  stacks and the software it is built to sit on top of by family, now stands at the top of the title page's right column, with the
  Omni-Compass as its owner pictures it under it (on a phone both sit under the title). Each is captioned an illustration, not a
  result; the poster's caption says the names and marks on it belong to their owners and claim no endorsement, and that the legal
  standing is as the notice states. The plate is kept with the others (`docs/book/plates/omni_compass_poster.webp`); the Live
  Engine Manual's front matter says so. Rendered in headless Chromium at 1,400 and 420 pixels wide before the push: no page error.

- **Alignment sweep, referee level** (the founder's order of 21 October, "fix, fix, align"): the Live Engine Manual named omni-v13
  as the engine the page is built on in four places and listed the page's section 10 without its 10a and 10b (now omni-v14, with
  both); the README gave the Operator's and Owner's books at 496 and 1,249 pages (now 506 and 1,470, as built) and wrote the
  license phrase in mixed case (now as the notice writes it); the reading page named only `V10_` and `V11_` tables; a retired
  word stood in `docs/LIMITATIONS.md` (a swarm draw "worse": it read LOSS), a "confirmed" in `docs/FORMAL_V5.md` (cards checked on
  untouched seeds) and in `docs/LAMBDA_SETUP.md` (a give-back acknowledged by Lambda), a "worse" in `CLAUDE.md`, and
  `DISCLOSURES.md` naming omni-v12 for the card's rerun on Lambda (omni-v14). Every count
  on the front pages read against its source: 1,107 muscles in 70 families, 12 Python/C++ twins, 50 and 77 figures, the
  index's +4.3% and +11.9%, the engine omni-v14 (digest `7afba44615fcff8f`, 47 files); all agree.

- **The Problem and the Answer, first** (the founder's order of 21 October): the README and all three manuals now open their
  front matter with what every stack faces (capacity held idle, late reaction, loops at cross purposes, demand outrunning the
  power and hardware that can be built) and what Omni-Compass does about it (a supervisory governor on top of the native
  controllers, never replacing them), where the proof is, what is not claimed and what is protected. The book builder prints it
  first, before the Foreword; the three PDFs are rebuilt.

- **The live engine's record check, read on the same commits as the build** (`docs/engine/build_live_engine.py`): the check that
  every record on the page is the repository's own run printed "differs: runs" on GitHub's builds of 21 October (05:15 and after),
  and the step went on, because the check's output was piped into the summary without `pipefail`; the workflow's bash with
  `pipefail` (from the live engine branch) now stops the page there. The cause: the build read each run's serial number (its full
  commit, where git knows it) before its GitHub ledger fetched the commits the shallow checkout lacked, and the check read it after.
  The build now reads GitHub first, so the build and its check read the records on the same commits; a check that still finds a
  difference prints the first field that differs.
- **The compass law's parity test reaches its "never take back while it climbs" line**: its random laws never drew a negative gain,
  so that line never decided an answer and a C++ law without it passed unseen (the negative control said so). 101 laws whose damping
  gain takes either sign, fed climbing readings, now run beside the 300 random ones; the twin stays identical, the mutant is caught.

- **The verdict in C++** (`cpp/src/verdict.cpp`, `cpp/include/omnicompass/verdict.hpp`, the tool `oc_verdict`): a line-by-line twin of
  `omnicompass/verdict.py` (the median, the log costs' mean and variance, Welch's interval, the trial's phases, both judges, the
  stepwise reference), with the Python's own `sum()` (Neumaier's compensated sum, as CPython 3.12 adds floats) and its `round()`.
  `tests/test_cpp_verdict_parity.py` runs 300 random verdicts (122,538 answers: trials allowed GAIN and STEADY, refused LOSS and past
  the allowance, abandoned for calm and for work, the median judge) through both: every answer identical. `verify.py` runs it and
  a negative control (a C++ verdict that allows a step read as a LOSS must be caught, and is).
- **The Python's runs through the C++ harness, to the last bit**: the C++ harness (`cpp/tools/engine_runs.cpp`, `oc_engine_runs`;
  the Python's draws from the jump generator are its input, `tools/engine_runs.py` injection(); the entry below) now runs on the
  sealed C++ twins of the compass law and of the verdict and on the C++ governor's own push. With the two fixes below, every one of
  the 500 receipts of GitHub's set 881947045 and of base 20261020 is the Python's to the last bit (it read 2.2e-15 before), one
  digest (`87e77e00bce8e482…` for GitHub's set). `tests/test_cpp_engine_runs_parity.py` holds it on every push (`verify.py`: 500, 50
  with `--quick`). A second C++ driver written the same hour, which drew the seeds itself in C++, agreed bit for bit as well and is
  removed, so the harness is one program with one input: the Python's own draws.
- **Two C++ twins brought to the last bit**: the C++ governor now carries the brain's push (`Directive.push`, the Python's
  `last_push`), and the C++ RK4 step adds (h/6)(k₁ + 2k₂ + 2k₃ + k₄) in `omnicompass/core.py`'s own order of operations; the governor's
  parity on 21,600 directives goes from 1e-15 to 0 (identical), and the 500 fixtures still pass.
- **On the live engine**: section 10 is now 10a (the component specification and its mathematics) and 10b, the C++ twin (`#s-cpp`):
  every twin's parity check, the Python's runs through the C++ harness receipt by receipt (500 of 500 identical, the two digests and
  the GitHub run that made the record), every compass law the page's runs wire, and every muscle of the seven organisms at the
  tune-down through the C++ law (156,480 readings, all identical). Where a record was made before the harness ran with every set,
  the proof monitor's C++ lane (section 1f) reads the harness's run of it at the page's build. The seal holds twelve twins (the
  verdict, and the engine's seeded runs through every twin); Student's t stays in Python only, because the verdict reads the
  fixed 1.96. The Live Engine Manual gains 24.3 and Appendix A's 10a and 10b.

## 2026-10-21 (morning): the live engine front to back as the founder reads it; every monitor drawn; the Python's runs through the C++

- **The front order** (the founder's order of 21 October): the title page first, then the executive summary and the reading key, then
  the Engine table of contents (iv), then the monitor wall; the contents carry no bullets and no dotted leaders: part 1 is lettered
  1a to 1i, one section for each of its panels (1a the control panel and the kill switch, 1b the wall, 1c the monitor list, 1d the
  status board, 1e the master switch's wiring, 1f the Python's runs, 1g every LOSS row, 1h the golden signals, the event log and the
  metrics, 1i the pipeline), each with its controls line and summary, every in-page reference moved with it.
- **The wall read left to right** (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, `docs/engine/monitors.json`): monitors numbered 1
  upward in their order of appearance and laid out left to right, then the next row; the right-to-left mode and its button removed.
  Two monitors that sit side by side in their section (native beside Omni-Compass) sit side by side on the wall and never split
  across two rows, and on the page the pairs stay side by side at every width, a phone included, their canvases level.
- **Every monitor drawn**: the wall redrew a resting monitor through code that refused to draw off screen, so monitors 2 to 7 and 22
  stayed stale or blank until scrolled to; every monitor is now drawn by its own code as the page opens (about 50 ms for all 58)
  and in turn while the wall is in view. The proof monitor's runs start on their own; Google's and Amazon's bill monitors show the
  mechanism every cloud set runs, live on the cloud setting's model (class S, never their bill) until their first set lands; the
  data pipeline is drawn whole on its own canvas at every width.
- **The Python's runs through the C++ harness** (`cpp/tools/engine_runs.cpp`, `oc_engine_runs`): the Python writes every draw of every
  run (the injection); the C++ program reads it, puts the mechanism on through the engine's C++ twins (the governor's sense,
  assimilation and RK4; the nervous system's grants; the compass law and the verdict's interval rule as the page carries them) and
  writes every receipt. On GitHub's set of 21 October (base 881947045) all 500 agree to 2.2e-15 and the digests are one
  (87e77e00bce8e482…). `engine-runs.yml` builds it and records the C++ digest, the run-by-run differences and the digest of the draws
  in every set; `verify.py` runs it on every push; the proof monitor (1f) reads every run three ways, the Python, the C++ and the
  page, one digest each.
- **The Live Engine Manual realigned**: the front order, part 1's sections, the wall's direction, the pairs, the three-way proof and
  the cloud and pipeline monitors; Appendix A rebuilt from the page's own contents (its numbers had kept an older order).

## 2026-10-21: the C++ twin of the compass law; the Python's runs fed through the C++ on the live engine; the wall-first page on main

- **The compass law and the two-way plug in C++** (`cpp/src/compass_law.cpp`, `cpp/include/omnicompass/compass_law.hpp`, the tool
  `oc_compass_law`): a line-by-line twin of `omnicompass/compass_law.py` (Band, CompassLaw, Plug), the one law every muscle runs at
  the tune-down and every live controller runs on its service. `tests/test_cpp_compass_law_parity.py` runs 300 random laws and
  plugs through both (readings past the wall and below calm, the band moved between readings, writes in and out of the cover,
  another writer moving the lever, restores): every one of 29,876 answers identical to the last bit. `verify.py` builds it, runs
  it, and runs a negative control (a C++ law that takes back while the reading climbs must be caught, and is). The seal holds
  ten Python/C++ twins (`results/SEAL.json`, `tools/seal.py`), and its list of what runs in Python only now names the max of
  every organism (`realms/compass_arm_v5.py`), the organisms' body and plants, the edge, and the verdict with its Student t.
- **The live engine's section 10b, the C++ twin** (`#s-cpp`, `docs/engine/export_cpp_twins.py`, the record `cpptwin`): on every
  rebuild the C++ is compiled where the page is built; every twin's parity check runs; every compass law the page's own runs
  wire is recorded as it runs (the file that wired it, each reading with the band and push as they stood) and fed through the
  C++ law and the Python again; and the seven organisms run at the tune-down on the climb, every muscle's law fed through the
  C++ the same way. On the first build every number is identical: ten parity checks, and 156,480 readings of the seven
  organisms' muscles (the tower's 239 muscles with a lever at the tune-down among them). A box finds any muscle by its id. At
  the max the edge and the bone decide each muscle, with no C++ twin yet; the section says so and lists them.
- **The wall-first live page is on main**: the branch that built it (the monitor wall and control panel first, the benefit board,
  the whole organism every way it is bought, the evidence from the cloud down to the chip, the Python's 500 runs from the jump
  generator replayed in the page) is merged into the omni-v14 landing, with the notice as the LICENSE writes it ("Evaluation and
  Simulation use only") on every file. The Live Engine Manual's Appendix A, its anchors and its chapter 24 follow the page.

## 2026-10-21: the live engine in the founder's order, every monitor numbered and knobbed, the Python's runs in the page, the third manual

- **The live engine's order** (the founder's orders of 20 October): the table of contents first, named "Engine table of contents",
  under the one line of the notice; the front matter (the title page, the reading key); then 1 the monitor wall and the control
  panel, 2 the benefit board, 3 the whole organism, then the whole down to the smallest part (4 the measured effect in full, 5 the
  evidence by stack from the cloud down to the chip, 6 the organism, 7 the console, 8 the brain, 9 the failure modes, 10 the
  components, 11 the page's rendering); every badge, part head and in-page reference renumbered; the contents name every
  section's monitors.
- **Every monitor numbered, on the wall, with its own knobs and its feed** (`docs/engine/monitors.json`): 58 monitors, numbered in
  their order on the page, the wall reading them right to left and down; every monitor carries the kill switch, the console's
  knobs where it is live and its own buttons where it replays; the inventory names each one's evidence class, state, the
  open-source exporter and Prometheus series that would carry it on a running system, and what is still awaiting its run; the
  whole wall as a Grafana dashboard (`docs/engine/export_grafana.py`, `deploy/grafana/omni-compass-wall.json`). New monitors: the
  GPU card's one metered run replayed second by second (class P, the replaced controller's record), the CPU host on the harness's
  own modelled machine until its machine (class S), an 8-card node awaiting `scripts/gpu_8card.sh`, the bill on Azure, Google
  Cloud and Amazon with each gate's own reason, GitHub's pipeline, the nine organisms, every muscle of the catalog, the grid, the
  Python's runs reproduced in the page and the Python's 500 scenarios a seed replayed with every trace hash. The tensor and
  service-level monitors are on the wall.
- **The kill switch's words** (the founder's order): ON green while Omni-Compass governs; engaged, the switch red and OFF white;
  it stands in the control panel, in the contents, at every section's head and in every monitor's knobs, one press everywhere.
  Each muscle of the organism carries its own switch: one muscle handed back to native, the rest under Omni-Compass.
- **The Python's runs in the page** (`tools/engine_runs.py`): N runs from a base seed (seed_k = base + k·0x9E3779B9 mod 2³²,
  mulberry32, the page's own generator in the Python bit for bit), each through 288 decisions of the brain (RK4), 80 steps of the
  compass law and one give-back trial; one SHA-256 digest of the receipts. The page runs the Python's 500 again at a button and
  matches every receipt and the digest (`d4f6586b…`); a new base runs in the page with the one Python command that runs the
  same set; the receipts print and download. `tests/test_engine_runs.py`, `tests/test_live_monitors.py`.
- **The whole organism every way it is bought** (`docs/engine/export_whole.py`): on-site bare metal, through the cloud (three
  pieces and two), in the device, as a service; the cloud's back end disclosed (`DISCLOSURES.md` section 9): a tenant cannot meter
  the provider's bare metal; the cloud piece is the bill and the machines the provider meters; the bare-metal piece is gauged on
  hardware we meter and carried to the provider's only as a modelled factor.
- **One third manual**: main's Live Engine Manual (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` and `.pdf`, built with the other
  two by `docs/book/build_book.py --live`) is the third book; this branch's page-generated text became its last appendix,
  Appendix L, the page word for word (`docs/engine/PAGE_WORD_FOR_WORD.md`, written from the page by
  `docs/book/build_live_manual.py` at every build): every section, every monitor under its number with its evidence class,
  state, feed and knobs, every knob and every LOSS row. The book was realigned to the page as it stands: the page's section
  numbers (the benefit board is section 2, every later section one on), Part III in the page's order (the benefit board, then
  the whole organism, now every way a stack is bought: on site, through the cloud, in the device, as a service), the numbered
  wall and its control panel, the 8-card node, the muscle's own switch on the page beside the next version's live switch per
  muscle on a running engine, and six references to other documents that a blind replacement had turned into the page's.
  The control panel downloads all three manuals.
- **The Python's runs linked to GitHub** (the founder's order of 21 October): `.github/workflows/engine-runs.yml` runs another set
  from the jump generator (500 by default, a new base each time) on every push that changes the live engine's page or the Python's
  runs, on a working branch as on main, and on every dispatch; runs the live engine's own code on every run of it in node
  (`tools/engine_runs.py --verify --all`), and commits the record with the GitHub run that made it (its id, address and commit);
  the page reads the newest record by its time and names that run beside the digest, and on main the job starts the page's
  rebuild itself (a commit made with GitHub's own token starts no workflow; a dispatch does). Dispatchable once the workflow is on main (GitHub starts a dispatch only from the default branch's list).
- **Simulation with a capital S** in the one notice (`tools/legal.py`), written on every file but the engine's fingerprinted ones,
  which take it with the next version; the workflows' embedded legal bundles re-written to match.
- **A newer engine's table stands only once its three runs share a reading** (`tools/readings.py`, `landed`): the three
  omni-v12 YCSB runs on MongoDB each failed partway, so their table holds no workload in all three; the benefit sheet, the Omni
  index, the levels page, the power page and the live engine took it as MongoDB's result and the benchmark fell off all of
  them. Each now reads the one rule: omni-v11's table stands, named as omni-v11's (+0.1% GAIN), until omni-v12's three runs
  land. `tests/test_readings.py`.
- **MongoDB's runs on GitHub's new machine** (`docs/YCSB_PREREGISTRATION.md`, amendment 5): GitHub's ubuntu-24.04 image of 18
  October runs Linux 7.0.0, and MongoDB 8.0 refuses or fails to start on Linux 6.19 to 7.0.13 (MongoDB's SERVER-121912); every
  failed job of the three omni-v12 runs (9 of 15) ran on that image and every passing job on the image before it. The workload
  jobs now run on GitHub's ubuntu-22.04 machine (Linux 6.8, the same 4 cores and 16 GB); the setup stops at once with the
  kernel, the server's status and its journal when the server does not answer, and every run's files carry the kernel, the
  release, the runner image and the server's journal; main's rig change of the same night (the server's journal in every
  run, a second restart before a run stops) is kept beside it. Every set runs on this machine in the omni-v13 campaign.
- **Main's red checks fixed here**: verify failed on main because `docs/LEVELS.md` and the state of play's standing block
  were not rebuilt after the twelve omni-v12 service tables landed (rebuilt); the security scan failed on Pillow 12.3.0's eight
  published advisories (Pillow 13.0.0 in the lock with every file's SHA-256, the bill of materials rewritten; matplotlib's
  charts and reportlab's PDFs checked on it). The notice check now refuses the lower-case wording, so a table a bot writes
  with the older notice fails until `tools/legal.py --fix` rewrites it.
- **GitHub**: the branch's verify failed only on the release manifest (hashed pages changed); the manifest and the receipt are
  regenerated with this change. Azure's set to the paid cap runs (repetition 31 of 100 at 20:13 UTC); Google's gate holds on a key
  stored short (595 characters, not the key file); Amazon's on the Free plan (the organization's policy denies every machine
  read). Both say so in their own words on the bill monitors.

## 2026-10-21: omni-v14 lands (a knob for every muscle; the operator's commands without a shell)

- **omni-v14** (`OMNI_V14.json`, digest `7afba44615fcff8f`, 47 files; `docs/OMNI_V14.md`), the founder's orders "knobs on every
  monitor, to turn off and on ... a muscle" (20 October) and "tune the engine" (21 October): omni-v13 with two changes in the
  Kubernetes governor (`omni_controller/controller.py`, `omni_controller/muscles.py`); the other 45 engine files are omni-v13's
  bytes. (1) `--native MUSCLE[,...]` (or `OMNI_NATIVE`) leaves any of eleven muscles where native runs it, never written, an
  unknown name refused at the start; the control panel carries it as `POST /v1/muscle`, every press audited, passed through
  native like a dial press (`tools/omni_control.py`). (2) The operator's own commands (the
  site power reading, a muscle's read command, a wall meter's) run without a shell unless they hold a pipe, a redirect or a
  variable; the static scan's high findings fall from 3 to 2 (`docs/SECURITY_SCAN.md`). The model gate against omni-v13 (`results/model_gate/V14_VS_V13.md`, eight seeds, every model, the batch pods listed as a cluster lists them) read every gauge identical, and the verdict model identical: no LOSS. Tests:
  `tests/test_native_muscles.py`, `tests/test_operator_cmd.py`. The commands without a shell come off the next version's list
  (`docs/CHANGE_CONTROL.md`). **Refused by the gate, not in omni-v14:** a change to the conveyance's reading on a shared host,
  meant to stop the one raise omni-v13 makes early in the batch model's queue (the batch's turnaround +0.05% against native). Three
  rules were tried against omni-v13 on the same eight seeds: no raise on any reading older than another workload's newest pod
  (the web's 95th percentile +6.4%, LOSS); no raise on the reading that opens another workload's run (never fires in the model,
  identical); and that rule with another workload's starting pods added to the reading (the batch back at native's exactly, the
  web's queue native's second by second, but its 95th percentile +6.4% against omni-v13, LOSS: omni-v13's one raise moves when
  every later batch pod finishes, and with it the seconds the web runs on its last pod). All three are kept on the branch
  `v14-convey-study` with their tests; the model's web model is set from a real run's files first (`docs/OMNI_V14.md`, section 3). The model gate's cluster model now starts every run with a fresh audit: its first
  run for omni-v14 read a folder an earlier, interrupted gate had left (a container restart), appended to its half-written
  audits and stopped on the broken line; run again in a fresh folder (`tools/model_gate.py`). The batch model listed a batch pod as Running from the moment it was made; it lists it Pending, not ready, until its container runs (3 s, the rig's own pod start), as a cluster does, the same for both engines. Bookkeeping by `tools/land_engine.py v14`; the three manuals rebuilt; every
  benchmark runs again on omni-v14.

- **The raw sweep leaves no cancelled runs either** (`raw-sweep.yml`): its one-at-a-time rule sat on the whole workflow, so
  every start after a skipped front page queued and was cancelled (five in a quarter hour); the rule sits on its job now, as
  the conductor's does, and a start whose job is skipped never queues.

## 2026-10-21: every check on GitHub green again; OCM's and Armada's four ways; Gödel's three runs started

- **The security scan passes again** (`security-scan.yml`, runs 22 to 24 red). Two causes, both fixed. The audit of the
  pinned dependencies found eight published advisories against Pillow 12.3.0 (the image library matplotlib and reportlab
  bring); `requirements-lock.txt` pins Pillow 13.0.0 with the SHA-256 of each of its 83 files, and `pip-audit` reads no
  known vulnerability. Pillow 13 needs Python 3.11, so `pyproject.toml` asks for 3.11 or newer (verify runs 3.12); Dependabot's
  Pillow updates had failed on the same floor. The static scan found one medium finding no review named, the control panel's
  default kill file under `/tmp/omni-compass` (`tools/omni_control.py`); it is reviewed by name in `tools/security_scan.py`
  (the operator's own machine, one user, set by `--kill-file` or `OMNI_CONTROL_KILL_FILE`) and the page is current. The bill of
  materials and the license list carry Pillow 13.0.0 (`tools/sbom.py`).
- **The conductor no longer leaves cancelled runs behind** (`grid.yml`). Its one-at-a-time rule sat on the whole workflow, so
  every scheduled start and every verify's start queued behind the five-hour conductor and was cancelled by the next one: four
  a day, read as failures. A start now opens with a gate that ends green when another conductor ticks or waits; only the
  successor a conductor starts as it ends (`chained`) waits its turn, and the one-at-a-time rule sits on the ticking job.
- **Open Cluster Management and Armada, four ways, three runs each, on omni-v12** (`results/live/V12_OCM_4W_*.md`,
  `V12_ARMADA_4W_*.md`; `docs/GROUP_PREREGISTRATION.md`, amendment 3). Every row is shown. Omni-Compass on top of Armada
  against Armada as shipped: six GAIN in all three runs (machines in service −40% to −43%, the response time's 95th percentile
  −44% to −45%) and no LOSS. Two LOSS rows on Omni-Compass's side are reported as they stand: the alert minutes on top of OCM
  (+5.7% to +45.5%) and the job turnaround on the group alone under Armada (+5.1% to +9.1%), both the shared-host raise
  omni-v13 fixed; both systems run again on the engine that stands. Armada A carries nine repetitions (a runner lost).
- **The Gödel scheduler's A, B and C started on omni-v13** (runs 39530159191, 39530162328, 39530165147), once its trial on the
  rig that tolerates both control-plane taints of Kubernetes 1.24 ran both arms whole (run 39485277362); they count as the
  campaign's own Gödel entry.

## 2026-10-21: the third manual (the Live Engine Manual); the database rigs leave the server's journal in the record

- **The Live Engine Manual** (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` and `.pdf`, `docs/book/OMNI_COMPASS_LIVE_ENGINE_BOOK.md`;
  `python3 docs/book/build_book.py --live`; the founder's order of 20 October, night: "There shall be three in the end"). The
  third book, for the operator at the dashboard: nothing more than the interpretation of the live engine page
  (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`): how to follow the wall and the master switch (green ON, red the kill switch
  engaged, white OFF), read every gauge and turn every knob of the console, trace any tile to the record it came from, and see
  the mechanism of action native beside Omni-Compass as the monitors show it (the two tickers, the phase plane, the brain's
  state, the verdict); every section of the page in the page's own order, named by title and anchor (its "Engine table of
  contents"); what to do when a tile reads LOSS; what the page does not tell you. 100 pages, 13 figures from the two kits, one
  numbering, every cross-reference and every contents row checked on the built PDF (`docs/book/nav_check.py`). It explains
  neither how the engine is built (the Owner's) nor how it is wired (the Operator's). The Operator's and Owner's Manuals now open
  with "The Three Manuals"; the README, the state of play and `CLAUDE.md` name all three; `tools/readings.py`,
  `tools/unicode_math.py` and `tools/land_engine.py` check the third as they check the other two.
- **The database rigs record why a server did not come back.** The omni-v12 MongoDB runs B and C died at `fresh_server`'s
  wait ("mongod did not come back after the restart") with an empty `mongod.log` and nothing else recorded, so the cause could
  not be read. `tools/run_ycsb.py` and `tools/run_sysbench.py` now wait about five minutes, restart the server once more with its
  `systemctl status` and `journalctl` printed, and stop the run with the journal in the error if it still does not answer;
  `ycsb.yml` and `sysbench.yml` save the unit's journal into every run's files. The runs B and C of MongoDB on omni-v13 will
  carry the cause if it happens again.
- **A three-run table says when a run lacks a workload.** The six table writers (`tools/ycsb_abc.py`, `kafka_abc.py`,
  `redis_abc.py`, `sysbench_abc.py`, `pgbench_abc.py`, `cpu_power_abc.py`) counted every workload at their foot, those a run
  never reached included (the omni-v12 MongoDB table read "across 4 untouched workloads" with none judged); now the foot counts
  only the workloads every run holds, and a warning names each run and what it lacks, with the rule that such a table is not
  read by the index or the benefit sheet until its runs land.

## 2026-10-20 (night): the run storm on GitHub stopped

- **Why runs read cancelled.** The live engine committed its rebuilt page to main, and its own push filter matched that page,
  so it rebuilt itself every seven minutes (ten bot commits between 19:43 and 20:52 UTC). Each of those commits also started
  21 workflows that run only when started by hand (they register on a push and skip it), each skipped run started the front
  page, and each front page started the live engine and the raw sweep, which then cancelled one another in their queues: in
  the hour and a half read, 320 cancelled runs and about 300 skipped ones, no benchmark among them, and every bot commit ran
  the whole verify. Now the live engine's own page is outside its push filter; a front-page run that did not succeed starts
  no rebuild and a skipped run no sweep; and the 21 workflows ignore pushes to main and to the level branches (a dispatch
  needs no push to register a workflow that is on main). `tests/test_workflow_triggers.py` fails a push where a workflow
  would again be started by every push, or the live engine by its own page.
- **omni-v13 landed on GitHub with two faults fixed on the way.** `tests/test_convey.py` still asserted omni-v12's rule (another
  pod on the machine counted by its request, web-2 given 2,800m); omni-v13 counts it by its limit, so the test now expects
  1,800m and a gain of 3.05, the engine unchanged. And the MongoDB benchmark had left the index, the benefit sheet and the
  standing block (26 rows to 25) because the omni-v12 YCSB table was written from two runs that failed (`mongod did not come
  back after the restart`; its runs B and C with no workload) and `tools/omni_index.newest` took the newest table whatever it
  held: it now takes the newest *whole* table (a gauge row, or a workload beside the tuning one), so a table written from
  failed runs is passed over until its runs land (`tests/test_index_newest.py`); MongoDB reads from its omni-v11 table again
  and the index headline is +4.3% (omni-v10, omni-v11 and omni-v12 tables). The YCSB rig's restart fault is the next thing fixed.
- **The cluster recorder takes its first reading before it reads the clock.** `fleet/capture/kube_capture.sh` ended the
  recording when the deadline had passed before any reading, so a clock tick between its start and its first look left an
  empty capture (`tests/test_capture_in_service.py` with `DURATION=0`, once in three whole checks on a loaded machine); the
  deadline now ends a recording only after at least one row.

## 2026-10-20 (evening): Omni v13 stands (no other muscle's room is conveyed)

- **omni-v13** (`OMNI_V13.json`, digest `0088837333c6f0fc`, 47 files; `docs/OMNI_V13.md`): omni-v12 with one fault fixed in the
  Kubernetes governor's conveyance (`omni_controller/muscles.py`), found on KubeRay's rig with the organism alone, whose
  three-run table read two LOSS rows (the queue finished 0.6% to 0.8% later, the web's 99th percentile 4% to 13% higher). The
  29 repetitions' own files, read job by job and pod by pod, name the mechanism (`docs/BATCH_QUEUE_PREREGISTRATION.md`,
  amendment 11, which replaces amendment 10's reading that it was the give-back): in the 16 repetitions whose slower runner
  saturated the kind cores, the web pods' CPU limits were raised to 3,700m at 33 s, on a busy reading that caught the dip as the
  stream's first pods started, and kept through the queue (omni-v7's guard holds a new raise at the host's top, never one
  already given); the batch pods hashed 7.6% slower (63.1 s against 59.2 s) while the web served no faster; no machine was
  parked during a saturated queue. Now, on a shared host at its top (busy at or over 75%) while another workload there has
  room of its own (a pod whose limit is above its request), every limit given goes back to the operator's and is conveyed again
  only under 70%; and every other pod on a machine is counted by its own limit, where omni-v12 counted requests.
  `tests/test_convey_handback.py`; the shared-host tests' coredns carries no room of its own, as kind's does not.
- **The model gate** (`results/model_gate/V13_VS_V12.md`, seeds 1 to 8): a new model, `convey_batch`, sets KubeRay's batch muscle
  beside the serving one on the batch rig's host (the kind nodes on 3 of 4 cores, the governor on the fourth, the stream of
  24 jobs, the kernel's request-weighted share, the pods' measured start lag, the governor's own windowed reading, and the
  batch pods' loss of work under a lifted quota taken from the saturated repetitions themselves). Against omni-v12 no reading is a LOSS in any model: the cluster, verdict and web-only convey models identical to the last digit;
  in `convey_batch` the queue 1.48% sooner, the job turnaround 9.59% shorter and the web's 95th percentile 17.4% lower (GAIN).
  Against native omni-v13 reads the queue identical, and three LOSS rows: the turnaround +0.05% (one raise on the queue's opening
  reading, handed back 15 s later; on the next version's list) and the requests served and alert minutes, which both engines read
  the same way with no batch at all on that 3-core host while the real runs read more requests (the model's web model, on the list).
- **Recorded with it**: the deviations register (71 amendments), the next version's list (`docs/CHANGE_CONTROL.md`: the model's
  web model on the 3-core host, where both engines read fewer requests served than native while the real runs read more after
  the queue), the mechanism identity and the engine coverage measured again on the omni-v13 tree, the Lambda branch
  `gpu-omni-v13`. Every benchmark runs again on omni-v13; omni-v12's tables stand as its record.

## 2026-10-20: the whole system, every layer composed by the product law; Gödel's rig on 1.24; the CPU power harness seeded

- **The whole system** (`results/WHOLE_SYSTEM.md`, `tools/whole_system.py`; the founder's question of 20 October: the cloud is
  the wire, Omni-Compass at both ends, what is the total). Every layer's own table, each measured with the layer under it as
  native runs it (the card, the cluster with its add-ons and governors, the services on it, the cloud's bill), composed by the
  product law Rℓ(g) = oℓ/nℓ or nℓ/oℓ toward the gauge's aim, R(g) = ∏ℓ Rℓ(g), with every interval carried through (the delta
  method on each run's paired interval, the runs pooled by inverse variance, the layers added in the log), read two ways (by
  the index's rule, a STEADY or one-run gauge counting as exactly 1; and with every interval carried), and the separability the
  product assumes tested on the governors' four ways (Omni-Compass on the organism alone against on top of the orchestrator, in
  the same repetitions). The composition is class S over class P and L tables and across engines, said so on the page; the
  stacked run is named as the measurement that would replace it. The modelled organisms and the omni-v3 organisms with the
  cluster inside stand beside the total, never inside it.
- **Gödel's rig** (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 10): on Kubernetes 1.24 the control plane carries two
  taints and the rig's metrics-server pod tolerated one, so it stayed Pending and every arm of Gödel's A, B and C was marked
  invalid before any stream ran; the pod now tolerates both (`scripts/kind_bench.sh`), the same on every rig, and Gödel's three
  runs start again. KubeRay A lost a runner in one repetition and Karmada A lost GitHub's checkout in one; both carry nine.
- **Crane, KubeRay and Karmada, the four ways, three runs each** (`results/live/V12_CRANE_4W_*.md`, `V12_KUBERAY_4W_*.md`,
  `V12_KARMADA_4W_*.md`; register rows 90, 92 and 95; KubeRay A and Karmada A carry nine repetitions, amendment 10). Omni-Compass
  on top of Crane: machines and energy STEADY, the 95th percentile STEADY, and one LOSS, the total pod start wait +54% to +104%, the
  per-pod wait STEADY and the pods started +50% to +67% (power given): the sum of a wait over more pods, read by the key as it
  stands and left for the metric-aims audit to rule on in writing before it is ever re-read. On top of KubeRay: every judged row
  STEADY; KubeRay as shipped against the organism alone: 8 LOSS (the Ray cluster's own cost); Omni-Compass on the organism alone
  on KubeRay's rig: machines −14% to −19% and the mean response −7% to −10% (GAIN) with the queue finished +0.6% to +0.8% and
  the 99th percentile +4% to +13% (LOSS), the engine's to fix in the next version (the give-back trial on a batch queue counts
  the queue's finish and the tail), through the model gate. On top of Karmada: every judged row STEADY; Karmada as shipped against
  the group alone: 6 LOSS (its own cost); Omni-Compass on the group alone against Karmada as shipped: 6 GAIN.
- **The stacked run, preregistered** (`docs/WHOLE_SYSTEM_PREREGISTRATION.md`): Omni-Compass at every layer at once against
  native at every layer, the measurement that replaces the whole-system composition; three stacks in order (the cluster and
  its services on GitHub's machines; the cloud at the tune-down on Azure, the bill metered; the card beside the cluster on
  Lambda, on the founder's word), the gauges, the arms and the reading written before any run; the whole-system page names it.
- **Gödel's three runs started again on the fixed rig, OCM's and Armada's four ways started** (trial, A, B and C each; 20
  October, 19:00 and 19:18 UTC); their ids on the governors page. The Gödel trial then found the same 1.24 taint on the load
  generator, pinned to the control plane with one toleration: every pod the rig pins to the control plane now tolerates both
  taints (`deploy/kind/*.yaml`, `scripts/kind_batch_queue.sh`; amendment 10), and Gödel's trial runs before its A, B and C.
- **The CPU power harness** (`tools/run_cpu_power.py`): the modelled service's spread of service times drew from Python's
  unseeded global generator; verify's run of its test read "0 notches allowed" once and passed when run again. Every worker's
  spread is now seeded from the arm's seed, so no draw in the harness is unseeded and the same requests meet the same service
  in both arms and in every run.
## 2026-10-20: Armada on the group of clusters, preregistered (amendment 2), four ways

- **Armada on the group rig** (`docs/GROUP_PREREGISTRATION.md`, amendment 2; register row 94; the founder's list): Armada
  v0.22.14 as its own local stack runs it, its server, scheduler, scheduler ingester, event ingester, Pulsar, Redis and
  PostgreSQL as containers on the runner's own network and on the cluster cores (every image pinned by digest, `armadactl` by
  SHA-256, its components' settings its local stack's: `deploy/kind/armada/`), one executor per member reaching its member by
  the member's kubeconfig, Armada's two priority classes in every member, one queue; each batch of the stream submitted as one
  job set of its pods (requests equal to limits, as Armada requires), done when its tenth pod has succeeded
  (`scripts/kind_group_orch.sh`, `ORCH=armada`; no `omni-host` cluster in its arms). Its record of every batch, where its
  pods ran and its scheduler's and server's last words are the arm's; the merger reads a batch's end from the orchestrator's
  record where a member has no Job of that name (`tools/merge_group.py`).
- `kind-group.yml` takes `orch=armada`; `tests/test_group_rig.py`; the governors page; the campaign's queue (its entry in a
  block of its own).

## 2026-10-20: Open Cluster Management on the group of clusters, preregistered (amendment 1), four ways

- **OCM on the group rig** (`docs/GROUP_PREREGISTRATION.md`, amendment 1; register row 96; the founder's list): its hub
  installed by its own CLI on the orchestrator's cluster (`clusteradm` v1.4.0 pinned by SHA-256, bundle 1.4.0), both members
  registered by `clusteradm join` and accepted, the default cluster set bound; for every job of the stream a Placement of its
  own with OCM's default prioritizers (Steady and Balance), and once OCM has decided, the job as a ManifestWork in the chosen
  member's namespace, which OCM's work agent applies there (`scripts/kind_group_orch.sh`, `ORCH=ocm`). Every ManifestWork
  and every PlacementDecision are the arm's record of what OCM did; the hub's images and the members' agents' are recorded
  with their digests.
- The members' clean-cluster check allows the orchestrator's agent namespaces (`GROUP_AGENT_NS`, several, in
  `scripts/kind_bench.sh`); `kind-group.yml` takes `orch=ocm`; `tests/test_group_rig.py`; the governors page.

## 2026-10-20: what the three trials found in the rigs, fixed before the counted runs

- **Crane** (`docs/CRANE_PREREGISTRATION.md`, amendment 1): Crane's override values name a kube-state-metrics image on
  Tencent's registry, which the chart composes under `registry.k8s.io`, where it does not exist; the trial's Prometheus
  install waited ten minutes on it in both arms. The rig's values name the chart's own image
  (`deploy/kind/crane-prometheus-values.yaml`); nothing else of the override changes.
- **Gödel** (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 9): metrics-server's pinned manifest is applied once with the
  rig's settings written in (one rollout; its image named by `registry.k8s.io`, where the old name redirects), in place of an
  apply and two patches, whose second rollout left the first pod terminating past the wait on Kubernetes 1.24. Every kind rig
  applies it this way (`scripts/kind_bench.sh`).
- **KubeRay** (amendment 9): the Ray worker group's ceiling is bounded by the machine's free memory as well as by the workers'
  processors (a kind node reports the whole machine's memory as its own; 48 workers of 1 GiB took the trial's runner down).
- **Kueue C** (run 39368401852): repetition 5's runner was lost by GitHub; the run's nine other repetitions are read and the
  table says so.

## 2026-10-20: the group of clusters (Karmada first), preregistered, four ways

- **A group of two clusters as one organism** (`docs/GROUP_PREREGISTRATION.md`; register row 95; the founder's list): two of
  the batch rig's six-worker kind clusters on one runner, each running the batch rig's bench unchanged as a member
  (`BATCH_QUEUE=group`: the stream comes from the group, and every member opens its window with the others, `GROUP_BARRIER`
  in `scripts/kind_bench.sh`), the stream sent to the group (`scripts/kind_group.sh`, `scripts/kind_group_orch.sh`), the
  members' records merged into the arm's own files (`tools/merge_group.py`), which the table tool reads as any arm.
- **Karmada v1.19.0**, installed by its own CLI on a cluster of its own (`deploy/kind/cluster-host.yaml`), its CLI and CRDs
  pinned by SHA-256, both members joined in push mode, the operator's one propagation policy
  (`deploy/kind/karmada-propagation.yaml`); on the group alone the harness sends the jobs to the members in turn. Karmada's
  certificates and the members' credentials never enter the run's files.
- `kind-group.yml` (four arms by default; archived by `archive-run.yml`; the label passed by the conductor),
  `tests/test_group_rig.py`, register row 95, the governors page.

## 2026-10-20: the Gödel scheduler's rig, preregistered (amendment 8), four ways, on Kubernetes 1.24

- **Gödel on the batch rig** (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 8; register row 93; the founder's list):
  Gödel publishes no release, so each runner builds its image once from its source at the pinned commit with the project's
  own Dockerfile (`scripts/kind_godel_build.sh`), and every arm checks the commit and the image's ID before loading it into
  its control plane and applying Gödel's own manifests (`BATCH_QUEUE=godel` in `scripts/kind_batch_queue.sh` and
  `scripts/kind_bench.sh`). The stream's pods go to Gödel by its scheduler's name with the three annotations its guide puts
  on every pod; on every other system the job file is the same as before.
- **Kubernetes 1.24 for this system alone** (Gödel supports 1.21.4 to 1.24.6): kind v0.22.0 with the pinned 1.24.17 node
  image, kubectl v1.24.17 and metrics-server v0.5.2 (`kind-godel.yml`; the bench's metrics-server floor now knows the 0.5
  line); no in-place resize, so no power cap or conveyance in any arm, as on Crane's 1.25.
- `kind-godel.yml` (four arms by default; archived by `archive-run.yml`; the label passed by the conductor),
  `tests/test_godel_rig.py`, register row 93, the governors page.

## 2026-10-20: Crane's rig, preregistered, four ways, on Kubernetes 1.25

- **Crane on the serving rig** (`docs/CRANE_PREREGISTRATION.md`; register row 90; the founder's list): Crane 0.11.0 and the
  Prometheus it reads, installed as its installation guide installs them (each chart and Crane's override values pinned by
  SHA-256, `scripts/kind_addons_crane.sh`), its controllers on the control plane; the service's HPA handed to Crane's own
  Effective HPA example in auto mode (`deploy/kind/crane-ehpa.yaml`), from which Crane builds and owns the HPA
  `ehpa-php-apache`. Run the four ways in every repetition (`kind-crane.yml`): the organism alone, Crane as shipped,
  Omni-Compass on the organism alone and on top of Crane, the governor on its own core (`GOV_CORE=1`).
- **Kubernetes 1.25 for this test alone**: Crane builds its HPA as `autoscaling/v2beta2`, which Kubernetes removed in 1.26, so
  its four arms run kind v0.24.0 with the pinned 1.25.16 node image (`KIND_NODE_IMAGE`, read by `scripts/kind_paired.sh`),
  kubectl v1.25.16 and metrics-server v0.6.4. `scripts/kind_bench.sh` now takes metrics-server's floor from its pinned line
  (its own compatibility table) and reads the cluster's API for in-place resize before every arm: where it is not served,
  the power cap and the conveyance are off in every arm and the preflight says so (a failed read stops the arm, never
  switches a lever off).
- **The plug** (`scripts/kubectl_crane.py`, `tests/test_kubectl_crane.py` against a stand-in that rebuilds the HPA as Crane
  does, `tests/standin_crane/kubectl`): Omni-Compass's moves to the HPA's processor target and range carried to Crane's EHPA,
  its records kept on the EHPA and the HPA (Crane's own `--ehpa-propagation-annotation-prefixes=omnicompass.io/`, the one
  setting of Crane's changed, `deploy/kind/crane-values.yaml`); its identity may get and patch that one EHPA
  (`deploy/kind/rbac-omni-crane.yaml`); every reset reads back the operator's settings on the EHPA and on Crane's HPA.
- **The four ways on the serving rig**: an arm named `...bare` carries no add-on (`scripts/kind_paired.sh`; on the batch rig
  it keeps the stream on the default scheduler as before), `tests/test_four_ways.py` running the runner's own lines.
- The governors page names Crane's rig and lists KubeRay and Crane among the four-way systems.

## 2026-10-20: KubeRay's rig, preregistered (amendment 7), and a trial workflow for every new rig

- **KubeRay on the batch rig** (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 7; register row 92; the founder's list):
  KubeRay 1.7.1 (its operator's chart pinned by SHA-256, on the control plane) and one Ray cluster (Ray 2.52.0, its image
  pinned by digest, pulled once by the runner and loaded into every node of each arm's fresh cluster), KubeRay's own
  autoscaling sample with the operator's three settings (`deploy/kind/kuberay-cluster.yaml`); the stream's same 24 jobs as
  Ray jobs sent over the cluster's own job API (`deploy/kind/kuberay-job.yaml`, `deploy/kind/kuberay_stream_job.py`); each
  job's wait, turnaround and end read from its own record (`ray_times.json`, `tools/live_reps.py`), an unfinished job never
  reading quick. `scripts/kind_batch_queue.sh` and `scripts/kind_bench.sh` take `BATCH_QUEUE=kuberay`;
  `kind-orchestrators.yml` makes room on the runner's disk for the Ray image (KubeRay only); `tests/test_kuberay_rig.py`.
- **`kind-trial.yml`**: a new rig tried before its preregistered runs, kind-orchestrators.yml's own job for one repetition
  or a few, its files archived like every run's (`archive-run.yml`), never counted in any table and never read by the
  conductor. KubeRay's trial first, then its four ways' A, B and C.

## 2026-10-20: the scheduler's two three-run tables, the governor's own core, and the four ways

- **`results/live/V12_KOORDINATOR.md`** (Koordinator 1.8.0, colocation as shipped, its repeated runs on the cgroup root its own kind tests use: amendment 4; ten paired repetitions a run, omni-v12, on the rig before amendment 5): GAIN in all three of our runs on the service's response time (mean −36% to −37%, 95th percentile −22% to −25%, 99th percentile −8% to −15%); STEADY on the machines, the machine-hours, the energy, the jobs' wait, turnaround and unfinished jobs, and the failures (none); **no LOSS**. Koordinator gives the batch jobs only what the service leaves unused, so five to eleven of the 24 jobs are still running when the window closes, in both arms alike. Recipe added.
- **`results/live/V12_VANILLA.md` and `V12_BINPACK.md`** (the Kubernetes scheduler as shipped, and with its bin-packing
  profile; ten paired repetitions a run, omni-v12): GAIN in all three of our runs on the machines in service (−12% to −19%
  as shipped, −24% to −28% bin-packing), the machine-hours, the energy at the declared standby (−8% to −13%, −17% to −19%), the
  service's mean response (−21% to −25%, −25% to −29%) and the workers kept after the queue (−22% to −30%, −42% to −48%); STEADY
  on a job's wait, the failures (none) and the jobs unfinished (none); and **LOSS in all three of our runs on a job's mean
  turnaround, +0.9% to +1.4%** in both. Reported as it reads; its cause found and fixed in the rig below.
- **The governor's own core** (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 5): the raw files show the same placement and
  the same start waits in both arms and each pod's hashing 1.3% to 1.5% longer with Omni-Compass on top: on kind the
  governor shares the one runner with every node and competes with them as a peer group, whatever its niceness. From now on,
  on the batch rig, in every arm, the kind nodes run on every core but the last and the governor alone on the last, as it runs
  on its own machine on a real cluster (`scripts/kind_bench.sh`); `tools/confirm_abc.py` names a table's rig from it. A
  governor restarted by the kill test inherits the same core (`GOV_PIN` exported with the rest of its wiring:
  `tests/test_robust_restart.py` caught it missing before any run).
- **The test cluster's state written whole** (`tests/standin_cluster/kubectl`): the stand-in kubectl rewrote its state file in
  place, so the master switch test once read it empty while a decision was being written; it now writes a whole file and
  renames it into place.
- **The four ways** (amendment 6; the founder's order of 20 October): each orchestrator runs with the organism alone, the
  orchestrator as shipped, Omni-Compass on the organism alone and Omni-Compass on top of the orchestrator, all four in every
  repetition (`scripts/kind_paired.sh`: an arm named ...bare runs on the organism alone); `tools/live_reps.py` pairs each
  comparison within the repetition and `tools/confirm_abc.py --pair` writes its three-run table; `kind-orchestrators.yml`
  holds four arms in a job; `tests/test_four_ways.py`. CLAUDE.md carries the order. **Started at 04:12 UTC**: the A, B and
  C of the KAI scheduler, Koordinator, Kueue, Volcano and the bin-packing profile (15 runs, ten repetitions of four arms
  each, $0 on GitHub's machines), in a block of their own in `scripts/reruns.txt`, their ids in
  `results/live/governors_runs.json`; the governors page carries the four ways, one cell per comparison.

## 2026-10-20: the KAI scheduler's three-run table on omni-v12: 5 GAIN, no LOSS

- **`results/live/V12_KAI.md`** (`tools/confirm_abc.py`; runs 39350900880, 39350907916 and 39350915166, ten paired
  repetitions each, one commit, omni-v12): the batch stream through KAI's queues as shipped, then Omni-Compass on top. GAIN
  in all three of our runs: worker machines in service −11% to −16%, machine-hours −11% to −16%, the energy at the declared
  25 W standby −7.5% to −11%, the service's mean response time −21% to −23%, and the workers kept after the queue finished
  −20% to −30%. STEADY in all three: a job's wait (mean and 95th percentile), the 95th and 99th percentile responses, the
  alert minutes, failed requests (none) and unfinished jobs (none). Two rows read STEADY by the three-run rule with a clear
  difference in some runs, shown as they are: the queue finished 0.2% to 0.4% later (about 5 s in 22 minutes; clear of the
  noise in A and B, not in C), and a job's mean turnaround rose 1.5% in A (B and C within the noise). No LOSS row.
- **The governors page** reads a three-run table as `tools/confirm_abc.py` records it (its runs with their ids, engines and
  pairs) and shows, after the queue's gauges, the machines, energy, speed and failures.

## 2026-10-20: the orchestra, the eighth organism: the governors' muscles, native and with Omni-Compass on top (modelled)

- **`results/orchestra/ORCHESTRA.md`** (`tools/run_orchestra.py`; the founder's word of 19 October, night: the governors and
  orchestrators in their own catalog group, an organism, benchmarked native and then with Omni-Compass on top): the 55
  catalog muscles that stand for the knobs of the fourteen governors he named, each governor's muscles a body of its own and
  all of them together one body, native against Omni-Compass on top at the max, seeds 3000-3009, modelled (class S). The
  orchestra reads GAIN (more work and fewer misses) under its own load, the climb and work waiting in line (decisions over
  the line 1.82% → 0.81%, 3.20% → 1.14% and 1.43% → 0.62%; work +0.04%, +0.14% and +0.02%; power given +25%, +55% and
  +42%). Eight governors' bodies read GAIN (the scheduler, CruiseKube, Crane, Armada, Karmada, Open Cluster Management,
  KubeEdge, Nephio) and six STEADY (Kueue, Volcano, KAI, Koordinator, KubeRay, Gödel: their natives miss nothing in the model
  and their work stays as it is); no LOSS, and no plant inside any body did less work or missed its line more often. Its
  A, B and C on GitHub's machines (`orchestra.yml`) must each reproduce the committed table; `tests/test_orchestra.py`; the
  governors page carries the orchestra and each governor's body beside its live test; CLAUDE.md names the eighth organism.

## 2026-10-20: Koordinator's runs repeated on the kubelet's cgroup root its own tests use

- **Koordinator's first A, B and C are invalid**, kept in the raw files and not counted: koordlet crash-looped on every kind
  node in every repetition, its install ran out of time and no window opened. kind starts the kubelet with its cgroup root at
  `/kubelet`, where koordlet finds no pod cgroups; Koordinator's own kind tests set it to `/`. Its runs are repeated on that
  cluster in both arms (`deploy/kind/cluster-koordinator.yaml`, chosen by `scripts/kind_paired.sh` for Koordinator alone; each
  arm's files name the cluster it ran on), koordlet's own log kept when it does not stand; written first as amendment 4 of
  `docs/BATCH_QUEUE_PREREGISTRATION.md`; docs/REGISTER.md row 89.
- **The Kubernetes scheduler's six runs** stand in their own block of `scripts/reruns.txt`, written after they were started
  so the conductor never starts one of them itself; their ids are on the governors page.

## 2026-10-20: the Kubernetes scheduler alone, as shipped and with its bin-packing profile; every governor's muscles named

- **The Kubernetes scheduler, register row 88** (the founder's "kubernetes schedulers, vanilla"): the row 63 stream placed by
  the scheduler alone, with no queueing system, in two settings, each its own table: as shipped (`BATCH_QUEUE=vanilla`: the
  cluster's own default scheduler, nothing installed) and with the operator's bin-packing profile (`BATCH_QUEUE=binpack`: a
  second scheduler from the cluster's own release, the image the control plane runs, one profile scoring a node higher the
  fuller it is, one replica on the control plane; `deploy/kind/binpack-scheduler.yaml`); the end record lists where every
  pod went, node by node. Preregistered as amendment 3 before any run; A, B and C of both settings in
  `kind-orchestrators.yml`; `tests/test_batch_queue.py`.
- **The governors page** names, for every governor, the catalog's muscles that stand for its knobs in the modelled organisms
  (class S, `realms/catalog_v5.csv`: the scheduler's in family 4, on the spine; the queueing systems' in families 1 and 14;
  the multi-cluster ones in family 39; Nephio's in family 66), and reads the scheduler's two settings from their two tables.

## 2026-10-20: the governors and orchestrators on one page

- **`results/live/GOVERNORS.md`** (`tools/governors_page.py`, the founder's word of 20 October: "I need to see what the
  results are of those governors"): every governor and orchestrator he named, what it governs, what native is under it,
  where its test stands, and once its three runs are in, its readings by the one key, every row counted, losses included,
  each line read only from its own three-run table (`results/live/V12_<NAME>.json`), never a number before. The runs started
  are listed in `results/live/governors_runs.json`; `verify.py` fails a push where the page is not what the tables and runs
  give; `tests/test_governors_page.py`.

## 2026-10-20: Koordinator under the batch stream

- **Koordinator, register row 89** (the founder's "coordinator with a K"): the row 63 rig with a fourth system
  (`BATCH_QUEUE=koordinator`): its chart 1.8.0 from its charts repository's release, the archive's SHA-256 pinned and refused
  otherwise, installed by Helm as its guide installs it, colocation on as shipped, with the operator's two settings for one
  control plane (`deploy/kind/koordinator-values.yaml`: its images from its GitHub registry; manager, scheduler and
  descheduler one replica each on the control plane); koordlet on every node as shipped; the jobs best effort on batch
  resources by the operator's colocation profile (`deploy/kind/koordinator-colocation.yaml`), its webhook proven to mutate a
  labelled pod before the window. Preregistered as amendment 2 before any run; A, B and C in `kind-orchestrators.yml`.

## 2026-10-20: the KAI scheduler under the batch stream, in a workflow of its own

- **The KAI scheduler, register row 91** (the founder's list of 19 October, night): the row 63 rig with a third queueing
  system (`BATCH_QUEUE=kai`): KAI's chart v0.18.6 from its own registry, the archive's SHA-256 pinned and refused otherwise,
  installed by Helm with the chart's own placement setting so its operator puts every component on the control plane
  (`deploy/kind/kai-values.yaml`), any deployment the setting does not reach placed there after install, every serving pod
  checked; the jobs sent to its default queue by its scheduler's name and the queue's label on the job and on every pod
  (`deploy/kind/batch-stream-job.yaml`, `POD_QUEUE_LABEL`, substituted before the job's label it contains). Preregistered as
  amendment 1 before any run (`docs/BATCH_QUEUE_PREREGISTRATION.md`).
- **`kind-orchestrators.yml`**: the same rig in a workflow of its own, so an orchestrator's A, B and C started together never
  take the place of a campaign run of `benchmark-reps.yml` (the conductor reads runs back by their count in a workflow); it
  records its letter (`LABELLED`), counts only on the rig's commits (`RIG_WORKFLOWS`) and hands its files to the raw branch
  (`archive-run.yml`). KAI's entry stands in its own block of `scripts/reruns.txt`; `tests/test_batch_queue.py`,
  `tests/test_release_campaign.py`.

## 2026-10-19 (night): the governors and orchestrators: Kueue and Volcano built and in the omni-v12 campaign; every other one has its place

- **Kueue and Volcano, register row 63** (the founder's list of 19 October, night): the batch test's work arrives as a stream
  of 24 jobs (one every 30 s, 10 pods each, 5 at a time; the batch test's 240 pods of 3,000 MB in all) and a queueing system
  of its own admits and places it, installed from its own release in every arm before the arms are told apart: Kueue v0.20.2
  with the operator's single ClusterQueue sized to the workers (read live), or Volcano v1.16.0 with its default queue, each
  release file SHA-256 pinned and refused otherwise, every piece of it on the control plane (Volcano's certificate Job ships
  with no placement and is placed there before the file is applied), the stream's image pulled onto every worker before the
  window (`scripts/kind_batch_queue.sh`, `deploy/kind/batch-stream-job.yaml`; `scripts/kind_bench.sh` with `BATCH_QUEUE`;
  `benchmark-reps.yml` input `batch_queue`). Native is the queueing system as shipped; omni is Omni-Compass on top with the
  batch test's live muscles, writing nothing of either project's and nothing of the jobs. Four judged gauges
  (`tools/live_reps.py`, `job_stream`): a job's wait from its submission to its first pod running (mean and 95th percentile),
  its turnaround, and the jobs unfinished at the window's end, a job not started or not done counting the window's end;
  `tests/test_batch_queue.py`. Preregistered before any run (`docs/BATCH_QUEUE_PREREGISTRATION.md`); both close the first
  block of the omni-v12 campaign, written before it opened (`scripts/reruns.txt`), so their A, B and C are the campaign's own.
- **Every other orchestrator named has its place** (`docs/REGISTER.md`, rows 88 to 98, each marked not yet run): the
  Kubernetes scheduler as shipped (under every Kubernetes set already; its own bin-packing set queued), Koordinator, Crane,
  the KAI scheduler, KubeRay, the Gödel scheduler, Armada, Karmada, Open Cluster Management, KubeEdge and Nephio (a candidate:
  its sandbox asks more than a free runner gives). CruiseKube stands at row 81.

## 2026-10-19 (late night): Omni v12 stands (a refused raise is held; the swarm's reflex acts at once); every fix lands as the next version

- **omni-v12** (`OMNI_V12.json`, digest `d38b58fbe28939b8`, 47 files; `docs/OMNI_V12.md`): omni-v11 with two faults fixed, both
  found on the omni-v11 runs of 19 October. (1) The Kubernetes governor's conveyance (`omni_controller/muscles.py`): a CPU-limit
  raise the cluster's admission refuses is not written again until the pod's limit changes, the raise shrinks, or a wait passes
  (5 minutes, doubled at each refusal up to an hour); an accepted raise clears the hold, and the audit records each hold and its
  wait (`held_s`). In the omni-v11 capacity test admission refused every raise (`exceeded quota: omni-cap`) and the governor
  wrote it again at every fast check, 970 to 1,000 refused writes an hour (`results/STEERING.md`); `tests/test_refused_raise.py`.
  (2) The swarm's wire (`tools/run_swarm.py`, outside the digest's scope, declared with the version): the proximity reflex hands
  back the planner's cruise in the tick it is triggered, its reach growing with the square of the speed (0.5 m at the planner's
  cruise, as before). The omni-v11 reflex let the override fall 0.01 a tick, and on a mission draw outside the counted cells
  two drones came within 0.083 m (`results/model_gate/V12_SWARM_REFLEX.md`).
- **The mechanism identity recorded again** (`results/MECHANISM_IDENTITY.json`, `tools/mechanism_identity.py`): its actuator
  component M_act holds the governor's muscles, so both configurations' mechanism ids move with omni-v12 (symmetric_verified
  `3161bef0a669625b`, printed_eight_line `d3b21fb8f9a25c9d`); every other component is omni-v11's. The deviations register lists
  the swarm's amendment 2 (`docs/DEVIATIONS.md`, 57 amendments), and the bill of materials names the package 0.12.0.
- **The model gate** (`results/model_gate/V12_VS_V11.md`, seeds 1 to 8: the cluster models at 60 s, at 15 s and with the blink, the
  three convey models, the verdict model at 20 and 200 pieces of work a decision): identical to omni-v11 on every gauge of every model
  but one, the convey model whose every raise is refused, where omni-v12 writes 49.75 commands a day against 1,985.5 (−97.5%,
  GAIN). No reading against omni-v11 is a LOSS. The swarm's fix held every drone at or outside the keep-out on all ten cells
  and draws tried and kept 49% to 92% of the energy cut (class S, our own runs of an outside simulator).
- **Studied and left out: the verdict's upper end** (branch `v12-verdict-study`). It answers a real fault, but on the model
  cluster set from a real run's regime no give-back trial could start (about 80 requests a decision against about 4,000
  needed a phase), so omni-v11's machine-hour and energy cuts would be gone, and on the data stores every knob would stay
  native. Refused as written; the row stays on the next version's list (`docs/CHANGE_CONTROL.md`) until a trial design that
  reads a 2% step in a trial's time is shown in the model gate.
- **Every fix lands as the next version, told, not asked** (the founder's order, the night of 19 October: "Of course I want you
  to land version 12 ... every time you do that ... it becomes a new version"): CLAUDE.md and `docs/CHANGE_CONTROL.md`, rule 6.
- **The swarm's preregistration, amendment 2** (`docs/SWARM_PREREGISTRATION.md`, written before omni-v12's runs): a collision
  with Omni-Compass on top where native has none is a judged LOSS row (until now it voided the cell), a cell is void only when
  native itself collides, and three mission draws no wire was ever run on (`short-314`, `mixed-315`, `long-316`, the seed plus
  303) are counted beside the first three cells. `tools/run_swarm.py`, `tools/swarm_abc.py` (the earlier tables rebuild as
  they were scored), `.github/workflows/swarm.yml`, `tests/test_swarm_abc.py`.
- **Everything runs again on it**: the conductor's campaign, the reruns, the grid (`results/grid_v12/`) and the Azure sets
  from A, from 00:30 UTC on 20 October (the conductor starts nothing before it); the omni-v11 runs already started run to
  their end as omni-v11's record (nothing is cancelled). The package is 0.12.0.
- **A fault in the coverage tool, found and fixed.** `tools/engine_coverage.py` started each file `tools/function_tests.py`
  runs as `coverage --append`, which coverage refuses ("no such option"), so those files ran untraced and a measurement
  counted the unittest suite alone (51% on the omni-v12 tree). It now starts them with `coverage run --append` and stops if
  coverage refuses a command (`tests/test_engine_coverage.py`). Measured again on the omni-v12 tree: 82% of the engine's
  6,531 statements run under the tests (`docs/ENGINE_COVERAGE.md`; 81% of 6,519 recorded on omni-v11).
- **Pages brought up to it**: README, CLAUDE.md, the state of play, the receipts, the referee summary and grades, the
  limitations, the safety case, the change control record, the Omni index, both manuals (rebuilt), the v11 page, and the live
  engine's page and appraisal: the page's words name omni-v12, its table of the real Kubernetes runs is read from the omni-v11
  tables that replaced four of the five it quoted (no LOSS: the KEDA pod start wait reads STEADY with the image pulled first),
  its banner shows only when a newer engine stands than its words were written for, and its controller trace, recorded again
  on the omni-v12 tree, is identical to the one on the page.

## 2026-10-19 (night): the control panel, the alert rules, the control-quality figures; the v12 candidate narrowed to two fixes

- **The control panel** (`tools/omni_control.py`, `tests/test_omni_control.py`; the Operator's Manual, section 22.5;
  `docs/OBSERVABILITY.md`): the governor's buttons behind a bearer-token HTTP API with an OpenAPI 3 document and a browser
  console. Mode (autopilot, watch, off), dial (max, tune-down) and reset to native for the operator role; the kill switch for
  every governor on the machine and the two-person arm for the security role; every press, refused ones included, logged with
  its holder and reason; tokens kept as SHA-256 digests; HTTPS required beyond the loopback. It writes no setting itself: every
  change goes through the governor's own hand-back (its kill file) and a restart with the new arguments, so the engine and its
  fingerprint do not change. A governor that exits on its own is never restarted by the panel; its lease hands back first.
- **The alert rules** (`deploy/prometheus/omni-compass-rules.yaml`, `tests/test_alert_rules.py`): ten Prometheus rules, each
  with severity, meaning and action, reading only series the exporter and the panel serve: governor stale, governor orphaned,
  writes hammering, write errors, a recommendation oscillating, a sense blind, the service at its line, the master switch off,
  the audit unreadable, the governor's own processor high.
- **The control-quality figures** (`tools/omni_exporter.py`, `tools/steering.py`, `results/STEERING.md`, four new Grafana
  panels): decisions by zone (slack, band, wall), the time from the line back into the band, the distance each recommendation
  travelled, errors by kind. Read on every omni-v11 Kubernetes table: in the add-on tests the compass sat at the line in 4% to
  9% of decisions and came back within a decision (61 to 62 s); in the capacity test and the two robustness tests the load
  holds the service near its line in both arms (54% to 79% at the line), and their alert minutes, the comparison with native,
  read GAIN. The capacity test's 940 to 967 errors an hour are the refused raises fixed in the v12 candidate.
- **The v12 candidate** (branch `v12-candidate`, landed the same night as omni-v12, `docs/OMNI_V12.md`): two fixes, the refused raise held until
  something changes (the model: 97.5% fewer writes, every other gauge identical) and the swarm's reflex at once with a reach that
  grows with the square of the speed. The stricter verdict (a step kept only when its whole 95% interval is inside the
  allowance) was taken out of it and kept on the branch `v12-verdict-study`: in the model cluster set from a real run's regime
  the governor reads about 80 requests a decision and the rule needs about 4,000 a phase, so no give-back trial started and the
  candidate read identical to native, the machine-hour cut gone; on the data stores it would leave every knob native. The fault
  it answers (a step whose interval reaches past the allowance kept on its estimate) stays on the next version's list until a
  trial design that can read a 2% step in a trial's time is shown in the model gate.

## 2026-10-19: The robustness tables on omni-v11, no LOSS; the governor's gauges for Prometheus and Grafana; the receipts page on the newest tables; the cost to match runs again

- **The kill test and the long run on omni-v11** (`results/live/V11_ROBUST_KILL.md`, `V11_ROBUST_LONG.md`, each with its recipe
  in `results/live/RECIPES.json`). The counted runs of each are the first three on commits carrying the kind rig's pre-puller;
  the earlier omni-v11 runs are kept on `raw`, and the three earlier kill runs read no LOSS either. The kill test: every setting
  back at the operator's 8 to 11 s after the kill in 30 of 30 repetitions, a second governor to the end in every one, the 120 s
  after the kill STEADY, five service rows GAIN in all three runs, replicas +3% to +6% power given. The long run: memory up 2.3% at
  most, 97.5% of the expected decisions, none failed, no slowing, everything handed back; three rows GAIN, replicas +49% to
  +52% power given. With the three data stores at the max that landed the same evening (`V11_PGBENCH_SERVICE.md`,
  `V11_SYSBENCH_SERVICE.md`, `V11_YCSB_SERVICE.md`: no LOSS, no single-run tail rise), 23 omni-v11 tables, 1,039 judged rows,
  0 LOSS.
- **The kill test's 99th percentile, read to the repetition.** It rose 25% in run A and fell in B and C (STEADY). In nine of run
  A's ten repetitions both arms read the probe's 10-second timeout; in the fifth the omni arm's slowest answers reached 9.2 s 140
  to 190 s after the kill, with every setting already handed back to native's, both arms at the HPA's cap of ten replicas, the
  runner's processor 100% busy for 70 s and the second governor started 50 s before on the same four cores: the likely cause,
  not proven, written in the preregistration's "On omni-v11" and `docs/TAIL_LATENCY.md`. The after-kill window widened to 300 s
  goes on the next version's list.
- **The governor's gauges** (`tools/omni_exporter.py`, `tests/test_omni_exporter.py`, `deploy/grafana/omni-compass.json`; the
  Operator's Manual, section 22.2): its audit served to Prometheus at `/metrics`, read-only, with a ready Grafana screen. Read on
  the omni-v11 long run's audit it showed the brain's recommended power cap switching between two values at 40 of its 41 moves
  (not written on Kubernetes, where the power wire is off); a band on that gate goes on the next version's list, to be read on
  the card's replay before any chip run (`docs/CHANGE_CONTROL.md`).
- **How steadily the governor steers** (`tools/steering.py`, `results/STEERING.md`): every omni-v11 Kubernetes table's omni
  arms read for their decisions, writes, moves and reversals an hour, shown and not judged. It found a fault: in the capacity
  test the governor's role cannot read the namespace's quota, so admission is the authority (as written), and admission refused
  every CPU-limit raise while the governor wrote it again at every fast check, about 970 to 1,000 writes an hour against 17 to
  214 in every other test. Nothing changed on the service (the table reads STEADY), but a refused write repeated forever is
  hammering. A refused raise held until the quota or the pod changes (an engine rule, `omni_controller/muscles.py`) and the
  rig's governor role reading the quotas go on the next version's list.
- **The receipts page** (`docs/THE_RECEIPTS.md`) had stayed on omni-v7's tables; every row now reads each test's newest table,
  its engine named, the swarm's fault and the robustness tables included.
- **The cost to match** (native tuned harder by its operator to HPA targets 40, 30 and 20, beside Omni-Compass on top) had run
  once, on 3 October, on an engine long gone (`results/live/COST_TO_MATCH.md`: no native setting reached Omni-Compass's 95th
  percentile). It goes into the campaign as a block of its own (`scripts/reruns.txt`), A, B and C on omni-v11, so whether native
  is as good as it can be is answered on the engine that stands.
- **What a buyer will ask for that is not here yet** (the founder's question of 19 October): written in the grades page's
  blueprint, proof, gauges and the operator's screen, each with what closes it.

## 2026-10-19: The conductor counts only the jobs a run can start; the verdict's allowance rule goes on the next version's list

- **The conductor** (`scripts/dispatch_grid.py`, found by the live-engine session). A 100-repetition Azure set runs one
  repetition at a time (max-parallel 1), and GitHub lists its other 99 jobs as queued for hours. The conductor counted them as
  the repository's queue, so it held back every grid start behind them. A run's queued jobs now count only up to the slots its
  own max-parallel leaves free (`max_parallel`). `tests/test_release_campaign.py` covers it. Writing that test found a second
  fault in the same reader: it read a run's job list page after page until a page came back short, so a list that kept
  answering full pages was read forever (the test's first version did exactly that and filled the memory). The reader now
  stops at ten pages, more than the 256 jobs a run can hold, and a test holds it there.
- **The release manifest** (`RELEASE_MANIFEST.json`) is written again. The supply-chain commit of 19 October pinned every
  workflow's actions and the manifest was not rewritten after those edits, so GitHub's verify failed on 4d06bf58 and 0bc4e62d
  (`release manifest: ... changed since the manifest`, every pinned workflow named).
- **The verdict** (`omnicompass/verdict.py`, the same session's finding, read in the code). A step is kept when its estimated
  cost is within the 2% allowance, even when the upper end of its 95% interval reaches past it. At the noise measured on the
  omni-v10 tables, a give-back that truly costs 3% would be kept about 31% of the time. No table read a LOSS from it. The fix is
  an engine rule: a step is kept only when the interval's upper end is inside the allowance, with a trial that could not be read
  in its time never started. It goes on the next version's list with its price, said before any run: some data-store GAIN
  rows may read STEADY, because there the muscle stays native (`docs/CHANGE_CONTROL.md`). Nothing in the engine changes here.
- **The founder's order, written down** (`CLAUDE.md`, Orders of 19 October; `AGENTS.md`, for any other agent): nothing is
  forced but the mechanism. No number is tuned to make a row read well; the code is made to do what its rule says and the
  wire is fastened right, and the runs say what it does. Every fix on the next version's list is of that kind: the swarm's
  reflex acting when its own rule says, the verdict judging by its interval, the Redis harness measuring as a deployment runs.

## 2026-10-19: The Redis 99th percentile, root-caused: the harness puts the brain inside the load generator

- **The question** (the founder's, 19 October): why the 95th and 99th percentiles show red on the live page. No tail row
  reads LOSS in any omni-v11 table. On real Kubernetes, Omni-Compass's 95th and 99th percentiles were below native's in all
  90 paired repetitions. The single-run rises are Kafka's and MySQL's one-run excursions, and a small, consistent Redis rise of
  about 6 µs (0.1%) at the 99th percentile (`docs/TAIL_LATENCY.md`).
- **The cause of the Redis rise.** `tools/run_redis.py` runs the brain as a thread inside the load generator's own Python
  process, so its once-a-second work shares the interpreter lock with the request threads. The test
  (`tools/redis_brain_probe.py`, `results/REDIS_BRAIN_PROBE.json`) runs the harness's own application and brain with a
  stand-in store and a plug that writes nowhere, so nothing differs between the arms but the brain thread. With the brain in
  the process the 99th percentile rose 101 µs (95% interval +50 to +151 µs, 10 of 12 pairs) and the mean 5.4 µs (11 of 12).
  In the set with native as shipped, where the brain computes nothing, no rise of consistent sign appears.
- **What it means.** The rise is the harness's layout, and it weighs against Omni-Compass, because only the omni arm carries
  the brain. No deployment runs the brain inside the application it governs, and the other data stores' load generators
  already run as processes of their own.
- **The fix.** The Redis harness runs the brain in a process of its own. It changes how the omni arm is measured, so it lands
  with the next engine version's reruns (`docs/CHANGE_CONTROL.md`).

## 2026-10-19: A fault found in the swarm's wire, beyond the counted cells; its fix waits for the next version

- **What was found.** The swarm wire (`tools/run_swarm.py`) moves one knob, the cruise override. Its proximity reflex is
  written to hand back the planner's cruise at once when another drone comes within 0.5 m. The code did something else: it
  let the override fall by 0.01 a control tick, so a drone kept flying fast for about a second after it saw a neighbour.
  - In the counted cells of the omni-v11 table this spent the margin without a judged miss. The closest approach, shown and
    not judged, fell from native's 0.30 to 0.46 m to about 0.16 m. There was no near miss and no collision.
  - On mission draws the wire was never run on, it did not hold. On the mixed cell with draw 214 two drones came within
    0.083 m, with 5 near-miss ticks and 3 collision ticks, where native flew the same draw with none.
- **The fix.** The reflex acts in the tick it is triggered, and its reach grows with the square of the override, as a drone's
  stopping distance grows with the square of its speed. Flown on our own machine on the four preregistered cells and six untouched
  draws, it held every drone at or outside the full 0.30 m keep-out (the least, 0.304 m), with no near miss and no collision. It
  kept 49% to 92% of the energy cut. The record is `results/model_gate/V12_SWARM_REFLEX.md` (class S, every flight in its
  `.json`).
- **Where it goes.** A change to a guard is the next engine version (`docs/CHANGE_CONTROL.md`, which now lists every change
  waiting for it). It is shown to the founder before it is pushed. Its preregistration adds a judged collision row and draws
  beyond the fixed seeds.
- **Where it is written.** `docs/LIMITATIONS.md` (sections 3 and 4), the referee summary's "does no harm" row, the state of
  play, the README, the grades (outside simulators held at B−), and the Owner's Manual (sections 3.5, 16.5 and 16.6).

## 2026-10-19: Every page lined up with the newest table of each benchmark

- **The Owner's Manual's results**, until now written from the omni-v7 tables, are read from each benchmark's newest table:
  - section 3.5, the evidence table, names its engine row by row;
  - section 16.1 is on omni-v10 (steady work, the wandering demand, all four, faults, the queue of jobs, the noisy neighbour,
    the Google day; steady and wandering written in for the first time);
  - section 16.1b is on omni-v11 (Goldilocks, KEDA two ways, fixed capacity), with CruiseKube on omni-v10;
  - section 16.4 covers the data stores on omni-v11, native as shipped beside the operator's setting;
  - section 16.4b has the two-hour run on omni-v10;
  - section 16.5 has the outside simulators on omni-v11, with the swarm's fault;
  - section 16.6 has the one number and the table.
- **The receipt charts** (`docs/book/schematics.py`) picture the omni-v11 tables for Goldilocks, KEDA two ways and the capacity
  test, and omni-v10's for CruiseKube.
- **The Omni index's page** names each table's engine from the tables themselves (7 tests on omni-v11, 7 on omni-v10). It no
  longer says every table ran on omni-v7.
- **The benefit sheet** dates a table that is new in the working tree with the day it lands, where it had read "unknown" in a
  shallow checkout.
- The referee summary, the state of play and the README say the same, the pod start wait's open item is closed (STEADY on
  omni-v11), and both books are rebuilt.

## 2026-10-19: The referee's grades, category by category, with the pages behind them

- **`docs/REFEREE_GRADES.md`** grades Omni-Compass in twenty categories, as a referee or an underwriter would. For each it
  gives the grade on the morning of 19 October, the grade the evidence supports now, the highest grade the category can
  reach, and what reaching it takes. A category with nothing measured yet (the cloud bill, energy, the GPU, production) is
  **Undetermined**, never failed. These are our own grades; no outside party has graded them.
- **New referee pages**, each bound into the Owner's Manual:
  - `docs/RELATED_WORK.md`: the published ideas Omni-Compass is built from (supervisory control over regulatory loops,
    reference governors, the Simplex fallback, online controlled experiments, shielding, feedback control of computing
    systems), each with the work that stated it, and the combination that is the claim.
  - `docs/CHANGE_CONTROL.md`: the rules by which the engine changes, the record of every version since omni-v5 (landed,
    digest, files, why), and one gap: the wires that are not yet in the fingerprint.
  - `docs/LIMITATIONS.md`: independence, internal, construct, statistical and external validity, and the engine's pace. A
    false GAIN or LOSS under the three-run rule has probability 2 × 0.025³ ≈ 3.1 × 10⁻⁵ a row, about 0.03 over the 854 judged
    rows of the omni-v11 tables.
  - `docs/POWER.md` (`tools/power.py`): the smallest change each judged row can see, in one run and in all three, and the
    repetitions a run would need to see 5%. `docs/DEVIATIONS.md` (`tools/deviations.py`): every amendment of every
    preregistration with its timing (56 in 12; 41 before the runs they govern, 5 after runs began, 10 not stated).
  - `docs/TAIL_LATENCY.md`: the founder's question on the 95th and 99th percentiles, answered from the receipts.
- `verify.py` checks that the power page, the deviations register, the coverage page, the bill of materials and the
  reproduction recipes are what their sources give.

## 2026-10-19: Supply chain and security: every package hashed, every action pinned by commit, every finding reviewed

- **Hash-checking.** `requirements-lock.txt` pins each of its 29 packages with the SHA-256 of every file PyPI serves for
  it, so `pip install --require-hashes -r requirements-lock.txt` refuses a package whose bytes changed. The two packages
  ReportLab and MuJoCo bring (charset-normalizer, websockets) are pinned with them.
- **Actions by commit.** All 407 `uses:` lines in the workflows name the action by its 40-character commit, with the
  version as a comment (`actions/checkout@11d5960… # v4`), so a moved tag cannot change what runs. `tools/legal.py` writes
  its steps the same way. `tests/test_supply_chain.py` fails a push with an unpinned action or an unhashed package.
  `docs/THREAT_MODEL.md`: T8 (the supply chain) is closed for what Omni-Compass installs.
- **The bill of materials.** `tools/sbom.py` writes `sbom/omni-compass.cdx.json` (CycloneDX 1.5),
  `sbom/omni-compass.spdx.json` (SPDX 2.3) and `docs/DEPENDENCY_LICENSES.md`: every package's license, its use, and a
  gate that fails on any strong copyleft. All are permissive except Hypothesis (MPL-2.0), which is used by the tests alone.
- **The static scan.** `tools/security_scan.py` runs Bandit over 34,657 lines of code that runs, and writes
  `docs/SECURITY_SCAN.md`. It found 3 high and 34 medium findings; every one is fixed or reviewed with its reason, and a
  new or stale one fails the check. Two fixes in `tools/run_pgbench.py`: PgBouncer's folder is owned by postgres and set
  0o755 (it was world-writable), and the MD5 that PostgreSQL's own password method defines is marked as not used for
  security. `security-scan.yml` runs the scan and `pip-audit` (0 known vulnerabilities in the 29 pins) on every push that
  touches code or the lock, and weekly.

## 2026-10-19: The engine's mathematics: the bath proved stable, 24 of 24; 81% of the engine run by the tests

- **`tools/prove_engine.py`** proves, by the z3 solver and by mpmath's interval arithmetic, 24 claims about the algorithm
  the engine executes, over every input in its declared set. The claims cover the compass law, the plug's clip, the
  verdict, the invariance of E, I and S, the tracking bound inside the basin and the steps to reach it. New today: **B1**,
  the bath's stability. For every quality factor Q ≥ ½ the engine's oscillators can take and every frequency on its grid,
  the spectral radius of one Runge-Kutta micro step is below 1, so the bath decays. The bound is
  |R(z)| ≤ exp(Re z) + |z|⁵/120 · exp(|z|), checked over 400 cells of ω with Re z = −hω/(2Q) and |z| = hω.
  `docs/ENGINE_PROOFS.md` states each claim, its method and what is still open (CERT-10 for every fixture, the bath's
  amplitude as a number). `tests/test_engine_proofs.py` fails a push where a claim is not proved, where a proof is vacuous,
  or where the stored record differs. `tests/test_engine_properties.py` checks every proved property on several thousand
  generated cases against the engine's own code.
- **Coverage.** `tools/engine_coverage.py` measures line coverage of each of the 47 engine files under the whole test
  suite. **81% of 6,519 statements run under the tests**; the files least covered are named first
  (`docs/ENGINE_COVERAGE.md`).

## 2026-10-19: Every omni-v11 table rebuilt from its raw receipts, identical to the byte

- **`tools/reproduce.py`** opens a table's runs from the branch `raw`, runs the table's own tool on them in a scratch
  folder, and compares the result with the table on main, byte for byte. The recipes are in `results/live/RECIPES.json` and
  the front page's state. **All 18 omni-v11 tables come out identical.** `reproduce.yml` repeats it every week and on
  request; `verify.py` checks that every omni-v11 table has a recipe.

## 2026-10-19: The omni-v11 three-run tables: 18 tables, 854 judged rows, 0 LOSS

- **Real Kubernetes** (kind, ten pairs a run):
  - Goldilocks and the VPA: the 95th percentile cut 61% to 64%.
  - KEDA's HTTP add-on: the 95th percentile cut 72% to 74%, alert minutes cut 100%.
  - KEDA on CPU and requests: the 95th percentile cut 52% to 53%.
  - Fixed capacity: STEADY at every cap.
  - The omni-v10 LOSS, the pod start wait under KEDA's HTTP add-on, reads STEADY now that the rig pre-pulls the served image.
  - In all 90 paired repetitions Omni-Compass's 95th and 99th percentiles were below native's.
- **The data stores** (three pairs a run): Kafka at the max and at the service objective, PostgreSQL, Redis (the operator's
  ceiling, native as shipped, the service objective), MySQL and MongoDB (the operator's setting and native as shipped):
  0 LOSS. Redis at the operator's ceiling reads 4 GAIN at the tune-down and 6 at the max.
- **Outside simulators:** CityLearn 27 GAIN, the power grids 67 GAIN, the robot arms 7 GAIN, the swarm 9 GAIN.
- **Three faults found while building them, each fixed before any table carried it:**
  - The front page grouped a data store's runs with native as shipped together with the runs at the operator's setting.
    `tools/front_page.py` now keeps them apart (`V11_REDIS` and `V11_REDIS_SHIPPED`), and `tests/test_front_page.py`
    fails a push that mixes them.
  - The conductor started the capacity test's B and C runs without their letter, so each read "A". `scripts/dispatch_grid.py`
    now passes the letter to every workflow that takes one, `tests/test_release_campaign.py` checks it, and the capacity
    table notes the runs started before the fix.
  - CityLearn's comfort score drifts by up to 3.6 × 10⁻⁵ between runs in both arms alike. The CityLearn table now notes
    each row that reads "the runs differ" while its paired change is exactly zero in every run (`tools/citylearn_abc.py`).
- `.github/archive_request.txt` lists the 17 runs these tables read, so their files are saved on `raw`.

## 2026-10-19: "Do no harm" has one meaning everywhere, and it is the organism's

- **The founder's words of 19 October**: "its real goal is to strengthen the organism and keep it healthy in any form and
  keep it working in its most optimal state that the organism can live within its own muscles ... If that means
  decreasing a muscle to push another muscle, but in the whole end makes the organism produce a better output, well, that
  was the goal in the beginning, is the output".
- **The meaning, written once** in `DISCLOSURES.md` section 3:
  - Harm is judged at the organism. It is the organism turning out less than its native controllers make it turn out
    (less work done; more time waited, missed or failed), or the organism made less healthy: a muscle past its own limit,
    a service over its own line, anything made to fail.
  - Every muscle works only as far as its own limit, never past it.
  - The muscles are one body: one may be used less, left native or rested so that another carries more, whenever the
    whole organism comes out ahead and every muscle stays healthy.
  - The brain answers a breach at once and acts before a line is crossed.
  - Every row is still shown.
- **Where it is carried:**
  - the key (`tools/readings.py`), and through it the README, the reading guide and both manuals;
  - both manuals' front matter and their section 1.2;
  - `CLAUDE.md`, the safety case, the proof program and the theory chapter;
  - `tools/summary.py`;
  - the four AI instruction files and `llms.txt`.

  Both books are rebuilt.
- **The engine that stands is unchanged.** It keeps do no harm in its strictest form: every muscle judged on itself by
  the 2% verdict, never below native, nothing traded between muscles. Every page says so. Three things come with the next
  engine version, through the model gate, after the founder is told:
  - the trade between muscles, judged on the organism;
  - the governor's count of the machines an add-on marks;
  - the engine's own words.

## 2026-10-19: Every finished run's files land in the repository by themselves

- **The founder's order of 19 October** ("it's mine ... it should have been in my shit"). Until now only the five live
  products' runs were copied onto the branch `raw` by themselves. Every other run's files stayed in GitHub's artifact
  store, where they expire and this session cannot open them, unless its id was listed by hand. That is how the files
  of the failed six-kube repetition (run 39214993403, the distribution organism at 10 copies, repetition 57) were out
  of reach.
- **The fix.** `archive-run.yml` now runs every hour by itself. Each pass takes every finished run, failed ones
  included, of every workflow that hands in files since omni-v11 landed (2026-10-18 16:06 UTC). It saves each one on
  `raw` as `run-<id>/`, then frees the runner's disk, up to about 4 GB a pass; the next pass goes on from there. A run id
  in `.github/archive_request.txt` still goes first, and this push lists the three failed six-kube runs and the three
  omni-v11 CruiseKube runs.
- `tests/test_archive_sweep.py` fails a push that leaves any workflow that uploads files off the list. The Owner's
  Manual and `CLAUDE.md` say so.

## 2026-10-19: The recorder counts a worker held by an add-on's own mark while it serves

- **Why two CruiseKube runs read failed.** Three native repetitions of the omni-v11 CruiseKube test (run 39171059299,
  repetitions 5 and 10; run 39175670991, repetition 2) were refused for "no machine in service" while the service answered
  every probe. In each, CruiseKube had marked every node `cruisekube.truefoundry.com/overloaded:NoSchedule`, every node Ready.
  That mark tells the scheduler to send the node no new pod; the pods already on it keep serving. The recorder
  (`fleet/capture/kube_capture.sh`) took any NoSchedule mark as a machine out of service, read 0, and the rig refused the
  window. The runs aggregated their other 9 pairs.
- **The fix.** A Ready worker that carries work and is held only by an add-on's own NoSchedule mark is in service, as the
  power capture already counted it. Kubernetes' own marks, the control plane's role mark and any NoExecute mark still take a
  node out. The same rule holds in both arms, and the refusal stands for a window with truly no machine in service.
  `tests/test_capture_in_service.py` runs the recorder on the cluster as those repetitions saw it: it read (0, 0) before the
  fix and (2, 2) after.
- **Run again.** The CruiseKube test runs again, A, B and C, on the corrected recorder (`scripts/reruns.txt`, the block of
  19 October). Its earlier runs stay their own record.
- **For the next engine.** The governor (`omni_controller/controller.py`, an engine file) counts machines by the old rule.
  Under the add-on's mark on every worker it holds, safely but blind. That changes in the next version, through the model gate.
  `docs/K8S_COMPASS_PREREGISTRATION.md`, the amendment of 19 October.

## 2026-10-19: The repository credits its making to The Omni-Compass LLC alone

- Four live lines named an AI tool as the maker of part of the work, and now say nothing of who typed them:
  - the governor's role file (`deploy/kind/rbac-omni.yaml`);
  - the v7 candidate's line in this changelog;
  - two rows of `docs/HISTORY.md`;
  - one step of `docs/METAL_KIT.md`.
  The authorship records already named the company: `codemeta.json`, `pyproject.toml` and `CITATION.cff`, and the © notice
  on every file. Where an AI tool read the results (`results/external_review/`, named as readers that never produce
  results), and in the review records and the branch names, the record stays as it was written.

## 2026-10-19: Every Azure set to the paid cap of 100 repetitions, with a preregistered stopping rule

- **The founder's orders of 19 October** ("I need a 3-run result ... the cap we can run it to ... do all, give all"). The
  twelve Azure runs measured to the end (5 paired repetitions each) swing about ±9% of native's bill, so a cut under about
  9% read STEADY. Every Azure set (`scripts/azure_queue.txt`) now runs up to 100 paired repetitions, the founder's cap for
  paid runs: at 100 a cut of about 3% reads GAIN eight times in ten.
- **The stopping rule** (`tools/stop_rule.py`, `aks-metered.yml` input `stop_looks`): looks after 10, 20, 40 and 70
  repetitions read the bill's paired change with its 99% interval and stop the run once it is read (GAIN, power given, or
  STEADY within ±2% of native's bill); never while the 95th percentile or the failed requests read a LOSS. A stopped run's
  remaining repetitions spend nothing on Azure; the aggregate carries every look (`STOP_RULE.txt`).
- **Counted apart.** A run under the rule carries "to the cap, stopping rule" in its title, so the conductor counts its A,
  B and C from zero; the omni-v11 steady run at 5 repetitions (39162654399, finished 01:46 UTC) stays its own record.
- **Written before any run of it**: `docs/K8S_COMPASS_PREREGISTRATION.md`, the amendment of 19 October, with both arms at
  once on twin clusters written for when Azure's processor allowance for the machine family is raised to 20.
  `tests/test_stop_rule.py`.

## 2026-10-18 (late night): Every workflow names its token's rights

- **The 28 workflows that set no token permissions now read the code and nothing else** (`permissions: contents: read`).
  None of them pushes, starts a run, reads another run's files or signs in through the token: they check out, build,
  run, sign in to a cloud with its own key and upload their files, none of which needs more. Before, their token had the
  repository's default rights. `tests/test_workflow_permissions.py` fails a push that leaves any workflow on the default,
  or gives a read-only token to a workflow that pushes, starts a run or reads another run's files. The threat model's T9
  row is closed.

## 2026-10-18 (late night): The watchdog trusts only its own registry; the threat model

- **Three faults in the switch tool, found and fixed** (`tools/omni_switch.py`; no engine file changes, no decision of any
  governor changes). (1) The watchdog ran every restore command it found in the registry, and stopped every hung
  governor's process, so a record another local user could write (the default registry is under `/tmp`) was a command run
  or a process stopped with the watchdog's rights. It now acts only on a record that it and the registry directory are
  owned by its own user (or root, or a uid named with `--trust-uid`), that is no symbolic link and that no other user can
  write; each record is opened inside the directory without following a link and checked on the open file. Any other is
  refused, named and left in place. (2) A governor that died and whose process number the system gave to another process
  was taken for hung, and that other process was killed. A number now counts as the governor's only while the process
  holding it started before the governor registered (`/proc`); otherwise nothing is signalled and the governor's
  settings are handed back. (3) `off` wrote the switch file through any link planted at its path; it no longer follows a
  link, and every governor is still signalled if the file cannot be written. `status` names what it refused and warns
  when the switch's or the registry's directory can be written by another user. `tests/test_switch_trust.py`
  reproduces each fault on the tool as it stood (the old watchdog killed the process holding a reused number; the old
  `off` overwrote the file a link pointed at) and passes on the fix. Every caller runs the governors and the tool as one
  user (the cloud install's pod as 10001, the GPU scripts under sudo, the kind and KWOK rigs as the runner), so every
  hand-back that worked still works.
- **The threat model** (`docs/THREAT_MODEL.md`, bound into the Owner's Manual after the safety case): what is worth
  protecting, where trust changes hands, twelve threats of misuse with the guard against each, its evidence and what is
  still open, and what would close the open rows. Among them, stated plainly: no outside review or penetration test; the
  default switch directory in `/tmp`, written in an engine file and so moved only by the next engine version; the lock
  file pinning versions, not hashes; the workflows naming actions by tag (402 uses, none by commit); 28 of 53 workflows
  without token permissions of their own. The safety case gains H13; `SECURITY.md`, both manuals and the integration
  manual say how to keep the switch and the registry private.

## 2026-10-18 (late night): The extended fault test; entries added under way keep every started run in its place

- **Two more faults, the ones that blind a governor** (`scripts/kind_faults.sh`, `FAULTS=2`; the amendment in
  `docs/K8S_COMPASS_PREREGISTRATION.md`, written before its run). After the four preregistered faults, which keep their
  moments, the API server's process is stopped for 30 s at 82% of the run, and the metrics server is scaled to none for two
  minutes at 88%, in both arms. Each outage is logged only once it took hold. The API server's process is found by its name
  in `/proc`, so the fault needs nothing the node image may lack. `tools/live_reps.py` reads the two like the four, and a
  four-fault run's table is unchanged.
- **The campaign runs it, A, B and C** (`scripts/reruns.txt`, "kubernetes faults extended", 2,500 s a window so the last
  outage's 300 s of recovery end inside it). `tests/test_faults_extended.py` holds the moments, the name lookup on a
  stand-in process, the table and the window's length.
- **Entries added once the campaign is under way keep every started run in its place** (`scripts/dispatch_grid.py`,
  `rerun_blocks`). The conductor reads a workflow's started runs back by their count, in the queue's order. The three data
  stores at the max, pushed earlier tonight among entries whose A, B and C had all started, would have been read as started
  in their place: MySQL's and MongoDB's tune-down C run would have run twice and their runs at the max A and B never, and
  PostgreSQL's likewise. The conductor reached none of them before the fix (they stood at place 17 and later in its list,
  six a tick). An entry added under way now stands in a block of its own below an `added=<UTC>` line, released after every
  entry above it, A, B and C; the block above is the queue byte for byte as it stood. `tests/test_release_campaign.py`
  freezes every block as its runs began, so an entry put among them fails the push, and `tests/test_run_scale.py` shows
  the started runs keeping their places.

## 2026-10-18 (late night): The referee's summary, the safety case, every data store at the max, the book's last page

- **The referee's summary** (`docs/REFEREE_SUMMARY.md`, bound into the Owner's Manual after "What Omni-Compass Is"): every
  claim with its standing (shown, small or STEADY, modelled, partly proved, or undetermined), every number with its engine and
  evidence class, and every Kubernetes gain beside what it cost. In the add-on tests the cost is the processor given to the
  service: CPU used, the governor's own included, +29% to +57%, shown and not judged under the preregistrations. In the
  stepping load and the public day, CPU fell slightly and the machines held. The bill, energy, the GPU and production are
  written undetermined until their runs exist.
- **The safety case** (`docs/SAFETY_CASE.md`, bound after "The Mechanism of Action"): twelve hazards of a governor on top of
  native, each with the guard in the code that stands against it and the test or measured run that shows the guard holds.
  Also the plug's interface as `omnicompass/muscle_sdk.py` defines it, and what the case does not yet cover (no outside
  security review, no proof of the whole controller, no production deployment).
- **Every data store at the max.** MySQL, MongoDB and PostgreSQL had run only at the tune-down (objective resource). There
  the governor's paired trial refuses most steps that spend memory, so they read STEADY. Their runs at the max (objective
  service, preregistered in each one's own preregistration) join the campaign's queue, A, B and C (`scripts/reruns.txt`).
  `tests/test_release_campaign.py` now holds every data store to both objectives.
- **The book's last page.** The end notice is kept whole, and the last chapter opens under a short space, so the notice no
  longer spills four lines onto an almost empty last page.

## 2026-10-18 (night): The KEDA pod start wait root-caused to the test machine; the kind rig pre-pulls the served image

- **Where the wait goes.** `tools/pod_phases.py` reads every serving pod started inside a measured window from the run's own
  files and splits it into scheduling, the node side and the app with its probe. It places each start by the host's busy
  share and by whether its node already served, and splits the change in the mean between the arms exactly in two: the
  shift of starts into other strata, and the wait in the same stratum. The receipt is `results/live/POD_START_PHASES.md`
  (741 starts, five KEDA runs, omni-v10 and omni-v11). On a node already serving a start takes 1.3 to 1.7 s in both arms;
  on an empty node it takes 7 to 12 s, because the image (`registry.k8s.io/hpa-example`) is downloaded and unpacked inside
  the window on the one runner all kind nodes share. Under the http setup, all of the omni arm's rise in the mean (+1.42 s
  on omni-v10, +0.65 s on omni-v11) is its starts' shift into a busier host (+1.57 s, +1.64 s), the processor its conveyance
  keeps busy. At the same host load on the same kind of node, its starts were as fast or faster (−0.14 s, −0.98 s).
  `docs/POD_START_WAIT.md` sets out the mechanism, the decomposition, the prediction for a fleet of separate machines and
  the threats; it is bound into the Owner's Manual beside the Kubernetes preregistration.
- **The rig fix, the same in both arms.** On kind, `scripts/kind_bench.sh` runs an image pre-puller before each arm
  (`deploy/kind/prepull.yaml`: one pod on every worker pulls the served image), waits for it on every worker, deletes it,
  and records `images=` and the digests in the arm's preflight record. A pre-puller that does not finish marks the arm
  invalid. The operator's manifests, the engine (omni-v11's digest), the loads, the gauges and the cloud sets are
  unchanged. Amendment in `docs/K8S_COMPASS_PREREGISTRATION.md`, written before any run on it.
- **Never two rigs in one table.** The conductor counts a kind workflow's omni-v11 run only when the run's own commit
  carries the pre-puller (`RIG_FILE` in `scripts/dispatch_grid.py`, read from GitHub once a commit; a read that fails for
  any reason but a missing file stops the tick, so no run is counted on a rig it was not read on). The runs on the rig
  before run to their end and stay as their own record. `tools/confirm_abc.py` reads each run's rig from its preflight
  records and heads any table whose A, B and C differ in rig with that fact. In the grid with the real cluster inside the
  amended rig is protocol 4 (`KUBE_PROTOCOL`, carried in each run's name by `six-kube` and `big-organism-detached`); no
  omni-v11 run with the cluster inside had started on protocol 3.
- **The raw archive opens runs saved since it was first opened.** `scripts/raw_archive.sh open` left an existing worktree at
  the commit it was first opened on, so a run saved to the branch afterwards could not be opened (its folder stayed absent).
  It now moves the worktree to the branch's newest commit, keeping any file written there and not yet saved; a clash with
  such a file leaves the folder where it was and says so. `tests/test_raw_archive.py` reproduces the fault and passes on the
  fix.

## 2026-10-18 (late): The Lambda launcher made safe before the first rental; the tests no check ran

- **A give-back that cannot be lost to a moved address.** Lambda moved from lambdalabs.com to lambda.ai. Python's own
  redirect resends a POST as a GET without its body, so a give-back sent to the old address would have arrived as a read:
  the machine would have stayed rented (the eight-card server at about $14 an hour) while the log read "given back: none
  listed" and the step passed. `scripts/lambda_gpu.py` now calls `https://cloud.lambda.ai/api/v1`, follows a moved address
  itself with the same request, only to Lambda's own hosts and never from https down to http (the key is never sent
  anywhere else), and refuses anything else.
- **Every give-back confirmed.** `terminate` reads each machine first (one already given back is fine), gives back the
  rest, and exits 2 with the machine's id when Lambda neither lists it as given back nor reports it terminating. The
  workflow's give-back job asks twice, then turns red and says to terminate it by hand. A launch that fails after renting
  is found by its name and given back (`terminate --name`).
- **The key pair checked at no cost, before anything is rented.** `lambda_gpu.py keycheck` reads the SSH keys Lambda holds
  and checks that the stored private key is the other half of the one named (`ssh-keygen -y`; no key material printed).
  `lambda-gpu` runs it on every run, dry runs too; a missing secret is named, and a missing secret or a wrong pair turns
  the run red with nothing rented (the dry runs of 18 October passed green while saying the secrets were missing).
- **`docs/LAMBDA_SETUP.md`**: the account, the API key, the SSH key, the three secrets, the dry run and the real runs with
  their costs, click by click; bound into the Owner's Manual beside "Running the GPU Benchmark".
- **The tests no check ran.** `python -m unittest discover` collects only TestCase classes. 76 of the 124 test files hold
  none (plain `test_*` functions, or a `main()` under `if __name__`); verify.py called some by name, and 61 never ran in
  any check. `tools/function_tests.py` runs each of them in its own process; verify.py runs it on every push. All 61
  pass after one fix: the modelled self-pilot (`pilot/selfpilot.py`) built the live governor, which starts a `kubectl
  proxy`, before its model's cluster replaced it, so it failed on any machine without kubectl; it now asks for no proxy
  (the governor's fingerprinted file is untouched). Among the 61 is the GPU harness's own end-to-end test on the stand-in
  card (about 7 minutes: the paired run, the compass bench, the organisms with the card inside, the pooled and the several
  cards), so the harness the Lambda runs use is checked on every push before any card is rented.
- **Google's stored text, named once more.** The check of 19:12 read the 595 characters as none of the shapes known, so
  they hold characters plain base64 does not (a dot, a dash, an underscore). `tools/cloud_key_check.py` now also names a
  token or a web-safe encoded string (an access token, for one, which expires within the hour): still not the key file.
  docs/GOOGLE_SETUP.md section 4 gains a new key file by clicks alone (Service Accounts, Keys, Add key, JSON), with no
  terminal; the Operator's Manual (Appendix G) is rebuilt with it.
- **Every workflow pinned to `ubuntu-24.04`.** GitHub announced on the runs' own pages that `ubuntu-latest` moves to
  Ubuntu 26 from 19 October. Every job (113 in 53 workflows) now names `ubuntu-24.04`, the image every run of the engine
  that stands has used, so its A, B and C runs share one operating system; moving to Ubuntu 26 is a step of its own,
  taken on purpose and written down, never a change under a running campaign.
- **The two version 11 runs that failed, and why.** CruiseKube's run 39145612309 (started 16:34, before the raw move)
  measured all ten repetitions and built its table; only its last step, which committed the folder into main's
  `results/live/raw/` (no longer part of main's tree), failed. Its files are its artifacts and are queued for the branch
  raw. Robustness run 39151686324: repetition 8 measured, then GitHub's artifact service timed out on the upload
  ("Request timeout: CreateArtifact"); that one repetition is re-run in place.
- **Azure.** The burst set `1 4 1 6 1 9` (run 39119345316, version 10) finished all five repetitions; it and the steady set
  of 17 October (39080133432) are queued for the branch raw (`.github/archive_request.txt`). The steady set started after
  it is running.

## 2026-10-18 (night): Tightened after the move; the stale branches kept on one archive branch

- **The Google key's shape, in plain words.** `tools/cloud_key_check.py` now says what a stored text that is not a key file
  looks like, from its shape alone and never a character of it: a piece from inside the file (the copy started part of the
  way in), the private key alone, an encoded string, or an account's address. Google's stored secret reads as 595
  characters that do not start with `{`, an encoded string: not the key file.
- **The clouds' refusals at the top of the run's page.** `cloud-check` repeats each pre-flight refusal (Google's quota,
  Amazon's Free plan) as an annotation, so the reason shows without opening the log.
- **The live engine's push.** A merged pull request changed the generated page while the bot pushed its rebuild, and every
  attempt stopped on the same conflict (run 39147114754); the bot's rebuilt page now wins such a conflict (`-X theirs`),
  and the next rebuild reads what landed.
- **GitHub's code scanning** had a Go pass that found Go only inside the raw receipts; with them off main it stopped
  ("no Go source"), and GitHub dropped the pass on its own. Nothing in the repository is Go.
- **Dead weight.** The verify log of 27 September (results/VERIFY_LOG.txt), which nothing reads (the release check's receipt replaced it),
  is removed. The 21 stale branches of 27 September to 15 October (the `xpass25`, `xpass26` and `codex` work branches,
  `v4`, `gpu-omni-v8`, `gpu-omni-v9` and others) are kept whole on one branch, `archive/stale-branches` (one commit whose
  parents are their tips, with each name and commit listed), so every commit stays reachable when their names are removed.
- **Found on the way.** The Lambda launcher ships the commit's tree to the rented machine (`git archive HEAD`); until the
  raw move that tree was 36 GB. It is 149 MB now.
- The conductor's dry run says a check *would* start rather than that one started.

## 2026-10-18 (evening): The raw receipts on their own branch; main's tree is the code and the tables

- **Why.** Main's tree carried 182,161 raw files (35.6 GB of archived runs) and Dependabot's every clone of it timed out after
  15 minutes (`job_repo_not_found`, "Timed out due to inactivity after 900 seconds"), so no dependency update has ever run; a
  buyer's or a runner's clone carried the same weight.
- **The move.** Every folder under `results/live/raw/` is on the branch `raw` by the same tree objects (nothing copied,
  nothing changed: the branch's root tree is the one main held, `78b7ba5c`, with the capacity run committed meanwhile); main
  keeps the code, the tables and the 20-set's checksum list (`results/live/SET20_RAW_SHA256SUMS_ALL.txt`). Main's tree went
  from 184,734 files to 2,577.
- **One helper** (`scripts/raw_archive.sh`): `open` places the branch at `results/live/raw/` as a worktree with only the
  folders asked for (one run in about 2 seconds), so every path a table names reads as written; `has` and `save` work from
  trees on the branch's newest tip (two jobs saving at once never conflict); `sweep` moves any raw folder main still carries,
  keeping a second copy under one name beside the first. `archive-run`, `front-page`, `kind-addons`, `kind-cruisekube`,
  `kind-goldilocks` and `capacity` save through it; `front-page` and `live-engine` open the folders they read
  (`docs/engine/export_runs.py` reads the branch); `raw-sweep.yml` runs every hour and after each of those workflows, for
  runs started before the move; `tools/export_zip.py --include-raw` and the grid page read or link the branch.
  `tests/test_raw_archive.py`.
- README, the Owner's Manual (rebuilt), the dossier and CLAUDE.md say where the receipts are and how to open them.

## 2026-10-18 (evening): Google Cloud and Amazon back on, behind a $0 check

- **Why they stopped.** Every Google set started that morning failed at Google's login ("unexpected end of JSON input"): the
  stored `GCP_CREDENTIALS` had been selected from Cloud Shell's screen and was cut short. Every Amazon set failed at the
  pre-flight: the account is on Amazon's Free plan, whose policy denies every machine read ("explicit deny in a service
  control policy"). Nothing was built or billed; those runs (Google 4, Amazon 8) were on omni-v10's commit and stay as its
  record. The founder's order: "fix the Google and Amazon cloud. To work".
- **The $0 check** (`.github/workflows/cloud-check.yml`): the stored key's shape (`tools/cloud_key_check.py`: its length and
  missing parts only, never a character of it), the login, the plan, the machine type and every quota a set needs, then it
  stops. Google's pre-flight (scripts/gke_paired.sh) now reads the processors in the region and in all regions (the free
  trial's 8 is named, with the fix), the solid-state disk and the external addresses, and gives Google's own words when a
  read is refused; Amazon's (scripts/eks_paired.sh) logs in first, names the Free plan when Amazon's policy denies the
  read, and, in the check, asks Amazon for a short processor quota itself (once; never shrunk to fit). The Google workflow
  reads the key's shape before its login too. Found on the way: the Google workflow switched the project's services on with
  a login whose roles carry no right to do so, so even a whole key would have stopped there; scripts/gcp_services.sh now
  reads them and asks for one only when it is off, naming the fix when the login may not.
- **The conductor waits for it** (`scripts/dispatch_grid.py`, `check_state`): a Google or Amazon set starts only after that
  cloud's newest check passed within a day; the conductor starts a check itself when there is none, the last failed an hour
  ago or more, or the last pass is a day old. Both queues are switched on again; a broken key or a plan that cannot rent
  spends no set's A, B or C, and once the founder's two fixes are stored the sets start on their own within the hour.
- **The setup pages** (bound into the Operator's Manual as appendices G and H): Google's key is now downloaded as a file
  (`cloudshell download key.json`) and pasted whole, never copied from the screen; Google's quotas and the free trial's
  activation have their own section; Amazon's page gains the move from the Free plan to the Paid plan (section 1a) and the
  check's quota request. `tests/test_cloud_check.py`.

## 2026-10-18 (afternoon): Omni v11 stands (a reading with no machine in service is blind); every version lands in one command; the model gate's arms each run their own engine

- **omni-v11** (`OMNI_V11.json`, digest `745aa53ec8eeb67b`, 47 files; `docs/OMNI_V11.md`): omni-v10 with one guard in the Kubernetes
  governor (`omni_controller/controller.py`). When the cluster's reading shows no machine in service, the decision holds: it is
  recorded with its reason, nothing is decided from the reading, nothing is written, the floor check returns, and the last
  reading with machines stays the bound on the conveyance. Found in the omni-v10 CruiseKube test (run 39120444653, repetition 8):
  every kind worker left service for two minutes while the service answered every probe, and omni-v10 fed its engine the highest
  overload, then divided by the empty capacity (two decisions and one floor check failed, each writing nothing).
  `tests/test_blind_reading.py` reproduces the fault on omni-v10 and passes on omni-v11. The founder's order: every fault found is
  fixed, none set aside.
- **The model gate** (`results/model_gate/V11_VS_V10.md`): the candidate against omni-v10 on seeds 1 to 8, every model, each arm proven to run its own checkout: every gauge and count identical (39 of 39 gauges), and in the new blink model omni-v10's decision failed 64 times where omni-v11 held 64 times with no error. Four model rows read LOSS against native on both engines alike (the pod start wait under conveyance +9.0%, the pending-pod minutes and response at a decision every 15 s, the blink model's alert minutes +2.35%): the next version's work, in the gate first.
- **The model gate's own fault, found and fixed.** From omni-v9's gate (17 October) on, `tools/model_gate.py` put its own tree ahead
  of the checkout under test, so both arms imported the candidate's engine. omni-v9 and omni-v10 changed no file any model runs,
  so their "identical" readings hold by construction (a correction stands on each page). The gate now places the checkout
  first, every worker names the tree its engine came from, and a reading taken on the wrong tree is refused
  (`tests/test_model_gate_tree.py`). It also gains the blink model: the cluster model with every machine out of service in the
  governor's reading for two minutes every six hours, the failure the real run met.
- **Version after version, nothing left behind** (the founder's order of 18 October: "version 10, 20, 30, 40 ... keep updating
  and moving and tightening ... leaving everything intact, only upgrading what keeps moving"): `tools/land_engine.py vN --since
  <UTC>` lands a version's bookkeeping in one command (the fingerprint, the version list, the conductor's campaign, the grid's
  manifest and its three workflows, the reruns header, the package, the root list, a release group), and lists the words a
  person writes next. `tools/land_engine.py --check`, run by `verify.py`, refuses a push in which any of those places, or the
  front page, CLAUDE.md, the manual or the live engine's page, still names an older engine as the one that stands
  (`tests/test_land_engine.py`). omni-v11 is the first version landed that way.
- **Everything runs again on it**: the conductor's campaign, reruns, grid (`results/grid_v11/`) and Azure sets from A; the
  omni-v10 runs already started run to their end as omni-v10's record (nothing is cancelled). The package is 0.11.0.
- **Pages brought up to it**: README, CLAUDE.md, the state of play (which also still said Google and Amazon were running; both
  queues are paused until Google's key is stored whole and Amazon's account is on its Paid plan), the receipts, both manuals
  (rebuilt), the live engine's page and appraisal, the v10 page, the preregistration (an amendment).

## 2026-10-18: Omni v10 stands (the battery glide that cuts the bill most); the CityLearn receipt reads by the key

- **omni-v10** (`OMNI_V10.json`, digest `4bf39b0d707784de`, 47 files; `docs/OMNI_V10.md`): omni-v9 with one file changed, the
  CityLearn runner. The battery wire's glide goes from 0.0625 to 0.0875 of the command's range an hour, the speed on omni-v9's
  ladder that cuts the bill most with no LOSS, read by the one key (the founder's rule: use everything that can be used, keep
  everything healthy, never raise the bill, hurt no one). Read on CityLearn 3.0.2 before any GitHub run: the bill −16.09% in the
  robustness district, −20.05% in the tuning district, −19.17%, −8.43% and −16.08% in the 2022 phases 2, 3 and all (omni-v9:
  −14.22%, −17.63%, −17.22%, −7.32%, −14.20%); no LOSS against native in any district read before the push (the two
  100-building neighbourhoods were still running locally: no price, no outage, no score there that can read LOSS moves with
  the glide; their three runs on GitHub decide). The trade, shown: the electricity bought,
  the carbon and the peaks fall a little less than on omni-v9, every one still GAIN, and two rows of the 2022 phase 3 are power
  given (the ramping +6.18%, the net-zero shortfall +0.25%).
- **Refused before it**: steering the outage buildings' batteries outside the outage hours (native through each outage). On six
  2023 districts it cut the energy not served in five, but raised it 0.69% in one (a LOSS) and raised the bill 0.19% in another;
  those batteries stay native all year, as in omni-v8.
- **The runner's own receipt reads by the one key**: `tools/run_citylearn.py` printed "same", "lower" and "higher" under "the aim
  is lower", which read a higher peak as if it were a miss. Each row now reads GAIN, STEADY, LOSS (a miss that rose) or power given (a
  resource spent or held that rose), and the across-districts table says which word a rise takes; `tests/test_citylearn_wire.py`
  holds it there.
- **The model gate** (`results/model_gate/V10_VS_V9.md`): the candidate against omni-v9 on seeds 1 to 8; no model reads the CityLearn
  wire.
- **Everything runs again on it**: the conductor's campaign, reruns, grid (`results/grid_v10/`) and Azure sets from A; the package
  is 0.10.0.
- **Google and Amazon's first sets (18 October, 04:57)**: both clouds took their keys and spent nothing. Google's login refused
  the stored key as incomplete JSON (the key block was cut short when copied; the founder stores it again whole). Amazon's
  login worked, and its pre-flight found no machine type offered in us-east-1. That check had hidden Amazon's own reason,
  so scripts/eks_paired.sh now prints AWS's error (a new account not yet verified, a region not enabled) instead of
  reading every refusal as "not offered"; the keys themselves are never printed.
- **Google's queue paused until its key is stored whole** (scripts/google_queue.txt), so failed logins do not use up
  its A, B and C; the failed steady A is re-run in place once the key is right. Amazon stays on: its next set prints AWS's
  own reason through the repaired pre-flight.
- **Amazon's reason, read (06:31)**: "not authorized to perform ec2:DescribeInstanceTypes with an explicit deny in a
  service control policy" of an AWS-run organization: the limit Amazon sets on an account on its Free plan. The queue is
  paused until the account is on the Paid plan; the seven sets that failed at the pre-flight (four A, three B, all at no cost)
  are re-run in place, then the switch goes back on. The omni-v9 runs already started run to their end as omni-v9's record; nothing is cancelled.
- **The day's failed repetitions, root-caused (14:30)**, each run again in place (same run, same commit):
  - The CruiseKube test, run 39120444653, repetition 8: every worker of the kind cluster left service for two minutes while
    the service answered every probe. The governor wrote nothing, and two of its decisions failed on the empty reading. A
    window with no machine in service is now refused in either arm, because its machine count is wrong; the capture keeps
    each node's taints and conditions at that moment; a failed decision is named by its error.
  - The KEDA test, run 39108180989, profile both, repetition 2: the native arm's set-up met the HTTP add-on's scaler still
    stopping after its rollout. The ScaledObject now waits for the scaler and is touched once a minute until KEDA builds the
    autoscaler whole.
  - The Azure steady A (omni-v10, run 39100680671), repetition 4: Azure's four new workers did not report Ready in ten
    minutes, before either arm began. The workflow's clean-up deleted the cluster, so nothing was left billing; the other
    four repetitions finished.
  - The benchmark repetitions (run 39107180703, repetition 7): GitHub lost the runner.
  - The organisms with the cluster inside, ×10 (run 39106236972, the spine): GitHub's artifact store timed out on the upload.
  - For the next engine version, with the founder told first: when no machine is in service, the Kubernetes governor's
    decision ends in a division by zero. It writes nothing either way, as the audit shows, but the decision should record
    the reason in words. (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendment of 18 October.)
- **Pages brought up to it**: README, CLAUDE.md, the state of play, the receipts, both manuals (rebuilt), the v7, v8 and v9 pages,
  the preregistration (an amendment, appended), the index's text. Retired words found and fixed on the way: the Owner's Manual
  and the README still named the 2022 robustness district's +0.11% unevenness, and the 2023 districts' ramping and highest peak,
  as LOSS (power given by the key); the state of play still said "SAME AS NATIVE" for STEADY.

## 2026-10-17 (night): one key for every gauge; every result read again; no LOSS on the engine that stands

- **The founder's correction**: "a minus doesn't mean a loss and neither does a plus mean a gain if you don't understand what it's
  against." A peak, a swing, an unevenness and wear are power held, and a rise is **power given**, never a LOSS, as a cluster's
  peak power always read; work per energy that falls is power given too (it falls when more power is given for the same work).
  LOSS is time waited, missed or failed that rose, or work that fell.
- **Where the words had been wrong**: `tools/citylearn_abc.py` filed CityLearn's peaks, ramping and unevenness as misses (12
  rows of the omni-v7 table printed LOSS that are power given); `tools/six_kube_report.py` and `tools/grid_v5.py` judged the
  organism's work per energy as work (21 grid squares printed LOSS that are power given); `tools/gpu_reps.py` and
  `tools/benefit_sheet.py` the same for work per energy. All of them read through `tools/readings.py` now (`SPENT_GAUGES` holds
  CityLearn's five power scores; a new aim, work per resource), and the key's own words name the power drawn, its peaks and
  swings, and wear.
- **Every table read again** (no number moved, only the word beside it): the newest three-run tables, 22 benchmarks and 794
  judged rows, read 211 GAIN, 509 STEADY, 50 power given and 13 LOSS, with 11 rows where the runs disagree or do not reproduce. The
  13 LOSS are the energy not served and the time uncomfortable in CityLearn's seven 2023 districts on omni-v7, the occupants'
  misses, repaired in omni-v8 (those batteries stay native); the levels page says so beside each row. On the engine that stands,
  no LOSS. `results/live/V7_CITYLEARN.md`, `results/grid_v5/GRID.md`, `docs/LEVELS.md`, the benefit sheet, the index, the state
  of play, the v8 and v9 pages (whose own tables now carry the key), the preregistration (an amendment, appended), README,
  CLAUDE.md and both manuals rebuilt.
- **What the wrong words cost**: omni-v9's battery glide stopped at 0.0625, where nothing rose; read by the key no glide from
  0.05 to 0.10 reads a LOSS, and the bill falls further up to 0.0875 to 0.10. And omni-v8 refused a repair (native only in
  outage hours) that cut both misses. Both go to the next engine version, read on CityLearn first.
- **A false stop in the Kepler add-on, found by a failing test**: the meter check `kubectl … | grep -q` quit at its first match,
  the writer died of a broken pipe, and under `pipefail` a working meter read "Kepler reports no node energy" (real Kepler
  output is thousands of lines, so a real run would have stopped there). The same pattern guarded the governor's permission
  checks (`! sed … | grep -q`), where a cut pipe could let a missing or forbidden permission pass. All eight now read the whole
  stream (`grep … >/dev/null`), and `tests/test_pipes.py` keeps any script from bringing the pattern back.
- **Three stuck things unstuck (18 October, after midnight)**: (1) every grid run with the real cluster inside that carried the
  spine failed at its report (`tools/six_kube_report.py` ordered six organisms, not seven: "'spine' is not in list"), so those
  squares produced no table; the spine now leads the order, and `tests/test_six_kube.py` holds the report to the seven names.
  (2) The front-page bot failed on its last two runs: the manifest refresh could not import `tools` when run as a script, and
  the v9 page's closing notice was not in the standard form the legal fixer writes; both fixed. (3) The Azure burst of 17
  October (run 39014972717, omni-v7, finished 23:43) is sent to the archive so its table can be built.

## 2026-10-17: Omni v9 stands (the battery reads the coming hour); native as shipped; every level on one page

- **Omni v9 is the engine that stands** (the founder's orders of 17 October: the fix proven in our own runs and in the model gate
  before it is pushed; tuned "to exploit all that can be and keep all healthy and never raise its bill"): `OMNI_V9.json`, digest
  `7379f3a79ff2c475`, 47 files, `docs/OMNI_V9.md`; package 0.9.0. The CityLearn battery wire reads the coming hour (the mean of
  the same hour over the past seven days, only hours already seen) and glides at up to 0.0625 an hour, the fastest glide that read
  no LOSS on any score in any district (0.05 left one district's daily unevenness LOSS; 0.075 and faster raised another's ramping).
  The reading of the hour gone had run about five hours behind the day and left the batteries empty at each month's top hour: the
  cause of omni-v8's one LOSS row, the 2022 robustness district's monthly unevenness (+0.11%). Read locally on CityLearn 3.0.2 on
  every battery district outside the 2023 set: no LOSS on any score (the robustness district's monthly unevenness −2.29%); the
  shipped runner equal to the study's copy to the last digit; the model gate identical to omni-v8 on every model
  (`results/model_gate/V9_VS_V8.md`). Every 95% interval now takes the exact Student t quantile (`omnicompass/student_t.py`);
  every tabled value is unchanged and no published reading moves. Disclosed in `docs/OMNI_V9.md`: the narrower repairs refused,
  the speed ladder, and the months whose peak hour still rises above native's though no score counts them.
- **The version tool fingerprints a new engine file before its first commit** only when it is staged; v9's new file was staged
  so the fingerprint holds it (a gap found while declaring v9). The model gate's page names every changed engine file, not only
  the last one printed.
- **Native as shipped** (the founder's order of 17 October): MySQL, Redis and MongoDB run with native exactly as the vendor ships
  them (`--native shipped`; the 128 MB pool, no memory ceiling with `noeviction`, half the machine's memory less 1 GB) beside the
  operator's setting; where the factory setting is already above Omni-Compass's cover, it writes nothing and reads "at its limit on
  native". Three entries in the omni-v9 campaign; preregistration amendments written for each.
- **Every level on one page** (`docs/LEVELS.md`, `tools/levels.py`, checked by `verify.py`, linked from the README and the state of
  play, bound into the Owner's Manual): the muscle, the organism, the cluster, its add-ons, the service, the plant, the cloud and a
  group of clusters, each with its counts and every gauge that goes the other way named.
- **The manuals' navigation checked row by row, and the checker made exact**: every Contents row, every figure and every index
  reference in both manuals lands on its printed page (a file name split over a page break or wrapped in a cell is read whole).
- **Smaller**: every Python file compiles and reads no undefined name (`tools/lint_names.py`, in `verify.py`); the archive bot
  gzips bulky raw logs before it commits them; the GPU receipt's wording; the requirements lock regenerated for Python 3.12.
- **The front-page bot keeps the reading key**: it rebuilt seven omni-v7 receipts (Kafka twice, PostgreSQL, Redis twice, MySQL,
  MongoDB) without the key at their top, and `verify.py` caught it; the key is back on all seven, and the bot now writes it on
  every table it rebuilds (`tools/readings.py --fix` in `.github/workflows/front-page.yml`). No reading moved.
- **The clouds and the GPU, checked without spending a cent** (a dry run of the all-benchmarks button, 17 October): the Azure
  key is in the repository; the Google, Amazon and Lambda keys are not, so their queues stay off and nothing there can start.

## 2026-10-17: Omni v8 stands (the outage battery left native); everything runs again on it

- **Omni v8 is the engine that stands** (the founder's order of 17 October: "there's a new version 8 ... push in all and update
  all"): `OMNI_V8.json`, digest `f93d233136a1f902`, 46 files, `docs/OMNI_V8.md`; package 0.8.0. It is omni-v7 with one wire
  changed, the CityLearn runner (`tools/run_citylearn.py`): a battery whose building simulates power outages (CityLearn's own
  `simulate_power_outage`) stays native, because its charge is also the building's reserve; every other battery is steered
  exactly as before, and each district's file says how many batteries were left native for outages. The other 45 engine files
  are omni-v7's bytes.
- **Why**: omni-v7's CityLearn table read LOSS in all three of our runs in the seven 2023 districts, the only ones with outages.
  Found on CityLearn 3.0.2 itself, run locally on the same districts and reproducing omni-v7's numbers to the last digit; three
  narrower repairs (charging only, native during outage hours, no more than the band's excess) each left a LOSS on the tuning
  district and were refused. Read locally before any GitHub run: the 2023 districts native's to the last digit; the 2022
  robustness district identical to omni-v7's GitHub run on every gauge of both arms. The amendment is written into
  `docs/CITYLEARN_PREREGISTRATION.md` (every district has now been seen; it is reported on all). The robustness district's
  monthly unevenness (+0.11%, LOSS) is not changed by it and is the next repair.
- **The model gate** ran omni-v8 against omni-v7 on seeds 1 to 8 (`results/model_gate/V8_VS_V7.md`): every gauge of every model
  identical, to the last digit; the change touches no Kubernetes, card or cloud controller.
- **Everything runs again on omni-v8**: the conductor (`scripts/dispatch_grid.py`) counts the reruns, the grid and every Azure
  set from the moment omni-v8 landed (the grid on its own manifest, `results/grid_v8/`); `scripts/reruns.txt` is the omni-v8
  campaign, the steady and wandering Kubernetes tests back in it. The omni-v7 runs already started run to their end and stay
  omni-v7's record. **The conductor reads the engine of the commit its runs start on** (the branch's newest commit, fetched each
  tick), not of its own checkout, so a tick that began before a new engine landed starts the new engine's runs at its next round
  instead of standing idle for up to five hours. **The campaign has a start time** (`SINCE`, set a little after the push): the
  conductor starts nothing before it, so no run of the engine before it can be counted in omni-v8's campaign.
- **The realms table run again on omni-v8** (`results/realms_v5/REALMS_V5.md`, commit `9819a903cba3`, seeds 3000-3009): every
  reading of the 1,107 muscles and the seven organisms the same as on omni-v7, to the digit; only the run's header changed.
- **Archived**: the kill test's three omni-v7 runs on the fixed harness (39040151044, 39040156477, 39040161755; all finished)
  and Azure's steady set A (38981149348, finished), requested in `.github/archive_request.txt`; their tables follow as
  omni-v7's record. Azure's burst `1 6 1 8 1 6` runs now.
- **Every page on omni-v8**: CLAUDE.md, the README, the state of play (its omni-v7 summary kept whole in
  `docs/history/STATE_OF_PLAY_2026-10-16.md`), both manuals (the Owner's section 3.5 rewritten from the omni-v7 tables, its
  engines table, section 16.5's CityLearn paragraph; the Operator's engine lines), the receipts page, the index's notes, the cloud
  setup pages, `docs/OMNI_V7.md` and `docs/OMNI_V6.md` marked as the engines before it, codemeta. Both PDFs rebuilt. The branch
  `v8` carries the engine that stands, in step with `main`; `v7` and `v7-candidate` are kept level.
- **GitHub's verify failed on the landing push (4d9e9da42) and is fixed**: the new conductor test set `FETCH_HEAD` with
  `git update-ref`, which GitHub's git (2.55) refuses for a pseudoref while the local git (2.43) allowed it; the test now writes
  `FETCH_HEAD` as a fetch does. The conductor's code was not at fault; every other check passed on GitHub.

## 2026-10-17 (late night: every page on the omni-v7 tables; the whole test suite in the push check)

- **The Omni index reads only omni-v7 tables**: +4.2% GAIN on the resource reading and +11.5% GAIN on the service reading
  (real Kubernetes +27.2% over seven tests, the cache +0.2%, messaging +0.1%, the three databases exactly nothing). No table of
  an earlier engine is read beside them; the steady and wandering Kubernetes tests, Azure and the card join as their omni-v7
  tables land (`tools/omni_index.py`, `results/OMNI_INDEX.md`).
- **The benefit sheet, the wiring page, the state of play and the receipts page** read the omni-v7 tables
  (`tools/benefit_sheet.py`, `tools/wiring_verdicts.py`, `tools/summary.py --fix`, `docs/THE_RECEIPTS.md`): 20 of 24 benchmarks
  on the engine that stands.
- **The Owner's Manual's results chapter** (sections 16.1 and 16.4 to 16.6) is rewritten from the omni-v7 tables, gauge by
  gauge, native against Omni-Compass on top, the CityLearn LOSS rows and their cause in the same paragraph as its gains; the
  sections as they stood on omni-v1 and omni-v3 are kept whole in `docs/history/OWNERS_MANUAL_RESULTS_V1_V3.md`.
- **The whole unit-test suite runs in the push check** (`verify.py`, 212 tests, about two and a half minutes): one failing
  test now stops a push. `tests/test_robust_restart.py` had failed for two days because no check ran it.
- **The figures are written the same way every time**: the drawings no longer stamp a render date or random clip ids
  into their SVG files (`docs/book/schematics.py`), so a figure's file changes only when its drawing does.
- **The steady and wandering Kubernetes tests had dropped out of the omni-v7 rerun list**; they are released with the next
  campaign.

## 2026-10-17 (night: the first omni-v7 reruns read back: seventeen three-run tables)

- **Seventeen three-run tables on omni-v7** from the reruns released on 16 October (A, B and C, separate GitHub runs,
  archived in `results/live/raw/`): Kubernetes all four in one run, fairness, faults, the batch queue, the Google 2011
  day and the long robustness run (`tools/confirm_abc.py`); Redis and Kafka, each for resource and for service; PostgreSQL,
  MySQL and MongoDB; the robot arms, the power grids, the buildings and batteries, the drone swarms (each with its own
  tool). Written to `results/live/V7_*.md` with their JSON. Every row is shown. No LOSS in sixteen of them. **CityLearn
  reads LOSS in all three runs on four of its eleven scores in the 2023 challenge districts** (energy not served +2.0 to
  +9.8% in seven districts, time uncomfortable +0.01 to +0.15% in six, ramping +4.5 to +6.2% in seven, highest peak +2.5%
  in three, monthly unevenness +0.07 to +0.11% in two), beside GAIN on electricity bought in all ten districts with
  batteries and on the daily peak in all ten. The same rows moved the same way on the engines before; the battery wire
  (`tools/run_citylearn.py`, a file of the engine's fingerprint) moves the batteries on the district's draw alone and
  does not read the outage hours those districts carry, so the fix belongs to the next engine version, in the model gate
  first. Redis service and MySQL each have one row where the runs point different ways; the swarm's three shown-only
  gauges (closest approach, tracking error, cruise level) did not reproduce to one part in a thousand across machines.
  The 1,107-muscle realm study reproduced the committed result exactly in all three runs. The CPU governor's three runs
  ran only their capability check: the measured run starts only on a machine with a power meter and frequency control,
  which GitHub's runners do not give, so it waits for such a machine (none is rented without the founder's word).
- **The full-control scorer reads one fact once.** `pilot/score.py` read a fall in utilisation as LOSS in the run that
  read the rise in node-hours as power given: both say the governor held more machine for the same work. A fall in
  utilisation now reads power given, as the node-hours do; the test covers the reverse pair.

## 2026-10-17 (night: three harness faults found in the finished reruns and fixed)

- **Azure runs no longer cancel each other.** GitHub keeps one waiting place in each concurrency group, and every Azure
  workflow shares one group per region (`azure-benchmark-<region>`); the conductor treated each machine size as its own
  queue, so a second start in the same region cancelled the first one waiting. Six reruns were lost that way before any
  machine was made (the Azure full-control burst and the large organisms). The conductor now starts one run at a time in
  each cloud and nothing while one waits or runs: A of every queued set, then A of the cloud's reruns, then B, then C. A
  cancelled run no longer counts as started, so the six are released again (`scripts/dispatch_grid.py`; tests in
  `tests/test_run_scale.py`).
- **The robustness kill test's second governor starts.** omni-v7 added `GIVE_BACK_ONLY` to the governor's command line on
  15 October; `scripts/kind_bench.sh` did not export it to the robustness script, which runs under `set -u`, so the
  governor restarted at 50% of the window stopped before it began and the three kill runs on omni-v7 were invalid in every
  repetition (6 of 15 decisions). The hand-back itself worked. The variable is exported, the script records whether the
  second governor really started, and a test fails if any variable the restart reads is not exported
  (`docs/ROBUSTNESS_PREREGISTRATION.md`, "On omni-v7"). Three new kill runs are released.
- **The realms runner's import.** `tools/run_realms_v5.py` used `receipt_key` without importing it: the three realms reruns
  on omni-v7 stopped writing their page after their CSV, JSON and run record were written. The import is added; the
  page is rebuilt from the archived JSON.

## 2026-10-17 (evening: one numbering, every reference realigned, the figures audited against the code)

- **One numbering in both books, every reference realigned to it** (the founder's order of 17 October: "once you change
  one page, everything changes"). Each book numbers its own chapters and sections in the order they print (chapter.section,
  chapter.section.subsection; an appendix by its letter), whatever label a bound page carried, and every reference in the
  text ("section 16.4b", "chapter 6", "Appendix E", "Part VI") is rewritten to the book's numbers at build time. The
  repository's pages bound into the Owner's cite the Operator's Manual ("the manual, section 4.5"); they are read onto the
  Owner's own sections that carry the same text. A reference to another document's numbering (`LICENSE`, section 10;
  `DISCLOSURES.md`, section 4; `docs/FORMAL_V5.md`, section 5; the founder's manuscript) keeps that document's numbering.
  The build lists every reference that resolves to nothing: none in either book. The navigation check reads every
  reference back against the headings of the built book (its heading pattern fixed: it had read "1.1" as chapter 1 and
  never matched "10."): 336 in the Operator's and 209 in the Owner's, each naming a heading. The Owner's now binds the two
  pieces of the Operator's that its text cited and did not carry (the chapter on the frozen engines and the three-run
  rule, and the appendix on reproducing everything from a clean machine), and its chapter 8 subsections are headings.
- **The figures read against the code, arrow by arrow.** The compass law's loop had its summing junction's signs swapped
  (e = p − c: the position enters plus, the centre minus); corrected. The verdict's three drawings (the block diagram, the
  flowchart, the timing diagram) showed the rule of the engines before v7, the medians alone with n ≥ 30 on every muscle;
  they are redrawn to the engine that stands (`omnicompass/verdict.py`, `judge="interval"`): the 95% interval of the
  change in log cost read GAIN, STEADY or LOSS, an interval wholly above zero refused, a wide one measuring on up to 3n, the
  median and the mean guards, and the controllers' own numbers (Kubernetes: n = 200 response times, trials 600 s apart, a
  phase abandoned past 1,200 s, a refusal resting 7,200 s; a card: n = 30, 8, 30 and 900 decisions). The flowchart is now
  two figures. The release gate is redrawn as the code tests it (`node_release_gate`, then the controller's own rule):
  nine reasons in their order, among them one machine left, the remaining machines at or under the utilisation target ρ
  (not "95% full"), the machine organ's own authority, and one release a minute; with what asks for it (the compass
  law's force past −0.2, the verdict's deepest step) and the cruise override. The authority diagram carries the calm
  formula and the thresholds (0.5 for the pods, 0.7 for the machines). The captions, the Operator's sections 1.2 and 6.1,
  the Owner's sections 1.2 and 7.1, and the Owner's Appendix C state the same rule and numbers.
- **The rest of the drawings, read against the code.** The cache rule is redrawn in its code order (fail up first, then grow, then
  give back): Redis grows on any slow second with the cache full, MongoDB and MySQL only while their misses reach 1% of
  the requests; growth is ⌈F / 0.1⌉ notches, at least one, not one; Redis gives a notch back when nothing was evicted in
  the last second, the other two when their misses are under 1%. The card governor's state machine now shows that it
  holds steady only under an operator's cap, that it may go from learning straight to pacing, and that fail-up and
  observe-only are entered from any state. The feed's blind case is read as past the wall (nothing given back, capacity
  added; in the cloud mode every parked machine woken), not as a hold. The stack schematics name the release gate only on
  the machines, where the code has one; the other muscles give back under their own rule and the verdict. The clocks'
  180-second clean line is the pods', the clock's and the power's; a machine needs no breach now. The lease limit is five
  periods, at least 2 minutes on Kubernetes and 60 s on a card. The muscle's life cycle shows the wire check's failure
  path, and the SDK's mode step names every mode that writes nothing. Captions in both manuals and `docs/GPU_BENCH.md`
  say the same.
- **The books:** the Operator's 496 pages with 50 figures, the Owner's 1,249 pages with 77; 487 and 1,240 pages at least
  four fifths used. Text references fixed at their source in `LICENSING_FAQ.md`, `docs/THE_RECEIPTS.md`,
  `docs/HOW_TO_READ_THE_RESULTS.md` (it now points to the Owner's chapter 3), `docs/CLAIMS_REGISTER.md` and
  `docs/TWO_WAY_NERVOUS_SYSTEM.md`. `CLAUDE.md`: the `v5` branch is history, never merged either way.

## 2026-10-17 (the navigation of both books, checked row by row)

- **The page number in both bottom corners, the running head on every page** (the founder's orders of 17 October). Every
  page but the title page carries the book's name at the head on the left and the part or chapter it belongs to on the
  right, so a reader flipping through always knows where they are (the part and chapter openers and the front matter
  included: Copyright and License, Contents, List of Figures, each named), and the page label in the left and the right
  bottom corner. The notice stays centred at the foot of every page.
- **Every figure where the text names it.** The builder had measured every figure as "taller than the page" (reportlab's
  answer to a kept-together block is "split me", not its height), so no figure ever sat under its own paragraph: every
  one floated to the next page top. It now reads the block's own height: a figure that fits under the paragraph that
  names it stays there; one that does not floats to the top of the next page, before the text that follows, and never
  further; a page never carries more than two; figures land in the order the text names them, and a figure is placed
  only with room to spare so its caption never parts from its drawing. A wiring caption longer than a few lines is cut
  at a sentence end: the first sentences stay under the drawing, the stack's rules follow as text right under the
  figure wherever it lands, so a drawing and its caption always fit one page. In the sources every figure line now
  stands under the paragraph that names it: the ten receipt charts had stood in one block under the first paragraph of
  the Owner's section 16.1, and the catalog grids, the cloud, the stops, the paired run, the cache rule, the trial, the
  reading rule and the model gate each had a cluster of their own. The Owner's chapter 16 carries a subsection of its own
  for the engine that stands (16.1b): one paragraph per three-run table of omni-v7 (Goldilocks, KEDA's two add-on
  tests, CruiseKube, the capacity test), each written from the table's own readings, GAIN, STEADY and power given with the
  numbers, with its judged chart and its shown chart under it, and a paragraph on how a receipt comes to be over the
  mechanism chart. The Owner's had carried the three-run figure twice (chapters 14 and 15); it stands once, in chapter
  15 where the rule is defined: 73 figures in the Owner's, 49 in the Operator's.
- **The capacity table's title named the wrong engine.** `tools/capacity_abc.py` wrote "(Omni v5)" into the title of
  every table it made, so the omni-v7 table (`results/live/V7_CAPACITY.md`) carried it over runs on omni-v7. The title
  now names the engine the three runs were on, read from the runs, and the table is corrected.
- **The index pointed to the wrong pages, now fixed.** reportlab's index recorded the physical page count from the title
  page, while the book's page labels restart at 1 where the body begins, so every index reference was off by the length
  of the front matter (26 pages in the Operator's, 34 in the Owner's). The index now records the page label the reader
  sees, roman in the front matter and arabic from the body's page 1, and the navigation check reads each reference back
  from the page it names. A second fault, found by that check: every index tag of a paragraph stood at the paragraph's
  start, so a paragraph split over two pages indexed a term printed on the second page under the first (one reference
  in seventy, one page early). Each tag now stands right after the term it names, in the paragraph's or the table
  cell's own markup (after it, because a zero-width mark before a term that is carried to the next line stays on the
  line before, and so on the page before at a page's foot; a mark inside the term would let the line break there).
- **A paragraph that names a figure waits for the figures before it.** Full-page charts named by short paragraphs ran
  pages behind their text: the ten receipt charts of the Owner's chapter 16 stood up to five pages after the paragraph
  that read them, four other figures between. A paragraph that names a figure (with the heading it opens under) now
  never starts on a page already four fifths used while an earlier figure waits, nor on a page over half used while two
  or more wait: the waiting figures take the next page tops and the paragraph follows them, so a figure stands under
  its paragraph or on the next page, one page further only where the figure before it took the page between. The wait
  may leave the one page before a run of full-page charts between half and four fifths used (one page in each book,
  at 55%); without it the text ran a whole paragraph ahead of its figures for the rest of the run. The two books: 484
  of 493 pages and 1,230 of 1,239 at least four fifths used; the rest are the title pages, the last page of the front
  matter and of the book, that one page, and chapter ends at 70% to 79% where the next chapter's opening did not fit.
- **The navigation checked, row by row, on the built PDF** (`docs/book/nav_check.py`, run on both books before the
  push): every Contents row's page against the page where its heading is printed, every List of Figures row against the
  page of its caption, every figure against the paragraph that names it, the index's references against the pages they
  name, the running head and both corner numbers on every page; it exits 1 on a missing head or corner number, a page
  with more than two figures, or a figure further than the next page from its paragraph.

## 2026-10-16 (night, the second figure kit: the wiring, the mechanism and the receipts drawn)

- **Fifty-eight more figures, drawn with a second tool** (the founder's order of 16 October, night: the Owner's Manual at a
  thousand pages needs fifty images that interpret the code, the wiring and the receipts, drawn with another kit so that they
  do not all look the same; everything drawn before is kept). `docs/book/schematics.py` draws them with schemdraw and
  matplotlib from the book's own code and the repository's own files: **wiring schematics** for every stack in the grammar
  of an electrical drawing (the governor with its sense terminals S1… and motor terminals M1…, the motor bus through the kill
  switch into the plug that carries the system's own command, the native controller setting the muscle, drawn as a
  potentiometer with its cover, the system under native with its meters, and the wire in back to the senses): Kubernetes in
  the cluster, the managed cloud cluster on the machines alone, the connection pooler, the message broker, the cache, the
  storage-engine cache, the buffer pool, the graphics card's two wires, the machine's frequency governor, the data center,
  the three simulators, the drone swarm, the response-time feed, the deployment on a managed cluster and the muscle SDK's
  runtime; **block diagrams** of the compass law as a closed loop, the engine to the authority, the verdict's paired trial,
  the card's two wires as an antagonist pair, and the nervous system's authority as logic; **flowcharts** of the wire check,
  the paired run, the eight phases, the release gate, the three stops, the model gate, the reading rule, parking and waking a
  machine, one tick of the conductor, the verdict's trial and the cache rule; **timing diagrams and modelled traces** (class
  S, said so in every caption): the clocks, the law answering a load step, the hand-back after a stop, the cloud sets' load
  schedules, the three loads, one pedal over a burst, a trial from reference to verdict, the engine answering a pulse, the
  force surface and the damping curve; **the receipts charted from their own tables**: Goldilocks, KEDA's two add-ons and
  CruiseKube (the judged rows with their three intervals and readings; the rows shown and not judged), the capacity test, how
  a receipt came to be (the governor's inputs beside the service's outputs), the seven organisms under the three loads, the
  two grids (modelled; with the real cluster inside) and the benefit sheet; and **the structure**: the families of the spine
  and of each realm, the pipeline from the audit to the one number, and three state machines (the modes, the card governor,
  the life of a muscle). A chart of a receipt pictures the table and adds nothing to it. `build_book.py` dispatches both
  kits by key; the List of Figures covers both; every figure is drawn to fit the page and is never scaled below its type
  (the wire check, the release gate, the paired run and the benefit sheet are each two figures, "continued"). The Operator's
  Manual carries 49 figures (the wiring, the flowcharts, the timing and the structure; no receipt charts and no engine
  internals); the Owner's carries 74, every one, three of them on the bound GPU bench page. The same drawings stand as SVG
  files in `docs/book/figures/`.
- **Every word inside its cell, at 9 pt** (the founder's orders of 16 October, night: no text wrapping outside its shape in
  any figure; the shells kept and the type set to 9 pt; every figure read at referee level). Both kits set their type at
  9 pt. The second kit measures every label in its own face before it draws it, wraps it to the width of its box, keeps a
  number and its unit on one line, and records any label that would not fit (`schematics.OVERFLOWS`; the build writes
  every figure with that record empty). All 76 figures were rendered and read one by one: every label sits inside its box,
  every flowchart's branch is labelled yes or no in the same type, every state machine's edges are numbered and keyed, and
  every chart names its axis and unit. The benefit sheet's chart reads its axis at 0, 10, 25, 50 and 100 % on a square-root
  scale (his order: "show 10, 25, 50, and 100 %"), so a gain of a few percent is seen beside a gain of fifty; a bar past
  100 % is drawn to the edge and marked ►, its number beside it.
- **No dead pages** (the founder's order of 16 October, night: "every page be fully populated, 80 % at least"). The builder
  no longer leaves a page mostly empty: a chapter starts on the next page unless that would leave the page before it under
  80 % used, and then opens on the same page under a short space; a figure that does not fit under its paragraph floats to
  the top of the next page while the text goes on, and a chapter's last figure is placed before the next chapter opens; no
  paragraph leaves one or two lines alone on a page; a listing is set in pieces of six lines so a page of code is filled to
  its foot. The fill of every page is measured on the built PDF (how far down the frame the content reaches) and reported
  with the build. A heading now keeps only the start of what follows it (a table or a listing splits under it instead of
  being carried whole to the next page), a part opens where the chapter before it ends unless that page is already four
  fifths used, and the index lists at most sixteen pages for a term (reportlab would otherwise shrink a long page list
  below 11 pt). The pages that stay under four fifths are the title page, the last page of the front matter (the body
  starts on its own page 1), the last page with the end notice, and a few pages where a part or chapter opener does not
  fit under a figure; the build prints them.
- **The Operator's Manual says what it leaves out** (the founder's order of 16 October, night). Its front matter carries a
  disclosure: the Owner's Manual holds the harness, the engine's source, the mechanism and every result; the Operator's
  carries the wiring and the operation only, and for anything it does not carry the reader goes back to the Owner's Manual,
  never to a guess.
- **The company's landline** (the founder's order of 16 October, night). The toll-free number 1-888-339-9551 stands first on
  every contact line, and under it the landline registered in Florida, 321-746-4411: README, LICENSE and its copy, NOTICE,
  the Enterprise License, Trademarks, the Licensing FAQ, Security, Support, `llms.txt`, `codemeta.json`, both manuals.

## 2026-10-16 (night, the figures and the mathematics)

- **Both books carry figures drawn from the code** (the founder's order of 16 October, night: flow charts and illustrations
  that interpret the language of the mathematics, built into the manuals). `docs/book/figures.py` draws them from the law's
  and the engine's own numbers: the two-way plug; the compass band, its cushions and the force F = A·tanh(r/A) against a plain
  spring; one decision of the governor from the senses to the audit; the eight levels; the one pedal with cruise, watching,
  reset, off and the kill switch apart; the seven organisms on the spine; the three-run rule read from the intervals; and,
  in the Owner's Manual, the engine's six states with their couplings and the control law, and the two landscapes (the
  alignment's double well and the stress's cubic potential, its root and ridge computed from the defaults). Each stands
  where the text first needs it, numbered and captioned, with a List of Figures after the Contents; the same drawings are
  SVG files in `docs/book/figures/` beside the text on GitHub. Every label is 11 pt. None of the founder's plates go in.
- **The mathematics in its own symbols.** Every equation the Owner's Manual binds (chapter 4, Appendix C,
  `docs/CANONICAL_ENGINE.md`, `docs/TRACKING_THEOREM.md`, `docs/MECHANISM_OF_ACTION.md`, the closure table of the theory)
  now reads in Unicode: α[E], β[int], β[ext], v[eff], μ, λ[U], σ₁, δ, λ[I], ω[B], Q[B], γ[c], αₛ, βₛ, Φ(S), Ḃ, d²B/dt², K[P],
  f[U], F[D], ε[h], eₖ₊₁, ρᵏ, with ≤, ≥, −, ·, ←, ⇒, ∈ and ∫ in place of their typed stand-ins; Appendix C adds the table of
  every symbol against its name in the source and its value in the live controllers.

## 2026-10-16 (night, the index and the room)

- **Both books carry an index** (`docs/book/build_book.py`): every glossary term where the book defines or discusses it, every
  muscle family where it is named, every file of the repository and every setting (`--...`) the book names, with the pages they
  stand on; a plain mention of a common word is not an entry. The index is the last chapter before Contact in both books, and
  the front matter of each names it. The Operator's is 496 pages, the Owner's 1,354.
- **The room search** (`docs/OMNI_V7.md`, "The room search (16 October)"): of the 159 muscles that read SAME AS NATIVE on omni-v7's
  realms table, 147 have no native misses to cut and fixed work, and the 12 battery power knobs miss only while the charge sits
  at the operator's reserve, which the power knob may not spend; the max already takes every muscle to the edge its own knob
  has. Six process loops miss at most 0.56% of decisions: a card candidate for a later version. No engine file moved.

## 2026-10-16 (night, after): the book as the teacher; the reading key on every receipt; the three clouds on one harness

- **Both manuals open with the two books explained** (the Owner's puts the engine inside the vessel; the Operator's drives it),
  **Where to Get Help** (every question's place in the book; the website and the toll-free line; what to send with a question),
  and **the output follows the input** (section 3.7: the tune, the wiring and the load name every receipt; a changed input is
  another result, its own). The Operator's eight levels each say **what you should see** when the level is wired right, in the
  audit's own records and the receipt's own words; chapter 10 (the Owner's section 13) carries **the readings to expect**: the v7
  three-run tables as the reference bands, read in three steps (the words, the direction, the power given), with the two readings
  that are not faults named.
- **How to read this receipt** (`tools/readings.py`, `receipt_key()`): the short reading instruction, GAIN, STEADY and LOSS by the
  gauge's aim and never by the sign, power given, the three-run rule and the disclaimer, now stands under the title of every
  table and receipt the repository writes (the three-run tables, the capacity tables, the live receipts, the realms, the grid,
  the benefit sheet, the wiring verdicts, the organisms with the cluster inside) and in every standing table
  (`python3 tools/readings.py --fix`; `--check` fails a standing table without it).
- **Google Cloud and Amazon on Azure's harness** (the founder's order of 16 October: the Azure run is the measure of the other
  two): `gke-metered.yml` and `eks-metered.yml` carry the replica room, the machine-family queue in their titles and
  concurrency groups, and a secrets gate that stops a run before anything is built or billed; scripts/google_queue.txt and
  scripts/amazon_queue.txt carry the same four sets as Azure at the same settings, behind a `switch=` line (off until the
  secrets are in and the founder turns it on); the grid conductor (`scripts/dispatch_grid.py`) reads all three queues, one set
  at a time per machine-family queue, dispatched runs only. Nothing is rented on Google or Amazon before the switch is on.
- **The conductor's hand-off** (`grid.yml`): when a five-hour conductor ends it starts the next unless one is already waiting;
  a run a verify had started (workflow_run), which only ticks when its commit says `[all-nongpu]` and is otherwise skipped, was
  counted as waiting, so no conductor ran from 15:33 to the hand start at 16:05 on 16 October. Only a dispatched or scheduled run
  counts now. The grid was restarted by hand the same minute; nothing was cancelled.

## 2026-10-16 (night, latest): both manuals to the engine that stands, for every reader

- **The Operator's Manual** (`docs/OMNI_COMPASS_MANUAL.md`, `.pdf`): section 5.5, the rules of omni-v7 as an operator meets them
  (the quota rule and its `no budget known` line, the shared host's busy guard and its `convey: held` record, the clocks in
  seconds, the verdict in the words of a receipt, the cloud's one flag); section 4.7, coding a new muscle on the muscle SDK
  (`omnicompass/muscle_sdk.py`: the five functions, the three contracts, the automation modes, the runtime's gate, the receipt,
  the standard classes, a worked example whose outcomes are the SDK's own tests); Appendix K.5, every setting of the two card
  governors; Appendices L.4 and L.5, every audit record of the other muscles and of the card governors; the gauges the v7
  receipts carry; a reading path for the CEO, CFO, CIO and board and one for counsel; Appendices R, S and T (the Enterprise
  License's standard terms, the patents and trademarks statements, the security policy) bound in with the license, the
  licensing answers and the third-party notices.
- **The Owner's Manual** (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`, `.pdf`): the chapter "The Engine That Stands: Omni v7"
  (`docs/OMNI_V7.md`) after the mechanism of action; section 8.7, coding a new muscle on the SDK; the Enterprise License, the
  patents and trademarks and the security policy as chapters after the licensing answers; the road to v7 (the v5 and v6 pages)
  placed as history before the History chapter; the Source appendix now prints every Python file the fingerprint `OMNI_V7.json`
  names (41 files, 10,703 lines) in the fingerprint's order, nothing in the mechanism withheld from the owner; a reading path for
  the CFO and CIO and one for counsel. The Owner's PDF is 1,332 pages; the Operator's 483.

## 2026-10-16 (night, last): the first three-run tables on omni-v7

- **Five tables, every run omni-v7** (`results/live/V7_GOLDILOCKS.md`, `V7_KEDA_REQUESTS.md`, `V7_KEDA_CPU_REQUESTS.md`,
  `V7_CRUISEKUBE.md`, `V7_CAPACITY.md`; runs 38843260818 to 38843289946, built by `tools/confirm_abc.py` and `tools/capacity_abc.py`):
  no row reads LOSS on the three-run rule. Goldilocks −45% to −47% mean and −60% to −62% at the 95th percentile, GAIN in all three
  of our runs; KEDA's HTTP add-on −57% to −58% mean, −71% to −75% at the 95th percentile, alert minutes −93% to −96%, replicas −15% to
  −19%, pods started −17% to −23%, GAIN in all three; KEDA on CPU and requests −36% to −38% and −52% to −54%, GAIN in all three;
  CruiseKube and the capacity caps STEADY; machines STEADY in every table; parked-worker energy +1.1% to +2.3%, power given. Single runs
  clear of the noise that the other two did not repeat, each STEADY on the rule: CruiseKube's 99th percentile +3.1% (run A) and
  node-hours +1.0% (run B); Goldilocks replicas +3.4% (run C); capacity's completed work +3.8% at 1 core (run A).
- **The benefit sheet reads the v7 tables** (`tools/benefit_sheet.py`): Goldilocks +18% GAIN, KEDA's HTTP add-on +78% GAIN, KEDA on
  CPU and requests +45% GAIN, CruiseKube 0% STEADY, each power given beside it; the v6 tables stay in `results/live` as that engine's.
  The standing block, the wiring verdicts, the state of play, the README and the Owner's evidence table carry them.

## 2026-10-16 (night, later): Omni v7 stands

- **Omni v7 is the engine that stands** (the founder's order of 16 October: "Where is version 7? That's what you gotta push
  everything to"). `v7-candidate` is merged into main (`OMNI_V7.json`, digest `d6d467b824c585f1`, 46 files; `docs/OMNI_V7.md`): v6
  plus conveyance bounded by each namespace's CPU quota (an unreadable quota is no budget known), the shared host's busy guard on
  every raise, the verdict reading a trial in the reports' words, every rule in seconds, the cloud's one flag. Omni v6 stood one day,
  15 to 16 October; its four three-run tables stay as its own. Its first runs on real Kubernetes, native against Omni-Compass on top,
  ten pairs each: Goldilocks response time −45% mean and −60% at the 95th percentile, GAIN, replicas and pods STEADY; KEDA's HTTP add-on
  −57% and −71%, alert minutes −94%, replicas −19%, GAIN; KEDA on the CPU target and the requests −38% and −52%, GAIN; no LOSS.
- **Everything runs again on v7.** The grid conductor's campaign restarts on omni-v7 (`scripts/dispatch_grid.py`: the grid's manifest
  `results/grid_v7/`, the reruns counted since the twelve trial runs of 16 October, every Azure set from A again; `scripts/reruns.txt`);
  the v6 shards still running and the queued Azure set finish and stand as that engine's record, nothing cancelled.
- **The realms table on omni-v7** (`results/realms_v5/REALMS_V5.md`, run 2026-10-16, commit `1637d32cd26c`, seeds 3000-3009): every
  muscle alone and the seven organisms under three loads reproduce the readings of the engine before it to the digit (the law and the
  muscles are unchanged; `MUSCLES_V5.csv` byte for byte the same), and the table now names omni-v7.
- **The branch `v7`** carries the engine that stands, in step with `main` (the founder's words: "push everything to version 7");
  `v5` and `v7-candidate` are kept level with them; the Google and Amazon appendices name `v7`.
- **Every page names v7**: the README, CLAUDE.md, the state of play, both manuals (the evidence table, the engine chapter, the file
  map), `docs/OMNI_V7.md` (no longer a candidate), `docs/OMNI_V6.md` (one day's engine), codemeta 0.7.0.

## 2026-10-16 (night): the spine, the seventh organism

- **Seven organisms** (the founder's order of 16 October). The spine, the 267 muscles every real stack runs on (every muscle that
  sits in all four realms: Kubernetes workloads, containers, placement, node fleets, cloud capacity, hosts, GPUs, network, storage,
  observability, reliability and security, electrical distribution, cooling), is an organism in its own right, the base of the
  other six as an operating system is the base of every program; it runs native and with Omni-Compass on top of native like the
  four realms, the four stacked and the tower. `docs/THE_SPINE.md` says what it is, why it is an organism and how it is wired, and
  is bound into both manuals.
- **In every runner, no engine file touched.** The organisms are groupings of catalog rows made in the runners: `tools/run_realms_v5.py`
  (`SPINE`, `spine_rows`, `ORGANISMS`; the spine's row first in every organisms table), `tools/run_scale.py` (organism 7),
  `tools/run_hil.py` and through it `tools/run_kil.py --organism spine`, the grid conductor (`scripts/dispatch_grid.py`: organism 7,
  `spine`, its shard shapes a planning estimate scaled from the distribution realm's until its first shards are measured), the
  workflows `six`, `six-kube`, `realms-v5`, `grid`, `aks-metered`, `gke-metered`, `eks-metered`, `cloud-organism` and
  `big-organism-detached`, the GPU campaign profiles, and the page generators (`tools/grid_v5.py`, `summary.py`,
  `wiring_verdicts.py`, `muscle_catalog.py`, `realm_muscles.py`, `six_kube_report.py`). The engine fingerprint is unchanged
  (`python3 tools/omni_version.py`: omni-v6). `tests/test_spine.py` holds the spine to 267 muscles in 13 families, cut the same in
  every runner and named in no fingerprinted file.
- **The spine's first reading, native against Omni-Compass on top** (`results/realms_v5/REALMS_V5.md`, run 2026-10-16 03:48 UTC,
  commit `1d870bc33b2b`, engine omni-v6, seeds 3000-3009, evidence class S): GAIN under all three loads. Misses 2.39% → 2.25% of
  decisions under its own load (−6.1%), 8.00% → 7.37% under the climb (−7.9%, with more work), 4.23% → 3.86% with work waiting in
  line (−8.8%); work otherwise equal; power given +0.01%, +0.04% and +0.04%; wear +0.12% to +0.45%; every knob handed back; not one
  of its 267 plants with less work or more misses. The other six organisms reproduced the 13 October table to the digit (the same
  seeds, the law unchanged; `MUSCLES_V5.csv` byte for byte the same), and the page now names the engine it ran on, omni-v6.
- **Every standing page says seven**: the README, CLAUDE.md (an "Orders of 16 October" section), `docs/REALMS.md`,
  `docs/REALM_MUSCLES.md` and `docs/MUSCLE_CATALOG.md` (the spine first), the theory chapter on the organisms, both manuals
  (chapter 2 and its organisms table; the spine's chapter bound in), `docs/HOW_TO_READ_THE_RESULTS.md`, `docs/OMNI_V6.md`, and an
  amendment each in `docs/REALMS_PREREGISTRATION.md` and `docs/K8S_COMPASS_PREREGISTRATION.md`. Result pages already written keep
  the six they were run on.

## 2026-10-16 (later): everything in line with the engine that stands

- **The realm pages on the catalog that stands.** `docs/REALM_MUSCLES.md` (`tools/realm_muscles.py`) now writes every organism out,
  muscle by muscle, from `realms/catalog_v5.csv`: the spine of 267, the four realms (540, 404, 480, 484), the four stacked (1,908)
  and the tower (1,107); it had stood on the 945-muscle v2 catalog. `docs/REALMS.md` says what the realms are on that catalog, how
  to run them (`tools/run_realms_v5.py`) and where every result and page is; "simulation" is not used for our own models.
- **The wiring verdicts from the v5 realms result.** `tools/wiring_verdicts.py` reads the 1,107 muscles under their two loads
  (`results/realms_v5/MUSCLES_V5.csv`) and the six organisms under three loads (`REALMS_V5.json`): a GAIN on work, speed or misses
  is write and the energy the max took for it is power given, never a trade; SAME AS NATIVE and AT ITS LIMIT ON NATIVE are watch.
  527 muscles write and 580 stay native (421 at their limit on native, 159 the same as native); every organism under every load
  writes. The page's power-given table replaces the v3 trades table.
- **The state of play on the engine that stands.** The body of `docs/STATE_OF_PLAY.md` (the 10 October narrative of Omni v3) is
  moved whole to `docs/history/STATE_OF_PLAY_2026-10-10.md`; the page now says, in words, what the standing block says in figures:
  omni-v6 stands, four benchmarks have their three-run table on it, every other row is its own engine's result queued to run again,
  the v5 muscles and organisms, Azure at the tune-down, the card, Linux, the open items. The Owner's Manual's evidence table (3.5)
  opens with the four v6 rows and names the engine of every row; section 3.6 and the engine chapter carry v5, v6 and the v7
  candidate with their fingerprints; the file map names `OMNI_V6.json`. The README's front-page line no longer says no v6 result
  is claimed. `docs/REGISTER.md` row 56 and the catalog generator's docstring name the 1,107-muscle catalog.
- **CLAUDE.md's grid paragraph** carries the founder's distinction of 15 October: the 1,000 tier stands again on GitHub's own
  machines only; paid cloud and GPU runs stay at 1, 10 and 100 copies.
- **The Azure receipts of 14 and 15 October** (six machines-only sets at the tune-down, one full-wiring burst) are requested
  from the archive bot (`.github/archive_request.txt`); their tables follow, each on the engine it ran on.
- **The v7 candidate's first trials, and the correction** are recorded on the branch `v7-candidate` (its page docs/OMNI_V7.md,
  section 1): an unreadable ResourceQuota was read as a zero budget, so conveyance never raised a limit; corrected, model-gated,
  and the trials run again. Nothing on main changes: omni-v6 stands.

## 2026-10-16: every family's wiring on your own stack, in both manuals

- **The wiring recipes** (`docs/wiring_recipes.csv`, 70 rows, one per family of the 1,107-muscle catalog): the native
  controller that owns the family's muscles, the wire out (what is read, and where), the wire in (what is written, and
  where), the restore, and whether that wire has run live in this repository or only on a model. The catalog page
  (`docs/MUSCLE_CATALOG.md`, `tools/muscle_catalog.py`) now opens with the plug's four rules and prints a "Wire it on
  your stack" block above every family's table, so the Operator's Manual (Appendix E) and the Owner's Manual (Appendix G)
  tell anyone how to physically wire every muscle in the catalog on their own stack. The generator stops if a family
  has no recipe. The README, the docs index and both manuals' descriptions of the appendix say so; both PDFs rebuilt.
- No engine change: omni-v6 stands on main; v7 stays a candidate under trial.

## 2026-10-15 (night): the audit's findings fixed: engines named on every row, formulas in Unicode, the v6 tables, v7 under test

- **Every result names its engine.** The benefit sheet and the state of play's standing block now carry an Engine column
  read from each table (its run table, its JSON, its name, or the engine of the commit it names, by
  `tools/omni_version.py --commit`), list the rows on the engine that stands first, and say how many of the benchmarks
  are on it (4 of 26). A table on the engine that stands takes the place of the same benchmark's older table on the
  sheet; the older one stays in `results/live` under its own name. Results are never read across engines.
- **The v6 three-run tables** (`results/live/V6_GOLDILOCKS.md`, `V6_KEDA_REQUESTS.md`, `V6_KEDA_CPU_REQUESTS.md`,
  `V6_CRUISEKUBE.md`), built by `tools/confirm_abc.py` from the twelve archived v6 runs, every run omni-v6: Goldilocks,
  response time 45 to 47% faster, GAIN in all three of our runs; KEDA's HTTP add-on, 59% faster and alert minutes
  GAIN in all three; KEDA on CPU and requests, GAIN; CruiseKube, STEADY in all three. No row reads LOSS on the three-run
  rule. The KEDA HTTP table's pod start wait, mean, read +12.5%, +12.0% and +22.7% (STEADY on the three-run rule, a LOSS
  in two single runs): its cause is found and fixed in the v7 candidate (below).
- **Formulas in Unicode, never LaTeX markup** (the founder's order of 15 October). `tools/unicode_math.py` rewrote
  every formula the two manuals print (326 in prose and one block of equations: w ∝ 1/√n, xᵢ,ₖ₊₁ = fᵢ(xᵢ,ₖ, …),
  ⌈R(1+h)/r⌉), leaving code, prices and constant names untouched; `verify.py` now fails a push in which any formula a
  manual prints is in LaTeX. Both PDFs rebuilt: the Operator's Manual 434 pages, the Owner's 820; neither prints a
  backslash command or a braced subscript.
- **The v7 candidate** (branch `v7-candidate`, docs/OMNI_V7.md on that branch): the quota-aware conveyance (pull request #13);
  the verdict reading a give-back trial in the reports' own words (a clear rise refused, the evidence measured on while
  it is wider than the allowance); every rule of the governor stated in seconds; the cloud's rule as one flag,
  `--give-back-only`; and on a shared host no limit raised while the machine is 75% busy or unread. The founder's order
  of 15 October, night: every change is tried in our own models before any real run (`tools/model_gate.py`, section 6
  of docs/OMNI_V7.md). The gate refused two repairs written for the v6 KEDA table's pod start wait, the host's processor
  counted once (nothing conveyed at the run's nine replicas: the +64% work and -53% response time of conveyance lost
  whole) and a hold while a pod starts (1% of start wait for a LOSS on work and speed); the slower start is the busier
  host serving more requests. v7 goes on main only if its live trials show no LOSS.
- **The first v7 trials, read on 16 October, and the correction.** Goldilocks, the KEDA add-ons and the capacity test
  ran once each (ten pairs) on the candidate as first pushed: the two add-on tests read the candidate well short of v6's
  three-run tables (Goldilocks p95 -6% STEADY against v6's -58% GAIN; the pod start wait +172% LOSS; KEDA on the requests
  p95 -2.7% STEADY against -73%; KEDA on CPU and requests +3% STEADY against -55%), the capacity test STEADY as before. The
  audit names the cause: the quota budget read an unreadable ResourceQuota (the governor's role on kind cannot list them)
  as a zero allowance, so conveyance never raised a limit (5 commands a run against v6's 15). Corrected in the candidate:
  an unreadable quota is no budget known, the raise proceeds as on v6 and Kubernetes' admission stays the authority; the
  model gate runs the convey model with the quota unreadable as well, a regression holds it, and the three trials run again.
  The first trials stay in `results/live/raw/` on the branch as the record of the fault (docs/OMNI_V7.md, section 1).
- **Wording**: the retired words in the day's new pages ("improved or worsened", "unfavorable", "standalone",
  "confirmed/unconfirmed", the label FEWER MISSES) are replaced; the Owner's Manual's KWOK nodes are "stand-in nodes".
- **CLAUDE.md**: the engine section names v6 as standing and v7 as the candidate; formulas in Unicode; the founder's
  free/paid line on 1,000 copies (free GitHub machines may run 1,000 copies and runs; every paid machine stays at 1, 10
  and 100), as relayed in commit `9f455da7e`.

## 2026-10-15: the Operator's Manual carries the implementer's whole cloud path

- **The founder's order of 14 October (night): the Operator's Manual at least half the Owner's, covering all that matters
  for the person putting Omni-Compass on a cloud.** Part VI now runs from chapter 13 to chapter 30: observability (the
  feed from the company's own monitoring, the governor's series, dashboards, alarms, the provider's billing records, one
  decision traced), change management, risk and compliance, planning the saving before the run (the room, the billable
  room, the governor's own floor, the autoscaler's profile, pricing terms, the load's shape), own racks and private
  clouds (bare metal, OpenShift, vSphere and Cluster API, air-gapped, edge), hardening and the supply chain (signed images,
  the restricted profile, admission policies that narrow the governor's writes to its own taint and pod mark, network
  policy, the API server's audit), a fleet under continuous delivery, the failure drill book, and one installation start
  to finish. New appendices: the governor's settings, the audit record by record, the three clouds side by side, every
  input of the paired run from GitHub; cloud troubleshooting rows and glossary terms. 434 pages against the Owner's 816.
- **Fixes found while writing it, each checked against the code.** The machine script no longer treats a machine
  someone else cordoned as parked: it never uncordons one (a person's maintenance, an upgrade's drain), never counts it,
  and removes its own mark from it (`scripts/kind_nodepool.sh`; test in `tests/test_staging_order.py`). The cloud
  manifest runs the watchdog in the governor's own pod with a shared process namespace, because a watchdog in another
  pod cannot see the governor's process. The OFF switch of record in a cluster is scaling to zero (the kill file lives in
  the pod). Wake timing as it is: a breach at the next full decision, a waiting pod at the next fast check, and no pod
  ever waits for either. Watch mode writes no `would_write` record (there is none); a dry run's trials compare the service
  with itself, so the paired run is the evidence. The cloud image builds pass the base image.
- **The book builder** no longer reads a `#` comment inside a code block as a chapter heading (it had silently dropped
  the text after such a comment, in chapter 6 among others), and prints the manual's LaTeX formulas as formulas.
- **`tools/prom_feed.py`**: the governor's feed from the company's own Prometheus, one row per quantile midpoint, failures
  capped, nothing for an empty window, its clock continued across restarts; test `tests/test_prom_feed.py`; in the cloud
  image.
- **Google and Amazon ready the way Azure is**: `gke-metered` and `eks-metered` take the dial (default `save`) and run
  the governor on the machines alone (`OMNI_MACHINES_ONLY=1`); setup pages and install files for all three. Not run:
  Google, Amazon and the GPU wait for the founder's word that Azure is done. No engine file changed.

## 2026-10-14: in the cloud, the machines alone: a bill that can only fall or stay

- **The founder's order of 14 October (night): never a bigger bill in the cloud.** The tune-down with native's replica
  cap still let a burst raise the bill (the pod target moved down to 60% of the operator's; more pods asked Azure for
  machines). Every Azure set now runs the governor on the machines alone (`OMNI_MACHINES_ONLY=1` in `aks-metered.yml`;
  `scripts/kind_bench.sh`): no pod autoscaler moved (`--sensed none/none`), no processor conveyed, no power capped, so the
  pods are exactly native's; the governor only parks machines Azure already made, after its own trial, and wakes them on
  a breach. No engine file changed: existing settings only. Written into the Kubernetes preregistration before any run
  at the tune-down. Test: tests/test_cloud_machines_only.py, removed on 31 October when the founder struck the cloud's rule (a breach moves no pod target; the cloud's settings; the
  machine lever never asks for a machine the cluster does not have).
- Both manuals (sections 7.1 and 10.1), the README, CLAUDE.md and the next version's plan say so.

## 2026-10-14: the babysitting tax in every Kubernetes and cloud receipt; the cloud bill in both manuals

- **The founder's order of 14 October (night):** show that Omni-Compass is an autopilot, self-running and self-steering
  like a self-driving car, acting ahead: nobody turns a knob, nobody has to react. Three rows join every Kubernetes and cloud receipt (`tools/live_reps.py`, `babysitting`), written
  into `docs/K8S_COMPASS_PREREGISTRATION.md` before any run at the tune-down: the **alert minutes** (whole minutes whose
  95th percentile, failed requests counted over, was over the line; judged, the aim lower), the **settings commands the
  governor wrote on its own** and the **share of its additions decided while the service was still inside its line**
  (both shown, not judged). Every receipt states that no person touched either arm. Test: `tests/test_babysitting.py`.
- **Both manuals** (the Operator's, sections 7.1 and chapter 8 and Appendix C; the Owner's, sections 10.1 and 11 and
  Appendix D), the metrics catalog and the README: in the cloud the bill is the gauge and is never raised (the tune-down
  with native's cap); the max belongs where the machines are paid for; no babysitting, and the rows that count it. Both
  PDFs rebuilt. No engine file changed.
- **The decision period in the cloud** (the founder's orders of 14 October, night: faster than every native controller,
  but only where it hurts nothing): read against the governor before any run, a shorter full-decision period changes four
  rules counted in decisions (at 5 s a give-back trial's phase would last 100 s, too short for the 200 response times it
  measures, so no machine would ever be given back and the bill could not fall). The cloud stays at the tested 60 s
  decision with fast checks every 5 s (three times as fast as the HPA's 15 s); the rig accepts `OMNI_INTERVAL` and
  `OMNI_FLOOR_INTERVAL`; the next version counts those rules in seconds. Written into the Kubernetes preregistration.
  The cloud's arms default to native and Omni-Compass on top in every cloud workflow and script.
- **Self-auditing, and no alert minute in the cloud** (the founder's words of 14 October, night): the governor audits
  itself (every write read back, every machine given back only after its own paired trial, every reason in its audit),
  and the cloud's aim is no alert minute at all; an alert minute in the omni arm is a LOSS of the aim, found and fixed.
  The next version's plan carries the changes that close the rest of the gap (the max halved the time over the line on
  Azure's steady load, 30.3% to 14.6%).

## 2026-10-14: in the cloud, the bill at native's work: Omni-Compass on top at the tune-down with native's cap

- **The founder's order of 14 October (night):** in the cloud Omni-Compass shows the same work as native for a smaller
  bill, never a bigger one; the benefit of the max belongs in the engine before the cloud or in the chip. The Azure steady
  run at the max (38455383137, three repetitions) had raised the bill 49% at list price to buy faster replies and fewer
  failed requests; it and the burst at `1 6 1 8 1 6` at the max (38500160429) are stopped and kept as runs of the max,
  counted in no bill result.
- **`aks-metered.yml`:** a `dial` input (default `save`, the tune-down) passed to the governor (`OMNI_DIAL`,
  `scripts/kind_bench.sh` `--dial`); the run's title carries the dial. Every line of `scripts/azure_queue.txt` runs at
  `dial=save` with native's own replica cap (`replica_ceiling=0`), `1 4 1 6 1 9` first among the bursts; the conductor
  reads the dial into each title (`azure_title`), so the runs of the max are never counted as started. Test updated.
- **Preregistration** (`docs/K8S_COMPASS_PREREGISTRATION.md`, last section, before any run): the bill and the machines
  aim lower; work, speed and failures must read STEADY or GAIN; disclosed: where native is short (at its cap and failing,
  as on the steady load) the bill is expected STEADY, and the cuts in the quiet stretches between bursts and a day's
  trough; inside native's cap the HPA target still moves, so a burst can still raise the bill (a give-back-only cloud
  setting is proposed for the next engine). The replica room is off in every cloud set (`docs/AKS_REPLICA_ROOM_PREREGISTRATION.md`).
- CLAUDE.md carries the order. No engine file changed: the dial and the replica cap are the engine's own settings.

## 2026-10-14: two manuals: the Operator's Manual (the glove box) and the Owner's Manual (the master, everything)

- **The founder's orders of 14 October (evening and night):** two manuals, both kept in the repository until the founder
  takes one out. The **Operator's Manual** (`docs/OMNI_COMPASS_MANUAL.md`, `docs/OMNI_COMPASS_MANUAL.pdf`) shows an
  engineering team how to embed, wire, tune, run and check Omni-Compass on a stacked, clustered system or on any one
  muscle, and says nothing about how it is built. The **Owner's Manual**, the master (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`,
  `docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`, 808 pages), holds everything, for whoever owns or licenses it and so must know the
  whole mechanism: the philosophy and the theory, the mathematics, the mechanism, the engine's source, every result, and
  the wiring. CLAUDE.md carries the orders.
- **The Owner's Manual** is the full manual as it stood (every chapter, the equations, the mechanism, the results, the
  evidence map, the reproduction chapter, the executive summary with the standing block), retitled, bound with the theory,
  the declaration, the repository's documents and the engine's source (`python3 docs/book/build_book.py --owner`).
- **The Operator's Manual, `docs/OMNI_COMPASS_MANUAL.md`, rewritten** (3,804 lines to about 2,000): front matter (the key, what you are looking
  at, the notice with the wiring disclaimer and the factory tune, a foreword, a preface for each reader, the prelude, an
  introduction on the problem, the idea and what the manual covers, and the card for the glove box); Part I the governor
  from the outside (what it is; your stack as one body; a new chapter on tuning: the factory tune, the dial, each muscle's
  card, the settings an installation writes, the profiles); Part II the plug, the adapters, the wire check and the rules
  the wires obey; Part III the eight levels and every stack's wiring, brought to the rules as they stand (the pooler's
  queue reading, the caches' miss-share gates, the buffer pool's hand-back on the server's time, the GPU and the cluster
  at the max and at the tune-down); Part IV operating it; Part V checking it on your own system (paired runs, evidence
  classes, the engine version and the three-run rule); Part VI the license and verifying a copy; back matter (glossary,
  commands, the files an installation touches, the gauges, troubleshooting, every muscle). Removed: the engine's
  equations, the mechanism and theory chapters, the compass law's gains, the engine's source, the results chapters, the
  evidence map, the reproduction chapter and the executive summary (all kept in the Owner's Manual).
- **The book builder** (`docs/book/build_book.py`) makes both: the Operator's Manual binds the manual, the muscle catalog
  (Appendix E) and the license papers; `--owner` binds everything. The copyright page no longer says "simulated". Both
  PDFs: no images, no blank page, nothing under 11 pt, the contents matching the pages.
- **Where things stand** (`tools/summary.py --fix`) now writes its block into `docs/STATE_OF_PLAY.md`, the results'
  own front page, and into the Owner's Manual's executive summary, and `verify.py` checks both; the key stands in both
  manuals.
- Every page that pointed into the old manual points to the new chapters: `DISCLOSURES.md`, the wiring banner on 20
  pages, `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md`, `docs/GPU_RUN_GUIDE.md`, `docs/REFEREE_CHECKLIST.md`,
  the muscle catalog (`tools/muscle_catalog.py`), the README and the instructions other AI tools read.

## 2026-10-14: the Azure sets queue themselves; two more burst shapes, `1 4 1 6 1 9` and the real day on 1 to 9

- **The Azure queue** (`scripts/azure_queue.txt`, read by the grid conductor every 15 minutes): every Azure set in
  release order, A of every set, then B, then C; a set starts when its machine family's queue (region and machine size,
  the workflow's own concurrency group) has nothing waiting or running, one a tick in each queue, and is read back by
  its run's title since 13 October 19:00 UTC (a cancelled run counts for nothing), so nothing starts twice and nobody has
  to be at the button between sets. Test added (`tests/test_run_scale.py`).
- **Two more burst shapes** (the founder's words of 14 October; `docs/K8S_COMPASS_PREREGISTRATION.md`, last section,
  written before any run): `1 4 1 6 1 9` (six steps over 1,800 s, after the `1 6 1 8 1 6` set in the Standard_D2_v4
  queue), and the real day on 1 to 9, Google's public 2011 day placed on 1 to 9 by the same rule and stepped by the
  founder's one-step rule for real traffic (`2 3 3 4 3 4 4 3 2 2 2 2 2 3 2 3 4 5 4 5 6 7 6 5`, 24 steps of 108 s, after
  the steady set in the Standard_D2s_v4 queue; disclosed: the day touches 9 for one hour, so the stepped schedule peaks
  at 7). Neither arm reads a schedule: the load generator alone steps through it.
- `tools/trace_schedule.py --load-max N --counts-from DIR`: an already derived day re-placed on another range with
  nothing downloaded, its parts and their SHA-256 carried over; receipt `results/traces/google2011_1to9/`. Test added.
- CLAUDE.md: the conductor's line names the Azure queue.

## 2026-10-14: the Azure burst back at `1 6 1 8 1 6` (the founder's order)

- The founder's order of 14 October: the burst runs at the steps first preregistered, `1 6 1 8 1 6`. Our amendment 11 of
  5 October (`1 3 1 4 1 3`, written after the first results at `1 6 1 8 1 6` showed about 41% of requests failing in both
  arms behind the service's cap of 10 pods) is withdrawn for every run from this date
  (`docs/K8S_COMPASS_PREREGISTRATION.md`, last section; `docs/AKS_REPLICA_ROOM_PREREGISTRATION.md`). The burst run at
  `1 3 1 4 1 3` on this engine (38455393389) was stopped after its second repetition and part of its third, its
  repetitions kept as runs of the withdrawn setting and counted in no burst result; the burst started again at
  `1 6 1 8 1 6` (run 38500160429), five repetitions, then B and C. CLAUDE.md says so.

## 2026-10-14: a running benchmark can be looked at before it ends (peek); the conductor runs its newest code every tick

- **`peek`** (`.github/workflows/peek.yml`; the founder's order of 14 October: look at a run while it goes and jump in
  if something is wrong): given a run number, it downloads the repetitions that run has finished so far and prints their
  paired table (native against Omni-Compass on top of native) in its log and report, with `tools/live_reps.py` for
  Kubernetes and Azure or `tools/six_kube_report.py` for the organisms. It reads only; its table is a look, never a
  result. The Azure job logs carry only the last ten lines of the Omni arm, so this is the way to see native beside it
  before a run's last repetition. The grid conductor lets a waiting peek go first.
- **The conductor runs its newest code every tick**: `grid.yml` runs eighteen ticks over five hours in one job and had
  read the conductor's code once at its start, so the Azure-first hold and the rerun queue (pushed at 01:55 UTC) would
  not have acted until about 05:35; each tick now fetches `scripts/` from the branch first, so a fix acts within 15
  minutes. The conductor started before the fix was cancelled and started again on the pushed code.

## 2026-10-14: the 100-copy LOSS found (replicas added on a saturated host) and its fix planned; the manual's organisms on the newest engine

- **Protocol 3 at 100 copies** (the organism's model on its own core, ten paired repetitions each; runs 38464343379,
  38462289297, 38462280620; omni-v5, digest `6093b2b8`): the whole tower's 95th percentile +47.7% (LOSS), the four
  stacked +87.2% at the 95th and +32.1% at the 99th (LOSS), the four realms STEADY on every response time; time over the
  line GAIN in the tower (-3.2%) and in Physics (-3.1%). The model's own processor time is ruled out as the cause. The
  cause: the four-core machine was about 80% busy and failing about half its requests in both arms, and the max raised
  the replicas 40% to 54% on nodes that could not grow, so the added pods crowded the same cores (host busy time +6.6%
  to +12.9%).
- **The fix, for the next version** (`docs/omni_v5/NEXT_VERSION_PLAN.md`, section 3): the replica muscle's live
  capacity becomes the smaller of its autoscaler range and the headroom of the machines under it; where the nodes have
  no headroom the max adds no replica. The founder is told before the version is declared; the eight-core Azure runs of
  the tower at 100 copies show how much of the LOSS the small machine carries.
- **The manual's organisms on the newest engine**: sections 2.4, 2.5 and 10.4 now describe the grid with the cluster
  inside on omni-v5, protocol 3, the 100-copy finding and its fix, and the eight-core Azure runs; the earlier engines'
  1,000-copy runs are pointed to in their own tables and never read across engines.

## 2026-10-14: the factory tune declared, the wiring disclaimer in capitals, the notice in every AI's instructions, the manual's standing block

- **The factory tune** (`DISCLOSURES.md`, section 3; the README; the manual's notice): the engine is presented as The
  Omni-Compass LLC tuned it and ships it, self-running and set at the factory; every muscle wired on its own setting (its
  own card where one was found, 364 muscles; the engine's setting for the rest); no setting presented as universal; a
  licensee may then add on, retune, upgrade or tune down any muscle, and a changed tune's results are its own.
- **The wiring disclaimer in bold capitals** (`DISCLOSURES.md`, section 4; the README; the manual's notice; `llms.txt`):
  the published benchmarks are the record of what Omni-Compass did on the systems, loads and engine they name; where a
  result elsewhere differs, the first presumption is the wiring, the settings, or how Omni-Compass was implemented or read.
- **`DISCLOSURES.md`, section 3, brought to the max**: the rule on every muscle no longer says "only to save energy"; it
  states the max (more work, faster, up to each muscle's own limit), the tune-down on the dial, the verdict that undoes a
  step costing the muscle more per piece of work or more than 2% on any measure, and power given. Section 2's class S
  now reads "our own models (modelled)".
- **The notice in every AI's instructions**: `AGENTS.md`, `GEMINI.md` and `.github/copilot-instructions.md` told an AI
  to attach "this notice, word for word" and then showed none (the legal tool strips a second copy near the top of a
  page); they now point to the notice at the top and end of their own file and require it on every output of any length,
  down to one line or one number. New `llms.txt`, the file AI crawlers read, carries the notice, the order, the classes,
  the words and the capitals disclaimer.
- **The manual's standing block**: the Executive Summary's results paragraph (Omni v3 figures, an index of +4.8% the index
  file no longer held) is replaced by a block that `python3 tools/summary.py --fix` writes from the result files: the
  engine, the muscles and organisms, the grid, the index and every benchmark's number with its word and class;
  `verify.py` fails a push in which the block no longer matches them. "What it does for you" now states the max and the
  tune-down.
- **Referee level** (the founder's correction of 14 October): the Introduction's problem and idea restated in control-
  and software-engineering terms (reaction latency, static over-provisioning, uncoordinated coupling; sense, normalize,
  decide, actuate, verify), and the standing orders say so.
- The book no longer prints the tools' page markers (`<!-- ... -->`), which had shown on three pages.
- **Every benchmark again on the engine that stands**: the reruns held back on 13 October so Azure could go first are
  now released by the grid conductor from `scripts/reruns.txt` (19 benchmarks: the other five Kubernetes tests, the KEDA
  add-ons, the five live stacks for resource and service, the four independent simulators, the two robustness tests), A
  of every benchmark first, then B, then C, up to six a tick and never while a run that goes first waits for a runner. A
  workflow's runs since the queue began are read back by count in the queue's order, so nothing starts twice. Kubernetes
  steady and wandering (A, B, C) are already running on this engine and CruiseKube (A, B, C) has finished on it.

## 2026-10-14: the manual without illustrations or blank pages, every line of text at 11 pt

- **No illustrations** (the founder's order of 14 October): the founder's plates are out of the manual: the cover art,
  the title-page rose, the nineteen plates, the List of Plates and the back cover; the dossier's charts are left out of
  the book too. The plates stay in `docs/book/plates/` as the founder's property; their links are gone from
  `docs/book/THEORY.md` and `docs/book/DECLARATION.md`.
- **No blank pages**: chapters no longer wait for a right-hand page; every chapter starts on the next page, and a part's
  heading sits at the top of a page with its first chapter under it. The contents and every page number are rebuilt
  from the book itself, and every page but the title page carries its number and the footer.
- **Type, by the founder's prompt rules**: body text, tables, lists, code, notes, captions and the contents at 11 pt
  (the body was 10.5 pt, tables 7 to 8.3 pt, code 6.7 to 7.6 pt) on a 16.5 pt line (1.5); headings scaled up (26, 16
  and 13 pt); only the running heads and footers are smaller, at 8 pt. A table row taller than a page now breaks across
  pages. The book ends with the full notice, as it begins.
- The rules are in `CLAUDE.md` (Orders of 14 October).

## 2026-10-14: the company's telephone in the founder's wording, and what its letters mean

- Every contact line now reads, in the founder's words: The Omni-Compass LLC, **main office infrastructure, toll-free
  direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1**, before the website (README, LICENSE and its copy, NOTICE,
  the Enterprise License, Trademarks, the Licensing FAQ, Security, Support, the manual's "Who to call"). The legal notice
  still ends with www.omni-compass.com and nothing after it.
- The README's new "Contact" section and the manual's "Who to call" show what the letters mean at Omni-Compass, read in
  order as the engine runs: **DEX**, Data Exchange (the input: the two-way plug, readings in, settings out); **YLL**,
  Yield Limit Line (the boundary: every muscle up to its own limit line and never past it, as an engineer loads a
  material up to its yield limit, the most it carries and still springs back unharmed); **1**, one closed loop (the
  output: in code 1 is true, in science 1 is unity; one body, one brain). The manual's glossary carries DEX-YLL-1 and
  the yield limit line.

## 2026-10-14: Azure goes first on GitHub's machines (the grid conductor; the engine unchanged)

- The founder's order of 13 October: Kubernetes on Azure is finished first. Its runs drive Azure from GitHub's machines,
  and on the night of 13 October an Azure repetition waited more than an hour behind about 140 grid jobs, the 100-copy
  reports behind them too. The grid's conductor (`scripts/dispatch_grid.py`) now starts nothing new while an Azure run
  (or, later, a Google or Amazon run), a grid run's report, a push's verify or the archive of finished runs waits for a
  runner, so that job is next in GitHub's queue. A run that waits only for its own one-at-a-time matrix (the AKS
  repetitions run one by one) does not hold the grid. Each conductor report names what it held. Test: `tests/test_run_scale.py`.

## 2026-10-13 (late night): GAIN, STEADY and LOSS everywhere (words only; the engine, every number and every verdict unchanged)

- **The founder's order of 13 October, evening**: "better, same and worse are going to be gain, even and loss, wherever
  and ever, all over where it lives, where it used to live". Every judged reading in every table, page, report, program
  output and the manual is now **GAIN**, **STEADY** or **LOSS**, decided by what the gauge is for and never by the sign of
  its number. A resource spent or held that fell is a cut, a GAIN; one that rose is **power given**, never a loss.
  Lower/higher-as-a-verdict and toward/away (the words of the morning's order) are retired with better/worse.
- **The key** (G.A.I.N. Growth, Advantage, Improvement, Net-positive; E.V.E.N. Equalized, Verified baseline, Equilibrium,
  Neutral; L.O.S.S. Leakage, Off-track, Setback, Subpar), disclosed and disclaimed, is written once in `tools/readings.py`
  and stands word for word at the top of the README, `docs/HOW_TO_READ_THE_RESULTS.md` and the manual's front matter
  (`python3 tools/readings.py --fix`; `verify.py` fails a page whose key differs). The manual's glossary carries the words.
- **`python3 tools/summary.py`**: the whole summary straight after a pull (what Omni-Compass is, the key, the engine, the
  index, every benchmark's number and word with its evidence class, the wiring counts, the realms, the grid), standard
  library only; `--markdown` for a page. Tests: `tests/test_readings.py`, `tests/test_summary.py`.
- Every table tool (Kubernetes, the databases, Kafka, Redis, MongoDB, MySQL, CPU power, the simulators, the per-run and
  organism reports, the grid, the realms, the GPU and card reports, the pilot), the index, the wiring page, the benefit
  sheet and the dossier write the new words; the recorded pages (`results/live/*.md`, the realms, the grid, the GPU and
  card pages) were re-rendered or reworded row by row from each gauge's declared aim, numbers untouched, and their
  checksum files updated. Raw machine records (JSON receipts, raw run folders) keep their recorded values; every reader
  translates them. Two physics rows renamed: "energy dissipated in lines and transformers (MWh)", "copper heating per
  cycle (J, I²R, declared model)". The index (+5.2% resource, +12.5% service), the 24 benefit-sheet numbers and the 1,037
  wiring rows are identical to before.
- **What the words now show plainly**: on the grid's cluster-inside half the organism's **work per energy reads LOSS in
  22 of 36 squares** (energy given, no extra modelled work), and the 95th and 99th percentiles read LOSS in 2 squares
  each (the 100-copy squares the machine limited); CityLearn (v1 and v3) reads LOSS on energy not served and time
  uncomfortable in several districts. These rows were in the tables before under the older words; they are shown, and
  their causes go to the next engine.
- The dossier's database paragraphs were brought up to the current tables (they described earlier sets).
- Removed: the three competitor-era report generators (abc_report, full_report, buyer_report in tools/) and
  the three-way script (an "Omni alone" third arm; the result page moved to `docs/history/three_way/`). The fleet,
  PlanetLab, multiplicity and lab modules print the new words; `results/MULTIPLICITY.json` regenerated, numbers identical.

## 2026-10-13 (night): Omni v5 re-declared (digest 6093b2b8): every muscle from 1 up to one click under its own capacity, read live

- **The founder's order of 13 October**: every muscle runs from 1 up to one click under what the system itself can hold,
  read live and guardrailed, unbounded where the system can keep adding, never below 1, and back down; no muscle may
  hurt the organism. Nothing in the live controllers is a top or floor written down for a muscle any more
  (`docs/OMNI_V5.md`, amendment 5):
  - machines: the operator's `--max-nodes` where given, else every ready worker plus the cluster autoscaler's own room,
    else (Omni-Compass resizing the pool itself) one under the first count the pool refuses (before: a fixed 1,000);
  - replicas: the replica room on by default, up to what the machines can hold of the service's pods, one pod under it,
    a kind cluster's one host counted once (before: off unless an operator gave a number);
  - the power cap at the max never under native: the capped pods get their machine's idle CPU, the frequency ceiling
    and the GPU limit stay at their top (before: the governor's trim could reach 69.5% even at the max); the tune-down's
    floor is the pod's own request and use, and the card's own minimum (before: a fixed 65%);
  - GPU: the clock floor is the card's lowest supported clock (before: 35% of the top); the heat line one degree under
    the card's own slowdown temperature where it reports it (before: 83 C for every card);
  - batch admitted up to the compass's wall less one cushion (0.90; before: load 0.80); the nervous system's power
    envelope is the band of the device's own range (before: from 0.65), its C++ twin re-proven equal and re-sealed.
- **The 100-copy squares were the test machine, not the governor** (protocol 3, `docs/K8S_COMPASS_PREREGISTRATION.md`):
  native's own failed requests rose from 6-10% at 1 copy to 32-43% at 100 as the model of the organism took the cluster's
  cores. Now the model runs on the runner's last core and the kind nodes on the others, the same in both arms, and the
  window is set from the heavier arm's step, measured before either arm (`tools/run_kil.py --calibrate`).
- The engine's own files say which way a number went; the older label "WORSE" is "AWAY FROM ITS AIM" (the GPU
  benchmark's own). The modelled organisms' code is unchanged but for comments, headers and that label.
- The engine files the fingerprint locks carry the current legal header (the files whose bytes a preregistration or the
  seal records keep theirs). Mechanism identity: the actuator part re-recorded, every other part unchanged.
- Every result runs again on this engine: the grid (both halves, 54 squares), the live sets and the Azure sets.

## 2026-10-13 (evening): no "better" or "worse" anywhere; every reading says which way the number went

- **The founder's order of 13 October**: who sets the aim differs from one system to the next, so no table, page or
  report judges. Every reading now says which way the number went against native, **lower** or **higher** ("lower in
  all three of our runs"); the tools that score a headline (the Omni index, the benefit sheet, the wiring verdicts, the
  dossier) say **toward** or **away from** each gauge's declared aim (each preregistration's: lower for an amount waited,
  spent or held, higher for work done). The benefit sheet's sign is now the system's own aims, never "good for Omni"
  (`tools/readings.py`).
- **Every reading tool rewritten**: the three-run tables (Kubernetes, PostgreSQL, Kafka, Redis, MongoDB, MySQL, the CPU's
  frequency ceiling, the robot arms, the power grid, CityLearn, the drone swarms, the capacity test), the per-run
  reports, the organisms' report, the grid page, the GPU reports, the realm tables (their kinds now read TOWARD ITS AIMS,
  BOTH WAYS and AWAY FROM ITS AIMS) and the card search, with their tests.
- **The recorded tables, the documents and the book carry the same words**: 140 tables in `results/`, every current
  document, the manual and the printed book (rebuilt, 538 pages). In a table each reading is the direction its own row's
  numbers show. A check compared every number in every table before and after, and none changed; the wiring verdicts
  (1,037 rows) and the benefit sheet (24 rows) read exactly as before. The documents as first written are in the
  repository's history; `docs/history`, the archived raw receipts and quotations of outside reviews stay as written.
- **The printed book no longer carries three September reports** that set Omni-Compass against other products (the
  benchmark report, the referee report, the buyer edition); they stay in `docs/history` as written. Every benchmark has
  two arms, native and omni.
- **Why the 100-copy squares read as they do**, now on the grid page and the front page: the test machine itself.
  GitHub's four cores carry the real cluster and the model of up to 190,800 muscles at once; native alone kept the CPU
  87% to 91% busy and failed 32% to 43% of requests there. The fix is the longer window already running and the organism
  moved off the cluster's cores, the same in both arms.
- **The standing orders** (`CLAUDE.md`) carry the orders of 13 October: the words; every muscle from 1 up to one click
  under its own capacity, read live, never a number written in code; the brain works for the organism; the written
  settings of a benchmark stand (the Azure burst steps are `1 3 1 4 1 3`), and the Azure replica-room preregistration
  is corrected to them, its ceiling to be read live.
- **Not changed yet, and why**: the engine's own files (fingerprint `5648f290`) keep two old label words (the v1 and v3
  realms' label, the per-run reports of the grid and CityLearn simulators); they change with the next engine version.
  The pre-v1 lab scripts (`omnilab/`, `fleet/`, `benchmarks/`, `tuning/`) and the generators of the September reports
  keep theirs until they move to the archive.

## 2026-10-13 (late afternoon): the grid of the card version, both halves; the knobs that were left off

- **The grid** (`results/grid_v5/GRID.md`, built by `tools/grid_v5.py` from the pooled receipts: six-pool runs
  38413185368, 38413200224, 38413211812; six-kube-pool runs 38416329587, 38416341417, 38416354634): the six organisms at
  1, 10 and 100 copies, each at its first 1, 10 and 100 runs, native against Omni-Compass on top. Modelled (class S):
  fewer misses in all 54 squares (every square of 10 and 100 runs labelled FEWER MISSES), the same work, power given at
  most +0.065%. With the real cluster inside (class L for the cluster): at 1 and 10 copies, in all 24 squares of 10 and
  100 repetitions, 12% to 59% less time over the response line and the 95th percentile 24% to 56% faster (inside the
  noise in 2); at 100 copies 8% to 13% less time over the line, but the four stacked and the whole tower at 100
  repetitions read the 95th and 99th percentiles higher (+45% and +19%; +13.5% and +14%), the four stacked off the
  window's clock in 49 of 100 repetitions; the report also reads the organism's modelled energy (+0.06% at most, the
  power given) away from its aim in 22 squares and 0.2% to 0.6% more copies of the service in 5. No square invalid; every knob
  handed back.
- **Those two squares again with a longer window** (`docs/GRID_LONG_WINDOW_PREREGISTRATION.md`, written before the
  runs): the four stacked at 5,400 s (was 3,600), the whole tower at 3,600 s (was 2,400), everything else protocol 2;
  pooled only among themselves, the earlier squares kept as they are.
- **Azure with Omni-Compass's replica room** (`docs/AKS_REPLICA_ROOM_PREREGISTRATION.md`, written before the runs): the
  steady run A read no difference because the service sat at its cap of 10 in both arms (over its line 30% of the time,
  4.4% of requests failed) while Azure kept about 1.9 of 4 machines in service, and the replica room, Omni-Compass's own
  lever for a cap that binds (in the engine since 4 October, off unless granted), was off. Two settings of their own,
  three runs each: the steady test and the burst at `1 6 1 8 1 6`, native at the operator's cap of 10, Omni-Compass
  granted the room up to 36 (what four machines hold), on `Standard_D2_v4` so they run beside the standard sets
  (`aks-metered.yml`: the `replica_ceiling` input, one queue per machine family and region, a run name that says what
  each run is). **Disclosed**: the burst run A on the card version (run 38339901189) was started at `1 6 1 8 1 6`, the
  steps amendment 11 replaced on 5 October; it is reported as run at those steps, and the standard burst runs at
  `1 3 1 4 1 3`.
- **CruiseKube's third trial ran end to end** (run 38412997261, never counted): CruiseKube installed, learned and applied
  its own change in both arms; its chart is now pinned (`a3c7fa89…`). In the trial's 360 s window Omni-Compass's governor
  decided six times and made no write: the service stayed well inside its line (95th percentile 133 to 199 ms against
  500 ms). **A decided window with no write now counts as it ran** (`scripts/kind_bench.sh`, every set; amendment 1 of
  `docs/CRUISEKUBE_PREREGISTRATION.md`): staying native is the governor's own decision at every step (the founder's order
  of 10 October); a governor that recorded no decisions was not running and its window is invalid; the table counts the
  windows in which Omni-Compass stayed native (`tools/live_reps.py`, `tests/test_stayed_native.py`).

## 2026-10-13 (afternoon): the meter kit for Kepler; the CruiseKube trial runs; Azure steady run A

- **The meter kit** (register row 79, the first of the founder's nine pieces; `docs/METER_PREREGISTRATION.md`,
  `docs/METAL_KIT.md`): on a rented bare-metal machine, one command (`sudo bash scripts/metal_kind_run.sh`) runs the
  standard Kubernetes set, native and Omni-Compass on top, ten paired repetitions, with the machine's own meter (the
  processor's RAPL counters, packages and memory, `tools/rapl.py`) read every 2 s over each measured window and judged
  like every gauge (class P), and Kepler 0.11.4 beside it (`scripts/kind_addons_kepler.sh`; shown, not judged). GitHub's
  virtual machines have no meter, so the kit refuses them. About 8 hours a run; three runs make the result.
- **CruiseKube's trial runs** (register row 81): the first two stopped on the harness's own lines (a placement check that
  counted pods still shutting down; a filter's precedence), never on CruiseKube, which installed end to end both times.
  Both fixed; the two add-on scripts now run end to end in the tests against stand-ins (`tests/standin_cruisekube`).
- **Azure steady run A** (run 38339858727, five paired repetitions on the real AKS cluster, card version): no measure
  differed beyond the noise in this run; Omni-Compass's own process used 0.014 cores. Runs B and C follow the burst run.

## 2026-10-13 (morning): Goldilocks and the capacity test, three runs each, on the card version

- **Goldilocks** (register row 80; runs 38339821941, 38339828150, 38339834658 on commit `148565d2`, omni-v5 digest
  `5648f290`; `results/live/V5_GOLDILOCKS.md`, class L): the average response 44% to 48% faster, the 95th percentile 59%
  to 62% faster, the 99th 68% to 69% faster, time over the response line down 99% to 100%, toward its aim in all three of
  our runs; machines the same; no failed request in either arm; energy 1.9% to 2.6% more on the declared model, away from its aim
  in all three of our runs (the power given: about 40% more CPU work done for the faster service).
- **The capacity test** (runs 38339841468, 38339847249, 38339853176; `results/live/V5_CAPACITY.md`, new three-run tool
  `tools/capacity_abc.py`): no difference beyond the noise at any of the four caps in the three runs (one run at 2 cores
  read 1.8% less completed work; the other two noise). The cap is a quota on the service's CPU and blocks the one lever
  Omni-Compass has there, more copies of the service.
- **The founder's nine pieces, checked against what each can run** (register rows 79 to 87): Kepler 0.10 and later carry
  no model and on a machine without the processor's power registers run only a stand-in development meter, so Kepler runs
  where the registers are, never on GitHub's virtual machines; PEAKS has a design and meeting notes, no scheduler to run;
  CruiseKube (non-production use granted by its license) skips any workload whose HPA scales on CPU or memory, as every
  Kubernetes set here does, so its set pairs it with KEDA's HTTP add-on scaling on requests in flight.
- **CruiseKube built and preregistered** (register row 81; `docs/CRUISEKUBE_PREREGISTRATION.md`, workflow
  `kind-cruisekube`, `scripts/kind_addons_cruisekube.sh`, `tests/test_cruisekube.py`): native is KEDA's HTTP add-on
  and CruiseKube 0.3.4 in Cruise mode on the service, right-sizing it live; omni is Omni-Compass on top (the replica
  range through the plug, the node pool, the rollout guard; never the CPU limit, which CruiseKube owns). Every
  download pinned, CruiseKube's usage reports off, each arm learning longer than CruiseKube's hour and starting only
  once CruiseKube has applied a change. A trial run, never counted, records the chart's SHA-256 for the pin; then A,
  B and C. The engine is unchanged (omni-v5, digest `5648f290`).

## 2026-10-13: Every muscle its own card (Omni v5 re-declared)

- **The founder's question** (12 October, night): does every muscle have its own tuning, maxed to its own benefit,
  instead of one global setting for a thousand muscles? It does. The brain stays one; its settings are now each muscle's
  own: the engine reads every muscle's card from `realms/muscle_cards_v5.csv` (a machine pool's edge utilisation and
  window, a battery's line margin and, wired by its power, its hold window and hold margin). A muscle without a card runs
  the global setting; the tune-down never reads cards (`docs/FORMAL_V5.md` section 5, `docs/OMNI_V5.md` amendment 4).
- **How the cards are found** (`tools/tune_cards.py`, development seeds only): every muscle whose settings can change what
  the max does tries every candidate in a declared grid, today's global setting always among them; a card is kept only if
  it beats the global setting beyond the noise on seeds 7100-7109 and again on seeds 7200-7209, moved away from its aim than it nowhere,
  and is never behind native on any of those seeds under any load (never over its line more often, never less work,
  never its line cleared later). 409 of 550 searched muscles won once, 364 won twice and are the engine's cards (333
  machine pools, 31 batteries); no axis setting beat the global one. A first set chosen by the mean over the seeds alone
  (371 cards) was caught by the engine's own no-harm test before anything was pushed (an electrolyzer battery, one
  decision over its line on one seed); the rule now checks every seed.
- **V14, the body has the last word on a line it shares**: inside a body a battery wired by its power keeps the body's
  margins on its line. In development the one plant behind native the cards produced was exactly that battery.
- **The official run** (preregistered seeds 3000-3009, commit `eea29150`, fingerprint `5648f2902f1fae68`, class S):
  every muscle alone 527 toward their aims (517 with one global setting), 421 at their limit on native, 159 the same, 0 away from their aims; inside
  the six organisms 0 plants with less work or more misses under every load; misses fall 1.9% to 7.5% (own load), 1.4% to 7.2% (the climb) and
  1.1% to 8.3% (work waiting in line), against 1.6% to 6.4%, 0.9% to 3.5% and 1.0% to 7.2% with one global setting, with
  less power given and less wear inside the bodies (`results/realms_v5/REALMS_V5.md`). Alone, a machine pool's card
  spends more machines to clear its line sooner (power given +33% against +21%).
- **Earlier tonight, on one global setting** (fingerprint `9be48445`): GitHub reproduced the realms table exactly in runs
  A, B and C; the first Goldilocks run (ten pairs) answered the 95th percentile in 133 ms instead of 331 and spent 99%
  less time over the line, for 2.3% more energy on the declared model; the first capacity run showed no difference beyond
  the noise at any cap (the quota on the service's CPU refuses the extra copies that are Omni-Compass's one lever there).
  Each runs again, A, B and C, on this version; the grid starts again on it (the manifest before kept in
  `results/grid_v5/history/`).
- The manual's muscle catalog prints every muscle's card in plain words; the evidence of the search is in
  `results/cards_v5/`.
- **No 1,000s anywhere** (the founder's order of 12 October): the GPU kit's organisms with the card inside run at 1, 10
  and 100 copies (amendment 13 of `docs/GPU_PREREGISTRATION.md`; one card's whole test about 36 hours instead of 45), the
  rented-machine grid script is removed, and the manual's grid chapter (54 squares), the benchmark map and the KWOK
  workflow say 1, 10 and 100.

## 2026-10-12 (midnight): Omni v5 re-declared: the living body, and the founder's nine open-source pieces as muscles

- **The living body** (the founder's order of 12 October: whatever one muscle has a problem with, the others carry it, and
  nothing is locked; `docs/FORMAL_V5.md` section 4, `realms/compass_arm_v5.py`). Eight causes of a plant doing less work or missing its line more often
  inside a body, found on development seeds only (7100-7299), and the property of the code that removes each: a
  battery's charge counts as room on its line only while it lasts (V6); machines a queue needs are never handed back
  (V7); every room has a twin, the same room under its operator's settings warmed by native's heat, equal to the room to
  the last digit while the max writes nothing (V8); a pull-down is handed back over the cooling's own reaction time,
  never snapped (V9), and granted only out of the room the lines have for that time (V10); a room that cannot cure
  itself puts a heat debt on the body, which hands back machines until no such room is warmer than native's (V11); a
  battery times its discharge after reading its line for a window (V12); and a forecast starts at the plant's first
  reading (V13: the jump from a plant's initial values to its first reading had locked every battery's timed discharge
  for the whole run). The battery's admission gate stays native: deferring a site's flexible load left work not caught up
  by the end of a run (work first). Four tests added to `tests/test_compass_arm_v5.py`.
- **The nine open-source pieces as muscles** (the catalog's third wave): Kepler, Climatik, EAR (two), CruiseKube,
  Goldilocks, the Kubernetes power manager, PEAKS, adaptive GPU power capping and NVIDIA's platform power budget, ten
  muscles (2172-2181), each in the spine family its knob belongs to. The catalog is 1,107 muscles in 70 families; the
  organisms 540, 404, 480 and 484, the four stacked 1,908, the shared spine 267 (`docs/OMNI_V5.md`, `docs/REGISTER.md`
  section 1, `docs/MUSCLE_CATALOG.md`, the manual's chapter 2).
- **The engine re-declared**: omni-v5, digest `9be48445438943c2` (43 files, `OMNI_V5.json`); every result is run again on
  it. The grid's manifest starts empty (`results/grid_v5/DISPATCHED.json`), the one before kept whole in
  `results/grid_v5/history/DISPATCHED_omni-v5_8d4f91f0.json`, and the conductor counts runs only from the push.
- **The official run** (preregistered seeds 3000-3009, commit `44aceb48`; class S): 0 of 1,107 muscles away from their aims (517
  toward their aims, 421 at their limit on native, 169 no difference beyond the noise); every organism with fewer misses under all
  three loads; **0 plants with less work or more misses inside any organism** under any load, where the engine before left 3 away from their aims under the climb.
  Misses fall 1.6% to 6.4% under each organism's own load, 0.9% to 3.5% under the climb and 1.0% to 7.2% with work
  waiting in line, against 0.1% to 0.7%, 0.0% to 2.1% and 0.1% to 2.1% before (`results/realms_v5/REALMS_V5.md`).
- **One lock left, said plainly**: a line that once jumped is read as able to jump that far again for the rest of the
  run. Removing it roughly triples the misses removed on development seeds, but in 36 of 400 runs a machine pool whose
  queue sat at its limit then did more work and took one decision longer to clear it, which the decision count reads as away
  from its aim. That is the next version's work, told to the founder first.

## 2026-10-12 (night): Goldilocks built as a benchmark; the capacity test's rates; the last 1,000s removed

- **Goldilocks with the Vertical Pod Autoscaler** (register row 80, the first of the founder's nine open-source pieces
  built as a benchmark): `scripts/kind_addons_goldilocks.sh` installs the VPA 1.7.1 recommender and Goldilocks 4.16.2
  (every file SHA-256 pinned, every pod on the control plane), lets the recommender learn the service while the load runs
  the benchmark's own steps, and applies the recommendation as the VPA applies one (`tools/goldilocks_apply.py`); native
  and Omni-Compass on top are then measured on the same rightsized service (`ADDONS=goldilocks` in
  `scripts/kind_bench.sh`, workflow `kind-goldilocks`, preregistration `docs/GOLDILOCKS_PREREGISTRATION.md`, tests in
  `tests/test_goldilocks.py`). The KEDA checks in `kind_bench.sh` now key on KEDA alone, and every reset check reads the
  operator's own CPU limit back, whatever it is.
- **The capacity test's rates** (amendment 1 of `docs/CAPACITY_PREREGISTRATION.md`, from the tuning case, before run A):
  two cores serve about 10 requests a second within the line, so the counted rates are eight steps of 150 s, 4 6 8 10 12
  14 16 20 requests a second; nothing else changes.
- **No 1,000s anywhere** (the founder's order of 12 October): the KWOK scale test runs 10 and 100 nodes, the organism
  ladder 100 runs at 1x, 10x and 100x, and the dossier's open items say the grid stops at 100.

## 2026-10-12 (late night): The seat, the receipts in their totality, the max written formally

- **The seat** (`docs/THE_SEAT.md`, in the book after "What Omni-Compass Is"): Omni-Compass is the governor on top of the
  muscles; the five systems named most often (IBM Turbonomic, Karpenter, NVIDIA's GPU power software, the Energy Aware
  Runtime, the Cluster Autoscaler with the commercial layers above it) with source, kind and how Omni-Compass sits with
  each; nine open-source pieces read from their own repositories (license, last change, kind, where each can run);
  who owns Omni-Compass and on what terms it is seen. Read from the projects themselves: CruiseKube is under the Business
  Source License (source-available, not open source); the Adaptive GPU Power Capping code carries no license; Climatik and
  PEAKS are early.
- **The receipts, in their totality** (`docs/THE_RECEIPTS.md`, at the head of "Proving It"): every result read together,
  receipt by receipt, by evidence class and engine, with what each shows and what it does not; the decisive receipt still
  to be produced is the chip's own energy meter on a real GPU.
- **The max, formally** (`docs/FORMAL_V5.md`, in "The Mathematics"): the setting, the two arms, the definition of one
  governor against a collection of tools, five properties the code guarantees (one wire; never fewer machines than
  native asks for; native at its limit left alone; grants only out of the shared lines' room, a forecast bound; the
  hand-back), the readings rule, what the runs measure, and the limits stated plainly. Its section 4 records why three
  plants moved away from its aim inside the organisms under the climb and the next version that fixes them (built and tested on
  development seeds: 19 plants with less work or more misses in 400 organism runs before, 7 after, the gains kept), which enters the engine only
  as a new version, the founder told first.
- **The register** rows 79 to 87: Kepler as the shared meter, Goldilocks with the Vertical Pod Autoscaler, CruiseKube,
  Climatik, the Kubernetes Power Manager, PEAKS, the HPDC '25 learned GPU power capping, NVIDIA's platform power manager
  and the Energy Aware Runtime, each with Omni-Compass on top of it as the native.
- **The wiring search** (`tools/wire_search.py`, `results/development/wiring/`, development seeds only): every muscle
  through fourteen candidate cards in the official loop under a rule fixed before any result was read; 503 muscles gain
  on the max alone, 670 on each muscle's own card, 427 on none (chiefly the 274 admission gates, which native already
  holds fully open), none away from its aim. Nothing in the engine changes; the cards enter it only as a new version.

## 2026-10-12 (night): Every workflow fetches the code, not the 25 GB archive; the capacity test

- **Why the Azure runs stood still.** The archive of raw runs (`results/live/raw`) has grown to 25.5 GB in 81,867 files,
  more than a GitHub machine's free disk. Sixty-three checkouts in thirty workflows (among them Azure's managed
  Kubernetes, `aks-metered.yml`) still fetched the whole tree, so they could not get past the checkout; the two Azure
  runs started this evening were cancelled in their checkout, before any Azure machine was rented (nothing billed). Every
  checkout now takes the code and everything else except that archive, as `verify.yml` and the grid already did; the
  KWOK report no longer runs on a push that ran no KWOK test.
- **1, 10 and 100 everywhere.** The rented-machine workflows (`big-organism.yml`, `big-organism-detached.yml`,
  `cloud-organism.yml`) default to 100 copies, and every copies input reads 1, 10 or 100.
- **The capacity test** (`docs/CAPACITY_PREREGISTRATION.md`, `capacity.yml`, `tools/capacity_report.py`,
  `deploy/kind/loadgen-meter.yaml`): native, and Omni-Compass on top of native, held to the same resource cap (a quota on
  the served app's CPU, enforced by the cluster) at 1, 1.5, 2 and 3 cores, under a load that rises past what the cap
  can serve; a work meter counts every request (within the line, late, failed, never sent). One row per cap level with
  its plain audit line: more work from the same cap, a loss reported as it stands, no difference beyond the noise, or
  (when the cap was never reached) speed and not more work. The engine is unchanged.

## 2026-10-12 (evening): The grid is 1, 10 and 100 only, the founder's order

- **No 1,000s.** Every organism runs at 1, 10 and 100 copies, each to 100 runs: 54 squares, native and Omni side by side,
  modelled and with the real cluster inside (`scripts/dispatch_grid.py`, `grid.yml`, `six.yml`, `six-kube.yml`,
  `tools/pool_scale.py`). The 1,000-copy squares and the 1,000-run blocks are gone, to cut the time and the bill.
- **Nothing is rented for the grid.** Every square fits GitHub's own machines, so the conductor's rented-machine part is
  removed (it existed only for the 1,000-copy squares) and the eight Azure machines that ran them are stopped. The runs
  made at 1,000 before the order are kept as recorded and counted in no square.
- **Time**: the modelled grid is fully started (1 and 10 copies done, 100 copies running); the grid with the real
  cluster inside needs 1,800 jobs, about 12 hours on GitHub's machines, free for this public repository.

## 2026-10-12: The grid with the real cluster inside, protocol 2 (the test rig amended; the engine unchanged)

- **What failed, and where.** Of the first runs with the real cluster inside, three causes marked repetitions invalid or
  ended jobs, all in the test rig, none in the engine (omni-v5, unchanged): the four stacked at 100 copies, repetition 3,
  made 47 of its governor's 60 decisions by the end of its window (one every 78 s against one a minute), because the
  modelled organism ran at normal CPU priority beside a governor at the lowest (nice 19), in the same cgroup, so the rig
  outranked the governor; the bench's wait for the governor could not see it (started in a subshell), so a late governor
  was still deciding when its decisions were counted; and GitHub refused two downloads (kind's checksum file, which ended
  a job before either arm ran, and the metrics-server manifest, HTTP 504, which marked an arm invalid).
- **Protocol 2** (`scripts/kind_bench.sh`, `docs/K8S_COMPASS_PREREGISTRATION.md`, carried in each run's name): with the
  organism inside, the governor runs at the organism's own priority (nice 0), never below the rig; without it, nice 19 as
  before. The decisions that count for validity are those inside the measured window (the 80% rule stands), with the
  mean time between them shown. A governor still running when the window ends is stopped through the master switch and
  watched until it is gone, before any check reads the cluster. The count, the stop and the retried downloads hold for
  every kind test from this commit; the priority changes only where the organism runs beside the governor.
- **Downloads tried again**: kind v0.31.0 (Kubernetes v1.35.0) and kubectl v1.35.0 are pinned at the versions every run
  so far used, with a second, slower, checksum-checked install when the first is refused (`scripts/kind_install.sh`, in
  every kind workflow); the metrics-server manifest is fetched once per machine and tried again; a kind cluster that fails
  to come up is tried again twice. The rented machines install the same pinned versions (before: whatever was newest).
- **Counting** (`scripts/dispatch_grid.py`): every square with the cluster inside is filled on protocol 2 alone. The
  protocol 1 runs (100 repetitions of every organism at 1 and 10 copies, 10 at 100 and at 1,000, and the first ten of the
  tower and the four stacked at 1,000 on rented machines) are kept, archived and shown beside, never pooled with protocol
  2. A repetition whose job fails is started again, up to three times, and paired within one run (`tools/six_kube_report.py`);
  one that fails three times is listed, never dropped. Every rented machine started counts against the budget.
- **Cost**: about 1,340 jobs run again on GitHub (free for this public repository; some seven hours of its queue), and the
  first ten repetitions of the two rented squares again, about $110 at list price.
- `tools/run_scale.py`: a shard always starts its first run (its deadline check read a run time before one was known).

## 2026-10-12: The grid filled to 1,000 runs in every square, on the max

- **Tonight's first dispatch was cut wrong and is replaced.** Its shards were sized from v3's run times; on the max a
  100-copy or 1,000-copy shard would have passed GitHub's six-hour job limit and handed in nothing, and with the cluster
  inside the 100- and 1,000-copy organisms could not keep the window's clock. 27 of its 31 runs were cancelled before
  any result (`results/grid_v5/DISPATCHED.json` says which); the 1-copy and 10-copy modelled squares (1,000 runs each)
  and the first ten repetitions with the cluster inside at 1 and 10 copies are kept.
- **Measured run times on the max** (work waiting in line): a paired run takes 7 to 29 s at 1 copy, 67 to 359 s at 10,
  11 minutes (compute) and 30 minutes (the tower) at 100, and at 1,000 copies the compute realm steps in 17.5 s and holds
  6.8 GB. Every shard is cut from these so it ends inside a runner's six hours and memory.
- **The conductor** (`scripts/dispatch_grid.py`, `grid.yml` every 15 minutes, and the six and six-kube buttons with their
  defaults): starts every run of every square not yet started, the 10-run squares of every size first, then 100, then
  1,000; reads started runs back from their own names and never starts one twice; keeps the repository's jobs at what
  GitHub runs plus a margin, so every runner is busy and other workflows still get one. The 1,000-copy shards are held at
  their first ten runs until those runs' own times are read back.
- **Nothing lost at a cutoff** (`tools/run_scale.py`): each run is written as it ends, with its plant sums, its own time
  and its memory; a shard starts no run past its deadline. `tools/pool_scale.py` says when a block is short of a run
  ("9 of 10"), and never pools across engines.
- **The four stacked at 1,000 modelled copies** is the four realms' runs on the same seeds joined plant for plant: its
  four bodies share nothing on the clock (each realm's own body, the founder's order), and whole it needs 30 GB, past a
  GitHub machine; joined and run whole agree to rounding (`tests/test_run_scale.py`).
- **Where a square cannot run on GitHub**: the tower at 1,000 modelled copies (about 6 hours and 15 GB a run) and the
  tower and the four stacked at 1,000 copies with the cluster inside (about 17 and 22 hours a repetition) run on rented
  Azure machines. With the cluster inside, the 100-copy tower and four stacked get 2,400 s and 3,600 s windows and the
  1,000-copy realms 7,200 s, so the max keeps the organism's clock; at 1,000 copies each arm runs on its own runner.
- **Jobs fetch only the code they run**: the whole tree (82,000 result files) took 16 of a shard's 20 minutes.

## 2026-10-12: Omni v5 at the max: every muscle at its own limit, work waiting in line, wear beside the work

- **The max is the default brain** (`realms/compass_arm_v5.py`, `V5CFG`; commits `8872db382`, `07a088433`): every
  muscle pushed to its own limit for the most work, never past it and never below native; the energy it takes is power
  given, shown beside the work, the speed and the wear. The tune-down (`V5SAVE`) is a position on the dial.
- **Work waiting in line** (`LINE`, a quarter of the run's own work at the start) for every muscle alone and every
  organism, beside the organism's own load and the climb; speed is judged where there is a line.
- **Axes at their own peak** (`s_peak`): joints, multirotors and road drives 1.25, a ship's engine 1.15; a reaction
  wheel, a train's line speed and an elevator's governor stay at their limit. Inside a body an axis keeps its everyday
  speed.
- **The bone and the lease** measured more finely: the forecast without the max's own machines, a room's degrees as a
  line, the catch-up of waiting flexible load first, machines started only when the lines carry them until ready, a
  measured hand-back; a floor that only held native's count let go at once at the kill.
- **The official table** (seeds 3000-3009, commit `07a088433`, `results/realms_v5/REALMS_V5.md`): of 1,097 muscles alone,
  504 toward their aims (489 clear the waiting line sooner, 385 over their line less often, 32 more work), 438 at their limit on
  native, 155 the same as native, 0 away from their aims. All six organisms ahead of native under all three loads. Under the climb,
  3 of 1,868 plants inside the organisms moved away from its aim (two server rooms 0.08% and 0.03% less work, one UPS once more over
  its line in 2,400 decisions); none under the own load or the line.
- **The front page** shows the engine that stands only (`tools/front_page.py`); the v3 front page is kept whole in
  `docs/history/FRONT_PAGE_2026-10-12.md`. The muscle catalog chapter is rebuilt from the v5 catalog with the max's words.
- **The grid** (`scripts/dispatch_grid.py`, `six.yml` with a load, `six-pool.yml`) is wired for the 96 squares under the
  line; the runs started on the earlier v5 brain were cancelled (their engine no longer stands).

## 2026-10-12: Omni v5 (branch v5): the live controllers, 1,097 muscles, the three-run words

- **The v5 law in the live controllers** (commit `403841c21`): the Kubernetes controller's compass law and the GPU
  governor hold their balance point at the v5 edge (`omnicompass/edge.py`, the same code the modelled law runs); the six
  organisms with a real cluster or card inside (`tools/run_kil.py`, `tools/run_hil.py`) run the v5 law on the v5 catalog,
  the four stacked keeping each realm's own body.
- **The catalog's second wave**: 1,097 muscles in 70 families (95 new: Financial Markets & Trading Systems, Media
  Streaming & CDN, Game Servers & Real-Time Interactive, Blockchain & Ledger Nodes, CI/CD & Build Farms, and additions to
  seven families); v5 re-declared (`OMNI_V5.json`); the official table rerun on the preregistered seeds
  (`results/realms_v5/REALMS_V5.md`, commit `04d9eb3b3`): 0 of 1,097 muscles behind native, all six organisms
  superior within guardrails, the whole tower, the four stacked and Energy / Facility each saving 3.0 times v3's.
- **Inside the organisms**: 1 to 3 UPS or power-distribution plants per organism one decision over their line in one of
  ten seeds (v3: 13 to 35); seven of the eight right after the safety cutoff, when every knob returns to native at once,
  one while Omni runs. A strict guard on the body's shared power lines was built and measured on development seeds: it
  removes them and almost all of the saving where those lines run full (Compute / AI / Cloud 0.47% to 0.01%). Held for
  the founder's decision; nothing in the engine changed for it.
- **Every cloud, the same tests**: Azure running on v5 (the 40-machine fleet, steady then burst; the whole tower and the four
  stacked at 1,000 copies on rented machines). Google and Amazon get Azure's big-machine test too: `cloud-organism`
  (scripts/cloud_machine.py, `scripts/organism_detached.sh`, scripts/cloud_machine_watch.sh; the price and a cost
  ceiling first, every machine labelled with its hour budget, always given back; tests/test_cloud_machine.py, run by
  `verify.py`), beside their Kubernetes bill tests (`gke-metered`, `eks-metered`). Setting each cloud up, click by click:
  docs/GOOGLE_SETUP.md, docs/AMAZON_SETUP.md (and `docs/AZURE_SETUP.md`). The Google, Amazon, Lambda and one-button
  workflows now register on the branch they are pushed to, so they can be started there.
- **The three-run words** (the founder's order of 11 October): no table or page says a result is "confirmed", because
  nobody outside The Omni-Compass LLC has reviewed or approved these results. A reading is lower or higher in all three
  of our runs, the same in all three, no difference beyond the noise, or the runs disagree; every three-run table, the
  Omni index, the dossier, the benefit sheet and the wiring verdicts say "Run and scored by The Omni-Compass LLC's own
  code. No outside party has reviewed or approved these results." and what preregistered means. The words are in
  `tools/readings.py`; the numbers in every table are unchanged. A GPU "confirmation" run is now called the counted run
  (its code name stays `PHASE=confirm`). Nine v3 tables that printed their title twice now print it once.

## 2026-10-11: the add-on test on main (Omni-Compass on top of KEDA)

- **Kubernetes with its add-ons, A/B/C on v3** (`docs/ADDONS_PREREGISTRATION.md`, declared before the first run; runs
  38096663118, 38099655092, 38099656930; 59 of 60 pairs valid): native is Kubernetes with KEDA 2.21 and its HTTP add-on
  0.16 owning the service's autoscaler; omni is Omni-Compass on top, its moves carried to KEDA's ScaledObject by the plug
  (`scripts/kubectl_keda.py`). With KEDA on the CPU target and the requests in flight (`results/live/V3_KEDA_CPU_REQUESTS.md`):
  p95 −51% to −53%, p99 −60% to −62%, time over the line −97% to −100%, toward its aim in all three of our runs; machines inside the noise. With the
  HTTP add-on alone (`results/live/V3_KEDA_REQUESTS.md`): p95 −73% to −76%, machines in service −5.9% to −7.8%, node-hours
  −5.8% to −8.2%, replicas −14%, toward its aim in all three of our runs. **away from its aim in all three of our runs in both:** the energy counted with parked workers at idle
  power, +1.0% to +2.6% (the closed-loop load put 24% to 54% more work through the service: its CPU, shown, not judged).
  The index moves to +5.2% (Kubernetes +31.8% over nine tests); the energy loss counts against Omni-Compass.
- The workflow (`.github/workflows/kind-addons.yml`), the plug, the add-on manifests (SHA-256 pinned), the KEDA role and the
  plug's tests (`tests/test_kubectl_keda.py`, a stand-in KEDA) are on main; every run commits its raw files and tables to
  `results/live/raw/addons-run-<id>/` on the branch it ran on, and the front page lists its runs.
- `tools/confirm_abc.py` reads one native setup's folder inside an add-on run (`addons-run-<id>/<setup>/`).

## 2026-10-11
- **The legal set at underwriter level.** `LICENSE` (Omni-Compass Evaluation License 1.0, revised 11 October 2026) now
  reads as a proprietary software asset's license: acceptance; definitions (evaluation, simulation, production use,
  commercial use, hosted service, derivative, results, Enterprise License); a copyright license and a patent license for
  evaluation and simulation only; every prohibited use (production, any commercialization or monetization, hosted or
  software-as-a-service offerings, resale and distribution, incorporation, competing products, machine-learning
  imitation, removing notices or the kill switch, safety-critical writes, the marks); rules for reproducing and publishing
  results, every row included; the Enterprise License path; ownership and the filings; patent and rights defense;
  feedback and contributions; the founder's reserved right to change the software, its documentation, its results and
  its terms at any time, without notice; safety; export control and sanctions; data; third-party components; term,
  termination and a narrow cure; no warranty; a liability cap; indemnity; U.S. Government end users; Delaware law and
  venue; general terms. New `ENTERPRISE_LICENSE.md` summarizes the paid license (production, hosted service, OEM and
  embedded, managed service provider, research; fees, deliverables, warranties, patent license, infringement indemnity,
  liability, confidentiality, data, security, safety, audit, transition and escrow). `.github/CLA.md` (assignment plus a
  contributor patent license), `TRADEMARKS.md` (usage rules), `SECURITY.md` (coordinated disclosure, fail-safe design),
  `LICENSING_FAQ.md` and `DISCLOSURES.md` follow; the SPDX copy and the SBOM carry the license word for word.
- **The notice as the founder ordered it (night of 10 October).** Two sentences are struck from the legal notice everywhere,
  and the notice now closes with the filing sentence and the website, nothing after it: "All patents, copyrights and
  trademarks filed in the USA. www.omni-compass.com". `tools/legal.py` holds the new wording (the page notice, the source
  header, the short line) and `--fix` wrote it into 663 files; the license papers (`LICENSE` and its SPDX copy, now revised
  11 October 2026, `NOTICE`, `DISCLOSURES.md`), the README's line under the headline, the assistants' rules files
  (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Copilot's and Cursor's), `CITATION.cff`, `REUSE.toml`, `codemeta.json`, the SBOM,
  the manual's front matter, the old closing lines of seventeen pages and the book's page footers, back cover and copyright
  page were rewritten by hand, and the printed book was rebuilt (520 pages, neither sentence in its text). `--check`, which
  `verify.py` runs on every push, now fails any file of any kind that still carries either sentence (`RETIRED`; a new test
  in `tests/test_legal.py`). The frozen engine files never carried them: omni-v3 is unchanged and no result is read
  differently. Two frozen originals keep a different sentence, about the introductory 10% license benchmark (that the
  benchmark may change or be withdrawn): the reference engine (`reference/`, held by its recorded SHA-256 and program fingerprint) and its
  dated source snapshot (`docs/handoff/`); they change only on the founder's word. The founder's reservation of the right
  to change the software, its documentation, its results and its terms at any time, without notice, stands in plain words
  in `LICENSE` section 9 (and its SPDX copy and the SBOM), `NOTICE`, `DISCLOSURES.md` item 4, the manual and the book's
  copyright page: it was taken out with the struck sentences by mistake and put back the same night.

## 2026-10-10
- **The notice everywhere, a front page the repository writes itself, and the book for the people who wire it (evening).**
  (1) **One legal notice, written once** (`tools/legal.py`): all rights reserved; all patents, copyrights and trademarks filed
  in the USA; www.omni-compass.com; every copy, export, report and printout carries it with `LICENSE`, `NOTICE` and
  `DISCLOSURES.md`. It now stands at the top and end of every page and table,
  in the header of every script, source file and workflow, at the top and end of every workflow job's report, beside every
  file a workflow hands out (`legal-notice`), and in every zip (`tools/export_zip.py`); `verify.py` fails any push where a
  file lacks it. The 67 files locked by a fingerprint (the engine, its C++ twins, the reference engine, the pre-registered
  harness) keep their earlier header until the next engine version rewrites them. `LICENSE` revised: licensed, not sold; no
  rights by implication; feedback; lawful use and export control; severability; the filing sentence in the founder's words
  with no grant claimed; `NOTICE`, `REUSE.toml` (the third-party traces marked as theirs), the FOSSA custom-license rule, the
  SBOMs and `CITATION.cff` with it. Instruction files for every AI assistant that reads the repository (`AGENTS.md`,
  `GEMINI.md`, `.github/copilot-instructions.md`, `.cursorrules`): every answer opens and closes with the notice. Two pages
  that promised "research and non-commercial use" corrected to the license's evaluation-only terms. (2) **The front page
  writes itself**: within minutes of every finished benchmark run, and every hour, `front-page.yml` rebuilds the five live
  products' tables from their three newest runs and writes the engine on main, the index now, every table by when it last
  changed and the newest run of every benchmark; the runner's folder path is gone from its lines; its checkout keeps off the
  archive of raw runs; the old front page is kept whole in `docs/history/FRONT_PAGE_2026-10-10.md`. (3) **The package version
  follows the engine** (0.3.0 is omni-v3; `verify.py` checks it, so a changed engine cannot keep an old number). (4) **The
  manual**: the card for the glove box at the front; reading paths for the data-center operator, the engineer on call,
  security and counsel; 6.5 the reflex rule (one body, one brain); 10.11 the data center under the servers (cooling, power,
  batteries; built connectors, modelled evidence, no live facility yet, said so); the reflex rule's own chapter in the book's
  Part One; the page foot, the copyright page and the back cover in the founder's wording; the book rebuilt, 520 pages.
- **The founder's afternoon orders, held and pushed as one (15:45 UTC).** (1) **Omni v4 ordered**: the collective mechanism, one
  body, one brain, one tick a second; a trial runs to its full measurement and is never ended by the calm it causes; the brain never
  forces, it reacts to what the system shows; the body's cost is judged with a guard for every part; one trial at a time inside a body;
  nothing permanent; the wall belongs to the body; every wire forced through it (`docs/OMNI_V4_PLAN.md`, rewritten). Everything is
  wired; staying native is the brain's live decision every second, never a verdict from one run. (2) **Six organisms**, restated and
  never again counted beside the live products; realms re-cut by a written rule at v4. (3) **The final coverage sweep** against the
  internet: register rows 74 to 78 (game server fleets, ledger nodes, build farms, network security engines, device brokers), lines
  on rows 9, 13, 19, 32 and 42, any vendor's card in section 2.3, five families and the robotics widening for the catalog at v4, the
  mega-caps' closed systems mapped to the open analogs that carry the same muscles, a ledger node's consensus added to the
  exclusions (`docs/REGISTER.md`, `docs/COVERAGE_MAP.md`). (4) **The legal wording** on every page outside the frozen engine: "all"
  before patents, copyrights and trademarks; "All rights reserved"; www.omni-compass.com; every export carries the notice, the license, the NOTICE and the disclosures (190 files, `LICENSE` section 9,
  `NOTICE`, `DISCLOSURES.md` item 4, the SBOM's embedded license, `CLAUDE.md`). (5) **Two faults GitHub's own runs showed and no
  local check had**: the release manifest not refreshed after the morning's last document edits (GitHub's verify red on four commits;
  refreshed) and `.github/workflows/cpu-power.yml` refused by GitHub since its first push for an unquoted colon in a step name (ten
  failed runs with zero jobs; quoted); `verify.py` now parses every workflow file (PyYAML in the requirements). (6) **The second set
  of the five live products** complete (21 runs, every job green) and archived; its early reading from the logs in
  `docs/RERUN_2026-10-10.md` and the manual's 16.6c: the Kafka gain is real and cheap and the trial's measurement is the fault, four
  trial rules written for v4. (7) The README leads with the newest work and carries a "Find it" section of the terms people search
  for; the word "simulation" is kept only in the license's own phrase and for third-party simulators by name, our own models being
  "modelled". (8) **The repository keeps itself current**: `.github/workflows/front-page.yml` runs after every finished live run
  of the five products, archives it with the code and runs `tools/front_page.py`, which groups the archived runs by what they are
  (product, objective, engine, workloads), takes the three newest complete runs of a kind as A, B and C, rebuilds every table whose
  runs changed (the old one kept whole in `docs/history`), then the index, the wiring page, the benefit sheet and the dossier, and
  writes the newest lines into the README's latest block; `results/live/FRONT_PAGE_STATE.json` records what each table was built
  from (seeded with the first set of 10 October); tests in `tests/test_front_page.py`, run by `verify.py`.
- **Every table remade from the rerun of 10 October** (69 of the 71 runs landed by 12:30 UTC; `docs/RERUN_2026-10-10.md`,
  "what landed"): the seven Kubernetes tests, the two robustness scenarios, the five stacks under both objectives (two new
  tables for the service objective, `results/live/V3_REDIS_SERVICE.md` and `results/live/V3_KAFKA_SERVICE.md`), the four
  simulators and the six organisms with the cluster inside were read from the archived runs by their table tools; the grid's
  receipts at 1, 10 and 100 copies were replaced (the 1,000-copy run's one cut-off shard runs again); the index, the wiring page,
  the benefit sheet and the dossier were regenerated; 19 superseded tables and 3 receipts went whole to `docs/history`. The index
  reads **+4.8%** (service reading +10.7%): Kubernetes +28.9%, PostgreSQL +0.8%, Kafka +0.1%, Redis nothing, MongoDB +0.7%, MySQL
  +1.0%. The five stacks ran for the first time with the brain's own verdict on the knob: PostgreSQL, MySQL and MongoDB gave memory
  back where it paid and lost nothing; **Kafka and Redis read nothing because every spend trial on Kafka and most on Redis were
  abandoned before they were judged**: the rule of 9 October ended a spend trial when the service turned calm, and a spend that
  works calms the service within seconds. **Amendment 3** (Redis, Kafka, MongoDB) and **amendment 4** (PostgreSQL, MySQL):
  `tools/knob_verdict.py` lets a spend trial run to its samples, only the wall or the engine's own time limit ending it early; a
  give-back trial still ends when the service leaves calm; `tests/test_knob_verdict.py` holds both rules; the five stacks run again
  on it and that set becomes the result of record. The state of play, the README, the engine page, the register, the manual and
  the history index carry the new numbers; the earlier numbers stay in the history pages and in the dated paragraphs.
- **The Linux kernel benchmark, built and preregistered** (`docs/CPU_POWER_PREREGISTRATION.md`; `tools/run_cpu_power.py`,
  `tools/cpu_power_abc.py`, `scripts/cpu_power_run.sh`, `.github/workflows/cpu-power.yml`, `tests/test_run_cpu_power.py`, run by
  `verify.py`), at the founder's order that the kernel's own knobs be benchmarked: the kernel's frequency governor as shipped is
  native; Omni moves the frequency ceiling of every CPU through the kernel's own files inside [half the top clock, the top], the
  governor still running under it; the compass law holds the service's own latency at 40% of a 20 ms line; every notch down is
  tried on the machine itself first by the brain's verdict (the knob verdict around the engine's own, unchanged); the snapshot is
  taken once, the ceiling handed back and read back, one writer, the master switch and the lease honoured; energy from the
  processor's own meter (RAPL, class P with the caveat stated) and a wall plug where fitted; a CPU-bound service under an open
  stepped load, the same requests in count and spacing in both arms. GitHub's machines are virtual and expose neither the governor
  nor the meter, so the workflow runs the tests and the probe there and the benchmark on a machine on the metal (the founder's own,
  a rented bare-metal server, or a self-hosted runner), in one command. The knob verdict gains a third objective, **per-work**
  (the resource per unit of work inside the line, the card's reading), declared for this benchmark's second set; the five stacks'
  counted runs keep the resource objective and are untouched by it. The manual (10.10; PDF rebuilt), the integration manual, the
  harness page, the documents index, the register (row 18), the proof program (row 6), the state of play and the wiring page's
  knob table carry it. No run yet: it waits for a machine.
- **The coverage map, the founder's second check the same night** (`docs/COVERAGE_MAP.md`; register rows 58 to 73 and the
  exclusions paragraph of section 4; proof program rows 50 to 62): every domain in the world of controllers walked against the
  register and the 59 muscle families, each read as done or running, queued, model only (with the nearest candidate named and why
  nothing open exists yet) or excluded by rule; the abbreviations the founder asked about (AKS, CPU, UPS, GPU, AWS, EKS, GKE, HPA,
  KEDA, KWOK, RAPL, RAN, FHIR, FIX, ROS, AMoD, EV, HVAC, PLC, CDN, ATM) each given its place. Added: self-driving stacks (Autoware on
  CARLA, openpilot), the EV powertrain (FASTSim), mobility fleets (AMoDeus), stream processing (Flink's autoscaler), storage clusters
  (Ceph), AI batch admission (Kueue, Volcano), games (Godot, candidate), thermal plants (the open Modelica libraries, candidate; nuclear
  stands as the model only because no open plant benchmark ships a controller), fabs (candidate), surgical robot servos (candidate),
  the other Kubernetes scalers (Karpenter-class, the Cluster Autoscaler, KEDA, VPA, which the proof program had and the register did
  not), distributed SQL, the other brokers, CDN caches, air traffic management (BlueSky), observability pipelines. Written as rules:
  safety reserves, clinical dosing controllers, trading decisions, weapons, a person's command and solvers without a controller are
  never a knob.
- **The founder's sweep: nothing with value left out** (register rows 39 to 57; proof program section 3.5): operating systems (the
  Linux kernel's scheduler, network and memory knobs; Windows processor power management on the founder's own laptop), television
  and streaming (adaptive bitrate), telecom (a software 5G cell), web platforms and social media (the serving layer; the LDBC Social
  Network Benchmark on a graph database), financial trading infrastructure (a matching engine and a FIX gateway; Omni governs the
  machinery, never a trade), serverless (Knative), distributed compute (Ray, Dask), HPC power saving (Slurm) and scientific
  workflows, oil, gas and heat networks (pandapipes), a wind turbine (OpenFAST with ROSCO), agriculture and irrigation, healthcare
  systems, robotics navigation, humanoids and marine vehicles, mining (a candidate until an open source with a shipped controller is found), video transcoding; aerospace and rockets were already rows 32 to 36. Each row names an open benchmark anyone can
  run, its shipped controller as native and one knob for Omni, and is preregistered before its first run.
- **Every benchmark run again on one commit** (`docs/RERUN_2026-10-10.md`): at the founder's order that every result be as of today,
  the seven Kubernetes tests, the five live stacks on the brain's own verdict (the resource objective; Redis and Kafka also under the
  service objective), the four simulators, the realms table and the kill and long robustness scenarios (three runs each), the six
  organisms with the real cluster inside, the modelled grid at 1, 10, 100 and 1,000 copies and the two big organisms at 1,000 copies
  on rented Azure machines were dispatched between 01:24 and 01:31 UTC on commit `3aac0ab7` (Omni v3 by `tools/omni_version.py`),
  native and omni, the wiring of each checked against its preregistration before the dispatch: 70 GitHub runs and two Azure
  machines. The five preregistrations' dispatch paragraphs, the state of play, the register (every row marked), the manual (9.4,
  16.6b), the wiring page and the v4 plan say so. Every published table stands until its new set lands; the new set then supersedes
  it and the old table goes whole to `docs/history`. Not restarted: the three 24-hour robustness machines (the same harness byte for
  byte, ending about 10:15 UTC) and the Azure fleet, which waits on the family allowance those machines hold.
- **The audit after the dispatch, at the founder's order that every term of 9 and 10 October be wired everywhere**: the wiring
  page gains a knob-by-knob table of where the brain's verdict stands today (the five stacks both ways through
  `tools/knob_verdict.py`; the cluster's machines, the card's clock ceiling, the robots' speed and the drones' cruise by the
  engine's own verdict; the grids, the districts and the 945 modelled muscles by the law alone, their trial being the next engine),
  pointed to from the state of play and the wiring guide, which now states how to wire for superiority (watch first, the
  observation run, the brain's verdict on the knob, the operator's setting always free). Three places that read "not confirmed"
  against the rule (the manual's PostgreSQL paragraph, the state of play's PostgreSQL row, the PostgreSQL preregistration) now read
  "inside the noise by the rule"; the manual's valley metaphor no longer uses the word the founder retired. The rerun record
  carries the measured length of every kind of run (from the earlier run of each kind, in runner-hours) and the two-day timeline.
- **The gaps the tree shows, written into the register** (the founder's reading of 10 October): the index's six real categories are
  Kubernetes, PostgreSQL, Kafka, Redis, MongoDB and MySQL; Azure waits on its three-run close and the card on its run on the current
  controller; the power grids and the districts are in as simulations, never in the index by rule. What is not yet a category: a
  second and a third cloud (AWS and Google Cloud under Azure's method, new row 38 of the register's queue: each needs its own
  account credential in a GitHub secret and its own allowance, nothing spent until then), CPU power through Linux's own governor
  with RAPL (row 18, now saying what it needs: a machine where the governor and the meter are writable, the founder's own tower or a
  rented bare-metal server, since GitHub's runners and cloud machines allow neither), and the card's energy meter, which the card
  harness already has (the integral of the device's power draw, the CPU package by RAPL, the wall plug where fitted) and which reads
  on the founder's run. The state of play lists the three as open item 8. (`tools/benefit_sheet.py`, `tools/wiring_verdicts.py`, both pages regenerated):
  the founder found the sheet read backwards against the tables (plus is good on the sheet; a cut reads minus in a table). Now the
  sheet's number carries its word (gain, loss, nothing) and every change the same in all three of our runs is written out beside it: a gauge that fell when
  falling is good reads **cut** (less waiting, fewer machines, less energy, less memory), one that rose when rising is good reads
  **up**, each with **good** or **cost**; the wiring page's columns, causes and loss list use the same words. The tables keep their
  raw signs with the Reading column beside them, and how to read the results and the manual (14) say so.

## 2026-10-09
- **The benefit sheet: one number per benchmark, plus always good for Omni** (`tools/benefit_sheet.py`, `docs/BENEFIT_SHEET.md`,
  `results/BENEFIT_SHEET.json`, checked by `verify.py`): at the founder's order that a reader must never have to work out
  whether a minus is good, every benchmark gets one figure whose sign always means the same thing (less energy, fewer machines,
  less memory, a shorter wait all read plus), with yes, no, none or trade beside it. The number is the Omni index's own reading
  where the test is in the index, and the same arithmetic over every judged gauge for the simulators and the organisms. README,
  the documents index, how to read the results, the state of play and the manual (14, the appendices) point to it.
- **The brain's own verdict on every live knob, in real time** (`tools/knob_verdict.py`, `tests/test_knob_verdict.py`; the five
  harnesses `tools/run_redis.py`, `run_kafka.py`, `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py` and their three-run table
  tools; the five workflows take an `objective` input; `verify.py` runs the tests): at the founder's order that the brain must
  decide, on the muscle and in real time, whether a knob pays before it writes it, every live knob now starts in watch and is
  written only inside the allowance a paired trial on the stack itself has earned, one notch a trial, under the declared
  objective (resource: the index's reading, the default; service: work and speed alone). A refused step is not taken, a trial
  holds the knob, a fail-up never spends beyond the allowance, the operator's setting is always free. The trial, the judge and
  the allowance are the frozen engine's own `omnicompass/verdict.py`, unchanged: Omni v3 stays v3. The audit lines carry the cost
  sample and the verdict's state every second; the arm records and the three-run tables carry the verdict per workload. Declared
  as amendments (Redis 2, Kafka 2, PostgreSQL 3, MySQL 3, YCSB 2) with the expectation written before the runs; no run dispatched
  yet, at the founder's word. The manual (9.4, 16.6b, appendix B), the integration manual, the state of play, the register and the
  wiring page carry it; `docs/OMNI_V4_PLAN.md` designs the same verdict per muscle inside the engine as the next engine, not built.
- **Wire in, or watch: the verdict per knob, from every result** (`tools/wiring_verdicts.py`, `docs/WIRING_VERDICTS.md`,
  `results/WIRING_VERDICTS.csv`, checked by `verify.py`): at the founder's order that Omni need not be wired into every
  muscle (where it cannot beat native, the muscle stays native and Omni only reads it: one wire out, no wire in), every
  three-run table, the four simulator tables, the 945 modelled muscles and the organism tables are read by one rule into
  three words: **write** (a gauge toward its aim in all three of our runs, none away from its aim in all three of our runs), **watch** (nothing toward its aim in all three of our runs; a loss is
  named with its cause) and **operator's choice** (a trade, shown with both readings of the index). Real stacks 12 write, 7
  operator's choice, 5 watch of 24; simulators 21, 15, 3 of 39; modelled muscles 124, 13, 808 of 945 (746 never wrote); the
  14 organism cells with the cluster inside all write on the cluster's gauges. Every loss in all three of our runs on a real stack is listed
  with its cause: Kafka's consumers and the CPU they poll with, Redis's memory, MySQL's pages on a written working set, and
  PostgreSQL's connections above the operator's setting on `simple_update`, where nothing was bought and the verdict is
  watch. The engine is unchanged (Omni v3); the page decides what an operator connects. README, the register, the state of
  play, how to read the results, the Kubernetes preregistration (the declaration), the wiring guide, the integration manual
  and the manual (1.2, 16.6b, the appendices; PDF rebuilt) carry it.
- **A second reading of the Omni index, declared beside the first** (`tools/omni_index.py`, `results/OMNI_INDEX.md`,
  `docs/K8S_COMPASS_PREREGISTRATION.md`): at the founder's question about what a cache is for (Redis is bought for speed and
  spends memory to deliver it; the resource reading counts that memory as a cost and reads Redis at −24.9% while its work and
  hit rate read toward its aim in all three of our runs), the same tests and the same three-run rule are also scored on **service alone, work and
  speed**, with machines, energy, memory, connections and consumers shown and not scored, for every test alike. The service
  reading stands at **+71.8%** (Kubernetes +83.2%, Kafka +1,192.8%, Redis +8.8%, the three database stacks exactly nothing,
  their gains being resources given back); the resource reading, +20.5%, stays the headline the program preregistered. Both
  are printed in the same tables as two columns; a loss in all three of our runs in work or speed counts against Omni in both. README, the
  state of play and the manual (summary, 16.6) carry the second number beside the first.
- **The whole tower at 1,000 copies with the real cluster inside, on v3, 3 of 3 on the clock** (`results/live/V3_BIG_ORGANISM.md`,
  now both big organisms side by side; started by run 37756284680, collected by run 37945866426 after 25 hours on one rented
  Azure machine, eastus `Standard_D8as_v4`, a 10,800 s window of 240 steps of 45 s, commit `6f0f93e5`, Omni v3): 945,000
  modelled muscles on one clock; the cluster's **p95 6,690 → 160 ms (−98%)**, p99 9,068 → 187 ms, **time over the line 76% →
  0, failed requests 4.8% → 0**, all clear of zero; replicas, pods started and machines (6 in both arms) the same or inside
  the noise; energy inside the noise; both arms 14 s behind the window; the organism's model energy −0.4% and work
  rounding-level lower, shown. The machine was deleted by the collect. The v3 record, register row 8, state of play, the
  manual (2.5, 16.2, the evidence map) and the Kubernetes preregistration carry it.
- **The second counted sets of PostgreSQL and MongoDB and the third of MySQL, on the amended harnesses: the costs are gone,
  the gains are smaller and real; the index moves from +24.1% to +20.5%** (runs 37858494179, 37858496620, 37858499033;
  37858501997, 37858505059, 37858509109; 37858512907, 37858515717, 37858519010; commit `310cf318`, Omni v3; the earlier
  tables kept whole in `docs/history`). **PostgreSQL** (`results/live/V3_PGBENCH.md`): host CPU and median latency inside the
  noise on all three workloads (the first set's +14% to +28% and +15% to +17% higher, gone); connections held open **−36% to
  −38% on `select`, toward its aim in all three of our runs**; `simple_update` connections most at once **+72% to +80%, away from its aim in all three of our runs** (amendment
  1's add rule buying servers above the operator's 20 on a slow write workload, as in the first set, nothing bought); the runs
  disagree on `tpcb_hot`; category +4.0% (was +14.2%). **MongoDB** (`results/live/V3_YCSB.md`): the cache held **−21% to −36% on
  all four untouched workloads, toward its aim in all three of our runs**, settling at 330 to 405 MB where the gate finds the working set; the burst
  mean latency inside the noise (the +2% to +4% higher, gone); 8 rows toward their aims, 0 away from their aims; category +8.5% (was +10.2%). **MySQL**
  (`results/live/V3_SYSBENCH.md`): burst pool **−49% to −56%, toward its aim in all three of our runs**; read_write pages holding data **+44% to +52%,
  away from its aim in all three of our runs** (was +53% to +70%) with host CPU **−4% to −6%, toward its aim in all three of our runs**, a trade; read_only inside the noise (the
  second set's −50% to −56% was in part the cold-start give-back now refused); update_index the runs disagree; category +5.2%
  (was +12.2%). Every knob handed back in every arm; no controller fault. The index, the dossier, the register, the v3 record,
  the state of play, README and the manual carry the new tables.

## 2026-10-08
- **The costs in the three database tables traced to their mechanisms, and the three that were ours amended, with the engine
  locked** (Omni v3 before and after; the harnesses are outside the fingerprint). **PostgreSQL** (`docs/POSTGRES_PREREGISTRATION.md`,
  amendment 2): the +14% to +28% host CPU was not "PgBouncer queuing", as the record had said without a measurement; it was
  our harness launching a `psql` process for every reading (7,956 console logins in one workload's pooler log; 52 ms of CPU
  a launch; a per-process meter on a paired `select` repetition put +55.9 CPU-seconds on the launches against a +52.8 s host
  difference, PgBouncer +1.2 s, PostgreSQL −4.7 s). The harness now holds one console connection an arm (`Console`, the
  server's own wire protocol), takes a server back only while clients waited for one under 1% of the pooler's time and a
  transaction was served, adds servers back one per percent of waiting, up to the operator's 20 (the +15% to +17% median was
  the pool shrunk into a queue), and records its own CPU. **MySQL**
  (`docs/MYSQL_PREREGISTRATION.md`, amendment 2): 36 of read_write's 82 grows came with the pool missing under 1% of its
  reads (slow writes the pool cannot mend); the pool now grows only while missing (1% or more, the give-back's own line), and
  no chunk is given back in a second with no read request. **MongoDB** (`docs/YCSB_PREREGISTRATION.md`, amendment 1): every
  burst and c arm gave four notches back in its first five seconds, before its first eviction, because a cold cache evicts
  nothing; the give-back gate is now the miss share under 1% of requests (the MySQL gate), growth is gated on missing the same
  way, and a second with no request moves nothing. Said before the runs: the MongoDB memory rows may fall to the noise, because
  the saving was the artefact. Tests cover every new case; the second (PostgreSQL, MongoDB) and third (MySQL) counted sets
  follow on these rules, the earlier tables kept whole in `docs/history`. Dispatched 23:16 UTC on commit `310cf318`:
  PostgreSQL A2/B2/C2 37858494179, 37858496620, 37858499033; MySQL A3/B3/C3 37858501997, 37858505059, 37858509109; MongoDB
  A2/B2/C2 37858512907, 37858515717, 37858519010.
- **The public-trace test done, A/B/C on v3: a day of demand nobody here wrote reads the same way as our own schedules**
  (`results/live/V3_TRACE_GOOGLE2011.md`, runs 37826513664, 37826518868, 37826522419, commit `13ee69e8`, 30 of 30 pairs
  valid): p95 **−65% to −71%**, p99 −49% to −61%, mean −51% to −55%, time over the line −81% to −84%, failed requests −8% to
  −17%, **machines in service −6% to −10%**, HPA replicas −5% to −6%, standby-model energy −4% to −7%, all toward its aim in all three of our runs;
  pods started +23% to +35% as point estimates, inside the noise in one run; no pod ever without a machine; 9 rows toward their aims, 0
  away from their aims. The Kubernetes category of the index moves to **+28.8%** over seven tests and the headline to **+24.1%**. The
  preregistration carries the result and the comparison with the wandering test; register row 17, proof-program row 4, the
  v3 record, state of play, README, the manual (3.5, 16.1, 16.6, 16.7, 16.8, the executive summary) and the dossier carry it.
- **A public demand trace on the real Kubernetes cluster, preregistered and built** (`docs/TRACES_PREREGISTRATION.md`,
  `tools/trace_schedule.py`, `tests/test_trace_schedule.py`, `results/traces/google2011/`; register row 17, proof-program row 4):
  the first day of the Google cluster-usage trace 2011 (jobs submitted an hour, 18 public parts named with their SHA-256)
  turned into the wandering test's load schedule by a rule written before the runs (min-max onto 1 to 8 generators, one
  step a bin, 24 steps of 108 s), the receipt committed; everything else is the wandering test's. Runs A, B and C on v3
  dispatched at 18:43 UTC on commit `13ee69e8`: 37826513664, 37826518868, 37826522419. The register's queue rows for robot
  arms and drones now read done (they were).
- **MySQL under sysbench, the second counted set A2/B2/C2 on the amended plug: the pool given back on read-mostly working sets,
  bought on a written one, handed back on every arm** (`results/live/V3_SYSBENCH.md`, runs 37770617236, 37770620582,
  37770624805, commit `a033fd09`, Omni v3): the pool held **−67% on burst and −50% to −56% on read_only, toward its aim in all three of our runs**; on
  read_write the pages holding data **+53% to +70%, away from its aim in all three of our runs**; work inside the line, p95, p99 and host CPU inside the
  noise on every workload; no error; **the pool handed back and read back on all 45 omni arms**. 4 rows toward their aims, 1 away from their aims, 0
  disagree; the category enters the index at +12.2% and the headline moves to **+23.5%** over six real categories. The first
  set's table (every row inside the noise, 15 arms not handed back) is kept whole in `docs/history/V3_SYSBENCH_set1.md`; the
  preregistration carries both sets. Register row 24, proof-program row 11, the v3 record, state of play, README, the manual
  (3.3, 3.5, 10.9, 16.4, 16.6, the executive summary, the evidence map) and the dossier carry the result.
- **The fleet's seventh dispatch ran no arm; an inventory workflow for the subscription** (`docs/K8S_COMPASS_PREREGISTRATION.md`
  amendment 8; `.github/workflows/azure-inventory.yml`): repetitions 1 to 3 refused by Azure's cluster capacity in eastus as
  before (32 refusals across seven dispatches); repetitions 4 and 5 stopped at the pre-flight, which found only 2 of 10 vCPUs
  free in two machine families. The new workflow lists, read-only, every resource group, AKS cluster, machine and scale set
  and one region's per-family vCPU usage, and deletes only groups named in full that begin with our own runs' prefixes. Its
  first run (37773586107) found exactly our four machines and nothing left behind: the holders are two of the 24-hour
  robustness machines, rented as eight-core sizes in those families; the eighth dispatch follows their collect.
- **MySQL under sysbench, the first counted set A/B/C on v3, every row inside the noise, and a hand-back finding**
  (`results/live/V3_SYSBENCH.md`, runs 37757840760, 37757850988, 37757861572, commit `23f6ca4c`; `docs/MYSQL_PREREGISTRATION.md`,
  register row 24, proof-program row 11, the v3 record): on the four untouched workloads no gauge-row is lower or higher in all three of our runs and none disagrees; no error; the pool moved 3 to 26 times an arm. **15 of 45 omni arms did not read the operator's
  512 MB back at the end**: the audits show the server still withdrawing the blocks of a shrink the law had asked for when the
  restore was issued (InnoDB finishes a shrink only when the load releases the pinned pages), and MySQL ignores a new size
  while a resize is in progress. The plug's restore, not the law: `BufferPool.restore` now waits for the resize in flight,
  writes the snapshot and writes once more if the server ignored it, with a receipt in every omni arm's record; the table
  (`tools/sysbench_abc.py`) counts the arms not handed back and those mid-resize; `tests/test_run_sysbench.py` proves the three
  cases. Declared as an amendment; the first set's rows stand; the second counted set runs on the amended plug. The index now
  spans six real categories at **+21.2%** (MySQL at +0.0%); README, the state of play, the manual (3.3, 3.5, 10.9, 16.4, 16.6,
  the executive summary, the evidence map) and the dossier carry it. The update_index "inside the line" row is disclosed as
  counting almost nothing in either arm (a single update's client round trip exceeds the server-side 0.6 ms line). The second
  counted set dispatched on the amended plug at 11:31 UTC, commit `a033fd09`: runs 37770617236, 37770620582, 37770624805.
- **The 24-hour robustness run dispatched on three rented machines** (`docs/ROBUSTNESS_PREREGISTRATION.md` scenario 2b, the
  dispatch record): runs 37761059781, 37761072412 and 37761084779 of `big-organism-detached` with `test=robust`, 86,400 s an
  arm, one pair a machine, commit `4d5633dd` (v3), eastus, all three rented at the first attempt and running by 10:20 UTC;
  collected and deleted at 60 hours at the latest. Corrected from the subscription's inventory the same day: the start job
  rented eight-core machines of three families (`Standard_D8as_v7`, `Standard_D8s_v7`, `Standard_D8s_v4`), not the four-core
  size the scenario named; about $55 to $70 for the three, the rules unchanged, the correction in the scenario's record. The index tool carries the MySQL table's entry
  ahead of the result (silent until the sysbench table exists in `results/live/`).
- **The manual, twelve thin sections expanded** (1.4 nothing hardwired, 1.5 the word, 2.3 the organism receipt, 2.4 the two
  axes of the grid, 2.5 the clock rule and the 1,000-copies result, 2.6 reading a register row, 3.1 why the room is there,
  3.3 both readings on real software, 4.3 one decision followed through, 6.3 the memory gates on MongoDB and MySQL, 7.2 the
  snapshot and the read-back, 7.3 the API errors held in the long run, 7.4 memory and decision time over time, 9.2 what the
  verifier checks, 10.4 the robust mode of the detached workflow, 16.3 the fleet's refusals); PDF rebuilt, 472 pages.
- **The four stacked at 1,000 copies with the real cluster inside, on v3, 3 of 3 on the clock** (`results/live/V3_BIG_ORGANISM.md`;
  started by run 37564821425, collected by run 37754612102; one rented Azure machine, eastus `Standard_D8as_v4`, a 10,800 s
  window of 240 steps of 45 s, three paired repetitions over 29 hours, commit `126b8941`, Omni v3): the cluster's p95 2,882
  → 150 ms, p99 5,405 → 165 ms, time over the line 51% → 0, failed requests 0.14% → 0, all clear of zero; replicas, pods and
  machines the same; energy inside the noise; the organism's model energy −0.4% and work rounding-level lower, shown; both
  arms 22 s behind the window (0.2%). The machine was deleted by the collect. The whole tower at 1,000 copies started the same
  way (run 37756284680). The v3 record, register row 8, state of play, README and the manual's section 16.2 carry it.
- **MySQL under sysbench, preregistered, built and smoke-tested four times** (`docs/MYSQL_PREREGISTRATION.md`,
  `tools/run_sysbench.py`, `tools/sysbench_abc.py`, workflow `sysbench`, tests in `tests/test_run_sysbench.py` and
  `tests/test_sysbench_abc.py`; register row 24, proof-program row 11): MySQL 8.0 and sysbench from Ubuntu's own packages,
  the operator's 512 MB InnoDB buffer pool as native, Omni on the pool size in the server's own 128 MB chunks through its
  console, reading the server's own statement latency from the performance schema. The four smoke runs on the tuning
  workload, all recorded: sysbench's shipped request draw never reached the pool (made uniform), the 1 ms line kept every
  reading under the center (set at 0.5 ms, then 0.6 ms), and the "no page read from disk" give-back gate was never satisfied
  because InnoDB keeps stale pages resident (now the pool's miss share under one percent); on the fourth smoke the pool
  followed the working set both ways. The counted runs A, B and C follow. The manual carries section 10.9 and the stack's
  settings row; the integration manual its row.
- **Robustness, the long run, three runs** (`results/live/V3_ROBUST_LONG.md`, runs 37716886448, 37716900258, 37716913526,
  3 pairs × 7,200 s an arm each, Omni v3; `docs/ROBUSTNESS_PREREGISTRATION.md` scenario 2): the governor's memory at most
  1.07 of its first ten minutes after two hours (no leak), 97.5% or more of the expected decisions in every repetition
  (valid), 2 to 3 failed decisions a run where the cluster's API answered 500 on the HPA read (held and resumed; shown with
  the reason, as preregistered), the decision time's last hour at most 1.20 of its first (no slowing), every setting handed
  back at the end; machines and energy inside the noise, service toward its aim in all three of our runs in one run and inside the noise in two.
  The reader (`tools/live_reps.py` `robust_decisions`, `tools/confirm_abc.py`) gained the long run's preregistered rows,
  with fixed cases in `tests/test_robust.py`; each run's live report in the archive was rebuilt from the untouched raw
  files and its checksum list updated for those two derived files.
- **MongoDB under YCSB on v3, the same in all three of our runs** (`results/live/V3_YCSB.md`, runs 37727968670, 37727976107,
  37727983746, all at `7ee471b4` on Omni v3; `docs/YCSB_PREREGISTRATION.md`, register row 24, proof-program row 11):
  the operator's 512 MB WiredTiger cache as native, the compass on the cache size inside [256, 2,048] MB through the
  server's own console as omni. On the four untouched workloads the cache held fell about half on c and burst and 13% to
  37% on f, toward its aim in all three of our runs (b inside the noise in one run); work inside the 1 ms line, p95, p99 and host CPU inside the
  noise on all four; no failed operation; the burst mean latency +2% to +4%, away from its aim in all three of our runs, the one loss; every cache
  handed back. 6 rows toward their aims, 1 away from their aims, 0 disagree. Four smoke runs preceded the counted runs and are all in the
  preregistration: two harness faults, YCSB's zipfian draw that never reached the cache, hashed run keys over an ordered
  load, and the line set at 1 ms from 2 ms on the tuning workload's own figures. **The Omni index now spans five real
  categories: +25.9%** (`results/OMNI_INDEX.md`; the MongoDB category +10.2%); `tools/omni_index.py` and `tools/dossier.py`
  carry the table (dossier section 3d).
- **The fleet's sixth dispatch** (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendments 5 and 6): eastus refused the fifth
  dispatch's first repetition (the 23rd refusal), the run was cancelled to weigh a second region, the 6 October survey shows
  no other region can take a 40-worker fleet on this subscription, and the fleet was dispatched a sixth time in eastus
  unchanged; its first repetition was refused too (the 24th); the run continues.
- **The manual, expanded to referee and underwriter level** (`docs/OMNI_COMPASS_MANUAL.md`, the PDF rebuilt): the
  standards every page keeps, the executive summary as prose with what is and is not shown, the governor's on-top
  principle, the verdict, the pedals, the modes and the two switches, the catalog, the realms, the organisms and the
  grid, the arithmetic with worked examples, every result with the question a referee will ask beside it, the engine's
  equations in words and where the engine sits against the compass law, the closed circle in plain words and what it does
  and does not certify, the compass's settings on every stack in one table, the direction rules, the do-no-harm gates,
  the profiles and the pedals, the nervous system's authority and release gate, the plug contract line by line, the
  levels, the wiring of a message broker, a cache and a drone swarm (sections 10.5 to 10.7), the three ways a governor
  stops and what each leaves behind, least privilege and the supply chain, the method of paired runs, the evidence
  classes with examples and how to read a row, why three runs and why geometric means, a narrative of every result family
  with its losses (16.1 to 16.6), threats to validity stated by us (16.7), what is not yet shown and the open program
  (16.8), a fuller glossary, file map, troubleshooting and the audit trail from any row to its raw files. The
  integration manual and the wiring guide carry the three new stacks.
- **Robustness, preregistered and built** (`docs/ROBUSTNESS_PREREGISTRATION.md`, register row 31): the governor killed
  outright at 40% of a governed window (SIGKILL) with the watchdog beside it, the seconds until every setting is back at
  the operator's polled by the harness (`scripts/kind_robust.sh`, `ROBUST=kill` in `scripts/kind_bench.sh`), a second
  governor to the end, the 120 s after the kill compared in both arms; the long run (eight windows) with the governor's
  memory sampled from the process table; the governor's own CPU at 1 to 1,000 copies from the audits already archived
  (`tools/own_cost.py`, `results/live/V3_OWN_COST.md`: 0.006 to 0.013 of one core at every size). `tools/live_reps.py`
  gains the robustness rows and `tools/confirm_abc.py` the three-run rows for them; `tests/test_robust.py` in
  `verify.py`. No engine file changes: `omni_controller/`, `omnicompass/` and `realms/` are the v3 bytes.
- **Robustness, the kill scenario, the same in all three of our runs** (`results/live/V3_ROBUST_KILL.md`, runs 37716845219,
  37716859133, 37716872788, all omni-v3 at `bd389c409ad9`, 10 pairs each): the governor killed with SIGKILL at 40% of the
  window in every repetition; the watchdog's hand-back put every setting back at the operator's 7 to 11 s later in 30 of
  30 (mean 9 s; allowance 60 s); a second governor started and governed to the end in every one; the 120 s after the kill
  read no difference beyond the noise against native in all three runs; the whole window, a kill and a restart inside it,
  read mean response −32% to −39%, p95 −42% to −45%, time over the line −28% to −34% and failed requests −9% to −15%,
  toward its aim in all three of our runs; machines and energy inside the noise. The register, the proof program, the engine page, the state of
  play and the manual (3.5, 16.4b, 16.8, the results table) carry it; the long run (3 pairs × 3 runs) is running.
- **YCSB on MongoDB, preregistered and built** (`docs/YCSB_PREREGISTRATION.md`, `tools/run_ycsb.py`, `tools/ycsb_abc.py`,
  workflow `ycsb`, tests in `verify.py`; register row 24): MongoDB 8.0 from its publisher's signed repository with the
  operator's 512 MB WiredTiger cache as native; Omni on the cache size inside [256, 2,048] MB through the server's own
  console, reading the server's own mean read latency, growing only while the cache is full, giving a notch back when calm
  and nothing is evicted; YCSB 0.17.0 (pinned by SHA-256) running its published core workloads with the key space stepping
  through the cache and past it; the disclosed limit that the data also sits in the OS page cache on this machine. The
  smoke run first, then A, B and C.
- **Robustness smoke run passed** (run 37713124793, one repetition, 600 s, not counted): the governor killed at 240 s,
  every setting back at the operator's 7 s later by the watchdog's hand-back, a second governor to the end, the reset
  check passed. One harness fault fixed before the counted runs: the memory sampler's process-id join (every sample read
  zero); the memory ratio now needs a window over twenty minutes. The kill (10 pairs × 3 runs) and long (3 pairs × 3
  runs) scenarios dispatched on v3.
- **The manual, further expanded**: the governor's audit read end to end, what an upgrade is and is not, why each
  requirement of a stack is there, the four realms in prose, what the Azure, database and simulator runs taught us, the
  twins and the three fingerprints, Appendix D as a table of every gauge with its source and class, Appendix G
  (reproducing everything from a clean machine); the theory chapters carry what the grid has shown, the receipt's
  arithmetic and the one number, and what closing the loop has shown since; the results reader carries the workload,
  swarm, own-cost and robustness tables.
- **Redis on v3, the same in all three of our runs** (`results/live/V3_REDIS.md`, runs 37704450300, 37704464642, 37704479534, all
  omni-v3 at `467f73eba7a6`): on all three untouched workloads (small, large, burst) work inside the 2 ms line +14% to
  +27%, the hit rate +14% to +27% and the mean latency −30% to −61%, toward its aim in all three of our runs; no failed request; the memory
  ceiling held 64 → 200 to 270 MB and the memory used away from its aim in all three of our runs (the resource the gain costs); host CPU-seconds
  inside the noise on all three; keys evicted −76% to −92% (shown); every ceiling handed back; 12 gauge-rows toward their aims, 6
  away from their aims, 0 where the runs disagree. **The Omni index with the cache in: +30.2%** (Kubernetes +25.5%, the database +14.2%,
  Kafka +166.9%, Redis −24.9%): the cache's category reads negative because the memory it holds for a wide working set is
  the resource it trades, and reads away from its aim by rule, while its work and hit rate read toward its aim; every category weighs the same.
- **Kafka on v3, the same in all three of our runs** (`results/live/V3_KAFKA.md`, runs 37697222651, 37697239400, 37697255445, all
  omni-v3 at `a0b5d2381e9e`): on all three untouched workloads (light, heavy, burst) work inside the 500 ms line +16% to
  +21%, end-to-end p95 1.6 s → 9 to 14 ms, mean lag −92% to −97%, toward its aim in all three of our runs; no message lost in any arm;
  consumers held 2 → 5.8 to 7.9 away from its aim in all three of our runs (the resource the gain costs); host CPU-seconds away from its aim in all three of our runs on light
  (+10% to +20%), inside the noise on heavy and burst; CPU per 1,000 messages inside the line lower on burst; every count
  handed back; 21 gauge-rows toward their aims, 8 away from their aims, 0 where the runs disagree. The tuning workload is shown and not counted.
- **The Omni index reads every workload table the same way** (`tools/omni_index.py`): the database, messaging and cache
  tables (`V3_PGBENCH.json`, `V3_KAFKA.json`, `V3_REDIS.json` when it lands) enter through one list, each a real category
  weighed the same, tuning workloads excluded. With Kafka in, the headline is **+56.4%** (Kubernetes +25.5%, the database
  +14.2%, Kafka +166.9%). The index page says why the messaging speed ratio is large: native sat at nine tenths of its
  measured capacity by design, so its queue grew and Omni's did not. README, the state of play, the manual, the engine
  page, the register and the proof program carry the result.

## 2026-10-07
- **Redis, preregistered and built** (`docs/REDIS_PREREGISTRATION.md`, `tools/run_redis.py`, `tools/redis_abc.py`, workflow
  `redis`, tests in `verify.py`): Redis as shipped with the operator's 64 MB ceiling and allkeys-lru as native; an
  application with a declared 5 ms store trip on a miss and a working set that steps 1 2 3 2 3 4 5 6 …; Omni on the
  ceiling inside [16, 512] MB through Redis's own console, growing only while the cache is full (a cold miss is not the
  ceiling's), giving back a notch a second when calm and nothing is evicted. The tuning workload on one machine (not
  counted): hit rate 66% → 81%, work inside the line +22%, the ceiling held 64 → 304 MB (the cost). Three untouched
  workloads run as A, B and C on v3. The two smoke runs that shaped the rule are described in the preregistration.
- **Azure**: the standard-tier fleet run was refused on all five repetitions too (seventeen refusals in seven hours, all
  Azure's eastus capacity for new clusters); dispatched again.
- **Kafka, preregistered and built** (`docs/KAFKA_PREREGISTRATION.md`, `tools/run_kafka.py`, `tools/kafka_abc.py`, workflow
  `kafka`, tests in `verify.py`): Apache Kafka 3.9.1 as shipped on the runner, a producer at a stepped rate, the consumer
  group at the operator's count as native; Omni on the consumer count inside [1, 8], holding the group's own end-to-end
  latency at 40% of a 500 ms line; the host's CPU seconds as the cost. The tuning workload on one machine (not counted):
  p95 429 → 12 ms, lag 329 → 45, consumers held 2 → 5.8. Three untouched workloads run as A, B and C on v3.
- **Drone swarms on v3, the same in all three of our runs** (`results/live/V3_SWARM.md`, runs 37677964512, 37677984739, 37678005151): in
  all three untouched 20-drone cells energy a mission −7% (short), −18% (mixed), −20% (long) and missions a charge +8%,
  +22%, +25%, toward its aim in all three of our runs; no late mission, reserve breach, near miss or collision in any arm of any run; 9 gauge-rows toward
  their aims, 0 away from their aims. PyBullet reproduced to a part in a thousand across GitHub's machines, not to the bit, so the table's
  reproduction tolerance is one part in a thousand (preregistration amendment 1, made after the runs were seen and said so).
- **Azure fleet on the standard control-plane tier** (amendment 4; `tier` input of `aks-metered`, `AKS_TIER` in
  `scripts/aks_paired.sh`): the free tier was refused by Azure's capacity in eastus on ten repetitions over four hours; the
  control plane's tier is not in the bill. The drone swarm runs A, B and C finished (37677964512, 37677984739, 37678005151)
  and are requested for archive.
- **Drone swarms, the first item of the queue, built and preregistered** (`docs/SWARM_PREREGISTRATION.md`, `tools/run_swarm.py`,
  `tools/swarm_abc.py`, workflow `swarm`, tests in `verify.py`): gym-pybullet-drones (University of Toronto, MIT) flies
  Crazyflie 2.x quadrotors with its shipped position controller as native; Omni sits on top on one knob, the cruise
  override inside the autopilot's limits, spending tracking slack as speed; a declared energy model, the autopilot's
  battery reserve, collisions void the cell. The tuning swarm (5 drones, not counted): energy a mission −16%, missions a
  charge 5.8 → 6.9, no late mission, no collision. Three untouched 20-drone cells run as A, B and C on v3.
- **Azure fleet run refused five times by Azure's own cluster capacity in eastus** (run 37651333302, "creating a new cluster is
  unavailable at this time"); dispatched again.
- **The referee dossier rebuilt from the v3 tables** (`tools/dossier.py`, `docs/DOSSIER.md`): real Kubernetes three times
  (one chart, every run's interval), the real database, the bill on a real cloud, the grid at 84 of 90 cells, the 945
  muscles and the three simulators, the harnesses, and what is not yet shown; the obsolete card charts removed.
- **The state of play rewritten for v3** (`docs/STATE_OF_PLAY.md`): current facts only, the six Kubernetes tests, the
  database, Azure, the simulated results, the card and the open items; the 2026-10-06 page moved whole to `docs/HISTORY.md`.
- **The v3 grid at 100 copies** (`results/scale/receipts/v3-100x.md`, run 37501765605, 170 shards pooled from the archive with
  the run's own command): every organism superior within guardrails at 10, 100 and 1,000 runs, work per energy +0.07%
  to +0.36%. **The grid is complete at 84 of 90 cells** (`results/scale/GRID.md`); the six left are beyond the machines
  available, as declared. The same figure at every size from 1 to 1,000 copies.
- **The v3 grid at 1,000 copies** (`results/scale/receipts/v3-1000x.md`, run 37578946088, 60 shards, 10 paired runs per
  organism; `results/scale/GRID.md` now 60 of 90 cells): every organism superior within guardrails at 10 runs, work per
  energy +0.07% (Physics) to +0.37% (Energy, the four stacked, the tower), work unchanged, every knob handed back. The
  100-copy run's shards are all done; its pooling job did not start, so the receipt is pooled from the archived shards.
- **Azure fleet at 40 workers** (amendment 3): the pre-flight found `Standard_D2s_v3` not offered in eastus and stopped the
  45-worker run before anything was built or billed; the pool is dropped and v3 steady runs on the nine remaining
  families (run 37651333302). **The v3 grid at 1,000 copies finished** (run 37578946088, 61 shards) and is requested for
  archive; the receipt and the grid table follow.
- **Azure fleet rebuilt from the families the subscription allows** (preregistration amendment 2): the DAv4, ESv4 and
  EAv4 families have no allowance at all (the "remaining 0" refusals), so three of the eight pools could never be built.
  Ten allowed families give 45 workers; list prices from Azure's own price API; `scripts/aks_paired.sh` pre-flights
  every pool's size and family allowance before anything is built or billed.
- **All six Kubernetes tests the same in all three of our runs on v3** (`results/live/V3_WANDERING.md`, `V3_ALL_FOUR.md` join the four already in):
  wandering p95 −57% to −63% and failed requests −9% to −12%; all four work inside the line +35% to +49%, p95 −61% to
  −66%, failed requests −11% to −14%; all toward its aim in all three of our runs; machines and energy inside the noise in both. The same
  readings as v1. **The Omni index now reads from the v3 tables** (`tools/omni_index.py`, `results/OMNI_INDEX.md`): +19.7%,
  real Kubernetes +25.5% (work +19%, speed +93%, machines +4%, energy +3%), the database +14.2%; the README's result
  table is the v3 run A. The v1 tables stay as the first engine's record in `docs/OMNI_V1.md`.
- **Power grid on v3, the same in all three of our runs** (`results/live/V3_PANDAPOWER.md`, runs 37568375564, 37568393269, 37568411160):
  the same table as v1 to the digit, as a deterministic simulator under the same runner bytes must give: 67 gauge-rows toward
  their aims, 14 away from their aims (losses in the four grids with their own generation; tap operations 4 → 8 a year in one rural grid),
  0 where the runs differ. Run C of the wandering and all-four tests finished and requested for archive.
- **Kubernetes batch queue on v3, the same in all three of our runs** (`results/live/V3_BATCH.md`): machines −19% to −23%, machines
  after the queue −29% to −35%, standby-model energy −13% to −16%, mean response −10% to −14%, all toward its aim in all three of our runs; the
  queue finished no difference beyond the noise in all three runs. Four of the six v3 Kubernetes tests are now in.
- **Azure fleet runs refused twice**: the 39-worker run (DASv4 held by the detached machine) and the 35-worker run (DAv4
  "remaining 0" on three repetitions over 45 minutes, something in the subscription holding that family); both cancelled
  before any arm ran; the survey mode now lists the families in use and every resource group and cluster still standing,
  so the holder can be found before the next dispatch.
- **Azure burst v1, five pairs** (`results/live/V1_AKS_BURST.md`, run 37534538088 attempt 2): the bill +5.0% with its
  interval across zero; machines, p95 and failed requests inside the noise; p99 −34% (6.0 s → 4.0 s) clear of the noise
  in this one run. Replaces the four-pair table. Power-grid v3 runs 1 and 2 archived; run C of the batch test on v3
  finished (37581021752) and requested for archive.
- **Azure fleet, 35 workers while the detached machine runs**: the 39-worker steady run was refused on every repetition
  (the DASv4 family had 2 vCPUs left: the rented Standard_D8as_v4 running the v3 stack holds 8 of its 10), cancelled
  before any arm ran, and dispatched again at 35 workers with the steps scaled as preregistered (amendment in
  `docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine).
- **Kubernetes on v3, three of six tests the same in all three of our runs** (`results/live/V3_STEADY.md`, `V3_FAIRNESS.md`,
  `V3_FAULTS.md`; every run omni-v3): steady p95 −65% to −66%, machines −1.5% to −2.9%, standby-model energy −1.3% to
  −2.1%, all toward its aim in all three of our runs; fairness no difference beyond the noise on every row; faults p95 −47% to −62% and time
  over the line −22% to −42% toward its aim in all three of our runs, machines and energy inside the noise. The same readings as v1. Register
  rows 1, 4 and 5; the other three tests land as their B and C runs finish.
- **Azure burst v1, the four-pair copy withdrawn**: repetition 4's rerun finished (run 37534538088, attempt 2, 5 of 5),
  so the raw copy of the first attempt is removed and the whole run is archived in its place; the table is remade with
  five pairs when the copy lands.
- **The manual brought up to everything built since v1** (`docs/OMNI_COMPASS_MANUAL.md`, PDF rebuilt): section 10 now
  wires Azure's managed Kubernetes with the bill as the gauge and the fleet sized to the lever, a database behind its
  pooler, the three independent simulators and the big organisms on a rented machine; section 13 adds preregistration,
  the clock rule, every-row reporting and the raw-file archive; a new section 15 explains the frozen engines v1, v2 and
  v3, the version tool, the three-run rule and the Omni index; section 16 (results) is rewritten from the v1 and v3
  tables, losses beside gains, the earlier card results marked obsolete and the queue named; the glossary, command
  reference, file map and evidence map follow. `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md` and
  `docs/HOW_TO_READ_THE_RESULTS.md` carry the same additions; the register's heading reads 945 muscles in 59 families.
- **The archive bot copies finished runs only** (`.github/workflows/archive-run.yml`): it had copied the first 108 jobs of
  the v3 grid at 100 copies (run 37501765605) while the run was still going, and would never have looked again. That
  part-copy is removed; the run is re-requested when it ends. The grid at 1,000 copies is queued behind it (run
  37578946088). Run C of the Kubernetes batch test on v3 dispatched (37581021752); run B (37573759437) archived.
- **A fleet of several machine families on Azure** (`scripts/aks_paired.sh` `AKS_WORKER_POOLS`, `scripts/kind_bench.sh`
  worker selector `omni-role=work` and per-pool machine counts in the bill file, `tools/live_reps.py` the bill at each
  pool's own list price, `aks-metered` inputs `worker_pools` and `pool_prices`): the subscription allows 200 vCPUs in
  eastus but 10 a family, so one family gives 5 machines; eight families give 39 workers. Preregistered in
  `docs/K8S_COMPASS_PREREGISTRATION.md` (the fleet that can show one machine), replacing the one-family 11- and 15-worker
  plan the allowance refused. Register rows 12c and 12d.
- **The v1 stack at 1,000 copies, 3 of 3** (`results/live/V1_BIG_ORGANISM.md`, collection run 37575930111 from the detached
  machine): p95 −74%, p99 −83%, clear of the noise; machines 6 in both arms; organism energy −0.2%; organism work
  rounding-level lower; the compass arm ended up to 615 s after the 2,880 s window in all three repetitions (marked OFF
  THE CLOCK; native kept the clock). The tower and the stack now make one report from both archived runs.
- **"Nothing here is set in stone" removed** from the notice (`tools/legal.py`), the standing orders and every tracked
  file outside the archived raw records (which stay byte-exact under their checksums), on the founder's order. The manual
  PDF carries the old notice until its rebuild.
- **Aerospace and propulsion in the queue** (`docs/REGISTER.md` rows 32 to 37, `docs/PROOF_PROGRAM.md`): Basilisk attitude,
  momentum and thrusters; Orekit and GMAT station-keeping; Basilisk constellations; RocketPy and OpenRocket; Cantera
  combustion. Pure physics solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) are named as not benchmarkable: no controller,
  no knob; their value is the HPC cluster that runs them.
- **CityLearn on v3, A/B/C** (`results/live/V3_CITYLEARN.md`, runs 37568381751, 37568399439, 37568416917): the same pattern
  as v1: electricity bought, daily peak and daily unevenness lower in all 11 battery districts, carbon in 8; the bill higher in 7 and ramping higher in 7 (the 2023 districts), reported as such; 71 score-rows toward their aims, 33 away from their aims, 1 where the runs
  differ. `tools/six_kube_report.py` now reads several archived runs and writes to a named file, so the big organisms'
  tower (job-bound run) and stack (collected from the detached machine) make one report.
- **The proof program** (`docs/PROOF_PROGRAM.md`): the program of record on the founder's order: every benchmark at the
  largest size each platform allows, on open native engines, with the rules, sizes, order, costs, the defensibility
  package and the disclosures.
- **Azure burst on v1** (`results/live/V1_AKS_BURST.md`, run 37534538088, 4 pairs; repetition 4 lost its native cluster to
  an Azure API error and is run again): no difference beyond the noise on any gauge on the 4-worker fleet; Omni's own CPU
  0.009 cores. The 11-worker start was refused by the machine family's 10-vCPU allowance; the regional total was raised to
  200 but every family's request was refused through the API (QuotaNotAvailableForResource, ContactSupport): the
  subscription's terms. Next: a fleet of several machine families (4 to 5 workers each under the one allowance), or the
  owner's request in the portal.
- **Robot arms on v3, A/B/C** (`results/live/V3_MUJOCO.md`, runs 37568387334, 37568405026, 37568422829): the same
  readings as v1, as the runner is the same bytes: Gen3 7 gauges toward its aim in all three of our runs, 0 away from their aims; UR5e and iiwa 14 nothing to
  move. The four A/B/C table tools (`confirm_abc`, `mujoco_abc`, `pandapower_abc`, `citylearn_abc`) now name in their
  title the engine the three runs carry instead of a fixed "Omni v1".
- **The v3 repeats dispatched** (03:48 UTC): power grid ×3, CityLearn ×3, robots ×3, the six Kubernetes tests (run A;
  B and C follow each A). They should have been queued when v3 was declared; they were not.
- **The register's queue, audited against every family and what a referee or buyer expects** (`docs/REGISTER.md` §4, rows
  23 to 31): drone swarms, aircraft and defense edge (PX4, ArduPilot, Crazyswarm, JSBSim, K3s), databases and caches at
  large (YCSB, HammerDB), big data (Spark TPC-DS), messaging (Kafka), caches (Redis), search (OpenSearch), storage (fio),
  warehouse robots (Open-RMF), and a robustness row (a 24-hour run, Omni killed mid-run, Omni's own cost at every size).
  None changes a result that stands; each gets its own preregistration, A, B and C, every row shown.
- **Azure with a fleet that can show one machine** (`docs/K8S_COMPASS_PREREGISTRATION.md`, written before the run;
  `.github/workflows/aks-metered.yml` inputs `max_workers` and `hpa_max`; `scripts/kind_bench.sh` raises the app's
  replica ceiling with the fleet and expects it back untouched): the 4-worker runs could not show anything under a
  quarter of the fleet, and the 10-pod ceiling kept the autoscaler at about 1.9 workers in both arms. Now 11 workers
  (15 once the stack machine frees its 8 vCPUs), ceiling 9 pods a worker, load steps scaled with the fleet, 5 pairs,
  v3 first. Register rows 12c and 12d.
- **The organism must keep the window's clock** (`tools/six_kube_report.py`, `docs/K8S_COMPASS_PREREGISTRATION.md`): the
  report now shows "organism behind its window (s)" (shown, not judged) and marks a repetition OFF THE CLOCK when either
  arm ended more than 5% of the window late, its last steps having seen a cluster whose load schedule had ended. Found
  while watching the v3 stack at 1,000 copies on Azure: 1.7 million muscles step in 31 s against a 12 s step, 4,628 s
  behind after the native arm. Marked in the published reports: v1 six-kube at 1,000 copies, the Physics realm (2 of 3,
  up to 290 s) and the tower (2 of 3, up to 3,820 s) on GitHub's 4-core runners; v3 six-kube, the stack at 100 copies
  (4 of 5, up to 277 s); v1 big organism, the tower's repetition 3 (2,392 s). The pairing stands in every case. The
  remedy is a longer window for that size on that machine, never a change to the organism or the law: the v3 stack
  machine was collected as it stood and started again with a 10,800 s window (45 s steps).
- **The v1 big organisms** (`results/live/V1_BIG_ORGANISM.md`, run 37359820055): the tower at 1,000 copies on a rented
  Azure machine, 3 of 3: p95 −95% (4.1 s → 0.2 s), time over the line −99.7%, both clear of the noise; machines 6 in both
  arms; organism energy −0.2%; organism work rounding-level lower. The stack's native arms ran 5,184 s and 5,984 s past
  the window and never finished a pair inside the six-hour job.

## 2026-10-06
- **Six organisms with the real cluster, Omni v3, 10 and 100 copies** (`results/live/V3_SIX_KUBE.md`, run 37501769448 on
  `33b15eb`, 12 cells, 5 pairs each, 62 of 62 jobs): every cell toward its aim on 4 to 6 gauges, away from its aim on none beyond the noise
  except a rounding-level organism-work loss (6 to 11 parts in a million; the rule reads anything past one part in a
  million) in 4 cells. The v1 and v3 copies now carry a Source line naming run, commit and engine.
- **Azure steady on Omni v1, 5 paired repetitions** (`results/live/V1_AKS_STEADY.md`, run 37385657374 on `f162ce8`;
  repetitions 3 to 5 re-run after the regional quota refused them while the big-organism machine was up): no difference
  beyond the noise on any gauge; the bill −4.7% with its interval across zero; Omni's own CPU 0.014 cores. The burst on v1
  follows (branch `omni-v1` at `f162ce8`, since the workflow needs a branch to run an older commit; a tag push was refused).
- **The stack at 1,000 copies, detached from the GitHub job** (`.github/workflows/big-organism-detached.yml`): every
  attempt at the four stacked with the real cluster inside was cut off by GitHub's six-hour job limit (v1 run
  37359820055: the tower 3 of 3 done, the stack 0 of 3). The new workflow rents one Azure machine, starts every repetition
  under nohup and leaves it running; a look every two hours collects the files when all are done (one artifact per cell,
  the same shape as `big-organism`'s) and deletes the machine; a machine older than 40 hours is collected as it stands.
  The commit to run is an input, so the v1 stack runs again on `f162ce8` (named `stack_1226` there) beside the v3 stack.
  Package install on the fresh machine is tried five times (one v1 attempt lost its machine to a stale package list).
  First starts (17:57 UTC, westus2 and centralus): every size refused, the CLI hiding Azure's reason behind its own
  "content already consumed" error; the workflow now reads the reason out of Azure's answer and lists the region's SKU
  restrictions. eastus2 refused every size too. The workflow's survey mode (rents nothing) then asked Azure, region by
  region, which 8-vCPU sizes this subscription may rent: eastus allows 32 vCPUs and the v4 sizes (D8as_v4 is the one
  granted on 2026-10-05); every other region surveyed allows 10 vCPUs and only the v5 to v7 sizes. So the start job
  asks Azure for each refused size's restriction, tries D8as_v4 and D8s_v4 first and falls back to the v7 sizes, and the
  default region is eastus. Both machines were then granted (eastus, D8as_v4, the v3 stack; westus3, D8as_v7, the v1
  stack) and the tests started, but the start step's ssh session hung until the job's hour ran out: the test had been
  put in the background as part of an "a && b &" list, so a shell holding the session waited for it. Fixed; the collect
  look, dispatched by hand, found both machines running.
- **The version tool reads a commit from before a runner was written** (`tools/omni_version.py`, `tests/test_omni_version.py`):
  the power-grid runner was added at `8eab01c` inside v1 without touching any other engine file, so the Kubernetes and
  organism runs at `a004a8f` (six-kube 37359815637, big-organism 37359820055) hold 37 of the 38 v1 files, all v1 bytes.
  The tool used to print only what differed from the newest version there; it now prints "omni-v1 (37 of 38 files, all v1
  bytes; not yet in this commit: tools/run_pandapower.py)", and `docs/OMNI_V1.md` says the same. A changed byte or an
  extra engine file is still no version. `tools/code_book.py` reads the version through the same functions.
- **The real database joins the Omni index** (`tools/omni_index.py`, `results/OMNI_INDEX.md`): per workload, work inside
  the line, p95, the connections held open (machines) and the host's CPU seconds (energy: the compass's own cost, away from its aim in all three of our runs, counted against Omni). Headline +20.1% over the two real categories in (Kubernetes +26.2%, the database +14.2%).
- **Omni v2** (`OMNI_V2.json`, `docs/OMNI_V2.md`; the founder's order: make v2, add every missing muscle family, don't be
  cheap). The law, the controllers and the runners are v1's byte for byte. The catalog (`realms/catalog.csv`, built by
  `tools/realms_catalog_v2.py` from `realms/catalog_v1.csv`, `docs/realm_study/TRUE_MUSCLES.csv` and the new
  `realms/wave4_families.csv` by the v1 rules) grows from 656 muscles in 46 families to 945 in 59: the 656 of v1 byte for
  byte, 118 real controls the realm study had found and the tower lacked, and 171 muscles in thirteen new families with
  one new preset each (`realms/presets.py`): hospitals' critical rooms, clinical systems, farms and irrigation, oil and
  gas pipelines, rail traction, marine propulsion, ports, mining, district heating and cooling, power generation,
  renewables and inverters, elevators, pharmaceutical and food plants. Every added muscle names its real system, its
  setting and its source. The organisms: Compute 430, Physics 376, Energy 470, Distribution 440, the stack 1,716, the
  tower 945, the spine 257. The two whole-tower organisms are named `tower` and `stack` in code and workflows (nothing is
  named by a count); `organism_656` and `stack_1226` are read as aliases, so every v1 record still reads. Every added
  muscle was run through the harness before the freeze (deterministic, watch equals native, every knob handed back, Omni
  never more often outside its band than native); two presets were adjusted on that check and the adjustment is written
  into `docs/REALMS_PREREGISTRATION.md`. `tools/omni_version.py` now prints omni-v2, omni-v1, or what differs; the
  three-run tables accept either fingerprint and refuse to mix them. Every modelled result is to be run again on v2;
  v1's tables stay v1's.
- **PostgreSQL, the counted runs on amendment 1** (`results/live/V3_PGBENCH.md`; runs 37435740735, 37435751322, 37435761371,
  three paired repetitions each, the three untouched workloads): the connections held open to the database (the machines)
  toward its aim in all three of our runs on `select` (−61% to −63%) and `tpcb_hot` (−69% to −72%); on `simple_update` the runs disagree (one
  run +12%, two runs −34% and −35%). Host CPU-seconds **away from its aim in all three of our runs** on all three workloads (+14% to +28%): a smaller
  pool makes PgBouncer queue clients, and queuing costs the host CPU. Work inside the line, throughput and every latency
  gauge read no difference beyond the noise: native's own p95 swings a hundredfold between repetitions on GitHub's shared
  runner. Failed transactions 0 in both arms; the knob handed back in every arm. The honest reading for a database behind
  a pooler: Omni holds a third of the connections for the same work, at a CPU cost, and the shared runner is too noisy
  to tell the latencies apart. Register row 30; the Omni index reads the table.
- The six organisms with the real cluster inside, v1 (`results/live/V1_SIX_KUBE.md`, run 37359815637): 98 of 100 cells
  (1, 10, 100 copies of all six; 1,000 copies of the four realms and the tower; the two 1,000-copy stack cells cut off by
  GitHub's six-hour job limit). p95 and time over the line toward its aim in every cell of every organism; 0 gauges away from their aims
  beyond the noise except a rounding-level work loss (−0.0003%) in the larger cells and HPA replicas +0.7% in one cell;
  the machines stay at 6 in both arms (kind has no node autoscaler). The big organisms on Azure (37359820055): the tower
  at 1,000 copies 3 of 3 done; the stack at 1,000 copies never finished inside a six-hour job and needs a run detached
  from GitHub's job, to build.
- The six-organism grid on v3, 10 copies (`results/scale/receipts/v3-10x.md` from run 37433972731): every organism
  superior within guardrails at 10, 100 and 1,000 runs; 100 copies dispatched.
- The six-organism grid on v3, 1 copy (`results/scale/GRID.md`, receipt `results/scale/receipts/v3-1x.md` from run
  37430723080: 60 shards, 1,000 paired runs per organism): every organism superior within guardrails at 10, 100 and
  1,000 runs, work per energy +0.08% to +0.3%, every knob handed back. The v1 grid and its receipts move to
  `results/scale/v1/`; `tools/grid.py` builds the grid from the current engine's receipts (`v3-<size>x.md`) and marks
  the sizes not yet run as "to run". 10 copies is running; 100 and 1,000 follow one at a time.
- **PostgreSQL: the first untouched run was a loss, and it is kept** (run 37425853293, `docs/POSTGRES_PREREGISTRATION.md`):
  on the read-only workload Omni gave the pool back to its floor of two and the users' p95 went from 4 ms to 3.9 s,
  work inside the line −47%, because the compass read the pooler's own service time (0.1 ms per transaction) and the
  pooler cannot see clients backed up behind their own schedule. On the two write workloads no difference beyond the
  noise on work and latency, half to three quarters fewer connections, 10% to 18% more host CPU. **Amendment 1**,
  declared before the counted runs: the reading is the pooler's service time or the share of its clients queued for a
  server, whichever moved away from its aim (every client waiting is past the wall); and the dwell holds only the brake, adding is never
  held. The three untouched workloads run again three times on the amended rule (A, B, C); the first run is recorded, not
  counted. `tools/pgbench_abc.py` (with `tests/test_pgbench_abc.py` in `verify.py`) builds the three-run table by the
  readings rule.
- The power grid's v1 A/B/C table (`results/live/V1_PANDAPOWER.md`; runs 37377029333, 37397142210, 37412578757 on the
  v1 fingerprint; 11 untouched SimBench grids, a full year each, both load models, every gauge reproduced in 3 of 3):
  with ZIP loads the energy the loads drew is toward its aim in all three of our runs in all 11 grids (−1.3% to −1.5%) and the net import in
  all 11 (−1% to −15%); losses toward its aim in all three of our runs in 7 and away from its aim in all three of our runs in 4 (the rural and semi-urban grids that carry
  their own generation, +0.6% to +1.5%: a lower voltage draws more current for the same power through those feeders);
  tap operations fewer in 10 grids (−27% to −36%) and 4 → 8 a year in one rural grid, the cost declared before the run;
  no grid is ever more often outside its 0.95-1.05 band, two are less often. With constant-power loads the energy
  drawn is the same by construction, the import lower in 7 grids and higher by 0.01% to 0.03% in 4. Register row 28.
- **The v3 realms table** (`results/realms/`; runs 37429141430, 37429151263 and 37429161515 on the v3 fingerprint, A, B
  and C reproduced to the last digit; v2's table moved to `results/realms/v2/`): 945 muscles, 0 away from their aims; 124 superior
  within guardrails, 807 no difference beyond the noise, 9 energy improvement with a service tradeoff (all of them
  v1's), 4 service improvement with an energy tradeoff, 1 not established (hoist_speed_target (elevator_hoist, capacity)). **Every organism superior within
  guardrails**: work per energy Compute +0.1%, Physics +0.1%, Energy +0.3%, Distribution +0.2%, the whole tower +0.3%;
  work unchanged; time over the line not above native's in any organism. Fourteen rows changed label against v2: the
  rail, marine, elevator, EV and robot-joint speed muscles the slack gate now leaves native read no difference beyond
  the noise (two of them had read superior under v2, two of them now read native: that is the price of the gate and it
  is shown).
- **Omni v3** (`OMNI_V3.json`, `docs/OMNI_V3.md`; declared in `docs/REALMS_PREREGISTRATION.md` before any v3 run, the
  founder told first). Two changes against v2, both in the modelled realms: the slack gate on speed knobs
  (`realms/compass_arm.py`, `speed_slack`): a motion axis is offered its speed knob only where it is busy at most half
  the time at full speed (task rate × (move time + dwell) ≤ 0.5, from the plant's own figures), as the robot benchmark's
  paired physics trial leaves a loaded arm native; and the marine propulsion preset, twelve 200 rad speed changes an
  hour instead of four of 600, so a one-hour run holds enough moves to count. On the shipped presets the knob is offered
  on a flight axis (duty 0.34) and a reaction wheel (0.35) and left native on rail traction (0.80), EV traction (0.76),
  robot joints (0.54 at the middle size; a muscle's own size moves it either side), marine propulsion (0.52) and
  elevator hoists (0.52). The law, the controllers, the catalog and the runners are v2's byte for byte.
  `tests/test_compass_arm.py` proves the gate; the realms workflow compares a run with the published table only when
  both carry the same frozen tree. Every modelled result is to be run again on v3; the v2 table stays a v2 result.
- **The v2 realms table** (`results/realms/REALMS.md`, `MUSCLES.csv`, `REALMS.json`; runs 37422832244, 37422840154 and
  37422847697 on the v2 fingerprint, A, B and C reproduced to the last digit; v1's table moved to `results/realms/v1/`):
  945 muscles, 0 away from their aims; 126 superior within guardrails, 793 no difference beyond the noise, 15 energy improvement with a
  service tradeoff (9 were v1's), 7 not established, 4 service improvement with an energy tradeoff. The not-established
  rows are new: three rail traction speed muscles where Omni's slowing adds 1.6 to 2.7 points of lateness on a train
  that runs near its timetable's capacity, two marine propulsion and two elevator speed muscles where the slower cycle
  finishes fewer moves in the hour. The organisms: Compute, Energy and Distribution superior within guardrails;
  Physics and the whole tower energy improvement with a service tradeoff (+0.1% and +0.3% work per energy, time over
  the line up by under 0.01 point), where v1 had every organism superior. By the honesty rule the first suspect is our
  own wiring: the speed knob on a motion axis has no do-no-harm gate in the realm harness (the robot benchmark has one,
  its paired physics trial), so a train or a ship with no slack is slowed anyway. The fix is an engine change and makes
  v3; it is declared in `docs/REALMS_PREREGISTRATION.md` before any v3 run.
- The PostgreSQL tuning run (37420052827, `tpcb`, 3 paired repetitions, not counted): server connections alive 20 to
  9.3 (−53%, lower); work inside the line, throughput and every latency gauge no difference beyond the noise (native's
  own p95 swung from 86 ms to 3.3 s between repetitions on GitHub's shared runner); host CPU-seconds +11% higher, CPU
  per 1,000 transactions inside the line no difference; 0 failed transactions in both arms; the knob handed back every
  time. Recorded in `docs/POSTGRES_PREREGISTRATION.md`; the three untouched workloads run next.
- `OMNI_V2.json` rewritten from the checkout's tracked files (40 files, digest `4fc223939c4fab03`): its first write had
  listed the last commit's tree and missed `realms/catalog_v1.csv` and `realms/wave4_families.csv`, so no commit read as
  v2 although the engine's bytes were v2's throughout; `tools/omni_version.py` now lists every tracked or staged file
  for the checkout, and `verify.py` requires the checkout's engine to carry a declared fingerprint.
- The realms runner's report (`tools/run_realms.py`) names the muscle count from the results it writes (the first three v2
  realms runs, 37420034190, 37420040519 and 37420047009, stopped at the report with an undefined name and are run again);
  the realms workflow compares a run's table with the published one only when both are on the same engine (the same
  muscle count), otherwise it says so and lets the run stand as the first on that engine.
- Databases, preregistered and built (`docs/POSTGRES_PREREGISTRATION.md`, `tools/run_pgbench.py`,
  `.github/workflows/pgbench.yml`, `tests/test_run_pgbench.py` run by `verify.py`): PostgreSQL 16 as the distribution
  ships it behind PgBouncer 1.22 with the pool of 20 server connections it ships with (the DBA's one fixed setting) is
  native; omni is the same with the compass law on the pool size, written through PgBouncer's own console inside [2, 90]
  and handed back at the end. The reading is the service time the pooler itself reports each second (transaction time
  plus the wait for a server), on a band to a 50 ms line; where the time goes decides the direction (waiting for a
  server: more slots, by the force; inside the server: one fewer); calm gives back one idle server a second and never
  one in use; past the wall the knob is handed back to the pooler's own setting at once. pgbench offers the load, 64
  clients, the rate stepping one notch at a time with the peak notch at nine tenths of native's own unlimited capacity,
  found once in native mode before the counted runs. Gauges from pgbench's own log (work inside the line, p95, failed),
  PgBouncer's pools (server connections alive, the machines) and the host's CPU-seconds, measured, no energy claimed.
  The first smoke on a 4-core box (one repetition, not counted): omni 1,400 against 1,312 transactions a second inside
  the line, p95 24.5 against 77.2 ms over the profile, 11 server connections alive against 20; at the lightest notch
  omni's p95 was higher (14.6 against 3.9 ms, inside the line), the declared cost of the take-back at light load.
- The robot runner's test (`tests/test_run_mujoco.py`) compares the result, not the wall-clock bookkeeping: the run's
  elapsed seconds flipped between 0.0 and 0.1 under load and had failed the determinism check once.
- The Omni index's columns now say what the sign means (`tools/omni_index.py`, `results/OMNI_INDEX.md`): "more work
  by", "faster by", "fewer machines by", "less energy by", every column pointing the same way, plus good for
  Omni-Compass; the reading line spells out each one ("fewer machines by +4%" is the same work on 4% fewer
  machine-hours).
- The legal notice every generated report carries (`tools/legal.py`) now says "filed in the USA" and "filed in the USA" with a closing sentence since removed (2026-10-07), as the standing orders had it; the committed reports were brought to the same wording (the archived
  raw run folders were left as the bot wrote them, their checksums intact).
- The robot arms' v1 A/B/C tables (`results/live/V1_MUJOCO.md`: UR5e, iiwa 14, Gen3, runs 37409191253, 37409852642,
  37410015922; `results/live/V1_MUJOCO_PANDA.md`: the tuning robot, runs 37409198316, 37409860065, 37410022940; all on
  the v1 fingerprint, every gauge reproduced to the last digit in all three). A robot on a line is judged on hitting its
  points and lasting, and that is where Omni moved it: where the paired physics trial let Omni move, the arm hit its
  points more accurately with less force on its motors, doing the same job inside the same takt. Peak motor torque
  toward its aim in all three of our runs (Gen3 −29%, Panda −10%), tracking error toward its aim in all three of our runs (−21% on both), the cycle 27% longer and
  inside the takt; the energy per takt also toward its aim in all three of our runs, by a little (Gen3 −0.8%, Panda −0.5%); the Panda's copper
  loss away from its aim in all three of our runs (+14%, the gravity-holding torque paid for longer). The UR5e and the iiwa 14 are left native by
  the trial (slowing would cost on their own figures), so Omni moves nothing there and nothing moves away from its aim.
- The robot arms, preregistered and built (`docs/ROBOTICS_PREREGISTRATION.md`, `tools/run_mujoco.py`,
  `.github/workflows/mujoco.yml`, `tools/mujoco_abc.py`; tests in `verify.py`): MuJoCo integrates each arm, MuJoCo
  Menagerie supplies the robot with the position servos it ships with as native, and Omni sits on top on one knob, the
  speed override, inside the task's takt. The planned speed is set per robot as the fastest its own servo tracks; a
  paired physics trial in native mode, before any counted cycle, leaves the override native where a slower cycle is not
  cheaper (the gravity-holding torque is paid for longer), the do-no-harm gate on the arm's own figures. Energy is a
  declared model from MuJoCo's torques and velocities, with the standing draw charged for the whole takt in both arms.
  The first smoke: the tuning robot and the Kinova move (tracking error and peak torque lower, cycles 25% longer inside
  the takt, motion energy −1.7% and −7%, energy per takt −0.5% and −0.8%); the UR5e and the iiwa are left native by the
  trial. Disclosed: the waypoint offset was capped at 0.6 rad after the first smoke showed the UR5e model's full-turn
  joint ranges turned "25% of the range" into 90-degree swings into the floor. MuJoCo and the Menagerie commit are pinned.
- CityLearn's v1 A/B/C table (`results/live/V1_CITYLEARN.md`, runs 37384954241, 37393198549, 37399402398, all on the v1
  fingerprint): 11 districts with electric batteries, every score reproduced to the last digit in all three runs except
  the comfort score, which CityLearn itself varies between runs (it reads "the runs differ" and is not claimed).
  Electricity bought, daily peak and daily load unevenness toward its aim in all three of our runs in all 11 districts; carbon lower in 8, same
  in 3; the bill toward its aim in all three of our runs in 1 district and away from its aim in all three of our runs in 7 (the 2023 challenge districts, +0.2% to
  +0.35%); ramping toward its aim in all three of our runs in 4 and away from its aim in 7 (the 2023 districts, +4.5% to +6.2%); the highest peak higher in
  the three 2023 phase-3 districts; energy not served higher in the 2023 districts. Three districts have no battery, so
  Omni moves nothing there; eight CityLearn's own controller cannot run, listed with its error.
- The Omni index rebuilt on v1 (`tools/omni_index.py`, `results/OMNI_INDEX.md`): it now reads each test's v1 table
  (`results/live/V1_*.json`, which `tools/confirm_abc.py` writes beside every `.md`) and lets a measure in only as its
  three-run reading allows: lower or higher in all three of our runs counts as the geometric mean of the three runs' ratios,
  and anything inside the noise counts as exactly 1. Real Kubernetes, six tests: **+26.2%** (work +20.4%, speed +95.1%,
  machines +4.4%, energy +2.7%). Azure's billed runs and the card join when their v1 runs land; the earlier engine's
  index (+12.9%) is kept at `docs/history/OMNI_INDEX_pre_v1.md`. The register's Kubernetes rows point at the v1 tables.
- `PATENTS.md` states what has been filed, from the application data sheet the founder supplied: a nonprovisional
  utility patent application under 35 U.S.C. 111(a), "The Omni-Compass", inventor Alan John Dubra, 15 drawing sheets,
  signed 20 September 2026, eighteen-month publication; the application number is withheld on purpose, and the sheet
  itself (which carries personal details) is not in the repository.
- The fifth and sixth v1 A/B/C tables: all four in one run (`results/live/V1_ALL_FOUR.md`, runs 37384945573, 37385646550,
  37394444337) and wandering demand (`results/live/V1_WANDERING.md`, runs 37384942870, 37385643291, 37394436586). All
  four: work inside the response line +48.4%, +44.7%, +42.1% (18.6 → 27.6 requests a second in A), p95 −57 to −63%,
  time over the line −39 to −43%, failed requests −12 to −13%, every one toward its aim in all three of our runs; machines and
  energy no difference beyond the noise. Wandering: p95 −56 to −60%, time over the line −37 to −44%, failed requests −12
  to −13%, toward its aim in all three of our runs; machines no difference; the declared energy models −0.3 to −0.8%, lower in all three of our runs. All six
  Kubernetes tests now have their three v1 runs; the README's result table is the v1 readings.
- The fourth v1 A/B/C table, the batch queue (`results/live/V1_BATCH.md`, runs 37385637932, 37385654462, 37394452486):
  machines in service −15 to −24%, machines after the queue is done −26 to −36%, standby-model energy −11 to −17% and
  mean response −11 to −13%, every one toward its aim in all three of our runs; the queue finished 0.7-0.9% later, clear of
  the noise in two runs and inside it in one, so that row reads no difference beyond the noise in 1 of 3 runs; p95 and
  the idle-power energy model no difference beyond the noise. The three-run tool now reads the batch queue's finish
  time and machines-after, and a real cloud's bill, as aiming lower (one row had read "lower in all three of our runs").
- The power grid's A/B/C table by rule (`tools/pandapower_abc.py`; `tests/test_pandapower_abc.py`, run by `verify.py`):
  pandapower is deterministic, so the three runs must reproduce each other; a gauge reads lower or higher in all three of our runs by its
  sign when they do, same under one part in a million, "the runs differ" when they do not; any added voltage violation and
  every extra tap operation read higher. The first v1 grid run (37377029333, 11 untouched SimBench grids, a full year,
  both load models): with ZIP loads the energy the loads drew is 1.3-1.5% lower in all 11 grids and the net import lower
  in all 11; losses are lower in 7 and higher in 4 (the rural and two semiurban grids, +0.6 to +1.5%); voltage violations
  never increase; tap operations fall in 10 grids (the city, suburb and commercial grids tap hundreds to thousands of
  times a year natively, Omni cuts that 20-35%) and double from 4 to 8 in one rural grid; with constant-power loads the
  load energy cannot change and the loss and import rows split the same way.
- GitHub's verify check caught a bug in the A/B/C tools that the local check missed: when a run's commit could not be
  read (GitHub's `gh` prints nothing for an unknown run), `tools/omni_version.py --commit ""` quietly checked the working
  tree instead, so an unresolvable run would have read as v1. Now a commit that cannot be read is "unknown" in both tables
  (`tools/confirm_abc.py`, `tools/citylearn_abc.py`), `omni_version.py` refuses an empty commit, and the test asserts it.
- The third v1 A/B/C table, steady load (`results/live/V1_STEADY.md`, runs 37384939815, 37385640601, 37391296025, all
  on the v1 fingerprint): mean response −47 to −51%, p95 −65 to −69%, time over the line −98 to −99%, machines in service
  −1.5 to −3.4%, standby-model energy −1.0 to −2.9%, every one toward its aim in all three of our runs; the idle-power energy
  model reads no difference beyond the noise in 2 of 3; failed requests zero in both arms. Three of the six Kubernetes
  tests now have their three runs: steady and faults toward its aim in all three of our runs, fairness no difference beyond the noise.
- CityLearn's A/B/C table by rule (`tools/citylearn_abc.py`; `tests/test_citylearn_abc.py`, run by `verify.py`). CityLearn is a
  deterministic simulator, so the three runs must reproduce each other: a score reads lower or higher in all three of our runs
  by its sign when they do, same under one part in a million, and "the runs differ" when they do not, which is a finding
  about the simulator or the harness. Two things the first v1 run showed, now stated in the table rather than hidden in a
  per-district reading: a district with no electric battery gets nothing from Omni (the runner moves only
  `electrical_storage` commands; the Quebec districts' comfort score still differs between the arms, which is CityLearn's
  own run-to-run variation, not an Omni result), and the 2023 challenge districts come out higher on the bill (+0.2 to
  +0.35%), ramping (+4.5 to +6.2%) and energy not served (+2 to +10%) while lower on daily peak and electricity bought.
  Eight districts CityLearn's own controller cannot run are listed with CityLearn's error.
- The three-run table carries the capacity test's own gauge as a judged row: work inside the response line (requests a
  second, the aim is higher), read from the run file's capacity block with its interval. The first v1 all-four run reads
  18.6 → 27.6 requests a second, +48.4% (+6.0 to +12.0 requests a second), p95 −63.2%, time over the line −40.0%.
- The A/B/C three-run table is made by rule (`tools/confirm_abc.py`; `tests/test_confirm_abc.py`, run by `verify.py`):
  three separate GitHub runs on the same frozen engine, each checked against the v1 fingerprint. Every judged row gets
  one of three readings: lower or higher in all three of our runs (the same sign in all three, every 95% interval clear of
  zero); no difference beyond the noise (an interval includes zero: native and omni could not be told apart on that
  measure, with the count of such runs); the runs disagree (runs clear of the noise point different ways). Nothing reads
  "not confirmed": a measurement the test cannot tell from zero is a result, and is stated as one.
- The archive keeps every raw file within GitHub's limit: GitHub refuses a file over 100 MB, and the 1,226-muscle
  organism at 1,000 copies writes a 99.6 MB record, so a slightly larger v1 record would have stopped the archive.
  `archive-run.yml` now stores any raw file over 50 MB gzipped (`gzip -n`, the same bytes every time; its repetition's
  `SHA256SUMS.txt` keeps the original's hash: `gunzip -c FILE.gz | sha256sum`). `tools/six_kube_report.py` reads the
  record plain or gzipped, and `tests/test_six_kube.py`, now run by `verify.py`, checks that both read the same.

## 2026-10-05
- Omni v1: the engine frozen and fingerprinted (`OMNI_V1.json`, `docs/OMNI_V1.md`, `tools/omni_version.py`): one SHA-256
  per engine file (38) and one digest over all of them. Every result states the version it ran on; any change makes v2
  and everything runs again. Every v1 benchmark runs three times (A, B, C); a claim is counted only when all three
  agree, with the 95% interval clear of zero in each. The register states the old GPU card result as the trade-off it
  was (card energy -3.5%, p95 +58.5%).
- The verify check on GitHub failed on the register commit (`f162ce8`) in the several-card GPU bench, which was ruled
  INVALID. The cause was in the test's stand-in `nvidia-smi` (`tests/standin_gpu/nvidia-smi`), not in Omni: every write
  opened the shared state file with "w", which empties it before the atomic replace. A process reading in that moment
  failed (22 of 400 reads with another process writing; 0 of 400 after the fix), which happens more often on GitHub's
  slower runners. Writes now go only through a temporary file and an atomic replace. A new test
  (`state_never_empty` in `tests/test_gpu_bench.py`) fails on the old stand-in (13 of 150 reads) and passes on the fixed
  one. Engine bytes unchanged: still omni-v1.
- `CLAUDE.md`: the founder's standing orders, kept in the repository so every working session starts from them.
- The batch test with cruise stepping back (`results/live/BATCH.md`): machines -20.7%, -32.4% once the queue is done,
  energy -14.3% (standby model), mean response -11.7%; queue time +1.1%, inside the noise. Added to the Omni index.
- Tweak A finished, muscle by muscle (`docs/MECHANISM_OF_ACTION.md` 9.6, `docs/REALMS_PREREGISTRATION.md`): the 656 muscles
  on the compass law read 0 away from their aims and 0 NOT ESTABLISHED (108 away from their aims this morning), every organism SUPERIOR WITHIN
  GUARDRAILS. Each lever moves only where its physics says it can pay: cooling power native; a UPS reserve native; a
  battery reserve spent only at the connection's wall when it can cover the overrun (the four batteries that buy fewer
  overruns read SERVICE IMPROVEMENT WITH ENERGY TRADEOFF); a power cap only where the machine's own curve saves (9.8);
  an effort cap only where copper loss exceeds the standing draw; node-pool machines released at margin 0.3, where no
  pool is later than native. Nine muscles read ENERGY IMPROVEMENT WITH SERVICE TRADEOFF: they run a little slower for
  less energy, which the label states.
- Tweaks A-E before any GPU run (`docs/MECHANISM_OF_ACTION.md` section 9; amendments 11 and 12; the realms amendment):
  - A. The 656-muscle realms table now runs the compass law (it still compared native against the retired allocation
    law). On the compass law all five organisms are SUPERIOR WITHIN GUARDRAILS: energy 0.1-0.2% lower, work the same,
    lateness no higher. Per muscle: 64 superior, 9 away from their aims (from 108). The allocation-law table moves to
    `docs/history/realms_allocation_law/`. Also fixed: each modelled muscle's compass was made fresh at every decision
    (from the rename); the organism runs go again on the fixed code.
  - B. The Azure burst test at `1 3 1 4 1 3`: at `1 6 1 8 1 6` the service's capped autoscaler could not serve the load in
    either arm (41% failed in both).
  - C. While cruising, the floor step reads and writes nothing (it read every pod every five seconds while a queue
    drained).
  - D. A change under one part in a million of the value reads "same", the number still shown.
  - E. The organism's start file is written whole and read only when whole (one six-kube repetition read it empty); the
    CityLearn omni arm's undefined name, left by the rename, is fixed.
- The Kubernetes results on the frozen engine: steady, wandering, all four, faults, fairness (`results/live/`). Capacity
  +41.7%, p95 59-64% faster, machines up to 2% fewer (the verdict keeps a machine when giving it back slows the
  service), energy equal or lower, no pod ever without a machine. The Omni index is now read from these only: +12.9%.
  The README and STATE_OF_PLAY say so; the earlier engines' sets go to history.
- Amendment 10 (Kubernetes reporting): pods the scheduler could not place are counted and judged; the snapshot count of
  pending pods and energy per core-hour are shown, not judged. Disclosed as made after the results were seen.
- GPU amendment 12: the steady hold applies only under an operator's cap (bisected: it slowed the card on its own
  firmware). The card model regenerated on this code.
- CityLearn round 2: four districts lower on electricity, peak and ramping (`results/citylearn/round2/`).
- Amendment 9: the emergency brake also reads idle from the autoscaler's floor (least pods, wanting no more, half
  its target or less), so it fires when a queue empties, not only at a zero reading a served service never shows. No
  result already measured could change (0 of 5,102 readings at the floor). The recording script no longer stops on an
  unanswered reading of machine CPU; end-of-window reads are retried. The batch test runs again.
- The law is named for what it is: the compass law (the word "bowl" is gone). In code: `omnicompass/compass_law.py`
  (class `CompassLaw`), `realms/compass_arm.py`, `omni_controller/gpu_compass.py`; the arm is `compass`. Runs recorded
  before the rename keep their folder names (`bench-bowl-N`), which the report tools read as the compass arm.
  The preregistration is `docs/K8S_COMPASS_PREREGISTRATION.md`. Raw recorded files and sealed records are untouched.
- The verifier's final line now reflects every check. It had read a local name left from the preregistration loop, so it
  printed PASS even when a check above it failed (`verify.py`). With that fixed, two hidden failures surfaced and were
  fixed. (1) The sealed GPU governor had three comment and log strings changed by the "reset" rename; its sealed bytes
  are restored, and behaviour is unchanged. (2) The mechanism identity was re-recorded: only M_act (the GPU actuator)
  changed, from the recorded GPU amendments; F, Theta, C, h, G, dt and A and every fixture result are identical.
  160 checks pass, none fail.
- On the frozen engine: the fault test and the fairness test, ten pairs each (`results/live/FAULTS.md`,
  `results/live/FAIRNESS.md`). Nothing moved away from its aim beyond the noise; the Omni index is now +15.6%.
- The archive takes a list of runs; failed Azure and CityLearn runs post their own output on the run's page.
- One engine, frozen: the live Kubernetes controller with rules 1-8. New today: rule 5 (a pinned gauge is not a steady
  demand), rule 6 (coasting: ease off a step a window), rule 7 (cruise: every machine in service while work waits),
  rule 8 (the emergency brake: straight to the floor at zero demand). The floor of two machines; every machine usable.
- The names: native (the system on its own) and omni (Omni-Compass on top of native); the pedals (idle, gas, brake,
  reset) and the kill switch (security only, `omnicompass/master.py`).
- CityLearn, an independent simulator of real buildings and batteries: round 1 recorded (battery districts lower on the bill,
  water-tank districts higher on peaks), the fix (only the electric batteries steered), round 2 on untouched districts.
- The harness keeps recording through an unanswered reading or load step (the Azure burst test lost two native arms to
  it before the fix).
- The batch test (a queue of jobs) for cruise and the emergency brake.
- The repository lined up: the front door, one index of documents, dated reports in `docs/history/`, the layout check
  in every verification.

## 2026-10-04
- The Omni index; all four in one run (+29% work, p95 -62%, machines -3.6%, energy -0.3%, each proven); the six
  organisms with the real cluster inside; the staging law written as equations.

## 2026-10-02
- The compass law (`omnicompass/compass_law.py`) and the plug contract: one smooth law for every muscle, one restore point,
  read-back, the one-writer rule.
- Two-wire GPU governor (`omni_controller/gpu_compass.py`): clock ceiling and power limit; the wire check
  (`tools/gpu_wire_check.py`) runs before anything else.
- The six organisms (four realms, the four stacked with duplicates, the whole tower) as one benchmark set, with the
  real card inside on a GPU machine (`tools/run_hil.py`) and the 1 / 10 / 100 / 1,000 runs-and-size grid
  (`tools/run_scale.py`, workflow `six`).
- Robot-joint simulation compiled (identical results, about 30 times faster).
- Real Kubernetes set 24 reproduces set 23.
- License: evaluation and Simulation use only; Omni-Compass Enterprise License for everything else; US filings notice.
- The Omni-Compass Manual, edition 1.0.

## Earlier
See `docs/HISTORY.md` and `docs/STATE_OF_PLAY.md`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
