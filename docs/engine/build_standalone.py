# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine as one file anyone can open: docs/engine/OMNI_COMPASS_LIVE_ENGINE.html with its 21 records packed inside
it (gzip, then base64), unpacked in the browser and put back as the same <script type="application/json"> blocks, the engine
script then run unchanged. It opens from a phone, a laptop's disk or any web host (docs/live/index.html, served by GitHub
Pages from docs/); nothing is fetched but the fonts and the three manuals, which open from GitHub.

    python3 docs/engine/build_standalone.py [page] [out]
"""
import base64
import gzip
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from tools import repo  # noqa: E402  (the repository's name, written once)

PAGE = HERE / "OMNI_COMPASS_LIVE_ENGINE.html"
OUT = HERE.parent / "live" / "index.html"
MANUALS = f"{repo.URL}/blob/main/docs/"
PDFS = ("OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf", "OMNI_COMPASS_MANUAL.pdf", "OMNI_COMPASS_OWNERS_MANUAL.pdf")
LOADER = """<div id="omni-unpack" style="position:fixed;inset:auto 0 0 0;padding:10px 16px;background:#111;color:#eee;font:14px/1.5 sans-serif;z-index:99999">Opening the engine's records&hellip;</div>
<script type="application/octet-stream" id="omni-records">%s</script>
<script>
// The page's records travel packed inside this one file; they are unpacked here and put back as the same
// <script type="application/json"> blocks the repository's page carries, and the engine then runs unchanged.
(async () => {
  const note = document.getElementById("omni-unpack");
  try {
    if (typeof DecompressionStream === "undefined") throw new Error("this browser is too old to open the packed records; please open the page in a current Chrome, Edge, Safari or Firefox");
    const b = atob(document.getElementById("omni-records").textContent.trim());
    const bytes = new Uint8Array(b.length); for (let i = 0; i < b.length; i++) bytes[i] = b.charCodeAt(i);
    const text = await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
    const recs = JSON.parse(text);
    for (const [id, body] of Object.entries(recs)) { const s = document.createElement("script"); s.type = "application/json"; s.id = id; s.textContent = body; document.body.appendChild(s); }
    const s = document.createElement("script"); s.textContent = document.getElementById("omni-engine-src").textContent; document.body.appendChild(s);
    note.remove();
  } catch (e) { note.style.background = "#7a1010"; note.textContent = "The engine could not open its records: " + e.message; }
})();
</script>
"""


def build(page: str) -> str:
    blocks = {m.group(1): m.group(2) for m in re.finditer(r'<script type="application/json" id="([^"]+)">(.*?)</script>', page, re.S)}
    if not blocks:
        raise SystemExit("the page carries no records")
    p = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>\n?', "", page, flags=re.S)
    eng = max(re.finditer(r"<script(?![^>]*application/json)[^>]*>(.*?)</script>", p, re.S), key=lambda m: len(m.group(1)))
    p = p[:eng.start()] + '<script type="text/plain" id="omni-engine-src">' + eng.group(1) + "</script>" + p[eng.end():]
    for pdf in PDFS:
        p = p.replace(f'href="../{pdf}"', f'href="{MANUALS}{pdf}" target="_blank" rel="noopener"')
    # the title and description into the head, where browsers, search engines and website builders read them
    m = re.search(r'<title>.*?</title>\n<meta name="claude:viewport-fit-sides"[^>]*>\n(<meta name="description"[^>]*>\n)', p, re.S)
    if m:
        title = re.search(r"<title>.*?</title>\n", m.group(0), re.S).group(0)
        p = p[:m.start()] + p[m.end():]
        p = p.replace("</head><body>", title + m.group(1) + "</head><body>", 1)
    packed = gzip.compress(json.dumps(blocks, separators=(",", ":"), ensure_ascii=False).encode("utf-8"), 9, mtime=0)
    body = p.rstrip()
    if not body.endswith("</body></html>"):
        raise SystemExit("the page does not end with </body></html>")
    return body[:-len("</body></html>")] + LOADER % base64.b64encode(packed).decode() + "</body></html>\n"


def main(src=PAGE, out=OUT):
    src, out = pathlib.Path(src), pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(src.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"{out}: {out.stat().st_size / 1e6:.2f} MB, one file")


if __name__ == "__main__":
    main(*sys.argv[1:3])
