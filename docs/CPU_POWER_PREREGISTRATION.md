# CPU power: Omni-Compass on top of the Linux kernel's own frequency governor, preregistered before any run

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-10, before any run, at the founder's order that the Linux kernel's own knobs be benchmarked (the register,
row 18). The rules below are frozen on the tuning workload before any untouched workload runs; a change is an amendment,
dated, declared here before the runs it governs. Nothing in the engine changes (`tools/omni_version.py` on the commit).

## 1. The question

Does Omni-Compass, sitting on top of the Linux kernel's own CPU frequency governor and moving only the frequency ceiling that
governor works under, deliver the same work inside the response line for less energy, measured by the processor's own
meter, on a real machine? Native is the machine as it runs today. Where a notch does not pay by the declared objective, the
brain refuses it on the machine itself and the ceiling stays where the operator left it: no gain, no loss, said so.

## 2. The two arms

- **native**: the kernel's frequency governor as shipped (`schedutil`, or the processor driver's own: `intel_pstate`,
  `amd-pstate`) chooses the clock every few milliseconds under the operator's ceiling, which is the top clock. Nothing is
  written. The governor is the native controller; it keeps running in both arms.
- **omni**: the same governor, the same machine, with one knob written on top: the frequency ceiling, `scaling_max_freq` of
  every CPU, through the kernel's own interface (`/sys/devices/system/cpu/cpu*/cpufreq/`), inside the cover **[half the top
  clock, the top clock]** and never under the processor's own minimum, **5% of the top clock a notch** (140 MHz on a 2,800
  MHz part). On a machine with two kinds of core the kernel clamps the smaller cores to their own top by itself, and Omni
  expects to read back what the kernel left. The snapshot (every CPU's governor, ceiling and floor as found) is taken once,
  before the first write; the ceiling is handed back to it at the end of every arm and read back. A ceiling found at a value
  Omni did not write stops Omni writing (one writer; recorded). The master switch and the lease (`omnicompass/master.py`)
  hold: if Omni dies, the watchdog (`tools/omni_switch.py`) runs the recorded hand-back from the snapshot file.

The harness is `tools/run_cpu_power.py` (the probe, the run, the hand-back, the report), the one-command script
`scripts/cpu_power_run.sh`, the workflow `.github/workflows/cpu-power.yml`, the three-run table `tools/cpu_power_abc.py`,
the tests `tests/test_run_cpu_power.py` on a modelled machine that is never a result.

## 3. The law, and the brain's verdict on every notch

**The reading** is the service's own: the mean latency of the last second's answered requests, on a band from 0 to the 20 ms
line, held at **40% of the line** (8 ms). The compass law (`omnicompass/compass_law.py`, dt 1 s, tau 2 s, smooth 0.5) turns
the reading into a force. Force above +0.05 (the service slow): the ceiling up by ceil(force / 0.1) notches toward the top.
Force under −0.05 (calm): one notch down, after a 5 s dwell since the last rise and never under the floor. In between: hold.
At 95% of the line (the wall): the top at once (fail up). Toward the top is always free.

**The verdict** (`tools/knob_verdict.py` around the frozen engine's own `omnicompass/verdict.py`, unchanged): the knob starts
in watch. A notch down is tried on the machine itself before it is allowed: the ceiling held at the deepest notch already
allowed (the top at first) until eight one-second cost samples are in after a 2 s settle, then one notch further for as many
again, under the same traffic; the notch is allowed only if the trial's median cost is no higher than the reference's within
2% and no higher than the cost first measured at the operator's ceiling; a refused notch is not tried again for 60 s; a trial
is started at most every 20 s and is abandoned if the service leaves calm. There is no spend direction: the ceiling cannot
go above the top. During a trial the ceiling stands at the phase's value whatever the compass asks; between trials the
compass moves it by its own law inside the allowance. Every trial, allowance, refusal and abandonment is in the audit
(`cost`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's record.

**The objectives**, declared here with the one that counts:

| Objective | The cost the verdict judges, one sample a second | Runs |
|---|---|---|
| **resource** (the Omni index's reading for one machine; **the counted set**) | package power (W) × mean latency / requests inside the line: a notch passes only if the energy saved outweighs the speed lost, by the index's own arithmetic (the machine count is one in both arms; the host's busy share is shown and not judged, since it is not a resource an operator pays for on one machine) | three |
| **per-work** (the card's reading: work per energy; the second set) | package power / requests inside the line, which is the energy per request inside the line; the speed is left to the compass's own line as the guardrail | three |
| service | latency / work: refuses every notch by construction; named for completeness, not run | none |

## 4. The service and the load

- One request is **k passes of SHA-256 over 64 KB** (CPU-bound, no I/O). k is calibrated once per run, at the top clock, to
  about **5 ms of one core**, and is then fixed for every arm and repetition of the run; k and the measured time are in the
  run file.
- One worker process per CPU. The load is **open**: requests are offered at the step's rate whether or not the last ones were
  answered, so both arms are offered the same work; the same seed gives the same spacing (a Poisson-like spread around the
  rate).
- Capacity at the top clock = CPUs × 1,000 / service ms. The unit rate = capacity × 0.9 / 8, so **step 8 offers 90% of the
  machine's capacity** at the top clock and step 1 offers about 11%.
- Workloads, 60 s a step: **tuning** (steady at step 3: `3 3 3 3 3 3`, the case the rules are frozen on, shown and not
  counted); **wandering** (`1 2 3 2 3 4 5 6 5 4 3 2 1 2 1`, the Kubernetes tests' own schedule); **burst** (`1 6 1 8 1 6`).
- **The line is 20 ms**: four times the service time at the top clock, so that at half the clock a request still answers in
  about 10 ms and the governor, not the line, decides what is possible; the line binds only when the queue builds.
- Three paired repetitions a run, native and omni alternating in order by repetition; each repetition's requests are the
  same in both arms. Three runs, A, B and C, on the same machine or on three machines of one kind, read by the three-run rule
  (`docs/OMNI_V1.md`): GAIN in all three of our runs, power given in all three of our runs, no difference beyond the noise (with the count), or the runs
  disagree. Never "not confirmed".

## 5. The gauges

| Gauge | Direction |
|---|---|
| work inside the response line (requests a second answered within 20 ms) | higher |
| throughput (requests a second) | higher |
| latency p95, p99, mean (ms) | lower |
| failed requests (not answered by the end of the arm) | never more |
| **energy, CPU package (J; the processor's own meter; the resource)** | lower |
| power, CPU package mean (W) | lower |
| **energy per 1,000 requests inside the line (J)** | lower |
| energy, whole machine at the wall (J; where a plug is fitted) | lower |
| frequency ceiling held, mean (MHz; the knob) | shown |
| frequency run at, mean (MHz; the governor's own choice under the ceiling) | shown |
| CPU busy (share of the run) | shown |
| ceiling changes written | shown |

## 6. The meter, and what is claimed

Energy is read from the processor's own energy counter (RAPL, `/sys/class/powercap/*rapl*:N/energy_uj`, summed over the
packages, wrap-around handled). In our evidence classes it is **class P**, a physical meter on the device, with the caveat
said plainly: RAPL is the processor's own calibrated counter, not an external meter; published comparisons put it within a
few percent of external meters on package power, and a referee who wants more fits a plug. Where a smart plug is fitted
(`WALL_METER`, `tools/wall_meter.py`, as the card test uses it) the whole machine's energy at the wall is reported beside it,
read by the harness only: Omni never sees it, so it is independent of Omni. No energy is claimed beyond what a meter read.
The modelled machine the tests run on is never a result; the table tool flags a run made on it.

## 7. What makes a run invalid, said before the run

- The ceiling found at a value Omni did not write (another writer): the arm stops writing and the run is reported with it.
- The ceiling not handed back, or not read back equal to the snapshot, at the end of an omni arm.
- Failed requests above 0.1% of those offered in either arm: the load is sized above the machine; the run is reported and
  the utilization at step 8 lowered by amendment before the next.
- The governor changed between arms, or the native arm's mean clock at step 8 under 90% of its top (a firmware cap, a
  machine on battery or throttling): reported, and the run read with that said.
- A run on a machine where the probe said no (a virtual machine, no meter, no root) is not a run.

## 8. Where it runs, what it costs, what the founder does

GitHub's own machines are virtual: they expose neither the governor nor the meter, and the workflow's first job proves it
with the probe on every dispatch. The benchmark runs on a machine on the metal, as root:

1. **Your own tower or laptop, on Linux** (a live USB stick counts; an Intel or AMD processor of the last ten years has the
   meter): free. Open a terminal, then
   `git clone https://github.com/the-omni-compass-llc/the-omni-compass && cd the-omni-compass && pip3 install -r requirements.txt`,
   then `sudo bash scripts/cpu_power_run.sh`. It probes the machine, runs the three workloads native and omni, three
   repetitions each (about an hour and a quarter), and leaves a folder `cpu-power-<time>/` with every raw file and the
   report. Do it three times (A, B, C), zip the three folders and send them, or add them to the repository under
   `results/live/raw/`; `tools/cpu_power_abc.py` makes the table.
2. **A rented bare-metal server** (an hourly dedicated machine from Hetzner, OVH, Equinix Metal or the like, not a virtual
   machine): about $10 for the three runs. The same commands.
3. **A self-hosted GitHub runner** registered on either machine lets the workflow run it from the Actions page with the
   runner's label in the `runner` input; the files come back as the run's artifact.

A plug on the wall socket (a Shelly or Tasmota plug, $20 to $30) adds the whole machine's energy: `WALL_METER=shelly2:<ip>`.

## 9. Expected before the run, in writing

- **Under the resource objective** (the counted set): on a machine whose idle package power is a large share of its power
  at step 3 (a desktop lightly loaded), a notch down costs more speed than it saves energy by the index's arithmetic; the
  brain refuses the first notch, the ceiling stays at the top, every gauge reads inside the noise and the category reads
  exactly nothing: no gain, no loss. On a machine whose dynamic power dominates (a server 30% to 50% busy), notches are
  allowed while power falls faster than latency rises: energy −5% to −20%, latency +5% to +25% inside the line, work inside
  the line unchanged.
- **Under the per-work objective**: notches are allowed down toward where the line binds at steps 6 to 8: energy −10% to
  −30% at the low steps, latency up but inside the line, no failed request; p95 and mean higher as point estimates and
  perhaps LOSS in all three of our runs, a trade shown with both readings.
- In both: the ceiling returns to the top under the bursts (fail up) and is handed back at the end of every arm; the
  wandering schedule shows the ceiling following the demand.

**Dispatch.** None yet: the harness waits for a machine, the founder's own or a rented one; the first run on it is the tuning
workload, shown and not counted. The rules above are frozen before it.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
