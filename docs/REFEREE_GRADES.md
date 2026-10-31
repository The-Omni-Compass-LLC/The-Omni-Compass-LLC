# The referee's grades, category by category, and the plan to raise each

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Our own grading of Omni-Compass in twenty categories, the way a referee or an underwriter would grade a study and a
product: the grade given on the morning of 19 October, the grade the evidence supports now, the highest grade the
category can reach, and what reaching it takes. These are The Omni-Compass LLC's own grades; no outside party has graded,
reviewed or approved them. A category with no measurement yet is **Undetermined**, never failed, and is graded once its
measurement exists.

## The chart

| # | Category | Morning of 19 Oct | Now | Highest reachable | What reaching it takes |
|---:|---|:-:|:-:|:-:|---|
| 1 | Concept | B+ | **A−** | A | an outside reading of the concept against its precedents (`docs/RELATED_WORK.md`) |
| 2 | Engine code | B− | **B** | A | the next version's fixes (below), coverage of every engine file at 90%, mutation testing of the core; an outside code review for A |
| 3 | Engine stability | C− | **C+** | A | one version standing through its whole campaign, every benchmark's three runs, unchanged |
| 4 | Mathematics | C+ | **A−** | A | CERT-10 proved for every fixture and the bath's amplitude as a number (`docs/ENGINE_PROOFS.md`, section 5) |
| 5 | Method | B | **A−** | A | rules timestamped outside our repository before their runs; the pairs the power page asks for |
| 6 | Real Kubernetes | B− | **B+** | A | every Kubernetes test's three omni-v11 runs in (seven waiting on their third run), and the cloud's multi-machine cluster |
| 7 | Databases and caches | C | **B−** | A− | more pairs a run (`docs/POWER.md`), the max for MySQL, MongoDB and PostgreSQL (archiving), gains where the knob has room |
| 8 | Cloud bill | Undetermined | Undetermined | graded on its result | the Azure sets at the cap (running), then Google and Amazon |
| 9 | Energy | Undetermined | Undetermined | graded on its result | a physical meter: Kepler and the machine's own meter on a bare-metal machine |
| 10 | GPU | Undetermined | Undetermined | graded on its result | the Lambda runs from one exact commit, on the founder's word |
| 11 | Modelled muscles | C− | **C−** | B | each plant model calibrated against a measured system, with its error stated |
| 12 | Outside simulators | C+ | **B−** | A | the swarm's three runs on omni-v12, which carries the reflex fix, with its judged collision row and draws beyond the fixed seeds (below), and BOPTEST beside CityLearn |
| 13 | Robustness | B | **B+** | A | the omni-v11 kill and long-run tables are in (no LOSS, every hand-back inside its allowance); next the extended-fault table, a longer after-kill window, then a multi-machine cluster |
| 14 | Reproducibility | B | **A** | A+ | an outside party rebuilding the tables from the receipts |
| 15 | Honesty | A− | **A** | A+ | an outside audit of the receipts against the pages |
| 16 | Manuals | C+ | **B−** | A | an editorial pass of both manuals at referee level, every figure and table against the code |
| 17 | Legal | B− | **B** | A | outside counsel's review of the license and the enterprise terms |
| 18 | Automation | B+ | **A−** | A | the Kubernetes three-run tables built by a bot as the data stores' are; one page of every bot's health |
| 19 | Security | C | **B+** | A | the next version without a shell for commands that hold no pipe, signed releases, an outside penetration test |
| 20 | Production readiness | Undetermined | Undetermined | graded on its result | a pilot on a customer's own system (`docs/PILOT_PROTOCOL.md`) |

## What moved each grade (19 October)

1. **Concept.** Where the idea comes from and what it adds, against supervisory control, reference governors, the
   Simplex fallback and online experiments (`docs/RELATED_WORK.md`).
2. **Engine code.** 71% of the engine's 9,685 statements run under the tests (`docs/ENGINE_COVERAGE.md`, measured again on the omni-v15 tree): 82% of the 6,579 in the files that stood before omni-v15, 49% of the 3,106 in the eight runners it took into the fingerprint, which their own benchmarks run whole on GitHub; every proved
   property checked on thousands of generated cases (`tests/test_engine_properties.py`); every static-scan finding fixed or
   reviewed (`docs/SECURITY_SCAN.md`). Held at B by a fault found in the swarm's wire, whose code did not do what its own
   comment says (`docs/LIMITATIONS.md`, section 3), and by the wires outside the fingerprint (`docs/CHANGE_CONTROL.md`).
3. **Engine stability.** The rules and the record of every version, why it changed and how results stay tied to it
   (`docs/CHANGE_CONTROL.md`); the pace itself is unchanged.
4. **Mathematics.** 24 of 24 theorems proved by machine on the engine as it executes: the compass law, the plug, the verdict,
   the invariance of E, I and S, the tracking bound inside the basin and the steps to reach it, and the bath's stability
   (`docs/ENGINE_PROOFS.md`).
5. **Method.** The smallest change every judged row can see (`docs/POWER.md`); every change to every preregistration with
   its timing (`docs/DEVIATIONS.md`); the chance of a false three-run reading, 3.1 × 10⁻⁵ a row (`docs/LIMITATIONS.md`).
6. **Real Kubernetes.** The omni-v11 tables for Goldilocks, both KEDA setups and fixed capacity: 0 LOSS; the omni-v10 LOSS
   reads STEADY; Omni-Compass's 95th and 99th percentiles below native's in all 90 paired repetitions
   (`docs/TAIL_LATENCY.md`).
7. **Databases and caches.** Ten omni-v11 tables, 0 LOSS; native as shipped kept apart from the operator's setting (a fault
   in the front page's grouping found and fixed before any table mixed them).
12. **Outside simulators.** CityLearn 27 GAIN, the power grids 67 GAIN, the robot arms 7 GAIN, the swarm 9 GAIN, 0 LOSS in
   all four on omni-v11, each rebuilt byte for byte. Held at B− by a fault found in the swarm's wire: on a mission draw outside
   the preregistered seeds it let drones collide where native did not. The fix held every drone outside the keep-out on all
   ten cells and draws tried (`results/model_gate/V12_SWARM_REFLEX.md`) and landed in omni-v12; the grade moves when its three runs land.
14. **Reproducibility.** All 23 omni-v11 tables rebuilt from their raw receipts and identical to the byte
   (`tools/reproduce.py`, weekly in `reproduce.yml`); every package pinned with its hashes, every action by its commit.
15. **Honesty.** The limitations page, the tail-latency page, the runs-disagree rows each explained, every row kept.
16. **Manuals.** Eleven referee chapters bound into the Owner's Manual (the proofs, the coverage, the power, the deviations,
   the limitations, change control, the security scan, the licenses, related work, the tail latency, these grades).
17. **Legal.** The bill of materials (CycloneDX 1.5, SPDX 2.3) and every dependency's license, with no strong copyleft
   allowed (`docs/DEPENDENCY_LICENSES.md`).
18. **Automation.** Every finished run archived by itself; the reproduction and the security scan run by themselves; the
   conductor stamps each capacity run with its own letter.
19. **Security.** Bandit over 34,000 lines with every high and medium finding fixed or reviewed; 0 known vulnerabilities in
   the 29 pinned packages; every package hashed; 407 action uses pinned to their commits (`docs/THREAT_MODEL.md`, T8 closed).

## The blueprint

**On GitHub already, at no cost.** The robustness kill test and long run and the three data stores at the max landed on 19
October (no LOSS in any); the third runs of the seven Kubernetes sets, the extended fault test and the CruiseKube rerun on the
corrected recorder are running, and the cost to match runs again from the campaign. Each lands as an omni-v11 table and
raises categories 6, 7 and 13.

**The next engine version, on the founder's word** (`docs/CHANGE_CONTROL.md`: any change to a rule or guard is the next
version, and every benchmark runs again on it):
- the swarm's proximity reflex at once, reaching out with the square of the speed (in our own flights: every drone at or
  outside the keep-out on the four preregistered cells and six draws the wire was never run on, where omni-v11 collided once),
  with a judged collision row and draws beyond the fixed seeds in its preregistration;
- every wire that holds a governor's rules taken into the fingerprint;
- a command with no pipe run without a shell;
- the Redis harness's brain in its own process, as a deployment runs it;
- the Kubernetes governor counting a worker an add-on marks while it serves, and keeping its clock under load.

**What a buyer will ask for that is not here yet** (the founder's question of 19 October, answered from the repository):
- *Proof*: a physical meter (every energy figure is a declared model; the GPU on Lambda or a metered machine closes it); a cloud
  bill on the engine that stands (Azure running, Google's key and Amazon's plan pending); native at its best (the cost to match,
  native tuned harder by its operator beside Omni-Compass on top, last run on 3 October on an engine long gone, runs again on
  omni-v11 from the campaign); an outside party's rerun; a real multi-machine cluster (kind puts every node on one runner);
  days to weeks on a real workload; each rule's share of the gain read on the live cluster, not only in our models.
- *Gauges*: measured joules and grams of carbon; the cost of 1,000 requests; the 99.9th percentile (the probes are too sparse
  for it); the operator's own terms (availability, error budget, burn rate) beside the alert minutes; each muscle's headroom to
  its own limit; the governor's own calls to the cluster's API. Now read for every omni-v11 Kubernetes table
  (`results/STEERING.md`): moves, reversals and distance travelled an hour, the share of decisions with the compass in its
  band and at the line, the time from the line back into the band, and errors an hour.
- *The operator's screen*: in. The gauges feed and a Grafana screen (`tools/omni_exporter.py`,
  `deploy/grafana/omni-compass.json`, read-only); ten alert rules (`deploy/prometheus/omni-compass-rules.yaml`); and the control
  panel (`tools/omni_control.py`): an authenticated API with an OpenAPI document and a console with the buttons (mode autopilot,
  watch or off; the dial, max or tune-down; reset to native; the kill switch for every governor on the machine; the two-person
  arm), roles on every button and every press logged. It writes no setting itself: every change goes through the governor's own
  hand-back and a restart with the new arguments, so the engine does not change for it (`docs/OBSERVABILITY.md`). Still to
  build: a row per muscle with its own hand-back and watch-only buttons (the engine that stands takes its mode for the whole
  governor, so that comes with the next version, through the model gate); the live native-against-Omni panel; a one-line install
  (a Helm chart); two governors with leader election.

**Mathematics.** CERT-10 for every fixture by entry bounds taken cell by cell instead of over the whole box; the bath's
amplitude from a discrete Lyapunov function per cell.

**Tests.** Every engine file to 90% coverage; mutation testing of the core, the compass law and the verdict.

**Outside parties** (the founder decides each): a referee's review, a penetration test, counsel's review of the license,
and an independent replication from a fork.

**The undetermined categories.** The Azure sets at the cap are running; a bare-metal machine with Kepler and its own meter
measures energy; the Lambda runs measure the GPU from one exact commit; a pilot measures production.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
