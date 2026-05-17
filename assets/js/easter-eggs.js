(function () {
  "use strict";

  // ── Console art ──────────────────────────────────────────────────────────────
  var G = "color:#00D936;font-family:monospace";
  var D = "color:#3FB85C;font-family:monospace";
  var A = "color:#E8A05B;font-family:monospace";
  var S = "color:#5FE07F;font-family:monospace";

  console.log("%c> SOLOMON SMITH // SYSTEM LOG", G);
  console.log("%c--------------------------------------------", D);
  console.log("%c  mise en place:  done.", D);
  console.log("%c  formerly:       head chef -- dishwasher to exec kitchen, 10 yrs", D);
  console.log("%c  now:            building LLM pipelines on a server named after middle-earth.", D);
  console.log("%c--------------------------------------------", D);
  console.log("%c  stack:   Python · FastAPI · LangChain · Claude API · RAG · MCP", S);
  console.log("%c  arda:    online  [Earendil routing | Sauron executing | Balrog guarding]", A);
  console.log("%c  status:  open for full-time AI/ML roles -- January 2027", G);
  console.log("%c--------------------------------------------", D);
  console.log("%c  contact: solomonsmithdev@gmail.com", S);
  console.log("%c  hint:    press / anywhere to open the terminal", D);
  console.log("%c--------------------------------------------", D);

  // ── Navigation routes ─────────────────────────────────────────────────────────
  var ROUTES = {
    home:     "/",
    about:    "/about/",
    projects: "/projects/",
    blog:     "/blog/",
    writing:  "/blog/",
    resume:   "/resume/",
  };

  // ── Hack detection ────────────────────────────────────────────────────────────
  var HACK_PATTERNS = [
    /\bhack\b/i, /\bexploit\b/i, /\bpayload\b/i, /\binjection\b/i,
    /rm\s+-rf/i, /drop\s+table/i, /select\s+\*\s+from/i,
    /<script/i, /javascript:/i, /\bxss\b/i,
    /\/etc\/(shadow|passwd)/i,
    /\bnmap\b/i, /\bsqlmap\b/i, /\bmetasploit\b/i,
    /\bnetcat\b|\bnc\s+-[lve]/i,
    /eval\s*\(/i, /exec\s*\(/i,
    /\bshellcode\b/i, /\brootkit\b/i,
  ];

  // ── Commands ──────────────────────────────────────────────────────────────────
  var CMDS = {

    help: function () {
      return [
        "commands:",
        "",
        "  -- content --",
        "  whoami               user profile",
        "  cat bio              full bio",
        "  cat mission          engineering philosophy",
        "  cat resume           condensed resume",
        "  cat experience       work history",
        "  cat education        education",
        "  cat certifications   certifications",
        "  cat contact          contact information",
        "  cat fellowship       [REDACTED]",
        "",
        "  -- browse --",
        "  ls                   list directory",
        "  ls projects          project index",
        "  ls skills            skill manifest",
        "  ls writing           recent posts",
        "",
        "  -- navigate --",
        "  open <page>          go to: about, projects, blog, resume, home",
        "  cd <page>            alias for open",
        "",
        "  -- system --",
        "  neofetch             system info",
        "  env                  environment variables",
        "  man solomon          manual page",
        "  history              command history",
        "  sudo hire-me         initiate offer sequence",
        "  clear                clear terminal",
        "",
        "  normies: type \"open about\" to see the full site.",
      ].join("\n");
    },

    whoami: function () {
      return [
        "USER:      Solomon Smith",
        "TITLE:     AI / ML Engineer",
        "ORIGIN:",
        "  dishwasher > line cook > sous chef > chef de cuisine > head chef",
        "  > CS degree > AI engineer.",
        "  same mise en place. different kitchen.",
        "",
        "LOCATION:  Montclair, CA. remote or relocation.",
        "AVAILABLE: January 2027",
      ].join("\n");
    },

    "cat bio": function () {
      return [
        "BIO",
        "",
        "  I spent over a decade in professional kitchens before this, working",
        "  my way from dishwasher to Head Chef across high-volume operations.",
        "  Long shifts, narrow margins for error, constant team coordination.",
        "  That taught me how to ship under pressure, diagnose what is breaking",
        "  in real time, and refine a system until it holds.",
        "",
        "  Now I am a CS senior at CSU San Bernardino, focused on AI/ML",
        "  engineering, backend systems, and applied LLM development.",
        "  What I care about is the systems side of AI: RAG pipelines,",
        "  multi-agent infrastructure, and the production hardening that turns",
        "  a working notebook into something a team can run.",
      ].join("\n");
    },

    "cat mission": function () {
      return [
        "MISSION",
        "",
        "  Production AI systems built to hold.",
        "",
        "  I came up in kitchens. You learn fast that mise en place is not",
        "  optional -- everything prepped, in position, before service starts.",
        "  No scrambling at 7pm. That discipline runs through everything I build.",
        "",
        "  Current focus: RAG pipelines, multi-agent infrastructure, and the",
        "  evaluation harnesses that tell you whether a system is actually",
        "  working. Not vibes. Numbers.",
        "",
        "  The ARDA system on my home server (Earendil, Sauron, Morgoth,",
        "  Balrog, Tom Bombadil) exists because I wanted to understand what",
        "  breaks when you run agents at 24/7 production load.",
        "  A lot breaks. I documented it.",
        "",
        '  "Not all those who wander are lost." -- Tolkien',
        "  (some of them are building agent infrastructure.)",
      ].join("\n");
    },

    "cat resume": function () {
      return [
        "RESUME: Solomon Smith",
        "--------------------------------------------",
        "",
        "SUMMARY",
        "  CS senior at CSU San Bernardino. Over a decade in professional",
        "  kitchens before pivoting into engineering. Building LLM pipelines,",
        "  RAG systems, and multi-agent infrastructure.",
        "  Targeting full-time AI/ML engineering roles starting January 2027.",
        "",
        "EXPERIENCE",
        "  Software Engineering Intern, Recursa AI        Dec 2025 - Mar 2026",
        "    RAG over legal corpus. 4s -> sub-600ms latency.",
        "    Caught 12% hallucination regression before release.",
        "    200K+ documents at 99%+ extraction accuracy.",
        "",
        "  Full-Stack Developer Intern, RideSplits        Jun 2025 - Sep 2025",
        "    Firebase Auth migration (60% fewer auth bugs).",
        "    Stripe Connect, MySQL migrations, Socket.IO.",
        "",
        "  Student Admin Asst, OSRI, CSUSB                Feb 2026 - present",
        "",
        "  IT Student Assistant, Cañada College           Jun 2023 - May 2025",
        "    20% reliability improvement. 90% tickets resolved in 24h.",
        "",
        "  Culinary Leadership (Head Chef / Chef de Cuisine)   10+ years",
        "",
        "EDUCATION",
        "  B.S. Computer Science, CSUSB        Expected December 2026",
        "  GPA: 3.14  |  Dean's List Spring 2025, Fall 2025",
        "",
        "CERTIFICATIONS",
        "  Google IT Support Specialization",
        "  Google Cloud Computing Foundations Certificate",
        "",
        "--------------------------------------------",
        'full version: type "open resume" or visit /resume/',
      ].join("\n");
    },

    "cat experience": function () {
      return [
        "EXPERIENCE",
        "",
        "  Software Engineering Intern, Recursa AI        Dec 2025 - Mar 2026",
        "    Built distributed scraping pipeline (200K+ docs, 99%+ accuracy).",
        "    Shipped RAG over legal corpus. Query latency 4s -> sub-600ms.",
        "    Evaluation harness caught 12% hallucination regression pre-release.",
        "    Python pipelines + CI schema checks cut prod incidents by 70%.",
        "",
        "  Full-Stack Developer Intern, RideSplits        Jun 2025 - Sep 2025",
        "    JWT -> Firebase Auth migration (60% fewer auth bugs).",
        "    Stripe Connect, MySQL schema migrations, Socket.IO real-time sync.",
        "    Secure document upload pipeline for ID verification (50+ users).",
        "",
        "  Student Admin Asst, OSRI, CSUSB                Feb 2026 - present",
        "    Research compliance, onboarding, event logistics.",
        "",
        "  IT Student Assistant, Cañada College           Jun 2023 - May 2025",
        "    20% reliability improvement. 90% tickets resolved in 24h.",
        "    Linux, Windows, and macOS lab systems.",
        "",
        "  Culinary Leadership                            10+ years",
        "    Dishwasher to Head Chef. Same discipline. Different kitchen.",
      ].join("\n");
    },

    "cat education": function () {
      return [
        "EDUCATION",
        "",
        "  B.S. Computer Science, CSU San Bernardino      Expected Dec 2026",
        "    GPA: 3.14",
        "    Honors: Dean's List Spring 2025, Dean's List Fall 2025",
        "    Coursework: Machine Learning, AI, Algorithms, OS, Architecture, Stats",
        "",
        "  Computer Science, Skyline College              Aug 2022 - Jun 2024",
        "",
        "  Computer Science, Butte College                2020 - 2022",
      ].join("\n");
    },

    "cat certifications": function () {
      return [
        "CERTIFICATIONS",
        "",
        "  Google IT Support Specialization",
        "  Google Cloud Computing Foundations Certificate",
      ].join("\n");
    },

    "cat certs": function () {
      return CMDS["cat certifications"]();
    },

    ls: function () {
      return [
        "/home/solomon/",
        "  projects/    skills/    writing/",
        "  bio          mission    resume",
        "  experience   education  certifications",
        "  contact      fellowship",
      ].join("\n");
    },

    "ls projects": function () {
      return [
        "/home/solomon/projects/",
        "",
        "  soc-triage-ai      [shipped]   RAG security alert triage",
        "  arda               [active]    multi-agent LLM orchestration",
        "  phishguard         [v0.2]      multi-modal phishing detector",
        "  claude-agents      [prod]      local multi-agent backend",
        "  DocMind            [active]    RAG document Q&A",
        "  adversarial-search [shipped]   minimax + alpha-beta + CSP",
        "",
        'full list: type "open projects"',
      ].join("\n");
    },

    "ls skills": function () {
      return [
        "/home/solomon/skills/",
        "",
        "  languages/   Python · TypeScript · C++ · Bash · SQL",
        "  ai-ml/       LangChain · RAG · pgvector · MCP · sentence-transformers",
        "  backend/     FastAPI · Express · PostgreSQL · Redis · Firebase",
        "  infra/       Docker · Linux · PM2 · Tailscale · GitHub Actions",
        "  kitchen/     mise en place · service under pressure · zero food waste",
      ].join("\n");
    },

    "ls writing": function () {
      return [
        "/home/solomon/writing/",
        "",
        "  2026-04-30   building-soc-triage-copilot",
        "",
        'full list: type "open blog"',
      ].join("\n");
    },

    "cat contact": function () {
      return [
        "contact:",
        "",
        "  email:     solomonsmithdev@gmail.com",
        "  github:    github.com/SolomonSmith-dev",
        "  linkedin:  linkedin.com/in/solomonsmithdev",
      ].join("\n");
    },

    "cat fellowship": function () {
      return [
        "[CLASSIFIED // ARDA SYSTEM AGENTS]",
        "",
        "  EARENDIL      router          the light-bearer. first through the gate.",
        "  SAURON        executor        gets things done. no questions asked.",
        "  MORGOTH       orchestrator    sees the whole board.",
        "  BALROG        security        you shall not pass.",
        "  TOM BOMBADIL  wildcard        answers to no one. oldest in the system.",
        "",
        '  "All we have to decide is what to do with the time that is given us."',
        "  -- Gandalf  (also: a reasonable engineering philosophy)",
      ].join("\n");
    },

    neofetch: function () {
      return [
        "",
        "  solomon@arda                          OS:      macOS Darwin 25",
        "  ------------------                    HOST:    MacBook M4 + Debian 12",
        "                                        SHELL:   zsh + starship",
        "                                        UPTIME:  ~2 yrs in production",
        "                                        ROLE:    AI / ML Engineer",
        "                                        ARDA:    5 agents online",
        "                                        STACK:   Python · FastAPI",
        "                                                 LangChain · RAG · MCP",
        "                                        CONTACT: solomonsmithdev@gmail.com",
        "                                        STATUS:  available January 2027",
        "",
      ].join("\n");
    },

    env: function () {
      return [
        "environment:",
        "",
        "  USER=solomon",
        "  ROLE=ai-ml-engineer",
        "  AVAILABLE=january-2027",
        "  LOCATION=montclair-ca",
        "  OPEN_TO=remote,relocation",
        "  CURRENT_BUILD=arda,soc-triage-ai,phishguard",
        "  STACK=python,fastapi,langchain,claude-api,rag,mcp,redis,docker",
        "  ARDA_STATUS=online",
        "  AGENTS=earendil,sauron,morgoth,balrog,tom-bombadil",
        "  CONTACT=solomonsmithdev@gmail.com",
      ].join("\n");
    },

    "man solomon": function () {
      return [
        "SOLOMON(1)               User Commands              SOLOMON(1)",
        "",
        "NAME",
        "  solomon -- AI/ML engineer, former head chef",
        "",
        "SYNOPSIS",
        "  solomon [--role ai-ml-engineer] [--available january-2027]",
        "          [--location montclair-ca] [--open-to remote,relocation]",
        "",
        "DESCRIPTION",
        "  Solomon Smith is a CS senior at California State University,",
        "  San Bernardino. Former Head Chef across multiple high-volume",
        "  restaurant operations. Currently building LLM pipelines, RAG",
        "  systems, and multi-agent infrastructure.",
        "",
        "OPTIONS",
        "  --hire        Strongly recommended.",
        "  --available   January 2027.",
        "  --location    Montclair, CA.",
        "",
        "FILES",
        "  ~/.arda/agents/   Earendil, Sauron, Morgoth, Balrog, Tom-Bombadil",
        "  ~/projects/       soc-triage-ai, phishguard, DocMind, arda ...",
        "",
        "SEE ALSO",
        "  /about/, /projects/, /resume/",
        "  github.com/SolomonSmith-dev",
        "",
        "AUTHOR",
        "  Solomon Smith <solomonsmithdev@gmail.com>",
        "",
        "SOLOMON(1)               User Commands              SOLOMON(1)",
      ].join("\n");
    },

    "sudo hire-me": function () {
      return [
        "[sudo] password for solomon: ........",
        "authenticating...",
        "",
        "offer sequence initiated.",
        "",
        "  ACTION REQUIRED: human approval needed.",
        "  contact:          solomonsmithdev@gmail.com",
        "  available:        January 2027",
        "",
        "  note: the kitchen taught me that good service is invisible.",
        "        the same is true of good systems.",
      ].join("\n");
    },

  };

  // ── Terminal UI ───────────────────────────────────────────────────────────────
  var terminal   = null;
  var termInput  = null;
  var termOutput = null;
  var termOpen   = false;
  var cmdHistory = [];
  var histIdx    = -1;

  function buildTerminal() {
    terminal = document.createElement("div");
    terminal.setAttribute("aria-label", "Easter egg terminal. Press Escape to close.");
    terminal.setAttribute("role", "complementary");
    Object.assign(terminal.style, {
      position:      "fixed",
      bottom:        "0",
      left:          "0",
      right:         "0",
      zIndex:        "200",
      background:    "#0F140F",
      borderTop:     "1px solid rgba(0,217,54,0.22)",
      fontFamily:    "monospace",
      fontSize:      "0.82rem",
      color:         "#00D936",
      maxHeight:     "340px",
      display:       "flex",
      flexDirection: "column",
      transition:    "transform 0.2s cubic-bezier(0.22,0.61,0.36,1)",
      transform:     "translateY(100%)",
    });

    var header = document.createElement("div");
    Object.assign(header.style, {
      display:        "flex",
      justifyContent: "space-between",
      alignItems:     "center",
      padding:        "0.4rem 1rem",
      borderBottom:   "1px solid rgba(0,217,54,0.22)",
      color:          "#3FB85C",
      fontSize:       "0.7rem",
      letterSpacing:  "0.18em",
    });
    var closeBtn = document.createElement("button");
    closeBtn.textContent = "[ESC] close";
    closeBtn.setAttribute("aria-label", "Close terminal");
    Object.assign(closeBtn.style, {
      background:    "transparent",
      border:        "none",
      color:         "#3FB85C",
      fontFamily:    "monospace",
      fontSize:      "0.7rem",
      letterSpacing: "0.18em",
      cursor:        "pointer",
      padding:       "0",
    });
    closeBtn.addEventListener("click", closeTerminal);
    header.appendChild(document.createTextNode("SOLOMON SMITH // TERMINAL v1.0"));
    header.appendChild(closeBtn);

    termOutput = document.createElement("div");
    termOutput.setAttribute("aria-live", "polite");
    Object.assign(termOutput.style, {
      flex:       "1",
      overflowY:  "auto",
      padding:    "0.6rem 1rem",
      color:      "#5FE07F",
      lineHeight: "1.55",
      whiteSpace: "pre-wrap",
      wordBreak:  "break-word",
    });
    termOutput.textContent = [
      'type "help" for commands.  ESC to close.',
      'normies: type "open about" to see the full site.',
      "",
    ].join("\n");

    var inputRow = document.createElement("div");
    Object.assign(inputRow.style, {
      display:    "flex",
      alignItems: "center",
      padding:    "0.4rem 1rem",
      borderTop:  "1px solid rgba(0,217,54,0.22)",
    });
    var promptLabel = document.createElement("span");
    promptLabel.textContent = "solomon@arda:~$ ";
    Object.assign(promptLabel.style, {
      color:       "#3FB85C",
      marginRight: "0.5rem",
      whiteSpace:  "nowrap",
      userSelect:  "none",
    });
    termInput = document.createElement("input");
    termInput.type = "text";
    termInput.autocomplete = "off";
    termInput.setAttribute("spellcheck", "false");
    termInput.setAttribute("aria-label", "Terminal command input");
    Object.assign(termInput.style, {
      flex:       "1",
      background: "transparent",
      border:     "none",
      outline:    "none",
      color:      "#00D936",
      fontFamily: "monospace",
      fontSize:   "0.82rem",
      caretColor: "#00D936",
    });
    termInput.addEventListener("keydown", onInputKey);

    inputRow.appendChild(promptLabel);
    inputRow.appendChild(termInput);
    terminal.appendChild(header);
    terminal.appendChild(termOutput);
    terminal.appendChild(inputRow);
    document.body.appendChild(terminal);
  }

  function onInputKey(e) {
    if (e.key === "Enter") {
      var cmd = termInput.value.trim();
      termInput.value = "";
      histIdx = -1;
      if (cmd) { cmdHistory.unshift(cmd); }
      runCommand(cmd);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (histIdx < cmdHistory.length - 1) {
        histIdx++;
        termInput.value = cmdHistory[histIdx];
      }
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (histIdx > 0) {
        histIdx--;
        termInput.value = cmdHistory[histIdx];
      } else {
        histIdx = -1;
        termInput.value = "";
      }
    }
  }

  function runCommand(raw) {
    print("solomon@arda:~$ " + raw);

    if (!raw) { return; }

    if (HACK_PATTERNS.some(function (p) { return p.test(raw); })) {
      print([
        "",
        "  [!!] BALROG DAEMON: INTRUSION DETECTED",
        "",
        "       YOU SHALL NOT PASS.",
        "",
        "  threat neutralized. incident logged.",
        "  (this is a static Jekyll site. there is nothing to hack here.)",
        "",
      ].join("\n"));
      return;
    }

    var key = raw.toLowerCase().replace(/\/+$/, "");

    if (key === "clear") {
      termOutput.textContent = "";
      return;
    }

    // history -- reads cmdHistory at call time, so handled here not in CMDS
    if (key === "history") {
      if (cmdHistory.length === 0) {
        print("\n  no commands in history yet.\n");
      } else {
        var lines = ["history:"];
        for (var i = cmdHistory.length - 1; i >= 0; i--) {
          lines.push("  [" + (cmdHistory.length - 1 - i) + "]  " + cmdHistory[i]);
        }
        print("\n" + lines.join("\n") + "\n");
      }
      return;
    }

    // open / cd -- argument-bearing navigation commands
    if (key.indexOf("open") === 0 || key.indexOf("cd ") === 0) {
      var dest = key.indexOf("open") === 0
        ? key.slice(4).trim()
        : key.slice(3).trim().replace(/^~\//, "");
      handleOpen(dest);
      return;
    }

    var handler = CMDS[key];
    if (handler) {
      print("\n" + (typeof handler === "function" ? handler() : handler) + "\n");
    } else {
      print('\ncommand not found: "' + raw + '". type "help" for available commands.\n');
    }
  }

  function handleOpen(dest) {
    if (!dest) {
      print('\nusage: open <page>\npages: about, projects, blog, resume, home\n');
      return;
    }
    var route = ROUTES[dest];
    if (!route) {
      print('\nunknown page: "' + dest + '". try: about, projects, blog, resume, home\n');
      return;
    }
    print('\nnavigating to ' + route + '...\n');
    setTimeout(function () { window.location.href = route; }, 800);
  }

  function print(text) {
    termOutput.textContent += text + "\n";
    termOutput.scrollTop = termOutput.scrollHeight;
  }

  function openTerminal() {
    if (!terminal) { buildTerminal(); }
    termOpen = true;
    terminal.style.transform = "translateY(0)";
    requestAnimationFrame(function () {
      setTimeout(function () { if (termInput) { termInput.focus(); } }, 220);
    });
  }

  function closeTerminal() {
    termOpen = false;
    if (terminal) { terminal.style.transform = "translateY(100%)"; }
  }

  // ── Konami overlay (DOM methods only, no innerHTML) ───────────────────────────
  function buildKonamiOverlay() {
    var overlay = document.createElement("div");
    Object.assign(overlay.style, {
      position:       "fixed",
      inset:          "0",
      zIndex:         "9999",
      display:        "flex",
      flexDirection:  "column",
      alignItems:     "center",
      justifyContent: "center",
      background:     "rgba(10,14,10,0.93)",
      fontFamily:     "monospace",
      color:          "#00D936",
      pointerEvents:  "none",
      opacity:        "1",
      transition:     "opacity 1s",
      textAlign:      "center",
      padding:        "2rem",
    });

    var tag = document.createElement("p");
    tag.textContent = "// KONAMI SEQUENCE ACCEPTED";
    Object.assign(tag.style, {
      fontSize: "0.72rem", letterSpacing: "0.22em",
      margin: "0 0 1.5rem", color: "#3FB85C",
    });

    var heading = document.createElement("p");
    heading.textContent = "ONE RING TO RULE THEM ALL";
    Object.assign(heading.style, {
      fontSize: "clamp(1.5rem,5vw,3rem)", fontWeight: "700",
      margin: "0 0 0.75rem", lineHeight: "1.15",
    });

    var sub = document.createElement("p");
    sub.textContent = "one ring to find them, one ring to bring them all, and in the darkness bind them.";
    Object.assign(sub.style, { fontSize: "1rem", margin: "0", color: "#5FE07F" });

    var hint = document.createElement("p");
    hint.textContent = "// closing in 3s";
    Object.assign(hint.style, {
      fontSize: "0.72rem", margin: "2rem 0 0",
      color: "#3FB85C", letterSpacing: "0.12em",
    });

    overlay.appendChild(tag);
    overlay.appendChild(heading);
    overlay.appendChild(sub);
    overlay.appendChild(hint);
    return overlay;
  }

  function triggerKonami() {
    var overlay = buildKonamiOverlay();
    document.body.appendChild(overlay);

    var rain = document.getElementById("rain");
    if (rain) { rain.style.cssText += ";opacity:0.9;transition:opacity 0.4s"; }

    setTimeout(function () {
      overlay.style.opacity = "0";
      if (rain) { rain.style.opacity = ""; rain.style.transition = "opacity 2s"; }
      setTimeout(function () {
        if (overlay.parentNode) { overlay.parentNode.removeChild(overlay); }
      }, 1000);
    }, 3000);
  }

  // ── Unified keydown handler ───────────────────────────────────────────────────
  var KONAMI = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
  var kIdx   = 0;

  document.addEventListener("keydown", function (e) {
    if (
      e.key === "/" && !termOpen &&
      document.activeElement.tagName !== "INPUT" &&
      document.activeElement.tagName !== "TEXTAREA"
    ) {
      e.preventDefault();
      openTerminal();
      return;
    }

    if (e.key === "Escape" && termOpen) {
      closeTerminal();
      return;
    }

    if (!termOpen) {
      if (e.keyCode === KONAMI[kIdx]) {
        kIdx++;
        if (kIdx === KONAMI.length) { kIdx = 0; triggerKonami(); }
      } else {
        kIdx = 0;
      }
    }
  });

})();
