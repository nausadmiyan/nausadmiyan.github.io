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
     Recent publications (2-up, auto-rotating like CMRG)
     ========================= -->
<section class="nm-recent-pubs" aria-label="Recent publications">
  <h3 class="nm-recent-pubs__title">Recent publications</h3>

  <!-- EDIT THESE: titles + details -->
  <ul id="nm-pub-source" hidden>
    <li>
      <a href="https://doi.org/10.1016/j.somejournal.2025.000001">Characterization of rapid-hardening alkali-activated binders (BOFS+BFS)</a>
      <small>Ömür T., Boylu S., Cafaloma T., Miyan N., Kabay N. — Recent Advances in Science and Engineering, 2025</small>
    </li>
    <li>
      <a href="https://doi.org/10.1080/21650373.2025.2514657">Rapid-hardening mortar with BOFS: mechanics, durability, LCA</a>
      <small>Miyan N., Ömür T., Kabay N., Birol B. — Journal of Building Engineering, 2025</small>
    </li>
    <li>
      <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=orlzgpMAAAAJ&citation_for_view=orlzgpMAAAAJ:paper3">Integrating imputation + augmentation with interpretable ML</a>
      <small>Authors — Journal/Venue, 2024</small>
    </li>
    <li>
      <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=orlzgpMAAAAJ&citation_for_view=orlzgpMAAAAJ:paper4">Freeze–thaw performance of PCM-modified mortars</a>
      <small>Authors — Conference/Journal, 2024</small>
    </li>
    <!-- Add more items as needed -->
  </ul>

  <!-- Display area: 1 row, 2 columns -->
  <div class="nm-pub-grid" id="nm-pub-grid" role="list"></div>

  <!-- Inline SVG icon (book) -->
  <svg xmlns="http://www.w3.org/2000/svg" style="display:none">
    <symbol id="nm-book" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M3 5.5A2.5 2.5 0 0 1 5.5 3H21v16H6a2 2 0 0 0-2 2v-1.5A2.5 2.5 0 0 1 6.5 17H21V5H6.5A1.5 1.5 0 0 0 5 6.5V20H3V5.5z"/>
    </symbol>
  </svg>
</section>

<style>
  .nm-recent-pubs { margin: 2.5rem 0 1.25rem; }
  .nm-recent-pubs__title {
    margin: 0 0 0.75rem 0;
    font-size: 1.15rem;
    font-weight: 600;
  }
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
  .nm-pub-item svg {
    width: 18px; height: 18px; margin-top: 0.15rem; opacity: 0.9;
  }
  .nm-pub-item a { text-decoration: none; }
  .nm-pub-item a:hover, .nm-pub-item a:focus { text-decoration: underline; }
  .nm-pub-item small { display: block; font-size: 0.86rem; opacity: 0.8; }

  /* Reduced motion: disable auto-rotate */
  @media (prefers-reduced-motion: reduce) {
    .nm-pub-grid { animation: none !important; }
  }
</style>

<script>
  (function () {
    var src = document.getElementById('nm-pub-source');
    var grid = document.getElementById('nm-pub-grid');
    if (!src || !grid) return;

    var items = Array.prototype.slice.call(src.querySelectorAll('li')).map(function(li){
      var a = li.querySelector('a');
      var sm = li.querySelector('small');
      return {
        href: a ? a.getAttribute('href') : '#',
        text: a ? a.textContent : '',
        meta: sm ? sm.textContent : ''
      };
    });
    if (!items.length) return;

    function renderPair(startIdx){
      grid.innerHTML = '';
      for (var k = 0; k < 2; k++){
        var i = (startIdx + k) % items.length;
        var wrap = document.createElement('div');
        wrap.className = 'nm-pub-item';

        var icon = document.createElementNS('http://www.w3.org/2000/svg','svg');
        var use = document.createElementNS('http://www.w3.org/2000/svg','use');
        use.setAttributeNS('http://www.w3.org/1999/xlink','href','#nm-book');
        icon.appendChild(use);
        icon.setAttribute('aria-hidden','true');

        var textWrap = document.createElement('div');
        var link = document.createElement('a');
        link.href = items[i].href;
        link.textContent = items[i].text;
        var meta = document.createElement('small');
        meta.textContent = items[i].meta;

        textWrap.appendChild(link);
        if (items[i].meta) textWrap.appendChild(meta);

        wrap.appendChild(icon);
        wrap.appendChild(textWrap);
        grid.appendChild(wrap);
      }
    }

    var step = 0, delay = 3000, timer = null;
    function start(){
      if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      stop();
      timer = setInterval(function(){
        step = (step + 2) % items.length; // show next 2
        renderPair(step);
      }, delay);
    }
    function stop(){ if (timer){ clearInterval(timer); timer = null; } }

    grid.addEventListener('mouseenter', stop);
    grid.addEventListener('mouseleave', start);
    grid.addEventListener('focusin', stop);
    grid.addEventListener('focusout', start);

    renderPair(step);
    start();
  })();
</script>
