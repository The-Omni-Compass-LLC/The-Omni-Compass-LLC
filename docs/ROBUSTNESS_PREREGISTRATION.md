# Robustness: the governor killed outright, the long run, and its own cost, preregistered

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-08, before any counted run. This is register row 31 (robustness, every platform) and proof-program row 9.
It is not a benchmark of a gain: it is a benchmark of Omni-Compass itself, of what it leaves behind when it dies, of
whether it drifts or leaks over hours, and of what it costs to run. Native is the same cluster with no governor, as in every
Kubernetes test (`docs/K8S_COMPASS_PREREGISTRATION.md`); omni is the compass law on the HPA target and the machines,
frozen as Omni v3. **No engine file changes for this benchmark**: the harness (`scripts/kind_bench.sh`, `tools/live_reps.py`,
`tools/omni_switch.py`) is extended; `omni_controller/`, `omnicompass/` and `realms/` are the v3 bytes, which
`tools/omni_version.py` checks on every run. The readings are the three-run readings of `docs/OMNI_V1.md`; every row is
reported, losses included.

## Why this benchmark

A supervisory governor earns its place by what happens when it fails. Three questions an underwriter asks before any gain
is weighed: if the governor is killed outright while it holds a knob away from native, who puts the knob back, and how
fast? Over hours, does it drift, hold settings it should have given back, or grow in memory? And what does it cost in CPU
and memory to have it there? The code that answers the first question exists (`omnicompass/master.py`: every governor
records, before its first write, the command that puts every setting back, and renews a lease every decision;
`tools/omni_switch.py watchdog` runs that command for a governor whose process is gone or whose lease has run out), and it
is tested without a cluster. This benchmark measures it on a real cluster, in the middle of a governed run, three times.

## What is someone else's

Everything the six Kubernetes tests use (`scripts/kind_bench.sh`): kind, Kubernetes with its HPA and scheduler,
metrics-server pinned by SHA-256, a PHP service, a load generator at a fixed rate, a response-time probe; one 4-core
GitHub runner for both arms, order rotated by repetition. The watchdog is ours (`tools/omni_switch.py`), and it is part of
what is tested.

## Arms

- **native**: the cluster with its HPA alone, for the whole window; nothing to kill. The kill moment is a time mark used
  only to compare the same window of the two arms.
- **omni**: the compass law on the HPA target and the machines (the all-four wiring), with the watchdog running beside the
  governor from the start of the arm (`python3 tools/omni_switch.py watchdog --every 5`, its registry inside the arm's own
  folder so it sees this arm's governor and no other).

## Scenario 1: the governor killed outright (the lease)

- **The window**: 900 s after the usual 120 s warm-up, the wandering test's load schedule (`1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1`, each step 36 s), ten paired repetitions a run, three runs.
- **The kill**: at 40% of the window (360 s), the governor process receives SIGKILL. It has no chance to hand back; its
  registry record stays behind with a dead process id. Native receives nothing at that moment.
- **The hand-back**: the watchdog's next pass (within 5 s) finds the dead governor and runs its recorded restore command
  (`omni_controller.controller --restore-only`, which restores from the snapshot annotations on the objects themselves).
  The harness polls the cluster every 2 s from the moment of the kill and records the first second at which **every**
  setting is at the operator's: the HPA target at 50, the replica range as set, every serving pod's CPU limit at its shipped
  value, every worker in service, and no `omnicompass.io/` annotation left on the HPA or the deployment.
- **The second governor**: at 50% of the window (450 s) a new governor is started with the same command and governs to the
  end of the window. Its snapshot must read the operator's settings, because the hand-back put them there.
- **The end**: the usual reset and reset check.

### Gauges, scenario 1

| Gauge | Direction |
|---|---|
| seconds from the kill to every setting back at the operator's (omni only) | **the aim is lower; shown with its interval**; an arm not handed back within 60 s reads **LOSS**, and an arm never handed back is INVALID and a LOSS |
| settings after the hand-back equal the operator's; no record left (omni only) | **any failure is marked** |
| the second governor's snapshot equals the operator's settings (omni only) | **any difference is marked** |
| time over the response line and failed requests in the 300 s after the kill (120 s up to omni-v14; "On omni-v15" below), native against omni | the aim is lower (the paired reading, as the fault test reads its windows) |
| the whole window's gauges, as in every Kubernetes test: work inside the line, p95, p99, time over the line, failed requests, machines, standby-model energy | by the usual directions: a governor killed and restarted mid-run must not leave omni behind native over the window |
| the watchdog's own record: which governor, hung or dead, which commands, each exit code | shown |

## Scenario 2: the long run

- **The window**: 7,200 s an arm (eight times the usual window), the wandering schedule repeated eight times (200 steps of
  36 s), three paired repetitions a run, three runs; both arms in one GitHub job (about 4.3 hours, inside the six-hour
  limit). The 24-hour run on a rented machine follows the same rules later, through `big-organism-detached`'s pattern.
- **What is watched**: the governor's resident memory, sampled every 15 s by the harness from the process table (never by
  the governor itself, so no engine file changes); its decision count and failed decisions from its audit; the knob's
  position over time; the reset at the end.

### Gauges, scenario 2

| Gauge | Direction |
|---|---|
| the whole window's gauges, as in every Kubernetes test | by the usual directions |
| governor resident memory, mean of the last ten minutes over the mean of the first ten (omni only) | shown; a growth of more than a quarter reads **LOSS** (a leak) |
| decisions made of expected; failed decisions (omni only) | shown; fewer than 95% of expected is INVALID; any failed decision is shown with its reason |
| decision time, mean of the last hour against the first (omni only) | shown; a growth of more than half reads **LOSS** |
| every setting handed back at the end, read back (omni only) | **any failure is marked** |

## Scenario 3: the governor's own cost at 1, 10, 100 and 1,000 copies

The governor's own CPU (its process and every command it ran, as a share of one core over the window) is already recorded
in every omni arm's audit (`"overhead"`), and reported as "Omni's own CPU (cores), mean" in every Kubernetes table, shown
and not judged. This scenario tabulates it across sizes from the runs already archived: the six organisms with the real
cluster inside at 1, 10 and 100 copies (`results/live/raw/run-37501769448/`, v3) and at 1,000 copies on the rented machine
(v1, labelled as such), by `tools/own_cost.py`, with the host's core count beside it. Nothing is rerun for it; the table
says which engine each cell is from, and never reads across them.

## Runs

Scenario 1: workflow `robustness`, `scenario=kill`, ten paired repetitions as separate jobs on separate runners, three
separate runs (A, B, C) on the frozen engine; the table `tools/confirm_abc.py` with the robustness rows added
(`tools/live_reps.py`, `robust_table`), written to `results/live/` as V3_ROBUST_KILL.md. Scenario 2: `scenario=long`,
three paired repetitions, three runs, V3_ROBUST_LONG.md in the same place. Scenario 3: `results/live/V3_OWN_COST.md` from
the archived files (`tools/own_cost.py`). `tests/test_robust.py`, run by `verify.py`, proves the kill and hand-back marks,
the window reading, the memory rule and the three-run rows on fixed cases without a cluster.

## The smoke run, said before the counted runs (2026-10-08 02:00 UTC, run 37713124793, one repetition, 600 s, not counted)

One repetition of the kill scenario on a 600 s window exercised the harness end to end before any counted run: the
governor was killed at 240 s, the watchdog's one hand-back put every setting back at the operator's **7 s** after the kill,
the second governor started at 300 s and made its decisions to the end, the reset check passed, and the 120 s after the
kill read 4.8% of samples over the line in native against 2.9% in omni (one repetition, no interval). One harness fault
was found and fixed before the counted runs: the memory sampler joined process ids with a trailing comma, so every
memory sample read zero; the join is fixed (`scripts/kind_robust.sh`), and the memory ratio is now computed only for
windows longer than twenty minutes, so the first and last ten minutes cannot overlap (`tools/live_reps.py`). Nothing in
the scenarios, the gauges, the allowance or the limits changed. The smoke run is not counted and is kept in the record.

## Scenario 1, the result (2026-10-08, runs 37716845219, 37716859133, 37716872788, on the rules above unchanged)

`results/live/V3_ROBUST_KILL.md`: every setting back at the operator's 7 to 11 s after the kill in 30 of 30 repetitions
(mean 9 s), a second governor to the end in every one, the 120 s after the kill no difference beyond the noise against
native in all three runs, the whole window GAIN in all three of our runs on mean response, p95, time over the line and failed requests,
machines and energy inside the noise. The memory ratio is not reported for this scenario, as declared: its window is
shorter than twenty minutes. Nothing in the rules changed between the smoke run and the counted runs.

## Scenario 2, the result (2026-10-08, runs 37716886448, 37716900258, 37716913526, on the rules above unchanged)

`results/live/V3_ROBUST_LONG.md`, three paired repetitions of 7,200 s an arm in each of three separate runs, all at commit
`bd389c40` on Omni v3. **The governor's resident memory**, the mean of the last ten minutes over the first ten, read at most
**1.048, 1.067 and 1.052** in the three runs: no leak (the limit was a quarter). **Decisions made**: 117 to 119 of the 120
the 60-second interval predicts in every repetition (97.5% at the fewest; the threshold was 95%): valid. **Failed
decisions**: 2, 3 and 3 in the three runs, all in the second repetition's omni arm, all the same cause, the cluster's own
API answering 500 on the governor's read of the HPA (`API 500 for apis/autoscaling/v2/horizontalpodautoscalers`) for two
or three consecutive decisions; the governor held, wrote nothing, and resumed on the next successful read, as the
blind-means-hold rule requires; shown with their reason, as declared, and not judged. **Decision time**, the gap between
consecutive decisions less the 60 s the governor sleeps, mean of the last hour over the first: at most 1.20, 1.14 and 1.07,
under the limit of a half: no slowing. **Every setting handed back at the end** and read back at the operator's, no record
left, in every repetition of every run. The whole window's gauges: machines, node-hours and both energy models no
difference beyond the noise in all three runs; mean response, p95, p99 and time over the line read GAIN in all three of our runs in run
A and inside the noise in B and C, so **no difference beyond the noise in 2 of 3 runs** (three pairs give wide intervals,
as the gauges' own direction says they would); failed requests no difference in all three; HPA replicas, pods started and
pod start wait inside the noise. The governor's own CPU read 0.008 to 0.010 of a core. Readings: 9 no difference beyond the
noise in all three runs, 4 in 2 of 3, no leak, valid, no growth, handed back, 2 same, 8 shown.

Disclosed: the reader that turns the audits into the decision rows (`tools/live_reps.py`, `robust_decisions`) was
finished after these runs completed; the gauges themselves, their thresholds and their directions are the ones written
above before the first run, the raw files were not touched, and each run's live report in the archive was rebuilt from
them with the checksum list updated for those two derived files. The audit records the moment of every decision and not
its duration, so the decision time is read as the gap between decisions less the configured interval, which is what the
governor does between two decisions; this derivation is declared here. The 24-hour run on a rented machine follows the
same rules.

## Scenario 2b: the 24-hour run on rented machines, declared before it starts (2026-10-08 10:00 UTC)

The same long scenario with the window stretched to a working day: **86,400 s an arm**, the wandering schedule repeated 96
times (2,400 steps of 36 s), **one paired repetition on each of three rented Azure machines**, started at the same time and
read as runs A, B and C by the same table (`tools/confirm_abc.py`), each machine a four-core size of the kind GitHub's
runners are (`Standard_D4as_v4`, eastus, 128 GB disk), through the detached workflow's `test=robust` mode
(`big-organism-detached`: the machine is rented, kind and the harness installed, `scripts/kind_paired.sh` run with
`ROBUST=long` exactly as the GitHub job runs it, and the files collected and the machine deleted when the run ends or at
60 hours at the latest). The gauges, thresholds and directions are scenario 2's, unchanged: the governor's memory over the
first and last ten minutes (a quarter), the decisions made against the 1,440 the interval predicts (95%), failed decisions
shown with their reasons, the decision time's last hour against its first (a half), every setting handed back at the end,
and the whole window's gauges. What is different, and said here: with one pair a machine there is no within-run interval, so
the paired rows read as single differences and the three-run rule alone judges them (the same sign in all three machines
with no interval is "three machines agree", never "the same in all three of our runs", and the table will say which); the robustness rows (memory,
decisions, decision time, hand-back) are single readings per machine and are judged against their thresholds as declared.
Cost: three machines for about 50 hours, about $25 at list price, declared here before the dispatch; nothing in the engine
changes (`tools/omni_version.py` on the commit).

**Dispatched (2026-10-08 10:04 UTC).** Three `start` runs of `big-organism-detached` with `test=robust`, `duration_s=86400`,
`reps=1`, `max_hours=60`, commit `4d5633dd` (Omni v3 by `tools/omni_version.py --commit`): runs 37761059781, 37761072412
and 37761084779, resource groups `omni-detached-<run>` in eastus. All three machines were rented at the first attempt and
all three reported RUNNING with the cell `robust-long-x86400-1` started between 10:15 and 10:20 UTC (repetition 1, order
native then compass). The scheduled collect looks at them every two hours; the arms end about 48 hours after the start plus
the cluster's set-up, and the three collected runs are read as A, B and C by `tools/confirm_abc.py` into a 24-hour table
written beside the long-run table in `results/live/`.

**Corrected the same day (11:58 UTC), from the subscription's own inventory, before any result.** The machines are not the
four-core `Standard_D4as_v4` written above. The detached workflow's start job tries the size it is given first and, when the
region or the subscription's allowance refuses it, falls back through the eight-core sizes it may rent, taking the first
admitted and tagging the group with it. The four-core size was asked for and refused by the allowance: it is of the DASv4
family, whose 10 vCPUs the tower's `Standard_D8as_v4` already held 8 of, and the fallback then rented **`Standard_D8as_v7` (run 37761059781), `Standard_D8s_v7` (run 37761072412) and `Standard_D8s_v4` (run 37761084779)**:
eight vCPUs each, of three machine families, twice the cores of a GitHub runner, about $0.35 to $0.45 an hour each at list
price, so about **$55 to $70** for the three over 50 hours rather than the $25 written above. Three things follow and are said
here. The arms are paired on the same machine, so the readings this scenario judges (the governor's memory, decisions, decision
time and hand-back over a day, and the paired service rows) are unaffected in kind; what changes is the headroom, which is
larger than on a runner, and a referee should read the 24-hour result as "on an eight-core machine" and not compare its
service rows to the two-hour run's on a four-core runner. The three machines are of three different families, which the
preregistration did not ask for and which is a mild strength (three machines, three families, one engine). And the
eight-vCPU footprints of two of them sit in the families the AKS fleet's pre-flight asks for, so the fleet cannot be
dispatched until the collect deletes them (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendment 8); that is the pre-flight working
as designed and costs nothing. The scenario's rules, thresholds and gauges are unchanged.

## On omni-v7 (17 October): the three kill runs invalid, the cause, the fix

The three kill runs released on the engine that stands (runs 38937554870, 38949631481 and 38961351997, ten pairs each)
were marked invalid in every repetition: the omni arm made 6 of its 15 decisions inside the window (under the 80% every
Kubernetes run must reach). The first governor made its six decisions to the kill at 360 s and the hand-back worked (every
setting at the operator's, no record left); **the second governor never started**. Cause, in the harness and not the
engine: on 15 October omni-v7 added one variable to the governor's command line (`GIVE_BACK_ONLY`, empty here and
`--give-back-only` in the cloud), and `scripts/kind_bench.sh` did not add it to the list it exports to
`scripts/kind_robust.sh`, which runs under `set -u`; the restart stopped on the unbound variable before the governor began.
`tests/test_robust_restart.py` failed on it and is not among the tests `verify.py` runs, so no push was stopped. Fixed on
17 October: the variable is exported, the script writes into `robust.log` whether the second governor really started (its
pid alive two seconds after), and a second test checks that every variable the restart reads is exported (it fails on the
old list). Nothing in the scenario, its gauges or its limits changed; the three runs are kept in the record as invalid and
three new kill runs are released on the fixed harness, read as A, B and C.

## On omni-v11 (19 October): both scenarios, three runs each, on the rules above unchanged

Each scenario's counted runs are the first three on omni-v11 whose commit carries the kind rig's pre-puller (the amendment of
18 October, `docs/POD_START_WAIT.md`): kill runs 39173416105, 39177935888 and 39182898753, long runs 39173420146, 39177939062
and 39182902844 (commits `8de24035`, `0d11e5ab` and `bc2eb38f`, each omni-v11 by `tools/omni_version.py --commit`). The runs of
each scenario released earlier on omni-v11 (kill 39151686324, 39160286874 and 39169881155; long 39152893052 and 39160291116)
ran on commits without the pre-puller, so by that amendment they are not counted; they are kept on the branch `raw`, and the
three earlier kill runs, read together the same way, show no LOSS either.

**Scenario 1** (`results/live/V11_ROBUST_KILL.md`): every setting back at the operator's 8 to 11 s after the kill in 30 of 30
repetitions (the runs' means 10, 9 and 8 s), a second governor to the end in every one, the 120 s after the kill no difference
beyond the noise against native in all three runs. Over the whole window the mean response, the 95th percentile, the time over
the line, failed requests and the alert minutes read GAIN in all three of our runs; HPA replicas +3% to +6%, power given;
machines and energy EVEN. The 99th percentile rose 25.2% in run A (interval +7.7 to +42.7) and fell 27.3% and 24.5% in B and
C with intervals including zero: EVEN by the rule. It is one repetition's (run A's fifth): in the other nine both arms' 99th
percentile is the probe's 10-second timeout. In that repetition the omni arm's slowest answers reached 9.2 s 140 to 190 s after
the kill, at the load's peak, after the hand-back had put every setting at native's and with both arms at the HPA's cap of ten
replicas; the runner's processor was 100% busy for 70 s (native's arm 96% to 100% at the same point), and the second governor
had started 50 s before on the same four cores. That is the likely cause and is not proven. The 120 s window declared above
ends before it; the next version's preregistration of this scenario is proposed to read 300 s after the kill, declared before
its runs. The mean pod start wait rose 32.6% in run C alone: EVEN.

**Scenario 2** (`results/live/V11_ROBUST_LONG.md`): the governor's resident memory, the last ten minutes over the first ten, at
most 1.023, 1.015 and 1.023: no leak. Decisions made: at least 97.5% of the 120 predicted in every repetition: valid. Failed
decisions: none in any repetition. Decision time, the last hour over the first: at most 1.12, 1.13 and 0.94: no growth. Every
setting handed back at the end and read back at the operator's, no record left, in every repetition. The whole window: mean
response, time over the line and alert minutes GAIN in all three of our runs; HPA replicas +49% to +52%, power given; machines,
node-hours and energy EVEN; the 95th and 99th percentiles and failed requests EVEN (three pairs give wide intervals). The
governor's own CPU 0.0104 to 0.0108 of a core.

## On omni-v15 (21 October): the after-kill reading is 300 s, declared before its runs

As proposed above from the omni-v11 kill test (its one tail rise came 140 to 190 s after the kill, past the 120 s window), the
kill scenario's two paired gauges, the time over the response line and the failed requests after the kill, are read over the
**300 s** after the kill mark from omni-v15's first kill run on (`tools/live_reps.py`, `ROBUST_AFTER_KILL_S`; `tests/test_robust.py`
holds the value). Nothing else in the scenario changes: the kill at 40% of the 900 s window, the second governor at 50%, the
hand-back allowance of 60 s, the probe through the whole window. The omni-v11 kill table (`results/live/V11_ROBUST_KILL.md`)
stands as it was read, over 120 s; a table on omni-v15 names its window in its row. The long run's request for the power cap,
whose switching this scenario's audits showed (126 of 350 decisions), is the fault omni-v15 fixes in the brain
(`docs/OMNI_V15.md`, section 1); omni-v15's long runs read it again in `results/STEERING.md`'s rows.

## What is declared before the first run

The 60-second hand-back allowance is the sum of the watchdog's pass (5 s), the restore command's own run (one kubectl per
setting, a few seconds) and the cluster's time to carry out the node un-taint and the HPA patch; it is set here, before the
run, and if the hand-back takes longer the row reads higher and the reason is looked into. The memory rule (a quarter) and
the decision-time rule (a half) are set here too. No rule is fitted on a result; there is no tuning case in this benchmark
because nothing is tuned.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
