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

<!-- News-style bottom ticker -->
<style>
  :root { --ticker-h: 44px; --ticker-speed: 28s; }
  /* Prevent content from being covered by the fixed ticker (home page only) */
  body { padding-bottom: var(--ticker-h); }

  .nm-ticker {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    height: var(--ticker-h);
    background: rgba(0,0,0,0.85);
    color: #fff;
    font-size: 0.95rem;
    line-height: var(--ticker-h);
    z-index: 9999;
    overflow: hidden;
  }
  .nm-ticker__mask { white-space: nowrap; }
  .nm-ticker__track {
    display: inline-block;
    padding-left: 100%;
    will-change: transform;
    animation: nm-ticker-scroll var(--ticker-speed) linear infinite;
  }
  .nm-ticker:hover .nm-ticker__track { animation-play-state: paused; } /* pause on hover */
  .nm-ticker__item { display: inline; margin: 0 1rem; }
  .nm-ticker__sep { opacity: 0.6; margin: 0 0.6rem; }

  @keyframes nm-ticker-scroll {
    0%   { transform: translateX(0); }
    100% { transform: translateX(-100%); }
  }

  /* Accessibility: respect reduced motion */
  @media (prefers-reduced-motion: reduce) {
    .nm-ticker__track { animation: none; padding-left: 0; }
  }
</style>

<div class="nm-ticker" aria-label="Research highlights">
  <div class="nm-ticker__mask" aria-hidden="false">
    <div class="nm-ticker__track">
      <span class="nm-ticker__item">Reproducible workflows (FE/ML pipelines)</span>
      <span class="nm-ticker__sep">•</span>
      <span class="nm-ticker__item">Design exploration &amp; surrogate modeling</span>
      <span class="nm-ticker__sep">•</span>
      <span class="nm-ticker__item">Multiscale, multiphysics mechanics</span>
      <span class="nm-ticker__sep">•</span>
  </div>
</div>
```

