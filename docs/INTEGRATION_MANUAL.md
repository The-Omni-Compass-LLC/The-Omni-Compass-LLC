# Omni-Compass integration manual

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Before you wire anything:** read [`DISCLOSURES.md`](../DISCLOSURES.md). Omni-Compass acts only through the wires it is given; it cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the first presumption is wiring: check the installation with section 4.5 of the manual (*Wired right or wired wrong*).

> **Which knobs to wire in at all:** `docs/WIRING_VERDICTS.md` gives every knob in every published result one of three
> words from the tables themselves: **write** (wire both ways), **watch** (wire out only: Omni reads, the native controller
> lives by itself) or **operator's choice** (a trade). A knob that showed nothing, or lost, stays native. How to wire for
> superiority, step by step (watch first, the observation run, the brain's own verdict on each knob, the recheck): the manual,
> section 9.4.

How to wire Omni-Compass into your own systems yourself, from watching only to running your stack from the top. This
manual ships in the box with the code and the license. Nobody from The Omni-Compass LLC needs to be on site.

Read section 1 once, then take the levels in section 4 in order. Each level has a pass condition; go to the next
level only when it holds. The OFF switch (section 2) works at every level.

---

## 1. What is in the box

| Item | Where |
|---|---|
| The engine, nervous system, safety shield, compass and conveyance law | `omnicompass/` |
| The Kubernetes controller and its muscles | `omni_controller/controller.py`, `omni_controller/muscles.py` |
| The GPU governor (one GPU box, no Kubernetes needed) | `omni_controller/gpu_governor.py` |
| Container image recipe; install and permission files | `deploy/Dockerfile`, `deploy/install/omni-compass.yaml`, `deploy/rbac-*.yaml`, `deploy/pilot/` |
| Proof tools: paired tests on your own stack, the GPU test, simulations | `scripts/`, `tools/`, `hardware/` |
| Every check the code must pass | `python3 verify.py` (ends with `VERIFICATION: PASS`) |
| The C++ engine: every law twinned in C++20, proven equal to the Python | `cpp/` (build: `cmake -S cpp -B cpp/build && cmake --build cpp/build`) |
| The seal: the fingerprints that lock each Python law to its C++ twin | `results/SEAL.json`, `python3 tools/seal.py --check` |
| Metrics: every gauge and where it comes from | `docs/METRICS_CATALOG.md` |
| How it compares with what you run today | `docs/COMPARISON.md` |
| The license and notices | `LICENSE`, `NOTICE` |

**License, in short** (the `LICENSE` file governs): you may download, run, modify and test Omni-Compass free of charge
only to evaluate it and to reproduce its published results, including in shadow or test mode on systems you own or
control (`LICENSE`, section 1). Every other use, commercial or not (running it for your business or in production,
selling it, hosting it, or building it into a product or service), needs a signed, paid Omni-Compass Enterprise
License from The Omni-Compass LLC. The copyright, patent and trademark notices, the `LICENSE`, the `NOTICE` and
`DISCLOSURES.md` stay with every copy.

---

## 2. The rules Omni-Compass keeps on your system

1. **One OFF switch for the whole harness, in a human hand.** `python3 tools/omni_switch.py off` turns every
   Omni-Compass governor on the machine off at once: each returns every setting it changed to the value it recorded
   before it acted, reads each back and exits, and no governor starts again until `python3 tools/omni_switch.py on`
   (`omnicompass/master.py`; the switch file is `OMNI_MASTER_OFF`, by default `/tmp/omni-compass/OFF`; set it, and
   `OMNI_REGISTRY`, to a directory only the governors' user can write, `docs/THREAT_MODEL.md`). Each governor
   also has its own switch for one muscle at a time: creating its kill file (or setting `OMNI_KILL=1`).
   - Kubernetes controller: `--kill-file` (default `/tmp/omni.kill`).
   - GPU governor: `--kill-file` (default `/tmp/omni-gpu-kill`), or send it SIGTERM.
2. **It records before it acts.** Every original setting is written down first (annotations on the Kubernetes
   objects, the `snapshot` line in the GPU audit), so the OFF switch always knows what to restore.
3. **It watches before it writes.** Every level starts in watch mode: it decides and logs, and writes nothing.
4. **It never goes blind and keeps acting.** If a reading fails (nvidia-smi, metrics, the response-time feed), it
   returns what it changed to the recorded setting at once and gives nothing back until it can see again.
5. **Service first.** While response time is over your target, and for a few decisions after (`--slo-clear`), it may
   not cap power or pack tighter than your own settings.
6. **Every change is read back.** No new order goes on top of one that has not landed.
7. **The living band.** No organ is driven below 5% or above 95% of its range; machines are marked idle, never
   switched off by Omni-Compass; it never evicts or moves a pod.
8. **Everything is logged.** Every read, decision, write and its reason goes to the audit log (`--audit`).

---

## 3. Before you start: what your system needs

| You run | You need |
|---|---|
| Kubernetes (any: vanilla, EKS, GKE, AKS, OpenShift/OKD, Rancher, kind) | Kubernetes 1.34 or newer (in-place pod resize); metrics-server (`kubectl top nodes` works); an HPA with a CPU target on each service to be governed; a readiness probe and a short preStop pause on each service |
| A response-time feed (strongly recommended at every level) | a CSV per service, `elapsed_seconds,latency_ms,ok`, written continuously; `scripts/latency_probe.py` writes one against any HTTP endpoint |
| NVIDIA GPUs | driver with `nvidia-smi`; root (or the capability to run `nvidia-smi -pl`); on a VM, full GPU passthrough (container or "pod" GPU rentals usually block power-limit changes) |
| CPU power control | Linux cpufreq with the schedutil governor (`/sys/devices/system/cpu/cpufreq`); RAPL for package watts (`/sys/class/powercap/intel-rapl`); usually bare metal only, since cloud VMs rarely expose these |
| Site power and cooling | a command that prints site watts, and (for cooling) a command that sets the supply-air setpoint through your building management system |

Build the image once:
```
docker build -f deploy/Dockerfile -t <your-registry>/omni-compass:<tag> .
docker push <your-registry>/omni-compass:<tag>
```
It runs as non-root, with a read-only root filesystem and no Linux capabilities.

---

## 4. The levels, from watching to running the stack

### Level 0. Evaluate without touching anything
```
pip install -r requirements.txt
python3 verify.py                       # every check; ends with VERIFICATION: PASS
python3 tools/gpu_physics_sim.py        # the GPU governor against a modelled NVIDIA card
python3 hardware/node_exchange.py       # CPU and GPU on one power budget, modelled
```
**Pass condition:** `VERIFICATION: PASS`. Nothing in your systems is touched.

### Level 1. Watch (read-only)
```
kubectl apply -f deploy/install/omni-compass.yaml     # set the image line; it runs --mode observe
kubectl -n omni-compass logs deploy/omni-compass -f
```
- The install file grants a read-only identity. `scripts/pilot_shadow.sh` records `kubectl auth can-i` receipts that
  show it cannot write.
- Every decision it would take is logged with its reason; nothing is written.

**Pass condition:** zero writes, and readings your operators agree with.

### Level 2. The pods, on top of your autoscalers
1. Grant `patch horizontalpodautoscalers` and `patch pods/resize` (`deploy/rbac-target.yaml`).
2. Run with `--mode target --latency-file <feed> --slo-ms <your p95 target>`.
3. Optional pod muscles, one at a time:

| Muscle | Switch | What it does |
|---|---|---|
| convey | on with `--latency-file` and `--cap-deployments ns/name` | gives each machine's idle CPU to the serving pods on it (default: always); `--convey-on 0.5 --convey-off 0.25` engages it only while response time is over half the target |
| rightsize | `--rightsize-deployments ns/name` | each pod's CPU request follows its measured use × (1 + headroom), in place |
| coldstart | `--coldstart-deployments ns/name --coldstart-signal ns/configmap` | scales a service to zero while no work waits, wakes it the moment work arrives |
| batch | `--batch` | admits held Jobs labelled `omnicompass.io/batch=true` when there is load and power headroom |
| batch pace | `--batch-pace` | pauses Jobs labelled `omnicompass.io/pausable=true` under power or heat stress, resumes them after |
| rollout guard | `--rollout-guard ns/name` | pauses a rollout while change is not permitted, undoes one past its deadline when rollback is authorised |
| contain | `--contain-namespaces ns --contain-cpu-m <m>` | holds an agent namespace to a CPU budget with a quota |
| security hold | `--security-configmap ns/name` | key `hold: "true"` blocks every expansion |

Your HPAs keep scaling as before. Omni-Compass sets their targets and raises floors ahead of bursts.

**Pass condition:** p95, p99 and failed requests never behind than your own, over paired runs (section 6).

### Level 3. The machines
1. Grant `patch nodes` and `patch pods` (`deploy/kind/rbac-omni.yaml`).
2. Run with `--mode nodepool --active-nodes-only --closure /app/law/closure.json --node-scale-cmd "<command with {n}>"`.

| Your platform | The park/wake command |
|---|---|
| any cluster, bare metal, kind | `bash scripts/kind_nodepool.sh {n}`: close machines to new work and mark them first to go; open again, warm machines first |
| Karpenter / EKS Auto Mode | the NodePool CPU limit at `{n} × node CPU`, parked nodes kept, not consolidated away |
| Cluster Autoscaler node group | the group's desired size, scale-down through parking, not deletion |
| OpenShift / OKD | the worker MachineSet replicas, parked, not deleted |

A machine is given back only when every sense is live, the last order landed, pods are not scaling up, nothing waits
for a place, and the remaining machines stay inside the band.

**Pass condition:** fewer machines in service and less energy, with no LOSS on any service gauge.

### Level 4. Omni-Compass decides; Kubernetes is the muscle
Add `--strict-replicas`: Omni-Compass decides each service's replica floor and when to shrink; your HPA stays as the
fast reflex upward; the node law sizes the machines.

**Pass condition:** as level 3.

### Level 5. A GPU box (with or without Kubernetes)
The GPU governor runs on any Linux machine with NVIDIA GPUs:
```
# watch: decides and logs, writes nothing
sudo python3 -m omni_controller.gpu_governor --mode watch --gpus 0,1,2,3 --audit /var/log/omni/gpu.jsonl \
     --latency-file <feed> --slo-ms <p95 target>
# cap: writes the power limits
sudo python3 -m omni_controller.gpu_governor --mode cap   --gpus 0,1,2,3 --audit /var/log/omni/gpu.jsonl \
     --latency-file <feed> --slo-ms <p95 target>
# OFF
sudo touch /tmp/omni-gpu-kill
```
What it does, every `--interval` seconds (default 2):
- reads each GPU's own meter: power draw, temperature, utilization, power limit;
- the engine sets a power cap; the shield keeps it above `--min-share` × the start limit (0.70) and above
  draw × (1 + `--headroom`);
- a busy card (smoothed utilization at or over `--util-gate`, 0.5) gets its full limit back at once;
- a response-time breach or a failed reading returns the start limit at once.

**Speed lock (optional).** Keep every response-time gauge at least `--speed-gain` (1%) faster than without
Omni-Compass, and spend any speed won elsewhere on watts:
```
python3 tools/gpu_baseline.py baseline.json native-run/latency.csv     # a run without Omni-Compass, other days
sudo python3 -m omni_controller.gpu_governor --mode cap --baseline-file baseline.json --latency-file <feed> ...
```
**Prove it on your card:** `sudo bash scripts/gpu_paired.sh` runs native, watch and Omni-Compass back to back on the
same machine and prints the table and verdict (`docs/GPU_RUN_GUIDE.md`).

**Pass condition:** work per energy up, and requests served and p95 inside the guardrails.

### Level 6. CPU clock and power
Add to the Kubernetes controller, on bare metal:
```
--cpufreq-policy-root /sys/devices/system/cpu/cpufreq --cpufreq-require-schedutil \
--rapl-cmd "<prints CPU package watts>"
```
The CPU frequency ceiling follows the engine's cap inside the nervous system's envelope; the OFF switch writes every
policy's recorded maximum back exactly. GPUs can be wired the same way from the controller:
`--gpu-query-cmd "nvidia-smi --query-gpu=power.draw,temperature.gpu --format=csv,noheader,nounits" --gpu-power-cmd "nvidia-smi -pl {w}" --gpu-max-w <max>`.

**Pass condition:** energy per unit of work down, no LOSS on any service gauge.

### Level 7. Site power, cooling, batteries
| Organ | Switch | Status |
|---|---|---|
| site power stress | `--power-cmd "<prints site watts>" --site-limit-w <limit>` | wired: power stress enters the engine; batch pace and caps respond |
| cooling setpoint | `--cooling-cmd "<sets {c}>" --cooling-min-c 18 --cooling-max-c 27 --cooling-restore-c 22` | wired: warmer supply air while cool, colder as heat rises |
| **CPU + GPU on one power budget** | `hardware/node_exchange.py` (the conveyance law over CPU and GPU organs) | **simulation only.** The live levers exist (levels 5 and 6); the exchange between them has not run on hardware |
| GPU groups sharing a site budget | `hardware/site_exchange.py` | **simulation only** |
| on-site batteries as an organ | designed (`docs/DOMAIN_MAP.md`) | **not built** |

---

## 5. Stack by stack

| Stack | Levels available | Notes |
|---|---|---|
| Vanilla Kubernetes, kind, Rancher | 1-6 | as written |
| Amazon EKS | 1-5 | nodes via Cluster Autoscaler node group or Karpenter NodePool (level 3 table); CPU power control is not exposed on EC2 VMs; GPUs on bare-metal or full-GPU instances |
| Google GKE, Azure AKS | 1-5 | as EKS, with the provider's node-pool size as the park/wake command |
| Red Hat OpenShift / OKD | 1-5 | OpenShift is Kubernetes underneath; grant the same permissions through a Role; machines via the worker MachineSet |
| NVIDIA GPU servers without Kubernetes | 5 | the GPU governor alone |
| Bare-metal CPU servers | 6 | cpufreq and RAPL through sysfs |
| Slurm / HPC schedulers | 5 on the GPU nodes | a Slurm connector for job-level decisions is not built |
| Building management (cooling, power meters) | 7 | through your BMS's command line or API, wrapped in the command templates |
| Azure AKS, the bill as the gauge | 1-3 | Azure's managed cluster autoscaler stays native and deletes the machines Omni-Compass idles; one or several work pools (`worker_pools`), the replica ceiling raised with the fleet (`hpa_max`); a fleet of 4 cannot show a saving of one machine, 39 can (manual, section 7.1; `docs/AZURE_SETUP.md`) |
| PostgreSQL behind PgBouncer, or any pooler with a console | one knob | the pool size through the pooler's own admin console, cover [2, 90], one writer, restored on OFF (manual, section 7.2; `docs/POSTGRES_PREREGISTRATION.md`) |
| Apache Kafka, or any consumer group an operator sizes | one knob | the consumer count inside [1, partitions], the group's own end-to-end latency as the reading, the rebalance paid on every move, handed back on OFF (manual, section 7.4; `docs/KAFKA_PREREGISTRATION.md`) |
| Redis, or any cache with a console and a memory ceiling | one knob | `maxmemory` through the cache's own console, cover [16, 512] MB, grown only while the cache is full (a cold miss is not the ceiling's), one writer, restored on OFF (manual, section 7.5; `docs/REDIS_PREREGISTRATION.md`) |
| Drone swarms (gym-pybullet-drones; PX4 and ArduPilot next) | one knob a drone | the cruise override inside the autopilot's limits, a separation wall, the paired physics trial, collisions void the cell (manual, section 7.6; `docs/SWARM_PREREGISTRATION.md`) |
| MongoDB, or any store whose engine exposes its cache size at run time | one knob | the storage-engine cache through the server's own console, cover [256, 2,048] MB, grown only while the cache is full, one writer, restored on OFF (manual, section 7.7; `docs/YCSB_PREREGISTRATION.md`) |
| MySQL, or any store whose engine resizes its buffer pool online | one knob | the InnoDB buffer pool through the server's own console (`SET GLOBAL innodb_buffer_pool_size`), cover [128, 2,048] MB in the server's own 128 MB chunks, grown only while the pool is full, the plug waiting for the server's asynchronous resize before reading back, one writer, restored on OFF (manual, section 7.8; `docs/MYSQL_PREREGISTRATION.md`) |
| A rented cloud machine running the big organisms | the whole harness | `big-organism-detached`: start, collect, survey; the clock rule sets the window (`.github/workflows/big-organism-detached.yml`) |
| Independent simulators (CityLearn, pandapower, MuJoCo) | one knob each | the simulator's own controller is native; preregistered, A/B/C (manual, section 7.3) |
| The machine itself: Linux's frequency governor under the processor's meter | one knob | the frequency ceiling of every CPU through the kernel's own files, cover [half the top clock, the top], the governor still running under it; every notch down tried on the machine first by the brain's verdict; energy from RAPL and a wall plug where fitted; root on a machine on the metal, never a virtual one (manual, section 7.9; `docs/CPU_POWER_PREREGISTRATION.md`; `sudo bash scripts/cpu_power_run.sh`) |

---

## 6. Proving it on your own system

1. **Paired runs.** Run your service the same way twice, once as you run it today and once with Omni-Compass on top,
   back to back on the same machines, order rotated, at least 5 times (10 for a result you publish).
   `scripts/kind_paired.sh` and `tools/live_reps.py` do this and print each gauge with its 95% interval. A change is
   proven only when its interval excludes zero.
2. **The switch drill,** after every run: turn Omni-Compass OFF, check every setting is back at its recorded
   original and no `omnicompass.io/*` annotation remains, turn it ON.
3. **Read the results** with `docs/METRICS_CATALOG.md`: every gauge says whether it is measured or modelled.

---

## 7. Reading the log

| Line | Meaning |
|---|---|
| `gate: a sense is blind` | a reading failed; nothing is given back until it returns |
| `gate: pods scaling up` | pods first, machines after |
| `decision failed (n in a row)` | the cluster could not be reached; nothing was written. Turn it OFF for native at once |
| `convey: <machine> idle CPU to its k serving pod(s), limit c` | that machine's idle CPU now reaches the work on it |
| `convey: response time calm, operator's limit` | the pods are back at your own CPU limit |
| `busy gate: utilization u, the limit read at start` | a busy GPU got its full power limit back |
| `speed lock: worst ratio r vs line 0.99 (spend / hold / release)` | the speed lock's reading and what it did |
| `response-time reflex: the limit read at start` | response time went over target; full power at once |
| `reset: the limit read at start` | the OFF switch restored this setting |

---

## 8. What is proven, and how

| Claim | Evidence | Kind |
|---|---|---|
| On real Kubernetes, Omni v1, three runs of ten pairs each: more work inside the response line (+42% to +48%), p95 −57% to −69%, machines fewer where a paired trial allowed it (steady −1.5% to −3.4%, batch −15% to −24%) | `results/live/V1_ALL_FOUR.md`, `V1_STEADY.md`, `V1_WANDERING.md`, `V1_FAULTS.md`, `V1_BATCH.md`, `V1_FAIRNESS.md` | measured on kind; read by the three-run rule (`docs/OMNI_V1.md`) |
| On a real database, Omni v3: 61% to 72% fewer connections held open for the same work and latency, at +14% to +28% host CPU-seconds (power given in all three of our runs, reported) | `results/live/V3_PGBENCH.md` | measured on GitHub's machines |
| On Azure's bill, 4 workers: no difference beyond the noise on any gauge (the fleet is too small for the lever) | `results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md` | a real bill |
| Energy on Kubernetes | declared model on kind, no meter | modelled |
| GPU: more work per energy within the speed guardrail | earlier card controller, obsolete; rerun on rented cards pending | hardware meter |
| CPU and GPU on one power budget: more work, never over the budget | `results/hardware/NODE_EXCHANGE_*.json` | modelled |
| Safety: OFF switch restores everything; watch mode writes nothing | every live run's switch drill; `verify.py` | measured / checked |

## 9. Python, C++ and the seal

Omni-Compass exists in two languages. The laws are twinned: each has a Python version and a C++20 version that give
the same answers, proven by a parity test on every build.

| Law | Python | C++ | Proven by |
|---|---|---|---|
| core engine (six-state equations) | `omnicompass/core.py` | `cpp/src/core.cpp` | 500 frozen fixtures |
| governor (allocation laws) | `omnicompass/adapter.py` | `cpp/src/governor.cpp` | `tests/test_cpp_governor_parity.py` |
| safety shield | `omnicompass/shield.py` | `cpp/src/shield.cpp` | `tests/test_cpp_shield_parity.py` (plus adversarial cases) |
| HPA replica law | `fleet/harness.py` | `cpp/src/hpa.cpp` | `tests/test_cpp_hpa_parity.py` |
| closure law (machines) | `omnicompass/closure.py` | `cpp/src/closure.cpp` | `tests/test_cpp_closure_parity.py` |
| conveyance law (the conserved budget) | `omnicompass/conveyance.py` | `cpp/src/conveyance.cpp` | `tests/test_cpp_conveyance_parity.py` (identical to the last bit) |
| nervous system (authority per organ, living band) | `omnicompass/nervous_system.py` | `cpp/src/nervous_system.cpp` | `tests/test_cpp_twins_parity.py` |
| compass and ledger (composite storage) | `omnicompass/compass.py`, `omnicompass/storage.py` | `cpp/src/compass.cpp` | `tests/test_cpp_twins_parity.py` |
| GPU governor rules (shield limit, busy gate, speed lock, window, baseline) | `omni_controller/gpu_governor.py` | `cpp/src/gpu_rules.cpp` | `tests/test_cpp_twins_parity.py` |

**The seal** (`results/SEAL.json`) holds the SHA-256 fingerprint of every file of every twin, written only after all
parity tests pass (`python3 tools/seal.py`). `verify.py` fails if any sealed file changes afterwards, and names it. So
the Python and the C++ cannot drift apart unnoticed. What stays in Python is the plumbing that talks to Kubernetes,
nvidia-smi and sensors (`omni_controller/controller.py`, `muscles.py`, the device I/O of `gpu_governor.py`) and the
simulation harnesses; every decision they take goes through the twinned laws. The seal lists them as Python only.

Keep this manual with the code. When Omni-Compass changes, this manual, the C++ twin and the seal change in the same
commit.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
