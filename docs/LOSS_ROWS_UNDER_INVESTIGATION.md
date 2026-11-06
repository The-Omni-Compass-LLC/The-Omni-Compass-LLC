# LOSS rows under investigation: the rows whose cause is not yet established, and what is known of each

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every row of every three-run table is shown, LOSS included (the founder's order of 11 October). Where a LOSS row of Omni-Compass
against its native has a page in `docs/` that states its cause (as `docs/POD_START_WAIT.md` does for the pod start wait under
KEDA's HTTP add-on), the live engine names that page beside the row (section 1d). This page holds the rows whose cause is **not yet
established**: what each row read, when it was raised, what is known, what is suspected and not yet shown, and what decides it.
A suspicion is written as a suspicion. Nothing here is a result; the rows stand as their tables read them until the engine that
stands has run the benchmark again three times. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or
approved these results.

## Job turnaround under Armada, Omni-Compass on the organism alone (V12_ARMADA_4W_BARE.md): under investigation since 21 October 2026

**The row.** `results/live/V12_ARMADA_4W_BARE.md`, the four-ways comparison BARE (Omni-Compass on the organism alone against the
organism alone, Kubernetes' own scheduler under both): job turnaround **LOSS in all three of our runs** (up 5.1%, 8.9% and 9.1%: the jobs took longer), on
omni-v12. The same table's other rows are its own; the table stands as recorded.

**What is known.** The arm with Omni-Compass raised the web pods' CPU limits (conveyance) while the batch queue ran on the same
kind host, as the governor's audit of each repetition records; on the batch rig the governor has its own core and the kind nodes
share the rest (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 5).

**What is suspected and not yet shown.** The mechanism found on KubeRay's rig on 20 October and fixed in omni-v13 (`docs/OMNI_V13.md`:
on a shared host at its top, beside another workload's room, a limit raised was kept through a saturated queue, so the batch pods
ran slower while the web served no faster) fits this row's shape: a batch gauge, turnaround, a few percent slower with Omni-Compass
on the organism alone. Whether it is the cause here is not established: the Armada rig was not read as KubeRay's was, and no
omni-v13 run of it has landed.

**What decides it.** Armada's three runs on omni-v13 (`scripts/reruns.txt`, released by the conductor in the order A of every
benchmark, then B, then C). If the row reads STEADY or GAIN there, the cause was the conveyance omni-v13 repaired and this entry
closes with that reading; if it reads LOSS again, the rig's own files are read repetition by repetition as KubeRay's were, and the
cause written here.

**Read again on omni-v25.** The row reads **LOSS in all three of our runs** again: job turnaround up 15.6%, 23.8% and 23.0%,
the jobs took longer (`results/live/V25_ARMADA_4W_BARE.md`), on an engine that carries omni-v13's repair; the same table
reads the alert minutes up 10.4% to 13.0%, LOSS in all three of our runs. So the conveyance omni-v13 repaired is not the
whole cause, and the rig's own files are next, repetition by repetition. The cause is still not established.

## Alert minutes under Open Cluster Management, Omni-Compass on top (V12_OCM_4W_TOP.md): under investigation since 21 October 2026

**The row.** `results/live/V12_OCM_4W_TOP.md`, the four-ways comparison TOP (Omni-Compass on top of Open Cluster Management against
Open Cluster Management as shipped): alert minutes **LOSS in all three of our runs** (up 5.7%, 6.1% and 45.5%: more minutes over the line), on omni-v12. The
third run's size is far from the other two; the three intervals are each clear of zero, so the rule reads LOSS and the row stands.

**What is known.** An alert minute is a minute in which the service's response time stood over its line (`tools/live_reps.py`,
`babysitting`): the gauge counts how long a person would have been paged, and the aim in every cloud and Kubernetes run is no alert
minute at all (the founder's order of 14 October). Open Cluster Management runs two clusters (a hub and a member); the governor
runs on top of the group. The page's scorer counts the group and the member cluster each by its own files (`docs/engine/export_runs.py`,
every file kept at its own path since 21 October).

**What is suspected and not yet shown.** Two candidates, neither established: a settings write of the governor landing while the
service was already over its line, lengthening the minute (the governor's audit of run C is the place to read it); or the member
cluster's capture, which until 21 October overwrote the group's in the page's own replay (a scorer fault, repaired that day, which
did not touch the table's own numbers). The table's own numbers were written by `tools/live_reps.py` on the run's files and are not
in question.

**What decides it.** Open Cluster Management's three runs on omni-v13, read with the governor's audit beside the service's response
line, minute by minute; and, before they land, a reading of run C's own audit (`results/live/raw/run-<id>/`), which is the next
step of this investigation.

**Read again on omni-v25.** The row reads **LOSS in all three of our runs** again: alert minutes up 17.9%, 25.6% and 12.1%,
more minutes over the line (`results/live/V25_OCM_4W_TOP.md`), the same table's job turnaround up 20.7% to 29.9%, LOSS in all
three. The scorer fault of 21 October is repaired, so it is not the cause; Omni-Compass's own audit beside the response line,
minute by minute, is the next step. The cause is still not established.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
