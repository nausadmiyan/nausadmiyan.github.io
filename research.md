---
layout: page
title: ""
permalink: /research/
---

<style>
/* Wider page content on large screens */
@media (min-width: 992px){
  .page-content .wrapper { max-width: 1100px; }
}

/* Section heading */
.research-section h2 {
  margin-top: 8px;
  margin-bottom: 16px;
  font-size: 1.6rem;
}

/* Two-column grid on desktop, single column on mobile */
.research-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 18px;
}
@media (min-width: 900px){
  .research-grid { grid-template-columns: 1fr 1fr; }
}

/* Cards */
.topic {
  padding: 14px 16px;
  border: 1px solid #e6e6e6;
  border-radius: 10px;
  background: #fff;
}

/* Underlined titles */
.topic-title {
  margin: 0 0 8px 0;
  font-size: 1.05rem;
  border-bottom: 2px solid #111;
  display: inline-block;
  padding-bottom: 2px;
}

/* Paragraphs */
.topic p { margin: 0; line-height: 1.55; font-size: 0.96rem; }
</style>

**Education**  
- PhD, Civil & Environmental Engineering (2023–now), [University of Rhode Island](https://www.uri.edu/)

<div class="research-section">
  <h2>Research Areas</h2>

  <div class="research-grid">

    <div class="topic">
      <h3 class="topic-title">Multiscale Simulation</h3>
      <p>
        I develop physics-informed links from material to component to system scales using the
        <a href="https://en.wikipedia.org/wiki/Finite_element_method">finite element method</a> coupled with
        <a href="https://en.wikipedia.org/wiki/Surrogate_model">surrogate models</a> and
        <a href="https://en.wikipedia.org/wiki/Uncertainty_quantification">uncertainty quantification</a>.
        Statistically representative microstructures are built as
        <a href="https://en.wikipedia.org/wiki/Representative_volume_element">representative volume elements</a> and
        upscaled via <a href="https://en.wikipedia.org/wiki/Homogenization_(materials_science)">homogenization</a> to calibrate continuum constitutive laws and predict service and extreme-load response; model transparency and design trade-offs are assessed with
        <a href="https://en.wikipedia.org/wiki/Shapley_value#Machine_learning">Shapley additive explanations</a>, while
        <a href="https://en.wikipedia.org/wiki/Digital_twin">digital twins</a> synchronize simulation and experiment for precast and reinforced concrete systems.
      </p>
    </div>

    <div class="topic">
      <h3 class="topic-title">Molecular Dynamics</h3>
      <p>
        At the atomistic scale I use <a href="https://en.wikipedia.org/wiki/Molecular_dynamics">molecular dynamics</a>
        with validated <a href="https://en.wikipedia.org/wiki/Force_field_(chemistry)">force fields</a> to interrogate the structure–property relations of
        <a href="https://en.wikipedia.org/wiki/Calcium_silicate_hydrate">calcium–silicate–hydrate</a>, including interlayer chemistry tuned by calcium-to-silicon ratio; hydration states are sampled by
        <a href="https://en.wikipedia.org/wiki/Monte_Carlo_method#Grand_canonical_Monte_Carlo">grand canonical Monte Carlo</a>, transport behavior is quantified through
        <a href="https://en.wikipedia.org/wiki/Diffusion_coefficient">diffusion coefficients</a> and
        <a href="https://en.wikipedia.org/wiki/Sorption_isotherm">sorption isotherms</a>, and nanoscale stiffness, fracture initiation, and adhesion at mineral interfaces inform mesoscale constitutive models that propagate upward through multiscale frameworks.
      </p>
    </div>

    <div class="topic">
      <h3 class="topic-title">Precast Component Design</h3>
      <p>
        My structural work advances <a href="https://en.wikipedia.org/wiki/Precast_concrete">precast concrete</a>
        component and connection design using
        <a href="https://en.wikipedia.org/wiki/Performance-based_design">performance-based design</a>
        under gravity, wind, and seismic demands with
        <a href="https://en.wikipedia.org/wiki/Progressive_collapse">progressive-collapse</a> checks; designs are optimized across strength, serviceability, durability, constructability, and cost, incorporating
        <a href="https://en.wikipedia.org/wiki/Life-cycle_assessment">life-cycle assessment</a> and
        <a href="https://en.wikipedia.org/wiki/Life-cycle_cost_analysis">life-cycle cost analysis</a> to quantify carbon–cost trade spaces, and simulation outputs are validated against laboratory testing and field observations to ensure code compliance and robust detailing at scale.
      </p>
    </div>

    <div class="topic">
      <h3 class="topic-title">Materials Characterization and Testing</h3>
      <p>
        I integrate mechanical and durability testing with microstructural analyses to close the loop between experiment and model:
        <a href="https://en.wikipedia.org/wiki/Mechanical_testing">mechanical testing</a> (compression, tension, flexure, fracture, and fatigue), transport and freeze–thaw resistance,
        <a href="https://en.wikipedia.org/wiki/Scanning_electron_microscope">scanning electron microscopy</a> with
        <a href="https://en.wikipedia.org/wiki/Energy-dispersive_X-ray_spectroscopy">energy-dispersive X-ray spectroscopy</a>,
        <a href="https://en.wikipedia.org/wiki/X-ray_diffraction">X-ray diffraction</a>,
        <a href="https://en.wikipedia.org/wiki/Mercury_intrusion_porosimetry">mercury intrusion porosimetry</a>,
        <a href="https://en.wikipedia.org/wiki/Thermogravimetric_analysis">thermogravimetric analysis</a>, and
        <a href="https://en.wikipedia.org/wiki/Differential_scanning_calorimetry">differential scanning calorimetry</a>;
        these data streams quantify phase evolution, pore structure, transport pathways, and degradation kinetics, enabling rigorous model calibration and predictive validation for cementitious and composite systems.
      </p>
    </div>

    <div class="topic">
      <h3 class="topic-title">Data-Driven Materials Informatics and Generative Modeling</h3>
      <p>
        I employ <a href="https://en.wikipedia.org/wiki/Machine_learning">machine learning</a> and
        <a href="https://en.wikipedia.org/wiki/Artificial_intelligence">artificial intelligence</a> for property prediction and materials enhancement, combining
        <a href="https://en.wikipedia.org/wiki/Regression_analysis">regression</a> and
        <a href="https://en.wikipedia.org/wiki/Classification">classification</a> models with
        <a href="https://en.wikipedia.org/wiki/Feature_selection">feature selection</a> and
        <a href="https://en.wikipedia.org/wiki/Model_selection">model selection</a>; I use
        <a href="https://en.wikipedia.org/wiki/Generative_adversarial_network">generative adversarial networks</a> for data augmentation and microstructure synthesis,
        <a href="https://en.wikipedia.org/wiki/Physics-informed_neural_networks">physics-informed neural networks</a> to embed governing constraints,
        <a href="https://en.wikipedia.org/wiki/Bayesian_optimization">Bayesian optimization</a> and
        <a href="https://en.wikipedia.org/wiki/Active_learning">active learning</a> for inverse design and accelerated experimentation, and
        <a href="https://en.wikipedia.org/wiki/Shapley_value#Machine_learning">Shapley additive explanations</a> for interpretable ranking of influential variables; the workflow targets predictive accuracy for strength, transport, and durability while guiding mixture design and processing routes that measurably enhance performance.
      </p>
    </div>

  </div>
</div>
