# The coverage map: every domain with a controller, against the register

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-10 at the founder's order to check, and check again, that nothing with value is left out: no mechanism, engine,
software, muscle or hardware with a native controller that Omni-Compass could sit on top of. This page walks every domain
against `docs/REGISTER.md` (section 2: every benchmark run or built; section 4: every open benchmark still to run; section 1:
the 945 modelled muscles in 59 families) and says, for each, one of four things:

- **done or running**: a real system or an independent simulator with a three-run table, or one running now;
- **queued**: an open benchmark anyone can run, with a shipped controller as native and one knob for Omni, in the register's queue
  with an owner, to be preregistered before its first run;
- **model only**: covered by the 945 modelled muscles (class S, never counted in the headline) because no open benchmark with a
  shipped controller exists that we can run, said plainly, with the nearest candidate named where one exists;
- **excluded by rule**: a controller Omni must never touch (section 3 below).

What a row needs to enter the queue: an open benchmark or simulator anyone can run, a controller that ships with it (native), one
knob Omni can move inside that controller's own limits, gauges that read the service and the resource, and an owner to name. A
candidate that lacks one of these is said to lack it and is not named as a benchmark.

**The final sweep of 10 October (15:00 UTC).** At the founder's order the three lists were walked once more against the internet:
the most-used open software of 2025-26 (GitHub's own report of the fastest-growing projects; the cloud-native foundation's top
tier), the mega-caps' open code and the open analogs of their closed systems, and every domain the founder named. Five rows were
missing (74 to 78), five lines were added to existing rows, and five families are missing from the catalog (financial markets,
media streaming and CDN, game servers, ledger nodes, build farms) and enter it at v4. The company-by-company map of closed
systems to the open analogs that carry the same muscles is `docs/OMNI_V4_PLAN.md`, section C. The founder's check stands: name
any system; it must be in one of the three lists, or it is a gap and gets a row.

## 1. The abbreviations, each with its place

| Short | Long | Where |
|---|---|---|
| AKS | Azure Kubernetes Service, Microsoft's managed Kubernetes | register section 2 rows 10 to 12d: v1 done on 4 workers; the 40-worker fleet on v3 waits on Azure's allowance |
| EKS, GKE | Amazon's and Google's managed Kubernetes | row 38, the same method as Azure's, each a credential and an allowance away |
| HPA | the Kubernetes horizontal pod autoscaler, the native controller under every cluster test | rows 1 to 9 of section 2 (done, three runs each, rerunning today) |
| Karpenter, Cluster Autoscaler, KEDA, VPA | the node scalers, the event-driven scaler and the vertical scaler underneath Kubernetes | row 68 (added today): Omni on top of each in turn |
| KWOK | Kubernetes without Kubelet, simulated nodes by the thousand | row 9 (runs on every push) and row 63 |
| CPU | the processor's clock and power, through the Linux kernel's own governor | row 18 (built and preregistered today), row 39 (the kernel's other knobs), row 40 (Windows) |
| GPU, the card | the graphics processor's power limit and clocks | section 2 rows 13 to 18 (the founder's run on the current controller is pending), rows 19 and 20 (serving and training) |
| DPU, SmartNIC, RDMA | the network card's own processor and the fabric | model only (families 6 and 8); a real test needs the hardware |
| RAPL | the processor's own energy counter | the meter of row 18 and of the card's CPU package |
| UPS, PDU | the battery backup and the power distribution unit | row 27: the reserve is **never a lever** (excluded by rule); the other knobs of the family are model only (family 38); a real UPS with a console and a wall meter is a candidate when one is at hand |
| RAN | the radio access network | row 21 (ns-3, 5G-LENA), row 42 (srsRAN), family 58 |
| FHIR, DICOM | the health-data standards behind hospital systems and imaging | row 53 |
| FIX | the trading message protocol | row 45 |
| YCSB, TPC, HammerDB, MLPerf, Rally | the open benchmark suites for stores, databases, AI and search | rows 24, 25, 19, 20, 28 |
| ROS 2, Nav2, MoveIt | the robot operating system and its navigation and motion stacks | row 54 |
| AMoD | autonomous mobility on demand (robotaxi fleets) | row 60 |
| EV, BMS | electric vehicles and the battery management system | rows 59 (the powertrain), 8 (the cell, PyBaMM), 7 (the charger), 26 (batteries in buildings, done) |
| HVAC, BMS (buildings) | heating, cooling and the building management system | rows 9, 10, 26 (done), families 28, 29, 34 |
| PLC, SCADA, DCS | the industrial controllers | row 13 (the Tennessee Eastman process), family 35; no open SCADA benchmark with a shipped controller beyond the process models, said in section 2 |
| CDN | content delivery caches | row 71 |
| ATM | air traffic management | row 72 |
| CFD, FEA | the physics solvers | row 37: no controller, no knob, not a benchmark |
| ARC | GitHub's actions-runner-controller, a build farm's own scaler | row 76 (added 10 October, the final sweep) |
| IDS | an intrusion detection engine (Suricata, Zeek) | row 77 (added 10 October) |
| MQTT | the device messaging protocol and its brokers (EMQX, Mosquitto) | row 78 (added 10 October) |
| cFS, NOS3 | NASA's open core Flight System and its open distribution | row 32 (line added 10 October) |
| UPF | the user-plane function of a 5G core (Open5GS, OpenAirInterface) | row 42 (line added 10 October) |

## 2. The map, domain by domain

| Domain | Real or simulator benchmarks (register rows) | Modelled muscle families (section 1) | Status today | The gap, and what was done about it |
|---|---|---|---|---|
| Kubernetes clusters | section 2 rows 1 to 9: seven tests, the organisms with the cluster inside, the big organisms, KWOK | 3, 4, 5, 11, 12, 13, 15, 16 | done on v3, three runs each; rerunning today | Karpenter, the Cluster Autoscaler, KEDA and VPA underneath were in the proof program (row 5) but not in the register's queue: **row 68 added** |
| Clouds | section 2 rows 10 to 12d (Azure); row 38 (AWS, Google Cloud) | 3, 5 | Azure v1 done, the v3 fleet waiting on the allowance; AWS and Google queued | each further cloud is the same method, a credential and an allowance away |
| Operating systems | row 18 (Linux: the clock, built today), row 39 (the kernel's scheduler, network and memory), row 40 (Windows power management) | 10 | built; queued | macOS exposes no writable power or scheduler knob to a program: not benchmarkable, by survey |
| Processors and hardware | the card (section 2 rows 13 to 18), the CPU (row 18), AI serving and training on the card (rows 19, 20) | 6 (DPU), 8 (GPU fabric), 10 (host), 14 (NVIDIA hardware), 17 (quantum control) | the card pending the founder's run; the CPU waiting for a machine | DPUs, fabrics and quantum control are model only: open control toolkits exist (Qiskit Pulse, QuTiP) but no benchmark ships a controller to sit on; a real test needs the hardware |
| Databases and caches | PostgreSQL, MySQL, MongoDB, Redis (done, section 2 row 30 and section 4 rows 24, 26, 27); Cassandra, Redis under YCSB, HammerDB (row 24); graph databases (row 44); OpenSearch (row 28) | 44, 47, 55 | done and running | distributed SQL with its own rebalancing: **row 69 added** |
| Messaging and streaming | Kafka (done, row 26); Flink's autoscaler (row 61); device brokers, EMQX and Mosquitto (row 78) | 49 | done; queued | the other brokers (RabbitMQ, NATS, Pulsar) with their shipped flow control: **row 70 added**; device brokers: **row 78 added 10 October**, their connection and in-flight muscles into family 49 at v4 |
| Storage | fio on the device (row 29); Ceph's own throttles (row 62) | 57 | queued | none |
| Web platforms and social media | the serving layer (row 43), the graph data layer (row 44), streaming (row 41), transcoding (row 57), CDN caches (row 71) | 54, 56, 51, 53, 45 | queued | observability pipelines were model only: **row 73 added** |
| Serverless and distributed compute | Knative (row 46), Ray and Dask (row 47), Spark (row 25), workflows (row 49) | 7, 46 | queued | none |
| AI | serving (row 19, ready on the card), training (row 20), batch admission on Kubernetes (row 63), the card itself (section 2) | 1, 2, 11, 14 | ready and queued | inference engines on the CPU (llama.cpp) run in row 19's pattern when asked |
| HPC and science | Slurm's power saving (row 48), Batsim (row 16), workflows (row 49), the solvers (row 37: no knob) | 7, 9 | queued | a solver's own adaptive step controller is a possible native, to be judged by the physics criterion before any row |
| Networks and telecom | ns-3 and 5G-LENA (row 21), srsRAN with the 5G core beside it, Open5GS or OpenAirInterface (row 42), the kernel's network stack (row 39), edge clusters (row 23) | 50, 58 | queued | the core was missing from row 42: **line added 10 October**; Open vSwitch and Linux traffic control belong to row 39's network knobs |
| Television and streaming | adaptive bitrate (row 41), CDN caches (row 71), transcoding (row 57) | 54; a Media Streaming & CDN family at v4 (the rows exist, the family does not yet) | queued | none |
| Finance and commerce | trading infrastructure (row 45); payment switches in row 43's pattern | 45 (payments); a Financial Markets & Trading Systems family at v4 (the muscles of row 45 exist as a row, not yet as a family) | queued | **trading decisions are excluded by rule** (section 3) |
| Healthcare and medicine | hospital systems and imaging pipelines (row 53), surgical robot servos (row 67, candidate), hospital environments (rows 9, 10; family 34) | 34, 48 | queued; candidate | **clinical dosing controllers are excluded by rule** (section 3) |
| Robotics | arms (done, section 2 row 29), legged (row 2), humanoids and marine (row 55), navigation (row 54), fleets (row 30), surgical (row 67) | 24, 25 | done; queued | none |
| Drones and aviation | gym-pybullet-drones (done), PX4, ArduPilot, Crazyswarm, JSBSim (row 23) | 20 | done; queued | air traffic management was missing: **row 72 added** |
| Space and rockets | Basilisk attitude, momentum and constellations (rows 4, 32, 34), NASA's open flight software cFS through NOS3 (row 32, line added 10 October), Orekit and GMAT (row 33), RocketPy and OpenRocket (row 35), Cantera (row 36) | 26 | queued | ascent guidance has no open shipped controller beyond the rocket rows, said here; the real flight software's open line is now on row 32 |
| Cars and mobility | driving models (row 15), **self-driving stacks (row 58 added)**, **the EV powertrain (row 59 added)**, charging (row 7), the cell (row 8), traffic signals (row 14), **mobility fleets (row 60 added)** | 19 | queued | engine control units (open ECU firmware) are a candidate only until a simulator with the shipped maps is found |
| Rail, elevators, ports | marine vehicles (row 55) | 21, 22, 23, 52 | model only for rail, elevators and ports | no open benchmark ships a train, lift or port controller we can run (Flatland is a scheduling game without one); the muscles stand as the model until one exists |
| Energy grids | pandapower (done, section 2 row 28), Grid2Op (row 5), OpenDSS feeders (row 6), microgrids and storage (row 8), CityLearn (done, row 26) | 31, 32, 33, 41 | done; queued | none |
| Power plants and generation | one wind turbine (row 51), wind farms (row 11), combustion (row 36), **thermal plants (row 65 added, candidate)** | 40, 41 | queued; candidate | **nuclear**: no open plant benchmark ships a controller (OpenMC and its kind are solvers without a knob); the thermal-plant libraries are the nearest; nuclear stands as the model only, said plainly |
| Buildings and facilities | BOPTEST (row 9, with Home Assistant's climate automations noted as a candidate shipped controller), Sinergym with its data-centre model (row 10), CityLearn (done), district heating (row 50), the UPS reserve (row 27, excluded) | 28, 29, 30, 34, 38 | done; queued | none |
| Industry and process | Tennessee Eastman (row 13, with the OpenPLC runtime noted as a candidate real PLC under the process model), pipelines (row 50), water (row 12), agriculture (row 52), mining (row 56, candidate), **fabs (row 66 added, candidate)** | 27, 35, 36, 37, 39, 42, 43 | queued; candidates | pharmaceutical and food batch processes have no open shipped controller beyond the process models (BioSTEAM is a design tool); 3D printing and CNC (Klipper) lack a standard benchmark: both candidates, not rows |
| Supply chain and logistics | OR-Gym (row 22), Open-RMF (row 30), mobility fleets (row 60) | 59, 52 | queued | none |
| Games and graphics | Godot (row 64, candidate); **game server fleets, Agones (row 74 added 10 October)** | 54; a Game Servers family at v4 | candidate; queued | game servers were in neither list until the final sweep: row 74 and a family at v4 |
| Blockchain and ledgers | **Bitcoin Core in regtest, go-ethereum later (row 75 added 10 October)** | none yet; a Ledger Nodes family at v4 | queued | the node's machinery only (cache, mempool, peers); **consensus and transaction decisions are excluded by rule** (section 3) |
| Software build farms | **actions-runner-controller runner scale sets, GitLab Runner later (row 76 added 10 October)** | none yet; a Build Farms family at v4 | queued | in neither list until the final sweep |
| Robustness and security | the governor killed, the long run, the 24-hour run (row 31, done and running); **network security engines as a governed system, Suricata and Zeek (row 77 added 10 October)** | 53 | done; queued | security of Omni itself is a review, not a benchmark; the kill switch and the lease are tested in row 31; the engines' capture threads and ring sizes are muscles of family 53 at v4 |

## 3. Excluded by rule, and why

Omni-Compass governs machinery. These are never a knob, whatever the gain would read:

1. **Safety reserves**: a reserve held for an outage (the UPS's reserve, row 27) or for a fault is never a lever; the physics
   criterion of `docs/MECHANISM_OF_ACTION.md`.
2. **Clinical dosing controllers**: insulin pumps, anaesthesia, ventilation, infusion. Omni may govern a hospital's servers,
   cooling and imaging pipelines (rows 53, 9, 10); it never touches a controller whose output goes into a patient.
3. **Trading decisions**: Omni governs a matching engine's pools and admission (row 45); it never decides a trade, a price or a
   position.
4. **Weapons**: in a defence fleet (row 23) Omni governs endurance, energy and admission; a controller whose output is a
   weapon's release is never a knob.
5. **A person's command**: where the native controller is a person (a surgeon's hand, a pilot's input, a driver's wheel) Omni
   sits only on the servo margins beneath (rows 58, 67), never on the command.
6. **Solvers without a controller**: OpenFOAM, SU2 and their kind (row 37) have no knob; their value here is the cluster that
   runs them (rows 16, 48).
7. **Consensus and transactions in a ledger node** (row 75, added 10 October): Omni governs the node's cache, peers and
   threads; it never decides what is validated, signed or relayed.

## 4. How this page is kept true

A domain enters section 2 of the register when its first run lands (a preregistration frozen on one tuning case, a workflow or a
one-command script, the three-run table, every row shown); it enters section 4 when an open benchmark with a shipped controller
is named; it is "model only" until then, and this page says so. The founder's standing order is one or two at a time, each
preregistered before it runs. When a reader finds a controller this page does not name, the answer is a new row with its
owner, not a claim.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
