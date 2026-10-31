# CLAUDE.md: standing orders for any session working on this repository

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

These are the founder's orders, gathered from the full working record. They load every session. Follow them unless
the founder overrides one in the conversation.

## What Omni is

- Omni-Compass is a **supervisory governor**. It always sits **on top of a native controller**: the Kubernetes HPA,
  GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo, and so on. It is never standalone and never a
  competitor to native.
- Every benchmark has exactly two arms, **native** and **omni** (omni means Omni on top of native). There is no other
  arm and no other name. The governors' four ways (the founder's order of 20 October, below) pair two arms at a time.
- **Do no harm** (its meaning, the founder's words of 19 October; it has no other, `DISCLOSURES.md` section 3): Omni's one
  goal is to strengthen the organism and keep it healthy, working at the best state its own muscles can carry; what is fed
  in (its nutrients: work, data, energy) goes through its muscles to the most and best output it can make. Harm is judged
  at the organism: less output than native (less work; more time waited, missed or failed) or less health (a muscle past
  its own limit, a service over its own line, anything made to fail). Every muscle only as far as it can go, never past.
  The muscles are offset and engaged as one body: one may be used less, left native or rested so another carries more,
  when the whole comes out ahead and every muscle stays healthy; which to drive and which to leave native is the brain's
  live decision. Reactive and proactive, like an immune system. Every row is still shown. The engine that stands keeps
  the strictest form: every muscle judged on itself, never below native, nothing traded between muscles; where it can't
  bring a knob a GAIN, that knob stays native. The 2% verdict (`omnicompass/verdict.py`) is the engine's trigger, not a
  stamp on a report. The trade between muscles, judged on the organism, is the next version's work (the model gate first).
  Gains are uncapped.
- Headline: more work, faster, on fewer machines, with less energy. One combined number: the Omni index.
- **The max is the default brain** (12 October): every muscle runs at its own limit, never past it and never below
  native; it rides the edge, not the middle. "We're never looking to shave energy": the energy it takes is **power
  given**, shown beside the work, the speed and the wear it bought, never called a loss; on the engine that stands the
  max takes nothing from one muscle to give to another (a muscle giving way for the organism's whole output is the next
  version's, under do no harm above). Results are judged on work, speed, misses and failures. Anyone can tune it down from the
  max (the dial: the tune-down, `V5SAVE`). A knob native already runs at the top of its range is "at its limit on native".
- The word is **compass**, never "bowl". The law is `omnicompass/compass_law.py` (`CompassLaw`): a band with 5%
  cushions, two antagonist forces, smooth (tanh), not hammering.
- Wiring is a two-way plug, one wire in and one wire out. The brain does the math. The knob is restored to the snapshot
  taken once, at the start.
- **One pedal, no brake** (12 October), like an electric car: push for more, lift off for less; lifting hands the
  setting back toward native; idle is the pedal lifted all the way; reset hands everything back to native; cruise (a
  known queue waiting), autopilot / watching / off. After a crash the plug walks every setting back to native gradually
  (the lease); the **kill switch** is separate, for security only, and instant (`omnicompass/master.py`,
  `tools/omni_switch.py`). The word "brake" is not used.
- Scaling: floor of 2 machines, no ceiling, every machine usable. Traffic tests step by one (1 2 3 2 3 4 …).
- Nothing is hardwired. Anything that doesn't work is removed, not just switched off.

## The engine: Omni v23 stands (v22, v21, v20, v19, v18, v17, v16, v15, v14, v13, v12, v11, v10, v9, v8, v7, v6, v5, v3, v2 and v1 kept for their results)

- **Omni v23** (`OMNI_V23.json`, digest `c96ea4105d8747db`, 65 files; `docs/OMNI_V23.md`) stands on main from 31 October, evening (its campaign from 20:00 UTC), on the
  founder's order of that day (Orders of 31 October: Omni direct keeps every muscle Omni-Compass cannot be; "any muscle that we don't
  have, Omni-Compass cannot be it: it has to be there, if that's Kubernetes or whatever") and the standing order that every fix lands as
  the next version, told, not asked: omni-v22 with one guard in the Kubernetes governor's pod muscle of its own
  (`omni_controller/controller.py`, `_own_pods`, `_own_refused`, `OWN_REFUSALS`). A write of a workload's own scale that the cluster
  refuses (its permission, its admission, its API) is recorded in the audit and the decision goes on, the cluster keeping the last
  count that landed; at three refusals in a row Omni-Compass cannot be that knob's muscle, so it makes native's own pod autoscaler
  from the operator's target and range recorded on the workload (`kubectl autoscale`; with no range recorded, one to ten times the
  operator's count), audits the hand-back and leaves the workload to it for the rest of the run; a write that lands ends the run of
  refusals. Every other arm is untouched (Omni on native never removes native's controller); 64 of its 65 files are omni-v22's
  bytes. Found the same day: every arm by itself on kind since omni-v19 had its pod writes refused by the rig's own identity (the scale
  subresource was not granted) and ran with no controller on the pod count; both rig faults fixed (`docs/SOLO_PREREGISTRATION.md`,
  amendments 1 and 2), the rig refusing a window of that arm in which a decision failed or the knob was handed back, the identity
  allowed to create an autoscaler in the workload's namespace for the hand-back alone. The model gate against omni-v22
  (`results/model_gate/V23_VS_V22.md`): identical on every gauge of all 11 models and every seed, no LOSS (no model refuses a write;
  the guard's proof is `tests/test_own_replicas.py`, `HandBack`, and the arm's own files when the entry runs again). Every benchmark
  runs again on it from 20:00 UTC on 31 October.
- **Omni v22** (`OMNI_V22.json`, digest `0e23a0bc561b900a`, 65 files; `docs/OMNI_V22.md`) stood on main from 30 to 31 October, on the founder's
  order of that morning ("find out why they went one way or the other and tweak it and turn it and tune it to the best possible way for
  an Omni Compass engine to interact with this as a system governor ... bring to a solid A mechanism"): omni-v21 with the five data
  stores' wires brought to the max. The store wires were written on 9 and 10 October, before the order of 12 October that the max is
  the default brain, and had never been brought to it; on omni-v21 they carried 33 of the 50 LOSS rows, because the wall abandoned every
  spend trial and the fail-up was clamped to the allowance those trials never earned (`docs/STORE_ROOT_CAUSES_2026-10-30.md`). Now what a
  wire's own rule asks goes through unclamped, up to the operator's cover, never below native, the resource power given; memory is spent
  only where **the store's own account of a miss** (MySQL: the performance schema's timer on the data files' reads against the statement
  timer; MongoDB: WiredTiger's page-read time for the application's threads against its read latency; Redis: the application's own split)
  says the misses are at least the one key's floor (0.5%) of the service's time, and only while the host keeps 5% of its memory available
  after the notch; a hand-back never goes below the working set's floor (the most the store held in 60 s); Kafka's group has a twin of its
  arrivals and a reflex that goes at once to the count that carries them; PostgreSQL's pool is never taken below the pooler's own setting
  (`tools/store_brain.py`, the five `tools/run_*.py` wires' `Brain`). `OMNI_DIAL=save` keeps omni-v21's loop on every wire (the tune-down);
  `tools/store_brain.py` and `tools/knob_verdict.py` join the fingerprint (`STORE_WIRES`). Declared before any run: MySQL amendment 6, YCSB
  6, PostgreSQL 4, Redis 5, Kafka 4. The model gate (class S): the store gate on omni-v21's archived seconds no LOSS on any wire; the Redis
  closed-loop model work inside the line GAIN (up 7.7% to 22.9%), latency GAIN, memory power given, no LOSS; the Kafka closed-loop model
  at the counted 30 s no LOSS on the development and the untouched seeds, one LOSS row at 20 s a notch (the burst's peak queue, +30.6%,
  inside the seeds' spread; run C's setting, not the counted one, on the next version's list); the Kubernetes governor's models identical
  to omni-v21 on every gauge. With it, **the hand-back lands**: every step of the Kubernetes governor's hand-back (`omni_controller/controller.py`
  `_persist`, `omni_controller/muscles.py` `_guard_restore`, `RESTORE_TRIES` 5) is tried five times against a transient failure of the
  cluster's API, each muscle on its own, and what did not land is raised and audited, never silent (six-kube run 41044680505, repetition 346:
  one 500 on the autoscaler list at the reset had ended the whole hand-back on its first read and left the conveyed limits and the replica
  range behind, the arm marked invalid). A slope of latency on miss share was tried as the price of a miss and is not used anywhere (it
  reads the host's noise as a price); the morning's reading that a MySQL or MongoDB miss costs nothing is withdrawn on the root-cause page
  (the server's own meter on a machine of our own: 3% to 32% of a statement's time, class L there). Every benchmark runs again on it, the
  five stores first, every store table at the counted 30 s a notch.
- **Omni v21** (`OMNI_V21.json`, digest `b658f05d43c1e602`, 63 files; `docs/OMNI_V21.md`) stood on main from 25 October, evening, to 30 October, when omni-v22 landed on it, on the
  founder's order of that afternoon: the immune system knows itself, knob by knob. A knob redlining past its line that Omni-Compass's
  own pushing cannot bring back goes to native when native's twin reads it lower, and stays with Omni-Compass when native is not
  stronger (redlining less than native would is still a benefit against native). `omnicompass/immune.py` and its C++ twin
  `cpp/src/immune.cpp` (sealed, `tests/test_cpp_immune_parity.py`); the hand-back carried through the nervous system in both twins
  (`native_hold`); wired into the Kubernetes governor for each service's autoscaler target with an M/M/1 native twin; omni-v19's
  immune rules (the hand-back on a waiting pod, the immune memory, native's line, maturity, the step back) carried onto omni-v20.
  The model gate against omni-v20: no LOSS in any model; pods waiting down about 13% in every cluster model, GAIN. Every benchmark
  runs again on it from 17:30 UTC on 25 October.

- **Omni v20** (`OMNI_V20.json`, digest `1df07f8e36a97985`, 62 files; `docs/OMNI_V20.md`) stands on the branch since 25 October,
  13:24 UTC, under the founder's words of 25 October ("Fix, fix, fix ... it can be fixed") and the standing order that every fault
  found is fixed and lands as the next version, told, not asked: omni-v19 with the five data stores' wires fixed at their causes,
  found by tracing why the Omni index fell from +4.32% to +3.397% under the 0.5% key (`docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md`).
  sysbench's brain reads sysbench's own statements, prepared ones included, as its own account (`tools/run_sysbench.py`; it read 4.1
  a second, the harness's own queries, against sysbench's 999 to 4,198); above the operator's count Kafka hands a consumer back on
  calm within one poll round, 30 s after the last change, with no double rebalance at the start (`tools/run_kafka.py`); below native
  YCSB grows its cache back 64 MB a second while it misses, full at WiredTiger's own 80% or evicting (`tools/run_ycsb.py`); YCSB and
  Redis record the stack's CPU apart from the host's; pgbench starts every arm from the same state and the workflow logs the
  runner's stalls. The store gate (`tools/store_gate.py`, `results/model_gate/STORE_GATE.md`, open-loop, class S) replayed every
  archived arm through both wires: no LOSS (the YCSB cache rise, +5.2%, power given). Every benchmark runs again on it, sysbench's
  rows first (its old reading was blind). 57 of its 62 files are omni-v19's bytes.
- **Omni v19** (`OMNI_V19.json`, digest `36ee67284c035235`, 62 files; `docs/OMNI_V19.md`) stood from 24 October, 16:54
  UTC, under the founder's order of 23 October (Orders of 23 October, the third arm, Omni-Compass by itself) and the standing order
  that every change lands as the next version, told, not asked: omni-v18 with a pod muscle of its own (`--own-replicas`,
  `omni_controller/controller.py` `_own_pods`): for a workload the operator names and no autoscaler governs, the governor sets the
  replicas itself through the workload's own scale by strict C's rule, at the target the compass moves inside the autoscaler's
  cover, never below the operator's count at the max, reconciled every 15 s on the fast checks (`--own-every-s`, the pod
  autoscaler's sync), the compass moving the target only in a decision, the operator's count handed back by the reset; and the
  models' arm by itself (`realms/harness.py` `SOLO`, `realms/plants.py` `native_off`). 59 of its 62 files are omni-v18's bytes.
  **One name, two engines, reconciled**: the change was first landed on the live engine's branch on 24 October, 01:30 UTC, under the
  name omni-v18 (digest `22486290b19349eb`, 55 files, on omni-v17) while main's omni-v18 stood; that engine never stood on main and
  none of its records is read as main's omni-v18; its change, taken onto main's omni-v18 and gated again against it, is omni-v19
  (the code's comments that named the branch's numbers now name omni-v19; every rule is the branch's). The model gate against omni-v18
  (`results/model_gate/V19_VS_V18.md`) read every gauge of all 11 models identical, seed for seed, every table the one the branch's own
  gate against omni-v17 printed; no LOSS against omni-v18; in the models the native and max arms read byte-identical on both engines
  (806 readings on the development seeds). By itself in our own model (`results/model_gate/SOLO_V19.md`, class S) against native on
  the same machines: the 95th percentile GAIN (down 19.4%), the minutes over the response line GAIN (down 64.9%), machines and
  energy EVEN; against omni-v18 by itself, which holds every workload at the operator's count
  (`results/model_gate/SOLO_V19_VS_V18.md`), the 95th percentile GAIN (down 100.0%) and the minutes over the line GAIN (down 99.3%). A
  fault found on the branch before it landed there (at the 60 s beat the first candidate moved pods once a minute; the minutes over
  the line read LOSS) is fixed in it. The real arm: `ARM=solo` on kind (`docs/SOLO_PREREGISTRATION.md`; `kubernetes by itself` in
  `scripts/reruns.txt`), three runs; in our models the organisms runner's third arm (`tools/run_realms_v5.py`). Every benchmark runs
  again on it from 16:54:55 UTC on 24 October.
- **Omni v18** (`OMNI_V18.json`, digest `1cb92edb64c4391d`, 62 files; `docs/OMNI_V18.md`) stood on main from 23 October, night,
  to 24 October, afternoon, when omni-v19 landed on it, on the founder's orders of that evening ("Native is Kubernetes on the muscles. Omni on native is Omni on top of Kubernetes on
  top of the muscles. And then Omni direct is simply Omni on top of the muscles, no Kubernetes ... they all need to be written in
  code"; "It should be not 17 anymore, it should be 18"): omni-v17 with Omni direct taken into the engine. The seven files of
  Omni-Compass's own orchestrator that hold its rules (`omni_orchestrator/`: the brain, the control plane, the room rule, the
  hand, the walls, the front, the package; not the showing's workload and clients) are fingerprinted like every other wire
  (`tools/omni_version.py`, `ORCHESTRATOR_WIRES`; a version declared before omni-v18 is read without them), so no rule of Omni
  direct changes without the version changing; 55 of its 62 files are omni-v17's bytes. The three arms are always shown together:
  native (Kubernetes' published autoscaling rule on the muscles, brain `yardstick`), Omni on native (Omni on top of the rule, never
  fewer units, no fold, brain `omni_native`) and Omni direct (Omni alone on the muscles, brain `omni`). Its brain carries the
  engine's conveyance, reflex, twin, busy room rule and the fold under the verdict, and a hold on trials the traffic keeps
  abandoning (6 beats, doubled in a row to the recheck), found on the first three-arm showing and fixed before it landed. Quick
  form after the fix, one run each, class L: Omni on native against native work GAIN (up 8.3%); Omni direct against native work
  GAIN (up 9.1%); Omni direct against Omni on native the 95th percentile GAIN (down 13.2%), units GAIN, a cut (down 9.5%); no
  LOSS in any pair. The three runs on GitHub's machines (full form, `results/orchestrator/V18_THREE_ARMS_ABC.md`): both Omni
  arms against native work GAIN and the 95th percentile GAIN in all three, machines EVEN, units power given or EVEN; Omni direct
  against Omni on native EVEN on every gauge; no LOSS. The model gate against omni-v17 (`results/model_gate/V18_VS_V17.md`) reads omni-v17's numbers on every model (none
  of its 55 files moved). Every benchmark runs again on it from 02:51 UTC on 24 October, when it reached main (a run counts only on a commit
  that carries `OMNI_V18.json`; the runs started from 21:19 UTC on 23 October ran omni-v17's commits). (Not to be confused with the live engine's branch's own omni-v18 of 24 October, digest
  `22486290b19349eb`, 55 files, which never stood on main: its change is omni-v19's.)
- **Omni v17** (`OMNI_V17.json`, digest `7c937d09e4031cc7`, 55 files; `docs/OMNI_V17.md`) stood on main on 23 October, from the
  morning to the night, on the founder's order of 22 October, afternoon (Orders of 22 October, the heartbeat a dial): the main engine takes its full
  decision every 60 s (`--interval 60`, the parser's default in `omni_controller/controller.py`, in every rig, install file and
  cloud run), any beat from 5 to 120 s can be set, and every beat is shown beside native with what it buys and what it costs
  (`results/model_gate/V17_LADDER.md`, `tools/beat_ladder.py`; on the live engine page, the page's section 1j; the real runs,
  `docs/PACE_PREREGISTRATION.md`, amendment 3, eight arms). The monitors scale with the beat (`omni_heartbeat_seconds`, the
  staleness alert at three beats, the control panel's `POST /v1/beat`). One fault the dial's ladder found before it landed is
  fixed in it: at 90 and 120 s the cruise wait (120 s) rounded to one decision, so one reading with a pod waiting put every
  machine in service (the kind setting's first reading: machine-hours +17% and +21% against 60 s, the minutes over the line −72%);
  the cruise wait is now never fewer than two readings (`tests/test_pace_clocks.py`, failing on the unfixed rule), and nothing at
  80 s or faster moves. 54 of its 55 files are omni-v16's bytes. Corrected, the kind benchmark's setting reads at 90 s, against 60
  s, the machine-hours down 1.7%, EVEN, the minutes over the line down 4.7%, EVEN, the pods waiting down 12.1%, EVEN, the 95th percentile down 0.2%,
  EVEN; at 120 s the machine-hours down 2.1%, EVEN, the minutes over the line down 3.7%, EVEN, the pods waiting down 29.6%, GAIN; machines parked
  over the eight days 190 and 119 against 329 at 60 s. The model gate against omni-v16 (`results/model_gate/V17_VS_V16.md`): Every model
  that sets its own period reads identical to omni-v16 on every gauge and every seed (9 models and the verdict); as shipped,
  omni-v17 at its 60 s against omni-v16 at its 15 s, every gauge reads EVEN; no LOSS against omni-v16. The ladder: Every beat
  reads the cluster from about 86,400 times a day at 5 s to 37,400 at 120 s (39,700 at the main engine's 60 s), for 5.5 to 1.6 s
  of Omni's own processor an hour. In the kind benchmark's setting every beat reads the minutes over the line GAIN against native
  (−12.0% at the main engine's 60 s, −28.2% at its most), for machine-hours and energy given; the rows that read LOSS against
  native are in the kind setting pods waiting for a place at 5, 10, 15, 30, 60, 75, 90 and 120 s (+175% to +317%); and in the
  cloud's pods waiting for a place at 5, 15 and 30 s (+102% to +127%), the 95th percentile at 15 and 30 s (+0.5%, +0.4%), the
  minutes over the line at 15 s (+2.3%): the engine's, on the next version's list. Every benchmark runs again on it from 17:00 UTC
  on 23 October.
- **Omni v16** (`OMNI_V16.json`, digest `5c5502f12b1c0ce4`, 55 files; `docs/OMNI_V16.md`) stood on main on 22 October, from the morning to the evening, on two
  words of the founder's: "Go opus" on the plan put to him that night (every clock of the Kubernetes governor in seconds, the pace
  read at 60, 15, 10 and 5 s in our models, three runs at each pace on GitHub's own machines), and, once the models had read,
  "15 sec all over heart beat fix update code". **The heartbeat is 15 s**: the governor's full decision comes every 15 s by default
  (`--interval 15`, `--floor-interval 5`; `omni_controller/controller.py`), native's own pod autoscaler's pace, in every rig,
  install file and cloud run (`scripts/kind_bench.sh` `OMNI_INTERVAL`, `kind_paired.sh`, `kind_robust.sh`, `kind_full.sh`,
  `kind_pilot.sh`, `deploy/install/*.yaml`, `deploy/controller.yaml`, the alert rules' 45 s staleness bound); each run writes its
  period beside its files (`omni_interval.txt`) and the receipts read each run at its own (`tools/live_reps.py`). omni-v15 with the
  clocks changed and the heartbeat set, and nothing else (every gain, guard, preset and muscle is omni-v15's; 50 of its 55 files
  are omni-v15's bytes): the brain's own minute (`omnicompass/adapter.py` `period_s`, and its C++ twin `cpp/src/governor.cpp`,
  sealed: the reading's weight 1 − (1 − 0.339)^k a step with k = period / 60 s, the inner time, the dwell and waits, the machines
  added or removed over the last minute's steps), the compass's damping and smoothing, the edge's window and rates
  (`omnicompass/edge.py` `pace`), the additions past the scheduling floor (a step a minute), a command's minute to land, the host's
  busy share over a minute (`omni_controller/capacity.py`), the heat law's minute and one batch job a minute
  (`omni_controller/muscles.py`), the coast per raise, the conveyance every 15 s whichever check falls due, and a loop that keeps
  its own schedule (`tests/test_pace_clocks.py`, `tests/test_loop_schedule.py`). The cushion each muscle keeps is the same at any
  pace; the pace sets only how soon trouble is seen, and a longer one would only blind the governor longer (the founder's question
  of 22 October, answered so). At 60 s it makes exactly omni-v15's decisions (the model gate, `results/model_gate/V16_VS_V15.md`: 4,578
  audit records, none different). The pace study (`results/model_gate/V16_PACE.md`, a plant that moves every 5 s): 15 s against 60 s,
  alert minutes −14.7% in the kind setting and energy per core −2.6% in the cloud's (GAIN), every other reading EVEN, no LOSS at
  any pace; as shipped (the gate's `cluster_shipped`, omni-v16 at 15 s against omni-v15 at 60 s) every gauge EVEN. Against native
  the pods waiting for a place read LOSS at every pace, the old 60 s default included, and in the cloud's setting at 15 s the 95th
  percentile (+0.36% to +0.47%) and the alert minutes (+2.31%), which read EVEN at 60 s only by the seeds' spread: the engine's, on
  the next version's list. The real runs (`docs/PACE_PREREGISTRATION.md`, amendment 2: native, Omni-Compass at 15 s, and at 60, 10
  and 5 s, three runs) read the heartbeat for real. The seal is written under Python 3.12 (its compensated `sum` is what the C++
  engine-runs twin follows; 3.11's differs by one rounding step). Every benchmark runs again on it: its campaign opened at 07:30 UTC
  on 22 October, and the conductor starts its runs from the afternoon's push that fixed its engine check (Orders of 22 October).
- **Omni v15** (`OMNI_V15.json`, digest `0a53cdd7a558f803`, 55 files; `docs/OMNI_V15.md`) stood on main 21 to 22 October, landed 21 October, evening, under the
  founder's standing order that every fault found is fixed and lands as the next version, told, not asked, and his word of 21 October
  ("push, push, push on GitHub, update, enhanced engine"): omni-v14 with two changes. The brain's request for the power cap
  (`omnicompass/adapter.py`, its C++ twin `cpp/src/governor.cpp`) trims to demand only while the response line has been clean for
  the governor's own clear time (the Kubernetes governor's `--slo-clear-s`, 180 s; the card governor's 3 decisions, which it now
  hands the brain): on the omni-v11 long run the request switched between the start limit and the trim at 126 of 350 decisions and
  turned back at 123 of them, at the one threshold on the queue and the state; on the same decisions, read from the governor's own
  audit, the gate leaves 35 moves and 32 reversals (`tests/test_cap_band.py`, the fixture
  `tests/fixtures/robust_long_39173420146_decisions.json`). On Kubernetes the cap wire is off, so no table moves for it; the card
  governor had applied the same gate outside the brain. A dwell with a glide was built first and refused by the gate (seven small
  moves for one on the model cluster, 25 limit writes for 16 on the model card). And every wire that holds a governor's rules is in the
  fingerprint (`tools/omni_version.py`: the data stores' five runners, the swarm, MuJoCo and the CPU power runner, their bytes as
  they stood; a version declared before them is read without those eight and only those). Declared with it, not an engine change: the kill test reads the
  300 s after the kill (`docs/ROBUSTNESS_PREREGISTRATION.md`, "On omni-v15"). The model gate against omni-v14
  (`results/model_gate/V15_VS_V14.md`, eight seeds, every model and two card models new with it) read every service gauge identical on every model, the card models identical (the card governor already applied the gate outside the brain), the verdict identical, and the request's own moves, reversals and travel EVEN on the model cluster (+3.7% at 60 s, −1.4% at 15 s, where breaches are rare and short; the fault's regime, the long run's clustered breaches, reads −72% on the run's own decisions): no LOSS. Its campaign opened at
  02:30 UTC on 22 October and started no run: the conductor read every commit from omni-v15's push on as no engine (Orders of 22
  October); the last runs it started, at 00:31 UTC, were omni-v14's.

- **Omni v14** (`OMNI_V14.json`, digest `7afba44615fcff8f`, 47 files; `docs/OMNI_V14.md`) stood on main on 21 October, from 04:47 UTC to the evening, the founder's
  orders "knobs on every monitor, to turn off and on ... a muscle" (20 October) and "tune the engine" (21 October): omni-v13 with
  two changes in the Kubernetes governor (`omni_controller/controller.py`, `omni_controller/muscles.py`). `--native MUSCLE[,...]`
  (or `OMNI_NATIVE`, the control panel's muscle button) leaves any muscle where native runs it, never written, an unknown name
  refused; and the operator's own commands run without a shell unless they hold a pipe, a redirect or a variable (the static
  scan's high findings 3 to 2). A third, no conveyance raise on a reading that leaves out another workload's starting pods (the
  raise omni-v13 makes once early in the batch model's queue), was refused by the model gate: the batch back at native's, but the
  web's 95th percentile 6.4% higher than omni-v13's; it is kept on the branch `v14-convey-study` until the model's web model is set
  from a real run's files. The model gate against omni-v13 (`results/model_gate/V14_VS_V13.md`, eight seeds, every model, the batch pods listed as a cluster lists them) read every gauge identical, and the verdict model identical: no LOSS. Every benchmark runs again on it.
- **Omni v13** (`OMNI_V13.json`, digest `0088837333c6f0fc`, 47 files; `docs/OMNI_V13.md`) stood on main 20 to 21 October, landed 20 October, evening, the
  founder's order that every fault found be fixed and every fix land as the next version, told, not asked: omni-v12 with one fault
  fixed in the Kubernetes governor's conveyance (`omni_controller/muscles.py`), found on KubeRay's rig with the organism alone (the
  queue 0.6% to 0.8% later and the web's 99th percentile 4% to 13% higher, LOSS in all three runs). The web pods' limits were raised
  to 3,700m in the queue's first half minute and kept through the saturated queue (omni-v7's guard holds a new raise at the host's
  top, never one already given): the batch pods hashed 7.6% slower and the web served no faster while the queue ran; no machine was
  parked during a saturated queue (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 11). Now, on a shared host at its top (busy at or
  over 75%) beside another workload's room (a pod whose limit is above its request), every limit given goes back to the operator's,
  conveyed again only under 70%; and every other pod on a machine is counted by its own limit, where omni-v12 counted requests. The
  model gate (`results/model_gate/V13_VS_V12.md`, with a batch model set from the KubeRay runs' own files): no LOSS against omni-v12 in
  any model, the web-only models identical; in the batch model the queue and the job turnaround back at native's. Every benchmark runs
  again on it.
- **Omni v12** (`OMNI_V12.json`, digest `d38b58fbe28939b8`, 47 files; `docs/OMNI_V12.md`) stood on main 19 to 20 October, landed the night of 19 October,
  the founder's order ("Of course I want you to land version 12 ... every time you do that ... it becomes a new version"):
  omni-v11 with two faults fixed, both found on the omni-v11 runs. A CPU-limit raise the cluster's admission refuses is held
  until the pod's limit changes, the raise shrinks or a wait passes (5 minutes, doubled up to an hour;
  `omni_controller/muscles.py`), where omni-v11 wrote it again at every fast check (the capacity test, about 970 to 1,000
  refused writes an hour); and the swarm's proximity reflex hands back the planner's cruise in the tick it is triggered, its
  reach growing with the square of the speed (`tools/run_swarm.py`, outside the fingerprint's scope, declared with v12). The
  model gate (`results/model_gate/V12_VS_V11.md`): identical to omni-v11 on every gauge of every model but the refused writes,
  −97.5%, GAIN; no LOSS. The stricter verdict built with it (a step kept only when its whole 95% interval is inside the
  allowance) was refused by the same gate (no give-back trial could start in the cloud model) and is kept on the branch
  `v12-verdict-study`. The swarm's preregistration takes amendment 2 with it (a collision with Omni-Compass on top is a judged
  LOSS row, a cell void only when native collides, three mission draws never flown). Every benchmark runs again on it from
  00:30 UTC on 20 October; earlier tables stand as their own engine's until each benchmark's three runs on v12 land.
- **Omni v11** (`OMNI_V11.json`, digest `745aa53ec8eeb67b`, 47 files; `docs/OMNI_V11.md`) stood on main 18 to 19 October, the
  founder's order that every fault found be fixed, none set aside: omni-v10 with one guard in the Kubernetes governor
  (`omni_controller/controller.py`). A reading with no machine in service is blind, never an overload: the decision holds and
  says why, nothing is decided from it or written, the floor check returns, and the last reading with machines stays the
  conveyance's bound. Found in the omni-v10 CruiseKube test (run 39120444653, repetition 8: every kind worker out of service
  for two minutes while the service answered every probe; omni-v10 fed the engine the highest overload, then divided by the
  empty capacity). `tests/test_blind_reading.py` reproduces the fault on omni-v10 and passes on omni-v11; the model gate
  (`results/model_gate/V11_VS_V10.md`, with a blink model) before it was pushed. Every benchmark runs again on it; earlier tables
  stood as their own engine's until each benchmark's three runs on v11 landed (its 23 tables are its own). Its bookkeeping
  was landed by `tools/land_engine.py`, the one command for every version from now on.
- **Omni v10** (`OMNI_V10.json`, digest `4bf39b0d707784de`, 47 files; `docs/OMNI_V10.md`) stood on main on 18 October, the
  founder's order ("Omni-Compass should be tuned to exploit all that can be and keep all healthy and never raise its bill";
  then "push, push in the bush"): omni-v9 with one file changed, the CityLearn runner. The battery wire's glide is 0.0875 of
  the command's range an hour (omni-v9: 0.0625), the speed that cuts the bill most with no LOSS read by the one key; the
  runner's own receipt reads every score by the one key. Read locally on CityLearn 3.0.2 before it was pushed: the bill
  −8.4% to −20.1% in every district with a price (1.1 to 2.4 points beyond omni-v9), no LOSS against native in any district read before the push;
  the electricity bought, the carbon and the peaks fall a little less than on omni-v9, still GAIN, and two rows of the 2022
  phase 3 are power given (the ramping +6.18%, the net-zero shortfall +0.25%). Refused before it: steering the outage
  buildings' batteries outside the outage hours (energy not served +0.69% in one 2023 district, a LOSS). The model gate
  (`results/model_gate/V10_VS_V9.md`) before it was pushed. Every benchmark runs again on it; earlier tables stand as their own
  engine's until each benchmark's three runs on v10 land.
- **Omni v9** (`OMNI_V9.json`, digest `7379f3a79ff2c475`, 47 files; `docs/OMNI_V9.md`) stood on main 17 to 18 October,
  the founder's order ("we're going into another version of Engine ... Apply the fix, run it, and see in the model sim that
  it works"; then "go go go"): omni-v8 with the CityLearn battery wire reading the coming hour (the mean of the same hour
  over the past seven days, only hours already seen) and gliding at up to 0.0625 an hour (0.05 before; the fastest glide that read no LOSS on any score
  in any district: 0.075 and faster raised the ramping in one district), because the reading of
  the hour gone ran about five hours behind the day and left the batteries empty at each month's top hour (the 2022
  robustness district's monthly unevenness +0.11%, power given: a peak, a swing and an unevenness are power held, the
  founder's correction of 17 October); and every 95% interval on the exact Student t quantile
  (`omnicompass/student_t.py`; every tabled value unchanged, no published reading moves). Proven locally on CityLearn
  3.0.2 and in the model gate (`results/model_gate/V9_VS_V8.md`, identical to v8 on every model) before it was pushed. 44 of its
  47 files are omni-v8's bytes. Its reruns started on 17 October and run to their end as its own record.
- **Omni v8** (`OMNI_V8.json`, digest `f93d233136a1f902`, 46 files; `docs/OMNI_V8.md`) stood on main on 17 October,
  the founder's order ("there's a new version 8 ... push in all and update all"): omni-v7 with one wire changed, the
  CityLearn runner (`tools/run_citylearn.py`): a battery whose building simulates power outages stays native, because its
  charge is also its building's reserve (omni-v7's CityLearn table read LOSS in all three runs in the seven 2023 districts,
  the only ones with outages; every other district's commands are omni-v7's bytes). The other 45 engine files are omni-v7's.
  Every benchmark runs again on it (`scripts/reruns.txt`; the conductor's reruns, grid and Azure queues restarted on 17
  October); one row the table printed LOSS stayed, the 2022 robustness district's monthly unevenness (+0.11%), power given by the
  key, and cut in omni-v9.
- **Omni v7** (`OMNI_V7.json`, digest `d6d467b824c585f1`, 46 files; `docs/OMNI_V7.md`) stood on main 16 to 17 October,
  the founder's order ("Where is version 7? That's what you gotta push everything to"): v6's law, catalog and shared-host
  capacity repair (on kind every node is a container on one runner: its processor is counted once and no replica is
  added while that runner is 75% busy or unread, `omni_controller/capacity.py`), plus conveyance bounded by each
  namespace's CPU quota (`omni_controller/quota.py`; an unreadable quota is no budget known, Kubernetes admission is the
  authority), on a shared host no limit raised while the machine is 75% busy or unread, the verdict reading a trial in
  the reports' words (GAIN, EVEN, LOSS: a clear rise refused), every rule in seconds, the cloud's one flag
  `--give-back-only`. Two repairs first written for the KEDA pod start wait were refused by the model gate and are not in
  it. Its seventeen three-run tables of 17 October (`results/live/V7_*.md`) and its twelve trial runs of 16 October
  (Goldilocks, KEDA's add-ons, fixed capacity, CruiseKube; A, B and C) are its own. **Omni v6** (`OMNI_V6.json`, `docs/OMNI_V6.md`) stood one day, 15 to 16 October; its four
  three-run tables are its own.
- `OMNI_V5.json` and `docs/OMNI_V5.md`: the max (`realms/compass_arm_v5.py`, `V5CFG`) on the 1,107-muscle catalog, the
  bone inside every organism with the living body's immune system (V6-V13, `docs/FORMAL_V5.md` section 4: native twins
  of every room, the heat debt, batteries timed for their lines, nothing locked), every muscle its own card
  (`realms/muscle_cards_v5.csv`, 364 muscles, found by `tools/tune_cards.py` on development seeds only and kept only when
  it wins twice and never falls behind native on any seed; inside a body a battery wired by its power keeps the body's
  margins, V14; `docs/FORMAL_V5.md` section 5), the lease's walk back, the tune-down on the dial. v5 is re-declared on
  every engine change while in development. `OMNI_V3.json` (`docs/OMNI_V3.md`), `OMNI_V2.json` and `OMNI_V1.json` stay for their results,
  never up front. Check with `python3 tools/omni_version.py [--commit <sha>]`: it prints omni-v18, omni-v17, omni-v16, omni-v15, omni-v14, omni-v13, omni-v12, omni-v11, omni-v10, omni-v9, omni-v8, omni-v7, omni-v6,
  omni-v5, omni-v3, omni-v2, omni-v1, or what differs.
- The version numbers are bookkeeping so no result is read across engines. When the founder says the engine is final, the
  engine that stands then is published as **Omni-Compass 1.0**; the older fingerprints go to `docs/history` as the road to
  1.0, never as a second product.
- Any change to a rule, gain, guard, preset or muscle makes **the next version**, and every result is run again on it. Never read a result across
  versions. Never change the engine without telling the founder first; telling is not asking (19 October, night): a version
  that passes the model gate with no LOSS lands, and he hears what it changed.
- Three runs: each benchmark runs as A, B and C (`tools/confirm_abc.py`). Every judged row gets one of three
  readings: GAIN or LOSS in all three of our runs (the same sign in all three, every 95% interval clear of zero, the word
  set by the gauge's aim; a resource spent that rose is power given); EVEN, no difference beyond the noise (an interval includes zero: that is the result, say so); the runs disagree (clear runs
  pointing different ways: the test is unstable there, look into it). Never write "confirmed" or "not confirmed"
  (the founder's order of 11 October: nobody outside approved these results); every three-run table says "Run and
  scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
  (`tools/readings.py`).
- Evidence classes: P (physical meter), L (live software), S (our own models). Never present S as proof.

## The seven organisms and the grid

- **Seven organisms** (the founder's order of 16 October): the **spine** (267 muscles, every muscle that sits in all four
  realms, the base every stack runs on as an operating system is the base of every program; `docs/THE_SPINE.md`), the four
  realms (Compute/AI/Cloud 540, Physics/Robotics/Autonomous 404, Energy/Facility/Industrial 480, Distribution/Specialized
  484, each its own families on the spine), the four stacked (1,908, the spine once in each realm's body) and the whole tower
  (1,107 distinct muscles in 70 families, the founder's nine open-source pieces among them: Kepler, Climatik, EAR, CruiseKube,
  Goldilocks, the Kubernetes Power Manager, PEAKS, Adaptive GPU Power Capping, NVIDIA's platform power manager). Every one
  runs native and with Omni-Compass on top of native. The organisms are groupings of catalog rows made in the runners
  (`tools/run_realms_v5.py`, `run_scale.py`, `run_hil.py`, `run_kil.py`), never in a fingerprinted engine file; the spine is
  `spine`, organism 7 in the numbered runners, and listed first on every page. Earlier catalogs' counts stay with their
  results in `docs/history`.
- **The orchestra, an eighth organism** (the founder's words of 19 October, night: "governors and orchestrators in their own
  category or catalog group organism ... benchmark them on the organism native, and then Omni on top of them on top of the
  organism"): every catalog muscle that stands for a knob of the governors and orchestrators he named (the Kubernetes
  scheduler, Kueue, Volcano, the KAI scheduler, Koordinator, CruiseKube, Crane, KubeRay, Gödel, Armada, Karmada, Open Cluster
  Management, KubeEdge, Nephio; the mapping in `tools/governors_page.py`), each governor's muscles a body of its own and all
  of them together one body, native and with Omni-Compass on top, modelled (`tools/run_orchestra.py`,
  `results/orchestra/ORCHESTRA.md`, its A, B and C in `orchestra.yml`); a grouping of catalog rows like the seven, never in a
  fingerprinted engine file. The governors themselves run live on real Kubernetes, each as its project ships it with
  Omni-Compass on top (`kind-orchestrators.yml`, `results/live/GOVERNORS.md`).
- The organisms are named `tower`, `stack` and `spine` in code and workflows (never by a count); the old names `organism_656`
  and `stack_1226` are read as aliases.
- The grid: each organism runs native and omni at clustered copies × runs: 63 squares (seven organisms) at 1, 10 and 100 copies × 1, 10
  and 100 runs, modelled and with the real cluster inside, with both values shown in every square. **On GitHub's own
  machines only, the 1,000 tier stands again** (the founder's distinction of 15 October, `scripts/dispatch_grid.py`,
  `docs/OMNI_V6.md`): the seven organisms and their modelled, Kubernetes, Linux and swarm workloads run at 1, 10, 100 and
  1,000 copies and nested 1, 10, 100 and 1,000 runs on free runners, and a cell beyond a free runner's memory or time is
  listed as pending runner capacity, never rented; **paid cloud and GPU runs stay at 1, 10 and 100 copies with at most
  100 repetitions** (the founder's order of 12 October, kept for everything that costs money). Nothing is rented for the
  grid. Every grid button starts all its sizes × all its run counts and uses every runner GitHub gives. The conductor
  (`scripts/dispatch_grid.py`, `grid.yml` every 15 minutes; the six and six-kube buttons with their defaults) starts every
  run not yet started, reads started runs back from their names, never starts one twice, and keeps the queue at what
  GitHub runs plus a margin; it starts nothing while an Azure run, a grid report or a verify waits for a runner (Azure
  first). It also releases the reruns of every benchmark on the engine that stands (`scripts/reruns.txt`; A of
  every benchmark, then B, then C; a few a tick; read back by count, never started twice; an entry added once the
  campaign is under way goes into a new block at the end, below an `added=<UTC>` line, never among entries already
  started, where it would take a started run's place: 18 October). It starts every Azure set from `scripts/azure_queue.txt` (A of every set, then B, then C; one at a time in each
  machine family's queue; read back by its run's title, never started twice): the steady set, the bursts `1 4 1 6 1 9`
  and `1 6 1 8 1 6`, and the real day (Google 2011) on 1 to 9, every one at the tune-down with native's cap (the founder's words of 14 October; the load generator alone
  reads a schedule, never the governor). Google Cloud and Amazon carry the same four sets from `scripts/google_queue.txt` and
  `scripts/amazon_queue.txt`, each behind its own `switch=` line, switched on by the founder on 18 October once their secrets were in the repository;
  both switched off on 24 October and kept, wired as Azure's sets run, shown everywhere as not yet run (Orders of 24 October; Amazon's
  account on the Free plan, which Amazon would not raise before the $100 credit is spent or six months pass; Google's key not yet
  stored whole), each on again on the founder's word
  (16 October: the Azure run is the measure of the other two clouds, the same tuning, mechanism and harness). Each tick runs the conductor's newest
  code (fetched from the branch). `peek` (`.github/workflows/peek.yml`) prints a running run's finished repetitions,
  paired, so a benchmark is looked at while it runs and a problem fixed before it ends. Shards are cut from measured run times; each stops at its deadline and hands in every run it finished. With
  the cluster inside only runs of protocol 4 count (12 Oct: the governor never below the organism's CPU priority, its
  decisions counted inside the window; 13 Oct: the model of the organism on the runner's last core and the kind nodes on
  the others, the same in both arms; 18 Oct: the served image pulled onto every worker before each arm); a repetition whose
  job fails runs again, up to three times, paired within one run,
  and one that fails three times is listed. With the cluster inside, the window is set from the heavier arm's step,
  timed before either arm, so the max keeps the organism's clock.
- Three loads: each organism's own load, the climb (the load stepping by one, 1 2 3 2 3 4 …) and work waiting in line
  (`LINE`, `realms/harness.py`); every muscle alone runs its own load and the line.
- Benchmark breadth: every domain that can be benchmarked defensibly (`docs/REGISTER.md`), with Omni on top of that
  domain's own native controller, one or two at a time.
- GPU: all old GPU results are obsolete. The founder reruns them on Lambda. Never spend GPU money before the CPU side
  is done, and give the founder one exact commit.

## Honesty

- Report every row, losses included. Never drop a row because it went against Omni. If Omni loses, first suspect our
  own wiring, native setup or scoring; fix that, then rerun. The founder may choose not to publish a benchmark; it is
  never published with rows cut out.
- Preregister before running, freeze the rules on one tuning case, and test on untouched cases.
- "Flake" is not a root cause.

## Legal, on every output

- At the top and end of every output: © 2026 The Omni-Compass LLC; all rights reserved; evaluation and simulation use
  only; any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License; then **all**
  patents, copyrights and trademarks filed in the USA (say "filed", never give numbers), followed by www.omni-compass.com
  and nothing after it (the founder's wording of 10 October: the word "all" before patents and "all rights reserved"
  everywhere; that night he struck two earlier sentences from the notice, and they stand nowhere: no page, header, report,
  license paper or program output carries them, and `tools/legal.py --check` fails any file that does).
- Every export of any part of Omni-Compass (a zip, a report, a table, a PDF, a chat answer) carries the README's notice,
  the LICENSE, the NOTICE and DISCLOSURES.md the same way, written as a multi-billion-dollar company would protect a
  released asset.
- Keep the SPDX headers so Black Duck, FOSSA and Snyk detect the license.
- The notice is written once, in `tools/legal.py`; `python3 tools/legal.py --fix` puts it on every page, header, workflow
  report and export, and `--check` (run by `verify.py`) fails any push where a file lacks it. Engine files locked by a
  fingerprint take the new header only with the next engine version.

## Orders of 15 October

- **The model gate first** (the founder's order of 15 October, night: every fix, knob and rule is tried in a model
  before it is pushed, and goes to a real run only where it shows promise there). Every change to the engine or to a
  live controller runs in our own models (`tools/model_gate.py`: the shipped controller on the model cluster in the cloud
  setting at 60 and 15 s, conveyance on one kind host set to the v6 KEDA run's own regime, the verdict on noisy work)
  against the engine that stands, on the same seeds, paired, read GAIN, EVEN or LOSS by the gauge's aim. A LOSS there
  is root-caused and fixed in the model, never carried into a real run; a change that reads no LOSS and shows promise
  goes to its GitHub trials; nothing is dispatched before. The gate's readings are models (class S), recorded in
  `results/model_gate/` and never presented as a benchmark result. The model's regime is set from a real run's own files
  (the host's busy share, the response time, the replicas), never guessed.

## Orders of 31 October

- **Omni direct keeps every muscle Omni-Compass cannot be** (the founder's words of 31 October, on reading that the arm by itself
  had read like native: "Omni direct is directly to muscles, but Omni direct still might need an autoscaler like Kubernetes ...
  we still might need a muscle or two we're using. We're going straight into all the muscles as the brain and orchestrator,
  scheduler and all that, but what Omni-Compass can't do and needs the muscle for has to be achieved even in direct, so that it
  can work and do everything else ... Don't just embed some shit and fail the whole system because we don't have the muscle to
  do something ... Direct means we directly talk to and receive from the muscle, and give and use all; but any muscle that we
  don't have, Omni-Compass cannot be it: it has to be there, if that's Kubernetes or whatever"). Omni direct means Omni-Compass
  talks to the muscles directly and is the brain, the orchestrator and the scheduler wherever it carries those muscles itself. A
  knob's native controller is switched off in the direct arm only where Omni-Compass carries that muscle and has proven, before
  the window, that it can move the knob; every muscle Omni-Compass cannot be (on Kubernetes the API server, the scheduler, the
  kubelet, and any autoscaler it has no muscle for on that platform) stays, native, under it. A knob left with no working
  controller fails the whole system and is never a result: the kind rig refuses a window of the arm by itself in which any
  decision of Omni-Compass failed (`scripts/kind_bench.sh`, `docs/SOLO_PREREGISTRATION.md` amendment 2,
  `tests/test_kind_rig_rbac.py`); the engine's own answer, a knob whose writes are refused handed back to native's controller so
  the organism never runs with a hole, is the next version's guard, through the model gate. Found the same day (amendment 1):
  every arm by itself since 24 October had its pod writes refused by the rig's own identity (the scale subresource was not
  granted) and ran with no controller on the pod count; omni-v21's three runs of it and omni-v22's two are void, read in no
  table, the entry queued again on the amended rig.
- **Every fix pushed, the website following GitHub, the live engine defensible in line** (the founder's words of 31 October: "push
  all the fixes into GitHub, so that the files in the GitHub are updated ... the live engine and all has to be 100% defensible in
  line"). A fix is pushed to main as soon as its release check reads PASS, the kept branches levelled with it; the website follows
  main's head; the live engine page on main is rebuilt by the repository's own code from the engine that stands, and every push
  is read on GitHub's own verify before it is called done.
- **"Direct" means becoming the mechanism; on Kubernetes no arm is direct** (the founder's analysis of 31 October, afternoon:
  "Omni-Compass is only a brain. It has no organs ... Only Compass would have to become the Kubernetes mechanism to be what's
  considered direct"). On a Kubernetes stack Omni-Compass is a brain with no organs: the scheduler places every pod and the kubelet
  runs every container in every arm, so Omni-Compass can be direct to a knob there, never to a muscle. The arm by itself on
  Kubernetes is Omni-Compass's own pod rule in place of the autoscaler's arithmetic and nothing else; it is never called direct, it
  is a mechanism test kept in the record, and the product has two sides (the order of 25 October). The one test where the word
  holds is the orchestrator showing without Kubernetes, where Omni-Compass's own small orchestrator is the organs; its third arm
  read nothing better than Omni-Compass on native (work LOSS by the mean of its three runs) and stays in the record. Every page and
  manual names the arm so (the Operator's and Owner's arm tables, `docs/OMNI_ORCHESTRATOR.md`, `docs/OMNI_V23.md`,
  `docs/SOLO_PREREGISTRATION.md` amendment 2).
- **Each run's own word stands by itself** (the founder's words of 31 October: "A gain in any run in itself is a gain ... Each one
  is independent and says whatever it says within itself"). Every run's cell carries that run's own word on its own number, as the
  one key of 24 October already reads it; the three-run column is the mean's word from half a percent up, "in all three of our
  runs" only a note on its strength, never a condition; in prose a result is said run by run (run A GAIN, run B GAIN, run C GAIN,
  the mean GAIN), never as "a gain only if all three agree".

- **No hard rule; the cloud at the max** (the founder's words of 31 October: "Why is there any hard rule written ... Whatever the
  math does and falls out is whatever happens. All we need to do is tune up what the math does to the best way we can and let
  whatever falls out fall out. And when it falls out wrong, the tuning is wrong"; and, on the cloud: "What I care is to make the
  cloud the best it can be with Omni-Compass in it, as well as on site with Omni-Compass on it, and we have to sit and tune and
  tweak both scenarios"). The cloud's rule of 14 October (the tune-down on the machines alone: `OMNI_MACHINES_ONLY=1`, `dial save`,
  the governor's `--give-back-only`, "nothing in a cloud adds a machine") is struck. Every cloud set runs the whole engine at the
  max, every muscle, on top of the cloud's own autoscaler (native's machine controller, which stays in every arm and alone adds
  machines; the lever parks and wakes what exists and asks the cloud for none, `scripts/kind_nodepool.sh`); the bill is judged
  beside the work by the one key, a service gauge with its aim lower: a tune that raises it is not admissible (`docs/THE_TUNE.md`),
  so "never raise its bill" (18 October) holds by judging, not by tying the engine's hands, and a bill that rose is a fault of the
  tune, root-caused in the model first. The two scenarios, on site and in the cloud, are the factory profile's declared operating
  conditions, each tuned through the tune study. In code: every cloud workflow's dial defaults to `max` and sets no machines-only
  switch, every `scripts/*_queue.txt` entry reads `dial=max` with the replica room read live as on kind, the rig wires the same
  muscles on every platform (`scripts/kind_bench.sh`), the model gate's cloud setting is the max (`tools/model_gate.py`), and
  `tests/test_cloud_at_the_max.py` holds it; the governor's own `--give-back-only` flag, an engine file, leaves with the next
  version. The Azure sets started before this order (omni-v18's steady set; omni-v21's, 25 of 100 repetitions on 31 October) finish
  as the tune-down's record; the sets at the max start as their own A, B and C (`docs/K8S_COMPASS_PREREGISTRATION.md`, the
  amendment of 31 October) once the cloud's tune is admissible in our models. In the cloud the aim is more work for the same
  bill (the founder's words of 31 October: "We never make the bill smaller ... they're looking to do more work with the money
  they're spending"), and on omni-v23 at the max the model reads the machine-hours, and so the bill, up 9% to 35% across the
  beats (14% at 60 s; `results/model_gate/V23_LADDER.md`, class S): Azure's queue is held (`switch=off`) until the version whose
  cloud tune holds the bill lands, and nothing is cancelled. Paid cloud and GPU runs stay at 1, 10 and 100 copies with at most
  100 repetitions.
- **The factory setting is found, then locked; the knobs are for seeing it move** (the founder's words of 31 October: "We'll have
  all these buttons that allow people to ... change it to see what happens when things move ... nothing breaks, it'll just change
  all these metrics ... we are going to find the most optimal state in every scenario with Omni-Compass, and then we will know
  that that's the setting, and we will lock the engine in that scenario ... When everybody buys a car, the engine's already tuned
  and running ... that is what we're attempting to get: the factory settings to the best"). The order of 24 October (one factory
  profile, found and then frozen; the live engine its tuning bench) stands as he restated it. The factory beat is read again on the
  engine that stands (`docs/PACE_PREREGISTRATION.md`, amendment 4, the pick rule written before the run): on omni-v17's ladder
  10 s read strongest on the service against 60 s (the kind setting: the minutes over the line down 18.4%, pods waiting down
  9.9%, machine-hours down 1.4%; 20 s: 14.7%, 6.8%, 0.8%), a reading of an engine that no longer stands, so the pick is made on
  omni-v23's ladder; 60 s, set on 22 October for the reads of the cluster, is one setting of the dial like every other, and the
  beat that reads best lands as the next version through the model gate, told, not asked. Read the same evening
  (`results/model_gate/V23_LADDER.md`, class S, seeds 101 to 108, the plant with the cloud's own autoscaler at the max, which is
  the cloud's setting and the kind setting at once): on the service 10 s reads best (against native pods waiting down 16%,
  the 95th percentile down 30%, the minutes over the line down 58%, all GAIN; 20 s waits more pods than 60 s, LOSS), but every
  beat buys machine-hours (up 9% to 35% against native, 14% at 60 s): the governor asks for pods ahead of the load and the
  cloud's autoscaler adds machines for them. In a cloud that is a bigger bill, a benefit with a cost (the founder's words of 31
  October: the chip and the cloud are the cost proof), so by the rule written before the run no beat qualifies there and 60 s
  stays until the tune itself holds the bill (the next version, through the model gate); the on-site beat is read on the kind
  rig's own fixed machines, a plant of its own, before it is picked.

## Orders of 24 October

- **One factory profile, found and then frozen; the live engine its tuning bench** (the founder's words of 24 October, late night:
  "once every knob is tuned for every organism ... lock that as its package tuned one setting system engine ... anybody can tweak
  and turn anything ... We ain't got to the basic yet. You just keep building it right, and we will sim it sooner or later once I
  know all the mechanisms are right"; then his master specification, the same night). The common language is written once,
  `docs/FACTORY_PROFILE.md`: the governing engine, its muscle adapters, the complete configuration profile and the validation
  harness; the factory, candidate, active and custom profiles; the mathematics of a fixed tune governing a changing system
  (θ(k + 1) = θ(k) = θ_factory while x, z and u change); the two objectives (the most healthy production; the least cost per
  unit of completed production); the eight steps that establish **the best validated factory profile for the declared operating
  conditions**; the contract every implementation (Python, C++, the browser) shares; and the two restoring controls, Restore
  factory profile and Return to native. No profile is locked as the baseline before those steps: the released factory profile
  (omni-v19's) stands, the live engine names the active profile (factory, candidate or custom, with its fingerprint), and a
  candidate is evaluated, never released, until it is validated and declared.
- **Red only as a stop sign** (the founder's words: "That red sign is never to be a circle. It is an eight stop sign shape
  octagon ... The yield is the diamond ... the circle is green only everywhere it lives"). Every red light and red mark is an
  octagon (a red word is shaped as a stop sign, white on red), every yellow one a yield diamond, every green one round, on every
  monitor, badge, breaker and canvas (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`).
- **Six heartbeat buttons: 10, 15, 30, 60, 90 and 120 s** (the founder's words: "We need that 10 because we need to show less
  than what's already standard"). The factory's beat stays the engine's own until the sims and the founder choose the next.
- **The bill is the sum of the costs** (the master specification): for each deployment route, on site and through the cloud,
  C(r, a) = Σₖ c(r, a, k) inside the declared boundary and S(r, a) = (C(r, native) − C(r, a)) / C(r, native); a component's
  percentage is a supporting measurement; a missing price or an incomplete workload stays visibly unresolved.
- **Every change of 0.5% or more is a change** (the founder's words: "Any gauge that gives anything over a 0.5 percent change
  either way is a change. I don't want to see even on shit that shows a 0.5% change up or down ... Not everything can just stay
  even ... because it's 2-3% away. That's not even"; and "You have to interpretate the muscle and what it's doing to know if a
  gain is a benefit or a minus is a plus"). The one key (`tools/readings.py` `three_run_reading`): the change is the mean of the
  three runs' changes in percent of native; from 0.5% up it reads GAIN, LOSS or power given by what the gauge is for, "in all
  three of our runs" where every run moved the same way clear of zero, otherwise "by the mean of our three runs" with the count of
  runs beyond the noise; EVEN is kept for a mean under 0.5% (EVEN, under the floor) or no change at all; runs that moved 0.5% or
  more in opposite directions read "the runs disagree"; a count that must never rise has no floor. Each run's own number wears
  that run's own word. Every table was read again from its own data by `tools/reread.py` (24 October: 4,037 readings in 194
  tables; the index's headline GAIN, up 3.4%), the model gate reads by the same floor, and the live engine's own key with it.
- **The immune system catches a LOSS under Omni** (the founder's words: "the only way anything can show a real loss would be ...
  Omni direct or native by itself. Everything else with Omni in it ... has Omni-Compass's mechanism of immune system and pathways
  ... that should have pushed signals when something is in its in a negative state, and adjusted ... like any human body"). A
  muscle whose own markers turn against native (pods waiting, a response over its line, failures) sends its signal to the muscle
  that caused it, and that muscle backs off toward native: the next version's work, through the model gate (first: the autoscaler
  target never asks for more pods than the machines can place while pods wait, the pods-waiting LOSS's root cause).
- **The live engine in the order a watcher needs it** (the founder's words of 24 October): the page, its contents and its
  instructions laid out by importance to the operator watching the system, first to last; on every monitor of Omni on native a
  switch that turns native off and leaves Omni direct on the organism with no other governor; live knobs, buttons and switches on
  every muscle that can scale out, up or down, each acting on the running code; buttons that run another set of the Python's 500
  runs (and the C++ harness's) from a new seed; and the page wired to a live governor through the control API
  (`tools/omni_control.py`), so a system owner can hook a system up and watch and drive it from these monitors.

- **Google and Amazon kept in, wired as Azure is, shown as not yet run** (the founder's words, the same morning he had ordered
  them taken out: "You leave the Google and Amazon runs in everywhere and just show it not ran yet, because someday, some way,
  I'm going to have it run and put in here ... It's got to be built everywhere as a mechanism, the code, regardless if we run it
  or not, and code it to wire it the same way that the Azure is running"). The removal of that morning was built here and never
  pushed; it is undone whole. Every Google and Amazon workflow (`gke-metered`, `eks-metered`, `cloud-organism`), paired script,
  queue, machine tool, setup page, $0 check, manual chapter, live page monitor and page mention stands, wired as Azure's sets run
  today: the same harness (`scripts/kind_bench.sh` in its managed-cluster mode, the main engine's 60 s beat), the whole engine at
  the max from 31 October (the tune-down on the machines alone until then), 100 paired repetitions a set under the preregistered
  stopping rule (`stop_looks`, `tools/stop_rule.py`), the $0
  check before any set. Both queues read `switch=off`, so the conductor neither checks nor starts anything for them; every page,
  board row and monitor reads them "not yet run". On the founder's word a queue's switch goes on (Google once its key is stored
  whole, Amazon once its account is on the Paid plan) and its sets start behind its own check. The engine, Python and its C++
  twin, names no cloud: the same governor runs on every one; what differs per cloud is the wire to it (the workflow, the paired
  script, the queue and the key check), and those are what stand ready.
## Orders of 23 October

- **Omni-Compass by itself, and on top of native: both, and both to the best** (the founder's words: "Within the native, we do
  whatever the native can be pushed to. And in our own, with no goddamn Kubernetes, we have our own Omni Compass ... We're gonna
  push it to the best with Omni Direct. We're gonna push it to the best with Omni on a native"; "the way you're writing this
  should be making OmniCompass better when it's on top of the native, as well as by itself on the organism as the orchestrator,
  replacing Kubernetes and whatever other managers, orchestrators in the system that OmniCompass is able to become"). Omni's own
  orchestrator (`omni_orchestrator/`, `docs/OMNI_ORCHESTRATOR.md`) is built from scratch, no orchestrator's code in it, and read
  against the yardstick (Kubernetes' published autoscaling rule, written by us) by the one key; every mechanism it gains is the
  engine's own (conveyance, the verdict, the reflex, the compass law) so the same gain goes to Omni on top of native. Every
  level is benchmarked on its own (nothing paid for with another), then all joined and benchmarked whole.
- **The brain finds the win; nobody turns a knob for it** (the founder's words: "the brain should have fucking wired it out";
  "it's supposed to be built in omnicompasses mechanism, defensive system, immune system, nervous system, pathways of signals
  moving through ... it should react with the same benefit ... Unless by taking less can show more, or vice versa"). A result
  that reads EVEN where the organism has room is a mechanism not yet wired, found in the files and wired (23 October: the
  response time was the unit's own paper quota, not a shortage of units; the engine's conveyance gives the unit the processor
  its machine can spare: faster, with no unit and no machine added). The win is said only when the run's own files read it.
- **Where a LOSS may ever be seen** (the founder's words: "Nothing should be shown as a loss because it would have been fixed
  and never gone there. The only way we're going to ever see a loss ... is in the live engine when people turn knobs and turn
  and tweak it to a point that fucks it up ... and that's the only benchmark proof that needs to be"). The factory tune reads
  no LOSS anywhere; a LOSS found in our own runs is a fault, fixed before anything is published, never shown as a result. The
  live engine's knobs (the dial, the heartbeat, the sizes 1, 10, 100, more or less load) exist so a person can see the system
  react, break it by hand and watch the brain hold or recover: that is the one place a LOSS is ever shown, as the proof that
  the factory tune is the best state and that the mechanism can be broken only by leaving it.
- **A reading leads with the word, never the sign** (the founder's words: "a loss can be a gain and a gain can be a loss
  depending on ... don't because it's minus and plus"). Every reading to the founder and on every page is written as the word
  first, then the direction in words (down 4.8%, a cut, GAIN), never a bare signed number.
- **Every tool to strengthen the engine** (the founder's words: "all you got in access to in libraries kits formalization tools
  all of the open source mechanisms on everything you can learn and figure and find and build and give me and strength in Omni
  compasses engine"). Anything available that strengthens the mechanism or its proof is used and named; nothing is built from
  another orchestrator's or governor's code.
- **Nothing is pushed until the founder says so** (23 October: "Don't push nothing"; "I don't want you to push shit until I
  tell you"). Work is built, run and shown here; the push waits for his word. His word came the same evening: "Native is
  Kubernetes on the muscles. Omni on native is Omni on top of Kubernetes on top of the muscles. And then Omni direct is simply
  Omni on top of the muscles, no Kubernetes ... they all need to be written in code ... put into the GitHub and push it all";
  then "Update, push, push, push in the bush". The three arms are always shown together (native, Omni on native, Omni direct;
  `omni_orchestrator/`, brains `yardstick`, `omni_native`, `omni`), and the push hold is lifted.
- **Omni-Compass by itself, the third arm** (the founder's words: "we're going to be expanding out a whole nother omni-compass by
  itself without any Kubernetes or any schedulers or any governors running direct muscles ... there's native, there's Omni and
  native, and then there's Omni by itself ... the one that said Omni before is going to have to add the word and native"). Every
  organism is shown three ways: native; Omni-Compass and native (the arm every table carried as "omni", its machine key unchanged);
  Omni-Compass by itself, each muscle's own native controller switched off and Omni-Compass the only controller moving that knob (on
  Kubernetes no pod autoscaler and no cluster autoscaler; Kubernetes' own scheduler and kubelet stay; where native is a setting rather
  than a controller the two Omni-Compass arms are one arm). Preregistered before any run (`docs/SOLO_PREREGISTRATION.md`); the engine
  that carries it (a pod muscle of its own, the models' arm with the pool's autoscaler off) lands as the next version through the model
  gate, and its runs go to GitHub's machines, three runs, read beside the other two. No cloud by itself without the founder's word
  (the order of 14 October, nothing in a cloud adds a machine, was struck on 31 October; a cloud by itself still waits for his
  word). The pages and the words say the three arms; the third's column appears
  from its first run, nothing written for it before.
- **The live engine is the operating control panel** (the founder's words: "build a live engine's mechanism, interpreting what it
  sees, as well as giving it knobs and buttons ... in every canvas section block ... every monitor needs to have a light in it ...
  gauging a couple percentage before ... there has to be a main button that puts it back"). Every monitor carries a light that reads
  the series it draws: green inside its lines, amber before the line (within 3% of it, or its own slope over the last readings crossing
  it within three readings), red over it, grey and said so where there is no line; the wall counts them and prints the engine's own
  last act beside them, because the brain reads the same slope and acts before the line. One button, on the console, the dock, the
  wall and every monitor's knobs, returns every knob to the factory tune and says what it put back; native alone stays the kill switch.
- **The sign explained where the number sits** (the founder's words: "you cannot just put minus 29 gain or down 29% and then say gain
  ... you need to now explain that wherever things are"). A number beside a word wears the word's sign (the order of 22 October), and
  wherever it stands the reason stands with it: on the live engine every word and size carries it on hover, and the key says it once in
  full ("How to read a number beside a word"); in prose a change is said in its verb with its reading ("pods waiting down 29.6%: fewer
  waiting, GAIN"), never a bare sign beside a word.
- **The factory beat is the best beat the sweeps read** (the founder's words: "whatever is the best one out of all that helps the best
  system is the factory set one ... I think 45 you didn't try"). The main engine's beat is whichever the ladder reads best by the key
  on the organism's gauges, not a number chosen for a reason of its own; the beats the ladder has not read (45, 40, 50, 20 s) are
  read in the model on the side first, and a beat that reads best lands as the next version through the model gate. The knobs stay for
  anyone to turn. Read the same evening (`results/model_gate/V17_LADDER.md`, class S): against 60 s in the kind benchmark's setting the
  minutes over the line GAIN at 20 s (+14.7%) and 40 s (+13.2%), EVEN at 45 and 50 s, every other gauge EVEN, the reads and the
  governor's own processor power given; in the cloud's setting every gauge EVEN. 60 s is not the beat that reads best on the service.
- **A LOSS at the factory tune is a fault to fix, never a number to accept** (the founder's words: "nothing should be shown as a loss
  because it would have been fixed and never gone there. The only way we're going to ever see a loss is ... when people turn knobs").
  Every LOSS row is still shown (Honesty); each one on the engine that stands is on the next version's list with its cause, and the
  live engine's knobs are where a reader may break the engine and watch it break.
- **Omni-Compass at every level** (the founder's words: "OmniCompass can go in the software side, in the hardware bare metal side ...
  in the brain ... in muscles itself ... into a chip ... every level of mechanism"). Its own muscles, built from the ground up with the
  compass's mathematics inside (a pod autoscaler of its own first), beside the open-source muscles it governs, each benchmarked native,
  with Omni-Compass on top, and by itself, and all of it together: the next versions' work, each through the model gate. A licensed
  mechanism is never copied; an interface a project publishes (the Kubernetes API) is talked to, as any client does.
- **Red and green on every monitor; every variation a knob; the live engine the real engine** (the founder's words of 23 October,
  night: "Every monitor is to have a red and green button as red is alert ... green has got to be good ... knobs, buttons that allow
  you to switch amongst all the different organisms ... direct, native, Omni on native ... 1, 10, 100 ... A, B, and C runs ... 5
  seconds ... 45 ... 120 seconds in the heartbeat ... buttons to run multiple Python hashtag jump generator run variances ... physical
  buttons that show these reports in some form of PDF ... for CTOs ... boards and all the CFOs"). Every monitor's light is a button
  in three colours (green working, yellow heading for its line or EVEN on a record, red an alert; the founder's word of 24 October:
  "Yellow would mean it's even"), native's side and Omni-Compass's apart where a monitor draws both, on the page and on the Grafana wall; one switchboard sets the arm, the organism, the
  copies, the runs, the run letter and the beat on every monitor that carries that variation and names the ones that do not; the
  Python's runs can be run again from the page (another 500, and variants on the tuning set's knobs) and on GitHub; the reports for
  engineers, CTOs, boards and CFOs print from the page, every reading by the one key, every number with its run's number (#run).
  Whatever the page computes is the engine's own code and says its class; nothing on it is written as commentary.

## Orders of 22 October

- **One tuned engine, and a tuning bench; the main tune found, not guessed** (the founder's words, the night of 22 October: "what
  the live engine is versus the main ... benchmark engine is two different things ... the real benchmarks that we're showing are
  proving a one set tuned engine ... and must explain and disclose that any turns and tweaks of knobs can change all metrics in
  any form"; "like any regular engine, carburetor to intake, outtake to pistons, to fires ... to show the versatility of an engine
  that can be put in many vessels, tuned many ways, achieve many outputs"; and "the main engine ... is the most tuned engine in its
  most optimal state that you will go through and find and confirm"). Every benchmark is the main engine at its one factory tune;
  the live engine page is a live tuning engine (every knob, button and monitor turned in real time, native alone, Omni-Compass on
  top, or both), whose readings at any other setting show the engine's range and are never a benchmark result; every page says
  that turning any knob can change every metric in any direction (`DISCLOSURES.md` section 3, the README, the live page's first
  box `#tuningBench`, all three manuals). The factory tune is chosen by a declared rule (`docs/THE_TUNE.md`, the Owner's Manual
  section 4.4, `tools/tune_study.py`): admissible = no gauge reads LOSS against native (in a cloud no rise in the bill); the
  factory tune stands when no admissible tune searched dominates it (against it no service gauge LOSS, one GAIN); searched
  on development seeds (101 to 108), read again on the gate's untouched seeds, landed as the next version only through the model
  gate; the claim is non-dominance in the tunes searched, never a global optimum. Every new search widens the grid (the cruise
  wait, the trial, the dwell in readings, each muscle's card at each beat).
- **The heartbeat a dial; the main engine at 60 s** (the founder's words, the afternoon of 22 October, once he had read the reads a
  day in the pace study, about 86,000 at 5 s against 39,700 at 60 s: "who knows if maybe the purpose is somebody wants to set it at 5
  seconds ... I know why we have to scale out 5, 15, 30, 60, 75, 90, 120 ... Heartbeat scaled in its monitors. And you're going to
  set OmniCompass is main engine"; and before it: "we are going to write the engine to have the 60 ... we have to actually have to
  be able to show the same 15 second beats"). omni-v17 (`docs/OMNI_V17.md`): the main engine takes its full decision every 60 s; any beat can be set
  (`--interval`, 5 to 120 s and every value between); every beat is shown beside native with what it buys (its reads of the
  cluster) and what it costs (its own processor, and every service row against native and against 60 s), in our models
  (`results/model_gate/V17_LADDER.md`), on the live engine page (section 1j, "The heartbeat dial") and in its real runs
  (`docs/PACE_PREREGISTRATION.md`, amendment 3: eight arms, native and 5, 15, 30, 60, 75, 90 and 120 s). The monitors scale with
  the beat: the exporter serves the beat the governor runs at (`omni_heartbeat_seconds`), the governor's Grafana screen counts the
  time since its last decision in beats, and the staleness alert fires after three beats at any setting. The engine "can always be
  tweaked, tuned, and turned with any knob, any button"; at each beat the other knobs may want their own combination to reach the organism's
  best state, and that per-beat tuning is the next study, in the model first (each beat's combination lands as a version only when it
  reads no LOSS). Nothing is read across beats as one result: every beat is its own row beside native.
- **The heartbeat at 15 s, "all over"** (the founder's words, once the pace models had read: "15 seconds back to, instead of 60
  seconds in the clock, the heartbeat"; "15 sec all over heart beat fix update code"). Who set 60 s: we did, on 26 September, with
  no reason recorded; native's pod autoscaler checks every 15 s by the Kubernetes project's default. omni-v16 puts every clock in
  seconds, so the pace changes only how often the governor looks, and sets the full decision every 15 s everywhere, the fast checks
  every 5 s. A longer period is not a bigger cushion: it is a longer blind spot (his question of the same night, answered so). The
  pace runs (`docs/PACE_PREREGISTRATION.md`) read 15 s for real, against native and against 60, 10 and 5 s; a LOSS at 15 s there
  is root-caused and fixed in the next version. The same afternoon the dial above replaced it: omni-v16 stood at 15 s from the
  morning's landing to omni-v17's, and 15 s is now one setting of the dial, read beside native like every other.
- **The heartbeat as a knob on the wall** (the founder's words, the same day: "5, 15, 30, 60 ... Then give me 75 90 And after 90,
  I want 120 ... Heartbeat sweeps. With buttons in my monitor canvas dashboard of that wired mechanism of the heartbeat ... Maybe
  somebody wants to pick a different one ... somebody might want to tune it to be something different"). The heartbeat sweep
  (`tools/heartbeat_sweep.py`, our own model, class S; the record `results/model_gate/HEARTBEAT_SWEEP.md`, written again from its
  runs by `tests/test_heartbeat_sweep.py`) reads the engine that stands and the one before it at every beat from 5 to 120 s,
  on-site and in the cloud. Each beat is read against native and against the same engine at 15 s and 60 s, with the engine's own
  cost and the fast check's rescues (a machine added only after a pod waited). The live engine's monitor `beatCv` (section 5c,
  after the heart) has a button for each beat, setting, engine, zero line and gauge. The factory's beat is the main engine's 60 s since omni-v17
  (the dial above); another beat is a changed tune, its receipts its own. On omni-v16 (our own model, class S): on-site every beat reads GAIN against native in
  pods waiting (GAIN +83.5% at 5 to 15 s, +72.9% at 60 s, +57.0% at 120 s), at 5 to 15 s with about 3% more machine-hours (power
  given +2.9%); a beat slower than 60 s waits more than the factory's 15 s (86% to 160% more, LOSS at 90 s) for at most 0.4 points
  fewer machines than 60 s, and the fast check's rescues rise from none at 15 s to 3 a day at 120 s. In the cloud, the machines
  alone, 5 to 15 s cut the machine-hours 1.5% to 1.8% (GAIN) with pods waiting +15% to +17% (LOSS, the engine's, on the next
  version's list, as omni-v16's own pace study found); from 20 s to 120 s the waiting reads EVEN and the cut 0.7% to 1.4%.
- **The number beside a word carries the word's sign** (the founder's words, 22 October, night: "If it's a gain, it should be a
  plus 73 with the word gain. When you put a minus, it confuses me ... that word gain can never have a minus beside the word
  gain"; the key's own rule of 20 October, said again). GAIN +, LOSS −, EVEN =, power given +: "+73.0% GAIN", "−16.8% LOSS",
  "=0.9% EVEN"; an interval beside GAIN or LOSS is its two sizes with the word's sign ("+47.3% to +127.5%"), beside EVEN as it
  lies. The heartbeat monitor had printed the gauge's raw direction ("−73% GAIN"); the key's formatter (`tools/readings.py`
  `by_word`, `interval_by_word`) now prints every number beside a word in the three-run tables, the receipts, the model gate, the
  heartbeat sweep and the live engine's trading floor, index, verdict and heartbeat monitor.
- **The beat, read right** (the same night: "73% gain means you're gaining more pods waiting ... Answer the question").
  No: down 73% at 60 s means 73% fewer pods waiting than native, down 87% at 15 s means 87% fewer; both GAIN, 15 s the
  larger. Native keeps its own 15 s autoscaler in both arms, so the benefit is not the beat: it is the governor sizing
  the pool ahead of the load, where native's autoscaler adds a machine after pods wait; the beat sets only how often the
  governor looks. The factory's beat was 15 s on omni-v16 and is 60 s on omni-v17 (the dial above). A beat shown to make the engine do too much work for
  nothing (120 s) is kept on the monitor only to show why nobody would tune there; no run is spent proving it further.
- **The page's order** (the same night: "my TOC is in order of comprehension ... there's too much shit before people see
  some metrics ... the real monitor wall ... got to hit them right away"): open order; the founder goes through the
  contents next.
- **Another person's cloud account** (the founder's words: he logged into another person's Azure account to use their free credit
  for his benchmark). A key bills only the account it belongs to; nothing merges. Using it is his and that person's matter: only
  with that person's agreement. Asked whether they agreed, he answered "Yes yes yes" the same day: the Azure queue's switch, off while the
  question stood, is on again (`scripts/azure_queue.txt`), and each set starts after Azure's own $0 check passes.
- **The conductor's engine check** (under the order of 18 October that every fault is fixed): from omni-v15's push (00:45 UTC on 22
  October) to the afternoon the conductor started nothing. On GitHub it fingerprinted the fetched commit with its own copy of the
  version tool's scope, which predated the eight wires omni-v15 took in, so omni-v15's and omni-v16's commits matched no version.
  It now runs the fetched commit's own version tool on that commit (`scripts/dispatch_grid.py`, `engine`), and
  `tests/test_release_campaign.py` fails the old code. No copy of a rule kept in two places.

## Orders of 21 October

- **Push, push, push; the enhanced engine** (the founder's words: "Back to work push push push on GitHub update enhanced engine"):
  omni-v15 landed the same evening by the standing rules (the fault from the next version's list, the model gate against omni-v14
  first, no LOSS, told, not asked): the brain's power-cap request through the line's own clear time and every wire in the
  fingerprint (`docs/OMNI_V15.md`). What the gate refused (a dwell with a glide) is written on the same page and is not in it.

- **Azure behind its own $0 check** (22 October, under the order of 18 October that no set's A, B or C is spent on a login):
  for a while on the night of 21 October the stored `AZURE_CREDENTIALS` held a text Azure's login refuses (not the JSON block of
  `docs/AZURE_SETUP.md`, section 3): the collect of 23:37 UTC failed at the login, and by 00:00 UTC the block was whole again
  (the steady set's next repetition logged in). A failed Azure set counts as started, and Azure had no check before it. The
  conductor now starts an Azure set only after `cloud-check azure` passed (the key's shape, the login, the subscription, the
  machine and its allowance; nothing built), as Google's and Amazon's; every Azure login reads the key's shape first
  (`tools/cloud_key_check.py azure`), because Azure's own login step quoted the stored text's first characters on a public run
  page while refusing it. Section 7 of `docs/AZURE_SETUP.md` is the founder's steps if the key is ever stored wrong again.

- **The problem and the answer, first** (the founder's words: "in the beginning we have to state in front matter the problem
  and omnicompasses solution, what the whole tech world is facing, and how omnicompass addresses it"). The README and all three
  manuals open their front matter with "The Problem and the Answer" (the book builder prints it first): what every stack faces
  (capacity held idle, late reaction, loops at cross purposes, demand outrunning power and hardware), what Omni-Compass does
  about it (on top of native, never replacing it), where the proof is (the Owner's carries the record; the Operator's points
  to it), what is not claimed, and what is protected. It is held to the honesty rules like every page: no claim beyond the
  record, no outside review implied, no equation that is not the engine's.

## Orders of 20 October

- **The governors four ways** (the founder's words: "We can show what they do natively on top of the system organism. And
  show what OmniCompass does on the organism without the orchestrator compare that. As well as put OmniCompass on top of the
  orchestrator that's on top of the whole organism and benchmark that"). Each governor and orchestrator runs with the organism
  alone (nativebare), the orchestrator as shipped (native), Omni-Compass on top of the organism alone (compassbare) and
  Omni-Compass on top of the orchestrator (compass), all four in every repetition, each comparison paired within it and read by
  the one key (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 6). Omni-Compass never replaces the orchestrator: on the
  organism alone it sits on top of Kubernetes' own scheduler. On the batch rig the governor has its own core and the kind
  nodes the others, in every arm (amendment 5), as it has its own machine on a real cluster.

## Orders of 19 October

- **Every fix lands as the next version, told, not asked** (the founder's words, the night of 19 October: "Of course I want you
  to land a version 12. I want you to keep fixing and building and straightening and enhancing and benchmarking and
  defensibility, and every time you do that to a new version, it becomes a new version ... What you asking me"). A change to
  the engine is built on its own branch, tried in the model gate against the engine that stands, and, when it reads no LOSS,
  landed at once with `tools/land_engine.py`: the fingerprint, the words on every page, all three manuals, the manifest, the push,
  the branches leveled and every benchmark run again on it. The founder is told what changed and what it read, never asked
  whether to land it. A change that reads a LOSS in the gate is fixed in the model first, or kept on its study branch with the
  reason written (`docs/CHANGE_CONTROL.md`).
- **Nothing is forced but the mechanism** (the founder's words: "We don't force anything. The only thing we force is the code
  and the mechanism and the correct mechanism. Because once the correct mechanism is enforced and wired correctly, it will do
  the physics and the math will do the work"). A result is never pushed toward GAIN: no number is tuned to make a row read
  well and no row is steered. What is held to the letter is the mechanism: the code does what its rule says, the wire is
  fastened right, the harness measures as a deployment runs. A LOSS is answered by finding where the mechanism or its wiring
  is wrong and correcting that; the runs then say what the corrected mechanism does.
- **Do no harm means the organism** (the founder's words: "its real goal is to strengthen the organism and keep it healthy
  in any form and keep it working in its most optimal state that the organism can live within its own muscles ... If that
  means decreasing a muscle to push another muscle, but in the whole end makes the organism produce a better output, well,
  that was the goal in the beginning, is the output ... You make sure in the terminology in the live engine's content and
  disclosures that's how do no harm is meant to mean"). Its meaning is written once, in `DISCLOSURES.md` section 3, and the
  key (`tools/readings.py`), both manuals, the README, the safety case and the theory carry it; the engine that stands
  keeps its strictest form, and the engine's own words and the trade between muscles come with the next version, through
  the model gate.
- **Every cloud set gets its three-run reading, to the cap** (the founder's words: "I need a 3-run result ... the cap we can
  run it to ... that's all we can run ... do all, give all, make it the best you can"). Every Azure set runs up to 100 paired
  repetitions a run (the paid cap of 12 October) under the preregistered stopping rule (`tools/stop_rule.py`; looks at 10,
  20, 40 and 70 with 99% intervals; it stops once the bill is read, never on a LOSS), counted apart by its title from the
  runs at 5 repetitions (`docs/K8S_COMPASS_PREREGISTRATION.md`, 19 October). Both arms at once on twin clusters waits for
  Azure's processor allowance for the machine family to be raised to 20.

## Orders of 18 October

- **Fix everything, and keep building, version after version** (the founder's words: every fault is to be fixed; and
  "at some point ... version 10, 20, 30, 40 for all I know ... keep updating and moving and tightening and coding and writing
  and building along the way to the full final destination organism ... leaving everything intact, only upgrading what keeps
  moving ... It has to live better than it did natively ... We can't make an organism live great for one day and die the second
  day"). No fault is set aside: each is root-caused and fixed, in the rig or, through the model gate, in the next engine version.
  A version lands with `python3 tools/land_engine.py vN --since <UTC>` (the fingerprint, the version list, the conductor's
  campaign, the grid's manifest and workflows, the package, the root list, a release group), then the words a person writes;
  `tools/land_engine.py --check`, run by `verify.py`, refuses a push where any of those places still names an older engine.
  The real GitHub is brought up to the newest work every few hours.
- **The kind rig pre-pulls the served image** (18 October, `docs/POD_START_WAIT.md`): the only LOSS row on the engine that
  stands, the KEDA HTTP pod start wait, is the test machine (an empty node unpacked the image inside the window on the one
  runner all kind nodes share; at the same host load omni's starts were as fast or faster). Every kind arm now pulls the
  image onto every worker before it begins, the same in both arms; a kind run counts only on a commit that carries the
  pre-puller (`RIG_FILE`); the grid's runs with the cluster inside are protocol 4; and `tools/confirm_abc.py` marks a table whose runs differ in rig.
- **Google and Amazon on** (the founder's words, once the four secrets were in: "Push the clouds, let's see. The Google
  AWS, I linked them up"). `GCP_CREDENTIALS`, `GCP_PROJECT`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are in the
  repository's secrets; both queues' `switch=` lines read on. The conductor starts their four sets, A, then B, then C, one
  at a time in each machine-family queue, at the tune-down with native's cap, as on Azure; the free credits pay first
  (Google $300, Amazon $100 to $200). A set that fails for a quota (a new account's processor limit) is raised with the
  cloud, never shrunk to fit. The GPU on Lambda: his word came the evening of 18 October ("we're running them all today");
  from the GPU branch (`gpu-omni-v21`, omni-v21 with the GPU rig's readiness barrier, 30 October; the next rental starts from the engine that stands then), the three Lambda secrets first (`docs/LAMBDA_SETUP.md`), then the free dry run, then the real runs,
  one exact commit given to him. The same morning both first
  sets stopped at the login at no cost (Google's stored key cut short when copied from Cloud Shell's screen; Amazon's new
  account on the Free plan, whose organization policy denies every machine read); those runs were on omni-v10 and stay its
  record. That evening ("fix the Google and Amazon cloud. To work") both queues went back on behind a $0 check
  (`.github/workflows/cloud-check.yml`, `tools/cloud_key_check.py`): the conductor starts a cloud's set only after that
  cloud's newest check passed (the key whole, the login, the plan, the machine type, every quota; a short Amazon quota asked
  of Amazon by the check itself), starts a check itself within the hour, and so never spends a set's A, B or C on a login.
  Google starts once the key is stored whole (downloaded as a file, `docs/GOOGLE_SETUP.md` section 4), Amazon once the
  account is on the Paid plan (`docs/AMAZON_SETUP.md` section 1a).

- **Version 10: exploit all that can be, never raise the bill, hurt no one** (the founder's words: "Omni-Compass should be
  tuned to exploit all that can be and keep all healthy and never raise its bill ... whatever one can't be achieved doesn't
  get achieved. And the tuning stays where it doesn't ever hurt anyone"; then "push, push in the bush. Make sure everything's
  running"). Read by the one key, the battery glide moves to the speed that cuts the bill most with no LOSS (0.0875); a change
  that raised a miss anywhere (the outage-hours hold) is refused, not carried. omni-v10 was on main and on the branch `v10`;
  every page, manual, table and queue points at it; every benchmark runs again on it.

## Orders of 17 October

- **One key for every gauge** (the founder's correction of 17 October, night: "a minus doesn't mean a loss and neither does a
  plus mean a gain if you don't understand what it's against"). LOSS is only time waited, missed or failed that rose, or work
  that fell. A peak, a swing, an unevenness, wear and every other resource spent or held is power: a fall is a cut, a GAIN, a
  rise is power given, never a LOSS; work per energy that falls is power given too. The CityLearn tool had filed peaks, swings
  and unevenness as misses and the grid had judged work per energy as work, so rows that were power given were printed LOSS;
  both read through `tools/readings.py` now, and every result was re-read: on the engine that stands, no LOSS.

- **Version 9: the fix proven in our own runs first, then pushed** (the founder's words: "Engine fix goes into models
  first ... Apply the fix, run it, and see in the model sim that it works ... lock everything else that you're not touching
  ... Get rid of dead weight"; then "go go go"). omni-v9 stood on main and on the branch `v9` from 17 to 18 October, and
  while it stood every page, manual, table and queue pointed at it. **Native as shipped**: MySQL, Redis and MongoDB run with native exactly as the vendor ships them
  beside the operator's setting (`--native shipped`); where the factory setting is already at the knob's top, the knob
  reads "at its limit on native" and Omni-Compass watches. **Every level on one page** (`docs/LEVELS.md`, `tools/levels.py`,
  checked by `verify.py`): the muscle, the organism, the cluster, its add-ons, the service, the plant, the cloud and a group
  of clusters, each with its counts, and any level whose gauges go the other way is named and taken to the founder.
- **Version 8 stands; push in all and update all** (the founder's words: "there's a new version 8. That means you got to
  push in all and update all ... We're going to start the GPU soon and the other two clouds"). omni-v8 is on main and on
  the branch `v8`; every page, manual, table and queue points at it; every benchmark runs again on it. The GPU runs on
  Lambda and the Google and Amazon sets start on his word: the GPU from one exact commit given to him, the two clouds by
  turning their `switch=` line on once their secrets are in the repository.
- **The page number in both bottom corners, the running head on every page.** Every page of every manual but the title
  page carries the book's name on the left of the head and the part or chapter it belongs to on the right (openers and
  front matter included), and the page label in the left and the right bottom corner, "so that when somebody can flip
  through it" they know where they are. The notice stays at the foot of every page.
- **The navigation is checked row by row before every push**: every Contents row against the page where its heading is
  printed, every List of Figures row against the page of its caption, every index reference against the page it names,
  every figure against the paragraph that names it (under it when it fits, else at the top of the next page, never
  further, never more than two to a page, never in one block), the running head and both corner numbers on every page.
  "Every time and every fix and change and upgrade" realigns all three manuals in the same push.
- **Every figure is read at referee level before it is placed**: what it pictures, where it lives, the mechanism it
  states (the book, the Python, the harness, the organisms), its mathematics, structure, grids, arrows and direction;
  anything under full comprehension is reworked before the push. Nothing may mislead the wiring of Omni-Compass into a
  stack.
- **Every benchmark that can exist has its place.** The register names every domain of the industry, every realm and
  every muscle with the software available to benchmark; where a benchmark is not yet run, its place is written and
  marked as not yet run, never with a result before the result exists. The gap audit against the whole industry (who we
  have, who we do not, whose software is available) is standing work.

## Orders of 16 October

- **Seven organisms, the spine the seventh.** The spine (267 muscles, every muscle in all four realms) is an organism in its
  own right: the base every stack runs on, as an operating system is the base of every program. With the four realms, the four
  stacked and the tower that makes seven; "all seven need to be wired, written everywhere, native, and with Omni-Compass wired
  on native." The spine is written into the runners and the pages (`docs/THE_SPINE.md`, bound into both manuals), never into a
  fingerprinted engine file; the engine's fingerprint does not move for it.
- **Older versions are history.** "Why do I want to hear about version 5?" Everything worked on is the newest engine; what is
  found to have more room goes into the next version. Reports say native against Omni-Compass,
  gauge by gauge, never one version against another; older fingerprints are the road, in `docs/history`.
- **Nothing is cancelled.** No run is ever cancelled; a problem found in a running benchmark is fixed and the benchmark run
  again. Everything except the GPU chips and the Google and Amazon clouds runs, pushes and benchmarks.
- **Azure finishes first.** The founder decides on Google and Amazon after the Azure results are where he needs them, because
  Azure teaches what the other two will need.
- **Both manuals carry every muscle with its physical wiring on any stack** (the wiring appendix, `docs/wiring_recipes.csv`),
  and the whole package is kept in line with the newest engine top to bottom, fixed and tightened as found, pushed to the real
  places: it is presented to one buyer.

## Orders of 14 October

- **In the cloud, the bill** (the founder's order of 14 October, night; **struck on 31 October**, Orders of 31 October: no hard
  rule, every cloud at the max with the bill judged beside the work; kept here as the record of the sets that ran under it).
  In a cloud (Azure now; Google and Amazon when he
  starts them) Omni-Compass is to show one thing: the same work as native for a smaller bill, never a bigger one. Every
  cloud set runs Omni-Compass on top at the tune-down (`dial save`) on the machines alone (`OMNI_MACHINES_ONLY=1`): no pod
  autoscaler moved, no processor conveyed, no power capped, so the pods are exactly native's; the governor only parks a
  machine the cloud already made, after its own trial, and wakes it on a breach. No more pods and no more machines than
  native: the bill can only fall or stay. The bill and the machines aim lower, and work, speed and failures must read
  EVEN or GAIN. The benefit of the max belongs where Omni-Compass sits in the engine before the cloud, or in the
  chip at its other end. Runs of the max in the cloud are stopped and kept as such, counted in no bill result.
- **On autopilot: no babysitting tax** (the founder's words of 14 October, night). Omni-Compass is an autopilot,
  self-running, self-steering and self-auditing inside the system like a self-driving car: nobody turns a knob, nobody
  checks its work (every write read back, every give-back on its own trial, every reason in its audit) and nobody has to
  react, because it acts before the line is crossed. In the cloud the aim is no alert minute at all (a minute over the
  line wakes a person): an alert minute in the omni arm is found and fixed, never accepted.
- **Faster, but only where it hurts nothing** (the founder's words of 14 October, night). The governor is to move faster
  than every native controller under it (asked: a decision every 15, then 10, then 5 seconds), and no change is made
  until it is known to hurt nothing anywhere. Its fast checks already run every 5 s (native's pod autoscaler: 15 s); its
  full decision stays at 60 s in every run, because four of its rules count in decisions (a give-back trial's 20-decision
  phase would shrink to 100 s at 5 s and every trial would be abandoned, so the bill could never fall; at 15 s the phase is
  5 minutes and the wait after a breach 45 s instead of 3 minutes, and both are written in the engine). Native's own
  15-second check runs underneath untouched. The next engine version counts those rules in seconds and puts the fast
  checks on their own clock; it is used only when a test shows no LOSS. Every Kubernetes and cloud receipt shows it in both arms: the
  alert minutes (judged), the settings commands the governor wrote on its own and its additions made inside the line
  (shown) (`tools/live_reps.py`, `babysitting`); both manuals and the README say so.
- **Three manuals** (the founder's orders of 14 October, evening and night, and of 20 October, night: "There shall be three in
  the end"), all kept in the repository until the founder takes the Owner's Manual out:
  - **The Operator's Manual** (`docs/OMNI_COMPASS_MANUAL.md` and `.pdf`): the glove box, not the blueprint. It shows an
    engineering team how to embed, wire, tune, run and check Omni-Compass on a stacked, clustered system, or on any one
    muscle, in all its processes. It does not explain what is inside Omni-Compass or how it is built: no theory, no
    equations of the engine, no gains or internal rules, no engine source, no benchmark results (those stay in `results/`
    and `docs/STATE_OF_PLAY.md`). The engine is shown only as its shell and its process. Nothing in it explains or points
    to how the code is written, and nothing is disclosed or disclaimed about it. It is at least half the Owner's length
    (the founder's order of 14 October, night) and carries the implementer's whole cloud path (Part VI, chapters 13 to
    30, with the install files in `deploy/install/` and `deploy/Dockerfile.cloud`): Google and Amazon ready the way Azure
    is, the whole engine at the max in every cloud (31 October; the machines alone until then).
  - **The Owner's Manual, the master** (`docs/OMNI_COMPASS_OWNERS_MANUAL.md` and `.pdf`, `build_book.py --owner`):
    everything and all, for whoever owns or licenses Omni-Compass and so must know the whole mechanism: the philosophy and
    theory (`docs/book/THEORY.md`, `docs/book/DECLARATION.md`), the mathematics, the mechanism, how it is built, the
    engine's source, every result, and the wiring. Every fix realigns all three.
  - **The Live Engine Manual** (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` and `.pdf`, `build_book.py --live`): nothing more
    than the interpretation of the live engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`) for the operator at the
    dashboard: how to follow the wall and the switch, read every gauge and knob, trace a tile to its record, and see the
    mechanism of action native beside Omni-Compass as the monitors show it; no theory, no engine internals beyond what the
    page itself prints, no wiring. It names the page's sections by title and anchor, in the page's own order (its "Engine
    table of contents"), and is realigned with the page in the same push that changes it.
- **The manuals carry drawn figures, no plates and no blank pages** (the founder's orders of 14 October and of 16 October,
  night: "flow charts, illustrations to interpret the language of mathematics, build it in the manuals"; then, the same
  night: fifty more that interpret the code, the wiring and the receipts, "with another tool", so they do not all look the
  same). Two kits draw them from the book's own code and the repository's own files: `docs/book/figures.py` (reportlab: the
  two-way plug, the compass band and the two forces, one decision of the governor, the eight levels, the one pedal, the seven
  organisms, the three-run rule; in the Owner's Manual also the engine's six states and the double well) and
  `docs/book/schematics.py` (schemdraw and matplotlib: a wiring schematic for every stack in the grammar of an electrical
  drawing, the governor with its sense and motor terminals, the kill switch, the plug, the native controller, the muscle and
  the meters; the control-loop block diagrams; the flowcharts of the wire check, the paired run, the gate, the verdict, the
  stops, the model gate, the reading rule; the timing diagrams and modelled traces, marked class S; the state machines; every
  receipt of the engine that stands charted from its own table; the grids of the organisms and the catalog). A chart of a
  receipt pictures the table and adds nothing to it. Each figure is placed where a manual carries an image line pointing at
  `book/figures/<key>.svg`, numbered, captioned, listed in a List of Figures after the Contents, and written as an SVG file
  in `docs/book/figures/` for the pages on GitHub. **Every word lives inside its cell** (the founder's order of 16
  October, night): the type in a figure is 9 pt (his order, the shells kept), every label is measured in its own type and
  wrapped to the width of its box before it is drawn, the kit records any label that would not fit (`schematics.OVERFLOWS`,
  empty on every build), and no figure is ever scaled below its type: a figure taller than a page is split into two,
  "continued". A chart's axis shows what the reader needs to read it: the benefit sheet's axis reads 0, 10, 25, 50 and
  100 % on a square-root scale so a small bar is seen, and a bar past 100 % is drawn to the edge and marked. The Operator's
  Manual carries the wiring, the flowcharts, the timing and the structure (no receipt charts, no engine internals); the
  Owner's carries all. None of the founder's plates (his illustration images) go in: no cover art, no title-page rose, no
  plates, no List of Plates; no chart of a result either. **No dead pages** (the founder's order of 16 October, night: "every
  page be fully populated, 80% at least"): a chapter starts on the next page unless that would leave the page before it
  under 80 % used, and then it opens on the same page under a short space; a figure that does not fit under its paragraph
  floats to the top of the next page while the text goes on; a page never ends on one or two lines of a paragraph; code is
  set in pieces of six lines so a listing fills its page; a part's heading sits at the top of a page with its first chapter
  under it. The fill of every page is measured on the built PDF before a push. The contents and page numbers are rebuilt
  from the book itself (`docs/book/build_book.py`). The plates stay in `docs/book/plates/` as his property.
- **The Operator's Manual discloses what it leaves out** (the founder's order of 16 October, night): the Owner's Manual
  holds the harness, the engine's source, the mechanism and every result; the Operator's holds the wiring and operation
  only, says so in its front matter, and names the Owner's Manual as the book to go back to for anything it does not carry.
- **Every fix realigns everything, on every push.** When code changes or a bug is fixed, everything that describes it is
  brought up to it in the same push: the manual and its PDF, the README, the index, the tables, the plans and the
  standing pages. Then the newest-engine material is scanned top to bottom for the retired words and the old ways
  (better/worse, brake, bowl, "confirmed", "simulation" for our own models, standalone or competitor arms, 1,000 copies
  on a paid machine, power given called a loss, LaTeX markup) and anything found is fixed before the push. Old material
  stays where it is.
- **The factory tune** is declared and disclosed (`DISCLOSURES.md`, section 3; the README; the manual's notice): the engine
  is presented as the owner tuned it and ships it, self-running, set at the factory; every muscle wired on its own setting
  (its card, or the engine's setting); no setting universal; any licensee may then add on, retune, upgrade or tune down
  any muscle, and a changed tune's results are its own.
- **The wiring disclaimer in bold capitals** (`DISCLOSURES.md`, section 4; the README; the manual's notice; `llms.txt`):
  the published benchmarks are the record of what Omni-Compass did on the systems, loads and engine they name; where a
  result elsewhere differs, the first presumption is the wiring, the settings, or how Omni-Compass was implemented or read.
- **The notice travels with every output.** No code can force an outside AI to print it, so it is placed in everything
  they read: the top and end of every file, every program output, `llms.txt` (for AI crawlers), `AGENTS.md`, `GEMINI.md`,
  `.github/copilot-instructions.md` and `.cursorrules`, each ordering the notice on every answer of any length; the
  license makes a copy without it a breach. Those instructions point to the notice at the top and end of their own file
  (a second copy near the top is stripped by `tools/legal.py`).
- **The founder hears where things stand** in every report: what is running, what landed, what reads GAIN, EVEN or LOSS,
  and what is still on an older engine, in plain words.
- **The founder's prompt rules** (his document "A.I. prompt rules"), as they apply here:
  - Type: all text (body, tables, lists, code) at **11 pt or larger** on a line height of at least **1.5**; only running
    heads, footers and page labels may be smaller, at 8 pt; headings scale up from the body.
  - Language (the founder's correction of 14 October): not a 10th-grade level. The manual is written at referee level, for
    CTOs, principal engineers, physicists and mathematicians who will wire Omni-Compass onto a whole company's stack: the
    exact terms of control engineering, software engineering, physics and mathematics, used precisely and defined where
    they first appear, so that no reader can mistake what is stated, what is measured or how to wire it. Formulas are
    written in Unicode (the founder's order of 15 October: "it's got to be Unicode", for printing and for the engineers
    who wire and code it): w ∝ 1/√n, xᵢ,ₖ₊₁ = fᵢ(xᵢ,ₖ, …), Σ, ≤, ⌈·⌉, never LaTeX markup (`$`, backslash commands,
    `_{}`) in any page, so one line reads the same on GitHub, in a terminal, in code and on paper; a letter Unicode has no
    subscript for is written x[i].
  - Before a document is finished, audit it like a referee: equation and theorem numbers, cross-references, undefined
    symbols, repeated claims, and every claim backed by the text. No padding: every addition must earn its place.
  - In chat: no greetings, no echoing the request, no sign-offs; no follow-up questions (decide and do it); do what can be
    done without listing what can't. This never hides a result: every row, LOSS included, is still reported (Honesty).

## Orders of 13 October

- **GAIN, EVEN, LOSS** (the founder's order of 13 October, evening: "better, same and worse are going to be gain, even and
  loss, wherever and ever, all over where it lives, where it used to live"). Every judged reading, in every table, page,
  report, program output and the manual, is GAIN, EVEN or LOSS, decided by what the gauge is for and never by the sign of
  its number: time waited, missed or failed, a fall is GAIN; work done, a rise is GAIN; a resource spent or held, a fall
  is a cut, a GAIN, and a rise is **power given**, never a loss. Better/worse, lower/higher-as-a-verdict and toward/away
  are not used. The key (G.A.I.N. Growth, Advantage, Improvement, Net-positive; E.V.E.N. Equalized, Verified baseline,
  Equilibrium, Neutral; L.O.S.S. Leakage, Off-track, Setback, Subpar), disclosed and disclaimed, is written once in
  `tools/readings.py` and stands at the top of the README, `docs/HOW_TO_READ_THE_RESULTS.md` and the manual's front matter
  (`python3 tools/readings.py --fix`; `--check` fails a page whose key differs). "Theoretically I should never see the word
  loss": a LOSS row is never cut; its cause is found and fixed and the test rerun. `python3 tools/summary.py` prints the whole
  summary straight after a pull. Raw machine records (JSON receipts, raw run folders) keep their recorded field values;
  every page that shows them uses the words. Next: the words become the code that tells Omni how to move (the next engine).
- Every muscle runs from 1 up to one click under its own capacity, read live from the system, never a number written in
  code: never below 1 (a pool's machines never below 2), no ceiling where the system can keep adding, and back down again;
  guardrailed so no muscle overworks and hurts the organism, and the organism never hurts a muscle. Where the brain's own
  math shares the machine, it counts in the body's load. Encoded in the live controllers as Omni v5 amendment 5 (digest
  `6093b2b8`, `docs/OMNI_V5.md`): machines, replicas, the power cap, the GPU's clock floor and heat line, batch.
- Omni's brain works for the organism, never for Omni: it decides what to push and pull so the whole system is the best it
  can be, collectively, one body.
- Never decide a benchmark's settings ourselves: the written ones stand (the Azure burst steps are `1 6 1 8 1 6`, as first
  preregistered; the founder's order of 14 October withdrew our amendment of 5 October that had set `1 3 1 4 1 3`). When a result comes in negative, find the cause and fix it at once, unasked; a test machine's limit is never
  reported as Omni's result.

- **Everything on the newest engine** (13 October, night): every benchmark runs again on the engine that stands, and its
  result carries that engine's name. Nothing is shown or compared as "v3" once v5 stands: a v3 table is the road, in
  `docs/history`, never a setting to go back to by name. More versions will follow (perhaps to v10); each one reruns
  everything. Where a change made a result read LOSS, the fix is made inside the newest engine and rerun.
- **One cloud first** (13 October, night): Kubernetes on Azure is finished first; Google (GKE), Amazon (EKS) and the GPU
  chips (Lambda) are not run until the founder says the Azure Kubernetes results are where he needs them.
- **The company's telephone** (13 October, night; wording of 14 October; the landline added 16 October, night): "main
  office infrastructure, toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1", and under it the landline
  registered in Florida, 321-746-4411 (the toll-free number always on top), on every contact line where the company is
  named for reaching it (README, LICENSE and its copy, NOTICE, Enterprise License, Trademarks, Licensing FAQ, Security,
  Support, the manual's "Who to call", codemeta), always before the website, never inside the legal notice, which ends with
  www.omni-compass.com. The letters, read in order, are the company's own reading of how the engine runs (README "Contact",
  the manual's "Who to call"): DEX, Data Exchange (the input, the two-way plug); YLL, Yield Limit Line (the boundary, every
  muscle to its own limit and never past it, as a material is loaded to its yield limit and springs back unharmed); 1, one
  closed loop (the output; in code 1 is true, in science 1 is unity; one body, one brain). The founder's order of 14
  October: write it as the meaning, the way science and software people read it, wherever it fits in the manual; "years
  of life lost" is written nowhere. The founder's
  personal number is never written anywhere.
- **A copy he can keep**: the manual's PDF and the whole repository as a downloadable zip, in parts, from a pushed commit,
  sent to the founder after each landed change.

## Orders of 10 October (afternoon)

- The reflex rule is the whole mechanism: a trial runs to its full measurement and is never ended by the calm it causes;
  the brain never forces, it reacts to what the system shows; one body, one brain, the body's cost judged, nothing anywhere
  pushed to a LOSS to move one thing to a GAIN; one trial at a time inside a body; nothing permanent; the wall
  belongs to the body.
  Written into the engine as **Omni v4** (`docs/OMNI_V4_PLAN.md`), every wire forced through it, every result rerun.
- Everything is wired. Staying native is the brain's live decision every second, never a verdict from one run.
- **Six organisms**, never five (superseded on 16 October: seven, the spine an organism of its own): the four realms, all realms stacked (1,716), the whole catalog once (945). The live
  software products are never counted beside them. Realms are re-cut by a written rule at v4; new muscles raise the count.
- The word "simulation" is not used for our own models in reports: they are "modelled" (class S); live software is "the
  real thing" (class L); a meter is class P. The license's own phrase stays as written.
- The newest result is always at the front; the repository keeps itself current (the archive bot and the front page);
  old material goes to `docs/history`.
- All three manuals are printed books, front matter, body and back matter (Orders of 14 October: the Operator's Manual for
  the people who wire and run it, the Owner's Manual with everything); rebuilt as PDFs whenever they change.
- The founder hears what a result says before it goes up.

## Repository

- Referee and underwriter level. Only finals up front; old material goes to `docs/history` / `archive/` or is removed.
  One version is always the main one; `main` and the working branch, `v23` (the engine that stands, 31 October), stay in
  sync, and `v22`, `v21`, `v19`, `v18`, `v17`, `v16`, `v15`, `v14`, `v13`, `v12`, `v11`, `v10`, `v9`, `v8`, `v7` and `v7-candidate` are kept level with them; the GPU runs on Lambda start from `gpu-omni-v23`,
  levelled with main at every landing, its head the one exact commit the founder's next GPU rental starts from (the last rental ran
  7770532ed5, omni-v21 with the GPU rig's readiness barrier, 30 October). `main` stays linear: a branch is rebased onto it and fast-forwarded, never merged with a merge commit. **The `v5` branch
  is history** (the founder's order of 17 October: "We won long past 5"): it is never merged into `main` and `main` is
  never merged or pushed into it; nothing is read across engines.
- **The raw receipts live on the branch `raw`** (18 October): its root is what `results/live/raw/` held (every archived run,
  byte for byte, with its SHA256SUMS files). Main's tree is the code and the tables, so a clone of main is small (Dependabot's
  every clone had timed out on 36 GB). `scripts/raw_archive.sh open /run-<id>/` places a run at `results/live/raw/run-<id>/`
  (the path every table names); every workflow that archives raw files saves through `scripts/raw_archive.sh save`, and
  `raw-sweep.yml` moves any raw folder that still lands on main. `raw` is never merged with main, nor main into it.
  **Every finished run's files land there by themselves** (the founder's order of 19 October: "it's mine ... it should
  have been in my shit"): `archive-run.yml` takes every hour every finished run, failed ones included, of every workflow
  that hands in files, since omni-v11 landed (`tests/test_archive_sweep.py` fails a workflow left off its list), and a run
  id in `.github/archive_request.txt` goes first. A run's files are read from `raw` (the contents API, or
  `scripts/raw_archive.sh open`), never said to be out of reach.
  The stale work branches of 27 September to 15 October are kept whole on `archive/stale-branches` (one commit whose
  parents are their tips); their names may be removed without losing a commit.
- Verify before every push: `tools/release_manifest.py` under Python 3.12 (as GitHub runs it), 0 FAIL. `verify.py` runs
  every test, the files unittest never collects included (`tools/function_tests.py`, 18 October). Clear
  `/tmp/tmp*` first, because test leftovers fill the disk. Keep the Python 3.12 environment outside `/tmp` (for example
  `/root/v312`), because a container reset wipes `/tmp`. After a push, check the GitHub verify run itself, not only the
  local one.
- The Operator's Manual (`docs/OMNI_COMPASS_MANUAL.md`, `python3 docs/book/build_book.py`) is the wiring and operating
  manual, with every muscle's wiring and card (Appendix E); the Owner's Manual (`docs/OMNI_COMPASS_OWNERS_MANUAL.md`,
  `build_book.py --owner`) explains the physics, philosophy, mechanism and wiring, how to read every metric, every result,
  and holds the muscle catalog, the register and the engine's source; the Live Engine Manual
  (`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`, `build_book.py --live`) is how to read the live engine page.
- Zips on request: split into parts under the upload limit, each part openable on its own, built from a pushed commit.
- Never put a model identifier in a commit, PR or file.

## Talking to the founder

- The founder is not an engineer. Use plain language: yes/no plus a number. When asked a question, answer it before
  doing any work.
- Say what each step costs and how long it takes. Give Lambda and Azure steps click by click (the founder types on a
  laptop and chats on a phone).
- Credentials go only into GitHub secrets. Never ask for them, never echo them back.
- Latest standing order (Oct 5): push everything on the newest engine, run it again and double-check it, keep the old
  runs going, don't ask questions, and work to the highest referee and underwriter level.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
