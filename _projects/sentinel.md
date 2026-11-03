---
title: "Sentinel"
eyebrow: "Project &middot; Sentinel"
heading: "A security monitor for my own LAN, built so no IP, MAC or payload leaves the house."
lede: "A C++17 libpcap sensor and Suricata feed a Python shipper that runs detection rules and an isolation-forest anomaly score, then ships anonymized one-minute rollups to a Cloudflare Worker and D1 behind a private dashboard."
description: "Sentinel by Solomon Smith: home-network security monitor with a C++ libpcap sensor, Suricata, isolation-forest anomaly scoring and a Cloudflare Workers + D1 dashboard. 119 vitest, 197 pytest, 4 ctest."
order: 4
status: "In production"
live: true
stack: [C++17, libpcap, Python, scikit-learn, Suricata, TypeScript, Hono, Cloudflare Workers, D1, React]
image: /assets/img/projects/sentinel-dashboard-desktop.jpg
image_alt: "Sentinel dashboard on desktop: device list, alert feed and traffic charts from the local synthetic-data preview"
image_width: 1265
image_height: 1444
image_caption: "Desktop capture from the local synthetic-data preview, not the private production network."
links:
  - label: "Source"
    url: "https://github.com/SolomonSmith-dev/sentinel"
---

## What it does

I self-host DNS, media and an agent stack on a Debian server, and I wanted to watch that network with a tool I control. The sensor parses Ethernet, VLAN, IPv4, IPv6, TCP and UDP into 10-second per-host windows. The shipper runs flood, port-scan, new-device and geo rules plus an isolation-forest score, replaces every MAC with a salted hash and every remote address with a country code, and pushes 60-second rollups to a Worker. The dashboard is private, behind Cloudflare Access.

## Why it is hard

Real packets, not a toy feed. A spoofed-MAC flood cannot grow memory because per-host state has hard caps (4096 hosts, 1024 destinations per host) and lives for one window. A home LAN has no labels, so raw isolation-forest output is recalibrated to [0, 1] on every nightly retrain and the 0.8 alert threshold keeps its meaning. Privacy is enforced twice: the shipper refuses any batch containing an IP or MAC, and the Worker independently rejects the same with `400 pii_rejected`. D1 counts every index entry against a 100k/day write budget, so the pipeline ships rollups and skips idle devices.

## Evidence

| Number | Reproduce with |
|---|---|
| 119 passed, 5 files | `cd api && npm ci && npm test`, vitest on the Workers runtime |
| 197 passed | `cd sensor/shipper && pip install -e '.[dev]' && pytest -q tests ../suricata/test_retention.py` |
| 4 of 4 | `cmake -S sensor/capture -B build && cmake --build build -j && ctest --test-dir build` |
| 100 SYNs across 100 ports | Exact-count replay of `sensor/tests/fixtures/port_scan.pcap` |
{: .evidence}

All three suites ran on 2026-11-03 and run in CI on every push. I have no measured detection rates on real traffic yet; the ML numbers are on labelled synthetic data.
