# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Study file (scratchpad only, never in the repository): Omni's MAX / dial modes for compute pools, and a wear gauge.
#
# The founder's order: not only "save" (least energy for the work) but "max" (the most work the same machines can do
# inside their edge), with a dial between them, and a health/wear limit so pushing hard never shortens life below native.
#
# The lever that is real in this model: the native autoscaler (HPA/CA) is conservative. It holds utilisation at its
# target (0.70) and only adds machines after utilisation has already risen, a start-up time late; during every ramp it
# queues or drops work it could have served. Omni reads the same meters, forecasts the next window's demand (the recent
# peak arrival rate times the largest jump it has seen, the v5 burst forecast), and pre-warms machines so they are hot
# when the burst lands, running utilisation up to the edge instead of the operator's soft target. Same work served
# within the SLO, fewer drops; at the edge, more of the offered load served than native can.
from __future__ import annotations

import math

# Dial: how hard Omni pushes the pool toward its edge. Each setting is an edge utilisation (how full it runs before it
# calls for more machines) and a queue tolerance (how much wait it will hold, as a share of the SLO), both inside the
# plant's own hard limits. Save = the operator's own; Sprint = right up against the edge.
DIAL = {
    "save":    dict(edge_util=0.70, q_share=0.30, prewarm=0.0),   # the operator's own target, no pre-warm (native-like)
    "balanced": dict(edge_util=0.85, q_share=0.50, prewarm=1.0),  # our default
    "edge":    dict(edge_util=0.92, q_share=0.70, prewarm=1.0),
    "sprint":  dict(edge_util=0.97, q_share=0.90, prewarm=1.5),   # right at the edge, forecast pre-warm widened
}


def max_override(plant, knob, dial):
    """Push a compute pool toward its edge for MAX work. Returns the override dict ({} = native).

    Request pools (not pausable): power stays full (native). The autoscaler target is set so the pool runs at the dial's
    edge utilisation, and machines are pre-warmed to cover the forecast burst so they are hot when it lands. A machine
    pool (ca) is driven the same way through its node count; admission is never paced for request traffic."""
    P = plant.P
    d = DIAL[dial]
    if knob not in ("capacity",):            # MAX touches only the machine count (capacity); power stays native (full)
        return {}
    k = plant.k
    mu = plant.mu(1.0)
    # the demand the next window may bring: the recent peak arrival rate, widened by the largest jump seen (v5 forecast)
    hist = getattr(plant, "_mx_lam", None)
    if hist is None:
        hist = plant._mx_lam = []
        plant._mx_jump = 1.0
    if k > 0:
        a = plant.lam[k - 1]
        if hist and hist[-1] > 0:
            plant._mx_jump = max(plant._mx_jump, a / hist[-1] - 1.0)
        hist.append(a)
        if len(hist) > 20:
            hist.pop(0)
    lam_now = plant.lam[k]
    lam_fore = max(lam_now, (max(hist) if hist else lam_now) * (1.0 + d["prewarm"] * plant._mx_jump))
    # machines to serve the forecast at the dial's edge utilisation, plus the queue already standing
    n_want = math.ceil((lam_fore + plant.Q / max(P["dt"], 1e-9)) / (mu * d["edge_util"]))
    n_want = int(min(P["n_max"], max(P["n_min"], n_want)))
    cur = plant.n + len(plant.pending)
    if P.get("ca") or not P.get("ca"):       # both pods (target lever) and machine pools (same, via target->count)
        if n_want > cur:
            # a target low enough that the HPA provisions up to n_want now (rec = ceil(n*util/target))
            u = max(plant.util, 1e-3)
            tgt = max(0.05, min(P["target"], plant.n * u / n_want))
            return {"target": tgt}
        # at or above what the forecast needs: hold the operator's own target (never fewer machines than native)
        return {"target": P["target"]}
    return {}


# ---------------------------------------------------------------------------------------------------------------------
# Wear / life gauge (reliability physics, scratchpad): life used per unit of work, so the health rule can hold Omni to
# "never age a part faster per unit work than native does".
#
#   silicon electromigration / NBTI: an Arrhenius clock, life halves about every 10 C hotter (Ea ~ 0.5 eV here)
#   thermal cycling (solder fatigue, Coffin-Manson): damage ~ swing^2 per cycle
#   a motor/fan: bearing and insulation life falls with speed and heat
K_B = 8.617e-5          # eV per kelvin


def arrhenius_rate(temp_c, ref_c=45.0, ea=0.5):
    """How fast a chip ages at temp_c, relative to a reference temperature (1.0 at ref_c). Doubles ~ every 10-12 C."""
    t, tr = temp_c + 273.15, ref_c + 273.15
    return math.exp(ea / K_B * (1.0 / tr - 1.0 / t))


def life_used(temps_c, dt_s, ref_c=45.0):
    """Reference-hours of life spent over a run: each decision's Arrhenius rate times its seconds."""
    return sum(arrhenius_rate(t, ref_c) * dt_s for t in temps_c) / 3600.0
