# Omni v4, ordered and designed: the collective mechanism, one body and one brain, every wire forced through it

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

First written 2026-10-09 (the brain's verdict on every muscle, inside the engine) and rewritten 2026-10-10 from the founder's
orders of that afternoon. The engine in this tree is still Omni v3 (`OMNI_V3.json`, digest `b53d05449ee04c4b`, 40 files): nothing
in this page is built in it yet. By the standing order, any change to a rule, gain, guard, preset or muscle makes the next version,
every result is run again on it, and the engine is never changed without the founder being told first. This page is the telling
and the work order. The founder gave the word on 10 October 2026.

## 1. The order, in the founder's words made rules

1. **The reflex rule is the whole mechanism.** Signal out, the muscle moves, the brain feels the full reaction, then it decides. A
   trial runs to its full measurement and is never ended by the calm it causes. Only the wall (a fail-up) or the engine's own time
   limit ends a trial early. The rule the harness broke on 10 October (every Kafka spend trial abandoned the second the spend
   calmed the service) becomes the engine's own rule, and every wire is forced through it.
2. **No forcing.** The brain never moves a muscle because it wants to. A spend is tried only when the muscle's own reading says
   there is something to buy (messages waiting, a cache missing, clients queued). A give-back is tried only when the whole body is
   calm. The compass force is an urge from where each service sits in its band: smooth (tanh), never a hammer.
3. **Collective processing.** One body, one brain, one tick a second. Read everything first: every muscle's state, every service's
   speed and work, the host's CPU, memory and energy where a meter exists. Then decide. The cost the brain judges is the body's
   cost (all the work, all the speed, all the machines, all the resources: the Omni index's own arithmetic), never one muscle's.
4. **Hurt nothing anywhere.** On top of the body's cost, a guard for every part: a step is refused if any one service read LOSS
   beyond its cushion even when the body's total improved. Pushing one thing to a LOSS to move another toward its own is refused by rule.
5. **One trial at a time inside a body.** If two muscles move together the brain cannot tell which one caused the reaction. The
   body grants one new trial at a time, to the muscle asking loudest whose own condition holds. Every other muscle keeps acting
   inside what it has already proven. Nothing is frozen; only new trials wait their turn.
6. **Nothing is permanent.** Every allowed step is re-tested on the recheck and pulled back when it stops paying. A muscle at
   native is asked again whenever its signal returns. Native is never a verdict, only where the brain stands when it has not yet
   been shown a reason.
7. **The wall belongs to the body.** If any service hits its line, the trial stops, that step is undone, and the brain's forces turn
   to brake across the body: the law's brake, not a reset.
8. **Everything is wired.** Every muscle gets both wires, always. Staying native is the brain's live decision every second, from the
   muscle's own state, the whole system's state and the law's force. It is never a one-time verdict from one run, and nothing is
   unwired because of one reading. The order of 9 October ("where a run reads native ahead, leave the knob native and watch
   first") is replaced by this one: the watching is the brain's own job each second.
9. **Six organisms.** (1) Compute / AI / Cloud, 430; (2) Physics / Robotics / Autonomous, 376; (3) Energy / Facility / Industrial,
   470; (4) Distribution / Specialized, 440; (5) all realms stacked together, every muscle used in every realm, 1,716; (6) the whole
   catalog, every muscle once, 945. Each runs native and with Omni on; each at 1, 10, 100 and 1,000 copies; each 1, 10, 100 and
   1,000 times; both values in every square. The live software products (Redis, Kafka, PostgreSQL, MySQL, MongoDB and the rows
   to come) are never counted beside the organisms.
10. **Realms re-cut by a written rule.** The rule, not a person, decides how many realms there are (for example: the muscles that
    share one kind of native controller and one kind of physics form a realm). The families are cut by it; Distribution /
    Specialized is today's catch-all and the one most likely to split; organisms 5 and 6 are rebuilt from whatever the realms
    become. New muscles enter the catalog at v4 and every realm is recounted.
11. **Words.** Our own models are "modelled" (evidence class S, never in the headline); live software is "the real thing" (class L);
    a physical meter is class P. "Simulation" stays only in the license's own phrase and in the names of third-party simulators.
12. **Reports.** We build every table, receipt and reading from the raw files with our own code; GitHub runs the jobs and stores
    the files; the raw files are archived with checksums. Every row is shown, always, native and Omni, plus or minus. A row that
    comes out LOSS in all three of our runs is a bug report against our own wiring: fix the wiring, run again, the rerun becomes the result of
    record, the earlier set stays in `docs/history`. No row is ever dropped.
13. **The card and the two clouds** are written onto the same mechanism before they run: the same probe first, snapshot once, wire
    owned by the brain, reflex rule, body judgement, three runs, receipts, archive. The GPU controllers are inside the engine and
    predate the verdict; bringing them onto the body is part of the v4 writing. GPU runs happen on v4, on one named commit, after
    the CPU side. Nothing is paid for twice.
14. **The founder hears what a result says before it goes up.**

## 2. What already does this, and where it stops

- **The engine's verdict** (`omnicompass/verdict.py`): a paired trial on the muscle itself before a slow knob is moved. In v3 it
  guards the Kubernetes controller's machines, the robot arms' speed override and the drones' cruise. It does not guard every
  muscle, it judges one knob's cost, and the condition under which a trial is fair is left to each harness.
- **The live harnesses** (`tools/knob_verdict.py`, since 9 October): the same verdict around every live knob of the database,
  messaging and cache products, with the declared objective, outside the engine. Its trial-ending rule was wrong for spends until
  amendment 3 of 10 October; and the second set of that day showed the measurement itself is unreliable (section 4).
- **The modelled realms** (`realms/harness.py`): one governor reads the organism's aggregate and its one directive sets every
  muscle's knob. No muscle is tried before it is moved; that is where the 13 trade muscles of the realms table come from.

## 3. What v4 changes (engine files, so a new fingerprint)

- **A new engine file, body.py in the omnicompass package: the body.** Holds every wire of one organism or stack. One `tick` a second: gathers every muscle's
  reading and every service's gauges; computes each muscle's compass force (the law, unchanged); computes the body cost (the
  index's arithmetic over the body's work, speed, machines and resources); grants at most one new trial per tick to the muscle
  asking loudest whose own condition holds; runs the reflex rule for the trial in flight; applies the per-part guard; hands every
  wire its target. The wall: any service at its line ends the trial, undoes the step, and sets every force to brake.
- **`omnicompass/verdict.py`, changed.** The trial-ending rule inside the engine: a spend trial runs to its samples; a give-back
  trial ends when the body leaves calm; both end on the wall or the time limit. The per-part guard joins the judge: a step passes
  only if the body cost did not rise within the tolerance and no service's own cost rose beyond its cushion. The four trial rules of
  section 4 are the trial's own.
- **A new engine file, wire.py in the omnicompass package: the wire belongs to the brain.** Snapshot once, restore, the foreign-writer check, and a write
  reachable only from the body's tick. Every harness, controller and realm plant plugs its knob in through it; none writes around
  it. "Written in every wire" is enforced by construction, not by copying a rule into every file.
- **Every controller through the body**: `omni_controller/muscles.py`, `omni_controller/gpu_compass.py`, `gpu_governor.py`,
  `realms/harness.py`, `realms/compass_arm.py`: the Kubernetes controller's machines, the robot arms' speed, the drones' cruise, the
  card's power and clocks, every realm muscle.
- **`tools/knob_verdict.py`** becomes a thin adapter over the engine's body for the live harnesses (Redis, Kafka, PostgreSQL, MySQL,
  MongoDB, CPU power, and the rows to come); its own trial rule is deleted. The engine's rule is the only one.
- **`realms/catalog.csv`**: one numbering (families 1 to N, the `AUDIT` labels on 98 muscles in 8 families replaced; the register's
  section 1 reads the CSV's numbering, one source instead of two); one `objective` column (resource by default, service where an
  operator would declare it); the new families and muscles of section 5; vendor-neutral names in the card's family.
- **The body grouping rule**, written in the preregistration before the first v4 run: one trial at a time inside a body; bodies
  that share nothing run their trials side by side; ten organisms stacked in a cluster are ten bodies sharing one host, so the
  collective judgement runs inside each body and across the bodies for what they share. How the catalog's muscles are grouped into
  bodies is the one design decision put to the founder with the written plan before the first run.
- **One test set on every kind of wire**: (a) a muscle whose spend calms the service instantly (the Kafka case) is judged, never cut
  off; (b) a muscle whose spend helps itself and hurts a neighbour is refused; (c) two muscles asking at once are taken in turn;
  (d) the wall ends the trial, undoes the step and brakes the body; (e) a refused muscle is asked again when its signal returns;
  (f) a hand-back restores every snapshot. A wire that does not pass the set is not plugged in.
- **The fingerprint**: `OMNI_V4.json` at the root, a v4 record page beside `docs/OMNI_V3.md`, `tools/omni_version.py` reading
  both; the older fingerprints go to `docs/history` as the road to 1.0, never as a second product.

## 4. The four trial rules the second set of 10 October taught

The five live products ran a second time on the amended trial rule (`docs/RERUN_2026-10-10.md`). The trials finished, and the
brain still refused the Kafka consumer almost every time. In the one repetition where it allowed the third consumer early, the
whole gain of the earlier law came back at a fraction of the spend: p95 2,450 ms to 57 ms, the queue from 3,375 waiting messages
to 253, work inside the line +17%, with 2.52 consumers on average where the earlier law spent 5.8 to 7.9. The gain is real and
cheap; the test of it is a coin flip. The faults are the harness's measurement, read from `tools/run_kafka.py`: the cost sample is
the age of the backlog, which does not fall until the backlog is gone; a joining consumer rebalances the group and the pause eats
the settle; the reference and the trial phases, fourteen seconds each, straddle a thirty-second load step and compare different
loads. On Redis with the large working set the brain allowed 15 MB more and bought more hits, more work and less host CPU, a row the
earlier law never showed because it spent 200 MB; with the small working set a 4 MB notch cannot show a gain the tolerance can
see, though forty notches together did under the earlier law. Hence:

1. **Samples count only once the muscle reports itself settled** (the group's assignment stable, the backlog's age no longer the
   reading), not after a fixed settle.
2. **A spend on a queue or a cache is judged by the muscle's own reading**, the lag and its drain rate, the misses, with the body's
   cost taken at the settled state, never by a lagging gauge alone.
3. **The reference and the trial are compared at the same load**, or the trial waits for a steady step (the cruise).
4. **Coarse to fine.** When single notches read flat, one scout step to the far side of the cover decides whether a hill exists at
   all; if the far point pays, the allowance opens to the proven point and the fine steps follow. A hill of forty notches is not
   refused one notch at a time.

The founder's words of 10 October, exactly: what the brain sends to a muscle has to coincide with what the muscle sends to itself
and where it is at.

## 5. The final sweep of 10 October, and what enters the catalog

The register's three lists (benchmarked, queued, excluded) and the catalog's 59 families were walked against the most-used open
software of 2025-26 (GitHub's own report: the fastest-growing projects by contributors were vLLM, cline, Home Assistant, RAGFlow
and SGLang, beside VS Code, Godot and Flutter; the cloud-native foundation's top tier, OpenTelemetry the latest), the mega-caps'
open code and the open analogs of their closed systems, and every domain the founder named. Each proposed knob was checked on the
project's own documentation.

**Already covered.** The Linux kernel's clock floor, clock ceiling and processor power cap are muscles of Host CPU & Memory; the
cloud autoscaler's node pool bounds and spot mix are muscles of Node Fleet and Cloud VM & Capacity, so a second or third cloud adds
a rental layer, not a muscle; the NVIDIA card has its own family. Finance, media, telecom radio, space, medicine, nuclear (model
only), self-driving, electric cars, robotics, drones, grids, buildings, water, agriculture, mining and fabs are in the register.

**Added to the register** (`docs/REGISTER.md`): rows 74 game server fleets (Agones), 75 ledger nodes (Bitcoin Core; machinery only,
consensus excluded by rule), 76 build farms (actions-runner-controller), 77 network security engines (Suricata), 78 device message
brokers (EMQX, Mosquitto); lines on rows 9 (Home Assistant as a candidate controller), 13 (the OpenPLC runtime as a candidate PLC),
19 (SGLang beside vLLM), 32 (NASA's open flight software, cFS through NOS3), 42 (the 5G core, Open5GS or OpenAirInterface); any
vendor's card in section 2.3 (AMD's power cap is NVIDIA's muscle under another name).

**The catalog at v4** (exact when written):

| Change | Families | Muscles, about |
|---|---:|---:|
| Financial Markets & Trading Systems (matching threads, order admission, risk-limit pools, gateway sessions; never a trade) | +1 | 12 to 16 |
| Media Streaming & CDN (bitrate ladder cap, buffer target, transcoder workers, edge cache size and TTL) | +1 | 12 to 16 |
| Game Servers & Real-Time Interactive (fleet buffer and bounds, tick budget, player cap, matchmaking admission) | +1 | 10 to 14 |
| Blockchain & Ledger Nodes (cache, mempool, peers, validation threads; never consensus) | +1 | 8 to 12 |
| CI/CD & Build Farms (runner bounds, concurrency, cache size, job admission) | +1 | 8 to 12 |
| Security engines into Reliability, Security & Recovery (capture threads, ring sizes, rule-group admission) | 0 | +4 to 6 |
| Device brokers into Messaging & Streaming; edge into Cross-Cluster & Edge; DNS and mail caches into Runtime & Application | 0 | +8 to 12 |
| Robotics widening (ROS 2 executors and QoS, drones by name, humanoids' balance and gait margins): the thinnest realm owns 119 muscles | 0 | +12 to 18 |
| GPU family vendor-neutral (renames) | 0 | 0 |
| **Total** | **64** | **about 1,020 to 1,050** |

**The closed systems, by their open analogs.** Borg is Kubernetes' own ancestor: Google's Borg paper says its lessons were applied
to Kubernetes, and Borg's top contributors built it (Omega is a sibling branch). Kubernetes' muscles are therefore Borg's muscles.
The same reading, company by company:

| Company | Closed system | Open analog carrying the same muscles | Rows |
|---|---|---|---|
| Google | Borg, Omega; the GKE autoscaler | Kubernetes, Knative; the same autoscaler, rentable | 1 to 9, 17, 46, 63, 68; 38 |
| Amazon | EC2 Auto Scaling, EKS | Karpenter (Amazon's own, open), EKS | 38, 68 |
| Microsoft | Azure, AKS | done | section 2.2 |
| Meta | Twine, TAO, Scuba | Kubernetes; RocksDB and Cassandra (Meta's own, open); Presto and Trino | 24, 25, 44 |
| NVIDIA, AMD | the card's governor | the card's own power limit and clocks (`nvidia-smi`, `amd-smi`); Triton, TensorRT-LLM, vLLM | section 2.3, 19, 20 |
| Tesla | Autopilot, the BMS | Autoware, openpilot, FASTSim, PyBaMM | 58, 59, 8 |
| SpaceX, Blue Origin | flight software | NASA cFS and NOS3, F Prime, Basilisk, RocketPy | 32 to 35 |
| Netflix, Disney, YouTube, TikTok | CDN, gateways, streaming | Varnish and nginx caches, Envoy, dash.js, FFmpeg | 71, 43, 41, 57 |
| NASDAQ, ICE, CME, Bloomberg | matching engines, terminals | exchange-core, QuickFIX | 45 |
| Visa, Mastercard, Stripe | payment switches | the serving-layer pattern; the commerce family | 43 |
| Coinbase, Binance | custody and nodes | Bitcoin Core, go-ethereum | 75 |
| EA, Activision, Riot | game server fleets | Agones, Open Match | 74 |
| AT&T, Verizon, Ericsson, Nokia | RAN and core | srsRAN, OpenAirInterface, Open5GS | 42, 21 |
| Starlink, OneWeb | constellations | Basilisk multi-vehicle, Orekit | 33, 34 |
| Siemens, ABB, Schneider, Rockwell, Honeywell | PLC, SCADA, DCS, BMS | Tennessee Eastman (Ricker), OpenPLC, BOPTEST, Sinergym | 13, 9, 10 |
| GE Vernova, Vestas, Siemens Gamesa | turbines | OpenFAST and ROSCO, FLORIS | 51, 11 |
| Westinghouse, Framatome, EDF | reactor control | none open: model only (ThermoPower and ClaRa the nearest) | 65 |
| Epic, Oracle Health, Philips, GE HealthCare | records, PACS, imaging | HAPI FHIR, MONAI, Orthanc | 53 |
| Intuitive Surgical, Medtronic | surgical robots, pumps | dVRK and AMBF servos only; pumps excluded by rule | 67 |
| Toyota, VW, GM, Bosch | AUTOSAR ECUs | Autoware, openpilot, FASTSim | 58, 59 |
| Deere | precision agriculture | AquaCrop-OSPy, pyfao56 | 52 |
| Shell, Exxon, Kinder Morgan | pipelines | pandapipes | 50 |
| Rio Tinto, BHP; TSMC, ASML | mills; fab dispatching | candidates only | 56; 66 |
| Maersk, Union Pacific, Otis, Schindler | ports, rail, lifts | none open with a shipped controller: model only | section 1 |
| Lockheed, Raytheon, Northrop | weapons release | excluded by rule; endurance and admission only | 23 |
| Oracle, IBM, Red Hat | MySQL, OpenShift, Ceph | done (MySQL); the OpenShift family; Ceph | 24, 62 |
| Alibaba, Uber, LinkedIn, Airbnb, Databricks, HashiCorp, Cloudflare, Elastic, MongoDB, Redis, Confluent | their open releases | the Alibaba trace, Jaeger and OpenTelemetry, Kafka, workflow engines, Spark, Nomad and Consul, Pingora and Envoy, OpenSearch, MongoDB, Redis | 17, 73, 26, 49, 25, 43, 28, 24, 27 |

Where a closed system has no open analog with a shipped controller, the row says model only and the organisms carry the family.
Where the controller must never be touched, the exclusions say so (`docs/COVERAGE_MAP.md`, section 3, with a ledger node's
consensus added on 10 October).

**What cannot be seen, said plainly.** Software with no open code and no open analog is modelled by its family in the catalog and
never counted in the headline. The sweep checks that every system of value is in one of the three lists; it does not check every
knob of every system, only that the kind of knob is in the catalog. The founder's own check stands: name any system; it must be in
one of the three lists, or it is a gap and gets a row.

## 6. What is expected

The 124 superior muscles of the realms table keep their wire in; the 13 trades read as watch (the trial refuses them); the
noninferior muscles stay watch; no muscle reads higher, by construction. Kafka's queue gain returns at a fraction of the earlier
consumers once the trial judges the queue by the queue; Redis buys only the memory that pays; the three databases give back what
proves to pay and lose nothing. The organisms' work per energy is expected unchanged or slightly lower (the trades no longer
contribute their energy saving), with time in violation no higher than native's everywhere.

## 7. What it costs, and how long

| Step | Where | Money | Time |
|---|---|---|---|
| Writing v4 as in section 3, with the test set and the fingerprint | here | none | about two days |
| The catalog's new families and the realm rule (section 5) | here | none | inside the two days |
| The organisms and the grid at 1, 10, 100 and 1,000 copies, A/B/C | GitHub | none | about a day |
| The seven Kubernetes tests, A/B/C | GitHub | none | one to two days, in parallel |
| The four independent simulators, A/B/C | GitHub | none | one day |
| The live products (Redis, Kafka, PostgreSQL, MySQL, MongoDB) under both objectives, A/B/C | GitHub | none | one day |
| The two big organisms at 1,000 copies | Azure, one rented machine each, about 25 hours | the same machines as the round of 10 October; the exact bill to the founder first | two days, in parallel |
| The CPU power benchmark on a real machine | the founder's tower or a rented bare-metal server | none or about $10 | a day |
| The card on Lambda, one named commit | Lambda | the founder's | after the CPU side |
| The two clouds | AWS, Google Cloud | about $12 a steady run and $22 a burst run at list price, six runs a cloud; nothing until the accounts exist | a day each to adapt the workflow |

About a week of runs in all, most of it waiting. Every v3 table stays a v3 result in `docs/history`; the index and the wiring page
are read again from the v4 tables.

## 8. The order of work

1. The fixes of 10 October (the release manifest, the cpu-power workflow file, the verifier's workflow check) and everything in this
   page, pushed as one; GitHub's own verify run checked as the record.
2. The second set's 21 runs archived; the five live products' tables rebuilt under both objectives; the index, the wiring page, the
   benefit sheet and the dossier regenerated; the first set of 10 October moved whole into `docs/history`; the founder told the
   readings first.
3. The repository keeps itself current: every finished benchmark run archived and the front page rebuilt by the workflows themselves.
4. Omni v4 written in the order of section 3, every preregistration amended for it, the version tool reading the new fingerprint.
5. Every result run again on v4 in the order of section 7; then the CPU power benchmark on the metal, the card on Lambda, the two
   clouds; then the manual's Part II gains the body chapter and the PDF is rebuilt.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
