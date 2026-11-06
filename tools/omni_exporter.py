#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governor's gauges for Prometheus and Grafana, read from its own audit (read-only: it writes nothing anywhere).

  python3 tools/omni_exporter.py serve --audit /var/log/omni/audit.jsonl [--port 9464] [--bind 127.0.0.1]
      follows the audit the governor writes (omni_controller/controller.py, one JSON record a line) and serves its gauges
      at http://<bind>:<port>/metrics in Prometheus's text format, for the monitoring an operator already runs
  python3 tools/omni_exporter.py once --audit FILE
      reads the whole audit once and prints the same page (a finished run's receipt, or a check by hand)

Every gauge comes from a record the governor already writes; nothing in the engine changes for it, and the engine's
fingerprint does not move. The exporter has no button: it reads one file and answers GET /metrics. The settings are
changed only by the governor, the kill switch (tools/omni_switch.py) and the operator's own tools, so a monitoring
system that scrapes it can see everything and change nothing. The Grafana screen that reads these gauges is
deploy/grafana/omni-compass.json.

The gauges (names as Prometheus shows them):
  omni_decisions_total, omni_decision_seconds_sum/_count, omni_decision_seconds_last   the governor's decisions and their time
  omni_last_decision_timestamp_seconds                                                 its heartbeat: alert when it stops moving
  omni_heartbeat_seconds                                                               its beat as measured: the median time between
                                                                                         its last eleven full decisions (the dial's
                                                                                         setting it runs at, 5 to 120 s; omni-v17)
  omni_writes_total{why}                                                                the settings commands it wrote, by reason
  omni_recommended{setting}                                                             the setting its last decision recommends
  omni_recommended_moves_total{setting}, omni_recommended_reversals_total{setting}      how often each recommendation moved, and
                                                                                         how often it turned back the other way;
                                                                                         a recommendation is not a write: what was
                                                                                         written is omni_writes_total
  omni_nodes_observed, omni_compass_position, omni_compass_force                        what it sees, where the compass stands
  omni_sense_blind{sense}                                                               1 while a sense is blind (it then holds)
  omni_verdict_state{state}                                                             1 for the verdict's current state
  omni_master_switch                                                                    1 while governing, 0 once switched off
  omni_own_cpu_cores                                                                    its own processor, from its last overhead record
  omni_compass_decisions_total{zone}                                                    decisions by where the compass stood: slack (under
                                                                                         the lower cushion), band, wall (at or past the line)
  omni_wall_recovery_seconds_sum/_count, omni_wall_recovery_seconds_max                  from the first decision at the wall to the first
                                                                                         back inside it: the time to recover (settling time)
  omni_recommended_travel_total{setting}                                                the distance each recommendation travelled, summed
  omni_errors_total{kind}                                                               the errors the governor recorded, by their head
  omni_audit_records_total, omni_audit_unreadable_total                                 the audit itself
"""
from __future__ import annotations

import argparse, json, math, os, re, sys, threading, time
from collections import deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# the recommended settings the decision record carries, by the name the gauges give them
SETTINGS = {"hpa_target": ("decision", "hpa_target_recommended"), "nodes": ("decision", "nodes_recommended"),
            "power_cap": ("decision", "power_cap")}


def _num(x):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) else None


def _label(v: str) -> str:
    return str(v).replace("\\", "\\\\").replace("\n", " ").replace('"', '\\"')


class Gauges:
    """Every gauge, built record by record from the audit."""

    def __init__(self):
        self.lock = threading.Lock()
        self.records = self.unreadable = self.decisions = 0
        self.decision_s_sum, self.decision_s_last, self.decision_count = 0.0, None, 0
        self.last_decision_t = None
        self.beat_t = deque(maxlen=11)                # when the last eleven decisions finished: the beat, measured
        self.writes: dict[str, int] = {}
        self.setting: dict[str, float] = {}
        self.moves: dict[str, int] = {}
        self.reversals: dict[str, int] = {}
        self._last_dir: dict[str, int] = {}
        self.nodes_observed = self.position = self.force = None
        self.blind: dict[str, int] = {}
        self.verdict_state = None
        self.switch = 1
        self.own_cpu = None
        self.zones = {"slack": 0, "band": 0, "wall": 0}
        self._wall_since = None
        self.recovery_sum, self.recovery_count, self.recovery_max = 0.0, 0, None
        self.travel: dict[str, float] = {}
        self.errors: dict[str, int] = {}

    def feed(self, line: str):
        line = line.strip()
        if not line:
            return
        with self.lock:
            self.records += 1
            try:
                r = json.loads(line)
            except ValueError:
                self.unreadable += 1
                return
            if not isinstance(r, dict):
                self.unreadable += 1
                return
            self._take(r)

    def _take(self, r: dict):
        t = _num(r.get("time"))
        ms = _num(r.get("decision_ms"))
        if ms is not None:                             # one decision finished (the governor writes its time last)
            self.decision_count += 1
            self.decision_s_sum += ms / 1000.0
            self.decision_s_last = ms / 1000.0
            self.last_decision_t = t if t is not None else self.last_decision_t
            if t is not None:
                self.beat_t.append(t)
        d = r.get("decision")
        if isinstance(d, dict):
            self.decisions += 1
            self.nodes_observed = _num(d.get("nodes_observed")) if "nodes_observed" in d else self.nodes_observed
            law = d.get("compass_law") if isinstance(d.get("compass_law"), dict) else {}
            self.position = _num(law.get("position")) if "position" in law else self.position
            self.force = _num(law.get("force")) if "force" in law else self.force
            self._zone(_num(law.get("position")), _num(law.get("wall")), t)
            for name, (_, key) in SETTINGS.items():
                self._setting(name, _num(d.get(key)))
        elif isinstance(d, str) and re.search(r"master switch: OFF", d):
            self.switch = 0
        if "write" in r:
            why = str(r.get("why") or "unstated")
            kind = re.split(r"[:(=]| to ", why, maxsplit=1)[0].strip()[:40] or "unstated"   # the reason's head: convey, reset, ...
            self.writes[kind] = self.writes.get(kind, 0) + 1
        a = r.get("authority")
        if isinstance(a, dict) and isinstance(a.get("senses"), dict) and isinstance(a["senses"].get("blind"), dict):
            for sense, b in a["senses"]["blind"].items():
                self.blind[str(sense)] = 1 if b else 0
        if isinstance(r.get("verdict"), dict) or "state" in r and "machines_native" in r:
            st = r.get("state")
            if isinstance(st, str):
                self.verdict_state = st
        o = r.get("overhead")
        if isinstance(o, dict) and _num(o.get("cores_mean")) is not None:
            self.own_cpu = o["cores_mean"]
        if r.get("error"):
            kind = str(r["error"]).split(":", 1)[0].strip()[:40] or "unstated"
            self.errors[kind] = self.errors.get(kind, 0) + 1

    def beat(self):
        """The median spacing of the last eleven decisions (a skipped slot moves it less than a mean would); None before two."""
        gaps = sorted(b - a for a, b in zip(self.beat_t, list(self.beat_t)[1:]) if b > a)
        if not gaps:
            return None
        m = len(gaps) // 2
        return gaps[m] if len(gaps) % 2 else (gaps[m - 1] + gaps[m]) / 2.0

    def _zone(self, pos, wall, t):
        """Where the compass stood at a decision, and the time from the first decision at the wall to the first back inside."""
        if pos is None:
            return
        wall = 0.95 if wall is None else wall
        zone = "wall" if pos >= wall else ("slack" if pos < 1.0 - wall else "band")
        self.zones[zone] += 1
        if zone == "wall":
            if self._wall_since is None:
                self._wall_since = t
        elif self._wall_since is not None:
            if t is not None:
                rec = t - self._wall_since
                self.recovery_sum += rec; self.recovery_count += 1
                self.recovery_max = rec if self.recovery_max is None else max(self.recovery_max, rec)
            self._wall_since = None

    def _setting(self, name: str, v):
        if v is None:
            return
        old = self.setting.get(name)
        self.setting[name] = v
        if old is None or v == old:
            return
        self.moves[name] = self.moves.get(name, 0) + 1
        self.travel[name] = self.travel.get(name, 0.0) + abs(v - old)
        way = 1 if v > old else -1
        if self._last_dir.get(name, way) != way:           # it moved one way, then the other: a reversal
            self.reversals[name] = self.reversals.get(name, 0) + 1
        self._last_dir[name] = way

    def page(self) -> str:
        with self.lock:
            out = []

            def g(name, kind, help_, samples):
                out.append(f"# HELP {name} {help_}")
                out.append(f"# TYPE {name} {kind}")
                for labels, v in samples:
                    lab = "{" + ",".join(f'{k}="{_label(x)}"' for k, x in labels.items()) + "}" if labels else ""
                    out.append(f"{name}{lab} {float(v):.6g}" if v is not None else f"{name}{lab} NaN")

            g("omni_decisions_total", "counter", "Decisions the governor recorded.", [({}, self.decisions)])
            g("omni_decision_seconds", "summary", "Time each decision took, seconds.",
              [])
            out.append(f"omni_decision_seconds_sum {self.decision_s_sum:.6g}")
            out.append(f"omni_decision_seconds_count {self.decision_count}")
            g("omni_decision_seconds_last", "gauge", "Time the last decision took, seconds.", [({}, self.decision_s_last)])
            g("omni_last_decision_timestamp_seconds", "gauge", "Unix time of the last finished decision (the heartbeat).",
              [({}, self.last_decision_t)])
            g("omni_heartbeat_seconds", "gauge", "The governor's beat as measured: the median time between its last eleven "
              "full decisions, seconds (the dial's setting it runs at).", [({}, self.beat())])
            g("omni_writes_total", "counter", "Settings commands the governor wrote, by the head of their reason.",
              [({"why": k}, v) for k, v in sorted(self.writes.items())])
            g("omni_recommended", "gauge", "The setting the governor's last decision recommends (not necessarily written).",
              [({"setting": k}, v) for k, v in sorted(self.setting.items())])
            g("omni_recommended_moves_total", "counter", "Times each recommended setting changed.",
              [({"setting": k}, self.moves.get(k, 0)) for k in sorted(self.setting)])
            g("omni_recommended_reversals_total", "counter", "Times each recommended setting turned back the other way.",
              [({"setting": k}, self.reversals.get(k, 0)) for k in sorted(self.setting)])
            g("omni_nodes_observed", "gauge", "Machines the governor saw in service at its last decision.",
              [({}, self.nodes_observed)])
            g("omni_compass_position", "gauge", "The compass law's position in its band (0 to 1).", [({}, self.position)])
            g("omni_compass_force", "gauge", "The compass law's force at the last decision.", [({}, self.force)])
            g("omni_sense_blind", "gauge", "1 while a sense is blind (the governor holds).",
              [({"sense": k}, v) for k, v in sorted(self.blind.items())])
            g("omni_verdict_state", "gauge", "1 for the verdict's current state.",
              [({"state": self.verdict_state}, 1)] if self.verdict_state else [])
            g("omni_master_switch", "gauge", "1 while governing, 0 once the master switch handed every setting back.",
              [({}, self.switch)])
            g("omni_own_cpu_cores", "gauge", "The governor's own processor, mean cores, from its last overhead record.",
              [({}, self.own_cpu)])
            g("omni_compass_decisions_total", "counter", "Decisions by where the compass stood: slack (under the lower "
              "cushion), band, or wall (at or past the line).", [({"zone": k}, v) for k, v in self.zones.items()])
            g("omni_wall_recovery_seconds", "summary", "From the first decision at the wall to the first back inside it, seconds.", [])
            out.append(f"omni_wall_recovery_seconds_sum {self.recovery_sum:.6g}")
            out.append(f"omni_wall_recovery_seconds_count {self.recovery_count}")
            g("omni_wall_recovery_seconds_max", "gauge", "The longest recovery from the wall so far, seconds.",
              [({}, self.recovery_max)])
            g("omni_recommended_travel_total", "counter", "The distance each recommended setting travelled, summed.",
              [({"setting": k}, self.travel.get(k, 0.0)) for k in sorted(self.setting)])
            g("omni_errors_total", "counter", "Errors the governor recorded, by the head of the error.",
              [({"kind": k}, v) for k, v in sorted(self.errors.items())])
            g("omni_audit_records_total", "counter", "Audit lines read.", [({}, self.records)])
            g("omni_audit_unreadable_total", "counter", "Audit lines that were not one JSON record.", [({}, self.unreadable)])
            return "\n".join(out) + "\n"


def follow(path: Path, gauges: Gauges, stop: threading.Event, every: float = 1.0):
    """Read the audit from its start, then every line appended; a rotated or truncated file is read again from its start."""
    pos, ino, buf = 0, None, ""
    while not stop.is_set():
        try:
            st = path.stat()
            if ino is not None and (st.st_ino != ino or st.st_size < pos):
                pos, buf = 0, ""
            ino = st.st_ino
            with path.open("r", encoding="utf-8", errors="replace") as f:
                f.seek(pos)
                chunk = f.read()
                pos = f.tell()
            buf += chunk
            *lines, buf = buf.split("\n")
            for ln in lines:
                gauges.feed(ln)
        except FileNotFoundError:
            pass
        stop.wait(every)


def server(gauges: Gauges, bind: str, port: int) -> ThreadingHTTPServer:
    class H(BaseHTTPRequestHandler):
        def do_GET(self):                                   # one path, read-only; every other path and method is refused
            if self.path.split("?", 1)[0] != "/metrics":
                self.send_error(404)
                return
            body = gauges.page().encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass
    return ThreadingHTTPServer((bind, port), H)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["serve", "once"])
    ap.add_argument("--audit", required=True, type=Path)
    ap.add_argument("--port", type=int, default=int(os.environ.get("OMNI_EXPORTER_PORT", "9464")))
    ap.add_argument("--bind", default=os.environ.get("OMNI_EXPORTER_BIND", "127.0.0.1"))
    a = ap.parse_args(argv)
    gauges = Gauges()
    if a.mode == "once":
        with a.audit.open(encoding="utf-8", errors="replace") as f:
            for ln in f:
                gauges.feed(ln)
        sys.stdout.write(gauges.page())
        return 0
    stop = threading.Event()
    threading.Thread(target=follow, args=(a.audit, gauges, stop), daemon=True).start()
    srv = server(gauges, a.bind, a.port)
    print(f"omni exporter: {a.audit} -> http://{a.bind}:{a.port}/metrics (read-only)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        srv.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
