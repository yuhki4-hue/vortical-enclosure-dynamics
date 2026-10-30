// Post-integration display checks for publication-releases/ (Chromium via Playwright; emulation is not a real device).
// Usage: node nav_render_check.js <publication-releases dir>   (the dir must sit at research/information-concept-map/publication-releases)
const { chromium, devices } = require('playwright'); const fs = require('fs'); const path = require('path');
const PR = path.resolve(process.argv[2]); const NAV = 'file://' + PR + '/index.html';
const RCURL = 'file://' + PR + '/four-bridge-rc1/renderer/index.html';
const R = []; const rec = (id, channel, result, evidence) => { R.push({ id, channel, result, evidence }); console.log(id, '|', channel, '|', result, '|', evidence); };
const js = fs.readFileSync(PR + '/four-bridge-rc1/renderer/data.js', 'utf8'); const D = JSON.parse(js.slice('window.FB_DATA = '.length, -2));
(async () => {
  const b = await chromium.launch(); rec('ENV', 'browser', 'INFO', 'Chromium ' + b.version() + ' headless; pages opened from the repository copy via file://');
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 } }); const p = await ctx.newPage();
  const errs = []; p.on('pageerror', e => errs.push(String(e)));
  // local HTML: navigation page
  await p.goto(NAV);
  const nav = await p.evaluate(() => ({ status: document.querySelector('[data-testid=deploy-status]').textContent, disc: document.querySelector('[data-testid=nav-disclaimer]').textContent, links: [...document.querySelectorAll('a[data-nav-link]')].map(a => ({ id: a.dataset.navLink, href: a.getAttribute('href'), abs: a.href })) }));
  const missing = nav.links.filter(l => !fs.existsSync(decodeURIComponent(new URL(l.abs).pathname)));
  rec('N-1 local HTML: navigation page', 'Desktop Chromium (file://)', nav.status === 'NOT-DEPLOYED' && /do not add, change or imply/.test(nav.disc) && missing.length === 0 ? 'PASS' : 'FAIL', `status=${nav.status}; ${nav.links.length} navigation links, missing targets=${JSON.stringify(missing.map(m => m.href))}; disclaimer shown`);
  // links and back navigation
  await p.click('a[data-nav-link=rc1]'); await p.waitForSelector('[data-render-unit=C0]');
  const t1 = await p.title(); const u1 = p.url();
  await p.goBack(); await p.waitForSelector('[data-testid=deploy-status]'); const back1 = p.url() === NAV;
  await p.click('a[data-nav-link=br3-012]'); await p.waitForLoadState('load'); const t2 = await p.title(); const hasR4 = await p.evaluate(() => document.body.innerText.includes('R4'));
  await p.goBack(); await p.waitForSelector('[data-testid=deploy-status]'); const back2 = p.url() === NAV;
  await p.goForward(); await p.waitForLoadState('load'); const fwd = (await p.title()) === t2; await p.goBack(); await p.waitForSelector('[data-testid=deploy-status]');
  rec('N-2 links and browser back', 'Desktop Chromium', t1 === 'Four-Bridge Publication RC1' && u1 === RCURL && back1 && /BR3-012/.test(t2) && hasR4 && back2 && fwd ? 'PASS' : 'FAIL', `RC1 link → “${t1}”, back → navigation=${back1}; BR3-012 link → “${t2}”, back=${back2}, forward=${fwd}`);
  // other link targets open (md/tsv as files)
  const texts = [];
  for (const id of ['rc1-readme', 'rc1-limits', 'br3-012-readme', 'decisions-v014', 'ledger', 'report']) {
    const l = nav.links.find(x => x.id === id);
    try { const r = await p.goto(l.abs); texts.push({ id, ok: !!r && (r.ok() || r.status() === 0), how: 'opened' }); }
    catch (e) { texts.push({ id, ok: /Download is starting/.test(String(e)) && fs.existsSync(decodeURIComponent(new URL(l.abs).pathname)), how: 'download (Chromium treats .tsv as a file download)' }); }
  }
  await p.goto(NAV);
  rec('N-3 document links open', 'Desktop Chromium', texts.every(t => t.ok) ? 'PASS' : 'FAIL', texts.map(t => `${t.id}:${t.ok} (${t.how})`).join(' '));
  rec('N-4 page errors (navigation)', 'Desktop Chromium', errs.length ? 'FAIL' : 'PASS', errs.join(' | ') || 'none');
  // width-dependent layout of navigation + RC1 page
  const lay = [];
  for (const w of [1366, 1024, 761, 760, 600, 375]) {
    await p.setViewportSize({ width: w, height: 900 });
    await p.goto(NAV); const n = await p.evaluate(() => ({ cols: getComputedStyle(document.querySelector('.cards')).gridTemplateColumns.split(' ').length, ov: document.documentElement.scrollWidth - window.innerWidth }));
    await p.goto(RCURL); await p.waitForSelector('[data-render-unit=C0]');
    const r = await p.evaluate(() => ({ cols: getComputedStyle(document.getElementById('units')).gridTemplateColumns.split(' ').length, toggle: getComputedStyle(document.getElementById('graph-toggle')).display !== 'none', graph: getComputedStyle(document.getElementById('graph-area')).display !== 'none', ov: document.documentElement.scrollWidth - window.innerWidth }));
    const expectNarrow = w <= 760;
    lay.push({ w, ok: n.ov <= 1 && r.ov <= 1 && n.cols === (expectNarrow ? 1 : 2) && r.cols === (expectNarrow ? 1 : 2) && r.toggle === expectNarrow && r.graph === !expectNarrow, n, r });
  }
  rec('N-5 layout by screen width', 'Desktop Chromium viewport 1366/1024/761/760/600/375', lay.every(x => x.ok) ? 'PASS' : 'FAIL', lay.map(x => `${x.w}px: nav cols=${x.n.cols}, units cols=${x.r.cols}, graph ${x.r.graph ? 'shown' : 'behind toggle'}, overflow=${Math.max(x.n.ov, x.r.ov)}`).join('; '));
  await ctx.close();
  // mobile emulation: navigation → RC1
  for (const [name, dev] of [['Pixel 7', devices['Pixel 7']], ['iPhone 13 profile (Chromium engine, not Safari)', devices['iPhone 13']]]) {
    const m = await b.newContext({ ...dev }); const mp = await m.newPage(); await mp.goto(NAV);
    const ov = await mp.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await mp.tap('a[data-nav-link=rc1]'); await mp.waitForSelector('[data-render-unit=C0]');
    const shorts = await mp.$$eval('#units [data-render-unit] [data-note=short]', es => es.map(e => ({ t: e.textContent, v: e.getClientRects().length > 0 })));
    const okShort = ['R0', 'Fc', 'M1', 'C0'].every((k, i) => shorts[i].t === D.units[k].note_short && shorts[i].v);
    await mp.tap('#graph-toggle'); await mp.tap('#graph [data-node=Fc]'); await mp.waitForSelector('#details:not([hidden])');
    const sheet = await mp.$eval('#details [data-note-text=unit]', e => e.textContent);
    await mp.goBack(); const backNav = await mp.evaluate(() => !!document.querySelector('[data-testid=deploy-status]'));
    rec('N-6 mobile: navigation → RC1 → back', `Mobile Chromium emulation: ${name}`, ov <= 1 && okShort && sheet === D.units.Fc.note_full && backNav ? 'PASS' : 'FAIL', `nav overflow=${ov}px; RC1 short notes inline and exact=${okShort}; graph → bottom sheet full note exact=${sheet === D.units.Fc.note_full}; back to navigation=${backNav}`);
    await m.close();
  }
  rec('N-7 Safari / iOS real device', 'Safari (macOS/iOS), iOS device', 'NOT-TESTED', 'not available in this environment');
  await b.close(); fs.writeFileSync(PR + '/integration/nav_render_results.json', JSON.stringify(R, null, 1));
})();
