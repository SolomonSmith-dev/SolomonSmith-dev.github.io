async function loadSite() {
  const res = await fetch("data/site.json");
  if (!res.ok) throw new Error("Failed to load site.json");
  return res.json();
}

function el(tag, attrs = {}, children = []) {
  const node = document.createElement(tag);
  Object.entries(attrs).forEach(([k, v]) => {
    if (k === "className") node.className = v;
    else if (k === "text") node.textContent = v;
    else if (k === "html") node.innerHTML = v;
    else node.setAttribute(k, v);
  });
  for (const child of [].concat(children)) {
    if (child == null) continue;
    node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
  }
  return node;
}

function pill(text, className = "") {
  return el("span", { className: `pill ${className}`.trim(), text });
}

function renderStats(stats) {
  const root = document.querySelector("[data-stats]");
  if (!root || !stats) return;
  const items = [
    ["Sources", stats.sources],
    ["Findings", stats.findings],
    ["Documented+", stats.documented_findings],
    ["Vendors", stats.vendors],
    ["Decision gates", stats.decision_interviews],
  ];
  root.replaceChildren(
    ...items.map(([label, value]) =>
      el("div", { className: "stat" }, [el("b", { text: String(value) }), el("span", { text: label })])
    )
  );
}

function renderFindings(findings) {
  const root = document.querySelector("[data-findings]");
  if (!root) return;
  root.replaceChildren(
    ...findings.map((f) =>
      el("article", { className: "card", id: f.id }, [
        el("div", { className: "meta" }, [
          pill(f.id),
          pill(f.claim_grade, f.claim_grade.toLowerCase()),
          pill(`Severity ${f.severity}`),
        ]),
        el("h3", { text: f.title }),
        el("p", { text: f.summary }),
        el("p", { className: "mono", text: `Evidence: ${(f.evidence_ids || []).join(", ") || "none"}` }),
      ])
    )
  );
}

function renderVendors(vendors) {
  const root = document.querySelector("[data-vendors]");
  if (!root) return;
  const list = vendors?.vendors || [];
  root.replaceChildren(
    ...list.map((v) =>
      el("article", { className: "card" }, [
        el("div", { className: "meta" }, [
          pill(v.id),
          pill(v.class),
          pill(v.confidence, v.confidence.toLowerCase()),
        ]),
        el("h3", { text: v.name }),
        el("p", { text: v.notes || "" }),
      ])
    )
  );
}

function renderDecisions(decisions) {
  const root = document.querySelector("[data-decisions]");
  if (!root) return;
  root.replaceChildren(
    ...((decisions && decisions.interviews) || []).map((d) =>
      el("article", { className: "card" }, [
        el("div", { className: "meta" }, [
          pill(d.id),
          pill(d.status, d.status),
          pill(`blocks: ${(d.blocks || []).join(", ")}`),
        ]),
        el("h3", { text: d.title }),
      ])
    )
  );
}

function renderCompletion(items) {
  const root = document.querySelector("[data-completion]");
  if (!root) return;
  root.replaceChildren(
    ...items.map((c) =>
      el("article", { className: "card" }, [
        el("div", { className: "meta" }, [pill(c.id), pill("pending", "open")]),
        el("h3", { text: c.title }),
        el("p", { text: `Done when: ${c.done_when}` }),
      ])
    )
  );
}

function renderSources(sources) {
  const root = document.querySelector("[data-sources]");
  if (!root) return;
  root.replaceChildren(
    ...sources.map((s) =>
      el("article", { className: "card" }, [
        el("div", { className: "meta" }, [pill(s.type), pill(s.retrieved_at || "")]),
        el("h3", {}, [el("a", { href: s.url, target: "_blank", rel: "noopener", text: s.title })]),
        el("p", { className: "mono", text: `${s.id} · sha256 ${String(s.sha256 || "").slice(0, 12)}…` }),
      ])
    )
  );
}

function renderMap(graph) {
  const svg = document.querySelector("#map-canvas");
  if (!svg || !graph) return;
  const nodes = graph.nodes || [];
  const edges = graph.edges || [];
  const width = svg.clientWidth || 900;
  const height = 420;
  svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
  svg.replaceChildren();

  const cols = 4;
  const positions = {};
  nodes.forEach((n, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    positions[n.id] = {
      x: 80 + col * ((width - 100) / (cols - 1 || 1)),
      y: 70 + row * 110,
    };
  });

  for (const e of edges) {
    const a = positions[e.from];
    const b = positions[e.to];
    if (!a || !b) continue;
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", a.x);
    line.setAttribute("y1", a.y);
    line.setAttribute("x2", b.x);
    line.setAttribute("y2", b.y);
    line.setAttribute("stroke", e.confidence === "Alleged" ? "#d2b56b" : "#6fbf9a");
    line.setAttribute("stroke-width", "2");
    line.setAttribute("opacity", e.confidence === "Alleged" ? "0.45" : "0.85");
    svg.appendChild(line);
  }

  for (const n of nodes) {
    const p = positions[n.id];
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", p.x);
    c.setAttribute("cy", p.y);
    c.setAttribute("r", 18);
    c.setAttribute("fill", "#171d1a");
    c.setAttribute("stroke", "#6fbf9a");
    c.setAttribute("stroke-width", "2");
    const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
    t.setAttribute("x", p.x);
    t.setAttribute("y", p.y + 36);
    t.setAttribute("text-anchor", "middle");
    t.setAttribute("fill", "#e8eee9");
    t.setAttribute("font-size", "12");
    t.textContent = n.label;
    g.appendChild(c);
    g.appendChild(t);
    svg.appendChild(g);
  }
}

function setYear() {
  const y = document.querySelector("[data-year]");
  if (y) y.textContent = String(new Date().getFullYear());
}

async function boot() {
  setYear();
  const page = document.body.dataset.page;
  try {
    const data = await loadSite();
    renderStats(data.stats);
    if (page === "home" || page === "findings") renderFindings(data.findings || []);
    if (page === "vendors") renderVendors(data.vendors);
    if (page === "methods") {
      renderDecisions(data.decisions);
      renderCompletion(data.completion_subtasks || []);
      renderSources(data.sources || []);
    }
    if (page === "map") renderMap(data.graph);
    const disc = document.querySelector("[data-disclaimer]");
    if (disc) disc.textContent = data.disclaimer;
  } catch (err) {
    console.error(err);
    const fail = document.querySelector("[data-fail]");
    if (fail) fail.textContent = "Could not load compiled site data. Run scripts/build_site_data.py.";
  }
}

boot();
