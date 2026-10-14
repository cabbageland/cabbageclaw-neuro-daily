# Excitation-Inhibition Balance and Fronto-Limbic Connectivity Distinguish TMS Treatment Outcomes in Refractory Depression

## Basic info

* Title: Excitation-Inhibition Balance and Fronto-Limbic Connectivity Distinguish TMS Treatment Outcomes in Refractory Depression
* Authors: Davide Momi; Zheng Wang; Mohammad P. Oveisi; Kevin Kadak; Sorenza P. Bastiaens; Jennifer I. Lissemore; Yoshihiro Noda; Jonathan Downar; Fidel Vila Rodriguez; Rebecca Strafella; Zafiris J. Daskalakis; Christoph Zrenner; Reza Zomorrodi; Camarin E. Rolle; Manish Saggar; Nolan Williams; Corey J. Keller; Daniel M. Blumberger; Daphne Voineskos; John D. Griffiths
* Year: 2026
* Venue / source: Biological Psychiatry; full text inspected through the bioRxiv preprint version
* Link: https://pubmed.ncbi.nlm.nih.gov/42863782/
* Date surfaced: 2026-10-14
* Why selected in one sentence: It links iTBS response in refractory depression to a concrete TMS-EEG plus whole-brain-modeling mechanism: inhibitory-shift physiology and DLPFC-sgACC state dynamics.

## Quick verdict

* Highly relevant

This is a strong translational neuromodulation preserve, with one serious caveat: the accessible full text was the bioRxiv preprint, while the final Biological Psychiatry page was blocked in this environment. The paper still earns a note because the PubMed record confirms the accepted version and the inspected full text exposes enough method and result detail to judge the mechanism. The useful contribution is not merely another depression-TMS biomarker claim; it tries to connect treatment response to fitted Jansen-Rit parameters, frontolimbic state geometry, and perturbation response.

## One-paragraph overview

The paper studies 90 patients with treatment-resistant depression who received left DLPFC intermittent theta-burst stimulation and had TMS-EEG measured before and after treatment. The authors fit a connectome-based Jansen-Rit whole-brain model to the TMS-evoked EEG responses, then ask which model-derived physiological and state-space features separate responders from non-responders. Responders show larger post-treatment reductions in 3-10 Hz induced power, and the model interprets that reduction as a shift toward greater inhibitory control, especially reduced pyramidal-to-excitatory drive and increased inhibitory-to-pyramidal feedback. A pre-treatment model-derived brain state also separates responders, with opposite-polarity DLPFC and sgACC loadings that echo the familiar fMRI sgACC-anticorrelation targeting literature. The paper is best read as a mechanistic biomarker study, not a finished clinical decision rule: it lacks sham control, uses normative rather than subject-specific structural connectivity, and needs external validation.

## Model definition

### Inputs

The model uses single-pulse TMS-EEG recordings before and after a 30-session iTBS course, HRSD-17 depression scores, responder/non-responder status, a 200-region Schaefer cortical atlas, a normative HCP-derived structural connectome, a lead-field mapping from source parcels to EEG channels, and TMS perturbation of the left DLPFC target.

### Outputs

The model emits simulated TMS-evoked EEG waveforms, fitted subject/session-level Jansen-Rit parameters, derived excitatory-inhibitory balance summaries, model-derived neural population time series, latent brain-state components, DLPFC/sgACC state loadings, sgACC engagement measures, and state-space trajectory metrics including post-treatment deviation and distance to a stable fixed point.

### Training objective (loss)

The goodness-of-fit loss compares simulated and empirical TMS-EEG time series. The authors optimize model parameters with autodiff-computed gradients and the Adam algorithm, then assess waveform similarity with Pearson correlations and permutation-based null distributions. The exact scalar loss formula is not fully specified in the accessible text beyond fitting simulated to empirical TMS-EEG waveforms.

### Architecture / parameterization

This is a connectome-based whole-brain neural mass model. Each of 200 cortical parcels contains a Jansen-Rit cortical column with pyramidal, excitatory interneuron, and inhibitory interneuron populations; parcels are coupled through a normative structural connectome; TMS is modeled as a perturbing voltage offset to pyramidal-cell membrane potential; simulated parcel time series are projected to EEG channel space through a lead field. Downstream analyses use time-frequency statistics, repeated-measures ANOVA on model parameters, singular value decomposition, mean-centered partial least squares, bootstrap/permutation inference, and state-space trajectory geometry.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Depression iTBS is clinically useful but still behaves like a trial-and-error intervention for many patients. The paper tries to identify neurophysiological mechanisms and pre-treatment state markers that explain why some refractory-depression patients respond while others do not.

### 2. What is the method?

The authors combine longitudinal TMS-EEG with connectome-based whole-brain modeling. They fit individual pre- and post-treatment TMS-evoked responses with a Jansen-Rit model, compare spectral changes and fitted physiological parameters between responders and non-responders, use PLS to find model-derived brain states that separate outcome groups, and analyze state-space trajectories before and after iTBS.

### 3. What is the method motivation?

TMS-EEG gives a perturbational readout of circuit reactivity, but raw components and scalp spectra are hard to interpret mechanistically. A physiologically parameterized whole-brain model can translate evoked responses into interpretable candidate mechanisms, such as altered excitatory drive, inhibitory feedback, frontolimbic engagement, and attractor stability.

### 4. What data does it use?

The study uses data from 90 adults with major depressive disorder and treatment resistance who underwent TMS-EEG assessment before and after iTBS treatment. Eligibility included HRSD-17 score of at least 18 and inadequate response or intolerance to antidepressant trials. Treatment was 30 sessions over 6 weeks, 5 days per week, targeting left DLPFC, with 1200 pulses per day. Structural coupling in the model comes from averaged HCP diffusion tractography rather than each patient's own tractography.

### 5. How is it evaluated?

The paper evaluates spectral TMS-EEG changes, model fit to empirical waveforms, pre/post and responder/non-responder differences in Jansen-Rit parameters, correlations between fitted parameters and clinical scores, PLS-derived brain-state separation with permutation and bootstrap testing, sgACC engagement differences, and state-space trajectory differences between pre- and post-treatment responses.

### 6. What are the main results?

Responders show a significantly greater post-iTBS reduction in 3-10 Hz induced power than non-responders. In the model, this spectral reduction correlates with reduced pyramidal-to-excitatory drive, and simulations that increase inhibitory influence recapitulate reduced low-frequency power and late GMFA amplitude. Responders also show increased inhibitory-to-pyramidal feedback after treatment, whereas non-responders do not. A pre-treatment model-derived brain state distinguishes responders from non-responders, with DLPFC and sgACC loading in opposite directions; responders have stronger baseline sgACC engagement. In state-space analysis, responders show larger treatment-induced trajectory reorganization and closer convergence toward the fitted stable point after treatment.

### 7. What is actually novel?

The novel move is not saying that sgACC and DLPFC matter for depression TMS; that is old terrain. The useful move is integrating perturbational EEG with a physiologically interpretable model so the biomarker story becomes about inhibitory feedback, excitatory drive, state expression, and attractor geometry rather than only scalp components or static connectivity.

### 8. What are the strengths?

The paper uses a clinically relevant patient cohort, perturbational physiology, a model with interpretable parameters, and several converging analyses rather than one decorative biomarker. It connects TMS-EEG low-frequency suppression to a plausible E/I mechanism, ties pre-treatment state expression to the DLPFC-sgACC targeting literature, and treats response as a dynamical-system reconfiguration rather than a simple before/after mean effect. The accessible text is unusually explicit about methods, parameterization, and limitations.

### 9. What are the weaknesses, limitations, or red flags?

The biggest clinical limitation is no sham control for the analyzed response mechanism, so specific iTBS effects are not cleanly separated from nonspecific treatment and time effects. The structural connectome is normative, not patient-specific, which undercuts the "personalized" claim. The Jansen-Rit model is interpretable but simplified, and fitted parameters are not direct measurements of synaptic physiology. The treatment protocol uses 1200 pulses per day, not the most standard 600-pulse iTBS protocol, which complicates generalization. The predictive state needs external validation before it can be treated as a targeting or triage rule.

### 10. What challenges or open problems remain?

The field still needs prospective validation showing that these model-derived markers improve treatment selection, target choice, dose, or protocol adaptation. It also needs subject-specific structural connectivity, sham-controlled designs, robustness checks across EEG preprocessing/model-fitting pipelines, and comparison against simpler predictors such as baseline severity, conventional TMS-EEG components, resting-state connectivity, and target coordinates.

### 11. What future work naturally follows?

Good next work would validate the inhibitory-feedback and DLPFC-sgACC state markers in an independent cohort, test whether they forecast outcome before treatment rather than only explain it after outcome labeling, swap normative connectomes for subject-specific tractography, and use the fitted model to choose protocol parameters. The stronger version would close the loop: estimate state, choose stimulation settings, perturb, update the model, and test whether the intervention moves the patient toward the responder-like state.

### 12. Why does this matter for cabbageland?

It is exactly the kind of paper that makes interventional psychiatry less mushy. It links a clinical neuromodulation outcome to perturbational physiology and model-derived state dynamics, while keeping the DLPFC-sgACC targeting story connected to actual evoked responses. For cabbageland, the transferable frame is that stimulation response should be modeled as state-dependent circuit reconfiguration, not just "hit left DLPFC and hope."

### 13. What ideas are steal-worthy?

- Treat TMS-EEG as a perturbational assay for state-dependent controllability, not just a biomarker fishing pond.
- Separate pre-treatment state eligibility from post-treatment mechanism: one marker may say who is reachable, another may say what changed.
- Put E/I balance into the model as an interpretable latent mechanism, but do not pretend fitted Jansen-Rit parameters are direct synaptic measurements.
- Use DLPFC-sgACC anticorrelation as a hypothesis about dynamical coupling, not as a ritualized targeting slogan.
- Pair state-space trajectory analyses with clinical response so "stability" and "attractor" language has quantitative teeth.

### 14. Final decision

Keep. The paper is not deployment-ready precision psychiatry, but it is a high-signal mechanistic biomarker study. Its best use is as a bridge between TMS-EEG physiology, whole-brain modeling, DLPFC-sgACC targeting, and closed-loop/adaptive neuromodulation design.
