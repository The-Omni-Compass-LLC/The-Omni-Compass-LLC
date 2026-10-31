# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CPU host monitor's record: the harness's own modelled machine (class S), until the real run on a machine with its meter.

No CPU run has been made yet: tools/run_cpu_power.py needs a Linux machine whose processor exposes its energy counter (RAPL,
/sys/class/powercap) and a frequency ceiling it may write, which no GitHub runner offers (the register's row 79; the workflow
cpu-power.yml waits for a self-hosted machine). The founder's order of 20 October: the monitor is built now from what exists,
so that it can be seen working and fills with the real run the day it lands. What exists is the harness itself on its own
modelled plant (``--plant sim``, written for its tests): results/sim/cpu_power_model holds one such run, three repetitions,
60 s an arm, with every sample, every decision of the governor and its receipt. Every number here is a model of a machine,
marked S, shown on the monitor as such and never counted in any table or composition (the machine layer enters the whole
organism as exactly 1 until the real run).

  python3 docs/engine/export_cpu_model.py OUT.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RUN = ROOT / "results" / "sim" / "cpu_power_model"
WL = RUN / "cpu-power-tuning"


def samples(path: Path) -> dict:
    t, power, ceil, cur, busy = [], [], [], [], []
    t0 = None
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if t0 is None:
            t0 = d["t"]
        t.append(round(d["t"] - t0, 2)); power.append(d.get("power_w")); ceil.append(round((d.get("ceiling_khz") or 0) / 1000)); cur.append(round((d.get("cur_khz") or 0) / 1000)); busy.append(d.get("busy"))
    return {"t": t, "power_w": power, "ceiling_mhz": ceil, "cur_mhz": cur, "busy": busy}


def audit(path: Path) -> list:
    out = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if "t" not in d:
            continue
        out.append([d["t"], d.get("force"), round((d.get("ceiling_khz") or 0) / 1000), round((d.get("target_khz") or 0) / 1000),
                    None if d.get("wrote_khz") is None else round(d["wrote_khz"] / 1000), d.get("verdict_phase"), d.get("verdict_direction"), d.get("reading_ms")])
    return out


def one_run_word(key: str, row: dict):
    """One run's word for a gauge of the CPU harness, by the key (tools/readings.py run_word; a count that must never rise, LOSS on any
    rise): None for a gauge the harness shows and does not judge, or one it does not declare."""
    sys.path.insert(0, str(ROOT))
    from tools import readings as R
    from tools.run_cpu_power import GAUGES
    aim = next((d for k, _, d in GAUGES if k == key), None)
    if aim in (None, "shown") or row.get("native") is None or row.get("diff") is None:
        return None
    if aim == R.NEVER_MORE:
        return R.LOSS if row["diff"] > 0 else R.STEADY
    return R.run_word({"native": row["native"], "diff": row["diff"]}, aim)


def main(out: str) -> None:
    if not WL.exists():
        Path(out).write_text(json.dumps({"missing": str(WL.relative_to(ROOT))}), encoding="utf-8")
        return
    tuning = json.loads((WL / "tuning.json").read_text(encoding="utf-8"))
    reps = []
    for rd in sorted(WL.glob("rep-*"), key=lambda p: int(p.name.split("-")[1])):
        rep = {"rep": int(rd.name.split("-")[1]), "arms": {}}
        for arm in ("native", "omni"):
            ad = rd / arm
            if not (ad / "samples.jsonl").exists():
                continue
            a = {"samples": samples(ad / "samples.jsonl")}
            if (ad / "arm.json").exists():
                aj = json.loads((ad / "arm.json").read_text(encoding="utf-8"))
                a["summary"] = {k: aj.get(k) for k in ("requests", "work_inside_line_rps", "p95_ms", "mean_ms", "failed", "energy_j", "power_w_mean",
                                                        "ceiling_mhz_mean", "freq_mhz_mean", "writes", "handed_back") if aj.get(k) is not None and aj.get(k) == aj.get(k)}
                if isinstance(aj.get("verdict"), dict):
                    a["verdict"] = {"state": aj["verdict"].get("state"), "counts": aj["verdict"].get("counts"), "events": aj["verdict"].get("events")}
            if (ad / "audit.jsonl").exists():
                a["audit"] = audit(ad / "audit.jsonl")
            rep["arms"][arm] = a
        reps.append(rep)
    data = {"source": str(RUN.relative_to(ROOT)), "table": str((RUN / "CPU_POWER.md").relative_to(ROOT)), "cls": "S",
            "note": "the harness tools/run_cpu_power.py on its own modelled machine (--plant sim): a model, never a measurement; the real run "
                    "waits for a Linux machine with its energy counter (RAPL) and a writable frequency ceiling (register row 18, cpu-power.yml)",
            "machine": tuning.get("machine"), "engine": tuning.get("engine"), "workload": tuning.get("workload"), "steps": tuning.get("steps"),
            "step_s": tuning.get("step_s"), "line_ms": tuning.get("line_ms"), "unit_rps": tuning.get("unit_rps"), "cover_khz": tuning.get("cover_khz"),
            "notch_khz": tuning.get("notch_khz"), "objective": tuning.get("objective"),
            # each row as its table writes it, and beside it its word read again by the key's one-run rule (tools/readings.py run_word,
            # the 0.5% floor, by the aim tools/run_cpu_power.py declares for the gauge): three paired repetitions are one run
            "paired": {k: {kk: v.get(kk) for kk in ("native", "omni", "diff", "ci95", "n", "significant", "reading")} | {"word": one_run_word(k, v)}
                       for k, v in (tuning.get("paired") or {}).items() if isinstance(v, dict)},
            "reps": reps}
    Path(out).write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "cpu_model.json")
