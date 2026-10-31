# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The monitor wall as a Grafana dashboard: one panel a monitor, each on the open-source feed that carries it live.

The live benchmark engine's monitors (docs/engine/monitors.json) are, in the founder's words, nothing more than a Grafana-type dashboard
wired to the organism. This writes that dashboard (deploy/grafana/omni-compass-wall.json, Grafana's dashboard model, schema 39):
a monitor with a Prometheus expression becomes a panel on that expression (the datasource a variable, ${DS_PROMETHEUS}); a
monitor the page computes from the repository's tables, or from its own clock, becomes a text panel saying so and where the
number lives. Beside deploy/grafana/omni-compass.json (the governor's own eighteen panels on tools/omni_exporter.py) it is the
whole wall for an operator's Grafana. The page embeds the same model and offers it for download; the builder writes the file.
Every panel carries its monitor's number on the page, its order of appearance; the panels run left to right, then the next row, each
under a row for the page's section that holds its monitor, and each says its wiring: the page's code, the Python, the C++, the checks.

  python3 docs/engine/export_grafana.py [OUT.json]      (default: deploy/grafana/omni-compass-wall.json)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REG = HERE / "monitors.json"
PAGE = HERE / "OMNI_COMPASS_LIVE_ENGINE.html"
OUT = ROOT / "deploy" / "grafana" / "omni-compass-wall.json"
W, H, COLS = 12, 8, 2
sys.path.insert(0, str(HERE.parents[1]))
from tools.legal import PLAIN as NOTICE   # noqa: E402  (the notice, written once in tools/legal.py, without its Markdown)
from tools.repo import URL as REPO_URL   # noqa: E402  (the repository, written once in tools/repo.py)


def page_order() -> list:
    """The page's canvases in their order of appearance: the monitors' numbers, as the page itself counts them."""
    import re
    if not PAGE.exists():
        return []
    body = re.sub(r"<script[^>]*>.*?</script>", "", PAGE.read_text(encoding="utf-8"), flags=re.S)
    return [m.group(1) for m in re.finditer(r'<canvas\b[^>]*\bid="([^"]+)"', body)]


def wall_order() -> list:
    """The wall's order: the registry's blocks by importance (the founder's order of 30 October), the first twelve the system's most
    important; a registered monitor in no block follows in the page's own order."""
    reg = json.loads(REG.read_text(encoding="utf-8")) if REG.exists() else {}
    ranked = [i for b in reg.get("blocks", []) for i in b["ids"]]
    return ranked + [c for c in page_order() if c not in ranked]


def page_sections() -> dict:
    """Each canvas's section as the page numbers it, {canvas id: (number, title)}: the nearest section around it whose heading
    carries a number, read from the page's own markup."""
    import re
    if not PAGE.exists():
        return {}
    body = re.sub(r"<script[^>]*>.*?</script>", "", PAGE.read_text(encoding="utf-8"), flags=re.S)
    stack, out = [], {}
    for t in re.finditer(r'<section\b[^>]*>|</section>|<h2\b[^>]*>(.*?)</h2>|<canvas\b[^>]*\bid="([^"]+)"', body, re.S):
        tag = t.group(0)
        if tag.startswith("<section"):
            stack.append(None)
        elif tag == "</section>":
            stack.pop()
        elif tag.startswith("<h2"):
            sn = re.search(r'<span class="sn">([^<]*)</span>', t.group(1))
            if stack and stack[-1] is None and sn:
                stack[-1] = (sn.group(1), re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t.group(1).replace(sn.group(0), ""))).strip())
        else:
            out[t.group(2)] = next((x for x in reversed(stack) if x), ("", ""))
    return out


def wiring(m: dict) -> str:
    w = m.get("wire") or {}
    if not w:
        return ""
    py = ", ".join(w.get("python") or []) or w.get("cpp_none", "none")
    cpp = ", ".join(w.get("cpp") or []) or w.get("cpp_none", "none")
    proof = f"; held equal by {', '.join(w['proof'])}" if w.get("proof") else ""
    return f" Wired: the page's {w['code']} → the Python {py} → the C++ {cpp}{proof}. Moves: {w['moves']}."


SCOPED = re.compile(r"\b((?:omni|node|http)_[a-z0-9_]+)(\{([^}]*)\})?")
KNOBS = 'route=~"$route",provider=~"$provider",instance=~"$instance"'


def scoped(expr: str) -> str:
    """A panel's expression read through the wall's knobs: every omni_, node_ and http_ series filtered by the route, the provider
    and the machine chosen, and a five-minute rate window set by the window knob (a series without the label matches All)."""
    def one(m):
        inner = m.group(3)
        return f"{m.group(1)}{{{inner + ',' if inner else ''}{KNOBS}}}"
    return SCOPED.sub(one, expr).replace("[5m]", "[$window]")


# the knobs on the wall (the founder's order of 24 October: knob it, tune it, give it all its buttons): which route, which
# provider, which machine, the rate window, and the control panel whose buttons the wall's links open
def knobs() -> list:
    q = lambda name, label, query: {"name": name, "label": label, "type": "query", "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                                   "query": {"query": query, "refId": name}, "definition": query, "includeAll": True, "multi": True,
                                   "allValue": ".*", "current": {"selected": True, "text": "All", "value": "$__all"}, "refresh": 2, "sort": 1}
    return [{"name": "DS_PROMETHEUS", "label": "Prometheus", "type": "datasource", "query": "prometheus", "current": {}, "hide": 0},
            q("route", "Route", "label_values(up, route)"),
            q("provider", "Provider", 'label_values(up{route=~"$route"}, provider)'),
            q("instance", "Machine", 'label_values(up{route=~"$route",provider=~"$provider"}, instance)'),
            {"name": "window", "label": "Rate Window", "type": "interval", "query": "1m,5m,15m,1h", "auto": False,
             "current": {"text": "5m", "value": "5m"}},
            {"name": "control", "label": "Control Panel URL", "type": "textbox", "query": "http://localhost:9465",
             "current": {"text": "http://localhost:9465", "value": "http://localhost:9465"}}]


# the key's colours on every panel: native orange, Omni-Compass blue (a series whose name says which side it is)
SIDES = [{"matcher": {"id": "byRegexp", "options": "/native/i"}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "#ff8a1f"}}]},
         {"matcher": {"id": "byRegexp", "options": "/omni|compass/i"}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "#4e97d1"}}]}]


def signals_row() -> list:
    """The wall's first row: the governor's signals as stat panels in the road's shapes' words (redlining red, steady yellow,
    accelerating green), each threshold the alert rule's own (deploy/prometheus/omni-compass-rules.yaml)."""
    def stat(i, x, title, expr, steps, words, desc, unit="short"):
        return {"id": 900 + i, "type": "stat", "title": title, "description": desc, "gridPos": {"x": x, "y": 1, "w": 6, "h": 5},
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "targets": [{"refId": "A", "expr": scoped(expr), "legendFormat": "{{instance}}"}],
                "options": {"colorMode": "background", "graphMode": "area", "reduceOptions": {"calcs": ["lastNotNull"]}, "textMode": "value_and_name"},
                "fieldConfig": {"defaults": {"unit": unit, "thresholds": {"mode": "absolute", "steps": steps},
                                             "mappings": [{"type": "range", "options": {"from": a, "to": b, "result": {"text": w}}} for a, b, w in words]},
                                "overrides": []}}
    g, y, r = "#50c878", "#f5c518", "#ff4d55"
    return [{"id": 899, "type": "row", "title": "Governor Signals", "collapsed": False, "gridPos": {"x": 0, "y": 0, "w": COLS * W, "h": 1}, "panels": []},
            stat(1, 0, "Beats Since Last Decision", "(time() - omni_last_decision_timestamp_seconds) / clamp_min(omni_heartbeat_seconds, 5)",
                 [{"color": g, "value": None}, {"color": y, "value": 1.5}, {"color": r, "value": 3}],
                 [(0, 1.5, "accelerating"), (1.5, 3, "steady"), (3, 1e9, "redlining")],
                 "Beats since the governor's last decision; three beats is the staleness alert's line (OmniGovernorStale)."),
            stat(2, 6, "Blind Sense Readings", "omni_sense_blind", [{"color": g, "value": None}, {"color": r, "value": 1}],
                 [(0, 0.5, "accelerating"), (0.5, 1e9, "redlining")], "1 while a sense the governor needs is unread; the engine holds and says why."),
            stat(3, 12, "Master Switch", "omni_master_switch", [{"color": r, "value": None}, {"color": g, "value": 1}],
                 [(-1, 0.5, "OFF: native alone"), (0.5, 2, "ON")], "ON: Omni-Compass governs; OFF: the kill switch is pulled and native runs alone."),
            stat(4, 18, "Alerts Firing", 'sum(ALERTS{alertstate="firing"}) or vector(0)', [{"color": g, "value": None}, {"color": y, "value": 1}, {"color": r, "value": 2}],
                 [(0, 0.5, "accelerating"), (0.5, 1.5, "steady"), (1.5, 1e9, "redlining")], "Alerts firing now across the wall (Prometheus's ALERTS series).")]


# the live engine's light in Grafana's own thresholds, where the monitor's line is a number on its series (the founder's words of 23
# and 24 October: green working, yellow heading for its line, red an alert): green below, yellow from 97% of the line, red at it;
# a series whose good side is high (the master switch ON, the error budget left) reads the other way
LIGHT = {"feed2": (0.2, False), "feed3": (0.75, False), "opsCandle": (200.0, False), "orchCv": (1.0, False), "ruStrip": (1.0, False),
         "immCv": (1.0, False), "cStrip": (0.95, False), "band": (0.95, False), "masterCv": (1.0, True), "tSlo": (0.999, True), "tBurn": (0.1, True)}
LIGHT_WORDS = (" Its light on the live benchmark engine, a signal standing as a traffic signal does, red on top, yellow in the middle, green at the"
               " bottom: red, an alert, over its line or a LOSS row; yellow, heading for its line (within 3% of it, or its slope crossing"
               " it within three readings), or STEADY on a record; green, working inside its lines.")


def thresholds(mid: str) -> dict:
    line, high_good = LIGHT.get(mid, (None, False))
    if line is None:
        return {"mode": "absolute", "steps": [{"color": "green", "value": None}]}
    if high_good:
        return {"mode": "absolute", "steps": [{"color": "red", "value": None}, {"color": "yellow", "value": round(line * 0.97, 6)}, {"color": "green", "value": line}]}
    return {"mode": "absolute", "steps": [{"color": "green", "value": None}, {"color": "yellow", "value": round(line * 0.97, 6)}, {"color": "red", "value": line}]}


def dashboard(reg: dict) -> dict:
    panels = []
    order = {cid: i for i, cid in enumerate(wall_order())}   # every panel numbered as the wall numbers its monitor, by importance, laid out left to right
    blocks = {i: (k, b) for k, b in enumerate(reg.get("blocks", []), 1) for i in b["ids"]}
    sec, last, col, y = page_sections(), None, 0, 6       # under the signals row
    for i, m in enumerate(sorted(reg["monitors"], key=lambda m: order.get(m["id"], len(order)))):
        n = i + 1
        sn, st = sec.get(m["id"], ("", ""))
        k, blk = blocks.get(m["id"], (0, None))
        head = (f"Block {k} · {blk['title']}" if blk else (f"{sn} · {st}" if sn else (st or "the page")))
        if head != last:   # each block of the wall a row, its monitors under it in rank order (the founder's order of 30 October)
            if col:
                col, y = 0, y + H
            panels.append({"id": 1000 + sum(1 for p in panels if p["type"] == "row"), "type": "row", "title": head,
                           "collapsed": False, "gridPos": {"x": 0, "y": y, "w": COLS * W, "h": 1}, "panels": []})
            y, last = y + 1, head
        x = col * W
        title = f"{n} · {m['name']}"
        base = {"id": n, "title": title, "gridPos": {"x": x, "y": y, "w": W, "h": H},
                "description": (f"Section {sn}, {st}. " if sn else "") + f"{m['what']} Evidence class {m['cls']}; on the live benchmark engine: {m['status']}. Feed: {m['feed']['exporter']}."
                               + (f" Awaiting: {m['awaiting']}." if m.get("awaiting") else "") + wiring(m) + LIGHT_WORDS}
        col += 1
        if col == COLS:
            col, y = 0, y + H
        if m["feed"]["promql"]:
            panels.append({**base, "type": m["grafana"]["type"] if m["grafana"]["type"] in ("timeseries", "stat", "bargauge", "heatmap", "table") else "timeseries",
                           "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                           "fieldConfig": {"defaults": {"unit": m["grafana"].get("unit") or "short", "thresholds": thresholds(m["id"]),
                                                        "color": {"mode": "thresholds"}, "custom": {"thresholdsStyle": {"mode": "line+area"}}}, "overrides": SIDES},
                           "targets": [{"refId": chr(65 + j), "expr": scoped(e), "legendFormat": m["feed"]["metrics"][j] if j < len(m["feed"]["metrics"]) else e}
                                       for j, e in enumerate(m["feed"]["promql"])]})
        else:
            panels.append({**base, "type": "text", "options": {"mode": "markdown", "content":
                           f"**{m['name']}** ({reg['layers'].get(m['layer'], m['layer'])}).\n\n{m['what']}\n\nSource: {m['feed']['exporter']}. "
                           f"No Prometheus series carries this panel: the live benchmark engine draws it from the repository's own records or from its own clock; "
                           f"this panel marks its place on the wall (monitor {n}).{LIGHT_WORDS}"}})
    return {"uid": "omni-compass-wall", "title": "Omni-Compass Monitor Wall", "tags": ["omni-compass", "wall"], "timezone": "utc", "schemaVersion": 39, "version": 1,
            "editable": True, "graphTooltip": 1, "time": {"from": "now-6h", "to": "now"}, "refresh": "30s",
            "templating": {"list": knobs()},
            "links": [{"title": "Governor Dashboard", "type": "dashboards", "tags": ["omni-compass"], "asDropdown": False},
                      {"title": "Control Panel", "type": "link",
                       "url": "${control}/", "targetBlank": True, "icon": "bolt"},
                      {"title": "Alertmanager", "type": "link", "url": "http://localhost:9093", "targetBlank": True},
                      {"title": "Live Benchmark Engine", "type": "link", "url": f"{REPO_URL}/blob/main/docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"}],
            "description": NOTICE,
            # the notice at the top and the end of the wall, where Grafana shows it (the underwriting seat of 24 October)
            "panels": [notice_panel(-1)] + signals_row() + panels + [notice_panel(max([p["gridPos"]["y"] + p["gridPos"]["h"] for p in panels] or [0]))],
            "__notice": NOTICE}


def notice_panel(y: int) -> dict:
    """A text panel carrying the legal notice, the full width of the wall: at its top (y below every other panel's 0) and its end."""
    return {"id": 9000 + (0 if y < 0 else 1), "type": "text", "title": "", "gridPos": {"x": 0, "y": max(y, 0) if y >= 0 else 0, "w": COLS * W, "h": 2},
            "transparent": True, "options": {"mode": "markdown", "content": NOTICE}}


def main(out: str | None = None) -> dict:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    d = dashboard(reg)
    p = Path(out) if out else OUT
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return d


if __name__ == "__main__":
    d = main(sys.argv[1] if len(sys.argv) > 1 else None)
    mons = [p for p in d["panels"] if p["type"] != "row" and p.get("id", 0) < 9000]
    print(f"{len(mons)} panels under {len(d['panels']) - len(mons)} section rows, {sum(1 for p in mons if p['type'] != 'text')} on Prometheus series")
