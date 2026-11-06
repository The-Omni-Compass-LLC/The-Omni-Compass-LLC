# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The legal notice, written once, and the check that it stands everywhere.

The founder's orders of 10 October 2026: every page, table, report, script, workflow run, export and chat answer about
Omni-Compass carries "all rights reserved" and "all patents, copyrights and trademarks filed in the USA" followed by
www.omni-compass.com and nothing after it, at its top and at its end, the way a company protects a released asset. Two
earlier sentences of the notice were retired the same evening and may stand nowhere (RETIRED; --check fails on them). This
module holds the one wording and the machinery that keeps it in place.

  python3 tools/legal.py --check           every file that lacks the notice or still carries an older wording; exit 1 if any
  python3 tools/legal.py --fix [PATH...]   write the notice wherever it is missing or old (all files, or only those under PATH)
  python3 tools/legal.py --summary         the notice as a workflow run's report opens with it (--summary-end: as it closes)
  python3 tools/legal.py --bundle DIR      put README.md, LICENSE, NOTICE, DISCLOSURES.md, PATENTS.md, TRADEMARKS.md into DIR

Where it goes: Markdown pages carry it under their title and again at their end; source files, scripts and workflows carry
it in their header; every workflow opens and closes each job's report with it and hands out the legal files beside the files
it produces (`legal-notice`); every zip and export carries the bundle above.

Locked files keep their bytes: the engine's fingerprinted files (tools/omni_version.py), the C++ twins under the seal
(results/SEAL.json), the reference engine (reference/PROVENANCE.json), the pre-registered harness files
(results/PREREGISTRATION.json, results/fleet/PREREGISTRATION.json) and the dated source snapshot under docs/handoff/. One
changed byte there would break a recorded fingerprint, so their headers are rewritten with the next engine version, never in
between; --check counts them as locked, not as missing. Data files (JSON, CSV, logs, archived run files) carry no comments:
REUSE.toml and the LICENSE beside them cover them, and third-party data keeps its own notice."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BODY = ("© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial "
        "use, commercialization, monetization, production use, redistribution or hosted service of any part of "
        "Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, "
        "report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`.")
CLOSE = "All patents, copyrights and trademarks filed in the USA. www.omni-compass.com"
NOTICE = f"{BODY} {CLOSE}"
# the founder's wording of 10 October 2026: "all" before patents, copyrights and trademarks; all rights reserved; and, as
# ordered that evening, the website directly after the filing sentence with nothing after it. Every generated report
# carries it at its top and at its end.
SPDX = "SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0"
TOP = f"{BODY} `{SPDX}` {CLOSE}"          # a page's opening notice carries the license tag for the scanners (Black Duck, FOSSA, Snyk)
MARK = "© 2026 Dubra Software Inc. / The Omni-Compass LLC"   # a page carrying this carries the notice (the owners in the founder's order of 6 November)
PLAIN = re.sub(r"[*`]", "", NOTICE)       # the same words without Markdown, for plain text, PDFs and chat answers
FILED = "All patents, copyrights and trademarks filed in the USA."
SHORT = ("© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. All patents, copyrights "
         "and trademarks filed in the USA. www.omni-compass.com")
HEADER = (
    "SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0",
    "Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.",
    "Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid",
    "Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.",
    "All patents, copyrights and trademarks filed in the USA. www.omni-compass.com",
)
BUNDLE = ("README.md", "LICENSE", "NOTICE", "DISCLOSURES.md", "PATENTS.md", "TRADEMARKS.md")
# the earlier filing sentence, written in two pieces so that --fix, which rewrites it everywhere, cannot rewrite it here
OLD_FILED = re.compile("All patent " + "applications, copyright registrations and trademark applications")
REQUIRED = ("omni-compass llc", "dubra software", "all rights reserved", "all patents, copyrights and trademarks", "omni-compass.com")
# the owners as the founder named them on 6 November: "Dubra Software Inc. / The Omni-Compass LLC" (Dubra Software, his own company, owns it with The Omni-Compass LLC)
# the two sentences the founder retired from the notice on the evening of 10 October; no page, header, report or program
# may carry them. Spelled word by word so that this file, which looks for them, carries neither
RETIRED = (" ".join(("subject", "to", "change")), " ".join(("authority", "of", "record")))
# the notice's word written in lower case: the founder's order of 20 October writes Simulation with a capital S, as the
# LICENSE does. Spelled in two pieces so that this file, which looks for it, does not carry it
LOWER_S = "Evaluation and " + "simulation use only"

HASH, SLASH = "#", "//"
BY_SUFFIX = {".py": HASH, ".sh": HASH, ".bash": HASH, ".yml": HASH, ".yaml": HASH, ".toml": HASH, ".cff": HASH, ".cfg": HASH,
             ".ini": HASH, ".cpp": SLASH, ".hpp": SLASH, ".h": SLASH, ".cc": SLASH, ".c": SLASH}
BY_NAME = {"Dockerfile": HASH, "CODEOWNERS": HASH, "OWNERS": HASH, "requirements.txt": HASH, "requirements-lock.txt": HASH,
           ".snyk": HASH, ".gitignore": HASH, ".gitattributes": HASH, ".dockerignore": HASH}
MARKDOWN_NAMES = {"SECURITY_CONTACTS"}
PLAIN_LEGAL = ("LICENSE", "NOTICE", "LICENSES/LicenseRef-OmniCompass-Evaluation-1.0.txt")   # written by hand; checked, not rewritten
EXEMPT = ("results/live/raw/", "tests/third_party/", "fleet/traces/", "k8s_controlplane/traces/", "release/")
SNAPSHOTS = ("docs/handoff/",)

START_STEP = "Legal notice at the top of this job's report"
END_STEP = "Legal notice at the end of this job's report"
LEGAL_ARTIFACT = "legal-notice"


# ---------------------------------------------------------------- which files, and which are locked

def tracked(root: Path = ROOT, others: bool = False) -> list[str]:
    """The repository's files; with others, also the new files not yet added (a bot stamps a page before it commits it)."""
    cmd = ["git", "-c", "safe.directory=*", "ls-files"] + (["--cached", "--others", "--exclude-standard"] if others else [])
    out = subprocess.run(cmd, cwd=root, capture_output=True, text=True).stdout
    return sorted({p for p in out.splitlines() if p})


def locked(root: Path = ROOT) -> set[str]:
    """Files whose bytes a recorded fingerprint holds: changing one byte would break the engine's version, the seal, the
    reference engine's provenance or a pre-registration."""
    out: set[str] = set()
    sys.path.insert(0, str(root))
    try:
        from tools.omni_version import SCOPE
    except Exception:                                    # a root without the version tool (a test's scratch tree)
        SCOPE = ()
    if SCOPE:
        names = subprocess.run(["git", "-c", "safe.directory=*", "ls-files", "--", *SCOPE], cwd=root, capture_output=True,
                               text=True).stdout.split()
        out |= {n for n in names if n.endswith((".py", ".csv")) and "__pycache__" not in n}
    for rel in ("results/PREREGISTRATION.json", "results/fleet/PREREGISTRATION.json"):
        p = root / rel
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            for key in ("sha256", "code_fingerprint"):
                out |= set((d.get(key) or {}).keys())
    seal = root / "results" / "SEAL.json"
    if seal.exists():
        for t in (json.loads(seal.read_text(encoding="utf-8")).get("twins") or {}).values():
            out |= set((t.get("sha256") or {}).keys())
    prov = root / "reference" / "PROVENANCE.json"
    if prov.exists():
        ref = json.loads(prov.read_text(encoding="utf-8")).get("reference_engine")
        if ref:
            out.add(ref)
    return out


def kind(path: str, text: str | None = None):
    """'md', 'legal', a comment marker ('#' or '//'), or None for a file that carries no notice of its own (data, images,
    PDFs, third-party files, archived run files)."""
    if path.startswith(EXEMPT):
        return None
    if path in PLAIN_LEGAL:
        return "legal"
    name = path.rsplit("/", 1)[-1]
    if name.endswith(".md") or name in MARKDOWN_NAMES:
        return "md"
    if name in BY_NAME:
        return BY_NAME[name]
    suffix = "." + name.rsplit(".", 1)[-1] if "." in name[1:] else ""
    if suffix in BY_SUFFIX:
        return BY_SUFFIX[suffix]
    if text is not None and text.startswith("#!"):
        return HASH
    return None


# ---------------------------------------------------------------- Markdown pages

def _flat(s: str) -> str:
    s = re.sub(r"[*_`>]", " ", s.lower())
    return re.sub(r"\s+", " ", s)


def _legal_paragraph(par: list[str]) -> bool:
    t = _flat(" ".join(par))
    if "omni-compass llc" not in t and "spdx-license-identifier" not in t:
        return False
    return any(h in t for h in ("evaluation and Simulation use only", "enterprise license", "all rights reserved",
                                "spdx-license-identifier", "proprietary") + RETIRED)


def _rstrip_blank(lines: list[str]) -> list[str]:
    lines = list(lines)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def _lstrip_blank(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    return lines[i:]


def _drop_top(body: list[str], limit: int = 40) -> tuple[list[str], list[list[str]]]:
    """The page without the notice paragraphs (block quotes that read as a notice) among its first lines; and what was cut.
    Only the notice goes, with the one blank line after it (and a rule the cut left directly under another rule); every
    other line of the page stays exactly as it was."""
    out, cut, i, n = [], [], 0, len(body)
    while i < n:
        if i < limit and body[i].lstrip().startswith(">"):
            j = i
            while j < n and body[j].strip() and body[j].lstrip().startswith(">"):
                j += 1
            if not _legal_paragraph(body[i:j]):
                out.extend(body[i:j])
                i = j
                continue
            cut.append(body[i:j])
            if j < n and not body[j].strip():
                j += 1
            if j < n and body[j].strip() == "---" and next((x.strip() for x in reversed(out) if x.strip()), None) == "---":
                j += 1
                if j < n and not body[j].strip():
                    j += 1
            i = j
            continue
        out.append(body[i])
        i += 1
    return out, cut


def _drop_end(body: list[str]) -> tuple[list[str], list[list[str]]]:
    """The page without its closing notice paragraphs (and the rule above them); and what was cut."""
    b, cut, removed = list(body), [], False
    while True:
        b = _rstrip_blank(b)
        if not b:
            return b, cut
        i = len(b) - 1
        while i > 0 and b[i - 1].strip():
            i -= 1
        par = b[i:]
        italic = par[0].lstrip().startswith("*") and par[-1].rstrip().endswith("*")
        quote = all(x.lstrip().startswith(">") for x in par)
        if (italic or quote) and _legal_paragraph(par):
            cut.append(par)
            b, removed = b[:i], True
            continue
        if removed and len(par) == 1 and par[0].strip() == "---":
            b = b[:i]
            continue
        return b, cut


def normalize_markdown(text: str) -> tuple[str, list[list[str]]]:
    """A page with the one notice under its title (or at its top) and again at its end, every earlier notice paragraph
    removed and every older filing sentence in the founder's wording; and the paragraphs that were cut."""
    text = OLD_FILED.sub("All patents, copyrights and trademarks", text)
    lines = text.split("\n")
    start = 0
    if lines and lines[0].strip() == "---":                   # front matter (an issue template) stays first
        for j in range(1, min(len(lines), 80)):
            if lines[j].strip() == "---":
                start = j + 1
                break
    head, body = lines[:start], lines[start:]
    body, cut_top = _drop_top(body)
    body, cut_end = _drop_end(body)
    i = 0
    while i < len(body) and not body[i].strip():
        i += 1
    if i < len(body) and re.match(r"#{1,6}\s", body[i]):
        title, rest = body[i:i + 1], body[i + 1:]
    else:
        title, rest = [], body[i:]
    rest = _rstrip_blank(_lstrip_blank(rest))
    out = head + title + ([""] if title else []) + [f"> {TOP}", ""] + rest
    out = _rstrip_blank(out) + ["", "---", "", f"*{NOTICE}*"]
    return "\n".join(out) + "\n", cut_top + cut_end


def stamp(lines):
    """A generated report's lines with the notice under its title and again at its end (every earlier notice replaced)."""
    text, _ = normalize_markdown("\n".join(lines))
    return text.rstrip("\n").split("\n")


# ---------------------------------------------------------------- source headers

def _legal_comment(line: str, c: str) -> bool:
    t = line.strip()[len(c):].strip().lower()
    return any(h in t for h in ("spdx-", "copyright", "evaluation and simulation", "enterprise license", "see license",
                                "all rights reserved", "all patents", "omni-compass.com", "monetization or other use") + RETIRED)


def normalize_header(text: str, c: str) -> str:
    """The file with the one header after its shebang (and any encoding or syntax line), replacing the earlier header."""
    text = OLD_FILED.sub("All patents, copyrights and trademarks", text)
    lines = text.split("\n")
    i = 1 if lines and lines[0].startswith("#!") else 0
    while i < min(len(lines), 3) and re.match(r"#.*(coding[:=]|syntax=|escape=)", lines[i]):
        i += 1
    pre, found = lines[:i], None
    for k in range(i, min(i + 4, len(lines))):
        if lines[k].lstrip().startswith(c) and "SPDX-License-Identifier: LicenseRef-OmniCompass" in lines[k]:
            found = k
            break
    new_header = [f"{c} {h}" for h in HEADER]
    if found is None:
        return "\n".join(pre + new_header + lines[i:])
    end = found + 1
    while end < len(lines) and lines[end].lstrip().startswith(c) and _legal_comment(lines[end], c):
        end += 1
    return "\n".join(pre + lines[i:found] + new_header + lines[end:])


# ---------------------------------------------------------------- workflows

def _yaml():
    import yaml
    return yaml


def _workflow_plan(text: str):
    """Where the notice goes in one workflow: (insertions as [(line, [lines])], the job that hands out the legal files)."""
    yaml = _yaml()
    node = yaml.compose(text)
    lines = text.split("\n")
    data = yaml.safe_load(text)
    ins = []
    keys = {k.value: (k, v) for k, v in node.value}
    if "env" in keys:
        k, v = keys["env"]
        if not isinstance(v, yaml.MappingNode) or v.flow_style:
            raise ValueError("a top-level env that is not a block mapping")
        names = [kk.value for kk, _ in v.value]
        if "OMNI_NOTICE" not in names:
            first = v.value[0][0]
            ins.append((first.start_mark.line, [" " * first.start_mark.column + _notice_env()]))
    else:
        jobs_key = keys["jobs"][0]
        ins.append((jobs_key.start_mark.line, ["env:", "  " + _notice_env()]))
    jobs = keys["jobs"][1]
    upload_jobs = {}
    for jk, jv in jobs.value:
        jd = data["jobs"][jk.value]
        if any(str(s.get("uses", "")).startswith("actions/upload-artifact") and (s.get("with") or {}).get("name") != LEGAL_ARTIFACT
               for s in jd.get("steps") or []):
            upload_jobs[jk.value] = jd
    needed = set()
    for jd in upload_jobs.values():
        n = jd.get("needs") or []
        needed |= set([n] if isinstance(n, str) else n)
    final = [j for j in upload_jobs if j not in needed]
    for jk, jv in jobs.value:
        jd = data["jobs"][jk.value]
        steps_node = dict((kk.value, vv) for kk, vv in jv.value).get("steps")
        if steps_node is None or not steps_node.value:
            continue
        names = [str(s.get("name", "")) for s in jd["steps"]]
        first = steps_node.value[0]
        first_line = first.start_mark.line
        dash = lines[first_line].index("-")
        ind = " " * dash
        if names[0] != START_STEP:
            ins.append((first_line, [
                f"{ind}- name: {START_STEP}",
                f"{ind}  run: printf '> %s\\n\\n' \"$OMNI_NOTICE\" >> \"$GITHUB_STEP_SUMMARY\""]))
        # the steps end at the first line, after the first step, that is neither inside a step (deeper than the dash) nor a
        # new step at the dash; blank lines and comments at or left of the dash are read through
        last_content = first_line
        for k in range(first_line + 1, len(lines)):
            ln = lines[k]
            if not ln.strip():
                continue
            indent = len(ln) - len(ln.lstrip())
            if indent > dash or (indent == dash and ln.lstrip().startswith("- ")):
                last_content = k
                continue
            if ln.lstrip().startswith("#"):
                continue
            break
        end_line = last_content + 1
        tail = []
        if jk.value in final and LEGAL_ARTIFACT not in "\n".join(lines):
            cond = "always() && strategy.job-index == 0" if jd.get("strategy") else "always()"
            tail += [f"{ind}- name: Legal files beside the files this run hands out",
                     f"{ind}  if: {cond}",
                     f"{ind}  uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4",
                     f"{ind}  with:",
                     f"{ind}    path: _legal",
                     f"{ind}    sparse-checkout-cone-mode: false",
                     f"{ind}    sparse-checkout: |"] + [f"{ind}      {f}" for f in BUNDLE] + [
                     f"{ind}- name: Legal notice handed out with this run's files",
                     f"{ind}  if: {cond}",
                     f"{ind}  uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4",
                     f"{ind}  with:",
                     f"{ind}    name: {LEGAL_ARTIFACT}",
                     f"{ind}    overwrite: true",
                     f"{ind}    path: |"] + [f"{ind}      _legal/{f}" for f in BUNDLE]
        if names[-1] != END_STEP:
            tail += [f"{ind}- name: {END_STEP}",
                     f"{ind}  if: always()",
                     f"{ind}  run: printf '\\n---\\n\\n*%s*\\n' \"$OMNI_NOTICE\" >> \"$GITHUB_STEP_SUMMARY\""]
        if tail:
            ins.append((end_line, tail))
    return ins, final


def _notice_env() -> str:
    return "OMNI_NOTICE: '" + NOTICE.replace("'", "''") + "'"


def fix_workflow(text: str) -> str:
    """A workflow whose every job opens and closes its report with the notice, whose final job hands out the legal files,
    and whose notice text is the one wording. The steps it already had are kept exactly."""
    yaml = _yaml()
    before = yaml.safe_load(text)
    text = re.sub(r"(?m)^(\s*)OMNI_NOTICE: '.*'$", lambda m: m.group(1) + _notice_env(), text)
    ins, _ = _workflow_plan(text)
    lines = text.split("\n")
    for line, new in sorted(ins, key=lambda x: x[0], reverse=True):
        lines[line:line] = new
    out = "\n".join(lines)
    after = yaml.safe_load(out)
    for jn, jd in (before.get("jobs") or {}).items():
        old = [s for s in jd.get("steps") or []]
        new = [s for s in after["jobs"][jn].get("steps") or [] if str(s.get("name", "")) not in
               (START_STEP, END_STEP, "Legal files beside the files this run hands out", "Legal notice handed out with this run's files")]
        old = [s for s in old if str(s.get("name", "")) not in
               (START_STEP, END_STEP, "Legal files beside the files this run hands out", "Legal notice handed out with this run's files")]
        if old != new:
            raise ValueError(f"job {jn}: its own steps would change")
    return out


def workflow_problems(text: str) -> list[str]:
    yaml = _yaml()
    d = yaml.safe_load(text)
    bad = []
    if (d.get("env") or {}).get("OMNI_NOTICE") != NOTICE:
        bad.append("its OMNI_NOTICE is missing or not the one wording")
    for jn, jd in (d.get("jobs") or {}).items():
        steps = jd.get("steps") or []
        if not steps:
            continue
        if str(steps[0].get("name", "")) != START_STEP:
            bad.append(f"job {jn} does not open its report with the notice")
        if str(steps[-1].get("name", "")) != END_STEP:
            bad.append(f"job {jn} does not close its report with the notice")
    _, final = _workflow_plan(text)
    if final and LEGAL_ARTIFACT not in text:
        bad.append("it hands out files without the legal files beside them")
    return bad


# ---------------------------------------------------------------- the check and the fix

def problems(path: str, text: str, k) -> list[str]:
    bad = []
    if OLD_FILED.search(text):
        bad.append("an older filing sentence (not 'All patents, copyrights and trademarks')")
    flat_all = _flat(text)
    gone = [r for r in RETIRED if r in flat_all]
    if gone:
        bad.append("wording retired from the notice on 10 October still stands here (" + "; ".join(gone) + ")")
    if LOWER_S in text:
        bad.append("the notice reads 'simulation' in lower case (the founder's order of 20 October: Simulation, as the LICENSE writes it)")
    if k == "md":
        lines = text.rstrip("\n").split("\n")
        top, end = _flat("\n".join(lines[:30])), _flat("\n".join(lines[-6:]))
        miss_top = [r for r in REQUIRED if r not in top]
        miss_end = [r for r in REQUIRED if r not in end]
        if miss_top:
            bad.append("no full notice at the top (missing: " + ", ".join(miss_top) + ")")
        if miss_end:
            bad.append("no full notice at the end (missing: " + ", ".join(miss_end) + ")")
    elif k in (HASH, SLASH):
        head = _flat("\n".join(text.split("\n")[:12]))
        miss = [r for r in REQUIRED + ("spdx-license-identifier: licenseref-omnicompass-evaluation-1.0",) if r not in head]
        if miss:
            bad.append("no full header (missing: " + ", ".join(miss) + ")")
        if path.startswith(".github/workflows/") and path.endswith((".yml", ".yaml")):
            bad += [f"workflow: {x}" for x in workflow_problems(text)]
    elif k == "legal":
        flat = _flat(text)
        miss = [r for r in REQUIRED if r not in flat]
        if miss:
            bad.append("missing: " + ", ".join(miss))
    return bad


def check(root: Path = ROOT) -> list[str]:
    """One line per file that lacks the notice or carries an older wording (empty when every file carries it)."""
    lock = locked(root)
    out = []
    for p in tracked(root):
        if p in lock or p.startswith(SNAPSHOTS):
            continue
        f = root / p
        if not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        k = kind(p, text)
        if k is None:
            # a file that carries no notice of its own (data, JSON, plain text, an assistant's rules file) still carries no
            # retired wording; archived run files and third-party files keep their bytes
            gone = [r for r in RETIRED if r in _flat(text)]
            if gone and not p.startswith(EXEMPT):
                out.append(f"{p}: wording retired from the notice on 10 October still stands here (" + "; ".join(gone) + ")")
            continue
        for b in problems(p, text, k):
            out.append(f"{p}: {b}")
    return out


def counts(root: Path = ROOT) -> dict:
    lock = locked(root)
    c = {"carry": 0, "locked": 0, "data": 0}
    for p in tracked(root):
        f = root / p
        if not f.is_file():
            continue
        if p in lock or p.startswith(SNAPSHOTS):
            c["locked"] += 1
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            c["data"] += 1
            continue
        c["carry" if kind(p, text) is not None else "data"] += 1
    return c


def fix(paths=None, root: Path = ROOT) -> tuple[list[str], list[str]]:
    """Writes the notice wherever it is missing or old. Returns (files changed, paragraphs cut that held no copyright line,
    for a person to read)."""
    lock = locked(root)
    changed, odd = [], []
    for p in tracked(root, others=True):
        if paths and not any(p == q or p.startswith(q.rstrip("/") + "/") for q in paths):
            continue
        if p in lock or p.startswith(SNAPSHOTS):
            continue
        f = root / p
        if not f.is_file():
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        k = kind(p, text)
        if k is None:
            continue
        new = text
        if k == "md":
            new, cut = normalize_markdown(text)
            for par in cut:
                t = _flat(" ".join(par))
                if "copyright" not in t and "©" not in " ".join(par) and "spdx" not in t:
                    odd.append(f"{p}: " + " ".join(par)[:160])
        elif k in (HASH, SLASH):
            new = normalize_header(text, k)
            if p.startswith(".github/workflows/") and p.endswith((".yml", ".yaml")):
                new = fix_workflow(new)
        elif k == "legal":
            new = OLD_FILED.sub("All patents, copyrights and trademarks", text)
        if new != text:
            f.write_text(new, encoding="utf-8")
            changed.append(p)
    return changed, odd


def bundle(dest: Path, root: Path = ROOT) -> list[Path]:
    """The legal files every export carries, copied into `dest`."""
    dest.mkdir(parents=True, exist_ok=True)
    out = []
    for name in BUNDLE:
        src = root / name
        if src.exists():
            shutil.copy2(src, dest / name)
            out.append(dest / name)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--fix", nargs="*", metavar="PATH")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--summary-end", action="store_true")
    ap.add_argument("--bundle", metavar="DIR")
    a = ap.parse_args(argv)
    if a.summary:
        print(f"> {TOP}\n")
        return 0
    if a.summary_end:
        print(f"\n---\n\n*{NOTICE}*")
        return 0
    if a.bundle:
        for p in bundle(Path(a.bundle)):
            print(p)
        return 0
    if a.fix is not None:
        changed, odd = fix(a.fix or None)
        print(f"legal notice written in {len(changed)} files")
        for x in odd:
            print(f"cut a notice paragraph without a copyright line, read it: {x}")
        return 0
    bad = check()
    c = counts()
    for x in bad:
        print(x)
    print(f"legal notice: {len(bad)} problems; {c['carry']} files carry it, {c['locked']} locked by their fingerprint until the "
          f"next engine version, {c['data']} data files covered by REUSE.toml and the LICENSE")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
