#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The software bill of materials and the dependency license inventory, written from the lock file.

Every package pip installs for Omni-Compass is pinned, with its hashes, in requirements-lock.txt. This writes, from that
file and the version in pyproject.toml:
  sbom/omni-compass.cdx.json     CycloneDX 1.5
  sbom/omni-compass.spdx.json    SPDX 2.3
  docs/DEPENDENCY_LICENSES.md    every pinned package, its version and its license, and the rule they are held to
Each package's license is its own declaration (its SPDX expression, or its license field and classifiers where it declares
no expression), written once in LICENSES below. A pinned package with no entry fails the check, and so does a license
that is not permissive or weak file-level copyleft (no GPL, LGPL or AGPL among the pins), so a new dependency cannot enter
without its license being read.

  python3 tools/sbom.py           write the three files
  python3 tools/sbom.py --check   exit 1 if a file is not what the lock gives (the creation time aside) or a license fails
"""
from __future__ import annotations

import argparse, datetime as dt, json, re, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402

LOCK = ROOT / "requirements-lock.txt"
CDX = ROOT / "sbom" / "omni-compass.cdx.json"
SPDX = ROOT / "sbom" / "omni-compass.spdx.json"
PAGE = ROOT / "docs" / "DEPENDENCY_LICENSES.md"
from tools.repo import URL as REPO  # noqa: E402  (the repository's name, written once)
OWN = "LicenseRef-OmniCompass-Evaluation-1.0"
# each package's own declaration, as an SPDX expression (a LicenseRef where SPDX has no identifier); its use in Omni-Compass
LICENSES = {
    "numpy": ("BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0", "numerical arrays"),
    "matplotlib": ("LicenseRef-Matplotlib", "charts in the reports (the Matplotlib License, PSF-based)"),
    "reportlab": ("BSD-3-Clause", "the printed manuals and reports"),
    "PyYAML": ("MIT", "reading workflow and configuration files"),
    "numba": ("BSD-2-Clause", "compiled inner loops of the motion-axis plant"),
    "llvmlite": ("BSD-2-Clause AND Apache-2.0 WITH LLVM-exception", "numba's compiler"),
    "mujoco": ("Apache-2.0", "the robot-arm benchmark (MuJoCo Menagerie)"),
    "z3-solver": ("MIT", "the machine-checked proofs (tools/prove_engine.py)"),
    "mpmath": ("BSD-3-Clause", "interval arithmetic in the machine-checked proofs"),
    "hypothesis": ("MPL-2.0", "the property tests (tests only, never shipped with the engine)"),
    "sortedcontainers": ("Apache-2.0", "brought by hypothesis"),
    "absl-py": ("Apache-2.0", "brought by mujoco"),
    "etils": ("Apache-2.0", "brought by mujoco"),
    "glfw": ("MIT", "brought by mujoco"),
    "contourpy": ("BSD-3-Clause", "brought by matplotlib"),
    "cycler": ("BSD-3-Clause", "brought by matplotlib"),
    "fonttools": ("MIT", "brought by matplotlib"),
    "kiwisolver": ("BSD-3-Clause", "brought by matplotlib"),
    "packaging": ("Apache-2.0 OR BSD-2-Clause", "brought by matplotlib"),
    "pillow": ("MIT-CMU", "brought by matplotlib and reportlab"),
    "pyparsing": ("MIT", "brought by matplotlib"),
    "python-dateutil": ("Apache-2.0 AND BSD-3-Clause", "brought by matplotlib"),
    "six": ("MIT", "brought by python-dateutil"),
    "PyOpenGL": ("BSD-3-Clause", "brought by mujoco"),
    "fsspec": ("BSD-3-Clause", "brought by mujoco"),
    "typing_extensions": ("PSF-2.0", "brought by mujoco"),
    "zipp": ("MIT", "brought by mujoco"),
    "charset-normalizer": ("MIT", "brought by reportlab"),
    "websockets": ("BSD-3-Clause", "brought by mujoco"),
}
REFS = {"LicenseRef-Matplotlib": ("Matplotlib License", "https://matplotlib.org/stable/project/license.html")}
STRONG_COPYLEFT = re.compile(r"\b(A?GPL|LGPL)-")


def pins(text: str):
    return re.findall(r"^([A-Za-z0-9_.\-]+)==([^\s\\]+)", text, re.M)


def version() -> str:
    return tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]


def purl(n, v):
    return f"pkg:pypi/{n.lower().replace('_', '-')}@{v}"


def problems(ps) -> list:
    out = [f"{n}: no license entry in tools/sbom.py LICENSES (read its own declaration first)" for n, _ in ps if n not in LICENSES]
    out += [f"{n}: {LICENSES[n][0]} is strong copyleft" for n, _ in ps if n in LICENSES and STRONG_COPYLEFT.search(LICENSES[n][0])]
    return out


def cdx(ps, ver, when):
    def lic(expr):
        if expr in REFS:
            return [{"license": {"name": REFS[expr][0], "url": REFS[expr][1]}}]
        return [{"expression": expr}] if any(k in expr for k in (" AND ", " OR ", " WITH ")) else [{"license": {"id": expr}}]
    return {"bomFormat": "CycloneDX", "specVersion": "1.5", "version": 1,
            "metadata": {"timestamp": when, "component": {
                "type": "application", "bom-ref": "omni-compass", "name": "omni-compass", "version": ver,
                "publisher": "The Omni-Compass LLC", "copyright": "Copyright (c) 2026 The Omni-Compass LLC",
                "licenses": [{"license": {"name": OWN, "url": f"{REPO}/blob/main/LICENSE"}}],
                "externalReferences": [{"type": "website", "url": "https://www.omni-compass.com"}, {"type": "vcs", "url": REPO}]}},
            "components": [{"type": "library", "bom-ref": purl(n, v), "name": n, "version": v, "purl": purl(n, v),
                            "licenses": lic(LICENSES[n][0]), "description": LICENSES[n][1]} for n, v in ps],
            "dependencies": [{"ref": "omni-compass", "dependsOn": [purl(n, v) for n, v in ps]}]}


def spdx(ps, ver, when):
    pkgs = [{"SPDXID": "SPDXRef-omni-compass", "name": "Omni-Compass", "versionInfo": ver, "supplier": "Organization: The Omni-Compass LLC",
             "downloadLocation": REPO, "licenseConcluded": OWN, "licenseDeclared": OWN, "copyrightText": "Copyright (c) 2026 The Omni-Compass LLC",
             "filesAnalyzed": False}]
    rels = [{"spdxElementId": "SPDXRef-DOCUMENT", "relationshipType": "DESCRIBES", "relatedSpdxElement": "SPDXRef-omni-compass"}]
    for n, v in ps:
        sid = "SPDXRef-pypi-" + re.sub(r"[^A-Za-z0-9.\-]", "-", n)
        pkgs.append({"SPDXID": sid, "name": n, "versionInfo": v, "downloadLocation": f"https://pypi.org/project/{n}/{v}/",
                     "licenseConcluded": LICENSES[n][0], "licenseDeclared": LICENSES[n][0], "copyrightText": "NOASSERTION",
                     "filesAnalyzed": False, "comment": LICENSES[n][1],
                     "externalRefs": [{"referenceCategory": "PACKAGE-MANAGER", "referenceType": "purl", "referenceLocator": purl(n, v)}]})
        rels.append({"spdxElementId": "SPDXRef-omni-compass", "relationshipType": "DEPENDS_ON", "relatedSpdxElement": sid})
    return {"spdxVersion": "SPDX-2.3", "dataLicense": "CC0-1.0", "SPDXID": "SPDXRef-DOCUMENT", "name": "Omni-Compass SBOM",
            "documentNamespace": f"{REPO}/sbom/omni-compass-{ver}",
            "creationInfo": {"created": when, "creators": ["Organization: The Omni-Compass LLC", "Tool: tools/sbom.py"]},
            "hasExtractedLicensingInfos": [{"licenseId": OWN, "name": "Omni-Compass Evaluation License 1.0",
                                            "extractedText": f"See LICENSE: {REPO}/blob/main/LICENSE"}] +
                                          [{"licenseId": k, "name": n, "extractedText": f"See {u}"} for k, (n, u) in REFS.items()],
            "packages": pkgs, "relationships": rels}


def page(ps, ver) -> str:
    L = ["# Every dependency and its license", "",
         f"Generated by `python3 tools/sbom.py` from `requirements-lock.txt` (Omni-Compass {ver}); `tools/sbom.py --check`, run by "
         "`verify.py`, fails a push where this page or the bill of materials (`sbom/omni-compass.cdx.json`, CycloneDX 1.5; "
         "`sbom/omni-compass.spdx.json`, SPDX 2.3) is not what the lock gives, where a pinned package has no license read, or "
         "where a license is strong copyleft. Every package is pinned with the SHA-256 of every file PyPI publishes for its "
         "version, and `security-scan.yml` audits every pin against the public vulnerability databases each week.", "",
         f"**{len(ps)} packages; every license permissive except one weak, file-level copyleft (MPL-2.0, Hypothesis, used by the "
         "tests alone and never shipped with the engine); no GPL, LGPL or AGPL.** Each package keeps its own license; nothing "
         "in the Omni-Compass Evaluation License changes those terms (`THIRD_PARTY_NOTICES.md`).", "",
         "| Package | Version | License (SPDX) | Its use in Omni-Compass |", "|---|---|---|---|"]
    L += [f"| {n} | {v} | {LICENSES[n][0]} | {LICENSES[n][1]} |" for n, v in ps]
    return "\n".join(L) + "\n"


def without_time(d: dict) -> dict:
    d = json.loads(json.dumps(d))
    d.get("metadata", {}).pop("timestamp", None)
    d.get("creationInfo", {}).pop("created", None)
    return d


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    ps, ver = pins(LOCK.read_text()), version()
    bad = problems(ps)
    if bad:
        print("sbom: " + "; ".join(bad))
        return 1
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    new = {CDX: cdx(ps, ver, now), SPDX: spdx(ps, ver, now)}
    text = "\n".join(stamp(page(ps, ver).split("\n"))) + "\n"
    old = {p: json.loads(p.read_text()) if p.exists() else None for p in new}
    same = {p: old[p] is not None and without_time(old[p]) == without_time(new[p]) for p in new}
    if a.check:
        ok = all(same.values()) and PAGE.exists() and PAGE.read_text(encoding="utf-8") == text
        print(f"sbom: {len(ps)} pinned packages, every license read; " + ("the bill of materials and the license page are current"
              if ok else "out of date (python3 tools/sbom.py)"))
        return 0 if ok else 1
    for p, d in new.items():
        if not same[p]:                                 # the creation time moves only when the content does
            p.write_text(json.dumps(d, indent=2) + "\n")
    PAGE.write_text(text, encoding="utf-8")
    print(f"sbom: {len(ps)} packages -> {CDX.relative_to(ROOT)}, {SPDX.relative_to(ROOT)}, {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
