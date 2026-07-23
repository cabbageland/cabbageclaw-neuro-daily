# Learning the Brain's Dynamics as a Port-Hamiltonian System: A GNN-Surrogate Metriplectic Twin for Non-Equilibrium Cortical Dynamics and Closed-Loop Neuromodulation

## Basic info

* Title: Learning the Brain's Dynamics as a Port-Hamiltonian System: A GNN-Surrogate Metriplectic Twin for Non-Equilibrium Cortical Dynamics and Closed-Loop Neuromodulation
* Authors: Dibakar Sigdel
* Year: 2026
* Venue / source: arXiv preprint
* Link: https://arxiv.org/abs/2607.10439
* Date surfaced: 2026-07-23
* Why selected in one sentence: It is a useful control-and-modeling note because it forces a purportedly intervention-ready cortical model to answer falsifiable dynamical tests instead of only reporting fit quality.

## Quick verdict

* Useful

This is worth keeping, but not because it has already solved closed-loop neuromodulation. It has not. The useful part is the combination of structural discipline and unusually explicit honesty: the paper fits a port-Hamiltonian style cortical dynamics model to real EEG, then scores the free-running model against invariants it did not author and states plainly that it clears branching but fails the spectral-slope and long-range-correlation tests. That is a better research norm than the usual control-flavored brain-model theater. The main caution is that the causal perturbation rung is still deferred, the model is not subject-specific, and even the arXiv abstract page still leaked placeholder strings instead of the real sample count and held-out error.

## One-paragraph overview

The paper builds a physics-structured cortical dynamics model on top of the PhysioNet EEG Motor Movement/Imagery database. EEG is decomposed into five canonical-band phasor coordinates, then a port-Hamiltonian and metriplectic formulation combines a band-stratified graph energy model, a phase-locking-gated functional connectome, and state-dependent dissipation. The model is fit on more than 1.1 million training phasor samples with a by-subject held-out split, then rolled out freely and scored against model-independent dynamical invariants from the recordings. It reproduces near-critical avalanche branching but fails to match the real 1/f slope and DFA exponent, which is exactly why the paper is useful: it makes the failure legible instead of hiding it under architectural vocabulary.

## Model definition

### Inputs
Sixty 64-channel EEG recordings from 12 EEGMMIDB subjects spanning eyes-open rest, eyes-closed rest, and motor-imagery conditions; band-limited phasor coordinates extracted via Butterworth filtering and Hilbert transforms; and empirical phase-locking-value connectivity priors derived from the recordings.

### Outputs
Predicted phasor-state derivatives, a learned state-dependent functional connectome, band-resolved energy terms, free-running cortical trajectories, and model-derived dynamical invariants such as branching parameter, spectral slope, and DFA exponent.

### Training objective (loss)
A composite physics-informed objective that combines kinematic reconstruction with energy-balance and non-equilibrium-steady-state constraints, a phase-locking coherence prior, and a theta-gamma phase-amplitude-coupling regularizer. The model also hard-codes skew-symmetry for the reversible generator and positive-semidefiniteness for dissipation rather than merely hoping those properties emerge.

### Architecture / parameterization
A port-Hamiltonian and metriplectic neural dynamics model with band-stratified graph energy terms, a graph-neural-network surrogate for the dynamic functional connectome, state-dependent dissipation, and explicit stimulation ports meant to represent tDCS, TMS, and DBS targets.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Most EEG and BCI models classify or fit signals without any serious story about the underlying dynamics, control semantics, or what a perturbation would even mean. This paper tries to build a cortical model whose structure still means something when one starts talking about stimulation and stability.

### 2. What is the method?

The method turns EEG into five-band phase-and-frequency phasor coordinates, fits a port-Hamiltonian and metriplectic dynamics model with a learned but structure-constrained connectome and dissipation operator, and then validates the resulting free-running model against independent dynamical invariants measured from the same recordings.

### 3. What is the method motivation?

If a model is going to claim relevance for control or neuromodulation, it should preserve the semantics of routing, dissipation, actuation, and bounded energy injection rather than behaving like an opaque recurrent network with prettier terminology.

### 4. What data does it use?

The PhysioNet EEG Motor Movement/Imagery database with 12 subjects, 60 recordings, 64 channels, and eyes-open rest, eyes-closed rest, and motor-imagery conditions. The paper reports roughly 1.48 million phasor samples overall, with 1,109,250 used for training and 368,250 held out by subject for testing.

### 5. How is it evaluated?

Evaluation uses a leakage-free by-subject split with three held-out subjects, held-out kinematic reconstruction error, seed robustness, and a validation ladder based on power-spectrum slope, avalanche branching, and detrended fluctuation analysis computed both on the recordings and on the model's free-running rollouts.

### 6. What are the main results?

The model reaches held-out kinematic reconstruction MSE of about 1.30 times 10 to the minus 4, with under 0.3 percent variation across three random seeds.

The free-running stochastic model reproduces near-critical avalanche branching with sigma around 1.00 versus the empirical target near 0.94.

It fails the spectral-slope and long-range-correlation tests: the model's aperiodic slope is about 1.96 versus the empirical 1.18, and the DFA exponent is about 1.68 versus the empirical 0.68.

The authors therefore argue that the current formulation captures one criticality signature while remaining too smooth and too over-persistent in time.

### 7. What is actually novel?

The useful novelty is not just calling a brain model Hamiltonian. It is pairing a structure-preserving dynamics model with an explicit falsifiable validation ladder and reporting the failures rather than pretending the fitting loss already implies representational adequacy.

### 8. What are the strengths?

The by-subject held-out split is more serious than random sample splitting.

The paper checks model-independent invariants instead of only in-sample fit quality.

The structure-preserving formulation gives intervention and stability claims a clearer meaning than generic sequence models do.

The paper is refreshingly explicit about what it has not yet achieved.

### 9. What are the weaknesses, limitations, or red flags?

The model is fit to scalp EEG rather than source-space cortical dynamics with an individual structural connectome, so "digital twin" language is premature.

It fails two of the most important invariants it sets for itself, namely spectral slope and long-range temporal correlations.

The decisive perturbational validation rung, especially TMS-EEG prediction, is still absent.

The arXiv abstract page still exposed placeholder strings like FitTrainN and FitTestMSE even though the PDF contains the real values, which is a quality-control red flag.

### 10. What challenges or open problems remain?

The open problems are source-space identifiability, subject-specific inference with uncertainty, robust excitation-inhibition and criticality control, structural-connectome and delay priors, and actual perturbational validation under stimulation rather than only observational fitting.

### 11. What future work naturally follows?

Move to source-space and structural-connectome-informed fitting, add explicit excitation-inhibition control, fit subject-specific posteriors, and then test the stimulation ports on TMS-EEG or other perturbation datasets before making stronger closed-loop claims.

### 12. Why does this matter for cabbageland?

Because it gives a cleaner way to judge whether a control-flavored cortical model is earning its language. A model that talks about energy shaping, stimulation ports, or digital twins should be forced to clear invariants and perturbation tests it did not write for itself.

### 13. What ideas are steal-worthy?

Validate brain-dynamics models against invariants they did not author instead of only against reconstruction loss.

Separate branching success from spectral and temporal-correlation success rather than collapsing them into a single "criticality" victory lap.

Keep actuation and stability semantics explicit when proposing models for future neuromodulation use.

### 14. Final decision

Keep as a useful methods and control note. It is not evidence that closed-loop neuromodulation is solved, but it is a better-than-average example of a brain-dynamics paper that at least tries to earn its control rhetoric with falsifiable tests.
