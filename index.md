---
layout: home
title: ""
permalink: /
---

<style>
@keyframes fadeZoom {
  0% { opacity: 0; transform: scale(0.9); }
  10%, 40% { opacity: 1; transform: scale(1.05); }
  50%, 100% { opacity: 0; transform: scale(1.0); }
}

.nm-collage {
  position: relative;
  width: 100%;
  max-width: 500px;
  margin: 20px auto 30px;
  aspect-ratio: 1 / 1;
  border-radius: 12px;
  overflow: hidden;
  background-color: #000;
  box-shadow: 0 4px 14px rgba(0,0,0,0.25);
}

.nm-collage a {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
}

.nm-collage img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background-color: #000;
  display: block;
  animation: fadeZoom 16s infinite ease-in-out;
}

.nm-collage a:nth-child(1) img { animation-delay: 0s; }
.nm-collage a:nth-child(2) img { animation-delay: 4s; }
.nm-collage a:nth-child(3) img { animation-delay: 8s; }
.nm-collage a:nth-child(4) img { animation-delay: 12s; }

@media (max-width: 480px) {
  .nm-collage {
    max-width: 340px;
  }
}
</style>

### Research focus
Sustainable cementitious systems, auxetic composites, and ML-driven modeling across experiments, numerical analysis, and interpretability.

<div class="nm-collage">
  <a href="https://www.sciencedirect.com/science/article/pii/S0950061821004517" target="_blank"><img src="/assets/img/pic-1.jpg" alt="Image 1"></a>
  <a href="https://www.sciencedirect.com/science/article/pii/S0301479724019091" target="_blank"><img src="/assets/img/pic-2.jpg" alt="Image 2"></a>
  <a href="https://www.sciencedirect.com/science/article/pii/S235271022402816X" target="_blank"><img src="/assets/img/pic-3.jpg" alt="Image 3"></a>
  <a href="https://www.sciencedirect.com/science/article/pii/S0959652621036623" target="_blank"><img src="/assets/img/pic-4.jpg" alt="Image 4"></a>
</div>


**Scholar:** [Google Scholar](https://scholar.google.com/citations?user=orlzgpMAAAAJ&hl=en)  
**Email:** nausad_miyan@uri.edu
