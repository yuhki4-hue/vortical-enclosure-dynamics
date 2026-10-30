// Display checks for navigation v0.3 on a checkout of main (Chromium via Playwright; emulation is not a real device).
// Usage: node main_nav_render_check_v0.2.js <publication-releases dir>
const { chromium, devices } = require('playwright'); const fs = require('fs'); const path = require('path');
const PR = path.resolve(process.argv[2]); const NAV = 'file://' + PR + '/index_main_v0.3.html';
const RCURL = 'file://' + PR + '/four-bridge-rc1/renderer/index.html';
const R = []; const rec = (id, channel, result, evidence) => { R.push({ id, channel, result, evidence }); console.log(id, '|', channel, '|', result, '|', evidence); };
const js = fs.readFileSync(PR + '/four-bridge-rc1/renderer/data.js', 'utf8'); const D = JSON.parse(js.slice('window.FB_DATA = '.length, -2));
(async () => {
  const b = await chromium.launch(); rec('ENV', 'browser', 'INFO', 'Chromium ' + b.version() + ' headless; checkout of the PR branch via file://');
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 } }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  await p.goto(NAV);
  const nav = await p.evaluate(() => ({ status: document.querySelector('[data-testid=deploy-status]').textContent, disc: document.querySelector('[data-testid=nav-disclaimer]').textContent,
    local: [...document.querySelectorAll('[data-local-only]')].map(e => e.dataset.localOnly), links: [...document.querySelectorAll('a[data-nav-link]')].map(a => ({ id: a.dataset.navLink, href: a.getAttribute('href'), abs: a.href })) }));
  const missing = nav.links.filter(l => !fs.existsSync(decodeURIComponent(new URL(l.abs).pathname)));
  const intoAudit = nav.links.filter(l => /cross-linguistic-audit/.test(l.href));
  rec('MV-1 navigation v0.3 page', 'Desktop Chromium (file://)', nav.status === 'NOT-DEPLOYED' && /do not add, change or imply/.test(nav.disc) && !missing.length && !intoAudit.length && nav.local.includes('br3-012') ? 'PASS' : 'FAIL',
    `status=${nav.status}; ${nav.links.length} links, missing=${JSON.stringify(missing.map(m => m.href))}; links into cross-linguistic-audit=${intoAudit.length}; local-only items=${nav.local.join(',')}`);
  await p.click('a[data-nav-link=rc1]'); await p.waitForSelector('[data-render-unit=C0]'); const t1 = await p.title(); const u1 = p.url();
  await p.goBack(); await p.waitForSelector('[data-testid=deploy-status]'); const back = p.url() === NAV;
  await p.goForward(); await p.waitForSelector('[data-render-unit=C0]'); const fwd = p.url() === RCURL; await p.goBack(); await p.waitForSelector('[data-testid=deploy-status]');
  await p.click('a[data-nav-link=nav-v01]'); await p.waitForSelector('[data-testid=deploy-status]'); const v01 = p.url().endsWith('/publication-releases/index.html'); await p.goBack(); await p.waitForSelector('[data-testid=main-context]');
  rec('MV-2 links and browser back', 'Desktop Chromium', t1 === 'Four-Bridge Publication RC1' && u1 === RCURL && back && fwd && v01 ? 'PASS' : 'FAIL', `RC1 → “${t1}”, back=${back}, forward=${fwd}; v0.1 navigation opens=${v01}`);
  const texts = [];
  for (const l of nav.links.filter(x => !['rc1', 'nav-v01', 'nav-v02'].includes(x.id))) {
    try { const r = await p.goto(l.abs); texts.push({ id: l.id, ok: !!r && (r.ok() || r.status() === 0) }); }
    catch (e) { texts.push({ id: l.id, ok: /Download is starting/.test(String(e)) && fs.existsSync(decodeURIComponent(new URL(l.abs).pathname)) }); }
  }
  await p.goto(NAV);
  rec('MV-3 document links open', 'Desktop Chromium', texts.every(t => t.ok) ? 'PASS' : 'FAIL', texts.map(t => `${t.id}:${t.ok}`).join(' ') + ' (.tsv opens as a download)');
  const tn = await p.evaluate(() => { const e = document.querySelector('[data-testid=tsv-encoding-note]'); return e && e.getClientRects().length > 0 ? e.textContent : null; });
  rec('MV-8 TSV display note visible', 'Desktop Chromium', tn && /Text Encoding/.test(tn) && /iPhone or iPad/.test(tn) ? 'PASS' : 'FAIL', tn ? 'note shown: ' + tn.slice(0, 80) + '…' : 'note missing');
  rec('MV-4 page errors', 'Desktop Chromium', errs.length ? 'FAIL' : 'PASS', errs.join(' | ') || 'none');
  const lay = [];
  for (const w of [1366, 1024, 761, 760, 600, 375]) {
    await p.setViewportSize({ width: w, height: 900 }); await p.goto(NAV);
    const n = await p.evaluate(() => ({ cols: getComputedStyle(document.querySelector('.cards')).gridTemplateColumns.split(' ').length, ov: document.documentElement.scrollWidth - window.innerWidth }));
    lay.push({ w, ok: n.ov <= 1 && n.cols === (w <= 760 ? 1 : 2), n });
  }
  rec('MV-5 layout by screen width', 'Desktop Chromium viewport 1366/1024/761/760/600/375', lay.every(x => x.ok) ? 'PASS' : 'FAIL', lay.map(x => `${x.w}px: cols=${x.n.cols}, overflow=${x.n.ov}`).join('; '));
  await ctx.close();
  for (const [name, dev] of [['Pixel 7', devices['Pixel 7']], ['iPhone 13 profile (Chromium engine, not Safari)', devices['iPhone 13']]]) {
    const m = await b.newContext({ ...dev }); const mp = await m.newPage(); await mp.goto(NAV);
    const ov = await mp.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await mp.tap('a[data-nav-link=rc1]'); await mp.waitForSelector('[data-render-unit=C0]');
    const shorts = await mp.$$eval('#units [data-render-unit] [data-note=short]', es => es.map(e => ({ t: e.textContent, v: e.getClientRects().length > 0 })));
    const okShort = ['R0', 'Fc', 'M1', 'C0'].every((k, i) => shorts[i].t === D.units[k].note_short && shorts[i].v);
    await mp.tap('#graph-toggle'); await mp.tap('#graph [data-node=M1]'); await mp.waitForSelector('#details:not([hidden])');
    const sheet = await mp.$eval('#details [data-note-text=unit]', e => e.textContent);
    await mp.goBack(); const backNav = await mp.evaluate(() => !!document.querySelector('[data-testid=main-context]'));
    rec('MV-6 mobile: navigation v0.3 → RC1 → back', `Mobile Chromium emulation: ${name}`, ov <= 1 && okShort && sheet === D.units.M1.note_full && backNav ? 'PASS' : 'FAIL', `nav overflow=${ov}px; short notes exact=${okShort}; bottom sheet M1 full note exact=${sheet === D.units.M1.note_full}; back=${backNav}`);
    await m.close();
  }
  rec('MV-7 Safari / iOS real device', 'Safari (macOS/iOS), iOS device', 'NOT-TESTED', 'not available in this environment');
  await b.close(); fs.writeFileSync(PR + '/integration/main_nav_render_results_v0.3.json', JSON.stringify(R, null, 1));
})();
