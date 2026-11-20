# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live page's one-press set (the founder's words of 20 November 2026: "the benchmark engine is able to run a 500 Monte
Carlo run with one click of the mouse ... with its raw data outputs and everything else like the Python gives"): the page's
own code, between its SET-FILES markers, run in node against the Python. From the same two records it writes
tools/run_reports.py's reports byte for byte (Markdown, text, the CSVs, the Word document's words, the summary's numbers);
its core summary of a set's paths is tools/core_runs.py's summary(); its zip opens with Python's own zipfile and carries
both records in the Python's fields, every run's path, every report in every form, the owners' notice at the top and the
end of each."""
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
NODE = shutil.which("node")


def port() -> str:
    """The page's exact t95 (and the functions it stands on) and its SET-FILES functions, as a node module."""
    s = PAGE.read_text(encoding="utf-8")
    a = s.index("function lgammaJS(")
    b = s.index("\n}\n", s.index("function t95(")) + 3
    blk = s[s.index("// SET-FILES-BEGIN"):s.index("// SET-FILES-UI")]
    return (s[a:b] + "\n" + blk + "\nmodule.exports={t95,sfSummary,sfDoc,sfMd,sfTxt,sfData,sfDocx,sfCoreSummary,sfZip,sfBundle,"
            "sfPaths,sfEngineRecord,sfCoreRecord,SF};\n")


def node(drive: str, inputs: dict) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "port.js").write_text(port(), encoding="utf-8")
        (t / "in.json").write_text(json.dumps(inputs), encoding="utf-8")
        (t / "drive.js").write_text("const P=require('./port.js'),fs=require('fs');const I=JSON.parse(fs.readFileSync('in.json','utf8'));"
                                    "const out={};" + drive + "fs.writeFileSync('out.json',JSON.stringify(out));", encoding="utf-8")
        subprocess.run([NODE, "drive.js"], cwd=t, check=True, capture_output=True, text=True)
        return json.loads((t / "out.json").read_text(encoding="utf-8"))


@unittest.skipUnless(NODE, "node is not on the PATH")
class PageSetFiles(unittest.TestCase):

    def test_the_page_writes_the_pythons_reports_byte_for_byte(self):
        from tools import run_reports as R
        from tools.legal import TOP, NOTICE, CLOSE
        runs, base = R.newest()
        files, blocks, S = R.texts(runs, base)
        e, c = R.load(runs, base)
        out = node("const S=P.sfSummary(I.e,I.c,P.t95);"
                   "for(const a of P.SF.AUD){const B=P.sfDoc(S,a,null);out[a+'.md']=P.sfMd(B,I.top,I.end);out[a+'.txt']=P.sfTxt(B,I.end);"
                   "const title=`The ${S.runs}-run set, base ${S.base}: ${a==='CTO'?'CTO':a[0]+a.slice(1).toLowerCase()} report`;"
                   "out[a+'.docx']=Buffer.from(P.sfDocx(B,title,S.written,I.end)).toString('base64');}"
                   "Object.assign(out,P.sfData(I.e,I.c,S,I.end,I.close));",
                   {"e": e, "c": c, "top": TOP, "end": NOTICE, "close": CLOSE})
        for name in ("ENGINEER.md", "CTO.md", "BOARD.md", "ENGINEER.txt", "CTO.txt", "BOARD.txt", "SET_ENGINE_RUNS.csv", "SET_CORE_WAYS.csv"):
            self.assertEqual(out[name], files[name], name)
        self.assertEqual(json.loads(out["SET_SUMMARY.json"]), json.loads(files["SET_SUMMARY.json"]))
        with tempfile.TemporaryDirectory() as tmp:
            for a in R.AUDIENCES:
                mine = Path(tmp) / f"page_{a}.docx"
                mine.write_bytes(__import__("base64").b64decode(out[f"{a}.docx"]))
                theirs = Path(tmp) / f"py_{a}.docx"
                R.to_docx(blocks[a], theirs, f"The {runs}-run set, base {base}: {a.title() if a != 'CTO' else 'CTO'} report", S["written"])
                self.assertEqual(R.docx_text(mine), R.docx_text(theirs), a)
                self.assertIsNone(zipfile.ZipFile(mine).testzip())

    def test_the_page_summary_of_a_sets_paths_is_the_pythons(self):
        from tools import core_runs as CR
        base, n = 1234567, 40
        runs = [CR.one(k, base) for k in range(n)]
        ways = {w: {"U": [r[w]["U"] for r in runs], "convey": [r[w]["convey"] for r in runs], "cert": [r[w]["cert"] for r in runs]} for w in CR.WAYS}
        out = node("const basin=u=>Math.abs(u-1)<=0.1?1:Math.abs(u+1)<=0.1?-1:0;out.s=P.sfCoreSummary(I.ways,20,basin);", {"ways": ways})
        self.assertEqual(out["s"], CR.summary(runs))

    def test_one_press_saves_one_zip_with_every_file(self):
        from tools import core_runs as CR, engine_runs as ER
        from tools.legal import PLAIN
        base, n = 7654321, 12
        rec = [ER.one_run(k, base) for k in range(n)]
        runs = [CR.one(k, base) for k in range(n)]
        ways = {w: {"U": [r[w]["U"] for r in runs], "convey": [r[w]["convey"] for r in runs], "cert": [r[w]["cert"] for r in runs]} for w in CR.WAYS}
        out = node("const e=P.sfEngineRecord({engine:'omni-test',runs:I.n,base:I.base,digest:'a'.repeat(64),written:'2026-11-20T00:00:00Z',receipts:I.rec});"
                   "const c=P.sfCoreRecord({runs:I.n,base:I.base,digest:'b'.repeat(64),written:'2026-11-20T00:00:00Z',summary:I.summary});"
                   "const S=P.sfSummary(e,c,P.t95);const prov={at:'2026-11-20T00:00:00Z',all_same:false,paths:P.sfPaths(I.ways,I.base,I.n)};"
                   "out.zip=Buffer.from(P.sfZip(P.sfBundle(e,c,S,prov,I.notice,'end'))).toString('base64');",
                   {"rec": rec, "ways": ways, "n": n, "base": base, "summary": CR.summary(runs), "notice": PLAIN})
        z = zipfile.ZipFile(io.BytesIO(__import__("base64").b64decode(out["zip"])))
        self.assertIsNone(z.testzip())
        d = f"OMNI_COMPASS_SET_{n}_{base}/"
        names = set(z.namelist())
        want = {f"ENGINE_RUNS_{n}_{base}.json", f"CORE_RUNS_{n}_{base}.json", f"CORE_PATHS_{n}_{base}.csv", "SET_ENGINE_RUNS.csv",
                "SET_CORE_WAYS.csv", "SET_SUMMARY.json", "README.md"} | {f"{a}{x}" for a in ("ENGINEER", "CTO", "BOARD") for x in (".md", ".txt", ".docx", ".html")}
        self.assertEqual(names, {d + w for w in want})
        e = json.loads(z.read(d + f"ENGINE_RUNS_{n}_{base}.json"))
        c = json.loads(z.read(d + f"CORE_RUNS_{n}_{base}.json"))
        for k in ("engine", "runs", "base", "jump", "generator", "decisions", "law_steps", "digest", "digest_of", "written", "receipts"):
            self.assertIn(k, e)
        for k in ("core", "runs", "base", "jump", "macro", "micro", "dt", "tol", "convey_window", "cert_window", "kp", "authority", "ways", "digest", "summary", "written"):
            self.assertIn(k, c)
        self.assertEqual(e["receipts"], rec)                       # every run's receipt, to full precision
        self.assertEqual(c["summary"], CR.summary(runs))
        paths = z.read(d + f"CORE_PATHS_{n}_{base}.csv").decode("utf-8").splitlines()
        self.assertEqual(len([p for p in paths if not p.startswith("#")]), 1 + 4 * n)      # a header, then every run in every way
        for name in names:
            if name.endswith((".md", ".txt", ".html", ".csv")) and "SET_" not in name:
                t = z.read(name).decode("utf-8")
                self.assertIn("© 2026 Dubra Software Inc. / The Omni-Compass LLC", t[:1500], name)
                self.assertIn("www.omni-compass.com", t[-1500:], name)
        board = z.read(d + "BOARD.md").decode("utf-8")
        self.assertIn(f"bash scripts/prove_runs.sh {base} {n}", board)      # a page set says where the other two digests come from

    def test_the_page_carries_the_buttons_and_wires_them(self):
        s = PAGE.read_text(encoding="utf-8")
        for i in ("ctlSet", "setRunNew", "setRunRec", "setSave", "setPdfE", "setPdfC", "setPdfB", "setNote", "setFilesRow"):
            self.assertIn(f'id="{i}"', s, i)
        self.assertIn('boot("setfSetup", () => setfSetup());', s)
        for m in ("// SET-FILES-BEGIN", "// SET-FILES-UI", "// SET-FILES-END"):
            self.assertEqual(s.count(m), 1, m)


if __name__ == "__main__":
    unittest.main()
