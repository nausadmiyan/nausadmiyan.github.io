---
layout: home
title: ""
permalink: /
---

<style>
@media (min-width: 850px){
  .page-content .wrapper { max-width: 950px; }
}
</style>



### Research focus
Sustainable cementitious systems, auxetic composites, and ML-driven modeling across experiments, numerical analysis, and interpretability.

- Reproducible workflows (FE/ML pipelines)
- Design exploration & surrogate modeling
- Multiscale, multiphysics mechanics

**Scholar:** [Google Scholar](https://scholar.google.com/citations?user=orlzgpMAAAAJ&hl=en)  
**Email:** nausad_miyan@uri.edu

<!-- =========================
     Recent publications (2-up, auto-sliding)
     ========================= -->
<section class="nm-recent-pubs" aria-label="Recent publications">
  <h3 class="nm-recent-pubs__title">Recent publications</h3>

  <!-- EDIT THESE: titles + details -->
  <ul id="nm-pub-source" hidden>
    <li>
      <a href="https://doi.org/10.1016/j.jobe.2025.113616">Characterization of rapid-hardening alkali-activated binders incorporating basic oxygen furnace slag and blast furnace slag</a>
      <small>T Omur, N Miyan, H ÖZKAN, N Kabay, Journal of Building Engineering, 113616, 2025</small>
    </li>
    <li>
      <a href="https://doi.org/10.1080/21650373.2025.2514657">Assessment of a novel rapid-hardening mortar incorporating waste basic oxygen furnace slag: mechanical behavior, durability, and environmental impact</a>
      <small>T Omur, N Miyan, H Özkan, N Kabay, Journal of Sustainable Cement-Based Materials, 1-21, 2025</small>
    </li>
    <li>
      <a href="https://doi.org/10.1016/j.jobe.2024.111248">Integrating data imputation and augmentation with interpretable machine learning for efficient strength prediction of fly ash-based alkali-activated concretes</a>
      <small>N Miyan, NMA Krishnan, S Das, Journal of Building Engineering 98, 111248, 2024</small>
    </li>
    <li>
      <a href="https://doi.org/10.1016/j.conbuildmat.2024.138767">LC3 cementitious binder incorporating microencapsulated phase change materials for self-defrosting traffic surfaces</a>
      <small>N Kabay, N Miyan, T Omur, ML Nehdi, Construction and Building Materials 450, 138767, 111248, 2024</small>
    </li>
    <!-- Add more items as needed -->
  </ul>

  <!-- Slider viewport + track with two panels -->
  <div class="nm-pub-viewport" id="nm-pub-viewport">
    <div class="nm-pub-track" id="nm-pub-track">
      <div class="nm-pub-panel" id="nm-panel-a"></div>
      <div class="nm-pub-panel" id="nm-panel-b"></div>
    </div>
  </div>

  <!-- Inline SVG icon (book) -->
  <svg xmlns="http://www.w3.org/2000/svg" style="display:none">
    <symbol id="nm-book" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M3 5.5A2.5 2.5 0 0 1 5.5 3H21v16H6a2 2 0 0 0-2 2v-1.5A2.5 2.5 0 0 1 6.5 17H21V5H6.5A1.5 1.5 0 0 0 5 6.5V20H3V5.5z"/>
    </symbol>
  </svg>
</section>

<style>
  .nm-recent-pubs { margin: 2.5rem 0 1.25rem; }
  .nm-recent-pubs__title { margin: 0 0 0.75rem; font-size: 1.15rem; font-weight: 600; }

  /* Slider layout */
  .nm-pub-viewport { overflow: hidden; }
  .nm-pub-track {
    display: flex;
    width: 200%;            /* two panels side-by-side */
    transform: translateX(0%);
    transition: transform 500ms ease; /* slide speed */
    will-change: transform;
  }
  .nm-pub-panel { width: 50%; padding-right: 1rem; box-sizing: border-box; }

  /* Two-up grid inside each panel */
  .nm-pub-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.75rem 1.5rem;
    align-items: start;
  }
  .nm-pub-item {
    display: grid;
    grid-template-columns: 20px 1fr;
    gap: 0.5rem 0.6rem;
    line-height: 1.3;
  }
  .nm-pub-item svg { width: 18px; height: 18px; margin-top: 0.15rem; opacity: 0.9; }
  .nm-pub-item a { text-decoration: none; }
  .nm-pub-item a:hover, .nm-pub-item a:focus { text-decoration: underline; }
  .nm-pub-item small { display: block; font-size: 0.86rem; opacity: 0.8; }

  /* Reduced motion: no auto-slide */
  @media (prefers-reduced-motion: reduce) {
    .nm-pub-track { transition: none !important; }
  }

  /* === WIDER VIEW JUST FOR "Recent publications" ===
     Break out of the site wrapper to a wider, full-bleed container,
     but keep an internal max width so it doesn't get too wide.
  */
  .nm-recent-pubs .nm-pub-viewport {
  /* Centered container (no full-bleed) */
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;

  /* Fill available width but cap at your chosen size */
  width: 100%;
  max-width: 1800px;  /* your chosen width */
  box-sizing: border-box;
}

  /* On very large screens you can allow even more width if desired */
  @media (min-width: 1200px){
  .nm-recent-pubs .nm-pub-viewport { max-width: 1800px; }
}

  /* Optional: add a bit more breathing room between items at wide sizes */
  @media (min-width: 992px){
    .nm-recent-pubs .nm-pub-grid { gap: 1rem 2rem; }
    .nm-recent-pubs .nm-pub-item { line-height: 1.35; }
  }

  /* Optional: on narrow screens, stack items for readability */
  @media (max-width: 540px){
    .nm-recent-pubs .nm-pub-grid { grid-template-columns: 1fr; }
  }
</style>

<script>
  (function () {
    var src = document.getElementById('nm-pub-source');
    var viewport = document.getElementById('nm-pub-viewport');
    var track = document.getElementById('nm-pub-track');
    var panelA = document.getElementById('nm-panel-a');
    var panelB = document.getElementById('nm-panel-b');
    if (!src || !viewport || !track || !panelA || !panelB) return;

    // Collect items
    var items = Array.prototype.slice.call(src.querySelectorAll('li')).map(function(li){
      var a = li.querySelector('a');
      var sm = li.querySelector('small');
      return { href: a ? a.href : '#', text: a ? a.textContent : '', meta: sm ? sm.textContent : '' };
    });
    if (!items.length) return;

    function makeGrid(startIdx){
      var grid = document.createElement('div');
      grid.className = 'nm-pub-grid';
      for (var k = 0; k < 2; k++){
        var i = (startIdx + k) % items.length;
        var item = document.createElement('div');
        item.className = 'nm-pub-item';

        var icon = document.createElementNS('http://www.w3.org/2000/svg','svg');
        var use = document.createElementNS('http://www.w3.org/2000/svg','use');
        use.setAttributeNS('http://www.w3.org/1999/xlink','href','#nm-book');
        icon.appendChild(use);
        icon.setAttribute('aria-hidden','true');

        var wrap = document.createElement('div');
        var link = document.createElement('a');
        link.href = items[i].href;
        link.textContent = items[i].text;
        var meta = document.createElement('small');
        meta.textContent = items[i].meta;

        wrap.appendChild(link);
        if (items[i].meta) wrap.appendChild(meta);

        item.appendChild(icon);
        item.appendChild(wrap);
        grid.appendChild(item);
      }
      return grid;
    }

    var step = 0;
    var delay = 3000;          // stay time for each pair
    var slideMs = 500;         // must match CSS transition
    var timer = null;
    var reduceMotion = (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

    function fill(panel, startIdx){
      panel.innerHTML = '';
      panel.appendChild(makeGrid(startIdx));
    }

    function schedule(){
      if (reduceMotion) return; // no auto-slide
      stop();
      timer = setInterval(next, delay);
    }

    function stop(){
      if (timer) { clearInterval(timer); timer = null; }
    }

    function forceReflow(el){ void(el.offsetHeight); } // ensure browser applies changes

    function next(){
      // Prepare next pair in off-screen panelB
      fill(panelB, (step + 2) % items.length);

      // Slide track to show panelB
      track.style.transform = 'translateX(-50%)';

      // After slide finishes, swap content: move B into A, reset transform (no flicker)
      setTimeout(function(){
        step = (step + 2) % items.length;
        // Replace A with what was in B
        panelA.innerHTML = panelB.innerHTML;

        // Reset transform instantly (temporarily disable transition)
        var oldTransition = track.style.transition;
        track.style.transition = 'none';
        track.style.transform = 'translateX(0%)';
        forceReflow(track);                 // flush
        track.style.transition = oldTransition;

        // Prefill panelB with the next-next pair for the upcoming slide
        fill(panelB, (step + 2) % items.length);
      }, slideMs);
    }

    // Init: show first pair in A, prefill B with the next pair
    fill(panelA, step);
    fill(panelB, (step + 2) % items.length);

    // Pause on hover/focus
    viewport.addEventListener('mouseenter', stop);
    viewport.addEventListener('mouseleave', schedule);
    viewport.addEventListener('focusin', stop);
    viewport.addEventListener('focusout', schedule);

    schedule();
  })();
</script>
