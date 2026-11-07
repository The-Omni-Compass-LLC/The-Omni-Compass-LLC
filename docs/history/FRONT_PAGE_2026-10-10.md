# The front page as it stood on 10 October 2026 (before the repository wrote its own)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

The Omni-Compass LLC · [www.omni-compass.com](https://www.omni-compass.com)

## Latest (10 October 2026, newest first)

The lines between the two markers below are written by the repository itself: after every finished live run, the front-page
workflow archives the run and rebuilds every table whose three runs are in (`tools/front_page.py`, `.github/workflows/front-page.yml`).

<!-- front-page:begin -->
- 2026-10-10 16:50 UTC: `V3_YCSB` rebuilt from runs 38054777807, 38054782696, 38054787517 (ycsb, the resource objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_YCSB.md: 4 untouched workloads; 4 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_SYSBENCH` rebuilt from runs 38054765202, 38054768832, 38054773573 (sysbench, the resource objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_SYSBENCH.md: 4 untouched workloads; 0 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_REDIS_SERVICE` rebuilt from runs 38054791688, 38054795871, 38054800068 (redis, the service objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_REDIS_SERVICE.md: 3 untouched workloads; 5 better, 2 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_REDIS` rebuilt from runs 38054731163, 38054735302, 38054739168 (redis, the resource objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_REDIS.md: 3 untouched workloads; 0 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_PGBENCH` rebuilt from runs 38054754511, 38054758150, 38054761503 (pgbench, the resource objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_PGBENCH.md: 3 workloads; 1 better, 1 worse, 1 disagree
- 2026-10-10 16:50 UTC: `V3_KAFKA_SERVICE` rebuilt from runs 38054804459, 38054808912, 38054812962 (kafka, the service objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_KAFKA_SERVICE.md: 3 untouched workloads; 1 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_KAFKA` rebuilt from runs 38054742933, 38054746778, 38054750788 (kafka, the resource objective, omni-v3): /home/runner/work/The-Omni-Compass/The-Omni-Compass/results/live/V3_KAFKA.md: 3 untouched workloads; 1 better, 0 worse, 0 disagree
<!-- front-page:end -->

- **Omni v4 ordered: the collective mechanism.** One body, one brain, one tick a second; a trial runs to its full measurement and
  is never ended by the calm it causes; the body's cost is judged and nothing anywhere is made worse to make one thing better;
  every wire forced through it. Designed in [`docs/OMNI_V4_PLAN.md`](../../docs/OMNI_V4_PLAN.md), with the final coverage sweep
  (register rows 74 to 78, five new muscle families, the closed systems of the mega-caps mapped to the open analogs that carry
  the same muscles) and the order of the rerun. Every result is run again on v4 when it is built.
- **The second set of the five live products** (Redis, Kafka, PostgreSQL, MySQL, MongoDB; 21 runs on the amended trial rule)
  landed and is archived; its three-run tables follow. From the logs: on Kafka the brain allowed the third consumer once and the
  whole gain returned at 2.5 consumers instead of 6 to 8 (delay 2.4 s to 57 ms); on every other repetition it refused. The
  trial's measurement, not the law, is the fault, and the four rules that fix it are in the v4 plan
  ([`docs/RERUN_2026-10-10.md`](../../docs/RERUN_2026-10-10.md)).
- **The rerun of 10 October**: every table remade from 67 archived runs on Omni v3; the Omni index +4.8%, service reading
  +10.7%, no losing row ([`docs/STATE_OF_PLAY.md`](../../docs/STATE_OF_PLAY.md)).

**Two names only: native is the system as it runs on its own; omni is Omni-Compass on top of native.** Omni-Compass
never replaces native; every comparison below is native against omni.

## The result

Omni-Compass on top of native Kubernetes, real clusters, ten paired runs per test, on **Omni v3**, the frozen and
fingerprinted engine ([`docs/OMNI_V3.md`](../../docs/OMNI_V3.md): v1's law and controllers byte for byte, the muscle catalog grown to 945 and a do-no-harm gate on speed knobs; the v1 tables, [`docs/OMNI_V1.md`](../../docs/OMNI_V1.md), read the same and stay as the first engine's record). Every test ran three times as separate GitHub runs (A the
result, B and C the replications); a reading below is **confirmed** only when it holds in all three runs with every 95%
interval clear of zero, and otherwise reads no difference beyond the noise. The six tables:
[`V3_ALL_FOUR`](../../results/live/V3_ALL_FOUR.md), [`V3_STEADY`](../../results/live/V3_STEADY.md),
[`V3_WANDERING`](../../results/live/V3_WANDERING.md), [`V3_FAULTS`](../../results/live/V3_FAULTS.md),
[`V3_BATCH`](../../results/live/V3_BATCH.md), [`V3_FAIRNESS`](../../results/live/V3_FAIRNESS.md).

| | native (run A) | omni (run A) | Reading over the three runs |
|---|---:|---:|---|
| **Work handled inside the response line** (all four in one run) | 21.0 req/s | **31.2 req/s** | **+35% to +49% more work on the same machines, confirmed better** |
| **Response time, 95th percentile** (steady, wandering, all four, faults) | 321-820 ms | 111-306 ms | **−47% to −66% in every run of all four tests, confirmed better** |
| **Failed requests** (wandering, all four) | 8.9-12.3% | 7.7-10.9% | **−9% to −14%, confirmed better**; zero in both arms at steady load; under faults lower in all three, clear of the noise in one |
| **Machines in service** | 6 | 5.90 (steady), 4.89 (batch) | steady **−1.5% to −2.9%** and batch **−19% to −23%, confirmed better**; the other tests no difference beyond the noise |
| **Energy** (a declared model: on kind the machines are containers on one runner, so a machine out of service saves modelled watts, not a metered bill) | | | standby model confirmed lower in steady (−1.3% to −2.1%) and batch (−13% to −16%); elsewhere no difference beyond the noise |
| **A noisy neighbour on the same workers** (fairness) | | | no difference beyond the noise on every row, the neighbour's own service included: Omni neither helps nor hurts |
| **Pods left with no machine to take them** | 0 | 0 | same, in every test |

Omni gives a machine back only after a paired trial shows the service is no slower without it (the verdict). On these
clusters one machine fewer made each request 30-45% slower in most trials, so Omni kept the machines and spent them on
speed and work. Earlier engines without that check parked 29-36% of the machines (`docs/history/`); the frozen engine
puts work and speed first.

**What this does and does not show.** The product gain measured so far is more work inside the response line on the same
machines, 34-52% across the three capacity runs on earlier engines ([`CAPACITY`](../../results/live/CAPACITY.md) +34.1%,
[`CAPACITY_2`](../../results/live/CAPACITY_2.md) +51.9%, [`ALL_FOUR`](../../results/live/ALL_FOUR.md) +41.7%), with a faster tail; the
v1 runs give one engine's number three times. Not yet shown: an energy or cloud-bill saving on real machines (Azure's bill
did not move on the earlier engine, [`AKS_BILL`](../../results/live/AKS_BILL.md), nor on v1's steady run, [`V1_AKS_STEADY`](../../results/live/V1_AKS_STEADY.md): every gauge inside the noise; the v1 burst is running), and the
current card governor on a real GPU (the one real-card run, on the governor since replaced, saved 1.6-3.5% of the card's
energy and made its 95th percentile 43-84% slower:
[`HIL_RESCORED`](../../results/hil/run-20261002T082232Z/HIL_RESCORED.md)).

**Two readings of one index, both in `results/OMNI_INDEX.md`.** The resource reading (the headline below) scores work,
speed, machines and energy together, so a governor that buys speed with memory pays for the memory. The service reading,
declared on 9 October at the founder's question about what a cache is for, scores work and speed only and shows the
resources beside them: **+10.7%** over the same six categories on the sets of 10 October (Kubernetes +84.5%; the five
stacks exactly nothing, because their gains are resources given back, and on Kafka and Redis the brain's first set could not
yet judge a spend: amendment 3, the next set running). Neither hides a loss; each says a
different true thing, and the first is the one preregistered.

**Wire in, or watch.** Omni is wired out of every muscle and into a knob only where the paired measurement shows the
muscle no worse for it; where it shows nothing, or a loss, the muscle stays native and Omni only reads it.
`docs/WIRING_VERDICTS.md` gives every knob in every result one of three words from the tables themselves, **write**,
**watch** or **operator's choice**: on the real stacks' sets of 10 October 11 of 24 knob-cases write, 0 are trades and 13
watch; of the 945 modelled muscles 124 write and 808 stay native, 746 of them because the native controller never left
the band. Every confirmed loss is listed there with its cause.

**One number per benchmark, one meaning of the sign.** `docs/BENEFIT_SHEET.md` gives every benchmark one figure where
plus is always good for Omni and minus always bad, whatever the gauge measures: less energy, fewer machines, less memory and
a shorter wait all read plus. Beside it: yes, no, none or trade. It is built from the tables by `tools/benefit_sheet.py`.

**The Omni index, every real test together: +4.8%** more for the same, or the same for less, across work, speed,
machines and energy, six real categories each weighed the same, on the sets of 10 October (every benchmark run again on one
commit, `docs/RERUN_2026-10-10.md`): real Kubernetes on v3 +28.9% over seven tests (work +26%, speed +106%, machines +4%,
energy +2%); the real database on v3, PostgreSQL behind PgBouncer, +0.8% (connections held open −6% to −11% on `select`,
confirmed better, with CPU and latency inside the noise, the add above the operator's setting refused on the slow write
workload, no loss); real messaging on v3, Apache Kafka, +0.1% (consumers 2 → 1.98 to 1.99, every other gauge inside the
noise: every spend trial was abandoned before it could be judged, our wiring, amended the same day as amendment 3, the next
set running); the real cache on v3, Redis, exactly nothing (every gauge inside the noise under both objectives, the same
amendment); the real database's storage-engine cache on v3, MongoDB under YCSB, +0.7% (the cache held −3% to −13% on `f`,
confirmed better, nothing worse); the real database's buffer pool on v3, MySQL under sysbench, +1.0% (the pool held −10% to
−20% on `read_write`, confirmed better, the earlier memory cost gone, nothing worse). These are the first sets on which the
brain's own verdict judged every notch on the stack before it was written: the number came down from +20.5% because the
spends that bought the earlier gains at a resource cost were refused or not yet judged, and every gain left is one the brain
proved on the stack itself. No row is a loss. The earlier tables are whole in `docs/history`.

Six organisms with the real cluster inside (the four realms, the whole tower of 945 muscles, the four stacked, 1,716),
on an earlier engine: late 23-52% less often and 24-40% faster in every one
([`results/live/V1_SIX_KUBE.md`](../../results/live/V1_SIX_KUBE.md), v1; the earlier engine's in [`results/live/SIX_KUBE.md`](../../results/live/SIX_KUBE.md)); on v3 at 10 and 100 copies every
cell is better on 4 to 6 gauges and worse on none beyond the noise but a rounding-level work loss in 4 of 12
([`results/live/V3_SIX_KUBE.md`](../../results/live/V3_SIX_KUBE.md)); the 1,000-copy cells run on Azure: the tower
on v1 ([`results/live/V1_BIG_ORGANISM.md`](../../results/live/V1_BIG_ORGANISM.md)) answered its slowest 5% in 0.2 s against native's
4.1 s and was over its line 0.2% of the time against 64%; the four stacked on v3
([`results/live/V3_BIG_ORGANISM.md`](../../results/live/V3_BIG_ORGANISM.md), 1.7 million muscles on one clock with the cluster
inside, three repetitions on a rented machine with a 10,800 s window) answered their slowest 5% in 150 ms against native's
2.9 s, were over the line 0% of the time against 51%, failed no request against 0.14%, on the same six machines and the
same energy inside the noise, both arms on the clock. A cell whose machine could not step the organism inside its window
is marked off the clock in the report and run again with a longer window.

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 945 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

## Check it yourself

```
pip install -r requirements.txt && python verify.py      # must end: VERIFICATION: PASS
bash scripts/run_live_local.sh 3                          # native against omni on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), holds each muscle's own setting in the middle of
its band with one bounded law, and hands every setting back the moment it stops. As demand rises, the warm machines
take it first; as it falls, the emptiest machine idles first, powered and ready, never switched off, and never below a floor of two (idle). The reset hands every setting back at
the end of a run; the kill switch, a separate security switch, turns Omni-Compass off everywhere at once. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](../../docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](../../docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](../../docs/CONVEYANCE_LAW.md).

## Read next

| For | Read |
|---|---|
| **The register: every muscle wired, every benchmark run, every benchmark still to run** | [`docs/REGISTER.md`](../../docs/REGISTER.md) |
| **The proof program: every benchmark at full size, every open native engine, the referee-grade package** | [`docs/PROOF_PROGRAM.md`](../../docs/PROOF_PROGRAM.md) |
| **Omni v3, v2 and v1: the frozen engines, fingerprinted; which version every result ran on; how each is confirmed three times** | [`docs/OMNI_V3.md`](../../docs/OMNI_V3.md), [`docs/OMNI_V2.md`](../../docs/OMNI_V2.md), [`docs/OMNI_V1.md`](../../docs/OMNI_V1.md), `python3 tools/omni_version.py` |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](../../docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](../../results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](../../docs/HOW_TO_READ_THE_RESULTS.md) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](../../docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](../../docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](../../docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](../../docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](../../docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](../../docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](../../docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](../../docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](../../docs/INTEGRATION_MANUAL.md) |
| The 945 muscles | [`docs/MUSCLE_CATALOG.md`](../../docs/MUSCLE_CATALOG.md) |
| Every command on one page | [`docs/HANDOFF.md`](../../docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 945-muscle catalogue and its models (Omni v2) |
| `scripts/`, `deploy/`, `.github/workflows/` | The benchmarks: kind, AKS, the card, eight cards |
| `tools/` | Report builders, the Omni index, the layout check |
| `results/` | Every result with its raw files and digests |
| `docs/` | Results, method, manual, due diligence |
| `tests/` | The tests `verify.py` runs |

## Find it

Omni-Compass is a **supervisory governor**: a control plane that sits on top of a native controller and never replaces it.
People searching for any of these should find this page: supervisory governor, supervisory control, control plane,
governor, controller, autoscaler, autoscaling, Kubernetes HPA, cluster autoscaler, Karpenter, KEDA, node pool, right-sizing,
conveyance, machinery, engine control, power cap, clock ceiling, DVFS, cpufreq, RAPL, GPU power limit, energy efficiency,
energy per unit of work, data center efficiency, PUE, green computing, FinOps, SRE, SLO, p95, tail latency, do no harm,
paired trial, A/B/C replication, preregistration, Redis maxmemory, Kafka consumer group, PostgreSQL pooler, MySQL buffer
pool, MongoDB WiredTiger cache, HVAC setpoint, building management, chiller plant, UPS, PDU, battery management, microgrid,
grid tap changer, voltage regulator, wind turbine pitch, pipeline compressor, water pump scheduling, robot servo, drone
autopilot, flight software, autonomous driving stack, 5G RAN scheduler, matching engine, game server fleet, build farm,
ledger node, IDS workers, control theory, closed loop, two antagonist forces, tanh law, nervous system, muscles, realms,
organisms, Omni index. GitHub topics for this repository are set from the repository's About panel by its owner.

## License

**Proprietary. Evaluation and Simulation use only.** You may download, run and modify the software only to evaluate
it and to reproduce the published results, including in shadow or test mode on systems you own or control. Everything
else requires a written **Omni-Compass Enterprise License** signed by The Omni-Compass LLC and paid for. No patent or
trademark license is granted for any other use.

| File | What it says |
|---|---|
| [`LICENSE`](../../LICENSE) | evaluation and Simulation use only; everything else needs a signed, paid Omni-Compass Enterprise License |
| [`NOTICE`](../../NOTICE) | copyright, the US filings notice, third-party notices |
| [`PATENTS.md`](../../PATENTS.md) | the nonprovisional utility patent application "The Omni-Compass" filed in the United States (title, inventor, date; the number is withheld on purpose); no patent license is granted |
| [`TRADEMARKS.md`](../../TRADEMARKS.md) | the Omni-Compass marks; trademark applications filed in the United States |
| [`DISCLOSURES.md`](../../DISCLOSURES.md) | every declaration, disclosure and disclaimer, made once |
| [`LICENSING_FAQ.md`](../../LICENSING_FAQ.md) | licensing in plain answers |
| [`.github/CLA.md`](../../.github/CLA.md) | contributions are assigned to The Omni-Compass LLC |
| [`REUSE.toml`](../../REUSE.toml), [`sbom/`](../../sbom), [`.fossa.yml`](../../.fossa.yml) | machine-readable license declarations for scanners |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
