// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// The live benchmark engine's acceptance run in a real browser (the solid-A directive's phase 6): load time, page errors,
// every contents link, the verdict geometry as the browser draws it, the four live words, the kill switch, the redline reflex
// running with the engine's own numbers, and the phone width. It prints one JSON object; tools/live_engine_acceptance.py
// reads it and writes docs/audit/LIVE_ENGINE_ACCEPTANCE.md. Usage: node docs/engine/accept_live_engine.js <page.html | URL>
const { chromium } = require("playwright");
const path = require("path");

(async () => {
  const target = process.argv[2] || path.join(__dirname, "OMNI_COMPASS_LIVE_ENGINE.html");
  const url = /^https?:/.test(target) ? target : "file://" + path.resolve(target);
  const out = {url, checks: {}};
  const browser = await chromium.launch();
  const errs = [], cons = [];
  const page = await browser.newPage({viewport: {width: 1366, height: 900}});
  page.on("pageerror", e => errs.push(String(e.message).slice(0, 300)));
  page.on("console", m => { if (m.type() === "error") cons.push(m.text().slice(0, 300)); });
  const t0 = Date.now();
  await page.goto(url, {waitUntil: "load", timeout: 180000});
  out.checks.load_ms = Date.now() - t0;
  await page.waitForTimeout(12000);
  const ev = (f, a) => page.evaluate(f, a).catch(e => ({error: String(e.message || e).slice(0, 300)}));
  out.checks.head = await ev(() => ({title: document.title, engine: document.documentElement.dataset.engine,
    prose: document.documentElement.dataset.prose, bytes: document.documentElement.outerHTML.length}));
  out.checks.anchors = await ev(() => {
    const ids = new Set([...document.querySelectorAll("[id]")].map(e => e.id));
    const links = [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute("href").slice(1)).filter(Boolean);
    const broken = [...new Set(links.filter(h => !ids.has(decodeURIComponent(h))))];
    return {links: links.length, broken: broken.length, sample: broken.slice(0, 12)};
  });
  out.checks.geometry = await ev(() => {
    const probe = cls => { const s = document.createElement("span"); s.className = "word " + cls; s.textContent = "X"; document.body.appendChild(s);
      const b = getComputedStyle(s, "::before"), w = getComputedStyle(s), o = {radius: b.borderRadius, transform: b.transform, clip: b.clipPath, bg: b.backgroundColor, content: b.content, pill_bg: w.backgroundColor, pill_clip: w.clipPath};
      s.remove(); return o; };
    const count = sel => document.querySelectorAll(sel).length;
    return {gain: probe("w-gain"), steady: probe("w-even"), loss: probe("w-loss"),
            drawn: {gain: count(".word.w-gain"), steady: count(".word.w-even"), loss: count(".word.w-loss")}};
  });
  out.checks.signals = await ev(() => ({words: typeof SIG_WORD !== "undefined" ? SIG_WORD : null,
    monitors: typeof MON !== "undefined" && MON.list ? MON.list.length : null,
    strips: document.querySelectorAll(".sigStrip, .sigw").length,
    redline_words_drawn: [...document.querySelectorAll(".sigw")].filter(e => /REDLINING/.test(e.textContent)).length}));
  out.checks.reflex_config = await ev(() => typeof MECH0 !== "undefined" ? MECH0.reflex : null);
  // the model runs at eight times speed under a surge (demand ×2 on a body part, both sides): then read what the immune rule did
  await ev(() => { if (typeof setSpeed === "function") setSpeed(8); if (typeof knobFault === "function") knobFault("surge"); return true; });
  await page.waitForTimeout(25000);
  out.checks.reflex_run = await ev(() => { const a = W.omniOn || W.omni; const tot = a && a.tot ? a.tot : {};
    return {t: W.t, handed_now: a && a.handed ? a.handed.size : 0, hand_backs: tot.handed || 0, stayed: tot.stayed || 0,
            immune_log: (typeof LOG !== "undefined" && LOG.rows) ? LOG.rows.filter(r => /redline reflex/.test(r.msg || r[2] || "")).length : null}; });
  // the kill switch: every Omni-Compass side hands back to native at once, and comes back on when pressed again
  out.checks.kill = await ev(async () => {
    const before = W.killed; setKill(true, "acceptance run"); await new Promise(r => setTimeout(r, 1500));
    const off = {killed: W.killed, pressed: document.getElementById("kKill").getAttribute("aria-pressed")};
    setKill(false); await new Promise(r => setTimeout(r, 1500));
    return {before, off, on_again: !W.killed};
  });
  out.checks.errors = {page_errors: errs.length, console_errors: cons.length, sample: errs.concat(cons).slice(0, 8)};
  // the phone: 390 px wide, no page wider than the screen
  const phone = await browser.newPage({viewport: {width: 390, height: 844}, deviceScaleFactor: 2, isMobile: true, hasTouch: true});
  const perrs = []; phone.on("pageerror", e => perrs.push(String(e.message).slice(0, 200)));
  await phone.goto(url, {waitUntil: "load", timeout: 180000});
  await phone.waitForTimeout(8000);
  out.checks.phone = await phone.evaluate(() => {
    const w = document.documentElement.clientWidth, sw = document.documentElement.scrollWidth;
    const wide = [...document.querySelectorAll("body *")].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.right > w + 2 && getComputedStyle(e).position !== "fixed"; })
      .slice(0, 8).map(e => (e.id ? "#" + e.id : e.tagName.toLowerCase() + (e.className && typeof e.className === "string" ? "." + e.className.split(" ")[0] : "")));
    return {client_width: w, scroll_width: sw, overflow_px: sw - w, wider_than_screen: wide};
  }).catch(e => ({error: String(e)}));
  out.checks.phone.page_errors = perrs.length;
  await browser.close();
  console.log(JSON.stringify(out));
})().catch(e => { console.log(JSON.stringify({fatal: String(e && e.stack || e).slice(0, 800)})); process.exit(1); });

// © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
// monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
