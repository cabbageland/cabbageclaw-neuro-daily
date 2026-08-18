# Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation

## Basic info

* Title: Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation
* Authors: Ehsan Ahmadi, Mojtaba Madadi Asl, Alireza Valizadeh
* Year: 2026
* Venue / source: arXiv q-bio.NC
* Link: https://arxiv.org/abs/2608.15081
* Date surfaced: 2026-08-18
* Why selected in one sentence: It turns phase-targeted stimulation from slogan into a concrete control problem by showing that the same pulse can synchronize, do almost nothing, or desynchronize an oscillatory excitatory-inhibitory network purely as a function of timing, then shows that the desynchronizing window survives repeated use.

## Quick verdict

* Highly relevant

This is a preserve from full-text arXiv HTML inspection, including the methods, results, and discussion sections. The paper is valuable because it asks a control question that actually transfers: if you are going to perturb an oscillatory circuit, what state variables do you need beyond phase, and where is the reliable desynchronizing window? The paper is still a clean toy-model study rather than an empirical neuromodulation result, but it is exactly the kind of mechanistic paper that sharpens how phase-targeted DBS, TMS, tACS, or ultrasound papers should justify their control logic.

## One-paragraph overview

The paper studies a balanced excitatory-inhibitory spiking network of 1,000 exponential integrate-and-fire neurons and asks how brief current pulses change collective oscillations depending on when the pulse arrives in the oscillation cycle. Instead of reporting only a network phase response curve, the authors jointly analyze phase resetting, oscillation amplitude changes, and synchrony changes through the population Fano factor. That three-axis view matters because the same pulse can delay the rhythm, advance it, strengthen synchrony, or weaken it depending on phase, and those effects do not collapse into one scalar. In the baseline configuration the network oscillates around 27.3 Hz with moderate synchrony, and the key result is that a desynchronizing window near phase 0.5 stays useful across repeated pulses, driving cumulative weakening of oscillatory activity without moving the optimal phase itself.

## Model definition

This paper does not contain a trainable predictive model. The relevant model is a mechanistic spiking-network simulator plus response-analysis pipeline.

### Inputs
The simulator takes the current network state of a sparse 1,000-neuron excitatory-inhibitory network with 800 excitatory and 200 inhibitory exponential integrate-and-fire neurons, conductance-based synapses, fixed connection probability 0.1, external tonic current plus noise, and brief phase-targeted current pulses. The pulse analyses vary stimulation phase through the oscillation cycle, pulse intensity from 50 to 250 pA, and in the robustness tests vary inhibitory synaptic decay time constants from 5 to 7 ms across five independent network realizations.

### Outputs
The primary outputs are a network phase response curve, a network amplitude response curve, and the change in population synchrony measured with the population Fano factor. In the repeated-stimulation experiments the model also outputs how those three response surfaces evolve after one, five, and ten pulses delivered at the desynchronizing phase.

### Training objective (loss)
There is no learning objective or fitted predictive loss here. The paper is a forward simulation and response-characterization study rather than a trained decoder or controller.

### Architecture / parameterization
The architecture is a balanced sparse excitatory-inhibitory spiking network of exponential integrate-and-fire neurons with conductance-based alpha-function synapses. The analysis layer computes phase, amplitude, and synchrony response functions for single and repeated perturbations and summarizes robustness over pulse amplitudes, inhibitory time constants, and random network realizations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to solve a very specific control problem: how to perturb an oscillatory neuronal network so that you suppress pathological synchrony rather than accidentally reinforce it. More bluntly, if you deliver the same pulse at different moments of the cycle, when do you actually get desynchronization, and what response variables tell you that you succeeded?

### 2. What is the method?
The authors simulate a balanced excitatory-inhibitory spiking network, let it settle into a self-sustained oscillatory state, and then apply brief current pulses at different phases of the oscillation. They compute the network phase response curve to measure timing shifts, the network amplitude response curve to measure oscillation-strength changes, and the change in population Fano factor to measure synchrony shifts. After identifying the strongest desynchronizing phase, they apply repeated pulses over ten consecutive cycles and test robustness across stimulation intensities, inhibitory time constants, and random network realizations.

### 3. What is the method motivation?
The motivation is that phase response curves alone are too thin. A pulse that advances or delays an oscillation is not automatically a pulse that weakens synchrony, and in neuromodulation those are different goals. If you want real intervention logic rather than pretty phase diagrams, you need to track whether the network is getting weaker, more coherent, less coherent, or merely time-shifted.

### 4. What data does it use?
There is no empirical human or animal dataset. The paper uses simulated activity from a 1,000-neuron excitatory-inhibitory network with 800 excitatory and 200 inhibitory neurons, sparse random connectivity, conductance-based synapses, tonic external drive, and noise. The repeated-stimulation robustness analyses use pulse amplitudes from 50 to 250 pA, inhibitory synaptic decay constants from 5 to 7 ms, and five independent network realizations.

### 5. How is it evaluated?
Evaluation happens in three stages. First, the authors characterize the baseline oscillatory regime, including synchrony and spectral peak. Second, they sweep stimulation phase and intensity for single pulses and measure network phase response, amplitude response, and synchrony change. Third, they deliver repeated pulses at the desynchronizing phase over ten cycles and test whether cumulative desynchronization remains stable across stimulation amplitudes, inhibitory kinetics, and independent realizations.

### 6. What are the main results?
The main result is that stimulation timing alone can flip the same perturbation between opposite collective outcomes. In the baseline configuration the network oscillates around 27.3 Hz with population Fano factor 5.0. Single-pulse sweeps show a biphasic phase response, a U-shaped amplitude response, and a clear synchrony dependence on phase: for a 225 pA pulse, phase 0.90 is synchronizing, phase 0.70 is nearly ineffective, and phase 0.50 is desynchronizing. The minimum amplitude response and strongest synchrony reduction consistently sit near phase 0.5, and when the authors repeat pulses at that phase over ten cycles, oscillation amplitude and synchrony progressively weaken while the optimal desynchronizing phase remains essentially stable. The cumulative effect remains robust across 50 to 250 pA pulses, inhibitory synaptic decay constants of 5 to 7 ms, and five independent network realizations.

### 7. What is actually novel?
The novelty is not that phase matters. The more useful novelty is the insistence that phase alone is not the right summary statistic for control. The paper explicitly combines phase resetting, amplitude modulation, and synchrony modulation, then shows that repeated desynchronizing stimulation changes the operating point of the network without moving the best phase window. That is a better control vocabulary than the usual phase-only story.

### 8. What are the strengths?
First, the paper is fully readable and methodologically transparent enough to support a real note instead of abstract theater. Second, it isolates a practically reusable claim: report nARC and synchrony changes, not just nPRC, when you talk about phase-targeted control. Third, it goes beyond one-shot perturbations and shows cumulative effects under repeated stimulation. Fourth, it does at least some robustness work across stimulation intensity, inhibitory kinetics, and network realizations rather than pretending one trace is enough.

### 9. What are the weaknesses, limitations, or red flags?
The paper is still a stylized mechanistic model. The network is sparse, random, homogeneous, and assigned fixed conduction delays, which is a long way from cortico-basal-ganglia loops, thalamocortical structure, or patient-specific anatomy. There is no observation noise, no phase-estimation error, no stimulation artifact problem, no plasticity, no adaptive controller, and no empirical validation showing that the same response geometry survives in real recordings. The population Fano factor is a decent coarse synchrony readout, but it is not a complete description of multiscale coordination or functional consequence.

### 10. What challenges or open problems remain?
The main open problem is translation. A real system would need noisy phase estimation, uncertain state tracking, heterogeneous delays, structured connectivity, and possibly drifting stimulation response over time. The field still needs to know whether the same desynchronizing windows survive in more biophysical models, in patient-specific network models, and in actual closed-loop recordings where you do not get to observe the true network phase for free.

### 11. What future work naturally follows?
The obvious next step is to embed the phase-amplitude-synchrony framework inside an actual controller rather than leaving it as a diagnostic map. After that, the right moves are to test heterogeneous delays, structured connectomes, plasticity, and stimulation artifact constraints, then compare phase-targeted policies against amplitude-only, frequency-only, or reinforcement-learning controllers in the same simulated and empirical environments. A more ambitious follow-up would connect this framework to patient-specific epilepsy or Parkinsonian models where the objective is not generic desynchronization but symptom-linked state steering.

### 12. Why does this matter for cabbageland?
Because it gives a sharper intervention language for neuromodulation papers that claim state-dependent control. If a paper says a pulse delivered at the right time changes circuit dynamics, this note says what the evidence should look like: not just a phase shift, but a clear account of amplitude suppression, synchrony reduction, and whether the useful phase window stays stable under repetition. It is a compact control-theory sanity check for a lot of phase-locked stimulation rhetoric.

### 13. What ideas are steal-worthy?
Three things are especially steal-worthy. First, phase response should not travel alone; pair it with amplitude and synchrony response maps. Second, the controller-relevant object may be a stable desynchronizing window rather than a single magic phase estimate. Third, repeated phase-targeted stimulation can move the network to a weaker-synchrony operating point without necessarily changing where the best stimulation window lives, which is a useful design principle for adaptive DBS, TMS, tACS, or ultrasound protocols.

### 14. Final decision
Preserve. This is a strong mechanistic control note because it turns phase-targeted stimulation into a three-axis response problem and shows that the desynchronizing window is stable enough to support repeated use. It is still a toy-model paper rather than a translational proof, but the intervention logic is sharp enough that future closed-loop papers should have to answer to it.
