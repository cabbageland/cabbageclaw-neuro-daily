# Phase-dependent stimulation response is shaped by the brain's dynamic functional connectivity

## Basic info

* Title: Phase-dependent stimulation response is shaped by the brain's dynamic functional connectivity
* Authors: Sophie Benitez Stulz, Samy Castro, Boris Gutkin, Matthieu Gilson, Demian Battaglia
* Year: 2026
* Venue / source: Network Neuroscience
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13108500/
* Date surfaced: 2026-06-18
* Why selected in one sentence: It is a sharp control-oriented modeling paper because it argues that stimulation timing must be referenced to transient whole-brain functional connectivity states, not just the local phase at the target.

## Quick verdict

* Useful

This is a preserve because it pushes stimulation theory in the right direction instead of pretending that local phase-locking is the whole story. The strongest claim is that the same pulse can produce different downstream effects depending on the transient functional-connectivity state, and that even crude FC-state labels improve response prediction over phase-only features. The obvious limitation is that all of this lives inside a whole-brain simulation built on a specific working point and macaque structural data, so it should be treated as a strong control hypothesis, not an experimentally validated rulebook.

## One-paragraph overview

The paper builds a connectome-based whole-brain model with 29 structurally connected regions, each represented by coupled excitatory and inhibitory neural-mass populations tuned to oscillate, and then runs large in silico phased-stimulation experiments to ask why stimulation outcomes are so variable. The answer is that local phase is only part of the story: transient large-scale functional-connectivity states change the effective phase-response curve of the stimulated node, and some pulses do not merely nudge the current state but trigger broader state switching. To quantify this, the authors infer discrete FC states from phase-locking patterns and compare machine-learning predictors that know only the local phase and structural outputs of the stimulated region against predictors that also know the current FC state, PLV matrix, and lag structure. FC-aware predictors do substantially better, sometimes by roughly 20 to 40 percent, which makes the paper useful as a conceptual argument for state-aware closed-loop neuromodulation.

## Model definition

This paper contains both a mechanistic whole-brain simulation model and a learned prediction model.

### Inputs
For the simulation layer: a directed 29-region macaque structural connectome from tracer data, local excitatory/inhibitory neural-mass parameters, background drive, long-range coupling strengths, and precisely timed single-pulse stimulation applied to selected regions. For the prediction layer: stimulation phase, outgoing structural connectivity of the stimulated region, inferred FC-state identity, and time-window-specific PLV and lag features describing transient whole-brain coordination.

### Outputs
Simulation outputs include regional firing rates, phase-locking patterns, inferred FC states, stimulation-induced phase shifts in target and remote regions, and probabilities of state morphing versus state switching. The machine-learning layer predicts stimulation-induced phase-shifting effects in affected regions.

### Training objective (loss)
The accessible full text describes random forest regression models trained to predict stimulation-induced phase shifts from various combinations of local and FC-aware features. The exact split criterion is not highlighted as a scientific result, so the safest summary is that the regressors are optimized to reduce phase-shift prediction error on simulated data under cross-validation.

### Architecture / parameterization
A two-layer stack: first, a connectome-based oscillatory whole-brain model with local E/I neural masses and tunable long-range coupling; second, random-forest regressors that map stimulation and brain-state descriptors to predicted phase-shifting outcomes.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Brain stimulation outcomes are notoriously variable, and a common explanation is that the effect depends on the local oscillatory phase at the time of the pulse. This paper asks whether that explanation is too small, and whether transient whole-brain functional-connectivity states are an additional hidden variable that shapes stimulation effects.

### 2. What is the method?
The authors build a large-scale oscillatory brain model using a directed macaque connectome and local excitatory/inhibitory neural masses, choose a working regime with rich synchronization dynamics, infer recurrent FC states from dynamic phase-locking structure, and then apply massive numbers of in silico phased stimulations to selected regions. They quantify both local phase shifts and more global state reconfiguration, and then use random forest regression to compare phase-only versus FC-aware prediction of stimulation effects.

### 3. What is the method motivation?
If the same stimulation can do different things depending on the hidden state of the broader network, then local-phase-locked stimulation is not enough. Closed-loop systems would need to estimate network state as well, otherwise variability is partly self-inflicted by incomplete control variables.

### 4. What data does it use?
No human patient cohort is analyzed directly. The core data are simulated trajectories from a 29-region whole-brain model parameterized by tracer-derived macaque structural connectivity, with dynamic FC states inferred from simulated PLV and phase-lag windows.

### 5. How is it evaluated?
The paper evaluates whether stimulation effects differ across FC states, whether stimulation causes limited state morphing or broader state switching, and how well different machine-learning feature sets predict phase-shifting outcomes under tenfold cross-validation. The critical comparison is between state-ignorant predictors and FC-aware predictors.

### 6. What are the main results?
The same pulse can produce different phase advances or delays depending on the transient FC state, so effective phase-response curves are state dependent rather than fixed. Stimulation can also push the system into broader FC-state switching rather than merely locally deforming the current state. Random-forest predictors that include FC-aware variables outperform phase-only predictors, with improvements that reach roughly 20 to 40 percent for some stimulated regions. Even a coarse discrete FC-state label already helps, and finer PLV/lag descriptions sometimes help more.

### 7. What is actually novel?
The novelty is the explicit attempt to formalize stimulation variability as a joint local-phase plus global-FC-state problem, and to separate state morphing from state switching. The machine-learning comparison is useful because it turns that conceptual claim into a measurable prediction-performance gap rather than a hand-wavy intuition.

### 8. What are the strengths?
- It attacks a real failure mode of phase-locked stimulation logic instead of treating variability as nuisance.
- The use of a directed tracer-derived connectome gives the model more structural asymmetry than many diffusion-MRI virtual-brain papers.
- The paper distinguishes mild local reconfiguration from whole-state switching, which is a genuinely useful control distinction.
- It tests multiple levels of FC-state description, from coarse labels to full PLV/lag matrices, rather than just asserting that "network state matters."

### 9. What are the weaknesses, limitations, or red flags?
- Everything is in silico, so the empirical bridge to real stimulation hardware and real measurements is still missing.
- The model's conclusions depend on a particular operating regime, neural-mass assumptions, and a 29-region macaque connectome.
- Random-forest prediction gains do not prove that the same feature set is measurable robustly enough in actual human closed-loop systems.
- The paper studies phase-shifting effects, not full clinical outcomes, so translational distance remains large.

### 10. What challenges or open problems remain?
The main open problem is whether transient FC states can be estimated quickly and cleanly enough in real human stimulation settings to improve control. It also remains unclear how much of the observed state dependence survives measurement noise, limited sensor coverage, and the coarser observability of noninvasive systems.

### 11. What future work naturally follows?
Fit similar state-aware response models to empirical EEG, MEG, ECoG, or LFP stimulation datasets; test whether coarse FC-state labels are enough in practice; and build closed-loop controllers that decide both when to stimulate and whether the current network state is even worth stimulating.

### 12. Why does this matter for cabbageland?
Because it makes a strong case that stimulation timing should be framed as a whole-brain state-estimation problem, not just a target-region phase problem. That shift is directly relevant to adaptive neuromodulation, biomarker design, and any attempt to make intervention logic less magical.

### 13. What ideas are steal-worthy?
- Treat network-state labels as control variables, not just descriptive post hoc summaries.
- Distinguish state morphing from state switching when thinking about intervention effects.
- Use coarse FC-state summaries first, because even they may add a lot over local phase alone.
- Build response models around what is actually predictable from transient network context, not what is easiest to measure at one electrode.

### 14. Final decision
Keep as a strong conceptual and computational reference for FC-aware stimulation control. It is not empirical enough to settle the question, but it is one of the cleaner recent arguments against local-phase reductionism.
