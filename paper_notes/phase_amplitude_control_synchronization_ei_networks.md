# Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation

## Basic info

* Title: Phase- and amplitude-dependent control of synchronization in excitatory-inhibitory networks via pulsed stimulation
* Authors: Ehsan Ahmadi, Mojtaba Madadi Asl, Alireza Valizadeh
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/html/2608.15081v1
* Date surfaced: 2026-08-24
* Why selected in one sentence: It turns phase-targeted stimulation from a vague slogan into a cleaner control argument by separating phase reset, oscillation amplitude, and collective synchrony.

## Quick verdict

* Highly relevant

This is a good control paper because it attacks a real confusion in the stimulation literature instead of dressing up another parameter sweep as mechanism. The strong claim is not that phase matters. Everyone says that. The strong claim is that phase reset alone is the wrong summary variable, because the same pulse can retime the rhythm without meaningfully desynchronizing it. The paper earns preserve status by showing that amplitude suppression and synchrony reduction identify a robust desynchronizing window that survives repeated pulses and parameter variation.

## One-paragraph overview

The paper studies a balanced excitatory-inhibitory network of 1,000 exponential integrate-and-fire neurons with sparse random connectivity and self-sustained oscillations near 27.3 hertz. The authors deliver brief two-millisecond current pulses at different phases of the oscillation cycle and analyze three response dimensions: the network phase response curve, the network amplitude response curve, and the change in population Fano factor as a synchrony measure. The central result is that identical pulses can synchronize, barely perturb, or desynchronize the network depending on their timing, and that the cleanest desynchronizing window sits near a half-cycle phase around phi equals 0.5 where amplitude and synchrony both decrease. Repeated stimulation in that window progressively weakens synchrony across pulse intensities, inhibitory time constants, and network realizations while leaving the optimal phase window largely intact.

## Model definition

### Inputs
The model takes the state of a simulated 1,000-neuron excitatory-inhibitory network with 800 excitatory and 200 inhibitory exponential integrate-and-fire neurons, sparse random connectivity with connection probability 0.1, conductance-based synapses, constant background current, and additive Gaussian noise. External perturbations are two-millisecond positive current pulses delivered to the whole population at specific oscillation phases and intensities spanning 50 to 250 picoamps.

### Outputs
The outputs are the network phase response curve for cycle advances or delays, the network amplitude response curve for oscillation suppression or enhancement, and the change in population Fano factor that measures whether synchrony increased or decreased after stimulation. The repeated-pulse analyses additionally output how those measures evolve over one to ten consecutive stimulation cycles.

### Training objective (loss)
There is no learned model and no training loss. The paper is a mechanistic simulation and analysis study rather than a predictive machine-learning paper.

### Architecture / parameterization
The architecture is a balanced excitatory-inhibitory network of exponential integrate-and-fire neurons simulated in NEST with random sparse coupling, conductance-based synapses, and oscillatory baseline dynamics. The main parameterization relevant to the results is the phase-targeted pulse timing, the pulse amplitude sweep from 50 to 250 picoamps, the inhibitory synaptic decay sweep from 5 to 7 milliseconds, and repetition across five independent network realizations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve a control-description problem in oscillatory neuromodulation. The field often treats phase-targeted stimulation as if the phase response curve alone captures whether a pulse meaningfully changes the network. This paper asks which stimulation phases actually suppress synchronized oscillatory activity rather than merely shifting its timing.

### 2. What is the method?
The authors simulate a self-oscillating excitatory-inhibitory network, estimate its baseline oscillation cycle, and deliver brief positive current pulses at many phases and amplitudes. They quantify the resulting phase shifts, amplitude changes, and synchrony changes, then repeat stimulation at the best desynchronizing phase over multiple cycles to test cumulative effects and robustness.

### 3. What is the method motivation?
The motivation is that stimulation control needs a better objective than “hit the right phase.” A pulse can advance or delay the rhythm without actually weakening pathological synchrony. If phase-targeted control is supposed to matter clinically, the field needs response measures that distinguish harmless retiming from real desynchronization.

### 4. What data does it use?
It uses simulated data from a 1,000-neuron balanced excitatory-inhibitory network with oscillations around 27.3 hertz. The paper reports analyses across pulse amplitudes from 50 to 250 picoamps, inhibitory synaptic decay constants from 5 to 7 milliseconds, and five independent random network realizations.

### 5. How is it evaluated?
It is evaluated by measuring the network phase response curve, the network amplitude response curve, and the change in population Fano factor after single and repeated stimulation pulses. The repeated-pulse evaluation asks whether desynchronization accumulates over one to ten cycles, whether the optimal phase window shifts, and whether the effect survives intensity, synaptic-timescale, and realization variation.

### 6. What are the main results?
First, the same pulse can synchronize, barely affect, or desynchronize the network depending only on when it lands in the oscillation cycle. Second, the strongest desynchronizing window sits around phi equals 0.4 to 0.6, with phi equals 0.5 used as the representative target. Third, negative amplitude responses in that window line up with reduced synchrony more reliably than phase reset alone. Fourth, repeated pulses at the desynchronizing phase progressively weaken synchrony and oscillation amplitude across one to ten cycles. Fifth, the optimal phase window remains largely stable even as the network moves into a less synchronized operating point.

### 7. What is actually novel?
The real novelty is not “phase matters.” The novelty is the explicit separation of phase reset, amplitude modulation, and synchrony change as different control dimensions. That gives the paper a more honest control geometry than most phase-targeting work, and it shows that amplitude-response minima are better candidates for desynchronization targeting than phase reset alone.

### 8. What are the strengths?
The paper asks a real control question instead of only reporting a simulation effect. It uses three response measures rather than one. It tests repeated stimulation instead of stopping at single-pulse curves. It checks robustness across pulse intensity, inhibitory timescale, and random realizations. And it keeps the take-home result simple enough to transfer: the useful phase window is where amplitude and synchrony both move in the right direction.

### 9. What are the weaknesses, limitations, or red flags?
This is still a simplified computational model with random sparse connectivity, full-population stimulation, and no empirical validation. The synchrony readout is population Fano factor, which is a reasonable model statistic but not a clinical biomarker. The paper assumes the relevant phase can be estimated and targeted reliably, which is exactly where real closed-loop systems get hard. And because the stimulation acts on the whole simulated network, the intervention geometry is much cleaner than realistic focal neuromodulation.

### 10. What challenges or open problems remain?
The main challenge is whether the same phase-amplitude-synchrony separation survives in more realistic models, empirical recordings, and spatially localized stimulation settings. Another open problem is how to estimate the relevant control phase online when the oscillation is noisy, transient, or only partially observed. A further challenge is deciding which synchrony or amplitude reduction is genuinely therapeutic rather than merely disruptive.

### 11. What future work naturally follows?
The next obvious step is to test the same framework in richer network architectures and with realistic focal stimulation footprints. After that, it should be validated against recorded neural data where phase, amplitude, and synchrony can be measured directly. The most useful translational follow-up would be a closed-loop controller that targets amplitude-suppressing windows while monitoring whether the operating point shifts enough to require retargeting.

### 12. Why does this matter for cabbageland?
It matters because it sharpens what a stimulation controller should actually optimize. If a pulse only retimes the rhythm, that is not the same thing as reducing pathological synchrony. This note gives a cleaner control vocabulary for neuromodulation: phase, amplitude, and synchrony are separate levers, and the best stimulation phase is the one that changes the right outcome, not merely the easiest one to describe.

### 13. What ideas are steal-worthy?
Treat amplitude-response minima as candidate control targets rather than relying only on phase response curves. Track whether repeated stimulation changes the operating point while leaving the optimal phase window intact. Use three-response benchmarking so that a perturbation is not called “effective” unless it actually reduces the network feature you care about. And be willing to compare fixed-phase targeting against update rules that only change timing if the amplitude-suppression window itself moves.

### 14. Final decision
Preserve. This is a full-text, directly relevant computational-control note that gives neuromodulation a sharper response geometry than the average phase-targeting paper. It is still a model, not a device-ready controller, but the conceptual upgrade is real and useful.
