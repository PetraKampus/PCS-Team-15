# Simulating Yayoi Kusama’s Visual Cortex with Reaction-Diffusion

[//]: # (**PCS-Team-15:** Mariam Saiqodze, Petra Kampus, Mark Haakman)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## &#40;1&#41; Introduction:)

[//]: # ()
[//]: # (Yayoi Kusama’s artwork is distinguished by the obsessive repetition of dots,)

[//]: # (nets, and dense geometric fields. Remarkably, Kusama has consistently reported that these visual motifs reflect persistent visual disturbances—fields of)

[//]: # (dots, flashes, and intricate patterns she has perceived since childhood. Such)

[//]: # (experiences closely resemble geometric visual hallucinations, a phenomenon extensively studied in neuroscience.)

[//]: # ()
[//]: # (**Figure 1:** yayoi Kusama)

[//]: # (![Yayoi Kusama]&#40;Figures/yayoi.jpg&#41;)

[//]: # ()
[//]: # (Theoretical and computational studies have shown that geometric hallucinations can arise from self-organized pattern formation in the primary visual cortex &#40;V1&#41;, particularly when the balance between)

[//]: # (neural excitation and inhibition is disrupted. These patterns are formally described as Turing instabilities)

[//]: # (in neural field models, with the Wilson–Cowan equations serving as a canonical)

[//]: # (mathematical framework for capturing the dynamics of interacting excitatory)

[//]: # (and inhibitory neural populations.)

[//]: # ()
[//]: # (In this project, we explore an alternative approach: modeling these cortical )

[//]: # (instabilities using a reaction–diffusion system. By mapping the excitatory and )

[//]: # (inhibitory populations in the Wilson–Cowan framework to activator and)

[//]: # (substrate variables in a canonical reaction–diffusion model, we aim to demonstrate )

[//]: # (that the resulting patterns reproduce the geometric structures observed in Kusama’s )

[//]: # (visual experiences. This mapping provides a mathematically tractable and visually )

[//]: # (interpretable analog of cortical pattern formation.)

[//]: # ()
[//]: # (## &#40;2&#41; Research Questions:)

[//]: # ()
[//]: # (This project investigates whether the characteristic patterns in Yayoi Kusama’s)

[//]: # (artwork can be understood as stable dynamical states of a cortical patternforming system)

[//]: # (driven by excitation–inhibition imbalance in the primary visual cortex &#40;V1&#41;. )

[//]: # (Specifically, we ask:)

[//]: # ()
[//]: # (&#40;1&#41;: Can the Wilson-Cowan model of cortical hallucinations be faithfully represented by a )

[//]: # (     reaction-diffusion system analog?)

[//]: # ()
[//]: # (&#40;2&#41;: Do different parameter regimes of this reaction–diffusion analog produce)

[//]: # (     spatial patterns resembling Kusama’s visual motifs, including dots, nets,)

[//]: # (     and dense geometric fields?)

[//]: # ()
[//]: # (**Figure 2:**Turing pattern of neural excitation in visual cortex coordinates.)

[//]: # (![Target]&#40;Figures/target.png&#41;)

[//]: # ()
[//]: # (## &#40;3&#41; Theory and Mathematical Model:)

[//]: # ()
[//]: # (### &#40;3.1&#41; Geometric Hallucinations and Cortical Turing Patterns.)

[//]: # ()
[//]: # (Geometric visual hallucinations are spontaneous visual patterns experienced)

[//]: # (when neural activity in the primary visual cortex &#40;V1&#41; is driven more by internal )

[//]: # (dynamics than by external stimuli. )

[//]: # (These patterns have been shown to emerge from self-organized instabilities in V1, )

[//]: # (which can be mathematically captured by the Wilson–Cowan equations. )

[//]: # (These equations describe the interactions between excitatory &#40;ϕ&#41; and inhibitory &#40;ψ&#41; neural populations, and)

[//]: # (under certain conditions, they exhibit Turing instabilities, leading to spatially)

[//]: # (patterned neural activity.)

[//]: # ()
[//]: # (### &#40;3.1&#41; Reaction-Diffusion as a Cortical Analog.)

[//]: # ()
[//]: # (Although the Wilson–Cowan model accurately describes cortical dynamics, simpler reaction–diffusion systems capture the same underlying pattern-forming mechanism. )

[//]: # (In particular, the Gray–Scott model provides a canonical activatorsubstrate system:)

[//]: # ()
[//]: # ($$ )

[//]: # (\frac{\partial V}{\partial t} = D_{V} \nabla^{2} V + UV^{2} - &#40;F+k&#41;V)

[//]: # ($$)

[//]: # ($$)

[//]: # (\frac{\partial U}{\partial t} = D_{U}\nabla^{2}U - UV^{2} + F&#40;1 - U&#41;)

[//]: # ($$)

[//]: # ()
[//]: # (where $V$ represents an activator &#40;analogous to excitatory activity ϕ in V1&#41;)

[//]: # (and $U$ represents a substrate &#40;analogous to inhibitory availability ψ&#41;. The key)

[//]: # (Turing condition, $D_{U} > D_{V}$ , mirrors the cortical requirement that inhibitory)

[//]: # (effects spread farther than excitatory ones.)

[//]: # (This project explores the hypothesis that a mapping between Wilson–Cowan)

[//]: # (dynamics and Gray–Scott reaction–diffusion dynamics is valid. We test whether)

[//]: # (reaction–diffusion patterns can reproduce hallucinatory motifs similar to those)

[//]: # (described by Kusama.)

[//]: # ()
[//]: # (### &#40;3.3&#41; Conceptual Mapping.)

[//]: # ()
[//]: # (Table 1 summarizes the correspondence between cortical and reaction–diffusion)

[//]: # (concepts:)

[//]: # ()
[//]: # (**Table 1:**)

[//]: # (![Mapping table]&#40;Figures/mappingtable.png&#41;)

[//]: # ()
[//]: # ()
[//]: # (## &#40;4&#41; Methods and Simulation:)

[//]: # ()
[//]: # (### &#40;4.1&#41; Numerical Implementation.)

[//]: # ()
[//]: # (The Gray–Scott equations were simulated on a 200 × 200 grid with periodic)

[//]: # (boundary conditions. Spatial derivatives were approximated using a five-point)

[//]: # (Laplacian stencil, and temporal integration was performed with a forward Euler)

[//]: # (method. A time step of ∆t = 1 was chosen to ensure numerical stability.)

[//]: # ()
[//]: # (### &#40;4.2&#41; Initial Conditions and Parameters.)

[//]: # ()
[//]: # (Patterns were initiated with a localized perturbation at the center of the grid:)

[//]: # ()
[//]: # (    - Central 20 × 20 region: $U = 0.50, V = 0.25$)

[//]: # (    - Surrounding domain: $U = 1.0, V = 0.0$)

[//]: # ()
[//]: # (Diffusion coefficients were set to satisfy the Turing condition:)

[//]: # ()
[//]: # ($D_{U} = 0.16, D_{V} = 0.08$)

[//]: # ()
[//]: # (Reaction parameters $F$ and $k$ were systematically varied to explore different)

[//]: # (pattern regimes:)

[//]: # ()
[//]: # ($F \in [0.02, 0.10]$, $k \in [0.04, 0.08]$)

[//]: # ()
[//]: # (Each simulation ran for 12,000 iterations to allow patterns to stabilize.)

[//]: # ()
[//]: # (### &#40;4.2&#41; Pattern Analysis.)

[//]: # ()
[//]: # (To quantify the emerging patterns, we measured:)

[//]: # ()
[//]: # ()
[//]: # (**Figure 3:** Variance of activator and inhibitor fields)

[//]: # (![variance]&#40;Figures/plots/variance_phase_diagram.png&#41;)

[//]: # ()
[//]: # (**Figure 4:** Temporal changes in pattern intensity)

[//]: # (![Stability]&#40;Figures/plots/stability_phase_diagram.png&#41;)

[//]: # ()
[//]: # (**Figure 5:** Dominant spatial frequency of the structures)

[//]: # (![freq]&#40;Figures/plots/frequency_phase_diagram.png&#41;)

[//]: # ()
[//]: # (### &#40;4.4&#41; Parameter-Dependent Pattern Morphology.)

[//]: # ()
[//]: # (Systematic exploration of the $&#40;F, k&#41;$ parameter space revealed several distinct)

[//]: # (pattern-forming regimes. Among all tested parameter combinations, four produced )

[//]: # (polka-dot patterns resembling Kusama’s visual motifs:)

[//]: # ()
[//]: # ($$)

[//]: # ([F,k] = )

[//]: # (\begin{bmatrix})

[//]: # (0.04 & 0.065 \\)

[//]: # (0.02 & 0.055 \\)

[//]: # (0.025 & 0.06 \\)

[//]: # (0.035 & 0.065)

[//]: # (\end{bmatrix})

[//]: # ($$)

[//]: # ()
[//]: # (Of these, the combination $[F, k] = [0.025, 0.06]$ $&#40;F/k ≈ 0.42&#41;$ yielded optimal results, )

[//]: # (producing the most regular, circular, and well-separated spots, closely)

[//]: # (matching both Kusama’s aesthetic and the target Turing patterns of neural)

[//]: # (excitation in visual cortex coordinates.)

[//]: # ()
[//]: # (Based on the full parameter sweep, we observed the following pattern regimes:)

[//]: # (    • Low $F/k$ &#40;< 0.35&#41;: Sparse or quiescent patterns)

[//]: # (    • Moderate $F/k &#40;0.36 − 0.50&#41;: Regular polka-dots resembling Kusama’s)

[//]: # (      motifs)

[//]: # (    • Intermediate $F/k$ &#40;0.50 − 0.65&#41;: Mixed dots and stripes)

[//]: # (    • High $F/k$ &#40;> 0.65&#41;: Labyrinthine and dense fields)

[//]: # ()
[//]: # (**Figure 6:** Gray-Scott simulation $F=0.025, k=0.06$)

[//]: # (![0025006]&#40;Figures/F0.025-k0.06_two.png&#41;)

[//]: # ()
[//]: # (**Figure 7:** Gray-Scott simulation $F=0.04, k=0.065$)

[//]: # (![0040065]&#40;Figures/F0.04-k0.065_two.png&#41;)

[//]: # ()
[//]: # (### &#40;4.5&#41; Reaction-Diffusion as a Cortical Analog.)

[//]: # ()
[//]: # (Simulations show that the Gray–Scott model produces spatial patterns qualitatively similar to )

[//]: # (those generated by cortical Turing instabilities. )

[//]: # (Reaction–diffusion system reproduces the core pattern-forming dynamics of the Wilson–Cowan)

[//]: # (model, with the optimal polka-dot parameters $&#40;F/k \approx 0.42&#41;$.)

[//]: # ()
[//]: # (## &#40;5&#41; Conclusion:)

[//]: # ()
[//]: # (This project demonstrates that:)

[//]: # ()
[//]: # (        1: The Gray–Scott reaction–diffusion system  can serve as a valid analog for cortical Turing patterns described by the Wilson–Cowan model. Both systems share the same underlying pattern-forming mechanism, allowing excitatory–inhibitory dynamics to be studied in a simpler framework.)

[//]: # ()
[//]: # (        2: Different parameter regimes of the reaction–diffusion system produce patterns closely resembling geometric hallucinations and Yayoi Kusama’s visual motifs.)

[//]: # (        In particular, F/k ≈ 0.42 generates regular polka-dot patterns, while other regimes produce nets or dense fields.)

[//]: # ()
[//]: # (These findings support the idea that Kusama’s characteristic visual experiences can be interpreted as a manifestation of cortical pattern formation. The reaction–diffusion framework provides a generative model that captures the essential mathematics of cortical instabilities, enabling exploration of hallucinationinspired patterns in a controlled, quantitative manner.)

[//]: # ()
[//]: # (## References)

[//]: # ([1] Butler, T. C., Benayoun, M., Wallace, E., van Drongelen, W., Goldenfeld,)

[//]: # (    N., & Cowan, J. &#40;2012&#41;. Evolutionary constraints on visual cortex architecture from the dynamics of hallucinations. Proceedings of the National Academy of Sciences, 109&#40;2&#41;, 606-609.)

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()




This repository contains an implementation of the Gray–Scott reaction–diffusion model for simulating self-organizing spatial patterns on a two-dimensional grid. The model is inspired by cortical Turing pattern formation in the primary visual cortex (V1), geometric visual hallucinations, and Yayoi Kusama's visual motifs.

## Project Structure

```
simulation/
    model.py        # Gray–Scott reaction–diffusion model
    animate.py      # visualization and animation utilities
    examples/       # generated simulation figures

runner/
    main.py         # main script to run and visualize simulations

tests/
    metrics.py      # computation of quantitative pattern metrics
    validation.py   # parameter sweeps and analysis plots
    test_model.py   # unit tests and assertions for ReactionDiffusionModel
    plots/          # generated statistical plots
```

## Requirements

* Python >= 3.9
* numpy
* matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

## Running the Simulation

The main entry point is `runner/main.py`. Running this script will:

* Execute a Gray–Scott simulation with default parameters
* Display a static binary snapshot of the final pattern
* Show an animation of the pattern evolution

Optional functionality includes generating side-by-side figures for different (F, k) parameter combinations.

Run the script from the project root:

```bash
python runner/main.py
```

## Default Parameters

* Grid size: 200 × 200
* Iterations: 12000
* Diffusion: Du = 0.16, Dv = 0.08
* Reaction: F = 0.025, k = 0.06
* Timestep: dt = 0.9

## Parameter Exploration

Key reaction–diffusion parameters:

* F – feed rate
* k – kill rate
* Du – diffusion coefficient of U
* Dv – diffusion coefficient of V

Common parameter pairs used in experiments:

* (F, k) = (0.04, 0.065)
* (F, k) = (0.02, 0.055)
* (F, k) = (0.025, 0.06) ← Main configuration
* (F, k) = (0.035, 0.065)

## Tests and Validation

Run quantitative analysis and generate plots:

```bash
python tests/validation.py
```

Statistical plots are saved in `tests/plots/`.

## Numerical Model

* Spatial diffusion: five-point finite-difference Laplacian
* Boundary conditions: periodic (via array rolling)
* Time integration: forward Euler scheme

Main implementation is in `simulation/model.py`.

## Output Files

* Generated images: `simulation/examples/`
* Statistical plots: `tests/plots/`
