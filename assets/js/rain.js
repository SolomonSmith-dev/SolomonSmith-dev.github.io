(function () {
  "use strict";

  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { return; }

  var canvas = document.createElement("canvas");
  canvas.id = "rain";
  canvas.setAttribute("aria-hidden", "true");
  var s = canvas.style;
  s.position = "fixed";
  s.top = "0";
  s.left = "0";
  s.width = "100%";
  s.height = "100%";
  s.zIndex = "-1";
  s.pointerEvents = "none";
  document.body.appendChild(canvas);

  var ctx = canvas.getContext && canvas.getContext("2d");
  if (!ctx) { return; }

  var GLYPHS = "0123456789ABCDEFｱｲｳｴｵｶｷｸｹｺｻｼｽｾ".split("");
  var FONT_SIZE = 16;
  var columns = 0;
  var drops = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    columns = Math.floor(canvas.width / FONT_SIZE);
    drops = [];
    for (var i = 0; i < columns; i++) {
      drops[i] = Math.floor(Math.random() * (canvas.height / FONT_SIZE));
    }
  }

  var resizeTimer;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(resize, 150);
  });

  resize();

  var last = 0;
  var FRAME_MS = 55; // about 18 fps, low CPU
  var rafId = null;

  function draw(now) {
    rafId = window.requestAnimationFrame(draw);
    if (now - last < FRAME_MS) { return; }
    last = now;

    ctx.fillStyle = "rgba(10, 14, 10, 0.10)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "rgba(0, 217, 54, 0.55)";
    ctx.font = FONT_SIZE + "px monospace";

    for (var i = 0; i < drops.length; i++) {
      var ch = GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
      ctx.fillText(ch, i * FONT_SIZE, drops[i] * FONT_SIZE);
      if (drops[i] * FONT_SIZE > canvas.height && Math.random() > 0.975) {
        drops[i] = 0;
      }
      drops[i]++;
    }
  }

  function start() { if (rafId === null) { last = 0; rafId = window.requestAnimationFrame(draw); } }
  function stop() { if (rafId !== null) { window.cancelAnimationFrame(rafId); rafId = null; } }

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) { stop(); } else { start(); }
  });

  start();
})();
