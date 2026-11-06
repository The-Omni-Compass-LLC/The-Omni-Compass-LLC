#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Check an archived run's receipt: its files against its sums, and its sums against their signature.

Every finished run's files are archived on the branch raw as run-<id>/ (.github/workflows/archive-run.yml) with
SHA256SUMS_ALL.txt, the SHA-256 of every file in the folder. A sum is a fingerprint: it shows that a file has not changed
since the sum was written, but not who wrote the sum. From 31 October 2026 the archive also signs each run's
SHA256SUMS_ALL.txt with Sigstore, keyless: GitHub vouches for the job that signs (this repository's archive workflow),
Sigstore's certificate authority issues a short-lived certificate to that identity, and the signature is entered in
Sigstore's public transparency log. The signature and its proof are saved beside the sums as
SHA256SUMS_ALL.txt.sigstore.json. Nobody, The Omni-Compass LLC included, can change a signed run's files afterwards or
backdate a signature without this check failing.

  bash scripts/raw_archive.sh open /run-<id>/            place the run at results/live/raw/run-<id>/
  python3 tools/verify_receipt.py results/live/raw/run-<id> [more folders]

1. Every file SHA256SUMS_ALL.txt lists is in the folder and hashes to its line, and no file is there that it does not
   list (a file stored gzipped is listed as stored; the signature file is the one expected addition).
2. The signature verifies against SHA256SUMS_ALL.txt on Sigstore's public trust root, issued to GitHub Actions running this
   repository's archive workflow (GitHub's number for the repository, kept through any rename). Needs
   `pip install sigstore==4.5.1`; --offline checks with the log proof the signature file carries.

A run archived before signing began reads "sums only": step 1 still holds and step 2 has nothing to check. Exit 0 when
every check that can run passes, 1 on any difference.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

SUMS = "SHA256SUMS_ALL.txt"
BUNDLE = SUMS + ".sigstore.json"

# GitHub Actions' identity, as Sigstore's certificate authority writes it into the signing certificate (the extensions
# of Fulcio's arc 1.3.6.1.4.1.57264.1, each a DER UTF8String)
ISSUER = "https://token.actions.githubusercontent.com"
REPOSITORY_ID = "1390458092"          # GitHub's number for the repository tools/repo.py names (it survives a rename)
OWNER_ID = "334396871"                # GitHub's number for the organization that owns it
WORKFLOW = "/.github/workflows/archive-run.yml@refs/heads/"
OID = {"issuer": "1.3.6.1.4.1.57264.1.8", "signer": "1.3.6.1.4.1.57264.1.9", "repository": "1.3.6.1.4.1.57264.1.12",
       "repository_id": "1.3.6.1.4.1.57264.1.15", "owner_id": "1.3.6.1.4.1.57264.1.17", "trigger": "1.3.6.1.4.1.57264.1.20",
       "run": "1.3.6.1.4.1.57264.1.21"}


class ReceiptError(Exception):
    """A check that failed, with the reason."""


def der_utf8(raw: bytes) -> str:
    """The text of a DER-encoded UTF8String (tag 12, definite length)."""
    if len(raw) < 2 or raw[0] != 0x0C:
        raise ReceiptError("a certificate field is not a UTF8String")
    n, i = raw[1], 2
    if n & 0x80:
        k = n & 0x7F
        n, i = int.from_bytes(raw[2:2 + k], "big"), 2 + k
    if len(raw) != i + n:
        raise ReceiptError("a certificate field's length does not match its bytes")
    return raw[i:i + n].decode("utf-8")


def cert_fields(cert) -> dict[str, str]:
    """GitHub's identity fields in a signing certificate (an x509 certificate as the cryptography package reads it)."""
    try:
        from cryptography.x509 import ObjectIdentifier
    except ImportError:                                     # a certificate read another way: its fields by dotted name
        ObjectIdentifier = str
    out = {}
    for name, oid in OID.items():
        try:
            ext = cert.extensions.get_extension_for_oid(ObjectIdentifier(oid))
        except Exception:                                   # ExtensionNotFound: the field is absent
            continue
        out[name] = der_utf8(ext.value.value)
    return out


def check_identity(fields: dict[str, str]) -> str:
    """Raise ReceiptError unless the certificate was issued to this repository's archive workflow on GitHub Actions;
    return the run that signed."""
    if fields.get("issuer") != ISSUER:
        raise ReceiptError(f"issued to {fields.get('issuer')!r}, not to GitHub Actions")
    if fields.get("repository_id") != REPOSITORY_ID or fields.get("owner_id") != OWNER_ID:
        raise ReceiptError(f"signed in repository {fields.get('repository')!r} (number {fields.get('repository_id')}), "
                           f"not in The Omni-Compass LLC's repository (number {REPOSITORY_ID})")
    if WORKFLOW not in fields.get("signer", ""):
        raise ReceiptError(f"signed by {fields.get('signer')!r}, not by the archive workflow")
    return fields.get("run", "")


class ArchiveJob:
    """Sigstore's verification policy: GitHub Actions running this repository's archive workflow, on any branch's copy
    of it (the kept branches are level with main)."""

    def __init__(self):
        self.run = ""

    def verify(self, cert) -> None:
        try:
            self.run = check_identity(cert_fields(cert))
        except ReceiptError as e:
            from sigstore.errors import VerificationError
            raise VerificationError(str(e)) from None


def parse_sums(text: str) -> dict[str, str]:
    """sha256sum's lines ('<hash>  <path>', or '<hash> *<path>' in binary mode) as {path: hash}."""
    out = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        h, sep, path = line.partition(" ")
        if len(h) != 64 or not sep or not path:
            raise ReceiptError(f"{SUMS} line {n} is not a sha256sum line")
        path = path[1:] if path[:1] in (" ", "*") else path
        out[path[2:] if path.startswith("./") else path] = h.lower()
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def check_files(folder: Path) -> int:
    """Step 1: every listed file is there with its hash, and nothing unlisted is there. Returns the count of files."""
    sums_file = folder / SUMS
    if not sums_file.exists():
        raise ReceiptError(f"{folder}: no {SUMS}")
    listed = parse_sums(sums_file.read_text(encoding="utf-8"))
    present = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()} - {SUMS, BUNDLE}
    bad = [f"missing: {p}" for p in sorted(set(listed) - present)]
    bad += [f"not in the sums: {p}" for p in sorted(present - set(listed))]
    bad += [f"changed: {p}" for p in sorted(set(listed) & present) if sha256(folder / p) != listed[p]]
    if bad:
        raise ReceiptError(f"{folder}: " + "; ".join(bad[:20]) + (f"; and {len(bad) - 20} more" if len(bad) > 20 else ""))
    return len(listed)


def check_signature(folder: Path, offline: bool = False) -> str:
    """Step 2: the bundle verifies against the sums for the archive workflow's identity. Returns the run that signed."""
    try:
        from sigstore.models import Bundle
        from sigstore.verify import Verifier
    except ImportError:
        raise ReceiptError("the signature check needs the sigstore package: pip install sigstore==4.5.1") from None
    bundle = Bundle.from_json((folder / BUNDLE).read_bytes())
    policy = ArchiveJob()
    try:
        Verifier.production(offline=offline).verify_artifact((folder / SUMS).read_bytes(), bundle, policy)
    except Exception as e:                                  # VerificationError and every malformed input
        raise ReceiptError(f"{folder}: the signature does not verify: {e}") from None
    return policy.run


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="+", type=Path)
    ap.add_argument("--offline", action="store_true", help="verify with the log proof in the bundle, no network")
    a = ap.parse_args(argv)
    failed = 0
    for folder in a.folders:
        try:
            n = check_files(folder)
            if (folder / BUNDLE).exists():
                run = check_signature(folder, a.offline)
                print(f"{folder}: {n} files match their sums; the sums carry a valid signature by the archive job {run}")
            else:
                print(f"{folder}: {n} files match their sums; sums only (archived before signing began, or its signing failed)")
        except ReceiptError as e:
            failed += 1
            print(f"DIFFERENCE {e}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
