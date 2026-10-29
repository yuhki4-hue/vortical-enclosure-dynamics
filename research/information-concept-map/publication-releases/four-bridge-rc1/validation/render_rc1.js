// Four-Bridge Publication RC1 — display validation per channel (Chromium via Playwright; emulation is not a real device).
// Usage: node render_rc1.js <rc1 dir>
const { chromium, devices } = require('playwright'); const fs = require('fs'); const { execSync } = require('child_process');
const RC = process.argv[2]; const URL = 'file://' + RC + '/renderer/index.html'; const SHOT = RC + '/validation/screenshots';
fs.mkdirSync(SHOT, { recursive: true });
const js = fs.readFileSync(RC + '/renderer/data.js', 'utf8'); const D = JSON.parse(js.slice('window.FB_DATA = '.length, -2));
const K = ['R0', 'Fc', 'M1', 'C0']; const BR = Object.keys(D.br3_012_units); const R = [];
const rec = (id, channel, result, evidence) => { R.push({ id, channel, result, evidence }); console.log(id, '|', channel, '|', result, '|', evidence); };
const state = (p, sel) => p.$$eval(sel, us => us.map(u => ({ k: u.getAttribute('data-render-unit'), ja: u.querySelector('[data-part=ja]').textContent, en: u.querySelector('[data-part=en]').textContent,
  label: (u.querySelector('[data-part=label]') || {}).textContent || '', formulaSameP: !!u.querySelector('[data-part=en-wrap] [data-part=formula]'), formula: (u.querySelector('[data-part=formula]') || {}).textContent || null,
  short: u.querySelector('[data-note=short]').textContent, shortVis: u.querySelector('[data-note=short]').getClientRects().length > 0, full: u.querySelector('[data-note-text=unit]').textContent,
  shared: u.querySelector('[data-note-text=shared]') ? u.querySelector('[data-note-text=shared]').textContent : null })));
const U = k => D.units[k] || D.br3_012_units[k];
const okUnit = s => { const u = U(s.k); return s.ja === u.ja && s.en === u.gloss && s.label === (u.label || '') && s.short === u.note_short && s.full === u.note_full && s.shortVis && (u.shared ? s.shared === D.shared_note.full : s.shared === null) && (u.formula ? s.formula === u.formula && s.formulaSameP : !s.formula); };
(async () => {
  const b = await chromium.launch(); rec('ENV', 'browser', 'INFO', 'Chromium ' + b.version() + ' headless (Playwright)');
  // ---------------- Desktop
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 } }); await ctx.grantPermissions(['clipboard-read', 'clipboard-write']);
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(URL); await p.waitForSelector('[data-render-unit=C0]'); await p.screenshot({ path: SHOT + '/desktop_publication.png', fullPage: true });
  let st = await state(p, '#units [data-render-unit]');
  rec('C-DESKTOP four-bridge units', 'Desktop Chromium 1366px', st.length === 4 && st.every(okUnit) ? 'PASS' : 'FAIL', st.map(s => `${s.k}:${okUnit(s) ? 'exact' : 'MISMATCH'}`).join(' ') + ' (Japanese, label, gloss, short note visible, full note, shared note)');
  const bst = await state(p, '#br-units [data-render-unit]');
  rec('C-BR3-012 units', 'Desktop Chromium', bst.length === BR.length && bst.every(okUnit) ? 'PASS' : 'FAIL', bst.map(s => `${s.k}:${okUnit(s) ? 'exact' : 'MISMATCH'}`).join(' ') + ' (unchanged BR3-012 texts)');
  rec('C-M1-FORMULA', 'Desktop Chromium', st.find(s => s.k === 'M1').formulaSameP && st.find(s => s.k === 'M1').formula === 'Rel(d;Q|Σ,𝒟,M,τ)' ? 'PASS' : 'FAIL', 'Rel(d;Q|Σ,𝒟,M,τ) is in the same paragraph as the M1 gloss');
  const gloss = await p.evaluate(G => { const out = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) for (const g of G) if (n.nodeValue.includes(g)) { const u = n.parentElement.closest('[data-render-unit]'); out.push(!!u && !!u.querySelector('[data-part=ja]') && !!u.querySelector('[data-note=short]')); } return out; }, [...K, ...BR].map(k => U(k).gloss));
  rec('C-DESKTOP gloss never without source and note', 'Desktop Chromium', gloss.length >= 7 && gloss.every(Boolean) ? 'PASS' : 'FAIL', `${gloss.length} gloss occurrences, all inside a unit with Japanese and note`);
  // graph
  const g = await p.evaluate(() => ({ nodes: [...document.querySelectorAll('#graph [data-node]')].map(n => n.getAttribute('data-node')), edges: [...document.querySelectorAll('#graph [data-edge]')].map(e => e.getAttribute('data-edge')),
    cmp: (() => { const l = document.querySelector('#graph [data-edge="OV-L-R0-R1"] line'); return l ? { ent: l.getAttribute('data-entailment'), marker: l.getAttribute('marker-end'), text: l.parentElement.textContent } : null; })(),
    clip: (() => { const svg = document.getElementById('graph'); const vb = svg.viewBox.baseVal; return [...svg.querySelectorAll('text')].filter(t => { const bb = t.getBBox(); return bb.x < 0 || bb.y < 0 || bb.x + bb.width > vb.width || bb.y + bb.height > vb.height; }).map(t => t.textContent); })() }));
  rec('C-GRAPH publication', 'Desktop Chromium', ['R0', 'Fc', 'M1', 'C0'].every(n => g.nodes.includes(n)) && g.edges.join() === 'OV-L-R0-R1' && g.cmp.ent === 'none' && !g.cmp.marker && !/requires/i.test(g.cmp.text) && g.clip.length === 0 ? 'PASS' : 'FAIL',
    `nodes=${g.nodes.join(',')}; edges=${g.edges.join(',')}; R0–R1 entailment=${g.cmp.ent}, arrowhead=${g.cmp.marker}; text outside viewBox=${JSON.stringify(g.clip)}`);
  // legend
  const leg = await p.$$eval('#legend [data-legend]', ls => Object.fromEntries(ls.map(l => [l.getAttribute('data-legend'), l.textContent])));
  rec('C-LEGEND', 'Desktop Chromium', K.every(k => leg[k] && leg[k].includes(D.units[k].note_short) && leg[k].includes(D.units[k].label)) && leg.compare ? 'PASS' : 'FAIL', 'legend shows each unit’s Japanese label, approved label and approved short note, plus the non-asserting comparison key');
  // details sheet
  const det = [];
  for (const k of K) { await p.click(`#graph [data-node=${k}]`); await p.waitForSelector('#details:not([hidden])'); const s = (await state(p, '#details [data-render-unit]'))[0]; const fullShown = await p.$eval('#details [data-note=full]', e => !e.hidden && e.getClientRects().length > 0); det.push({ k, ok: okUnit(s) && fullShown }); await p.click('#details-close'); }
  await p.click('#graph [data-node=M1]'); await p.waitForSelector('#details:not([hidden])'); await p.screenshot({ path: SHOT + '/desktop_details_M1.png' }); await p.click('#details-close');
  rec('C-DETAILS', 'Desktop Chromium', det.every(x => x.ok) ? 'PASS' : 'FAIL', det.map(x => `${x.k}:${x.ok}`).join(' ') + ' (graph node → sheet with Japanese, gloss, full note expanded)');
  // copy
  const cp = [];
  for (const k of [...K, ...BR]) {
    await p.evaluate(k => { const en = document.querySelector(`[data-render-unit="${k}"] [data-part=en]`); const r = document.createRange(); r.selectNodeContents(en); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }, k);
    await p.keyboard.press('Control+C'); await p.waitForTimeout(120); const c1 = await p.evaluate(() => navigator.clipboard.readText());
    await p.click(`[data-render-unit="${k}"] [data-action=copy-unit]`); await p.waitForTimeout(120); const c2 = await p.evaluate(() => navigator.clipboard.readText());
    const u = U(k); cp.push({ k, sel: c1.includes(u.ja) && c1.includes(u.note_short) && c1.includes(u.gloss), btn: c2.includes(u.note_full) && (!u.shared || c2.includes(D.shared_note.full)), f: !u.formula || c1.includes(u.gloss + ' ' + u.formula) });
  }
  rec('C-COPY', 'Desktop Chromium in-page copy', cp.every(x => x.sel && x.btn && x.f) ? 'PASS' : 'FAIL', cp.map(x => `${x.k}: sel=${x.sel} btn=${x.btn} formula=${x.f}`).join('; '));
  // layer switch
  const pubT = await p.evaluate(() => ({ e1: !!document.querySelector('#graph [data-edge="E2-001"]'), banner: document.getElementById('scope-banner').textContent, recon: document.querySelectorAll('#units [data-origin^=TARGET]').length }));
  await p.click('[data-mode=reconstruction]'); await p.screenshot({ path: SHOT + '/desktop_reconstruction.png', fullPage: true });
  const recT = await p.evaluate(() => ({ e1: (document.querySelector('#graph [data-edge="E2-001"]') || {}).textContent || null, e2: !!document.querySelector('#graph [data-edge="E2-002"]'), cmp: !!document.querySelector('#graph [data-edge="OV-L-R0-R1"]'),
    banner: document.getElementById('scope-banner').textContent, flagged: [...document.querySelectorAll('#units [data-origin^=TARGET]')].every(li => /not a condition of the Japanese source/.test(li.textContent)), n: document.querySelectorAll('#units [data-origin^=TARGET]').length,
    r0sub: [...document.querySelectorAll('#graph [data-node=R0] [data-sub] tspan')].map(t => t.textContent).join(' ') }));
  await p.click('[data-mode=publication]');
  const back = await p.evaluate(() => !document.querySelector('#graph [data-edge="E2-001"]'));
  rec('C-LAYER publication ↔ reconstruction', 'Desktop Chromium', !pubT.e1 && pubT.recon === 0 && pubT.banner.includes('neither asserted nor denied') && recT.e1 && /English reconstruction/.test(recT.e1) && recT.e2 && !recT.cmp && recT.flagged && recT.n > 0 && /causal coupling/.test(recT.r0sub) && back ? 'PASS' : 'FAIL',
    `publication: E2-001 drawn=${pubT.e1}, reconstruction items shown=${pubT.recon}; reconstruction: E2-001 caption “${recT.e1}”, E2-002 drawn=${recT.e2}, R0 node “${recT.r0sub}”, ${recT.n} reconstruction items flagged=${recT.flagged}; switching back hides E2-001=${back}`);
  rec('C-DESKTOP page errors', 'Desktop Chromium', errs.length ? 'FAIL' : 'PASS', errs.join(' | ') || 'none');
  // print
  await p.emulateMedia({ media: 'print' }); await p.pdf({ path: RC + '/validation/rc1_print.pdf', format: 'A4', printBackground: true }); await p.emulateMedia({ media: 'screen' });
  const nz = s => s.replace(/\s+/g, ' ').replace(/-/g, ''); const txt = nz(execSync(`pdftotext "${RC}/validation/rc1_print.pdf" -`).toString());
  const pr = [...K, ...BR].map(k => { const u = U(k); return { k, ok: txt.includes(nz(u.note_full)) && txt.includes(nz(u.note_short)) && txt.includes(nz(u.gloss)) }; });
  rec('C-PRINT', 'Chromium print-to-PDF (A4)', pr.every(x => x.ok) && txt.includes(nz(D.shared_note.full)) && txt.includes(nz('Rel(d;Q|Σ,𝒟,M,τ)')) ? 'PASS' : 'FAIL', pr.map(x => `${x.k}:${x.ok}`).join(' ') + ' + shared note + M1 formula (whitespace/hyphen-insensitive for pdftotext wraps)');
  await ctx.close();
  // ---------------- Mobile emulation
  for (const [name, dev] of [['Pixel 7', devices['Pixel 7']], ['iPhone 13 profile (Chromium engine, not Safari)', devices['iPhone 13']]]) {
    const m = await b.newContext({ ...dev }); const mp = await m.newPage(); await mp.goto(URL); await mp.waitForSelector('[data-render-unit=C0]');
    const tag = name.split(' ')[0].toLowerCase(); await mp.screenshot({ path: `${SHOT}/mobile_${tag}_initial.png` });
    const ms = await state(mp, '[data-render-unit]');
    const lay = await mp.evaluate(() => ({ ov: document.documentElement.scrollWidth - window.innerWidth, hidden: getComputedStyle(document.getElementById('graph-area')).display === 'none' }));
    await mp.tap('#graph-toggle'); const open = await mp.evaluate(() => getComputedStyle(document.getElementById('graph-area')).display !== 'none');
    await mp.tap('#graph [data-node=R0]'); await mp.waitForSelector('#details:not([hidden])');
    const sheet = await mp.evaluate(() => { const r = document.getElementById('details').getBoundingClientRect(); return r.bottom >= window.innerHeight - 1 && r.width >= window.innerWidth - 1 && !document.querySelector('#details [data-note=full]').hidden; });
    await mp.screenshot({ path: `${SHOT}/mobile_${tag}_sheet.png` });
    rec('C-MOBILE', `Mobile Chromium emulation: ${name}`, ms.length === 7 && ms.every(okUnit) && lay.ov <= 1 && lay.hidden && open && sheet ? 'PASS' : 'FAIL',
      `7 units exact with short notes inline=${ms.every(okUnit)}; horizontal overflow=${lay.ov}px; graph hidden by default=${lay.hidden}, opens=${open}; bottom sheet with full note=${sheet}`);
    await m.close();
  }
  rec('C-SAFARI-IOS', 'Safari (macOS/iOS), iOS real device, touch-selection copy', 'NOT-TESTED', 'not available in this environment');
  rec('C-RESIDUAL', 'screenshots, share sheets, reader mode, external excerpts, screen-reader extraction', 'RESIDUAL-RISK', 'outside page control; mitigations: inline short notes, formula in gloss paragraph, C0 inline qualifier, aria-describedby, copy interception');
  await b.close(); fs.writeFileSync(RC + '/validation/render_results_rc1.json', JSON.stringify(R, null, 1));
})();
