# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The power-cap band (omni-v15, omnicompass/adapter.py): the brain's request for the power cap trims to demand only while
the response line has been clean for the caller's own clear time (obs slo_clean: the Kubernetes governor's --slo-clear-s,
180 s; the card governor's --slo-clear decisions); a breach of the line or a line not yet clean releases it to the start
limit in the same decision; a caller that senses no line is clean. On the omni-v11 long run (run 39173420146, the
robustness long scenario, three paired repetitions of two hours on real Kubernetes) the request switched between the
start limit and the trim at 126 of 350 decisions and turned back at 123 of them, at the one threshold on the queue and the
state (docs/CHANGE_CONTROL.md); on the same decisions, read from the governor's own audit, the gate leaves 35 moves. The
request is tested here as the brain makes it: on Kubernetes the cap wire is off, and on a card the request passes the
shield (omni_controller/gpu_governor.py), which applied the same gate outside the brain before omni-v15."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.adapter import AllocationLaw, Governor, clamp, mode_law, observe_vector  # noqa: E402

CALM = {"queue_ratio": 0.0, "load_ratio": 0.3, "power_stress": 0.4, "thermal": 0.3}
BREACH = {**CALM, "queue_ratio": 1.5}            # the response line breached: the controller folds its pressure into the queue
FIXTURE = ROOT / "tests" / "fixtures" / "robust_long_39173420146_decisions.json"


def requests(law, obs_seq, nodes=6):
    """The requests of one governor fed a sequence of observations, with the state's U and the machine step beside each
    (the Kubernetes governor's wiring: the cap is never written, so the current cap it hands the brain stays native's, 1.0)."""
    g = Governor(law=law); out = []
    for o in obs_seq:
        g.current_cap = 1.0; g.nodes = nodes
        d = g.step(o, 0)
        out.append((d["power_cap"], d["state"]["U"], d["node_delta"]))
    return out


def trim_target(law, obs):
    return clamp(1.0 * obs["load_ratio"] * (1.0 + law.margin), law.cap_min, 1.0)


def wear(caps):
    moves = [b - a for a, b in zip(caps, caps[1:]) if b != a]
    return len(moves), sum(1 for a, b in zip(moves, moves[1:]) if (a > 0) != (b > 0)), sum(abs(m) for m in moves)


def test_observe_vector_carries_the_clear_flag():
    assert observe_vector({}, 0)["clean"] == 1.0, "a caller that senses no line is clean"
    assert observe_vector({"slo_clean": True}, 0)["clean"] == 1.0 and observe_vector({"slo_clean": False}, 0)["clean"] == 0.0
    assert not hasattr(AllocationLaw(), "cap_dwell"), "the band adds no constant to the law: the clear time is the caller's own"


def test_clean_line_trims_and_an_unclean_line_releases():
    law = mode_law("fleet")
    seq = requests(law, [CALM] * 30)
    on = [cap for cap, U, delta in seq if U >= law.U_gate and delta <= 0]
    assert on and all(abs(cap - trim_target(law, CALM)) < 1e-12 for cap in on), "calm, over the gate, the line clean: the trim at every decision, as omni-v14 asked"
    seq2 = requests(law, [{**CALM, "slo_clean": False}] * 30)
    assert all(cap == 1.0 for cap, _, _ in seq2), "the same decisions with the line not yet clean: the start limit at every one"
    mixed = [{**CALM, "slo_clean": (i % 5) != 0} for i in range(30)]
    seq3 = requests(law, mixed)
    for (cap, U, delta), o in zip(seq3, mixed):
        if U >= law.U_gate and delta <= 0:
            assert cap == (trim_target(law, CALM) if o["slo_clean"] else 1.0), "decision by decision, the flag alone switches the request"


def test_breach_releases_in_the_same_decision():
    law = mode_law("fleet")
    g = Governor(law=law); caps = []
    for o in [CALM] * 20 + [BREACH] + [CALM] * 3:
        g.current_cap = 1.0; g.nodes = 6
        caps.append(g.step(o, 0)["power_cap"])
    assert caps[19] == law.cap_min and caps[20] == 1.0, "the trim before the breach; the start limit in the decision of the breach"


def test_spread_under_backlog_is_not_delayed():
    """power_protect: under backlog at the power envelope the cap spreads down a step at once (a protective move, outside the gate)."""
    law = AllocationLaw()
    g = Governor(law=law); g.current_cap = 1.0; g.nodes = law.max_nodes      # at the machine ceiling: no step that expands capacity
    d = g.step({"queue_ratio": 0.5, "load_ratio": 0.9, "power_stress": 1.05, "thermal": 0.5, "slo_clean": False}, 0)   # over the backlog envelope (1.0)
    assert d["node_delta"] == 0 and abs(d["power_cap"] - clamp(1.0 - law.spread_step, law.cap_min, 1.0)) < 1e-12, d["power_cap"]


def test_the_long_runs_own_decisions():
    """The omni-v11 long run's three audits (tests/fixtures/robust_long_39173420146_decisions.json, the source files' SHA-256
    inside): the recorded request is omni-v14's rule on the recorded queue and state, decision for decision; the omni-v15 gate
    on the same decisions, read with the recorded clear flag, leaves 35 moves of 126 and 32 reversals of 123."""
    fx = json.loads(FIXTURE.read_text())
    law = mode_law("fleet")
    tot14, tot15 = [0, 0, 0.0], [0, 0, 0.0]
    for n, p in fx["pairs"].items():
        trim = [q < law.guard_queue and U >= law.U_gate for q, U in zip(p["queue_ratio"], p["U"])]
        v14 = [law.cap_min if t else 1.0 for t in trim]            # the load stayed under the floor's: the trim is cap_min throughout
        assert v14 == p["power_cap"], f"pair {n}: the recorded request is not omni-v14's rule on the recorded state"
        v15 = [law.cap_min if (t and c) else 1.0 for t, c in zip(trim, p["slo_clean"])]
        for tot, caps in ((tot14, v14), (tot15, v15)):
            m, r, tr = wear(caps); tot[0] += m; tot[1] += r; tot[2] += tr
    assert tot14[:2] == [126, 123], tot14
    assert tot15[:2] == [35, 32], tot15
    assert tot15[2] < 0.3 * tot14[2], (tot14, tot15)


def main():
    test_observe_vector_carries_the_clear_flag(); test_clean_line_trims_and_an_unclean_line_releases()
    test_breach_releases_in_the_same_decision(); test_spread_under_backlog_is_not_delayed(); test_the_long_runs_own_decisions()
    print("PASS  the power-cap band: the request trims only while the line has been clean for the caller's own clear time, is released "
          "in the decision of a breach, spreads under backlog at once; on the long run's own 350 decisions 35 moves where omni-v14 made 126")


if __name__ == "__main__":
    main()
