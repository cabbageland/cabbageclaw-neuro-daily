A Whole-Brain Dynamical Framework Linking Resting-State Activity to TMS-Evoked Responses.

This note was surfaced on July 22, 2026. The paper is by Andrea Veronese, Davide Momi, Simone Sarasso, Maurizio Corbetta, Michele Allegra, and Samir Suweis, and it is a bioRxiv preprint.

Quick verdict. Highly relevant.

Why it was selected in one sentence: it is one of the cleanest recent attempts to make resting-state dynamics and TMS-evoked propagation live inside the same tractable model instead of pretending they are separate problems.

This is a real keep because it improves intervention logic rather than just fitting another pretty whole-brain model. The useful move is not merely predicting TMS-evoked potentials. It is using resting-state EEG as a hard prior on the intrinsic scaffold, then allowing only a small, constrained effective-connectivity reconfiguration from a small TMS training subset. The caveat is equally obvious: the cohort is tiny, healthy, and much easier than a clinical depression population, and the prefrontal fits are visibly weaker than the motor fits.

One-paragraph overview.

The paper builds a connectome-coupled Hopf whole-brain model in which each Schaefer-200 parcel is a noisy Stuart-Landau oscillator. First, the authors derive a closed-form cross-spectral-density solution and fit each subject's resting-state EEG covariance and spectral structure, yielding local dynamical parameters plus a resting effective-connectivity scaffold. Second, they keep those local parameters fixed and re-optimize only effective connectivity using 10 percent of TMS-EEG trials for a given stimulation site, with the reconfiguration constrained to stay near the resting backbone. That hybrid model then predicts the remaining 90 percent of unseen TMS-evoked potentials. It performs strongly for motor stimulation, more modestly for prefrontal stimulation, and shows that group-level site-specific propagation templates can approximate the first part of the response. The main value is that it treats perturbation as a controlled deformation of intrinsic dynamics rather than a disconnected fitting exercise.

Now the model definition.

Inputs.

Source-resolved resting-state EEG, structural connectivity and delays derived from each subject's anatomy, source-to-sensor mappings, stimulation-site electric-field reconstructions, and a small training subset of TMS-EEG trials for the stimulated site.

Outputs.

Subject-specific local dynamical parameters, resting effective-connectivity matrices, stimulation-site-specific refined effective-connectivity matrices, and predicted spatiotemporal TMS-evoked potentials and time-frequency responses.

Training objective, or loss.

The resting-state stage fits the analytical covariance and spectral structure implied by the model to the empirical resting EEG. The TMS stage then refines only effective connectivity on a 10 percent training subset while constraining the refined matrix to remain close to the resting-state backbone. The accessible text does not spell out a single neat scalar loss in the compact form a machine-learning paper would.

Architecture and parameterization.

A connectome-coupled whole-brain Hopf model in which each cortical parcel is a noisy Stuart-Landau oscillator near bifurcation, combined with structural delays, source-to-sensor projection, SimNIBS-informed TMS input, and stimulation-specific effective-connectivity refinement.

Now the key questions.

First, what problem is the paper trying to solve?

It is trying to solve a common split-brain habit in TMS modeling: resting-state dynamics get analyzed in one framework, evoked responses in another, and the field quietly hopes the two belong to the same mechanism story. This paper asks for one model that can explain both.

Second, what is the method?

The method is a two-stage fit. First, fit a whole-brain Hopf model analytically to resting-state EEG, estimating local parameters and a resting effective-connectivity scaffold. Second, freeze those local parameters and refine only effective connectivity using 10 percent of TMS-EEG trials so the model can predict the remaining 90 percent of unseen TMS responses.

Third, what is the method motivation?

If TMS propagation depends on ongoing whole-brain dynamics, then resting activity should not be discarded after preprocessing. It should regularize the perturbation model and stop effective-connectivity inference from becoming a biologically silly overfitting machine.

Fourth, what data does it use?

The main dataset contains resting-state EEG and TMS-EEG from 12 healthy adults, with 11 usable resting datasets after artifact exclusion. The stimulation cohorts are split between prefrontal and motor sites, with additional premotor and parietal datasets used for cross-site generalization checks.

Fifth, how is it evaluated?

Resting-state fits are evaluated on held-out data using a block sequential split. TMS fits are trained on 10 percent of trials and tested on the remaining 90 percent using temporal and spatial goodness-of-fit metrics, spectral correlations, null comparisons against structural-connectivity-only models, donor-parameter swaps, donor-effective-connectivity swaps, and group-average propagation templates.

Sixth, what are the main results?

The resting-state model fits held-out EEG covariance well, with group mean R2 around 0.74.
The fitted local dynamics land in a supercritical regime with alpha-range intrinsic frequencies, giving the authors a self-sustained oscillatory scaffold rather than a noise-only rest model.
For motor stimulation, the model reproduces the triphasic TEP waveform and reaches mean R2 around 0.77 on unseen trials.
For prefrontal stimulation, it still captures the broad waveform and spectral motifs, but predictive accuracy drops to mean R2 around 0.50.
Premotor stimulation generalizes moderately from the motor setup, whereas parietal stimulation fails, which is actually useful because it shows the framework is spatially selective rather than universally mushy.
Group-average stimulation-specific effective-connectivity templates can approximate the early, roughly first-100-millisecond response, while later components remain more individualized.

Seventh, what is actually novel?

The novelty is not whole-brain modeling by itself. The useful novelty is the analytical rest-to-perturbation bridge: closed-form fitting of resting-state EEG, constrained refinement of stimulation-specific effective connectivity from only a small TMS subset, and explicit demonstration that structural connectivity alone is not enough.

Eighth, what are the strengths?

It gives resting-state activity a real mechanistic role instead of using it as decoration.
The analytical cross-spectral solution makes the model more interpretable and computationally tractable than many whole-brain fitting stacks.
The held-out TMS evaluation is real, not just an in-sample curve-hugging demo.
The null comparisons are useful because they show what the model is gaining beyond anatomy alone.
The group-template result is a nice compromise between individualized fitting and transferable propagation motifs.

Ninth, what are the weaknesses, limitations, or red flags?

The cohort is small and healthy, which makes any clinical translation claim premature.
The model needs a small TMS training subset, so it is not yet a pure rest-only predictor of perturbation.
Prefrontal fits are clearly weaker than motor fits, which hints that nonlinear and state-dependent recurrent dynamics are not fully captured.
Effective connectivity is still represented as a static refined matrix rather than a richer time-varying control object.
The framework depends on the quality of the structural scaffold and electric-field reconstruction.

Tenth, what challenges or open problems remain?

The main open problems are whether this framework survives clinical heterogeneity, whether it can predict useful perturbation responses with less stimulation data, how to represent nonlinear site-dependent reconfiguration more honestly, and whether the same logic can help choose or adapt stimulation targets rather than only explain them after the fact.

Eleventh, what future work naturally follows?

Apply the model in depression and other clinical TMS cohorts, test whether mid-course effective-connectivity reconfiguration predicts response, combine it with patient-specific field models and biomarker priors, and move from single-shot TEP prediction toward adaptive target or dose selection.

Twelfth, why does this matter for cabbageland?

Because model-based neuromodulation needs a bridge between intrinsic dynamics and perturbational spread. This paper is one of the better recent attempts to build that bridge without disappearing into black-box fitting theater.

Thirteenth, what ideas are steal-worthy?

Treat resting-state dynamics as a prior on perturbation, not a separate descriptive chapter.
Refine only the parameters that should actually move under stimulation instead of relearning the whole brain from scratch.
Use small stimulation subsets to estimate site-specific propagation motifs, then test generalization on held-out responses.
Separate what looks group-canonical in the early response from what stays individually state-dependent later.

Fourteenth, final decision.

Preserve. This is not the final answer to individualized TMS modeling, but it upgrades the conversation from anatomical wiring plus vibes to an actual rest-to-reactivity generative framework with meaningful held-out tests.
