# Distributed Timing Evidence

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

## Scope

This document defines the optional timing layer for experiments whose receipts originate on more than one hardware clock. It is not part of the single-node GPU power-cap counted run.

## PCIe PTM

PCIe Precision Time Measurement is an in-band PCIe timing protocol. A PTM Root provides master-time ancestry; Requesters initiate dialogs; Responders timestamp the adjacent link. Hardware timestamps the request/response exchange. Software does not reproduce PTM by bracketing a transaction with `clock_gettime()` or `rdtsc`.

For one link, with requester request-transmit `t1`, responder request-receive `t2`, responder response-transmit `t3`, and requester response-receive `t4`:

```text
wire_round_trip = (t4 - t1) - (t3 - t2)
one_way_delay   = wire_round_trip / 2
```

The one-way estimate assumes sufficiently symmetric propagation. A PTM path is only qualified when the required root/requester/responder capabilities and every intervening hop are supported and enabled. Timeout/retry, stale-dialog association, asymmetric behavior, or a non-PTM hop invalidates the stronger timing claim.

PTM is not RAPL, thermal control, PTP, or a power actuator.

## IEEE 1588 PTP

PTP distributes a common timebase over a network. In the common end-to-end delay exchange:

```text
delay  = ((t2 - t1) + (t4 - t3)) / 2
offset = ((t2 - t1) - (t4 - t3)) / 2
```

Hardware timestamping at the MAC/PHY is required for evidence-grade nanosecond-class work. Software timestamping is recorded as a weaker timing class rather than silently described as equivalent.

Profiles constrain interoperable behavior. The active profile, delay mechanism, transport, Sync/Announce intervals, and timestamp mode belong in the receipt.

## Boundary Clock

A Boundary Clock has one disciplined timebase. BMCA selects the parent relationship. A SLAVE port receives timing from the selected parent; the servo disciplines the shared PHC/timebase; MASTER ports originate downstream Announce and Sync from that disciplined clock.

Per-port state and the datasets required to establish parentage must be retained when timing provenance matters. `stepsRemoved` is evidence of hierarchy depth and loop prevention, not decoration.

A Boundary Clock is not a Transparent Clock. A Transparent Clock does not terminate and regenerate the timeline; it forwards timing and contributes residence/link-delay correction.

## PI servo

Conceptually:

```text
drift   <- drift + Ki * offset
adj_ppb <- Kp * offset + drift
adj_ppb <- clamp(adj_ppb, -max_frequency, +max_frequency)
```

Actual configured/effective gains and Sync interval are recorded. Post-lock phase steps are timing discontinuities and must be explicitly recorded or excluded from scored intervals. Saturation at `max_frequency` marks loss of normal correction authority and requires diagnosis.

## linreg servo

linreg is a regression servo, not PI with hidden gains. It maintains recent weighted `(local_time, master_time)` observations and fits:

```text
master_time ~= slope * local_time + intercept
frequency_error_ppb = 1e9 * (slope - 1)
```

The implementation adaptively chooses among recent history sizes rather than exposing a `linreg_kp`, `linreg_ki`, or ordinary configuration knob for the window. The common servo cage still controls phase stepping, maximum frequency, and stable-lock declaration.

## DPLL and PHC ownership

The DPLL on a timing-capable NIC is hardware. It may discipline oscillator frequency/phase from physical references and provide holdover. It is not a linuxptp servo option.

`ptp4l` handles network PTP and a PHC servo. `ts2phc` relates external time/1PPS to a PHC. `phc2sys` can transfer time between PHC and system clock. Driver/netlink facilities expose hardware pin/reference/DPLL state on supported devices.

A receipt must name the intentional owner of each clock relationship. Competing undisclosed PHC/ToD writers invalidate the timing provenance.

## Holdover

Loss of the grandmaster or physical reference changes evidence quality. Holdover is explicitly marked. The last frequency estimate or hardware oscillator may preserve useful time, but uncertainty grows with elapsed holdover. A holdover timestamp is not silently labeled equivalent to locked PTP time.

## Omni validity gate

A cross-node causal claim may be qualified only when the declared timing error budget is supported by the recorded clock state. At minimum:

```text
hardware timestamping present
qualified parent / GM identity
servo locked to declared criterion
frequency correction not persistently saturated
no unaccounted phase step
holdover state known
clock ownership unambiguous
```

If the gate fails, the experiment data may remain useful, but the stronger cross-node temporal-causality claim is withheld.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
