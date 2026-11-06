#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Rent one Lambda Cloud GPU machine for one Omni-Compass GPU run, and always give it back
(.github/workflows/lambda-gpu.yml; docs/LAMBDA_SETUP.md, click by click).

  python3 scripts/lambda_gpu.py plan --type gpu_8x_a100_80gb_sxm4 --hours 11.5   the price, the regions with a machine
                                                                                free, the estimate; rents nothing
  python3 scripts/lambda_gpu.py launch --type T --name N --ssh-key-name K [--region R]   rents one; prints its id
  python3 scripts/lambda_gpu.py wait ID [--timeout 1800]    until it is running; prints its address
  python3 scripts/lambda_gpu.py status ID                   its state and address
  python3 scripts/lambda_gpu.py list [--prefix omni-]       our machines, with how long each has been up
  python3 scripts/lambda_gpu.py terminate [ID ...] [--name N] [--prefix omni-...] [--run RUN]   gives them back (by id,
                                                            the machine of that name, every machine whose name starts so
                                                            (only omni- names), or every machine a workflow run rented,
                                                            its name ending -r<run id>) and confirms each one; the bill stops
  python3 scripts/lambda_gpu.py keycheck --name K --private-file F   the SSH key pair, at no cost: Lambda holds a key named
                                                            K, and F is its private half; rents nothing

The key is read from the environment (LAMBDA_API_KEY), never from the command line, and is never printed. LAMBDA_API sets
the address of the API (default https://cloud.lambda.ai/api/v1, Lambda's address since its move from lambdalabs.com). A
moved address is followed here, with the same request, and only to Lambda's own hosts: Python's own redirect turns a POST
into a GET, so a launch or a give-back sent to a moved address would arrive as a read and the machine would stay rented. A
machine is named omni-<test>-<epoch>-<hours>, so anyone listing the account can see when it was rented and the hour budget
it was rented for.
Exit codes: 0 done; 2 usage, a refused request, or a machine not confirmed given back; 3 no machine of that type free
anywhere; 4 unknown type; 5 not running in time; 6 over the cost ceiling; 7 the SSH key pair does not match.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("LAMBDA_API", "https://cloud.lambda.ai/api/v1").rstrip("/")
LAMBDA_HOSTS = ("lambda.ai", "lambdalabs.com")
MOVED = (301, 302, 307, 308)          # the address moved; the request was not carried out (303 is not followed)
GONE = ("terminated", "terminating")


class _Stop(urllib.request.HTTPRedirectHandler):
    """Never follow a redirect behind call()'s back (urllib would resend a POST as a GET, without its body)."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(_Stop)


def lambdas_own(url_from: str, url_to: str) -> bool:
    """A moved address is followed only to the same host or to Lambda's own, and never from https down to http, so the key
    is never sent anywhere else."""
    a, b = urllib.parse.urlsplit(url_from), urllib.parse.urlsplit(url_to)
    host = b.hostname or ""
    if b.scheme != "https" and b.scheme != a.scheme:
        return False
    return host == a.hostname or any(host == h or host.endswith("." + h) for h in LAMBDA_HOSTS)


def call(method: str, path: str, body: dict | None = None, missing_ok: bool = False) -> dict | None:
    """One request to Lambda's API. missing_ok: a 404 (no such machine) returns None instead of stopping."""
    key = os.environ.get("LAMBDA_API_KEY", "")
    if not key:
        sys.exit("LAMBDA_API_KEY is not set (it lives only in the repository's secrets)")
    url = API + path
    data = None if body is None else json.dumps(body).encode()
    for _ in range(4):
        req = urllib.request.Request(url, method=method, data=data,
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                              "Accept": "application/json", "User-Agent": "omni-compass-lambda-gpu"})
        try:
            with OPENER.open(req, timeout=60) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            if e.code in MOVED:
                to = urllib.parse.urljoin(url, e.headers.get("Location") or "")
                if not lambdas_own(url, to):
                    print(f"Lambda's address for {method} {path} moved to {urllib.parse.urlsplit(to).hostname or '?'}, "
                          "which is not Lambda's: refused (the key is never sent there)", file=sys.stderr)
                    sys.exit(2)
                url = to
                continue
            if missing_ok and e.code == 404:
                return None
            try:
                err = json.loads(e.read().decode()).get("error", {})
                msg = f"{err.get('code', '')} {err.get('message', '')} {err.get('suggestion', '')}".strip()
            except Exception:                                    # noqa: BLE001  (the body may not be JSON)
                msg = ""
            print(f"Lambda refused {method} {path}: HTTP {e.code} {msg}", file=sys.stderr)
            sys.exit(2)
        except urllib.error.URLError as e:
            print(f"Lambda unreachable for {method} {path}: {e.reason}", file=sys.stderr)
            sys.exit(2)
    print(f"Lambda's address for {method} {path} moved more than three times: refused", file=sys.stderr)
    sys.exit(2)


def instance_types() -> dict:
    return call("GET", "/instance-types").get("data", {})


def plan(a) -> int:
    types = instance_types()
    if a.type not in types:
        print(f"unknown instance type {a.type}; offered: {', '.join(sorted(types))}")
        return 4
    t = types[a.type]
    cents = t.get("instance_type", {}).get("price_cents_per_hour", 0)
    regions = [r["name"] for r in t.get("regions_with_capacity_available", [])]
    est = cents / 100.0 * a.hours
    print(f"type {a.type}: ${cents / 100.0:.2f} an hour; free now in: {', '.join(regions) or 'nowhere'}")
    print(f"estimate for {a.hours:g} hours: ${est:.2f} (the bill stops when the machine is given back)")
    if a.max_cost and est > a.max_cost:
        print(f"over the ceiling of ${a.max_cost:.2f}: nothing rented")
        return 6
    if not regions:
        print("no machine of this type is free in any region now: nothing rented")
        return 3
    return 0


def launch(a) -> int:
    region = a.region
    if not region:
        types = instance_types()
        if a.type not in types:
            print(f"unknown instance type {a.type}")
            return 4
        free = [r["name"] for r in types[a.type].get("regions_with_capacity_available", [])]
        if not free:
            print("no machine of this type is free in any region now: nothing rented")
            return 3
        region = free[0]
    body = {"region_name": region, "instance_type_name": a.type, "ssh_key_names": [a.ssh_key_name], "quantity": 1,
            "name": a.name}
    ids = call("POST", "/instance-operations/launch", body).get("data", {}).get("instance_ids", [])
    if not ids:
        print("Lambda accepted the request but returned no machine")
        return 2
    print(ids[0])
    return 0


def status(a) -> int:
    got = call("GET", f"/instances/{a.id}", missing_ok=True)
    if got is None:                                   # Lambda no longer knows it: given back (the watch stops on this)
        print(f"{a.id} - terminated -")
        return 0
    d = got.get("data", {})
    print(f"{d.get('id', a.id)} {d.get('name', '')} {d.get('status', 'unknown')} {d.get('ip') or '-'}")
    return 0


def wait(a) -> int:
    t_end = time.time() + a.timeout
    while time.time() < t_end:
        d = call("GET", f"/instances/{a.id}").get("data", {})
        st, ip = d.get("status"), d.get("ip")
        if st == "active" and ip:
            print(ip)
            return 0
        if st in ("terminated", "unhealthy"):
            print(f"machine {a.id} is {st}", file=sys.stderr)
            return 5
        time.sleep(a.every)
    print(f"machine {a.id} not running after {a.timeout} s", file=sys.stderr)
    return 5


def age_hours(name: str, now: float) -> float | None:
    parts = name.split("-")
    try:
        return (now - int(parts[2])) / 3600.0
    except (IndexError, ValueError):
        return None


def list_(a) -> int:
    now = time.time()
    for d in call("GET", "/instances").get("data", []):
        name = d.get("name") or ""
        if not name.startswith(a.prefix):
            continue
        age = age_hours(name, now)
        print(f"{d.get('id')} {name} {d.get('status')} {d.get('ip') or '-'} "
              f"{'%.2f' % age if age is not None else '?'}h")
    return 0


def state(i: str) -> str:
    """A machine's state as Lambda reports it; a machine Lambda no longer knows is given back."""
    d = call("GET", f"/instances/{i}", missing_ok=True)
    return "terminated" if d is None else str((d.get("data") or {}).get("status") or "unknown")


def terminate(a) -> int:
    """Give machines back and confirm each one: a machine already given back is fine; one that Lambda neither lists as
    given back nor reports as terminating is still billing, and that is exit 2 with its id (never a quiet success)."""
    ids = [i for i in a.ids if i]
    prefix = getattr(a, "prefix", "") or ""
    if prefix and not prefix.startswith("omni-"):
        # only the machines this workflow names (omni-...); a machine launched by hand on Lambda's page is never touched
        print(f"refused: --prefix must start with omni- (the names this workflow gives), not {prefix!r}", file=sys.stderr)
        return 2
    run = getattr(a, "run", "") or ""
    if a.name or prefix or run:
        # a run's own machines by the run number its name ends with (-r<run id>): found even when the launch job was cut off
        # before it could hand the machine's id on
        ids += [d.get("id") for d in call("GET", "/instances").get("data", [])
                if (d.get("name") == a.name or (prefix and (d.get("name") or "").startswith(prefix))
                    or (run and (d.get("name") or "").endswith(f"-r{run}")))
                and d.get("id") not in ids]
    if not ids:
        print("nothing to give back" + (f" (no machine named {a.name})" if a.name else "")
              + (f" (no machine whose name starts {prefix})" if prefix else "")
              + (f" (no machine of run {run})" if run else ""))
        return 0
    live = [i for i in ids if state(i) not in GONE]
    for i in ids:
        if i not in live:
            print(f"{i}: already given back")
    if live:
        done = call("POST", "/instance-operations/terminate", {"instance_ids": live}).get("data", {})
        gone = {d.get("id") for d in done.get("terminated_instances", [])}
        print("given back: " + (", ".join(i for i in live if i in gone) or "none listed"))
        left = [f"{i} ({st})" for i in live if i not in gone and (st := state(i)) not in GONE]
        if left:
            print("NOT confirmed given back, still billing: " + ", ".join(left)
                  + " (terminate it by hand: cloud.lambda.ai, Instances, tick it, Terminate)", file=sys.stderr)
            return 2
    return 0


PEM = re.compile(r"(-----BEGIN ([A-Z0-9 ]+)-----)(.*?)(-----END \2-----)", re.S)


def fix_key(text: str) -> str:
    """The stored private key as ssh-keygen reads it: carriage returns dropped, anything pasted before its first line dropped,
    and, where its line breaks were lost on the way in (the whole key on one line, or breaks turned into spaces), the body
    wrapped again at the width its form uses (64 for PEM, 70 for OpenSSH). A text that is not a key is returned as it was."""
    t = text.replace("\r", "").strip()
    i = t.find("-----BEGIN ")
    if i > 0:
        t = t[i:]
    m = PEM.match(t)
    if not m or any(":" in ln for ln in m.group(3).splitlines()):     # not a key, or an encrypted PEM's header lines
        return t + "\n"
    body = re.sub(r"\s+", "", m.group(3))
    width = 70 if "OPENSSH" in m.group(2) else 64
    return "\n".join([m.group(1), *(body[k:k + width] for k in range(0, len(body), width)), m.group(4)]) + "\n"


def key_shape(text: str) -> str:
    """What a stored text that ssh-keygen cannot read looks like, from its outline alone: its size and lines, which form its
    first line names, whether it ends, and whether it is something else (a public key, the API key, a passphrase-locked
    key). Never a character of the key."""
    t = text.replace("\r", "").strip()
    lines = t.splitlines()
    size = f"{len(t)} characters on {len(lines)} line{'s' if len(lines) != 1 else ''}"
    if not t:
        return "it is empty"
    if t.startswith(("ssh-rsa ", "ssh-ed25519 ", "ecdsa-sha2-", "sk-ssh-", "sk-ecdsa-")):
        return (f"it holds a public key ({size}), the line Lambda shows on its SSH keys page: GitHub needs the other half, the "
                "file downloaded when the key was made")
    if t.startswith("secret_") or (len(lines) == 1 and "-----" not in t and " " not in t):
        return f"it holds one line with no key markers ({size}): an API key or a name, not the downloaded key file"
    if "-----BEGIN " not in t:
        return f"it holds no key's first line ({size}): open the downloaded .pem file and copy all of it"
    if "ENCRYPTED" in t:
        return f"it holds a key locked with a passphrase ({size}): make a new key in Lambda (it has none) and store that file"
    if not PEM.search(t):
        return f"it starts a key but has no matching last line ({size}): it was cut short when it was copied"
    form = ("an OpenSSH key" if "OPENSSH" in t else "an RSA key in PEM form" if "RSA" in t else
            "an EC key in PEM form" if "EC " in t else "a PKCS#8 key in PEM form")
    return f"it is {form} ({size}), whole in its outline, that ssh-keygen still cannot read: make a new key in Lambda and store that file"


def keycheck(a) -> int:
    """The SSH key pair, checked before anything is rented: the stored private key is the other half of a public key Lambda
    holds (ssh-keygen derives the public half; no key material is printed). The key is found by its own half, so a name
    stored a little differently from Lambda's (Lambda keeps a generated key under its file name, "name.pem.") still finds
    it; the name Lambda holds is written to --resolved-out for the launch. A wrong pair otherwise shows only after a machine
    is rented and refuses the login."""
    keys = call("GET", "/ssh-keys").get("data", [])
    names = [str(k.get("name", "")) for k in keys]
    raw = open(a.private_file, encoding="utf-8", errors="replace").read()
    fixed = fix_key(raw)
    if fixed != raw:              # written back in place, its mode kept: the key every later step uses is the same repair
        with open(a.private_file, "w", encoding="utf-8") as fh:
            fh.write(fixed)
    try:
        out = subprocess.run(["ssh-keygen", "-y", "-P", "", "-f", a.private_file], capture_output=True, text=True,
                             timeout=30)
    except FileNotFoundError:
        print("ssh-keygen is not installed here: the pair is not checked")
        return 0
    if out.returncode != 0 or not out.stdout.split():
        print("LAMBDA_SSH_PRIVATE_KEY: not a whole private key without a passphrase (ssh-keygen could not read it): "
              f"{key_shape(fixed)}; store the whole .pem file Lambda downloaded when the key was made")
        return 7
    half = out.stdout.split()[:2]
    mine = [k for k in keys if str(k.get("public_key", "")).split()[:2] == half]
    if not mine:
        named = a.name in names
        print(("LAMBDA_SSH_PRIVATE_KEY is not the private half of the key Lambda holds under that name"
               if named else f"LAMBDA_SSH_KEY_NAME: Lambda holds no SSH key by that name; it holds {len(names)}: "
               f"{', '.join(names) or 'none'}") + ", and the stored private key is the other half of none of Lambda's keys: "
              "store the .pem file downloaded when one of them was made, or make a new key and store both again")
        return 7
    held = str(mine[0].get("name", ""))
    if a.resolved_out:
        with open(a.resolved_out, "w", encoding="utf-8") as fh:
            fh.write(held + "\n")
    note = "" if held == a.name else " (found by its own half; LAMBDA_SSH_KEY_NAME holds another spelling, and Lambda's is used)"
    print(f"SSH key {held}: Lambda holds it, and the stored private key is its other half{note}")
    return 0


def addkey(a) -> int:
    """Registers a public key with Lambda under a name (the run's own key, when the stored one cannot be used); prints its id."""
    pub = open(a.public_file, encoding="utf-8").read().strip()
    got = call("POST", "/ssh-keys", {"name": a.name, "public_key": pub}).get("data", {})
    print(got.get("id", ""))
    return 0


def delkey(a) -> int:
    """Removes every key Lambda holds under the name (the run's own key, at the run's end); a name it does not hold is fine."""
    gone = 0
    for k in call("GET", "/ssh-keys").get("data", []):
        if k.get("name") == a.name and k.get("id"):
            call("DELETE", f"/ssh-keys/{k['id']}", missing_ok=True)
            gone += 1
    print(f"SSH key {a.name}: {'removed from Lambda' if gone else 'not held by Lambda (nothing to remove)'}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("--type", required=True); p.add_argument("--hours", type=float, required=True)
    p.add_argument("--max-cost", type=float, default=0.0); p.set_defaults(fn=plan)
    p = sub.add_parser("launch"); p.add_argument("--type", required=True); p.add_argument("--name", required=True)
    p.add_argument("--ssh-key-name", required=True); p.add_argument("--region", default=""); p.set_defaults(fn=launch)
    p = sub.add_parser("status"); p.add_argument("id"); p.set_defaults(fn=status)
    p = sub.add_parser("wait"); p.add_argument("id"); p.add_argument("--timeout", type=float, default=1800.0)
    p.add_argument("--every", type=float, default=15.0); p.set_defaults(fn=wait)
    p = sub.add_parser("list"); p.add_argument("--prefix", default="omni-"); p.set_defaults(fn=list_)
    p = sub.add_parser("terminate"); p.add_argument("ids", nargs="*"); p.add_argument("--name", default="")
    p.add_argument("--prefix", default="", help="every machine whose name starts with this (omni-... only)")
    p.add_argument("--run", default="", help="every machine a workflow run rented (its name ends -r<run id>)")
    p.set_defaults(fn=terminate)
    p = sub.add_parser("keycheck"); p.add_argument("--name", required=True); p.add_argument("--private-file", required=True)
    p.add_argument("--resolved-out", default="")
    p.set_defaults(fn=keycheck)
    p = sub.add_parser("addkey"); p.add_argument("--name", required=True); p.add_argument("--public-file", required=True)
    p.set_defaults(fn=addkey)
    p = sub.add_parser("delkey"); p.add_argument("--name", required=True); p.set_defaults(fn=delkey)
    p = sub.add_parser("fixkey", help="stdin to stdout: the stored private key repaired as keycheck repairs it")
    p.set_defaults(fn=lambda a: sys.stdout.write(fix_key(sys.stdin.read())) and 0)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
