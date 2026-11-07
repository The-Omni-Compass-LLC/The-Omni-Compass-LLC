# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""scripts/cloud_machine.py against stand-ins for Google's and Amazon's command-line tools (no account, no network):
the price and the ceiling, what renting asks each cloud for (the label or tag, the hour budget, the key, Ubuntu, a 100 GB
disk), the state and address read back, a fresh key let in, and giving back (on Amazon the security group and the key pair
too)."""
import json
import os
import stat
import sys
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cloud_machine as CM  # noqa: E402

STANDIN = r'''#!/usr/bin/env python3
import json, os, sys
log = os.environ["STANDIN_LOG"]; state = os.environ["STANDIN_STATE"]
a = sys.argv[1:]
open(log, "a").write(os.path.basename(sys.argv[0]) + " " + " ".join(a) + "\n")
s = json.load(open(state)) if os.path.exists(state) else {}
j = " ".join(a)
def save(): json.dump(s, open(state, "w"))
if os.path.basename(sys.argv[0]) == "gcloud":
    if "instances create" in j: s["gcp"] = "RUNNING"; save(); print("[]")
    elif "instances describe" in j:
        if s.get("gcp"): print(json.dumps({"status": s["gcp"], "networkInterfaces": [{"accessConfigs": [{"natIP": "34.1.2.3"}]}]}))
        else: sys.exit(1)
    elif "instances delete" in j: s.pop("gcp", None); save()
    elif "instances list" in j: print(json.dumps([{"name": "omni-detached-1", "zone": "zones/us-central1-a", "status": "RUNNING", "labels": {"born": "0", "maxh": "39"}}]) if s.get("gcp") else "[]")
else:
    if "ssm get-parameter" in j: print("ami-123")
    elif "create-security-group" in j: print("sg-9")
    elif "run-instances" in j: s["aws"] = "running"; save(); print("i-42")
    elif "describe-instances" in j:
        if s.get("aws"): print(json.dumps({"Reservations": [{"Instances": [{"InstanceId": "i-42", "State": {"Name": s["aws"]}, "PublicIpAddress": "3.4.5.6", "KeyName": "omni-detached-1", "Tags": [{"Key": "omni-sg", "Value": "sg-9"}, {"Key": "omni-detached", "Value": "1"}, {"Key": "born", "Value": "0"}, {"Key": "maxh", "Value": "39"}]}]}]}))
        else: print(json.dumps({"Reservations": []}))
    elif "terminate-instances" in j: s["aws"] = "terminated"; save()
'''


def _setup(tmp):
    for name in ("gcloud", "aws"):
        p = Path(tmp) / name
        p.write_text(STANDIN)
        p.chmod(p.stat().st_mode | stat.S_IEXEC)
    os.environ.update(CLOUD_GCLOUD=str(Path(tmp) / "gcloud"), CLOUD_AWS=str(Path(tmp) / "aws"),
                      STANDIN_LOG=str(Path(tmp) / "calls.log"), STANDIN_STATE=str(Path(tmp) / "state.json"), CLOUD_POLL_S="0")
    (Path(tmp) / "k.pub").write_text("ssh-ed25519 AAAATEST omni\n")
    return Path(tmp) / "calls.log"


def _run(*argv):
    out = StringIO()
    with redirect_stdout(out):
        rc = CM.main(list(argv))
    return rc, out.getvalue().strip()


def test_price_and_ceiling():
    rc, out = _run("plan", "--cloud", "gcp", "--hours", "39")
    assert rc == 0 and "e2-standard-8" in out and "$10.45" in out, out          # 0.268 x 39
    rc, out = _run("plan", "--cloud", "aws", "--hours", "39", "--max-cost", "10")
    assert rc == 6, "over the ceiling: nothing rented"
    rc, _ = _run("plan", "--cloud", "aws", "--type", "no-such.size", "--hours", "1")
    assert rc == 4


def test_google_rent_read_key_give_back():
    with tempfile.TemporaryDirectory() as tmp:
        log = _setup(tmp)
        rc, mid = _run("launch", "--cloud", "gcp", "--name", "omni-detached-1", "--pubkey", str(Path(tmp) / "k.pub"),
                       "--hours", "39")
        assert rc == 0 and mid == "gcp:us-central1-a:omni-detached-1", mid
        calls = log.read_text()
        assert "--labels omni-detached=1,maxh=39" in calls and "ubuntu-2204-lts" in calls and "100GB" in calls
        assert "ssh-keys=omni:ssh-ed25519 AAAATEST omni" in calls
        assert _run("wait", mid)[1] == "34.1.2.3"
        assert _run("status", mid)[1] == f"{mid} running 34.1.2.3"
        assert _run("user", mid)[1] == "omni"
        assert _run("key", mid, "--pubkey", str(Path(tmp) / "k.pub"))[0] == 0 and "add-metadata" in log.read_text()
        assert "up" in _run("list", "--cloud", "gcp")[1]
        rc, out = _run("terminate", mid)
        assert "given back" in out and _run("status", mid)[1].endswith("gone")


def test_amazon_rent_read_key_give_back():
    with tempfile.TemporaryDirectory() as tmp:
        log = _setup(tmp)
        rc, mid = _run("launch", "--cloud", "aws", "--name", "omni-detached-1", "--pubkey", str(Path(tmp) / "k.pub"),
                       "--hours", "39")
        assert rc == 0 and mid == "aws:us-east-1:i-42", mid
        calls = log.read_text()
        for must in ("ssm get-parameter", "import-key-pair", "create-security-group", "--port 22", "run-instances",
                     "Key=omni-detached,Value=1", "Key=maxh,Value=39", "VolumeSize=100", "m6i.2xlarge"):
            assert must in calls, must
        assert _run("wait", mid)[1] == "3.4.5.6"
        assert _run("user", mid)[1] == "ubuntu"
        assert _run("key", mid, "--pubkey", str(Path(tmp) / "k.pub"))[0] == 0 and "send-ssh-public-key" in log.read_text()
        rc, out = _run("terminate", mid)
        calls = log.read_text()
        assert "given back" in out and "delete-security-group --group-id sg-9" in calls and "delete-key-pair" in calls


def main():
    test_price_and_ceiling()
    test_google_rent_read_key_give_back()
    test_amazon_rent_read_key_give_back()
    print("PASS  the rented cloud machine (Google, Amazon): the price and the ceiling first, every machine labelled with its "
          "hour budget, a fresh key per job, and always given back (on Amazon its security group and key pair too)")


if __name__ == "__main__":
    main()
