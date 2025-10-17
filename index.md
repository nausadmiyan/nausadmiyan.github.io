---
layout: home
title: ""
permalink: /
---

### Research focus
Sustainable cementitious systems, auxetic composites, and ML-driven modeling across experiments, numerical analysis, and interpretability.

- Reproducible workflows (FE/ML pipelines)
- Design exploration & surrogate modeling
- Multiscale, multiphysics mechanics

**Scholar:** [Google Scholar](https://scholar.google.com/citations?user=orlzgpMAAAAJ&hl=en)  
**Email:** nausad_miyan@uri.edu

<!-- =========================
     Recent publications (2-up, auto-rotating)
     ========================= -->
<section class="nm-recent-pubs" aria-label="Recent publications">
  <h3 class="nm-recent-pubs__title">Recent publications</h3>

  <!-- Edit this hidden list to change which papers rotate -->
  <ul id="nm-pub-source" hidden>
    <li><a href="https://doi.org/10.1016/j.somejournal.2025.000001">Characterization of rapid-hardening alkali-activated binders (BOFS+BFS)</a></li>
    <li><a href="https://doi.org/10.1080/21650373.2025.2514657">Rapid-hardening mortar with BOFS: mechanics, durability, LCA</a></li>
    <li><a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=orlzgpMAAAAJ&citation_for_view=orlzgpMAAAAJ:paper3">Integrating imputation + augmentation with interpretable ML</a></li>
    <li><a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=orlzgpMAAAAJ&citation_for_view=orlzgpMAAAAJ:paper4">Freeze–thaw performance of PCM-modified mortars</a></li>
    <!-- Add more <li><a href="URL">Paper title…</a></li> as needed -->
  </ul>

  <!-- Display area (2 columns, 1 row) -->
  <div class="nm-pub-grid" id="nm-pub-grid" role="list"></div>

  <!-- Reusable inline SVG icon (book) -->
  <svg xmlns="http://www.w3.org/2000/svg" style="display:none">
    <symbol id="nm-book" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M3 5.5A2.5 2.5 0 0 1 5.5 3H21v16H6a2 2 0 0 0-2 2v-1.5A2.5 2.5 0 0 1 6.5 17H21V5H6.5A1.5 1.5 0 0 0 5 6.5V20H3V5.5z"/>
    </symbol>
  </svg>
</section>

<style>
  .nm-recent-pubs { margin: 2.5rem 0 1rem; }
  .nm-recent-pubs__title {
    margin: 0 0 0.75rem 0;
    font-size: 1.15rem;
    font-weight: 600;
  }
  .nm-pub-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.5rem 1.25rem; /* 1 row, 2 columns; gap kept modest */
    align-items: center;
  }
  .nm-pub-item {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
    line-height: 1.3;
  }
  .nm-pub-item svg {
    width: 18px;
    height: 18px;
    flex: 0 0 18px;
    opacity: 0.85;
    margin-top: 0.05rem;
  }
  .nm-pub-item a {
    text-decoration: none;
  }
  .nm-pub-item a:hover,
  .nm-pub-item a:focus {
    text-decoration: underline;
  }

  /* Respect reduced motion: no auto-rotate */
  @media (prefers-reduced-motion: reduce) {
    .nm-pub-grid { animation: none !important; }
  }
</style>

<script>
  (function () {
    var src = document.getElementById('nm-pub-source');
    var grid = document.getElementById('nm-pub-grid');
    if (!src || !grid) return;

    // Collect links from the hidden list
    var items = Array.prototype.slice.call(src.querySelectorAll('li > a'))
      .map(function(a){ return { href: a.getAttribute('href'), text: a.textContent }; });

    if (!items.length) return;

    // Helper: render a pair (two items)
    function renderPair(idx){
      grid.innerHTML = ''; // clear
      for (var k = 0; k < 2; k++){
        var i = (idx + k) % items.length;
        var wrap = document.createElement('div');
        wrap.className = 'nm-pub-item';
        var icon = document.createElementNS('http://www.w3.org/2000/svg','svg');
        var use = document.createElementNS('http://www.w3.org/2000/svg','use');
        use.setAttributeNS('http://www.w3.org/1999/xlink','href','#nm-book');
        icon.appendChild(use);
        icon.setAttribute('aria-hidden','true');

        var link = document.createElement('a');
        link.href = items[i].href;
        link.textContent = items[i].text;
        link.setAttribute('role','listitem');

        wrap.appendChild(icon);
        wrap.appendChild(link);
        grid.appendChild(wrap);
      }
    }

    var step = 0;
    renderPair(step);

    // Auto-rotate every 3s; pause on hover/focus
    var delay = 3000;
    var timer = null;

    function start(){
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      stop();
      timer = setInterval(function(){
        step = (step + 2) % items.length; // advance by two
        renderPair(step);
      }, delay);
    }
    function stop(){ if (timer){ clearInterval(timer); timer = null; } }

    // Pause on hover/focus within the grid
    grid.addEventListener('mouseenter', stop);
    grid.addEventListener('mouseleave', start);
    grid.addEventListener('focusin', stop);
    grid.addEventListener('focusout', start);

    start();
  })();
</script>
