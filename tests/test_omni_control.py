# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The control panel (tools/omni_control.py): every button behind a token and a role, every press logged, every change
made through the governor's own hand-back, the kill switch for every governor, the two-person arm."""
import json, os, sys, tempfile, textwrap, threading, time, unittest, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.omni_control as C

STANDIN = textwrap.dedent(f"""
    import json, os, sys, time
    sys.path.insert(0, {str(ROOT)!r})
    from omnicompass import master
    args = sys.argv[1:]
    kill = args[args.index("--kill-file") + 1]
    out = os.environ["STANDIN_OUT"]
    with open(out, "a") as f:
        f.write(json.dumps({{"start": args}}) + "\\n")
    while True:
        if os.path.exists(kill) or master.is_off():
            with open(out, "a") as f:
                f.write(json.dumps({{"handed_back": True}}) + "\\n")
            sys.exit(0)
        time.sleep(0.02)
""")


class Panel(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.env = {k: os.environ.get(k) for k in ("OMNI_MASTER_OFF", "OMNI_REGISTRY", "STANDIN_OUT")}
        os.environ["OMNI_MASTER_OFF"] = str(self.d / "switch" / "OFF")
        os.environ["OMNI_REGISTRY"] = str(self.d / "switch" / "running")
        os.environ["STANDIN_OUT"] = str(self.d / "standin.jsonl")
        (self.d / "standin.py").write_text(STANDIN)
        self.tokens = self.d / "tokens.json"
        self.tok = {n: C.make_token(self.tokens, n, r) for n, r in
                    (("vera", ["viewer"]), ("otto", ["operator"]), ("sam", ["security"]), ("sue", ["security"]))}
        self.panel = C.Panel([sys.executable, str(self.d / "standin.py")], self.d / "panel.kill", self.d / "state.json",
                             self.d / "control.jsonl", handback_s=10)
        self.srv = C.server(self.panel, self.tokens, "127.0.0.1", 0)
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.srv.server_address[1]}"

    def tearDown(self):
        with self.panel.lock:
            self.panel._hand_back()
        self.srv.shutdown(); self.srv.server_close()
        for k, v in self.env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def call(self, path, who=None, body=None):
        req = urllib.request.Request(self.url + path, data=None if body is None else json.dumps(body).encode(),
                                     method="GET" if body is None else "POST")
        if who:
            req.add_header("Authorization", "Bearer " + self.tok[who])
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read().decode()
                return r.status, (json.loads(raw) if r.headers.get_content_type() == "application/json" else raw)
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode())

    def starts(self):
        p = Path(os.environ["STANDIN_OUT"])
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []

    def test_reads_need_a_token_and_the_console_and_document_do_not(self):
        self.assertEqual(self.call("/v1/status")[0], 401)
        code, page = self.call("/")
        self.assertEqual(code, 200); self.assertIn("Kill switch", page); self.assertIn("www.omni-compass.com", page)
        code, doc = self.call("/v1/openapi.json")
        self.assertEqual(code, 200)
        self.assertTrue({f"/v1/{b}" for b in C.BUTTONS} <= set(doc["paths"]))
        code, st = self.call("/v1/status", "vera")
        self.assertEqual((code, st["master_switch"], st["desired"]["mode"]), (200, "ON", "off"))

    def test_a_viewer_cannot_press_and_the_refusal_is_logged(self):
        code, out = self.call("/v1/mode", "vera", {"mode": "autopilot"})
        self.assertEqual(code, 403)
        last = self.panel.presses()[-1]
        self.assertEqual((last["who"], last["button"], last["outcome"]), ("vera", "mode", "refused"))
        self.assertEqual(self.starts(), [])

    def test_every_change_goes_through_the_governors_own_hand_back(self):
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "watch"})[0], 200)
        self.assertEqual(self.call("/v1/dial", "otto", {"dial": "save"})[0], 200)
        t0 = time.time()
        while len(self.starts()) < 5 and time.time() - t0 < 10:      # the last start is written once the child is up
            time.sleep(0.05)
        ev = self.starts()
        self.assertEqual([("start" if "start" in e else "back") for e in ev], ["start", "back", "start", "back", "start"])
        first, watch, save = ev[0]["start"], ev[2]["start"], ev[4]["start"]
        self.assertNotIn("--dry-run", first); self.assertEqual(first[first.index("--dial") + 1], "max")
        self.assertIn("--dry-run", watch)
        self.assertEqual(save[save.index("--dial") + 1], "save"); self.assertIn("--dry-run", save)
        self.assertEqual(json.loads((self.d / "state.json").read_text())["dial"], "save")

    def test_a_muscle_is_switched_through_native_and_carried_into_the_governors_arguments(self):
        """omni-v14: POST /v1/muscle leaves one muscle native (never written) or turns it on again, through native."""
        self.assertEqual(self.call("/v1/muscle", "vera", {"muscle": "cpu", "on": False})[0], 403)
        self.assertEqual(self.call("/v1/muscle", "otto", {"muscle": "cpus", "on": False})[0], 400)
        self.assertEqual(self.call("/v1/muscle", "otto", {"muscle": "cpu", "on": "no"})[0], 400)
        code, out = self.call("/v1/muscle", "otto", {"muscle": "cpu", "on": False})
        self.assertEqual((code, out["native"], out["applies"]), (200, ["cpu"], "at the next start"))
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)
        self.assertEqual(self.call("/v1/muscle", "otto", {"muscle": "machines", "on": False})[0], 200)
        t0 = time.time()
        while len(self.starts()) < 3 and time.time() - t0 < 10:
            time.sleep(0.05)
        ev = self.starts()
        self.assertEqual([("start" if "start" in e else "back") for e in ev], ["start", "back", "start"])
        first, second = ev[0]["start"], ev[2]["start"]
        self.assertEqual(first[first.index("--native") + 1], "cpu")
        self.assertEqual(second[second.index("--native") + 1], "cpu,machines")
        self.assertEqual(json.loads((self.d / "state.json").read_text())["native"], ["cpu", "machines"])
        self.assertTrue(self.call("/v1/muscle", "otto", {"muscle": "cpu", "on": False})[1]["unchanged"])
        code, page = self.call("/")
        self.assertIn("muscle:'cooling',on:false", page)

    def test_the_beat_is_set_through_native_and_carried_into_the_governors_arguments(self):
        """omni-v17: POST /v1/beat sets the heartbeat, the governor's full decision every so many seconds (5 to 120; the main
        engine 60), through native like a dial press, and the console offers every stop of the dial."""
        self.assertEqual(self.call("/v1/beat", "vera", {"seconds": 15})[0], 403)
        for bad in (3, 121, "15", True, None):
            self.assertEqual(self.call("/v1/beat", "otto", {"seconds": bad})[0], 400, bad)
        self.assertTrue(self.call("/v1/beat", "otto", {"seconds": 60})[1]["unchanged"])      # the main engine's beat already
        code, out = self.call("/v1/beat", "otto", {"seconds": 15})
        self.assertEqual((code, out["beat_s"], out["applies"]), (200, 15.0, "at the next start"))
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)
        self.assertEqual(self.call("/v1/beat", "otto", {"seconds": 120})[0], 200)
        t0 = time.time()
        while len(self.starts()) < 3 and time.time() - t0 < 10:
            time.sleep(0.05)
        ev = self.starts()
        self.assertEqual([("start" if "start" in e else "back") for e in ev], ["start", "back", "start"])
        first, second = ev[0]["start"], ev[2]["start"]
        self.assertEqual(first[first.index("--interval") + 1], "15")
        self.assertEqual(second[second.index("--interval") + 1], "120")
        self.assertEqual(json.loads((self.d / "state.json").read_text())["beat"], 120.0)
        self.assertTrue(self.call("/v1/beat", "otto", {"seconds": 120})[1]["unchanged"])
        self.assertEqual(self.call("/v1/status", "vera")[1]["beat_s"], 120.0)
        self.assertIn("omni_control_beat_seconds 120", self.call("/metrics", "vera")[1])
        page = self.call("/")[1]
        for b in (10, 15, 20, 30, 60, 90, 120):                 # the seven stops (the founder's orders of 24 and 31 October)
            self.assertIn(f"go('beat',{{seconds:{b}}})", page)
        for b in (5, 75):
            self.assertNotIn(f"go('beat',{{seconds:{b}}})", page)
        self.assertIn("/v1/beat", self.call("/v1/openapi.json")[1]["paths"])

    def test_reset_needs_a_reason_then_hands_back_and_stops(self):
        self.call("/v1/mode", "otto", {"mode": "autopilot"})
        self.assertEqual(self.call("/v1/reset", "otto", {})[0], 400)
        code, out = self.call("/v1/reset", "otto", {"reason": "maintenance window"})
        self.assertEqual((code, out["mode"], out["reset"]["handed_back"]), (200, "off", True))
        self.assertFalse(self.panel.running())

    def test_restore_factory_profile_reapplies_the_released_configuration(self):
        # Restore factory profile and Return to native are two controls (the founder's master specification of 24 October)
        self.call("/v1/mode", "otto", {"mode": "watch"})
        self.call("/v1/dial", "otto", {"dial": "save"})
        self.assertEqual(self.call("/v1/factory", "vera", {})[0], 403)                      # a viewer cannot press it
        code, out = self.call("/v1/factory", "otto", {"reason": "back to the factory profile"})
        self.assertEqual((code, out["profile"], out["mode"], out["dial"], out["native"]), (200, "factory", "autopilot", "max", []))
        self.assertTrue(self.panel.running())
        self.assertTrue(self.call("/v1/factory", "otto", {})[1]["unchanged"])
        page = self.call("/")[1]
        self.assertIn("Restore factory profile", page)
        self.assertIn("Return to native", page)
        self.assertIn("/v1/factory", self.call("/v1/openapi.json")[1]["paths"])

    def test_the_kill_switch_is_security_only_and_holds_until_two_arm_it(self):
        self.call("/v1/mode", "otto", {"mode": "autopilot"})
        self.assertEqual(self.call("/v1/kill", "otto", {"reason": "x"})[0], 403)
        code, out = self.call("/v1/kill", "sam", {"reason": "drill"})
        self.assertEqual((code, out["master_switch"]), (200, "OFF"))
        time.sleep(0.3)
        self.assertFalse(self.panel.running())
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 409)       # nothing starts while OFF
        self.assertEqual(self.call("/v1/arm", "sam", {"reason": "drill over"})[0], 202)
        self.assertEqual(self.call("/v1/arm", "sam", {"reason": "again"})[0], 202)            # the same holder twice is one
        code, out = self.call("/v1/arm", "sue", {"reason": "drill over"})
        self.assertEqual((code, out["master_switch"], out["armed_by"]), (200, "ON", ["sam", "sue"]))
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)

    def test_every_press_is_logged_with_its_holder(self):
        self.call("/v1/mode", "otto", {"mode": "watch", "reason": "trial"})
        self.call("/v1/mode", "otto", {"mode": "bogus"})
        log = self.panel.presses()
        self.assertEqual([(x["who"], x["button"], x["outcome"]) for x in log],
                         [("otto", "mode", "done"), ("otto", "mode", "refused")])
        self.assertEqual(log[0]["reason"], "trial")
        code, page = self.call("/metrics", "vera")
        self.assertIn('omni_control_presses_total{button="mode",outcome="done"} 1', page)
        self.assertIn('omni_control_mode{mode="watch"} 1', page)

    def test_tokens_are_kept_as_digests_only(self):
        stored = self.tokens.read_text()
        for t in self.tok.values():
            self.assertNotIn(t, stored)
        self.assertEqual(oct(self.tokens.stat().st_mode & 0o777), "0o600")

    def test_only_a_named_origin_may_call_across_and_it_still_needs_a_token(self):
        page = "https://the-omni-compass-llc.github.io"
        srv = C.server(self.panel, self.tokens, "127.0.0.1", 0, allow_origins=[page])
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{srv.server_address[1]}"
        try:
            def ask(method, origin, token=None):
                req = urllib.request.Request(url + "/v1/status", method=method)
                req.add_header("Origin", origin)
                if token:
                    req.add_header("Authorization", "Bearer " + token)
                try:
                    with urllib.request.urlopen(req, timeout=30) as r:
                        return r.status, r.headers.get("Access-Control-Allow-Origin"), r.headers.get("Access-Control-Allow-Headers")
                except urllib.error.HTTPError as e:
                    return e.code, e.headers.get("Access-Control-Allow-Origin"), e.headers.get("Access-Control-Allow-Headers")
            self.assertEqual(ask("OPTIONS", page), (204, page, "Authorization, Content-Type"))
            self.assertEqual(ask("OPTIONS", "https://elsewhere.example")[:2], (403, None))
            self.assertEqual(ask("GET", page)[:2], (401, page))                      # the header, and still no data without a token
            self.assertEqual(ask("GET", page, self.tok["vera"])[:2], (200, page))
            self.assertEqual(ask("GET", "https://elsewhere.example", self.tok["vera"])[:2], (200, None))   # its browser refuses it
        finally:
            srv.shutdown(); srv.server_close()

    def test_a_bind_beyond_the_loopback_needs_https(self):
        with self.assertRaises(SystemExit):
            C.server(self.panel, self.tokens, "0.0.0.0", 0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
