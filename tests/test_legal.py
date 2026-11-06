# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The legal tool: one notice under every title and at every end, older notices replaced and never doubled, headers rewritten
after a shebang, every workflow job opening and closing its report with the notice while its own steps stay exactly as they
were, the final job handing out the legal papers, locked files untouched, and the export bundle complete."""
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import legal  # noqa: E402

OLD_TOP = ("> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not "
           "open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use requires a "
           "signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. All patent " + "applications, copyright "
           "registrations and trademark applications covering the Omni-Compass engine have been filed in the United States.")
OLD_END = ("*Evaluation and Simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use requires a signed, paid\n"
           "Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. All rights reserved.*")

WORKFLOW = """# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
name: demo
on:
  workflow_dispatch:
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs: {w: "${{ steps.w.outputs.w }}"}
    steps:
      - id: w
        run: |
          echo "w=[1,2]" >> "$GITHUB_OUTPUT"

  run:
    needs: plan
    runs-on: ubuntu-latest
    strategy:
      matrix: {w: [1, 2]}
    steps:
      - uses: actions/checkout@v4
      - run: |
          mkdir out && echo ${{ matrix.w }} > out/x.txt
          # a comment inside the script stays inside the script
      - uses: actions/upload-artifact@v4
        if: always()
        with: {name: "run-${{ matrix.w }}", path: out}
# a comment between jobs
  report:
    needs: run
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo report > REPORT.md
      - uses: actions/upload-artifact@v4
        with: {name: report, path: REPORT.md}
"""


class TestMarkdown(unittest.TestCase):
    def test_one_notice_on_top_and_at_the_end_older_ones_replaced(self):
        page = f"# Title\n\n{OLD_TOP}\n\n> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.\n\nBody text.\n\n> a quote that is content, not a notice\n\n---\n\n{OLD_END}\n"
        out, cut = legal.normalize_markdown(page)
        lines = out.split("\n")
        self.assertEqual(lines[0], "# Title")
        self.assertEqual(lines[2], f"> {legal.TOP}")
        self.assertEqual(out.count(legal.MARK), 2)                      # once at the top, once at the end
        self.assertIn("> a quote that is content, not a notice", out)
        self.assertNotIn("PROPRIETARY", out)
        self.assertTrue(out.rstrip("\n").endswith(f"*{legal.NOTICE}*"))
        self.assertEqual(len(cut), 3)
        self.assertEqual(legal.normalize_markdown(out)[0], out)          # a second pass changes nothing
        self.assertEqual(legal.problems("x.md", out, "md"), [])

    def test_front_matter_stays_first_and_a_page_without_a_title_gets_the_notice_on_top(self):
        page = "---\nname: Bug\n---\n**What you ran**\n"
        out, _ = legal.normalize_markdown(page)
        self.assertTrue(out.startswith("---\nname: Bug\n---\n> "))
        bare, _ = legal.normalize_markdown("Just text.\n")
        self.assertTrue(bare.startswith(f"> {legal.TOP}\n\nJust text."))

    def test_stamp_keeps_a_generated_report_to_one_notice(self):
        lines = legal.stamp(["# Report", "", OLD_TOP, "", "| a | b |"])
        self.assertEqual(sum(legal.MARK in x for x in lines), 2)
        self.assertEqual(legal.stamp(lines), lines)

    def test_the_older_filing_sentence_is_a_problem(self):
        page = f"# T\n\n> {legal.TOP}\n\nAll patent " + "applications, copyright registrations and trademark applications were filed.\n\n---\n\n*" + legal.NOTICE + "*\n"
        self.assertTrue(any("older filing" in p for p in legal.problems("x.md", page, "md")))
        self.assertTrue(legal.problems("y.md", "# T\n\nno notice\n", "md"))

    def test_simulation_in_lower_case_is_a_problem(self):
        # the founder's order of 20 October: Simulation with a capital S, as the LICENSE writes it; a table a bot wrote with the
        # older notice fails the check until --fix rewrites it
        good = f"# T\n\n> {legal.TOP}\n\n---\n\n*" + legal.NOTICE + "*\n"
        self.assertEqual(legal.problems("x.md", good, "md"), [])
        low = good.replace("Evaluation and Simulation", "Evaluation and " + "simulation")
        self.assertTrue(any("lower case" in p for p in legal.problems("x.md", low, "md")))

    def test_the_notice_closes_with_the_website_and_the_struck_wording_is_a_problem(self):
        # the founder's order of 10 October (night): the filing sentence, then the website, nothing after it; the two struck
        # sentences stand nowhere (spelled word by word here too, so this file carries neither)
        close = "All patents, copyrights and trademarks filed in the USA. www.omni-compass.com"
        self.assertTrue(legal.NOTICE.endswith(close) and legal.TOP.endswith(close) and legal.HEADER[-1] == close)
        for r in legal.RETIRED:
            for text in (legal.NOTICE, legal.SHORT, " ".join(legal.HEADER)):
                self.assertNotIn(r, legal._flat(text))
        struck = " ".join(("Everything", "here", "is", "subject", "to", "change", "at", "any", "time."))
        page = f"# T\n\n> {legal.TOP}\n\nBody. {struck}\n\n---\n\n*{legal.NOTICE}*\n"
        self.assertTrue(any("retired" in p for p in legal.problems("x.md", page, "md")))
        old_top = "> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. " + struck + " See LICENSE."
        fixed, _ = legal.normalize_markdown(f"# T\n\n{old_top}\n\nBody.\n")
        self.assertFalse([r for r in legal.RETIRED if r in legal._flat(fixed)])
        self.assertFalse(legal.problems("x.md", fixed, "md"))


class TestHeaders(unittest.TestCase):
    def test_header_rewritten_after_the_shebang_and_idempotent(self):
        src = "#!/usr/bin/env python3\n# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0\n# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid\n# Omni-Compass Enterprise License. See LICENSE.\n# What this script does.\nprint(1)\n"
        out = legal.normalize_header(src, "#")
        lines = out.split("\n")
        self.assertEqual(lines[0], "#!/usr/bin/env python3")
        self.assertEqual(lines[1:6], [f"# {h}" for h in legal.HEADER])
        self.assertEqual(lines[6], "# What this script does.")
        self.assertEqual(legal.normalize_header(out, "#"), out)
        self.assertEqual(legal.problems("x.py", out, "#"), [])

    def test_a_file_without_a_header_gets_one(self):
        out = legal.normalize_header("int main() { return 0; }\n", "//")
        self.assertTrue(out.startswith("// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0\n"))


class TestWorkflows(unittest.TestCase):
    def test_every_job_opens_and_closes_its_report_and_keeps_its_own_steps(self):
        out = legal.fix_workflow(legal.normalize_header(WORKFLOW, "#"))
        before, after = yaml.safe_load(WORKFLOW), yaml.safe_load(out)
        self.assertEqual(after["env"]["OMNI_NOTICE"], legal.NOTICE)
        for job in ("plan", "run", "report"):
            steps = after["jobs"][job]["steps"]
            self.assertEqual(steps[0]["name"], legal.START_STEP)
            self.assertEqual(steps[-1]["name"], legal.END_STEP)
            own = [s for s in steps if not str(s.get("name", "")).startswith("Legal ")]
            self.assertEqual(own, before["jobs"][job]["steps"])
        # the legal papers are handed out once, by the final job
        uploads = {job: [s for s in after["jobs"][job]["steps"] if (s.get("with") or {}).get("name") == legal.LEGAL_ARTIFACT]
                   for job in ("plan", "run", "report")}
        self.assertEqual([j for j, u in uploads.items() if u], ["report"])
        self.assertEqual(legal.workflow_problems(out), [])
        self.assertEqual(legal.fix_workflow(out), out)                   # a second pass changes nothing
        self.assertTrue(legal.workflow_problems(WORKFLOW))


class TestRepository(unittest.TestCase):
    def test_locked_files_are_the_fingerprinted_ones(self):
        lock = legal.locked()
        for f in ("omnicompass/core.py", "cpp/src/core.cpp", "reference/omni_compass_reference_engine.py", "fleet/harness.py"):
            self.assertIn(f, lock)
        self.assertNotIn("tools/legal.py", lock)

    def test_the_bundle_every_export_carries(self):
        with tempfile.TemporaryDirectory() as t:
            got = sorted(p.name for p in legal.bundle(Path(t)))
            self.assertEqual(got, sorted(legal.BUNDLE))


if __name__ == "__main__":
    unittest.main()
