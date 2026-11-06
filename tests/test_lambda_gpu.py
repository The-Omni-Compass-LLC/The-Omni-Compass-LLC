# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Lambda launcher (scripts/lambda_gpu.py) against a stand-in for Lambda's API on this machine: it prices before it
rents, refuses over the cost ceiling or with no machine free, rents in a region with a machine free, waits until the
machine runs, lists our machines with their age, gives them back, and never prints the key. Nothing leaves this machine.
"""
import contextlib
import io
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

KEY = "secret-key-never-printed-123"
STATE = {"instances": {}, "polls": 0, "capacity": True, "auth_ok": True, "seen": [], "ignore_terminate": False}
PUBLIC = "ssh-ed25519 AAAAPUBLICHALF"


class StandinLambda(BaseHTTPRequestHandler):
    def log_message(self, *a):                       # quiet
        pass

    def moved(self):
        """/old308/... and /old301/... answer as a moved address does, to the same path under /api/v1 on this host;
        /away/... points at a host that is not Lambda's."""
        for prefix, code, to in (("/old308", 308, ""), ("/old301", 301, ""), ("/away", 301, "http://example.invalid")):
            if self.path.startswith(prefix + "/"):
                self.rfile.read(int(self.headers.get("Content-Length", 0)))
                self.send_response(code)
                self.send_header("Location", to + self.path[len(prefix):])
                self.send_header("Content-Length", "0")
                self.end_headers()
                return True
        STATE["seen"].append((self.command, self.path))
        return False

    def reply(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def authed(self):
        if self.headers.get("Authorization") != f"Bearer {KEY}":
            self.reply(401, {"error": {"code": "global/invalid-api-key", "message": "bad key"}})
            return False
        return True

    def do_GET(self):
        if self.moved() or not self.authed():
            return
        if self.path == "/api/v1/ssh-keys":
            self.reply(200, {"data": [{"id": "k1", "name": "omni-key", "public_key": PUBLIC + " made-on-a-laptop"}]
                             + STATE.setdefault("added", [])})
            return
        if self.path == "/api/v1/instance-types":
            regions = [{"name": "us-east-1", "description": "Virginia"}] if STATE["capacity"] else []
            self.reply(200, {"data": {
                "gpu_8x_a100_80gb_sxm4": {"instance_type": {"name": "gpu_8x_a100_80gb_sxm4", "price_cents_per_hour": 1432},
                                          "regions_with_capacity_available": regions},
                "gpu_1x_a10": {"instance_type": {"name": "gpu_1x_a10", "price_cents_per_hour": 75},
                               "regions_with_capacity_available": regions}}})
        elif self.path == "/api/v1/instances":
            self.reply(200, {"data": list(STATE["instances"].values())})
        elif self.path.startswith("/api/v1/instances/"):
            i = self.path.rsplit("/", 1)[1]
            d = STATE["instances"].get(i)
            if d is None:
                self.reply(404, {"error": {"code": "global/object-does-not-exist", "message": "no such instance"}})
                return
            STATE["polls"] += 1
            if STATE["polls"] >= 2 and d["status"] == "booting":
                d.update(status="active", ip="203.0.113.7")
            self.reply(200, {"data": d})
        else:
            self.reply(404, {"error": {"code": "not-found", "message": self.path}})

    def do_DELETE(self):
        if self.moved() or not self.authed():
            return
        i = self.path.rsplit("/", 1)[1]
        STATE["added"] = [k for k in STATE.setdefault("added", []) if k["id"] != i]
        self.reply(200, {"data": {}})

    def do_POST(self):
        if self.moved() or not self.authed():
            return
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if self.path == "/api/v1/ssh-keys":                 # a run's own key, registered by its public half
            k = {"id": f"k{len(STATE.setdefault('added', [])) + 2}", "name": body["name"], "public_key": body["public_key"]}
            STATE["added"].append(k)
            self.reply(200, {"data": k})
            return
        if self.path == "/api/v1/instance-operations/launch":
            assert body["ssh_key_names"] == ["omni-key"] and body["quantity"] == 1
            i = f"inst{len(STATE['instances']) + 1}"
            STATE["instances"][i] = {"id": i, "name": body["name"], "status": "booting", "ip": None,
                                     "region": {"name": body["region_name"]}}
            self.reply(200, {"data": {"instance_ids": [i]}})
        elif self.path == "/api/v1/instance-operations/terminate":
            gone = []
            for i in body["instance_ids"]:
                if i in STATE["instances"] and not STATE["ignore_terminate"]:
                    STATE["instances"][i]["status"] = "terminated"
                    gone.append({"id": i})
            self.reply(200, {"data": {"terminated_instances": gone}})
        else:
            self.reply(404, {"error": {"code": "not-found", "message": self.path}})


def run(argv):
    import lambda_gpu
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        try:
            rc = lambda_gpu.main(argv)
        except SystemExit as e:
            rc = e.code
    return rc, out.getvalue()


def test_lambda_launcher_end_to_end():
    srv = HTTPServer(("127.0.0.1", 0), StandinLambda)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    os.environ["LAMBDA_API"] = f"http://127.0.0.1:{srv.server_address[1]}/api/v1"
    for v in ("NO_PROXY", "no_proxy"):                # the stand-in is on this machine: never through a proxy
        os.environ[v] = ",".join(x for x in (os.environ.get(v, ""), "127.0.0.1", "localhost") if x)
    os.environ["LAMBDA_API_KEY"] = KEY
    import importlib
    import lambda_gpu
    importlib.reload(lambda_gpu)                     # pick up LAMBDA_API
    try:
        printed = ""
        rc, o = run(["plan", "--type", "gpu_8x_a100_80gb_sxm4", "--hours", "11.5", "--max-cost", "400"]); printed += o
        assert rc == 0 and "$14.32 an hour" in o and "us-east-1" in o and "$164.68" in o, o
        rc, o = run(["plan", "--type", "gpu_8x_a100_80gb_sxm4", "--hours", "27", "--max-cost", "300"]); printed += o
        assert rc == 6 and "nothing rented" in o, o                                   # over the ceiling
        rc, o = run(["plan", "--type", "gpu_9x_imaginary", "--hours", "1"]); printed += o
        assert rc == 4, o                                                             # unknown type
        STATE["capacity"] = False
        rc, o = run(["plan", "--type", "gpu_1x_a10", "--hours", "9"]); printed += o
        assert rc == 3 and "nowhere" in o, o                                          # no machine free
        rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", "omni-1card-1-8", "--ssh-key-name", "omni-key"])
        printed += o
        assert rc == 3 and not STATE["instances"], o                                  # never rents blind
        STATE["capacity"] = True
        name = f"omni-8card-{int(time.time()) - 7200}-10"
        rc, o = run(["launch", "--type", "gpu_8x_a100_80gb_sxm4", "--name", name, "--ssh-key-name", "omni-key"])
        printed += o
        assert rc == 0 and o.strip() == "inst1" and STATE["instances"]["inst1"]["region"]["name"] == "us-east-1", o
        rc, o = run(["wait", "inst1", "--timeout", "10", "--every", "0.01"]); printed += o
        assert rc == 0 and o.strip() == "203.0.113.7", o                              # booting, then running
        rc, o = run(["list"]); printed += o
        assert rc == 0 and "inst1" in o and " 2.00h" in o, o                          # its age, from its name
        rc, o = run(["terminate", "inst1"]); printed += o
        assert rc == 0 and "inst1" in o and STATE["instances"]["inst1"]["status"] == "terminated", o
        rc, o = run(["wait", "inst1", "--timeout", "1", "--every", "0.01"]); printed += o
        assert rc == 5, o                                                             # a given-back machine never runs
        rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", f"omni-1card-{int(time.time())}-9",
                     "--ssh-key-name", "omni-key"]); printed += o
        stuck = o.strip()
        STATE["instances"]["hand"] = {"id": "hand", "name": "my-a100", "status": "active", "ip": None,
                                      "region": {"name": "us-east-1"}}            # one launched by hand on Lambda's page
        rc, o = run(["terminate", "--prefix", "my-"]); printed += o
        assert rc == 2 and STATE["instances"]["hand"]["status"] == "active", o        # only names this workflow gives
        rc, o = run(["terminate", "--prefix", "omni-1card-"]); printed += o
        assert rc == 0 and STATE["instances"][stuck]["status"] == "terminated", o     # a stuck run's card, by its name
        assert STATE["instances"]["hand"]["status"] == "active", o                    # the hand-launched one untouched
        rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", f"omni-1card-{int(time.time())}-9-r4242",
                     "--ssh-key-name", "omni-key"]); printed += o
        cut = o.strip()
        rc, o = run(["terminate", "--run", "424"]); printed += o
        assert rc == 0 and STATE["instances"][cut]["status"] != "terminated", o     # another run's number never matches
        rc, o = run(["terminate", "--run", "4242"]); printed += o
        assert rc == 0 and STATE["instances"][cut]["status"] == "terminated", o     # a launch cut off: found by its run
        assert STATE["instances"]["hand"]["status"] == "active", o
        rc, o = run(["list"]); printed += o
        assert rc == 0 and " 0.00h" in o, o                                           # its age still read from its name
        del STATE["instances"]["hand"]
        os.environ["LAMBDA_API_KEY"] = "wrong"
        rc, o = run(["list"]); printed += o
        assert rc == 2 and "HTTP 401" in o, o                                         # a refused key is reported
        assert KEY not in printed and "wrong" not in printed, "the key must never be printed"
    finally:
        os.environ["LAMBDA_API_KEY"] = KEY
        srv.shutdown()


def use(base: str):
    """Point the launcher at an address of the stand-in (LAMBDA_API is read when the module loads)."""
    import importlib
    import lambda_gpu
    os.environ["LAMBDA_API"] = base
    importlib.reload(lambda_gpu)


def test_moved_address_given_back_confirmed_and_key_pair(tmp_path):
    """A moved address keeps a launch and a give-back what they are (urllib alone resends a POST as a GET without its
    body, so the machine would stay rented and the give-back would look done); a move to a host that is not Lambda's is
    refused; a give-back Lambda does not confirm is exit 2 with the id; the SSH pair is checked before anything is rented."""
    srv = HTTPServer(("127.0.0.1", 0), StandinLambda)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    here = f"http://127.0.0.1:{srv.server_address[1]}"
    for v in ("NO_PROXY", "no_proxy"):
        os.environ[v] = ",".join(x for x in (os.environ.get(v, ""), "127.0.0.1", "localhost") if x)
    os.environ["LAMBDA_API_KEY"] = KEY
    STATE.update(instances={}, polls=0, capacity=True, seen=[], ignore_terminate=False)
    try:
        printed = ""
        for prefix in ("/old308", "/old301"):
            use(f"{here}{prefix}/api/v1")
            STATE["seen"].clear()
            rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", f"omni-1card-{int(time.time())}-8",
                         "--ssh-key-name", "omni-key"]); printed += o
            i = o.strip()
            assert rc == 0 and i in STATE["instances"], o
            assert ("POST", "/api/v1/instance-operations/launch") in STATE["seen"], STATE["seen"]   # still a POST
            rc, o = run(["terminate", i]); printed += o
            assert rc == 0 and STATE["instances"][i]["status"] == "terminated", o
            assert ("POST", "/api/v1/instance-operations/terminate") in STATE["seen"], STATE["seen"]
        use(f"{here}/away/api/v1")
        rc, o = run(["list"]); printed += o
        assert rc == 2 and "not Lambda's" in o and "example.invalid" in o, o              # the key never leaves

        use(f"{here}/api/v1")
        STATE["ignore_terminate"] = True
        rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", "omni-1card-2-8", "--ssh-key-name", "omni-key"])
        i = o.strip(); STATE["instances"][i]["status"] = "active"
        rc, o = run(["terminate", i]); printed += o
        assert rc == 2 and "NOT confirmed" in o and i in o and "still billing" in o, o   # never a quiet success
        STATE["ignore_terminate"] = False
        rc, o = run(["terminate", "--name", "omni-1card-2-8"]); printed += o
        assert rc == 0 and STATE["instances"][i]["status"] == "terminated", o          # found by its name
        rc, o = run(["terminate", i, "no-such-machine"]); printed += o
        assert rc == 0 and o.count("already given back") == 2, o                       # asking twice is fine
        rc, o = run(["terminate", "--name", "omni-never-rented"]); printed += o
        assert rc == 0 and "nothing to give back" in o, o
        rc, o = run(["status", "no-such-machine"]); printed += o
        assert rc == 0 and o.split()[2] == "terminated", o                            # the watch reads field 3

        standin = tmp_path / "bin"; standin.mkdir()                 # ssh-keygen -y: the public half of a private key file
        (standin / "ssh-keygen").write_text("#!/bin/sh\nf=''; while [ $# -gt 0 ]; do [ \"$1\" = -f ] && f=\"$2\"; shift; done\n"
                                         f"grep -q GOOD-PRIVATE \"$f\" && {{ echo '{PUBLIC} omni'; exit 0; }}\n"
                                         "grep -q OTHER-PRIVATE \"$f\" && { echo 'ssh-ed25519 AAAAOTHER omni'; exit 0; }\n"
                                         "echo 'Load key: invalid format' >&2; exit 1\n")
        (standin / "ssh-keygen").chmod(0o755)
        os.environ["PATH"] = f"{standin}{os.pathsep}{os.environ['PATH']}"
        keys = {}
        for k, body in (("good", "GOOD-PRIVATE"), ("other", "OTHER-PRIVATE"), ("cut", "-----BEGIN OPENSSH"),
                        ("public", "ssh-ed25519 AAAAPUBLICHALF omni"),
                        ("oneline", "-----BEGIN OPENSSH PRIVATE KEY----- GOOD-PRIVATE -----END OPENSSH PRIVATE KEY-----")):
            keys[k] = tmp_path / k; keys[k].write_text(body + "\n"); keys[k].chmod(0o600)
        rc, o = run(["keycheck", "--name", "omni-key", "--private-file", str(keys["good"])]); printed += o
        assert rc == 0 and "its other half" in o, o
        out = tmp_path / "resolved"
        rc, o = run(["keycheck", "--name", "omni-key.pem", "--private-file", str(keys["good"]), "--resolved-out", str(out)]); printed += o
        assert rc == 0 and "found by its own half" in o and out.read_text().strip() == "omni-key", o   # Lambda's name is used
        rc, o = run(["keycheck", "--name", "omni-kye", "--private-file", str(keys["other"])]); printed += o
        assert rc == 7 and "no SSH key by that name" in o and "omni-key" in o and "none of Lambda's keys" in o, o
        rc, o = run(["keycheck", "--name", "omni-key", "--private-file", str(keys["other"])]); printed += o
        assert rc == 7 and "not the private half" in o, o
        rc, o = run(["keycheck", "--name", "omni-key", "--private-file", str(keys["cut"])]); printed += o
        assert rc == 7 and "not a whole private key" in o and "cut short" in o, o
        rc, o = run(["keycheck", "--name", "omni-key", "--private-file", str(keys["public"])]); printed += o
        assert rc == 7 and "holds a public key" in o, o                                # named, never shown
        rc, o = run(["keycheck", "--name", "omni-key", "--private-file", str(keys["oneline"])]); printed += o
        assert rc == 0 and "its other half" in o, o                                    # line breaks lost on the way in: repaired
        assert keys["oneline"].read_text().splitlines()[1] == "GOOD-PRIVATE" and (keys["oneline"].stat().st_mode & 0o777) == 0o600
        pub = tmp_path / "own.pub"; pub.write_text("ssh-ed25519 AAAAOWNHALF omni-gh-1\n")      # a run's own key
        rc, o = run(["addkey", "--name", "omni-gh-1", "--public-file", str(pub)]); printed += o
        assert rc == 0 and o.strip() and [k["name"] for k in STATE["added"]] == ["omni-gh-1"], o
        rc, o = run(["delkey", "--name", "omni-gh-1"]); printed += o
        assert rc == 0 and "removed from Lambda" in o and STATE["added"] == [], o              # gone at the run's end
        rc, o = run(["delkey", "--name", "omni-gh-1"]); printed += o
        assert rc == 0 and "nothing to remove" in o, o                                         # asking twice is fine
        assert KEY not in printed and "AAAAPUBLICHALF" not in printed and "PRIVATE" not in printed.replace("LAMBDA_SSH_PRIVATE_KEY", ""), printed
    finally:
        os.environ["PATH"] = os.pathsep.join(p for p in os.environ["PATH"].split(os.pathsep) if not p.startswith(str(tmp_path)))
        srv.shutdown()


if __name__ == "__main__":
    import tempfile
    test_lambda_launcher_end_to_end()
    with tempfile.TemporaryDirectory() as t:
        test_moved_address_given_back_confirmed_and_key_pair(Path(t))
    print("test_lambda_gpu: OK")
