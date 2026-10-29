/* Four-bridge render check. Every English gloss is rendered only inside a render unit that also carries
   the Japanese original, the approved label and the mandatory note. */
(function () {
  "use strict";
  var D = window.FB_DATA;
  var ORDER = ["R0", "Fc", "M1", "C0"];
  var mode = "publication";
  function U(key) { return D.units[key] || D.br3_012_units[key]; }

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "text") n.textContent = attrs[k];
      else if (k === "class") n.className = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return n;
  }
  var SVGNS = "http://www.w3.org/2000/svg";
  function svg(tag, attrs, text) {
    var n = document.createElementNS(SVGNS, tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (text != null) n.textContent = text;
    return n;
  }

  function isTarget(it) { return /^TARGET/.test(it.origin); }
  function visibleItems(u) {
    return u.items.filter(function (it) {
      if (it.item_kind !== "AUDIT") return false;
      return mode === "reconstruction" ? true : it.scope === "PUBLICATION-AND-RECONSTRUCTION";
    });
  }

  /* ---------- render unit ---------- */
  function unit(key, where) {
    var u = U(key);
    var uid = where + "-" + key.replace(/[^A-Za-z0-9-]/g, "");
    var root = el("article", { class: "render-unit", "data-render-unit": key, "aria-labelledby": uid + "-h" });
    root.appendChild(el("div", { class: "ru-head" }, [
      el("h3", { id: uid + "-h", class: "ru-id", text: u.id }),
      el("span", { class: "ru-jalabel", lang: "ja", "data-part": "ja-label", text: u.ja_label }),
      el("span", { class: "ru-label", "data-part": "label", text: u.label || "" })
    ]));
    root.appendChild(el("p", { class: "ru-ja", lang: "ja", "data-part": "ja", text: u.ja }));
    var en = el("p", { class: "ru-en", "data-part": "en-wrap", "aria-describedby": uid + "-note" });
    en.appendChild(el("span", { "data-part": "en", text: u.gloss }));
    if (u.formula) { en.appendChild(document.createTextNode(" ")); en.appendChild(el("span", { class: "ru-formula", "data-part": "formula", text: u.formula })); }
    if (key === "C0") { en.appendChild(document.createTextNode(" ")); en.appendChild(el("span", { class: "ru-qual", "data-part": "qualifier", text: "(‘passive’ ≠ ‘no pathways’; see note)" })); }
    root.appendChild(en);
    var note = el("div", { class: "ru-note", id: uid + "-note", "data-part": "note" });
    note.appendChild(el("span", { "data-note": "short", text: u.note_short }));
    var full = el("div", { class: "full", "data-note": "full", hidden: "" }, [el("p", { "data-note-text": "unit", text: u.note_full })]);
    if (u.shared) full.appendChild(el("p", { "data-note-text": "shared", text: D.shared_note.full }));
    note.appendChild(full);
    root.appendChild(note);
    if (u.cc) { root.appendChild(el("dl", { class: "ru-cc" }, [el("dt", { text: "Constitutive conditions (publication)" }), el("dd", { "data-part": "cc", text: u.cc })])); }
    if (u.items.length) {
    var det = el("details", { class: "audit" }, [el("summary", { text: mode === "publication" ? "Audit conditions (publication scope)" : "Audit conditions (all scopes)" })]);
    var ul = el("ul", { class: "audit-list" });
    visibleItems(u).forEach(function (it) {
      var li = el("li", { "data-item": it.item_id, "data-origin": it.origin, "data-scope": it.scope }, [
        el("span", { class: "badge " + (isTarget(it) ? "recon" : "source"), text: it.role }),
        el("span", { text: it.item_text })
      ]);
      if (isTarget(it)) li.appendChild(el("span", { class: "recon-flag", "data-flag": "recon", text: "English reconstruction; not a condition of the Japanese source. Status: " + it.status }));
      ul.appendChild(li);
    });
    det.appendChild(ul);
    root.appendChild(det);
    }
    var toggle = el("button", { type: "button", class: "btn", "data-action": "full-note", "aria-expanded": "false", text: "Full note" });
    toggle.addEventListener("click", function () { var h = full.hasAttribute("hidden"); if (h) full.removeAttribute("hidden"); else full.setAttribute("hidden", ""); toggle.setAttribute("aria-expanded", String(h)); });
    var copy = el("button", { type: "button", class: "btn", "data-action": "copy-unit", text: "Copy with source and note" });
    copy.addEventListener("click", function () { copyText(unitText(key, true)); });
    root.appendChild(el("div", { class: "ru-actions" }, [toggle, copy]));
    return root;
  }

  function unitText(key, withFull) {
    var u = U(key);
    var t = u.id + (u.ja_label ? " | " + u.ja_label : "") + (u.label ? " | " + u.label : "") + "\n" + u.ja + "\n" + u.gloss + (u.formula ? " " + u.formula : "") + "\n" + u.note_short;
    if (withFull) t += "\n\n" + u.note_full + (u.shared ? "\n\n" + D.shared_note.full : "");
    return t + "\n[Source: Information Concept Map (Japanese original). English: author's approved rendering; see note.]";
  }
  function copyText(t) {
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(t).catch(function () { fallback(t); }); }
    else fallback(t);
  }
  function fallback(t) {
    var ta = el("textarea"); ta.value = t; document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }
  /* Any manual copy that touches a gloss carries the Japanese original, the label and the short note with it. */
  document.addEventListener("copy", function (e) {
    var s = window.getSelection(); if (!s || s.isCollapsed) return;
    var r = s.getRangeAt(0); var keys = [];
    document.querySelectorAll("[data-render-unit]").forEach(function (u) {
      var g = u.querySelector("[data-part=en]");
      if (g && r.intersectsNode(g) && keys.indexOf(u.getAttribute("data-render-unit")) < 0) keys.push(u.getAttribute("data-render-unit"));
    });
    if (!keys.length) return;
    e.preventDefault();
    e.clipboardData.setData("text/plain", keys.map(function (k) { return unitText(k, false); }).join("\n\n"));
  });

  /* ---------- graph ---------- */
  var NODES = {
    R0: { x: 24, y: 60, sub: "相互作用", unit: true }, R1: { x: 24, y: 170, sub: "comparison node" }, R2: { x: 24, y: 280, sub: "comparison node" },
    Fc: { x: 320, y: 60, sub: "因果役割的機能", unit: true }, M1: { x: 320, y: 240, sub: "関連性", unit: true },
    C0: { x: 572, y: 60, sub: "受動的安定化", unit: true }, C1: { x: 572, y: 170, sub: "動的負帰還" }, C2: { x: 572, y: 280, sub: "特異的調節" }
  };
  var W = 164, H = 60;
  function drawGraph() {
    var g = document.getElementById("graph");
    while (g.lastChild && g.lastChild.nodeName !== "desc") g.removeChild(g.lastChild);
    var defs = svg("defs"); var m = svg("marker", { id: "arrow", viewBox: "0 0 10 10", refX: "9", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" });
    m.appendChild(svg("path", { d: "M0,0 L10,5 L0,10 z", fill: "currentColor" })); defs.appendChild(m); g.appendChild(defs);
    function group(id, x, y, w, h, label) { var gg = svg("g", { class: "group", "data-group": id }); gg.appendChild(svg("rect", { x: x, y: y, width: w, height: h, rx: 10 })); gg.appendChild(svg("text", { x: x + 8, y: y + 16 }, label)); g.appendChild(gg); }
    group("F", 306, 30, 192, 95, "F family (navigation)");
    group("C", 558, 30, 192, 315, "C family (not exclusive)");
    if (mode === "publication") group("M", 306, 210, 192, 95, "M group (Japanese map)");
    // edges
    function edge(id, from, to, cls, label, labelCls, ent, arrow, lx, ly) {
      var a = NODES[from], b = NODES[to];
      var ge = svg("g", { "data-edge": id });
      var line = svg("line", { x1: a.x + W / 2, y1: a.y + H, x2: b.x + W / 2, y2: b.y, class: "edge-line " + cls, "data-entailment": ent });
      if (arrow) { line.setAttribute("marker-end", "url(#arrow)"); line.setAttribute("x1", a.x + W / 2); line.setAttribute("y1", a.y); line.setAttribute("x2", b.x + W / 2); line.setAttribute("y2", b.y + H + 2); line.style.color = "var(--recon)"; }
      ge.appendChild(line);
      label.split("\n").forEach(function (t, i) { ge.appendChild(svg("text", { x: lx, y: ly + i * 14, class: "edge-label " + (labelCls || "") }, t)); });
      g.appendChild(ge);
    }
    if (mode === "publication") {
      edge("OV-L-R0-R1", "R0", "R1", "edge-compare", "comparison (Japanese map);\nno prerequisite asserted\nor denied", "", "none", false, 116, 135);
    } else {
      edge("E2-001", "R1", "R0", "edge-requires", "E2-001 requires\n(English reconstruction)", "recon", "necessary", true, 116, 134);
      edge("E2-002", "R2", "R1", "edge-requires", "E2-002 requires\n(English reconstruction)", "recon", "necessary", true, 116, 244);
    }
    Object.keys(NODES).forEach(function (k) {
      var n = NODES[k];
      var gn = svg("g", { class: "node" + (n.unit ? " unit" : ""), "data-node": k, tabindex: n.unit ? "0" : "-1", role: n.unit ? "button" : "img", "aria-label": k + (n.unit ? " — open unit" : "") });
      gn.appendChild(svg("rect", { x: n.x, y: n.y, width: W, height: H, rx: 8 }));
      var title = k; if (k === "M1" && mode === "reconstruction") title = "M1 → QREL";
      gn.appendChild(svg("text", { x: n.x + 10, y: n.y + 20 }, title));
      var sub = n.unit ? n.sub + " · see note" : n.sub;
      if (n.unit && mode === "reconstruction") { var rl = (D.scope_labels || []).filter(function (s) { return s.source_id.toUpperCase() === k.toUpperCase() && s.scope === "reconstruction"; })[0]; if (rl) sub = "recon.: " + rl.display_label; }
      var t = svg("text", { x: n.x + 10, y: n.y + 37, class: "sub", "data-sub": "1" });
      var lines = [], cur = "";
      sub.split(" ").forEach(function (w) { if ((cur + " " + w).trim().length > 27 && cur) { lines.push(cur); cur = w; } else { cur = (cur + " " + w).trim(); } });
      if (cur) lines.push(cur);
      lines.slice(0, 2).forEach(function (ln, i) { var ts = svg("tspan", { x: n.x + 10, dy: i ? 13 : 0 }, (i === 1 && lines.length > 2) ? ln + " …" : ln); t.appendChild(ts); });
      gn.appendChild(t);
      if (n.unit) { gn.addEventListener("click", function () { openDetails(k); }); gn.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openDetails(k); } }); }
      g.appendChild(gn);
    });
    if (mode === "reconstruction") g.appendChild(svg("text", { x: 306, y: 310, class: "edge-label recon", "data-note": "qrel-placement" }, "QREL outside M (English reconstruction only)"));
    // legend
    var lg = document.getElementById("legend"); lg.innerHTML = "";
    var ul = el("ul");
    ORDER.forEach(function (k) { ul.appendChild(el("li", { "data-legend": k }, [el("strong", { text: k + " " }), el("span", { lang: "ja", text: D.units[k].ja_label + " " }), el("span", { text: D.units[k].label }), el("div", { class: "ru-note", text: D.units[k].note_short })])); });
    if (mode === "publication") ul.appendChild(el("li", { "data-legend": "compare" }, [el("strong", { text: "Dashed green: " }), el("span", { text: D.links["OV-L-R0-R1"].mandatory_ambiguity_note_short })]));
    else ul.appendChild(el("li", { "data-legend": "requires" }, [el("strong", { text: "Solid red arrow: " }), el("span", { text: "necessary in the English reconstruction only; not a Japanese source condition." })]));
    lg.appendChild(el("h3", { text: "Legend" })); lg.appendChild(ul);
  }

  /* ---------- details sheet ---------- */
  function openDetails(k) {
    var b = document.getElementById("details-body"); b.innerHTML = ""; b.appendChild(unit(k, "details"));
    var f = b.querySelector("[data-note=full]"); f.removeAttribute("hidden");
    document.getElementById("details").hidden = false; document.getElementById("sheet-backdrop").hidden = false;
  }
  function closeDetails() { document.getElementById("details").hidden = true; document.getElementById("sheet-backdrop").hidden = true; }
  document.getElementById("details-close").addEventListener("click", closeDetails);
  document.getElementById("sheet-backdrop").addEventListener("click", closeDetails);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeDetails(); });

  /* ---------- page ---------- */
  function render() {
    var banner = document.getElementById("scope-banner");
    banner.className = "scope-banner" + (mode === "reconstruction" ? " recon" : "");
    banner.innerHTML = "";
    banner.appendChild(el("strong", { text: mode === "publication" ? "Scope: Publication layer (source-faithful)" : "Scope: Reconstruction layer (English reconstruction)" }));
    banner.appendChild(el("span", { text: mode === "publication"
      ? "Shows the Japanese original, the approved English label and gloss, and the mandatory note. Necessary-condition edges of the English reconstruction (E2-001, E2-002) are not drawn, and are neither asserted nor denied."
      : "Also shows English-reconstruction items (necessary edges, method settings, legacy clauses). They are not conditions of the Japanese source." }));
    document.getElementById("graph-title").textContent = mode === "publication" ? "Publication graph" : "Reconstruction graph";
    var us = document.getElementById("units"); us.innerHTML = "";
    ORDER.forEach(function (k) { us.appendChild(unit(k, "main")); });
    var bu = document.getElementById("br-units"); bu.innerHTML = "";
    Object.keys(D.br3_012_units).forEach(function (k) { bu.appendChild(unit(k, "br")); });
    drawGraph();
    var ap = document.getElementById("appendix"); ap.innerHTML = "";
    ["OV-E-E2-001", "OV-E-E2-002", "OV-A-QREL-PLACEMENT"].forEach(function (id) {
      var l = D.links[id];
      ap.appendChild(el("div", { class: "appendix-item", "data-appendix": id }, [el("strong", { text: l.object_id + ": " }), el("span", { text: l.selected_english_gloss_candidate + ". " }), el("span", { text: l.mandatory_ambiguity_note_full }), el("span", { class: "recon-flag", text: "Evidence: " + l.evidence_class + " · display: " + l.publication_display })]));
    });
    document.querySelectorAll(".mode-btn").forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-mode") === mode)); });
  }
  document.querySelectorAll(".mode-btn").forEach(function (b) { b.addEventListener("click", function () { mode = b.getAttribute("data-mode"); render(); }); });
  var gt = document.getElementById("graph-toggle");
  gt.addEventListener("click", function () { var a = document.getElementById("graph-area"); var open = !a.classList.contains("open"); a.classList.toggle("open", open); gt.setAttribute("aria-expanded", String(open)); gt.textContent = open ? "Hide graph" : "Show graph"; });
  document.getElementById("provenance").appendChild(el("p", { text: "Data: " + D.sources.overlay + " · " + D.sources.provenance + " · " + D.sources.draft + ". Render check only; canonical effect NONE." }));
  render();
})();
