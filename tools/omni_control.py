#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The control panel: the governor's buttons behind an authenticated API, each press audited (the engine untouched).

  python3 tools/omni_control.py serve --governor "python3 -m omni_controller.controller --mode target --audit /var/log/omni/audit.jsonl" \\
      --tokens /etc/omni/tokens.json [--audit /var/log/omni/audit.jsonl] [--bind 127.0.0.1] [--port 9465] \\
      [--state /var/lib/omni/control.json] [--log /var/log/omni/control.jsonl] [--cert FILE --key FILE]
      runs the governor as its child and serves the panel: the API at /v1/..., the console (the buttons in a browser page)
      at /, the OpenAPI document at /v1/openapi.json and the panel's own counters at /metrics
  python3 tools/omni_control.py token --name NAME --roles viewer,operator[,security] --tokens FILE
      makes a bearer token, prints it once and stores only its SHA-256 with the holder's name and roles

The buttons (each a POST carrying a bearer token; JSON body):
  POST /v1/mode   {"mode": "autopilot"|"watch"|"off", "reason": ...}   role operator
        autopilot: the governor runs and writes. watch: it runs, decides and audits every decision, and writes nothing (its
        dry run). off: it hands every setting back and stops.
  POST /v1/dial   {"dial": "max"|"save", "reason": ...}                role operator
        the max (the factory default) or the tune-down
  POST /v1/reset  {"reason": ...}                                       role operator
        Return to native: every setting handed back to native; the governor stops (mode off) until the next mode press
  POST /v1/factory {"reason": ...}                                      role operator
        Restore factory profile: the released configuration reapplied (autopilot, the max, every muscle driven, the
        command's own beat), passing through native like every press
  POST /v1/kill   {"reason": ...}                                       role security
        the master switch OFF for every Omni-Compass governor on the machine (omnicompass/master.py): the security switch,
        instant; every governor restores its settings and exits, and none starts while it is OFF
  POST /v1/arm    {"reason": ...}                                       role security
        the master switch ON again, only when two different holders of the security role press it within ten minutes
        (the two-person rule); the first press is recorded and answered 202
  POST /v1/muscle {"muscle": NAME, "on": true|false, "reason": ...}     role operator
        one muscle on (Omni-Compass drives it) or left native (never written), omni-v14's --native; the muscles are the
        governor's own list (omni_controller/controller.py, MUSCLES). Like a dial press, it passes through native: the
        governor hands every setting back and starts again with the new list
  POST /v1/beat   {"seconds": 5 to 120, "reason": ...}                  role operator
        the heartbeat, a dial (omni-v17): the governor's full decision every so many seconds (the main engine 60 s; the
        dial's stops 10, 15, 20, 30, 60, 90 and 120 s, and any value from 5 to 120 s), its fast checks every 5 s at every beat; like
        a dial press it passes through native, and the governor starts again with --interval set to the beat
The reads (role viewer): GET /v1/status (the switch, the desired and the actual state, the governor's process, the
registry and its leases, the age of the last decision), GET /v1/presses (the last presses), GET /metrics. The console
(GET /) and the OpenAPI document (GET /v1/openapi.json) carry no data and need no token; every call the console makes
carries the token typed into it. Operator and security imply viewer.

How a change is made. The engine that stands takes its mode and dial when it starts, and when its own kill file appears it
puts every setting it wrote back to the snapshot it took at its start, reads each one back and exits
(omni_controller/controller.py, --kill-file). So every mode, dial or reset press is: the kill file set, the governor's exit
awaited, the kill file removed, and the governor started again with the new arguments (or left stopped). Every change
passes through native; nothing is changed under a running governor, and nothing in the engine changes for the panel (its
fingerprint does not move). A governor that exits on its own is not restarted by the panel: its settings are handed back
by its lease (tools/omni_switch.py watchdog), and a new start would take a new snapshot over settings not yet handed back.
Status shows it as exited; the next press starts it. Presses are served one at a time.

Security. Bound to 127.0.0.1 unless --bind says otherwise, and a bind beyond the loopback is refused without --cert and
--key (HTTPS). Tokens are kept as SHA-256 digests only; a request without a valid token is answered 401, one whose
holder lacks the role 403. Every press, refused ones included, is one JSON line in the control log: the time, the holder,
the button, the reason, the outcome. The kill switch also stays on the command line and as a file (tools/omni_switch.py
off), so the panel being down never stops anyone from switching Omni-Compass off.
"""
from __future__ import annotations

import argparse, contextlib, hashlib, io, json, os, secrets, shlex, signal, ssl, subprocess, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omnicompass import master                    # noqa: E402
from tools import omni_switch                     # noqa: E402
from tools.legal import PLAIN                     # noqa: E402
from omni_controller.controller import MUSCLES    # noqa: E402

BUTTONS = {"mode": "operator", "dial": "operator", "reset": "operator", "kill": "security", "arm": "security", "muscle": "operator",
           "beat": "operator", "factory": "operator"}
MODES, DIALS = ("autopilot", "watch", "off"), ("max", "save")
MAIN_BEAT, BEAT_RANGE = 60.0, (5.0, 120.0)            # the heartbeat dial (omni-v17): the main engine's beat and the dial's span
BEAT_STOPS = (10, 15, 20, 30, 60, 90, 120)                 # the stops the console offers (the founder's order of 24 October); any value in the span can be pressed
ARM_WINDOW_S = 600.0              # the two-person rule: two different holders of the security role within ten minutes
MAX_BODY = 4096


class Refused(Exception):
    def __init__(self, code, why):
        super().__init__(why)
        self.code, self.why = code, why


# ---------------------------------------------------------------------------------------------------------- the tokens
def digest(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def load_tokens(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def make_token(path: Path, name: str, roles: list[str]) -> str:
    bad = [r for r in roles if r not in ("viewer", "operator", "security")]
    if bad:
        raise SystemExit(f"unknown role(s): {', '.join(bad)} (viewer, operator, security)")
    tok = secrets.token_urlsafe(32)
    t = load_tokens(path)
    t[digest(tok)] = {"name": name, "roles": sorted(set(roles) | {"viewer"}), "made": time.time()}
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path) + ".tmp", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(t, f, indent=1, sort_keys=True)
    os.replace(str(path) + ".tmp", path)
    return tok


# ---------------------------------------------------------------------------------------------------------- the panel
class Panel:
    def __init__(self, governor, kill_file, state=None, log=None, audit=None, flags=None, handback_s=120.0):
        self.cmd = list(governor)
        self.kill_file = Path(kill_file)
        self.state_path, self.log_path, self.audit = state, log, audit
        self.flags = {"kill": "--kill-file", "dial": "--dial", "watch": "--dry-run", "native": "--native", "beat": "--interval",
                      **(flags or {})}
        self.handback_s = handback_s
        self.lock = threading.Lock()
        self.proc = None
        self.arms = {}                                    # security holder -> time of their arm press
        self.counts = {}                                  # (button, outcome) -> presses
        self.desired = {"mode": "off", "dial": "max", "native": [], "beat": None}   # beat None: the command's own (else 60 s)
        if state and Path(state).exists():
            try:
                d = json.loads(Path(state).read_text(encoding="utf-8"))
                self.desired.update({k: d[k] for k in ("dial",) if d.get(k) in DIALS})
                self.desired["native"] = sorted(m for m in (d.get("native") or []) if m in MUSCLES)
                b = d.get("beat")
                if isinstance(b, (int, float)) and not isinstance(b, bool) and BEAT_RANGE[0] <= b <= BEAT_RANGE[1]:
                    self.desired["beat"] = float(b)
            except (OSError, ValueError):
                pass                                      # a panel never starts a governor by itself: mode starts off

    # the governor's process
    def args(self):
        a = self.cmd + [self.flags["kill"], str(self.kill_file), self.flags["dial"], self.desired["dial"]]
        a += [self.flags["native"], ",".join(self.desired["native"])] if self.desired["native"] else []
        a += [self.flags["beat"], f"{self.desired['beat']:g}"] if self.desired["beat"] is not None else []
        return a + ([self.flags["watch"]] if self.desired["mode"] == "watch" else [])

    def beat(self):
        """The beat the governor runs at: the one pressed, else the one its own command sets, else the main engine's 60 s."""
        if self.desired["beat"] is not None:
            return self.desired["beat"]
        flag = self.flags["beat"]
        try:
            return float(self.cmd[len(self.cmd) - 1 - self.cmd[::-1].index(flag) + 1])
        except (ValueError, IndexError):
            return MAIN_BEAT

    def running(self):
        return self.proc is not None and self.proc.poll() is None

    def _start(self):
        if master.is_off():
            raise Refused(409, f"the master switch is OFF ({master.reason() or 'no reason given'}): nothing started; "
                               "two holders of the security role arm it again (POST /v1/arm)")
        with contextlib.suppress(FileNotFoundError):
            self.kill_file.unlink()
        self.proc = subprocess.Popen(self.args(), stdin=subprocess.DEVNULL)
        return {"started": self.proc.pid, "args": self.args()}

    def _hand_back(self):
        """The governor's own kill file set and its exit awaited: it restores every setting it wrote and exits."""
        if not self.running():
            return {"handed_back": "nothing running"}
        self.kill_file.parent.mkdir(parents=True, exist_ok=True)
        self.kill_file.write_text(json.dumps({"by": "omni_control", "time": time.time()}))
        try:
            rc = self.proc.wait(self.handback_s)
            out = {"handed_back": rc == 0, "exit": rc}
        except subprocess.TimeoutExpired:
            self.proc.send_signal(signal.SIGTERM)                  # the governor's own handler hands back on SIGTERM too
            try:
                rc = self.proc.wait(30)
            except subprocess.TimeoutExpired:
                self.proc.kill(); rc = self.proc.wait()
            out = {"handed_back": False, "exit": rc,
                   "why": f"no exit within {self.handback_s:.0f} s; stopped; its lease hands back what it wrote "
                          "(tools/omni_switch.py watchdog)"}
        with contextlib.suppress(FileNotFoundError):
            self.kill_file.unlink()
        return out

    # the buttons
    def press(self, who, button, body):
        reason = str(body.get("reason", ""))[:500]
        rec = {"time": time.time(), "who": who["name"], "button": button, "body": body, "reason": reason}
        try:
            need = BUTTONS[button]
            if need not in who["roles"]:
                raise Refused(403, f"{who['name']} does not hold the {need} role")
            if button in ("kill", "arm", "reset") and not reason:
                raise Refused(400, f"{button} needs a reason")
            with self.lock:
                code, out = 200, getattr(self, f"_{button}")(who, body)
                if isinstance(out, tuple):
                    code, out = out
            rec.update(outcome="done" if code == 200 else "recorded", result=out)
            return code, out
        except Refused as e:
            rec.update(outcome="refused", result={"refused": e.why})
            return e.code, {"refused": e.why}
        finally:
            self.counts[(button, rec["outcome"])] = self.counts.get((button, rec["outcome"]), 0) + 1
            self._log(rec)
            self._save()

    def _mode(self, who, body):
        m = body.get("mode")
        if m not in MODES:
            raise Refused(400, f"mode must be one of {', '.join(MODES)}")
        if m == self.desired["mode"] and (m == "off" or self.running()):
            return {"mode": m, "unchanged": True}
        out = {"hand_back": self._hand_back()}
        self.desired["mode"] = m
        if m != "off":
            try:
                out.update(self._start())
            except Refused:
                self.desired["mode"] = "off"
                raise
        return {"mode": m, **out}

    def _dial(self, who, body):
        d = body.get("dial")
        if d not in DIALS:
            raise Refused(400, f"dial must be one of {', '.join(DIALS)}")
        if d == self.desired["dial"]:
            return {"dial": d, "unchanged": True}
        self.desired["dial"] = d
        if not self.running():
            return {"dial": d, "applies": "at the next start"}
        out = {"hand_back": self._hand_back()}
        out.update(self._start())
        return {"dial": d, **out}

    def _muscle(self, who, body):
        m, on = body.get("muscle"), body.get("on")
        if m not in MUSCLES:
            raise Refused(400, f"muscle must be one of {', '.join(MUSCLES)}")
        if not isinstance(on, bool):
            raise Refused(400, "on must be true (Omni-Compass drives it) or false (left native)")
        native = set(self.desired["native"])
        if (m not in native) == on:
            return {"muscle": m, "on": on, "unchanged": True}
        (native.discard if on else native.add)(m)
        self.desired["native"] = sorted(native)
        if not self.running():
            return {"muscle": m, "on": on, "native": self.desired["native"], "applies": "at the next start"}
        out = {"hand_back": self._hand_back()}
        out.update(self._start())
        return {"muscle": m, "on": on, "native": self.desired["native"], **out}

    def _beat(self, who, body):
        s = body.get("seconds")
        if isinstance(s, bool) or not isinstance(s, (int, float)) or not BEAT_RANGE[0] <= s <= BEAT_RANGE[1]:
            raise Refused(400, f"seconds must be a number from {BEAT_RANGE[0]:g} to {BEAT_RANGE[1]:g} (the dial's stops "
                               f"{', '.join(str(b) for b in BEAT_STOPS)}; the main engine {MAIN_BEAT:g})")
        s = float(s)
        if s == self.beat():
            return {"beat_s": s, "unchanged": True}
        self.desired["beat"] = s
        if not self.running():
            return {"beat_s": s, "applies": "at the next start"}
        out = {"hand_back": self._hand_back()}
        out.update(self._start())
        return {"beat_s": s, **out}

    def _factory(self, who, body):
        """Restore factory profile: the released configuration reapplied, every knob back (autopilot, the max, every muscle driven,
        the command's own beat); like every press it passes through native. Return to native is the other control (reset)."""
        factory = {"mode": "autopilot", "dial": "max", "native": [], "beat": None}
        if {k: self.desired.get(k) for k in factory} == factory and self.running():
            return {"profile": "factory", "unchanged": True}
        out = {"hand_back": self._hand_back()}
        self.desired.update(factory)
        out.update(self._start())
        return {"profile": "factory", "mode": "autopilot", "dial": "max", "native": [], "beat_s": self.beat(), **out}

    def _reset(self, who, body):
        out = self._hand_back()
        self.desired["mode"] = "off"
        return {"reset": out, "mode": "off"}

    def _kill(self, who, body):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = omni_switch.main(["off", "--reason", f"{body['reason']} ({who['name']}, control panel)", "--wait", "60"])
        if self.proc is not None:
            with contextlib.suppress(subprocess.TimeoutExpired):
                self.proc.wait(5)
        self.desired["mode"] = "off"
        self.arms.clear()
        return {"master_switch": "OFF", "all_handed_back": rc == 0, "report": buf.getvalue().splitlines()}

    def _arm(self, who, body):
        if not master.is_off():
            return {"master_switch": "ON", "unchanged": True}
        now = time.time()
        self.arms = {k: t for k, t in self.arms.items() if now - t <= ARM_WINDOW_S}
        self.arms[who["name"]] = now
        if len(self.arms) < 2:
            return 202, {"master_switch": "OFF", "armed_by": sorted(self.arms),
                         "waiting": f"a second holder of the security role, within {ARM_WINDOW_S / 60:.0f} minutes"}
        names = sorted(self.arms)
        with contextlib.redirect_stdout(io.StringIO()):
            omni_switch.main(["on"])
        self.arms.clear()
        return {"master_switch": "ON", "armed_by": names, "next": "governors may be started (POST /v1/mode)"}

    # the reads
    def status(self):
        now = time.time()
        recs = master.records()
        gov = {"running": self.running(), "pid": self.proc.pid if self.proc else None,
               "exit": None if self.proc is None else self.proc.poll(), "args": self.args()}
        if self.proc is not None and not self.running() and self.desired["mode"] != "off":
            gov["note"] = "exited on its own: not restarted by the panel; its lease hands back what it wrote"
        return {"notice": PLAIN, "master_switch": "OFF" if master.is_off() else "ON", "master_reason": master.reason(),
                "desired": dict(self.desired), "beat_s": self.beat(), "governor": gov,
                "registered": [{"name": r.get("name"), "pid": r.get("pid"), "lease_age_s": round(now - r.get("lease", 0), 1)}
                               for r in recs],
                "orphans": len(master.orphans(now)), "last_decision_age_s": self.last_decision_age(now),
                "arm_pending": sorted(self.arms)}

    def last_decision_age(self, now):
        if not self.audit:
            return None
        try:
            with open(self.audit, "rb") as f:
                f.seek(0, 2); f.seek(max(0, f.tell() - 65536))
                tail = f.read().decode("utf-8", "replace").splitlines()
        except OSError:
            return None
        for ln in reversed(tail):
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            if isinstance(r, dict) and "decision" in r and isinstance(r.get("time"), (int, float)):
                return round(now - r["time"], 1)
        return None

    def presses(self, n=100):
        if not self.log_path or not Path(self.log_path).exists():
            return []
        return [json.loads(x) for x in Path(self.log_path).read_text(encoding="utf-8").splitlines()[-n:] if x.strip()]

    def metrics(self):
        L = [f"# {PLAIN}", "# HELP omni_control_presses_total Button presses on the control panel, by button and outcome.",
             "# TYPE omni_control_presses_total counter"]
        L += [f'omni_control_presses_total{{button="{b}",outcome="{o}"}} {n}' for (b, o), n in sorted(self.counts.items())]
        L += ["# HELP omni_control_mode 1 for the mode the panel holds.", "# TYPE omni_control_mode gauge"]
        L += [f'omni_control_mode{{mode="{m}"}} {int(self.desired["mode"] == m)}' for m in MODES]
        L += ["# HELP omni_control_governor_up 1 while the governor the panel started is running.",
              "# TYPE omni_control_governor_up gauge", f"omni_control_governor_up {int(self.running())}",
              "# HELP omni_control_master_switch_on 1 while the master switch is ON.",
              "# TYPE omni_control_master_switch_on gauge", f"omni_control_master_switch_on {int(not master.is_off())}",
              "# HELP omni_control_beat_seconds The heartbeat the panel starts the governor at, seconds (the dial; omni-v17).",
              "# TYPE omni_control_beat_seconds gauge", f"omni_control_beat_seconds {self.beat():g}",
              "# HELP omni_control_orphans Governors that died or hung without handing back (the watchdog's work).",
              "# TYPE omni_control_orphans gauge", f"omni_control_orphans {len(master.orphans())}"]
        return "\n".join(L) + "\n"

    def _log(self, rec):
        if not self.log_path:
            return
        Path(self.log_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")

    def _save(self):
        if not self.state_path:
            return
        Path(self.state_path).parent.mkdir(parents=True, exist_ok=True)
        Path(self.state_path).write_text(json.dumps(self.desired, sort_keys=True) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------------------------------------- the API
def openapi():
    body = {"type": "object", "properties": {"reason": {"type": "string", "maxLength": 500}}}
    def post(summary, role, extra=None):
        props = {**body["properties"], **(extra or {})}
        return {"post": {"summary": summary, "x-role": role, "security": [{"bearer": []}],
                         "requestBody": {"required": True, "content": {"application/json": {"schema": {"type": "object", "properties": props}}}},
                         "responses": {"200": {"description": "done"}, "202": {"description": "recorded, waiting for a second press"},
                                       "400": {"description": "bad request"}, "401": {"description": "no valid token"},
                                       "403": {"description": "the role is not held"}, "409": {"description": "refused by the master switch"}}}}
    get = lambda s: {"get": {"summary": s, "x-role": "viewer", "security": [{"bearer": []}], "responses": {"200": {"description": "ok"}}}}
    return {"openapi": "3.0.3",
            "info": {"title": "Omni-Compass control panel", "version": "1", "description": PLAIN},
            "components": {"securitySchemes": {"bearer": {"type": "http", "scheme": "bearer"}}},
            "paths": {"/v1/status": get("The switch, the desired and actual state, the governor's process, the registry"),
                      "/v1/presses": get("The last presses of every button, refused ones included"),
                      "/metrics": get("The panel's own counters (Prometheus text format)"),
                      "/v1/mode": post("autopilot, watch (decides, writes nothing) or off (hands back and stops)", "operator",
                                       {"mode": {"type": "string", "enum": list(MODES)}}),
                      "/v1/dial": post("the max or the tune-down", "operator", {"dial": {"type": "string", "enum": list(DIALS)}}),
                      "/v1/reset": post("Return to native: every setting handed back to native; the governor stops", "operator"),
                      "/v1/factory": post("Restore factory profile: autopilot, the max, every muscle driven, the command's own beat", "operator"),
                      "/v1/kill": post("the master switch OFF for every governor on the machine (security)", "security"),
                      "/v1/arm": post("the master switch ON again: two holders of the security role within ten minutes", "security"),
                      "/v1/muscle": post("one muscle on (Omni-Compass drives it) or left native (never written); passes through native",
                                         "operator", {"muscle": {"type": "string", "enum": list(MUSCLES)}, "on": {"type": "boolean"}}),
                      "/v1/beat": post("the heartbeat: seconds between the governor's full decisions, 5 to 120 (the main engine 60); "
                                       "passes through native", "operator",
                                       {"seconds": {"type": "number", "minimum": BEAT_RANGE[0], "maximum": BEAT_RANGE[1]}})}}


MUSCLE_ROWS = "".join(f'<div><small>{m}: {d}</small><br><button onclick="go(\'muscle\',{{muscle:\'{m}\',on:true}})">On</button>'
                      f'<button onclick="go(\'muscle\',{{muscle:\'{m}\',on:false}})">Native</button></div>' for m, d in MUSCLES.items())
BEAT_ROWS = "".join(f'<button onclick="go(\'beat\',{{seconds:{b}}})">{b} s{" (main)" if b == MAIN_BEAT else ""}</button>'
                    for b in BEAT_STOPS)
CONSOLE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Omni-Compass control</title><style>
:root{--bg:#fff;--fg:#111;--muted:#555;--line:#ccc;--kill:#b00020}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#eee;--muted:#aaa;--line:#444;--kill:#ff5c6c}}
body{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif;margin:0 auto;max-width:860px;padding:16px}
small{color:var(--muted)}button{font:inherit;padding:8px 14px;margin:4px 4px 4px 0;border:1px solid var(--line);border-radius:6px;background:transparent;color:inherit;cursor:pointer}
button.kill{border-color:var(--kill);color:var(--kill)}input{font:inherit;padding:6px;width:100%;box-sizing:border-box;margin:4px 0;border:1px solid var(--line);background:transparent;color:inherit}
pre{white-space:pre-wrap;border:1px solid var(--line);padding:8px;overflow-x:auto}fieldset{border:1px solid var(--line);margin:12px 0}
</style></head><body><p><small>NOTICE_TEXT</small></p><h1>Omni-Compass control</h1>
<label>Bearer token<input id="t" type="password" autocomplete="off"></label><label>Reason (written to the control log)<input id="r"></label>
<fieldset><legend>Mode</legend><button onclick="go('mode',{mode:'autopilot'})">Autopilot</button><button onclick="go('mode',{mode:'watch'})">Watch (writes nothing)</button><button onclick="go('mode',{mode:'off'})">Off (hand back)</button></fieldset>
<fieldset><legend>Dial</legend><button onclick="go('dial',{dial:'max'})">Max</button><button onclick="go('dial',{dial:'save'})">Tune-down</button></fieldset>
<fieldset><legend>Heartbeat: seconds between full decisions (the main engine 60)</legend>BEAT_ROWS</fieldset>
<fieldset><legend>The two restoring controls</legend><button onclick="go('factory',{})">Restore factory profile</button><button onclick="go('reset',{})">Return to native: every setting back to native</button></fieldset>
<fieldset><legend>Muscles: on, or left native</legend>MUSCLE_ROWS</fieldset>
<fieldset><legend>Security</legend><button class="kill" onclick="if(confirm('Master switch OFF for every governor on this machine?'))go('kill',{})">Kill switch</button><button onclick="go('arm',{})">Arm (two holders)</button></fieldset>
<button onclick="look()">Refresh status</button><pre id="o"></pre><p><small>NOTICE_TEXT</small></p>
<script>
const h=()=>({'Authorization':'Bearer '+document.getElementById('t').value,'Content-Type':'application/json'});
async function go(b,body){body.reason=document.getElementById('r').value;const r=await fetch('/v1/'+b,{method:'POST',headers:h(),body:JSON.stringify(body)});show(r.status,await r.json());}
async function look(){const r=await fetch('/v1/status',{headers:h()});show(r.status,await r.json());}
function show(s,j){document.getElementById('o').textContent=s+'\\n'+JSON.stringify(j,null,1);}
</script></body></html>"""


def server(panel: Panel, tokens_path: Path, bind: str, port: int, cert=None, key=None, allow_origins=()) -> ThreadingHTTPServer:
    allowed = {o.rstrip("/") for o in allow_origins if o}

    class H(BaseHTTPRequestHandler):
        def _origin(self):
            """The page that called, where the operator named it (--allow-origin): the live engine page served from its own
            address may then read the status and press the buttons, each call still carrying its bearer token; any other
            origin gets no cross-origin header and its browser refuses the answer."""
            o = (self.headers.get("Origin") or "").rstrip("/")
            return o if o and o in allowed else None

        def _cors(self):
            o = self._origin()
            if o:
                self.send_header("Access-Control-Allow-Origin", o)
                self.send_header("Vary", "Origin")

        def do_OPTIONS(self):
            """The browser's preflight before a cross-origin call with a token: answered only for an origin the operator named."""
            if not self._origin():
                return self._send(403, {"error": "this origin is not allowed (serve --allow-origin)"})
            self.send_response(204)
            self._cors()
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
            self.send_header("Access-Control-Max-Age", "600")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def _send(self, code, obj, ctype="application/json"):
            data = (obj if isinstance(obj, str) else json.dumps(obj, indent=1)).encode()
            self.send_response(code)
            self._cors()
            self.send_header("Content-Type", ctype + "; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(data)

        def _who(self):
            auth = self.headers.get("Authorization", "")
            if not auth.startswith("Bearer "):
                return None
            rec = load_tokens(tokens_path).get(digest(auth[7:].strip()))
            return None if rec is None else {"name": rec["name"], "roles": set(rec.get("roles", [])) | {"viewer"}}

        def do_GET(self):
            path = self.path.split("?", 1)[0]
            if path == "/":
                return self._send(200, CONSOLE.replace("NOTICE_TEXT", PLAIN).replace("MUSCLE_ROWS", MUSCLE_ROWS)
                                  .replace("BEAT_ROWS", BEAT_ROWS), "text/html")
            if path == "/v1/openapi.json":
                return self._send(200, openapi())
            if path not in ("/v1/status", "/v1/presses", "/metrics"):
                return self._send(404, {"error": "no such path"})
            if self._who() is None:
                return self._send(401, {"error": "a valid bearer token is required"})
            if path == "/metrics":
                return self._send(200, panel.metrics(), "text/plain; version=0.0.4")
            return self._send(200, panel.status() if path == "/v1/status" else {"notice": PLAIN, "presses": panel.presses()})

        def do_POST(self):
            path = self.path.split("?", 1)[0]
            button = path[len("/v1/"):] if path.startswith("/v1/") else ""
            if button not in BUTTONS:
                return self._send(404, {"error": "no such button"})
            who = self._who()
            if who is None:
                return self._send(401, {"error": "a valid bearer token is required"})
            n = int(self.headers.get("Content-Length") or 0)
            if n > MAX_BODY:
                return self._send(413, {"error": "body too large"})
            try:
                body = json.loads(self.rfile.read(n) or b"{}")
                if not isinstance(body, dict):
                    raise ValueError
            except ValueError:
                return self._send(400, {"error": "the body must be a JSON object"})
            code, out = panel.press(who, button, body)
            self._send(code, out)

        def log_message(self, *a):
            pass

    loopback = bind in ("127.0.0.1", "::1", "localhost")
    if not loopback and not (cert and key):
        raise SystemExit(f"refused: a bind beyond the loopback ({bind}) needs --cert and --key (HTTPS)")
    srv = ThreadingHTTPServer((bind, port), H)
    if cert and key:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        ctx.load_cert_chain(cert, key)
        srv.socket = ctx.wrap_socket(srv.socket, server_side=True)
    return srv


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["serve", "token"])
    ap.add_argument("--tokens", type=Path, default=Path(os.environ.get("OMNI_CONTROL_TOKENS", "/etc/omni/tokens.json")))
    ap.add_argument("--name"); ap.add_argument("--roles", default="viewer")
    ap.add_argument("--governor", help="the governor's command line, without its kill file, dial or dry-run flags")
    ap.add_argument("--kill-file", default=os.environ.get("OMNI_CONTROL_KILL_FILE", "/tmp/omni-compass/panel.kill"))
    ap.add_argument("--kill-flag", default="--kill-file"); ap.add_argument("--dial-flag", default="--dial")
    ap.add_argument("--watch-flag", default="--dry-run", help="the governor's flag for deciding without writing")
    ap.add_argument("--handback", type=float, default=120.0, help="seconds to wait for the governor to hand back and exit")
    ap.add_argument("--audit", help="the governor's audit, for the age of its last decision")
    ap.add_argument("--state"); ap.add_argument("--log", default="omni_control.jsonl")
    ap.add_argument("--bind", default=os.environ.get("OMNI_CONTROL_BIND", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("OMNI_CONTROL_PORT", "9465")))
    ap.add_argument("--cert"); ap.add_argument("--key")
    ap.add_argument("--allow-origin", action="append", default=[o for o in os.environ.get("OMNI_CONTROL_ALLOW_ORIGIN", "").split(",") if o],
                    help="a page allowed to call the panel from another address (the live engine page's origin, e.g. "
                         "https://the-omni-compass-llc.github.io); repeat for more; none by default")
    a = ap.parse_args(argv)
    if a.cmd == "token":
        if not a.name:
            raise SystemExit("--name is required")
        tok = make_token(a.tokens, a.name, [r for r in a.roles.split(",") if r])
        print(f"{PLAIN}\ntoken for {a.name} (shown once; only its SHA-256 is kept in {a.tokens}):\n{tok}")
        return 0
    if not a.governor:
        raise SystemExit("--governor is required")
    panel = Panel(shlex.split(a.governor), a.kill_file, a.state, a.log, a.audit,
                  {"kill": a.kill_flag, "dial": a.dial_flag, "watch": a.watch_flag}, a.handback)
    srv = server(panel, a.tokens, a.bind, a.port, a.cert, a.key, a.allow_origin)
    scheme = "https" if a.cert else "http"
    print(f"{PLAIN}\nomni control panel: {scheme}://{a.bind}:{a.port}/ (mode off until a press starts the governor)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        with panel.lock:
            panel._hand_back()
        srv.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
