#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A cloud key's shape, read before the cloud's login, so a key cut short or stored in the wrong form is named at no cost.

  python3 tools/cloud_key_check.py           Google: GCP_CREDENTIALS (and GCP_PROJECT to compare)
  python3 tools/cloud_key_check.py azure     Azure: AZURE_CREDENTIALS
  python3 tools/cloud_key_check.py kubeconfig  a cluster built in a provider's console (Oracle, DigitalOcean, Alibaba, Linode,
                                               IBM or any other): KUBECONFIG_RAW, the kubeconfig from KUBECONFIG_<CLOUD>

On 18 October the stored GCP_CREDENTIALS ended part of the way through (it had been selected from Cloud Shell's screen),
and every Google set failed at the login with Google's "unexpected end of JSON input". For a while on the night of
21 October AZURE_CREDENTIALS held a text that is not the JSON block Azure's login takes (a collect failed at 23:37 UTC; the
block was whole again by 00:00), and Azure's own login step quoted its first characters on the run's page while refusing it. This reads the key from the environment and prints
only what is wrong with its shape: how many characters were stored, which fields are missing, where the JSON stops, what
the stored text looks like. It never prints a character of the key, and it runs before the cloud's own login step, so a
key in the wrong form never reaches a step that would quote it.
Exit 0: a whole key. Exit 2: what is wrong, and what to store again (docs/GOOGLE_SETUP.md, docs/AZURE_SETUP.md,
docs/BYOC_SETUP.md)."""
from __future__ import annotations

import base64
import binascii
import json
import os
import re
import sys

FIELDS = ("type", "project_id", "private_key_id", "private_key", "client_email", "token_uri")
WHOLE = "a whole key is about 2,300 to 2,400 characters, from { to }"


def what_it_holds(raw: str) -> str:
    """What a stored text that is not a key file looks like, read from its shape alone (never a character of it), so the
    person storing it again knows what went wrong: a piece from inside the file, the private key alone, an encoded string,
    an account name, or too little to be any of these."""
    if before_brace(raw):
        return before_brace(raw)
    if "workloadIdentityPools" in raw or "workload_identity_provider" in raw:
        return ("it holds the settings of a GitHub link made without a key (a Workload Identity provider"
                + (" and a service account" if "service_account" in raw or ".iam.gserviceaccount.com" in raw else "")
                + "), not the key file")
    if "gcloud " in raw:
        return ("it holds commands (lines that start with gcloud), the setup lines that are run in Google's Cloud Shell; the "
                "key file they make, key.json, is what goes in the box")
    if any(f'"{f}"' in raw for f in FIELDS):
        return "it holds a piece from inside the file (its first line, the {, is missing): the copy started part of the way in"
    if "-----BEGIN PRIVATE KEY-----" in raw or "PRIVATE KEY-----" in raw:
        return "it holds the private key alone, a part of the file; store the whole file"
    if "@" in raw and raw.count(" ") == 0 and n_lines(raw) == 1 and len(raw) < 200:
        return "it looks like an account's address, not the key file"
    if len(raw) >= 200 and all(c.isalnum() or c in "+/=\n\r" for c in raw):
        return "it looks like an encoded string (the middle of the private key, or the file encoded), not the key file"
    if len(raw) >= 100 and all(c.isalnum() or c in "-_.~+/=\n\r" for c in raw):
        return ("it looks like a token or a web-safe encoded string (an access token, for one, which expires within the "
                "hour), not the key file")
    return "it is not the key file" + shape_words(raw)


def n_lines(raw: str) -> int:
    return raw.count("\n") + 1


def before_brace(raw: str) -> str:
    """Words for a text that holds a { but not at its start: something was pasted in front of the key (a name, a quote, a
    word), counted, never shown. Empty when there is no { or it stands first."""
    i = raw.find("{")
    if i <= 0:
        return ""
    return (f"{i} character{'s stand' if i != 1 else ' stands'} before its first {{ (a name, a quotation mark or a word "
            "pasted with it): store only from { to }")


def shape_words(raw: str) -> str:
    """The stored text's outline, so the person can tell which text it was: its lines, and whether it holds spaces, a web
    address or quotation marks. Never a character of it."""
    n = n_lines(raw)
    bits = [f"{n} line{'s' if n != 1 else ''}"]
    marks = [w for w, hit in (("spaces", " " in raw), ("a web address", "://" in raw), ("quotation marks", '"' in raw))
             if hit]
    bits.append(("with " + ", ".join(marks) + " in it") if marks else "no spaces")
    return "; it is " + ", ".join(bits)


def problems(raw: str | None, project: str = "") -> list[str]:
    """What is wrong with a stored service-account key, in words that carry none of its characters (empty: whole)."""
    raw = (raw or "").strip()
    if not raw:
        return ["the secret is empty"]
    n = len(raw)
    if not raw.startswith("{"):
        return [f"it does not start with {{ ({n} characters stored; {WHOLE}); {what_it_holds(raw)}"]
    if not raw.endswith("}"):
        return [f"it does not end with }}: it was cut short when it was copied ({n} characters stored; {WHOLE})"]
    try:
        key = json.loads(raw)
    except ValueError as e:
        where = getattr(e, "pos", None)
        return [f"it is not whole JSON (it breaks at character {where} of {n}): it was cut or changed when it was copied"]
    if not isinstance(key, dict):
        return ["it is not a key (not one JSON object)"]
    out = []
    missing = [f for f in FIELDS if not key.get(f)]
    if missing:
        out.append("fields missing: " + ", ".join(missing))
    if key.get("type") and key["type"] != "service_account":
        out.append("it is not a service-account key (its type field reads otherwise)")
    pk = str(key.get("private_key") or "")
    if pk and not ("-----BEGIN PRIVATE KEY-----" in pk and pk.rstrip().endswith("-----END PRIVATE KEY-----")):
        out.append("its private key is not whole")
    if project.strip() and key.get("project_id") and key["project_id"] != project.strip():
        out.append("its project is not the one in GCP_PROJECT (GCP_PROJECT holds the Project ID the key was made in)")
    return out


# Azure: the block `az ad sp create-for-rbac ... --sdk-auth` prints (docs/AZURE_SETUP.md, section 3), the form azure/login's
# creds input takes; its four fields that login reads
AZURE_FIELDS = ("clientId", "clientSecret", "subscriptionId", "tenantId")
AZURE_WHOLE = "the whole block is about 400 to 700 characters on about ten lines, from { to }"


def _guid(s: str) -> bool:
    parts = s.split("-")
    return [len(x) for x in parts] == [8, 4, 4, 4, 12] and all(all(c in "0123456789abcdefABCDEF" for c in x) for x in parts)


def azure_what_it_holds(raw: str) -> str:
    """What a stored text that is not the JSON block looks like, from its shape alone (never a character of it)."""
    if before_brace(raw):
        return before_brace(raw)
    if any(f'"{f}"' in raw for f in AZURE_FIELDS):
        return "it holds a piece from inside the block (its first line, the {, is missing): the copy started part of the way in"
    one = raw.strip()
    if len(one) == 88 and one.endswith("==") and all(c.isalnum() or c in "+/=" for c in one):
        return ("it looks like a storage account's access key (88 characters, encoded: the size Azure gives every storage "
                "and database account key, from a storage account's Access keys page), not the block: such a key opens one "
                "storage account, never the subscription")
    if _guid(one):
        return ("it holds one identifier alone (an application, tenant or subscription ID, a 36-character GUID), not the "
                "whole block")
    if "\n" not in one and " " not in one and 30 <= len(one) <= 48:
        return ("it looks like a client secret's value alone (one line, no { or }): Azure's login needs the whole block that "
                "the line in section 3 prints, the secret one of its fields")
    if "=" in one and ";" in one:
        return "it looks like a connection string, not the block"
    return "it is not the block" + shape_words(one)


def azure_problems(raw: str | None) -> list[str]:
    """What is wrong with a stored AZURE_CREDENTIALS, in words that carry none of its characters (empty: whole)."""
    raw = (raw or "").strip()
    if not raw:
        return ["the secret is empty"]
    n = len(raw)
    if not raw.startswith("{"):
        return [f"it does not start with {{ ({n} characters stored; {AZURE_WHOLE}); {azure_what_it_holds(raw)}"]
    if not raw.endswith("}"):
        return [f"it does not end with }}: it was cut short when it was copied ({n} characters stored; {AZURE_WHOLE})"]
    try:
        block = json.loads(raw)
    except ValueError as e:
        where = getattr(e, "pos", None)
        return [f"it is not whole JSON (it breaks at character {where} of {n}): it was cut or changed when it was copied"]
    if not isinstance(block, dict):
        return ["it is not the block (not one JSON object)"]
    out = []
    missing = [f for f in AZURE_FIELDS if not str(block.get(f) or "").strip()]
    if missing:
        out.append("fields missing: " + ", ".join(missing))
    bad_ids = [f for f in ("clientId", "subscriptionId", "tenantId") if f not in missing and not _guid(str(block[f]).strip())]
    if bad_ids:
        out.append("not a 36-character GUID: " + ", ".join(bad_ids))
    return out


# Azure's four boxes (24 October): the same login typed one value to a box, as the portal shows each value on its own, so no
# block is assembled by hand. The three IDs are the boxes the sign-in without a password already reads (docs/AZURE_SETUP.md,
# section 8); the password is AZURE_CLIENT_SECRET, or AZURE_CREDENTIALS when that box holds a password's value alone.
AZURE_BOXES = (("AZURE_CLIENT_ID", "clientId", "the Application (client) ID"),
               ("AZURE_TENANT_ID", "tenantId", "the Directory (tenant) ID"),
               ("AZURE_SUBSCRIPTION_ID", "subscriptionId", "the Subscription ID"))


def _secret_value(s: str) -> bool:
    """A client secret's value as the portal's Value column gives it: one line of 30 to 48 characters, no spaces, no { },
    and not an ID (the Secret ID column beside it is a 36-character GUID, never the password; a storage account's key is
    88 characters)."""
    return bool(s) and not _guid(s) and not s.startswith("{") and " " not in s and "\n" not in s and 30 <= len(s) <= 48


def azure_login(env) -> tuple[str | None, str, list[str]]:
    """The block azure/login's creds takes, from AZURE_CREDENTIALS whole or from the four boxes: (block, where it came from,
    problems). Every problem names a box and what is wrong with its shape, never a character of it."""
    raw = (env.get("AZURE_CREDENTIALS") or "").strip()
    one = azure_problems(raw)
    if not one:
        return json.dumps(json.loads(raw), separators=(",", ":")), "AZURE_CREDENTIALS, the whole block", []
    secret = (env.get("AZURE_CLIENT_SECRET") or "").strip()
    secret_box = "AZURE_CLIENT_SECRET"
    if not secret and _secret_value(raw):
        secret, secret_box = raw, "AZURE_CREDENTIALS"
    four, block = [], {}
    for box, field, what in AZURE_BOXES:
        v = (env.get(box) or "").strip()
        if not v:
            four.append(f"{box} is empty (it takes {what}, a 36-character ID)")
        elif not _guid(v):
            four.append(f"{box} is not a 36-character ID ({len(v)} characters stored; it takes {what})")
        else:
            block[field] = v
    if not secret:
        four.append("AZURE_CLIENT_SECRET is empty (it takes the password's Value from Certificates & secrets, about 40 "
                    "characters)")
    elif _guid(secret):
        four.append(f"{secret_box} holds a 36-character ID, not a password: on Certificates & secrets copy the Value column, "
                    "never the Secret ID beside it")
    elif not _secret_value(secret):
        four.append(f"{secret_box} is not a password's value ({len(secret)} characters stored, {n_lines(secret)} line(s))")
    else:
        block["clientSecret"] = secret
    if not four:
        block = {f: block[f] for f in AZURE_FIELDS}
        return json.dumps(block, separators=(",", ":")), f"the four boxes (the password from {secret_box})", []
    return None, "", ["AZURE_CREDENTIALS: " + "; ".join(one), "the four boxes: " + "; ".join(four)]


# the command-line tools a kubeconfig's exec credential plugin may call that GitHub's runner does not carry: such a kubeconfig
# logs in on the tester's own computer and nowhere else (docs/BYOC_SETUP.md, section 3: a token kubeconfig instead)
NOT_ON_RUNNER = ("oci", "doctl", "aliyun", "ibmcloud", "linode-cli", "kubelogin", "gke-gcloud-auth-plugin", "aws-iam-authenticator")


def kubeconfig_text(raw: str) -> str | None:
    """The kubeconfig as stored (YAML) or base64 of it; None where it is neither."""
    s = (raw or "").strip()
    if "apiVersion" in s:
        return s
    try:
        d = base64.b64decode(re.sub(r"\s+", "", s), validate=True).decode("utf-8")
    except (binascii.Error, ValueError, UnicodeDecodeError):
        return None
    return d if "apiVersion" in d else None


def kubeconfig_problems(raw: str | None) -> tuple[list[str], str]:
    """What is wrong with a stored kubeconfig's shape, and a line on what it holds; never a character of its values. A
    kubeconfig is whole when it names at least one cluster with an https server, one context and one user, and the user
    logs in by what the file carries itself (a token, or a client certificate and key) or by an exec plugin GitHub's runner
    has; a plugin only the provider's own command line has is refused here, before anything is measured."""
    if not (raw or "").strip():
        return ["it is empty"], ""
    text = kubeconfig_text(raw)
    if text is None:
        return [f"it is neither a kubeconfig (no apiVersion line) nor base64 of one ({len(raw.strip())} characters stored, "
                f"{len(raw.strip().splitlines())} line(s))"], ""
    keys = {k for k in re.findall(r"^([a-z-]+):", text, re.M)}
    bad = [f"no top-level {k}: line" for k in ("clusters", "contexts", "users") if k not in keys]
    servers = re.findall(r"^\s*server:\s*(\S+)", text, re.M)
    if not servers:
        bad.append("no cluster server: line")
    elif not all(s.strip("'\"").startswith("https://") for s in servers):
        bad.append("a cluster server is not an https:// address")
    token = bool(re.search(r"^\s*token:\s*\S", text, re.M))
    cert = bool(re.search(r"^\s*client-certificate-data:\s*\S", text, re.M)) and bool(re.search(r"^\s*client-key-data:\s*\S", text, re.M))
    execs = re.findall(r"^\s*command:\s*['\"]?([^\s'\"]+)", text, re.M) if re.search(r"^\s*exec:\s*$", text, re.M) else []
    off = sorted({os.path.basename(c) for c in execs if os.path.basename(c) in NOT_ON_RUNNER})
    if off and not (token or cert):
        bad.append(f"its user logs in through {', '.join(off)}, a provider's command line GitHub's runner does not carry: store a "
                   "kubeconfig whose user holds a service-account token (docs/BYOC_SETUP.md, section 3)")
    elif not (token or cert or execs):
        bad.append("its user carries no way to log in (no token, no client certificate and key, no exec plugin)")
    how = "a token" if token else "a client certificate and key" if cert else f"the plugin {', '.join(sorted(set(execs)))}" if execs else "nothing"
    return bad, f"{len(servers)} cluster server(s), logging in by {how}"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args[:1] == ["kubeconfig"]:
        bad, holds = kubeconfig_problems(os.environ.get("KUBECONFIG_RAW"))
        if not bad:
            print(f"the kubeconfig: whole ({holds})")
            return 0
        for b in bad:
            print(f"::error::the kubeconfig: {b}.")
        print("::error::Nothing measured, nothing billed. Store the cluster's kubeconfig again in KUBECONFIG_<CLOUD> "
              "(docs/BYOC_SETUP.md, section 3).")
        return 2
    if args[:1] == ["azure"]:
        block, where, bad = azure_login(os.environ)
        if block:
            print(f"Azure's login: whole, from {where}")
            out = os.environ.get("GITHUB_ENV")
            if out:
                # the next step's azure/login reads it as env.AZ_CREDS; masked first, so no log line can carry it
                print(f"::add-mask::{block}")
                with open(out, "a", encoding="utf-8") as fh:
                    fh.write(f"AZ_CREDS={block}\n")
            return 0
        for b in bad:
            print(f"::error::{b}.")
        print("::error::Nothing built, nothing billed. Fill either way (docs/AZURE_SETUP.md, section 7): the four boxes, one "
              "value each, from the app's Overview page, its Certificates & secrets and the subscription; or "
              "AZURE_CREDENTIALS with the whole block from { to }.")
        return 2
    bad = problems(os.environ.get("GCP_CREDENTIALS"), os.environ.get("GCP_PROJECT", ""))
    if not bad:
        print("GCP_CREDENTIALS: a whole service-account key")
        return 0
    for b in bad:
        print(f"::error::GCP_CREDENTIALS: {b}. Nothing built, nothing billed. Store the key again, whole: "
              "docs/GOOGLE_SETUP.md, section 4 (download the key file and paste all of it).")
    return 2


if __name__ == "__main__":
    sys.exit(main())
