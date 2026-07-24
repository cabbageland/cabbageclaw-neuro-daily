# Subthreshold violations of trajectory predictions are sensitive to TMS of cerebellum Crus I/II

## Basic info

* Title: Subthreshold violations of trajectory predictions are sensitive to TMS of cerebellum Crus I/II
* Authors: Ellen Joos, Camille Scherer, Philippe Isope, Jack Foucher, Anne Giersch
* Year: 2026
* Venue / source: NeuroImage: Reports
* Link: https://pubmed.ncbi.nlm.nih.gov/42495160/
* Date surfaced: 2026-07-24
* Why selected in one sentence: It actually tests a millisecond-scale visual prediction claim with both a subthreshold trajectory violation and cerebellar iTBS, then shows a cleaner neural effect than behavioral effect instead of bluffing a total win.

## Quick verdict

* Useful

This is a mechanistic perturbation paper worth preserving because it does not merely decorate itself with predictive-processing language. It creates a subthreshold trajectory violation, records EEG, and perturbs right cerebellar Crus I and II with sham-controlled iTBS. The main caution is that the TMS story is modest and order-dependent: the strongest effect is a neural modulation in perturbed trials, not a robust overall behavioral intervention effect. I inspected the accessible full text through PMC, so the caveats here come from the paper itself rather than from abstract fog.

## One-paragraph overview

The paper studies a visual collision illusion in which two briefly contacting moving squares can be perceived as separated by a gap. The authors ask whether the illusion depends on millisecond-scale trajectory prediction and sensory checking. To stress that claim, they introduce a subtle trajectory violation less than 60 milliseconds before the collision, measure EEG, and apply neuronavigated intermittent theta-burst stimulation to right cerebellar Crus I and II in a sham-versus-verum crossover. The trajectory perturbation reliably reduces the illusion rate and increases a late positive ERP over CP4. Verum cerebellar stimulation modulates that ERP on perturbed trials, but the effect appears only when verum is delivered in the second session. So the useful result is not that cerebellar TMS cleanly changes conscious perception. The useful result is that subthreshold trajectory checking looks real, cerebellar involvement remains plausible, and the neural signal is more convincing than the behavioral intervention claim.

## Model definition

### Inputs
Visual trials in which two squares move toward collision with either unperturbed or subtly perturbed trajectories, contact durations of 17, 33, or 200 milliseconds, sham versus verum cerebellar intermittent theta-burst stimulation, pre-versus-post intervention timing, and EEG recordings.

### Outputs
Behavioral reports of whether the squares touched or did not touch, illusion rates across conditions, and ERP amplitudes, especially the late positive signal over CP4 during perturbed trials.

### Training objective (loss)
There is no trainable predictive model in the machine-learning sense. The paper uses Bayesian statistical analyses with minimally informative priors to estimate condition effects, odds ratios, credible intervals, and intervention interactions.

### Architecture / parameterization
A within-subject psychophysics plus EEG experiment with MRI-guided cerebellar iTBS in sham-versus-verum crossover order, analyzed with Bayesian models of behavioral and electrophysiological effects rather than with a learned classifier or decoder.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper tries to determine whether a visual collision illusion depends on automatic millisecond-scale trajectory prediction and whether cerebellar circuitry contributes to detecting tiny violations of that predicted motion.

### 2. What is the method?
The authors recruit healthy adults, run a visual task where two squares move toward each other, insert subthreshold trajectory violations shortly before collision, record EEG, and compare sham versus verum intermittent theta-burst stimulation over right cerebellar Crus I and II in a crossover design.

### 3. What is the method motivation?
If the illusion relies on predictive checking rather than passive sensory registration, then a tiny trajectory irregularity should disrupt the illusion, and cerebellar perturbation should modulate the neural signature of that disruption.

### 4. What data does it use?
The study recruited 24 healthy young adults. After exclusions for task compliance, abnormal perception profiles, and acquisition issues, the main behavioral and EEG analyses were conducted on 19 participants, with 16 participants contributing to behavioral-ERP correlation analyses.

### 5. How is it evaluated?
Evaluation is done by comparing illusion rates and ERP amplitudes across non-perturbed versus perturbed trials, pre-versus-post intervention time points, sham versus verum stimulation, and session order. The paper reports Bayesian effect sizes, odds ratios, credible intervals, and posterior probabilities.

### 6. What are the main results?
- The subthreshold trajectory perturbation reliably reduces the illusion rate relative to non-perturbed trials.
- Perturbed trials produce higher late positive ERP amplitudes over CP4 than non-perturbed trials, in the rough window from 0.15 seconds to 2 seconds after contact.
- There is no convincing overall behavioral effect of verum cerebellar stimulation on perturbed trials.
- On perturbed trials, EEG amplitudes increase after verum TMS relative to before verum TMS, and the intervention-by-time interaction is strong.
- That EEG increase appears only when verum TMS is applied in the second session, which makes the intervention result order-dependent and therefore less clean than it first sounds.

### 7. What is actually novel?
The novelty is not just another cerebellar TMS study or another predictive-processing argument. The useful novelty is combining a subthreshold sensory prediction violation, EEG measurement, and sham-controlled cerebellar iTBS inside the same millisecond-scale task.

### 8. What are the strengths?
- The paper actually perturbs the claimed predictive process instead of merely inferring it from behavior.
- Full task logic, TMS targeting, and result caveats are visible in accessible full text.
- The cerebellar stimulation is MRI-guided and neuronavigated rather than hand-waved.
- The authors separate behavioral and neural effects instead of forcing a fake unified success story.
- Bayesian analysis is a reasonable choice for a small exploratory dataset and makes the uncertainty visible.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is small, with 19 analyzed participants in the main datasets.
- The TMS effect is stronger in ERP than in behavior, which limits intervention-level conclusions.
- The clearest intervention effect is order-dependent, appearing only when verum TMS is delivered in the second session.
- This is a healthy-young-adult psychophysics study, not a clinical perturbation paper.
- The task is narrow and somewhat idiosyncratic, so generalization to broader predictive-processing or neuromodulation settings is unearned.

### 10. What challenges or open problems remain?
The biggest open problems are replicating the order-sensitive ERP effect in a larger sample, clarifying whether the cerebellum is specifically necessary rather than merely part of a broader circuit, and showing whether stronger or differently timed stimulation changes behavior more convincingly.

### 11. What future work naturally follows?
Larger preregistered replications, active-control stimulation sites, online or phase-specific perturbation rather than a brief offline iTBS block, patient-population extensions for disorders with altered predictive processing, and integration with whole-brain perturbation models would all follow naturally.

### 12. Why does this matter for cabbageland?
Because it is a good example of how to make a mechanistic claim earn its keep. If you want to talk about prediction, state checking, or cerebellar timing in intervention logic, this paper shows a better standard: perturb the stream, perturb the putative predictor, record the neural consequence, and do not pretend the behavioral story is cleaner than it is.

### 13. What ideas are steal-worthy?
- Use subthreshold task violations to assay whether a proposed predictive computation is actually live.
- Treat neural sensitivity and behavioral sensitivity as separable readouts instead of demanding they move together immediately.
- Use cerebellar timing machinery as a candidate component in rapid sensory regularity checking, but require perturbational evidence before saying so loudly.
- Prefer papers that leave visible where the mechanism stops being demonstrated and starts being conjectured.

### 14. Final decision
Preserve. This is not a must-read or a clinically decisive paper, but it is a useful mechanistic note because it actually stresses the prediction claim and surfaces a cerebellum-sensitive ERP effect without pretending the behavioral intervention result is already settled.
