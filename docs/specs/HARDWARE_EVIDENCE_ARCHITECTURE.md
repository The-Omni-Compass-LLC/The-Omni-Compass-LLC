# Hardware Evidence Architecture

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **Dubra Software Inc. / The Omni-Compass LLC**. The root `LICENSE` controls.


## Purpose

Omni-Compass separates control authority from measurement, attribution, safety, and time synchronization. A measurement source is not an actuator. A synchronization mechanism is not an energy meter. A requested limit is not proof that hardware enforced it.

The physical qualification path therefore uses independent evidence planes and fails closed when those planes disagree.

## Evidence planes

```text
                         OMNI-COMPASS
                    canonical six-state core
                              |
                       bounded authority
                              |
                 +------------+------------+
                 |                         |
            ACTUATION PLANE           AUDIT PLANE
                 |                         |
        NVIDIA power-limit write       decision log
                 |                     state + command
                 v                         |
              GPU plant <-----------------+
                 |
       +---------+----------+--------------------+
       |                    |                    |
 ENERGY PLANE        ATTRIBUTION PLANE       SAFETY PLANE
       |                    |                    |
 DCGM energy         requested/enforced      thermal events
 RAPL energy         limit readback          power brake
 wall meter          clock-event reasons     restore watchdog
       |
 successful frozen work
       |
       v
 work / joule
```

Timing is a separate optional plane. It is required only when receipts from independent clocks must be placed on a common timeline.

## NVIDIA GPU evidence

For the single-GPU counted run, one workload owns one GPU. The power-limit writer is singular. The scored interval records:

- GPU identity, driver, persistence mode, default/min/max/start limit;
- requested and enforced power limits when the installed stack exposes them;
- board power, total-energy counter where available, utilization, clocks, temperature;
- raw and decoded clock-event reasons;
- workload unit, completed work, failures and latency;
- Omni CPU cost;
- restoration to the frozen starting limit.

The preferred device-energy receipt is the cumulative device energy counter. Integrated sampled board power remains an independent numerical cross-check. A disagreement large enough to call telemetry quality into question is reported, not averaged away.

### Attribution rules

A lower requested power limit is not credited to Omni unless the device readback establishes that the request landed and the enforced limit is compatible with the claimed intervention.

`SwPowerCap` while useful work and service guardrails hold is compatible with the software power cap being operative. Thermal slowdown, hardware slowdown, or hardware power brake is adverse attribution evidence and prevents crediting the reduction to Omni. `GpuIdle` requires a starvation check. Application-clock limitation indicates another clock authority. Unknown/new bits are preserved in raw form.

A transient instantaneous power sample above a nominal cap is not by itself a failed experiment. The scored objects are enforced authority, accumulated energy, successful work, service behavior, and the device's own limiter/event evidence.

## CPU/package evidence

Production measurement uses Linux powercap zones when present:

```text
/sys/class/powercap/intel-rapl:*/energy_uj
/sys/class/powercap/intel-rapl:*/max_energy_range_uj
/sys/class/powercap/intel-rapl:*/constraint_*_power_limit_uw
/sys/class/powercap/intel-rapl:*/constraint_*_time_window_us
```

Counter wrap is handled with the reported range. Package, DRAM, and platform/PSYS scopes remain distinct and are never blindly summed. Raw Intel MSRs are a diagnostic path for missing sysfs, lock-state investigation, or platform bring-up, not the normal Omni receipt path. The kernel interface is preferred because it owns model-specific units and quirks.

## Whole-node evidence

GPU-board joules and CPU-package joules are not whole-machine joules. When whole-node efficiency is claimed, an independent wall/PDU meter is the primary whole-system energy receipt. Device and package counters remain supporting attribution evidence.

No wall meter is permitted to steer the governor during the qualification run.

## Timing plane

### Single node

`CLOCK_MONOTONIC` is sufficient for duration and event ordering in the current single-node GPU experiment. PTP, PCIe PTM, boundary clocks, and NIC DPLLs are not dependencies of that experiment.

### Distributed receipts

When receipts from multiple machines must share a common physical timeline, the timing hierarchy may be:

```text
GNSS / atomic reference
        |
PTP Grandmaster
        |
IEEE 1588 PTP over Ethernet
        |
NIC PHC
        |
PCIe PTM where supported end-to-end
        |
root/device time correlation
```

PTP distributes time across a network. PCIe PTM correlates time across a PCIe path. Neither measures energy and neither writes a power limit.

### PTP ordinary, boundary, and transparent clocks

An Ordinary Clock is an endpoint. A Boundary Clock has multiple ports but one disciplined clock: a parent-facing SLAVE port disciplines that clock and downstream MASTER ports originate new Sync messages from it. A Transparent Clock forwards the timing exchange and accounts for residence/link delay in the correction field. Boundary and transparent behavior must not be double-counted.

A multi-NIC boundary clock is not accepted as one clock merely because multiple interfaces are configured. Independent PHCs require a declared synchronization mechanism or shared hardware timebase.

### Servo qualification

linuxptp PI and linreg are distinct servo algorithms.

PI derives correction from proportional and integral error. Its effective gains may be fixed or derived from the Sync interval. Repeated frequency saturation is a diagnostic condition, not an instruction to widen authority blindly.

linreg fits a weighted relationship between recent local-PHC and master-time observations. Its adaptive history selects among recent windows in the implementation; it has no PI Kp/Ki tuning surface. The common outer policy still governs step/slew behavior, maximum frequency, and stable-lock criteria.

For an evidence-grade distributed run, the receipt should preserve GM identity, parent identity, steps removed, servo algorithm/state, offset, frequency adjustment, saturation state, hardware timestamping, phase-step events, and holdover state. "PTP enabled" alone is not evidence of a qualified common timebase.

### NIC DPLL

A NIC DPLL is hardware, not a linuxptp `clock_servo`. On supported timing NICs it may lock frequency/phase to GNSS 1PPS, external pins, or recovered line timing and provide holdover. `ptp4l`, `ts2phc`, and `phc2sys` have separate roles. A PHC must not be silently disciplined by competing time-of-day owners.

DPLL lock and PTP synchronization are separate states and must be reported separately.

## Qualification rule

The current physical claim is deliberately narrow:

```text
successful SLO-compliant frozen work unit
------------------------------------------
independently measured energy
```

A publishable result requires frozen code/configuration, Native/Watch/Omni separation, Watch with zero writes, verified requested/enforced authority, no hostile limiter explaining the result, service guardrails, restoration, and the preregistered statistical decision rule.

PTP/PTM/DPLL sophistication cannot substitute for missing joules or missing useful work.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
