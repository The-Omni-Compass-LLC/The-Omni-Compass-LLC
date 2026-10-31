# Omni-Compass's own orchestrator: the organism run without Kubernetes

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 23 October 2026: "I want to build my own components ... the whole orchestration in Omni Compass would
only be to replace ... Kubernetes, and whatever orchestration ... Go ahead and build such a thing." This page is what was built
that day and what its first showing read. It is a first showing on one host, class L (live software, every piece a real
process), one run of each arm: it shows that the mechanism works end to end and how it behaved here, not yet a three-run
reading. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. What it is

`omni_orchestrator/` is written from scratch on Python's standard library and Omni-Compass's own compass law
(`omnicompass/compass_law.py`). No code of Kubernetes, Docker Swarm, Nomad, Slurm or any other orchestrator is in it; the
only outside mechanism it uses is the Linux kernel's own, which stays native under it (its control groups wall the
processor and memory, its scheduler shares each core). What Kubernetes' published autoscaling rule says is written here, by
us, from its documentation, as the yardstick Omni is read against; that is a description of a rule, not Kubernetes' code.

| piece | file | what it does |
|---|---|---|
| the walls | `cgroup.py` | a machine's and a unit's CPU quota and memory limit through the kernel's control groups (`omni/<machine>/<unit>`); the processor each one used, read from the kernel's own counter |
| the machine's hand | `agent.py` | one process per machine, the only thing that starts or stops a unit on it: starts each unit inside its own walls on the machine's cores, probes a service on its health path twice a second (ready at its first answer; killed and started again after three missed answers), starts a crashed unit again after a wait that doubles from 1 to 30 s, marks a batch task done at exit 0 or failed after three tries; the units keep running whatever happens to the control plane |
| the front | `front.py` | one address for a service, its own process: every request joins one line, each ready unit has one hand that takes the next request and waits for its answer (one request at a time a unit, the waiting measured here), a unit that fails to answer sends the request back to the head of the line for another unit (three tries); the response time it measures is the brain's sense |
| the room rule | `scheduler.py` | a unit goes only where its request fits on a machine awake and, for Omni, only onto a machine under 75% of its measured busy share (the engine's own rule, `omni_controller/capacity.py`); **pack** (Omni): the machine left fullest, but a service of two or more units never on one machine alone; **spread** (the yardstick): the machine with the fewest units of the service, then the most room, as Kubernetes' scheduler scores by default, by requests alone |
| the brain | `brain.py` | **Omni, every 5 s:** the reflex (work waiting in line at the front adds units now, one for each request waiting, up to the step); the compass law on the service's 95th percentile response time in the band from 0 to its line (a force up adds units at once in proportion, past the wall the most it may; a force down gives back one unit after it has held down for three beats with nothing waiting); the twin, the yardstick's rule computed on the same readings (what Kubernetes would hold for this work), which Omni holds at least, less only the depth the verdict has allowed (`omnicompass/verdict.py`, the engine's own trigger: one unit fewer than the twin is tried on the service's own response times and kept only where they read no LOSS within the 2% allowance; a trial walks to its step one unit a beat and stands there while it measures; work waiting in line hands one allowed step back). **Conveyance:** each unit's CPU wall set to the room its machine can still give under 75%, less other workloads' units by their limits, shared among the service's units there, never under the request (the engine's rule, `omni_controller/muscles.py`, omni-v7 and omni-v13): a unit answers at its machine's speed, not its paper quota's, with no unit and no machine added; Kubernetes' autoscaler never moves a limit. **Yardstick:** every 15 s, units = ⌈units × busy ÷ 50%⌉ (busy read capped at the request, as a pod walled at its request can use), no move inside 10%, a rise to at most max(2 × units, units + 4), a fall only to the highest count of the last 300 s. **Machines:** the units' requests plus room for the next step, never fewer than two |
| the control plane | `control.py` | the ledger of what is wanted and what was placed, every change a line in a journal before it is acted on, replayed when the control plane starts again (the units it finds running are taken back as they are, none started again); every second: every hand polled (a machine silent three times is down and its units placed again), retiring units stopped once drained, the brain on its beat, the room rule for every unit the ledger lacks, batch tasks into the room the service leaves (a task yields its room the moment a service needs it), the routes for the front (only ready units), one timeline line; the kill switch is a file: the brain off, the declared state held; every decision one audit line with its reason |
| the workload | `workload.py` | a service whose every answer is checked (a chain of SHA-256 hashes from the request's seed; the digest is fixed by the seed, so the client knows whether the answer is right) and a batch task of the same kind |
| the clients | `load.py` | closed-loop clients stepping by one (1 2 3 2 3 4 …): each sends its next request when the last is answered and it has thought 0.1 s, so a slower answer brings fewer requests, as programs and people do; every answer checked against its known digest |

`tools/orchestrator_show.py` runs the whole showing on one host and writes `report.html` from its files;
`tests/test_orchestrator.py` holds the rules (the room rule and the busy rule, the yardstick's arithmetic with its busy
capped at the request, the twin floor and the verdict's depth, the reflex, conveyance, the ledger's replay with a conveyed
wall). The hand takes a wall change on `POST /units/<id>/limit` and reports every unit's wall as the kernel holds it; the
front hands the control plane every answer's response time since its last beat (`GET /_stats?since=<seq>`), the pieces of
work the verdict measures a trial on.

## 2. The first showing, 23 October (quick form: six steps of 15 s)

The rig: six machines of half a processor each (the kernel's CPU quotas, two machines on each of three cores); the control
plane, the front, the six hands and the clients on the fourth core. Units of 250 millicores (request and limit); a request
about 40 ms of processor. Both arms took the same clients, 1 2 3 2 3 4, 15 s a step. Every number is from the showing's own
files (each request's record, the control plane's timeline and audit, the kernel's processor counters).

| gauge | yardstick | Omni | Omni against it |
|---|---:|---:|---:|
| requests answered (work) | 1,174 | 1,044 | −11.1% |
| requests failed | 0 | 0 | — |
| answers wrong | 0 | 0 | — |
| response time, 50th percentile (ms) | 89 | 110 | +23% |
| response time, 95th percentile (ms) | 165 | 213 | +29% |
| machine-minutes on (the bill) | 9.0 | 6.6 | −27% |
| processor-seconds used by the units | 52.8 | 50.2 | −5% |

Read by the one key, step by step (six pairs): requests answered −11.1% **LOSS**; the 95th percentile +23.8% **LOSS**;
machines on −26.5% **GAIN (a cut)**. The units Omni held were the yardstick's own at every beat (2 → 3 → 4 → 6 → 7, each
equal to the native twin, the compass force negative throughout because the 95th percentile sat far under the 800 ms line);
no unit ever waited for room. What differed is where they stood: Omni packed them, four units of 250 m on the two machines
of one core, and parked the two empty machines; the yardstick spread them, two units a core at most. Four units whose
quotas sum to the whole of a core, busy at once, share that core: each 40 ms answer waits for the others, and a slower answer
brings fewer requests from closed-loop clients. That is the trade of packing read on this rig: fewer machines on, each one
fuller, each answer slower.

The mechanism answer is already in the engine that stands and not yet in this orchestrator: on the kind rig no replica is
added to a host while it is 75% busy (`omni_controller/capacity.py`, omni-v7). The room rule here counts requests only; its
next form counts the machine's measured busy share as well, so a machine at its top takes no more units and the brain wakes
another instead. It is in the orchestrator as a declared option, `--room-rule busy` (`omni_orchestrator/scheduler.py`,
`BUSY_TOP`), off by default; the showing that runs it is read against this one, and nothing here was tuned after the reading.
The yardstick always places by requests alone, as Kubernetes' scheduler does.

**One body.** A job of 16 batch tasks (about 2 s of processor each, four at a time) ran in the room the service left while
the clients went 3 → 6 → 3: 16 of 16 tasks finished with their result files written, the service answered 603 requests, 0
failed, 0 wrong, its 95th percentile 233 ms.

**The drills**, with the clients running (four) through all of them: a unit killed (its hand started it again; 0 requests
failed), a machine lost with its units (declared down after three silent polls, its units placed again elsewhere; 0 failed)
and repaired (it joined empty), the control plane killed for 10 s and started again (the units kept serving; it replayed its
journal and took every unit back as it stood, none started again; 0 failed), the kill switch on (the brain off, the declared
two units and every machine held) and off. 1,507 requests through the drills, 1,507 answered, 0 failed, 0 wrong.

## 2b. The showing with the engine's own mechanisms, 23 October evening (quick form)

The two showings above read STEADY where the organism had room, and STEADY is the reading of a room not taken (`docs/THE_ROOM.md`,
section 3). The files said where it was: in both arms no request ever waited in line at any second of any step, so the
response time was not a shortage of units but **the unit's own paper quota** (a 40 ms request inside 250 m, 25 ms of every
100 ms period, takes 115 ms or more). Omni's brain, holding the yardstick's own count with a force that never fired under the
800 ms line, was the same mechanism with packing. What was missing was the engine's own: **conveyance** (`docs/THE_ROOM.md`,
section 7), the **reflex** on work in line, the yardstick twin read as Kubernetes would read it, and the **fold under the
verdict**; all four are in the brain now (section 1). The same rig and clients, the quick form, one run of each arm:

| gauge | yardstick | Omni | Omni against it |
|---|---:|---:|---|
| requests answered (work) | 1,182 | 1,224 | up 3.6% |
| requests failed | 0 | 0 | none in either |
| answers wrong | 0 | 0 | none in either |
| response time, 50th percentile (ms) | 90 | 79 | down 12% |
| response time, 95th percentile (ms) | 176 | 146 | down 17% |
| response time, 99th percentile (ms) | 210 | 216 | up 3% |
| machine-minutes on (the bill) | 9.0 | 8.3 | down 8% |
| unit-minutes | 6.2 | 7.5 | up 21% |
| processor conveyed above the requests (core-minutes) | 0 | 0.6 | Omni's walls raised; Kubernetes never moves one |
| processor-seconds used by the units | 52.6 | 55.6 | up 6%: more work done |

Read by the one key, step by step (six pairs, the exact Student t interval): requests answered **STEADY**, up 3.6% a step
(−6.7 to +20.7); the 95th percentile **STEADY**, down 13.3% a step (−50.4 to +7.7 ms); machines on **STEADY**, down 6.6% a step
(−0.9 to +0.2); units standing **power given**, up 23.4% a step (+0.4 to +1.6). No row reads LOSS. Six pairs of 15 s are
too few for a 13% fall in the 95th percentile to clear zero; the full form (18 steps of 25 s) is read next, and the three-run
reading after it.

What the files say happened. Omni's lone units stood at 370 m (the room under 75% of a half-processor machine), read back
from the kernel's own `cpu.max`; two were handed back to 250 m when a second unit joined their machine. The units Omni held
rose above the yardstick's (2 → 4 → 5 → 6 → 7 → 9 against 2 → 2.5 → 4 → 5 → 5 → 6): the twin follows the work, and Omni's
faster answers brought more requests from the closed-loop clients, so more processor was used and Kubernetes' rule asked for
more units. The one mechanism that takes units back below the twin, the verdict, ran one trial in 90 s and refused it as a
LOSS: its reference phase measured under one client and its trial phase under two (the clients stepped between them), so what
it read was the traffic, not the step. A trial is paired under the same traffic; the brain now abandons a phase whose
arrivals move by more than 15% (the traffic gate, written after this run, before the full form). On this rig the count has
no room in any case (`docs/THE_ROOM.md`, section 8: with one to four clients the yardstick's count is already the edge); the
room here was the quota, and conveyance took it.

**One body**, quick form (3 → 6 → 3 clients over 36 s): 612 requests, 0 failed, 0 wrong, the 95th percentile 279 ms beside
the batch; 8 of 16 tasks finished inside the 36 s window (the full form runs the job to its end). **The drills**, with four
clients running through all of them: a unit killed and started again, a machine lost with two units (placed again) and
repaired, the control plane killed for 10 s and started again (nine units kept, the same nine after the replay), the kill
switch on (every wall back to its request, the declared state held) and off: 1,680 requests, 1,680 answered, 0 failed,
0 wrong.

## 2c. The full form, 23 October evening: native against Omni direct, 18 steps of 25 s

The same rig and brain as 2b, the long form (the clients 1 2 3 2 3 4 3 4 5 4 5 6 5 6 7 6 7 8, 25 s a step, 450 s an arm; one
run of each arm, class L, every number from the run's own files):

| gauge | native | Omni direct | Omni direct against native |
|---|---:|---:|---|
| requests answered (work) | 9,991 | 10,461 | up 4.7% |
| requests failed | 0 | 0 | none in either |
| answers wrong | 0 | 0 | none in either |
| response time, 50th percentile (ms) | 100 | 90 | down 11% |
| response time, 95th percentile (ms) | 184 | 168 | down 9% |
| response time, 99th percentile (ms) | 218 | 216 | down 1% |
| machine-minutes on (the bill) | 45.0 | 44.2 | down 2% |
| unit-minutes | 61.1 | 54.8 | down 10% |
| processor conveyed above the requests (core-minutes) | 0 | 1.2 | Omni's walls raised; Kubernetes never moves one |
| units below the twin the verdict allowed, at most | 0 | 1 | one step, kept |

**Read by the one key, step by step (18 pairs, the exact Student t interval):** requests answered **GAIN**, up 4.7% a step
(+14.8 to +37.4 requests a step, the interval clear of zero); the 95th percentile **GAIN**, down 9.9% a step (−31.3 to −4.9 ms,
clear of zero); units standing **GAIN, a cut**, down 10.3% a step (−1.5 to −0.2 units, clear of zero); machines on **STEADY**,
down 1.7% (−0.2 to +0.0). No row reads LOSS. More work, faster, on fewer units, on the same machines, nothing failed: the
first reading of Omni direct against Kubernetes' own rule that the key calls GAIN, and still one run of each arm,
not the three-run reading.

Where it came from, in the files. Conveyance stood a mean of 160 m above the requests across the run (18 walls raised, 2 handed
back when a second unit joined a machine), so the lone units answered at their machines' speed: the 50th percentile 100 → 90 ms.
The verdict ran 12 trials: 9 abandoned by the traffic gate (the arrivals moved more than 15% inside the phase), 2 refused (the
muscle was slower at the step), 1 allowed at 140 s (the response times at one unit below the twin read GAIN within the
allowance), kept to the end: that is the unit cut, 10% fewer units for more work. Machines stayed STEADY because on this rig the
count has no room (`docs/THE_ROOM.md`, section 8) and six half-processor machines are the whole fleet; the cut would reach the
machines on a fleet where the count has room. **One body** (3 → 6 → 3 clients, 120 s): 16 of 16 tasks finished, the service
2,447 requests, 0 failed, 0 wrong, 95th percentile 162 ms. **The drills** (four clients): a unit killed, a machine lost and
repaired, the control plane killed and started again (every unit taken back), the kill switch on and off: 3,308 requests,
0 failed, 0 wrong.

## 2d. The three arms together: native, Omni on native, Omni direct

The founder's order of 23 October, evening: the three arms are always shown together. **Native:** Kubernetes' rule on the
muscles (the yardstick). **Omni on native:** Omni-Compass on top of that rule, the engine's strict form as on the kind rigs: the
units are the rule's and never fewer, Omni adds a unit the beat work waits and past the wall, conveys each unit's wall, places by
the busy rule, packs, parks and wakes machines (brain `omni_native`, `omni_orchestrator/control.py`). **Omni direct:** Omni-Compass
on the muscles directly, itself the brain, the orchestrator and the scheduler, because in this one test it carries every one of
those muscles (the placement, the room rule, the machines, built from scratch for it); no Kubernetes (brain `omni`). This is the
only test where the word direct holds: on a Kubernetes stack Omni-Compass is a brain with no organs and can be direct to a knob
only, never to a muscle (the founder's analysis of 31 October). Where it does not carry a muscle, that muscle stays, native, under
it: a knob left with no working controller fails the whole system and is never a result (`docs/SOLO_PREREGISTRATION.md` amendment 2). Every pair is read by the one key, paired by step: Omni on native against native,
Omni direct against native, and Omni direct against Omni on native. The showing runs all three in one go
(`tools/orchestrator_show.py`), the report carries three columns, and the GitHub run (`orchestrator.yml`) prints the three.

**The first three-arm showing, and the fault it found** (quick form: six steps of 15 s, one run of each arm, class L). Omni on
native against native and Omni direct against native read no LOSS, but Omni direct against Omni on native read work LOSS (down
5.2%, 10.5 requests a step fewer, every step at or below). The run's own files show why. Every trial the verdict began in that
run was abandoned by the traffic gate, because the clients step every 15 s, faster than a trial can be judged; each trial still
held one unit below the twin while it ran (5 to 15 s at a time), and one trial's step was counted from a twin the traffic had
since raised (the phase began at a twin of 5, the twin rose to 6, the trial's step went to 4). The brain is fixed in two places,
both the orchestrator's own (the verdict, `omnicompass/verdict.py`, is in the engine's fingerprint and untouched):

- a trial the traffic abandons holds the next one off for 6 beats, doubled at each abandonment in a row up to the verdict's
  recheck (24 beats), and a trial judged to its end clears the hold (`omni_orchestrator/control.py`); a trial that cannot be
  judged is not paid for again and again;
- during a phase the step is counted from the higher of the twin as the phase found it and the twin now
  (`omni_orchestrator/brain.py`): the floor never follows the count down and never stays below a twin the traffic has raised.

Both are held by unit tests (`tests/test_orchestrator.py`, 20 tests).

**After the fix** (the same quick form, one run of each arm, class L; nothing failed and nothing wrong in any arm):

| gauge | native | Omni on native | Omni direct |
|---|---:|---:|---:|
| requests answered | 1,167 | 1,264 | 1,273 |
| 95th percentile (ms) | 149.9 | 141.3 | 126.6 |
| 99th percentile (ms) | 210.1 | 206.5 | 167.8 |
| machine-minutes | 9.0 | 8.5 | 8.5 |
| unit-minutes | 6.17 | 8.42 | 7.62 |
| failed, wrong | 0, 0 | 0, 0 | 0, 0 |

Read by the one key, paired by step:

- **Omni on native against native:** work GAIN, up 8.3%; the 95th percentile STEADY, down 1.9%; machines STEADY, down 5.6%; units
  power given, up 36.5%.
- **Omni direct against native:** work GAIN, up 9.1%; the 95th percentile STEADY, down 14.8%; machines STEADY, down 5.6%; units
  power given, up 23.5%.
- **Omni direct against Omni on native:** work STEADY, up 0.7%; the 95th percentile GAIN, down 13.2%; machines STEADY; units GAIN, a
  cut, down 9.5%.

The batch job beside the service: 746 requests, 0 failed; the drills: 1,711 requests, 0 failed. Two trials began in 90 s and
the traffic gate abandoned both (the second held the next off for 12 beats), so no step was allowed: in the quick form Omni
direct's edge over Omni on native is its own reflex and conveyance with fewer units, not the fold. One run of each arm on one
host.

**The three runs on GitHub's machines** (the full form: 18 steps of 25 s, the busy room rule, A, B and C from one commit, `0ca2bbdac`, omni-v18's bytes; runs 40023524338, 40023529155 and 40023534013, their files on the branch `raw`; the table `results/orchestrator/V18_THREE_ARMS_ABC.md`, written by `tools/orchestrator_abc.py` from the runs' own summaries):

| Pair | Work | The 95th percentile | Machines | Units |
|---|---|---|---|---|
| Omni on native against native | **GAIN in all three** (up 5.2%, 5.3%, 7.4%) | **GAIN in all three** (down 9.0%, 12.1%, 7.5%) | STEADY (down 2.2%, 4.6%, 2.4%) | power given in all three (up 11.0%, 8.9%, 10.8%) |
| Omni direct against native | **GAIN in all three** (up 7.3%, 5.7%, 9.4%) | **GAIN in all three** (down 9.8%, 15.7%, 10.8%) | STEADY (down 2.2%, 3.1%, 2.2%) | STEADY (up 6.9%, down 0.3%, up 9.0%) |
| Omni direct against Omni on native | STEADY (up 2.0%, 0.4%, 1.9%) | STEADY (down 0.9%, 4.1%, 3.6%) | STEADY | STEADY (down 3.7%, 8.5%, 1.7%) |

No LOSS in any pair in any run; nothing failed and nothing wrong in any arm of any run (28,528 to 34,837 requests a run across the three arms), the batch job and the drills included. Both Omni-Compass arms do more work than native, answer faster, and pay for it in units (power given); Omni direct and Omni on native read STEADY against each other on every gauge in the three runs. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.


## 3. What it covers, and what it does not yet

Covered and shown: the desired state kept and survived (the journal), placement by room, a unit's whole life (start, probe,
restart, stop), processor and memory walls, one address with the load shared, units scaled with the load, machines woken
and parked, batch beside a service with the service first, a machine lost, a kill switch, an audit of every decision.

Not yet: many hosts over a network (the hands already answer over HTTP; the showing ran on one host), container images and a
registry (units are processes), network isolation, service names and encryption, storage that follows a unit, rolling updates
of a new version, secrets, users and permissions. The comparison that matters, this orchestrator against Kubernetes itself on
the same organism and load, runs on the kind rig on GitHub and has not run yet.

Ready, not yet run: the same full form on a rented machine in a cloud, one machine of 8 processors, the test `direct` on the
one-machine buttons (`big-organism-detached.yml` on Azure, `cloud-organism.yml` on Google and Amazon; `scripts/organism_detached.sh`):
a dry run by default, shown at its price, rented only on the founder's word.

## 4. The claim, exactly

Omni-Compass can run the showing's organism (a checked service and a batch job) without Kubernetes, with its own scheduling,
scaling, lifecycle, recovery and coordination, on one host, with no request lost through a unit's death, a machine's loss,
the control plane's death or the kill switch. With the engine's own mechanisms in its brain (conveyance, the reflex, the twin
read as Kubernetes would, the fold under the verdict), in one full-form run of each arm on this rig (section 2c) it read
against Kubernetes' own rule: work GAIN (up 4.7%), the 95th percentile GAIN (down 9.9%), units GAIN, a cut (down 10.3%),
machines STEADY, nothing failed and nothing wrong. That is one run of each arm, class L, on one host: the three-run reading (A,
B and C on GitHub's machines from one commit) and the comparison against Kubernetes itself on the kind rig are what would make
it a benchmark result. Equivalent output and complete functional coverage of a declared organism are targets to engineer
toward, not results this showing establishes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
