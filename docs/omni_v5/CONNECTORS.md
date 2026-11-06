# Omni v5 — the connector blueprint: every monitor (read) and knob (write) in the industry, by muscle (scratch, NOT pushed)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

Founder's order, 11 Oct: wire Omni into every muscle through the monitors and knobs the world already uses (open source
first), so an owner can drop it on a real system in real time with almost no setup, and never get a confusing or wrong
number. This is the paper blueprint we will push from. Scratch only — nothing pushed.

## The plug is always the same; only the adapters differ
Every muscle, whatever it is, plugs in the same way: **one wire in** (read the gauges) → **brain (math)** → **one wire
out** (write one knob), with snapshot-once / restore-to-native / one-writer / read-back / heartbeat-lease around it (the
DNA, unchanged). A **connector** is just the adapter that knows, for a given muscle, which gauge to read and which knob to
write and in what units. The catalog below is the set of adapters.

## Read side (monitors) and write side (knobs), by muscle

### Compute — server / OS / CPU
- **Read:** Prometheus `node_exporter`, cAdvisor, `/proc` + `/sys`, `lm-sensors`, `turbostat`, Intel RAPL (`intel-rapl`
  powercap), `perf`/eBPF, IPMI/Redfish BMC (fan rpm, PSU watts, board temps, voltages), ACPI.
- **Write (knobs):** `cpufreq` governor + `scaling_max_freq` (DVFS), `intel_pstate`/`amd_pstate`, `cpuidle` C-states,
  RAPL power cap, cgroups v2 (`cpu.max`, `memory.max`, `io.max`), CPU affinity / NUMA, uncore frequency, fan curves
  (`ipmitool`, `fancontrol`).

### Compute — GPU / accelerator
- **Read:** NVIDIA **DCGM** / `nvidia-smi` / NVML (power, temp, SM & memory clocks, utilization, memory, ECC, throttle
  reasons); AMD `rocm-smi`; Habana/others' own telemetry.
- **Write:** power limit (`nvidia-smi -pl`), clock caps (`-lgc`/`-lmc`), **MIG** partitioning, MPS, persistence/compute
  mode, DCGM policy.

### Compute — Kubernetes / orchestration
- **Read:** metrics-server, kube-state-metrics, cAdvisor, Prometheus (node/pod CPU & mem, pending pods, HPA state,
  throttling).
- **Write:** **HPA** (target utilization, min/max replicas), **VPA** (requests/limits), **Cluster Autoscaler**,
  **Karpenter** (nodepools, consolidation), **KEDA** (event/queue scalers), PriorityClass & preemption,
  PodDisruptionBudget, descheduler, cordon/drain, resource quotas.

### Compute — cloud fleet
- **Read:** AWS CloudWatch, Azure Monitor, GCP Cloud Monitoring; scale-set metrics; spot/preemptible prices.
- **Write:** autoscaling groups / VM Scale Sets / Managed Instance Groups (size, instance type, spot vs on-demand,
  scheduled scaling), right-sizing.

### Compute — web / API / AI serving
- **Read:** Nginx `stub_status`, Envoy/Istio stats, HAProxy; vLLM / NVIDIA Triton / TGI / TensorFlow-Serving metrics
  (RPS, p50/p99 latency, queue depth, batch size, KV-cache use).
- **Write:** worker/replica count, connection & concurrency limits, batch size (vLLM `max_num_seqs`), KV-cache budget,
  tensor/pipeline-parallel, keep-alive.

### Compute — database
- **Read:** Postgres `pg_stat_*` + `postgres_exporter`, MySQL `performance_schema` + `mysqld_exporter`, MongoDB
  `serverStatus`, Redis `INFO` (connections, wait, buffer-pool/cache hit, lag).
- **Write:** connection-pool size (**PgBouncer**, **ProxySQL**), `shared_buffers`/`work_mem`,
  `innodb_buffer_pool_size`, WiredTiger cache, Redis `maxmemory` + eviction.

### Compute — messaging / streaming / queues
- **Read:** Kafka JMX + **Burrow** (consumer lag), RabbitMQ management, Pulsar stats (queue depth, throughput, lag).
- **Write:** consumer count / partitions, prefetch, batch size, KEDA queue scaler.

### Compute — big data / storage
- **Read:** Spark metrics + YARN (executors, shuffle); `fio`, `iostat`, SMART (IOPS, latency, queue, disk health).
- **Write:** Spark dynamic allocation (executors), parallelism, memory; I/O scheduler, queue depth, cache/tier mode.

### Thermal zone — cooling / facility / building
- **Read:** BMS / SCADA over **OPC UA**, **Modbus**, **BACnet** (supply & return temp, flow, pressure, CRAH/CRAC,
  chiller, PUE, outside air).
- **Write:** temperature setpoints, fan & pump VFD speeds, valve position, economizer / free-cooling.

### Energy storage — battery / inverter / grid
- **Read:** battery management system, inverter telemetry (**SunSpec**/Modbus), SCADA, meters (state of charge, state of
  health, power, voltage, grid price, carbon).
- **Write:** charge/discharge setpoint, reserve floor, power limit, demand-response.

### Motion axis — robotics / drives / vehicles
- **Read:** **ROS 2** topics, **CANopen**, **EtherCAT**, servo-drive & PLC telemetry via OPC UA (position, velocity,
  torque, current, motor temp).
- **Write:** velocity & acceleration limits, torque/current limit, trajectory timing, power/eco mode.

### Process loop — industrial control
- **Read:** PLC / DCS via OPC UA / Modbus (process value, setpoint, output, disturbances).
- **Write:** setpoint, output limits, cascade/ratio.

## One plug, works out of the box (almost no setup, the founder's rule)
1. **Auto-discover.** On attach, Omni probes what is actually present — Prometheus targets, the Kubernetes API, DCGM,
   OPC UA browse, SMART, cloud APIs — and maps each muscle it finds to the adapter it already knows. It never invents a
   muscle it cannot read and write and read back.
2. **Snapshot first.** It records every knob's current value before touching anything (the restore point).
3. **Watch before it acts.** It starts read-only (watching), learns each muscle's normal physics and edges from the
   device's *own reported limits*, and only then goes to gas. The operator confirms once; nothing moves until then.
4. **Safe defaults.** Balanced dial; edges from the hardware's own limits; the health rule on. The owner changes the dial
   on one screen, not a hundred settings.

## Never a wrong or confusing number (the founder's frustration, answered)
- **Read back every write.** Omni writes a knob, reads it back, and only trusts it if the device took it. If it can't
  verify, that muscle goes native.
- **Units are checked.** Every gauge carries its unit; a reading that breaks physics (impossible value, wrong unit) is
  rejected, not acted on (the immune reflex).
- **One number, one meaning.** The panel shows **native vs Omni side by side** for every muscle and for the whole body,
  so there is never ambiguity about what a number is against.
- **Evidence classes stay on every number:** P (real meter), L (live software), S (our model). A model number is never
  shown as proof.
- **Three-run reading:** a result is reported only as "the same in all three of our runs", "no difference beyond the
  noise", or "the runs disagree — unstable here". Never a bare percentage that reads as approved.
- **Restore is proven.** On kill or lease-expiry, Omni reads back that every knob equals the snapshot; the panel shows it.

### Muscle families added on the coverage check (were missing or only implied)
- **Network fabric / SDN / load balancers / CDN.** Read: SNMP, sFlow/NetFlow/IPFIX, switch & NIC telemetry, Envoy/HAProxy,
  CDN edge stats (port utilization, drops, latency, queue). Write: port speed & Energy-Efficient-Ethernet, QoS / traffic
  shaping, ECMP weights, CDN cache TTL & tiering, NIC interrupt coalescing.
- **Telecom / RAN / 5G.** Read: O-RAN / base-station counters (traffic, PRB use, carrier load). Write: cell/carrier sleep
  modes, carrier on/off, MIMO layers, transmit-power trim — one of the largest energy levers in the world (idle cells).
- **HPC / batch schedulers.** Read: Slurm / PBS / LSF queues, job mix, node power. Write: power-aware scheduling, node
  power caps, queue priority, pack/consolidate, DVFS per job.
- **Serverless / FaaS.** Read: Lambda / Cloud Functions / Knative concurrency, cold-start rate. Write: provisioned
  concurrency, memory size (which sets CPU), warm-pool.
- **Virtualization / VMs.** Read: hypervisor (KVM/VMware) metrics. Write: vCPU allocation, memory ballooning, live
  migration / consolidation, host power states.

### Gut — digestion, metabolism and waste (intake → break down → route nutrients → eliminate waste)
- **Read (gauges):** intake rate & shape (ingress / gateway / message-intake), queue & **dead-letter** depth, scheduler
  backlog, disk / log / temp use, memory-leak slope (RSS climbing with flat work), retry & duplicate rate, zombie/orphan
  count, cache hit/evict, hot-partition skew.
- **Write (knobs):** intake pacing / admission (the mouth), scheduler placement & resource routing (liver/kidneys —
  which work and which power/memory/I-O to which muscle), dead-letter & drop poison, garbage-collect, reap zombies, evict
  cache, rotate & ship logs, clear temp, retry caps / circuit-breaker, TTL-expire stale items.
- **Rule:** you cannot always know waste before it's processed — Omni runs it, watches the result, eliminates what proves
  useless or toxic **before it backs up and poisons the body**, and remembers it (immune memory) to catch it earlier next
  time. Indigestion (bad batch, slow query, thundering herd) and diarrhea (over-shedding, cascading timeouts) are
  self-healed (pace intake, isolate, rebalance) and then reported on the one screen.

### Deliberately NOT a muscle (safety-of-life / regulated) — written so no one mis-wires it
Omni never takes a knob where a wrong move risks a life or breaks a safety certification. On these it is **watch-only
(advisory)** or off, and it never touches a safety interlock: flight-critical avionics & engine FADEC, nuclear protection
systems, medical life-support & implantable devices, railway signalling interlocks, automotive brake/steer safety, grid
protective relays, battery fire protection, building fire & life-safety. The manual states this in bold: these report into
the one screen so humans see them, but Omni does not drive them.

## One screen, not a thousand — cut the babysitting tax (≈ half the benefit)
A thousand muscles today can mean a thousand dashboards and an engineer babysitting each. Omni collapses that to **one
pane**: every muscle is one tile, colored by state, and the knobs all live in that one place. A couple of engineers watch
the wall; they act only when a tile changes color.
- **Colors (per muscle and rolled up per organism):** green = healthy, inside its band; yellow = inflammation, Omni is
  handling it; orange = a limb hurt / wearing, a person should look; red = brain sick/hijacked, spreading, or a muscle
  Omni has cut to native and cannot help — human attention.
- **Drill-down only on alert.** The wall stays green; an engineer opens the one tile that lit up and sees that muscle's
  live gauges (band position, edge, wobble, work, energy, wear, native-vs-Omni) and its decision log.
- **Omni already acted.** On trouble Omni quarantines the muscle (off, or native) on its own; the tile is for the human to
  *see*, not to race. Omni keeps re-checking and brings the muscle back the moment it can safely help; if native stays
  ahead, Omni leaves it native — Omni never needs to be in the loop when native serves the body as well or more.
- **Human override on the same screen.** Each tile has a switch the engineers can throw themselves — force the muscle off,
  or force it native — without touching the machine. The physical master switch sits above all of it.
- **The babysitting tax is a counted benefit.** The bill reports engineer-hours saved (one pane + auto-handling vs one
  babysitter per muscle) beside energy, work and wear — a real line of value, not a footnote.

## Chain of command (unchanged DNA)
Human **master** (holds the physical switch, sets the dial) → **Omni** (the foreman: runs the muscles on the master's
behalf, by the master's rules, never overriding the master) → **muscles** (do the work). The master's tuning and switch
are always the last word; whatever Omni does, and at whatever cost, is because the master set it that way.

## Build note
- Code it as omnicompass/connectors/* — one small adapter per muscle (read fn, write fn, readback fn, unit, edge-source),
  all behind the one Plug interface already in omnicompass/wire.py. Discovery in omnicompass/discover.py. Panel +
  outside watcher as separate always-on processes. Nothing here changes the DNA.
- Not pushed. When the founder says go: build adapters, wire discovery, run the modelled organisms through them, then the
  free clouds, then GPU on Lambda (one exact commit).

© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only. Any commercialization or
monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the
USA. www.omni-compass.com

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
