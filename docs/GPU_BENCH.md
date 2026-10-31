# The GPU bench: one command, real watts

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Before you wire anything:** read [`DISCLOSURES.md`](../DISCLOSURES.md). Omni-Compass acts only through the wires it is given; it cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the first presumption is wiring: check the installation with section 4.5 of the manual (*Wired right or wired wrong*).

This is the test that answers "does Omni-Compass save real energy?" with the GPU's own power meter. There is no model
in it. Nobody has run it yet on real hardware for this repository; the first run is the first real-meter result.

## What you need

- A Linux machine with one NVIDIA GPU (a rented cloud GPU works: A100, H100, L4, A10, RTX), the NVIDIA driver and
  `nvidia-smi`.
- Python 3 with PyTorch built for CUDA (`pip install torch numpy`).
- Root, because setting a GPU power limit (`nvidia-smi -pl`) needs it. Persistence mode on is recommended
  (`sudo nvidia-smi -pm 1`); the receipt records it either way.

## Run it

```bash
git clone <this repository> && cd <it>
sudo bash scripts/gpu_paired.sh                       # 5 repetitions, 10 minutes per arm: about 3 hours
sudo REPS=5 DURATION=300 bash scripts/gpu_paired.sh   # 5-minute arms: about 1.5 hours
```

Options (environment variables): `REPS`, `DURATION` (s per arm), `DRAIN` (s after arrivals stop), `COOLDOWN` (s idle
before each arm), `GPU` (index), `SAMPLE_MS`, `INTERVAL` (s between Omni decisions), `SLO_MS` (response-time target;
default ten bare service times), `WORKLOAD_ARGS` (e.g. `--n 8192 --target-ms 80`).

## Two phases

- `PHASE=smoke` (the default): look for faults and for an effect worth a counted run. Any number of repetitions.
- `PHASE=confirm`: the preregistered test (`docs/GPU_PREREGISTRATION.md`), 10 repetitions. Omni's code must be
  committed; its files are hashed before the first arm and again after the last, and any change invalidates the run.

```bash
sudo PHASE=confirm bash scripts/gpu_paired.sh
```

The **primary outcome** is work per energy: requests served per kilojoule the GPU drew.

## What it does

1. **Receipt.** GPU name, UUID, VBIOS, driver, kernel, host, persistence mode, power management, the enforced limit,
   default, minimum, maximum and current power limit, the workload's hash, the mechanism id, git commit
   (`receipt.json`). The current power limit is the **snapshot**; every arm must start and end at it. The bench
   refuses to start unless power management is Enabled (otherwise a written limit would not bind).
2. **Calibrate once.** The workload times its request at the snapshot limit and picks the request size so one request
   takes about 50 ms (`calib.json`). Every arm uses the same calibration.
3. **Three arms per repetition, order rotated,** each after `COOLDOWN` s idle:
   - **native**: no Omni process.
   - **watch**: Omni runs, reads the GPU and decides, and is forbidden to write. This is the control: it shows what
     the machine does with Omni present and silent. If it writes even once, the run is invalid.
   - **omni**: Omni writes the GPU power limit.
4. **The same work in every arm.** `tools/gpu_workload.py` sends one seeded stream of requests (fp16 matrix products)
   at 30%, 60%, 80%, 30%, 60% and 30% of the GPU's full-power capacity. Every arm gets the same requests at the same
   moments.
5. **Measured by the device.** `nvidia-smi` samples power draw, temperature, utilisation, the power limit, the
   **enforced** power limit and the clock-limit reasons every 200 ms for the whole arm (the fields the driver reports,
   listed in `smi_fields.txt`); RAPL CPU package counters are read at both ends where the machine has them. This is
   receipt C, the outcome: Omni never supplies it.
6. **Reset.** After the omni arm Omni restores the snapshot limit and reads it back. The script checks the limit
   after every arm.
7. **The table** (`GPU_REPS.md`): each gauge for native, watch and omni, and three paired contrasts with 95%
   intervals — observation (watch − native), authority (omni − watch), total (omni − native). If an interval includes
   zero, it reads **STEADY, no difference beyond the noise**; wholly on one side, **GAIN** (or **LOSS**, or **power given**)
   **clear of the noise** (the words of amendment 14). The result label is chosen by rule (`docs/GPU_PREREGISTRATION.md`, amendment 1):
   SUPERIOR WITHIN GUARDRAILS, ENERGY IMPROVEMENT WITH SERVICE TRADEOFF, NONINFERIOR / INCONCLUSIVE, NOT ESTABLISHED,
   AWAY FROM ITS AIM, or INVALID. Also: actuator fidelity (receipt B), control effort and representation fidelity (receipt A). A
   meter that was not fitted prints UNAVAILABLE. The run folder holds every raw file and `SHA256SUMS.txt`.

## What Omni does on the GPU (omni_controller/gpu_governor.py)

Every 2 s it reads the GPU and runs the Omni-Compass engine (the throughput law in `omnicompass/adapter.py`): load is
GPU utilisation, power stress is draw over the snapshot limit, heat is temperature over 83 C, queue is response-time
pressure. The engine's power cap becomes a power limit, inside hard rules:

![Wiring schematic: a graphics card, two wires. The schematic is read top to bottom as an electrical drawing: the governor (the control unit) with its sense terminals S1, S2, … on the left and its motor terminals M1, M2, … on its lower edge; the motor bus through the kill switch into the plug, the system's own command written and read back; the plug into the native controller; the native controller setting the muscle, drawn as a potentiometer with its cover; the system under native carrying the meters; and the meters back along one bus, the wire in, to the sense terminals. The audit stands beside the governor. The senses are the card's utilization, draw and temperature, its clocks and top clock, and the workload's feed; the two motors are the clock ceiling (-lgc) and the power limit (-pl), both through nvidia-smi and both read back. Learns the card on its own first (15 busy readings); races while work waits (≥ 95% utilization); at the max never below the top while the card serves; at the tune-down paces the slack in 15 MHz steps, each step through the paired trial.](book/figures/s_gpu.svg)

- never below the GPU's current draw x 1.3, never below 0.70 of the snapshot (`--min-share`), never below the device
  minimum, never above the snapshot;
- a busy card (utilisation smoothed over decisions at or over 0.5, `--util-gate`) gets the snapshot limit back at once,
  and the cap returns only under 0.4;
- optional speed lock (`--baseline-file`, from `tools/gpu_baseline.py` on runs without Omni): the limit follows
  response time against that baseline, every gauge kept at least 1% faster (`docs/INTEGRATION_MANUAL.md`, level 5);
- no new write until the last one reads back from the device; every write is read back at once and recorded
  (requested, return code, read back, enforced limit, delay); the engine senses the enforced limit, the one the card
  obeys; a write the device refuses ends the arm (exit 4) and makes the run invalid; no clock locks are ever written;
- if it cannot read the GPU or the response times, the snapshot limit at once;
- if response time breaks its target, the snapshot limit at once, and for three decisions after;
- kill file or SIGTERM: the snapshot limit, read back.

- **one writer:** if the limit ever reads a value Omni did not write, Omni stops writing, leaves that limit alone,
  and exits 5 (the run is invalid);
- **heat fails up:** while the card reports a thermal or hardware slowdown, no lower limit is written;
- every decision names every rule that held the engine back (`blocked_by`) and the one that decided (`decided_by`).

![Block diagram: the two wires of a card as an antagonist pair. The band (the mean response of the last 5 s, from a tenth of the line to the line) yields the force F; the mode decides between racing (both wires to full while work waits, utilization ≥ 95%), steady under the limit (the card's own busy clock as the ceiling) and pacing. The up wire is the clock ceiling, raised in 15 MHz steps toward the top and lowered only through the verdict; the down wire is the power limit, the lid at ⌈1.10 × the busy draw⌉, never over the start limit and never under the envelope floor. The card's own boost climbs to the ceiling and its own limiter knocks back at the lid; the meters close the loop every 2 s.](book/figures/c_gpu_pair.svg)

Any workload plugs in through `WORKLOAD_CMD` (for example a vLLM or MLPerf inference harness), if it writes
`latency.csv`, `requests.csv` and `summary.json` in `tools/gpu_workload.py`'s format and `SLO_MS` is given.

The table also credits each write: joules and requests against native at the same moments of the same stream, grouped
by the rule that decided it. CPU energy comes from RAPL by domain: package and DRAM apart, psys never added, wrap
undone. The card's own energy counter (NVML) and its ECC and retired-page counters are read at both ends of each arm.

![State machine: the two-wire card governor. It learns the card on its own first (15 busy readings), then races while work waits (utilization at 95% or more), holds steady at the card's own busy clock while saturated under an operator's cap, or paces the slack in 15 MHz steps through the verdict; from any state it fails up on a breach, a failed request, a blind feed or a heat slowdown, and it observes only, for the rest of the run, once a limit is found that it did not write.](book/figures/g_gpu_states.svg)

## Gauges

| Gauge | From | Its aim |
|---|---|---|
| **work per energy (served requests per kJ), primary** | requests served / GPU energy | higher |
| energy, GPU (J) | power.draw integrated over the arm's window | lower |
| energy per served request (J) | the same, over requests served | lower |
| power, GPU mean (W) | energy / window | lower |
| requests served, not served | the workload's own record | more served, fewer not |
| response time mean, 95th, 99th percentile (ms) | arrival to finish of each request | lower |
| temperature, peak and mean (C) | temperature.gpu | lower |
| energy, CPU package (J) | RAPL counters, when present | lower |

## Testing the bench without a GPU

`python tests/test_gpu_bench.py` runs the whole script against a stand-in `nvidia-smi` (`tests/standin_gpu/`), with the
workload's `--sim` mode. The stand-in has no real power physics, so its numbers mean nothing; it proves the script,
the controls and the validity checks work.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
