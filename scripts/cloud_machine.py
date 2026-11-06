#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Rent one Google Cloud or Amazon machine for one detached Omni-Compass run, and always give it back
(.github/workflows/cloud-organism.yml: the same big-organism test Azure runs in big-organism-detached.yml).

  python3 scripts/cloud_machine.py plan --cloud gcp --type e2-standard-8 --hours 35 [--max-cost 60]
                                                             the list price and the estimate; rents nothing
  python3 scripts/cloud_machine.py launch --cloud gcp --type T --name N --where us-central1-a --pubkey k.pub --hours 35
                                                             rents one; prints its id (cloud:where:name-or-instance)
  python3 scripts/cloud_machine.py wait ID [--timeout 900]   until it is running; prints its public address
  python3 scripts/cloud_machine.py status ID                 its state and address (state "gone" when it no longer exists)
  python3 scripts/cloud_machine.py key ID --pubkey k.pub     lets a fresh key in (each GitHub job makes its own key)
  python3 scripts/cloud_machine.py list --cloud gcp|aws --where W   every machine of ours, with how long it has been up
  python3 scripts/cloud_machine.py terminate ID [ID ...]     gives them back; the bill stops

It drives the clouds' own command-line tools (gcloud, aws), logged in by the workflow from the repository's secrets
(GCP_CREDENTIALS and GCP_PROJECT; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY); no secret ever passes through here or
is printed. CLOUD_GCLOUD and CLOUD_AWS name other binaries (the tests use stand-ins). Every machine carries the label (Google)
or tag (Amazon) omni-detached=1 and the hour budget it was rented for, so anyone listing the account can see it.
The login user on the machine is "omni" on Google and "ubuntu" on Amazon (printed by `user`).
Exit codes: 0 done; 2 a refused request or bad usage; 4 unknown machine type; 5 not running in time; 6 over the cost ceiling.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time

# list prices, on demand, Linux, USD an hour (Google us-central1, Amazon us-east-1; check the price lists on the day)
PRICES = {
    "gcp": {"e2-standard-8": 0.268, "e2-highmem-8": 0.362, "n2-standard-8": 0.389, "n2d-standard-8": 0.338,
            "e2-standard-16": 0.536, "n2-standard-16": 0.777},
    "aws": {"m6i.2xlarge": 0.384, "m5.2xlarge": 0.384, "m6a.2xlarge": 0.3456, "m7i.2xlarge": 0.4032,
            "r6i.2xlarge": 0.504, "m6i.4xlarge": 0.768},
}
DEFAULT = {"gcp": ("e2-standard-8", "us-central1-a"), "aws": ("m6i.2xlarge", "us-east-1")}
USER = {"gcp": "omni", "aws": "ubuntu"}
UBUNTU_SSM = "/aws/service/canonical/ubuntu/server/22.04/stable/current/amd64/hvm/ebs-gp2/ami-id"


def run(argv: list[str], check: bool = True) -> str:
    """One call to the cloud's own tool; its error goes to stderr, never a secret (the tools hold the login)."""
    tool = {"gcloud": os.environ.get("CLOUD_GCLOUD", "gcloud"), "aws": os.environ.get("CLOUD_AWS", "aws")}[argv[0]]
    p = subprocess.run([tool] + argv[1:], capture_output=True, text=True)
    if check and p.returncode != 0:
        print(f"{argv[0]} refused {' '.join(argv[1:4])} ...: {p.stderr.strip()[-400:]}", file=sys.stderr)
        sys.exit(2)
    return p.stdout


def parse_id(mid: str) -> tuple[str, str, str]:
    try:
        cloud, where, name = mid.split(":", 2)
    except ValueError:
        sys.exit(f"not a machine id: {mid} (cloud:where:name)")
    if cloud not in PRICES:
        sys.exit(f"unknown cloud in {mid}")
    return cloud, where, name


def cmd_plan(a) -> int:
    price = PRICES[a.cloud].get(a.type)
    if price is None:
        print(f"unknown machine type {a.type} for {a.cloud}; known: {', '.join(sorted(PRICES[a.cloud]))}", file=sys.stderr)
        return 4
    est = price * a.hours
    print(f"{a.cloud} {a.type}: about ${price:.3f} an hour at list price; {a.hours:g} hours at most: about ${est:.2f}")
    if a.max_cost is not None and est > a.max_cost:
        print(f"over the ceiling of ${a.max_cost:.2f}: nothing rented", file=sys.stderr)
        return 6
    return 0


def _aws_region(where: str) -> str:
    return where[:-1] if where[-1:].isalpha() and where[-2:-1].isdigit() else where   # us-east-1a -> us-east-1


def cmd_launch(a) -> int:
    if a.type not in PRICES[a.cloud]:
        print(f"unknown machine type {a.type} for {a.cloud}", file=sys.stderr)
        return 4
    pub = open(a.pubkey).read().strip()
    if a.cloud == "gcp":
        run(["gcloud", "compute", "instances", "create", a.name, "--zone", a.where, "--machine-type", a.type,
             "--image-family", "ubuntu-2204-lts", "--image-project", "ubuntu-os-cloud", "--boot-disk-size", "100GB",
             "--labels", f"omni-detached=1,maxh={int(a.hours)},born={int(time.time())}",
             "--metadata", f"ssh-keys={USER['gcp']}:{pub}", "--format", "json"])
        print(f"gcp:{a.where}:{a.name}")
        return 0
    region = _aws_region(a.where)
    ami = run(["aws", "ssm", "get-parameter", "--name", UBUNTU_SSM, "--region", region, "--query", "Parameter.Value",
               "--output", "text"]).strip()
    run(["aws", "ec2", "import-key-pair", "--key-name", a.name, "--public-key-material", "fileb://" + a.pubkey,
         "--region", region])
    sg = run(["aws", "ec2", "create-security-group", "--group-name", a.name, "--description",
              "Omni-Compass detached run (ssh only)", "--region", region, "--query", "GroupId", "--output", "text"]).strip()
    run(["aws", "ec2", "authorize-security-group-ingress", "--group-id", sg, "--protocol", "tcp", "--port", "22",
         "--cidr", "0.0.0.0/0", "--region", region])
    tags = (f"ResourceType=instance,Tags=[{{Key=Name,Value={a.name}}},{{Key=omni-detached,Value=1}},"
            f"{{Key=maxh,Value={int(a.hours)}}},{{Key=born,Value={int(time.time())}}},{{Key=omni-sg,Value={sg}}}]")
    iid = run(["aws", "ec2", "run-instances", "--image-id", ami, "--instance-type", a.type, "--key-name", a.name,
               "--security-group-ids", sg, "--region", region, "--count", "1",
               "--block-device-mappings", "DeviceName=/dev/sda1,Ebs={VolumeSize=100,VolumeType=gp3,DeleteOnTermination=true}",
               "--tag-specifications", tags, "--query", "Instances[0].InstanceId", "--output", "text"]).strip()
    print(f"aws:{region}:{iid}")
    return 0


def state(mid: str) -> tuple[str, str]:
    """(state, public address): state is running, starting, stopping or gone."""
    cloud, where, name = parse_id(mid)
    if cloud == "gcp":
        out = run(["gcloud", "compute", "instances", "describe", name, "--zone", where, "--format", "json"], check=False)
        if not out.strip():
            return "gone", ""
        d = json.loads(out)
        st = d.get("status", "")
        ip = ""
        for ni in d.get("networkInterfaces", []):
            for ac in ni.get("accessConfigs", []):
                ip = ac.get("natIP", ip)
        return {"RUNNING": "running", "PROVISIONING": "starting", "STAGING": "starting"}.get(st, "stopping" if st else "gone"), ip
    out = run(["aws", "ec2", "describe-instances", "--instance-ids", name, "--region", where, "--output", "json"], check=False)
    try:
        inst = json.loads(out)["Reservations"][0]["Instances"][0]
    except (ValueError, KeyError, IndexError):
        return "gone", ""
    st = inst.get("State", {}).get("Name", "")
    return ({"running": "running", "pending": "starting"}.get(st, "gone" if st in ("terminated", "shutting-down") else "stopping"),
            inst.get("PublicIpAddress", ""))


def cmd_wait(a) -> int:
    t_end = time.time() + a.timeout
    while time.time() < t_end:
        st, ip = state(a.id)
        if st == "running" and ip:
            print(ip)
            return 0
        if st == "gone":
            print(f"{a.id} is gone", file=sys.stderr)
            return 5
        time.sleep(float(os.environ.get("CLOUD_POLL_S", "15")))
    print(f"{a.id} not running after {a.timeout} s", file=sys.stderr)
    return 5


def cmd_status(a) -> int:
    st, ip = state(a.id)
    print(f"{a.id} {st} {ip}".rstrip())
    return 0


def cmd_user(a) -> int:
    print(USER[parse_id(a.id)[0]])
    return 0


def cmd_key(a) -> int:
    """A fresh key for this job: Google takes it into the machine's metadata; Amazon's Instance Connect lets it in for
    the next 60 seconds of connecting (an open session stays open)."""
    cloud, where, name = parse_id(a.id)
    pub = open(a.pubkey).read().strip()
    if cloud == "gcp":
        run(["gcloud", "compute", "instances", "add-metadata", name, "--zone", where,
             "--metadata", f"ssh-keys={USER['gcp']}:{pub}"])
    else:
        run(["aws", "ec2-instance-connect", "send-ssh-public-key", "--instance-id", name, "--instance-os-user",
             USER["aws"], "--ssh-public-key", "file://" + a.pubkey, "--region", where])
    return 0


def cmd_list(a) -> int:
    now = time.time()
    if a.cloud == "gcp":
        out = run(["gcloud", "compute", "instances", "list", "--filter", "labels.omni-detached=1", "--format", "json"])
        for d in json.loads(out or "[]"):
            zone = d.get("zone", "").rsplit("/", 1)[-1]
            born = float(d.get("labels", {}).get("born", now))
            print(f"gcp:{zone}:{d['name']} {d.get('status', '').lower()} up {(now - born) / 3600:.1f} h "
                  f"of {d.get('labels', {}).get('maxh', '?')}")
        return 0
    region = _aws_region(a.where)
    out = run(["aws", "ec2", "describe-instances", "--region", region, "--filters", "Name=tag:omni-detached,Values=1",
               "Name=instance-state-name,Values=pending,running,stopping,stopped", "--output", "json"])
    for r in json.loads(out or '{"Reservations": []}').get("Reservations", []):
        for i in r.get("Instances", []):
            tags = {t["Key"]: t["Value"] for t in i.get("Tags", [])}
            born = float(tags.get("born", now))
            print(f"aws:{region}:{i['InstanceId']} {i.get('State', {}).get('Name', '')} up {(now - born) / 3600:.1f} h "
                  f"of {tags.get('maxh', '?')}")
    return 0


def cmd_terminate(a) -> int:
    for mid in a.ids:
        cloud, where, name = parse_id(mid)
        if cloud == "gcp":
            run(["gcloud", "compute", "instances", "delete", name, "--zone", where, "--quiet"], check=False)
        else:
            out = run(["aws", "ec2", "describe-instances", "--instance-ids", name, "--region", where, "--output", "json"],
                      check=False)
            tags, key = {}, ""
            try:
                inst = json.loads(out)["Reservations"][0]["Instances"][0]
                tags = {t["Key"]: t["Value"] for t in inst.get("Tags", [])}
                key = inst.get("KeyName", "")
            except (ValueError, KeyError, IndexError):
                pass
            run(["aws", "ec2", "terminate-instances", "--instance-ids", name, "--region", where], check=False)
            run(["aws", "ec2", "wait", "instance-terminated", "--instance-ids", name, "--region", where], check=False)
            if tags.get("omni-sg"):
                run(["aws", "ec2", "delete-security-group", "--group-id", tags["omni-sg"], "--region", where], check=False)
            if key:
                run(["aws", "ec2", "delete-key-pair", "--key-name", key, "--region", where], check=False)
        st, _ = state(mid)
        print(f"{mid} {'given back' if st in ('gone', 'stopping') else 'STILL ' + st}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("plan"); p.add_argument("--cloud", choices=list(PRICES), required=True)
    p.add_argument("--type", default=""); p.add_argument("--hours", type=float, required=True)
    p.add_argument("--max-cost", type=float, default=None)
    p = sp.add_parser("launch"); p.add_argument("--cloud", choices=list(PRICES), required=True)
    p.add_argument("--type", default=""); p.add_argument("--name", required=True); p.add_argument("--where", default="")
    p.add_argument("--pubkey", required=True); p.add_argument("--hours", type=float, required=True)
    p = sp.add_parser("wait"); p.add_argument("id"); p.add_argument("--timeout", type=float, default=900)
    p = sp.add_parser("status"); p.add_argument("id")
    p = sp.add_parser("user"); p.add_argument("id")
    p = sp.add_parser("key"); p.add_argument("id"); p.add_argument("--pubkey", required=True)
    p = sp.add_parser("list"); p.add_argument("--cloud", choices=list(PRICES), required=True); p.add_argument("--where", default="")
    p = sp.add_parser("terminate"); p.add_argument("ids", nargs="+")
    a = ap.parse_args(argv)
    if a.cmd in ("plan", "launch", "list"):
        t, w = DEFAULT[a.cloud]
        if hasattr(a, "type") and not a.type:
            a.type = t
        if hasattr(a, "where") and not a.where:
            a.where = w
    return {"plan": cmd_plan, "launch": cmd_launch, "wait": cmd_wait, "status": cmd_status, "user": cmd_user,
            "key": cmd_key, "list": cmd_list, "terminate": cmd_terminate}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
