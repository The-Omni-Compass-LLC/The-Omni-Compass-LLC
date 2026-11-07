#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The wire from the wall's alarms to the control panel's buttons: Alertmanager's webhook in, a press of tools/omni_control.py out.

Prometheus fires the governor's alert rules (deploy/prometheus/omni-compass-rules.yaml); Alertmanager sends each firing alert to
this bridge (deploy/monitoring/alertmanager.yml); the bridge looks the alert's name up in the action list the operator wrote
(deploy/monitoring/actions.json) and presses that one button of the control panel with its own operator token, the reason
"alert <name> firing (Alertmanager)" written to the panel's control log like any person's press. It answers GET /metrics with
its own counters.

  python3 tools/omni_alert_bridge.py serve --actions actions.json --panel http://127.0.0.1:9465 --token-file FILE
          [--bind 127.0.0.1] [--port 9466] [--log bridge.jsonl] [--press]

What it may press, and what it never does:
  - It presses only the operator's buttons: factory (Restore factory profile), reset (Return to native), mode (autopilot, watch,
    off) and dial (max, save). The kill switch and its arming are the security role's, and arming takes two people; the bridge
    refuses an action list that names either.
  - It is off until it is told: without --press it writes every press it would make to its log and presses nothing.
  - It acts on an alert that starts firing, once for each firing (Alertmanager's fingerprint and its start time), never on one
    that resolves, and never twice for the same firing however often Alertmanager repeats it.
  - Every decision is one JSON line in its log: the alert, the action, pressed or only written, the panel's answer.
Omni-Compass is the autopilot; this is the wall's hand on the panel, wired to its alarms and held to the panel's own roles.
"""
from __future__ import annotations

import argparse
import json
import sys
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ALLOWED = {"factory": None, "reset": None, "mode": {"mode": ("autopilot", "watch", "off")}, "dial": {"dial": ("max", "save")}}
NEVER = ("kill", "arm")


def load_actions(path: Path) -> dict:
    """The action list: {"alert name": {"button": ..., "body": {...}}}; refused whole when it names a button the bridge may not press."""
    acts = json.loads(path.read_text(encoding="utf-8")).get("actions", {})
    for name, a in acts.items():
        b = a.get("button")
        if b in NEVER:
            raise SystemExit(f"{path}: {name} names the {b} button: the kill switch and its arming are the security role's, never the bridge's")
        if b not in ALLOWED:
            raise SystemExit(f"{path}: {name} names {b!r}; the bridge presses only {', '.join(ALLOWED)}")
        for k, values in (ALLOWED[b] or {}).items():
            if (a.get("body") or {}).get(k) not in values:
                raise SystemExit(f"{path}: {name}: {b} needs {k} in {', '.join(values)}")
    return acts


class Bridge:
    def __init__(self, actions: dict, panel: str, token: str, press: bool, log: Path | None):
        self.actions, self.panel, self.token, self.press, self.log = actions, panel.rstrip("/"), token, press, log
        self.seen: set[tuple[str, str]] = set()
        self.counts: dict[str, int] = {}
        self.lock = threading.Lock()

    def _record(self, rec: dict) -> None:
        self.counts[rec["outcome"]] = self.counts.get(rec["outcome"], 0) + 1
        if self.log:
            with self.log.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec) + "\n")

    def _post(self, button: str, body: dict) -> tuple[int, dict]:
        req = urllib.request.Request(f"{self.panel}/v1/{button}", data=json.dumps(body).encode(), method="POST",
                                     headers={"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.status, json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read() or b"{}")
        except (urllib.error.URLError, OSError) as e:
            return 0, {"error": str(e)}

    def handle(self, payload: dict) -> list[dict]:
        """One Alertmanager webhook: every alert that starts firing and has an action, pressed (or written) once."""
        done = []
        for al in payload.get("alerts", []):
            name = (al.get("labels") or {}).get("alertname", "")
            act = self.actions.get(name)
            key = (al.get("fingerprint") or name, al.get("startsAt") or "")
            rec = {"time": time.time(), "alert": name, "status": al.get("status"), "starts_at": al.get("startsAt")}
            with self.lock:
                if al.get("status") != "firing" or act is None:
                    rec.update(outcome="no action", why="resolved" if al.get("status") == "resolved" else "no action listed for it")
                elif key in self.seen:
                    rec.update(outcome="no action", why="this firing was acted on already")
                else:
                    self.seen.add(key)
                    body = {**(act.get("body") or {}), "reason": f"alert {name} firing (Alertmanager)"}
                    if not self.press:
                        rec.update(outcome="written, not pressed", button=act["button"], body=body)
                    else:
                        code, out = self._post(act["button"], body)
                        rec.update(outcome="pressed" if 200 <= code < 300 else "refused by the panel", button=act["button"], body=body,
                                   panel_status=code, panel_answer=out)
                self._record(rec)
            done.append(rec)
        return done

    def metrics(self) -> str:
        lines = ["# HELP omni_bridge_decisions_total The bridge's decisions on Alertmanager's alerts, by outcome.",
                 "# TYPE omni_bridge_decisions_total counter"]
        lines += [f'omni_bridge_decisions_total{{outcome="{k}"}} {v}' for k, v in sorted(self.counts.items())]
        lines += ["# HELP omni_bridge_pressing 1 when the bridge presses the panel's buttons, 0 when it only writes what it would press.",
                  "# TYPE omni_bridge_pressing gauge", f"omni_bridge_pressing {1 if self.press else 0}"]
        return "\n".join(lines) + "\n"


def server(bridge: Bridge, bind: str, port: int) -> ThreadingHTTPServer:
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _send(self, code, body, ctype="application/json"):
            data = body.encode() if isinstance(body, str) else json.dumps(body).encode()
            self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(data))); self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path == "/metrics":
                return self._send(200, bridge.metrics(), "text/plain; version=0.0.4")
            return self._send(404, {"error": "GET /metrics only"})

        def do_POST(self):
            if self.path != "/alerts":
                return self._send(404, {"error": "POST /alerts only (Alertmanager's webhook)"})
            n = int(self.headers.get("Content-Length") or 0)
            try:
                payload = json.loads(self.rfile.read(n) or b"{}")
            except json.JSONDecodeError:
                return self._send(400, {"error": "not JSON"})
            return self._send(200, {"decisions": bridge.handle(payload)})
    return ThreadingHTTPServer((bind, port), H)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("serve")
    s.add_argument("--actions", required=True); s.add_argument("--panel", required=True); s.add_argument("--token-file", default="")
    s.add_argument("--bind", default="127.0.0.1"); s.add_argument("--port", type=int, default=9466); s.add_argument("--log", default="")
    s.add_argument("--press", action="store_true", help="press the panel's buttons (without it: write what it would press, press nothing)")
    c = sub.add_parser("check"); c.add_argument("--actions", required=True)
    a = ap.parse_args(argv)
    acts = load_actions(Path(a.actions))
    if a.cmd == "check":
        print(f"the action list: {len(acts)} alerts wired to the panel's operator buttons; no security button named")
        return 0
    token = Path(a.token_file).read_text(encoding="utf-8").strip() if a.token_file else ""
    if a.press and not token:
        raise SystemExit("--press needs --token-file: an operator token of the control panel")
    br = Bridge(acts, a.panel, token, a.press, Path(a.log) if a.log else None)
    print(f"the alert bridge on {a.bind}:{a.port}: {len(acts)} alerts wired; {'pressing' if a.press else 'writing what it would press, pressing nothing'}")
    server(br, a.bind, a.port).serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
