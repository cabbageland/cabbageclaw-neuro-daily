# Human brain changes after first psilocybin use

## Basic info

* Title: Human brain changes after first psilocybin use
* Authors: T. Lyons, M. Spriggs, L. Kerkela, et al.
* Year: 2026
* Venue / source: Nature Communications
* Link: https://doi.org/10.1038/s41467-026-71962-3
* Date surfaced: 2026-06-27
* Why selected in one sentence: It is one of the cleaner recent attempts to connect acute psychedelic state metrics, one-month structural brain changes, and downstream psychological outcomes without pretending they are all the same thing.

## Quick verdict

* Highly relevant

This is a preserve note because it is unusually useful for sorting acute psychedelic signal from durable change. The paper is based on full-text inspection and the main contribution is not "psilocybin raises entropy" as a slogan. It shows robust acute EEG entropy changes, modest but nonzero one-month white-matter and modularity effects, and a plausible mediating role for next-day psychological insight. The important caveat is that this is still an exploratory fixed-order healthy-volunteer study, so it sharpens biomarker and mechanism language more than it proves therapeutic neuroplasticity.

## One-paragraph overview

The study followed 28 healthy, psychedelic-naive adults in a single-blind, placebo-controlled, fixed-order repeated-measures design in which participants received 1 mg psilocybin and then 25 mg psilocybin one month later. Resting-state EEG was recorded during dosing, and diffusion MRI plus fMRI were collected before and one month after each session. Acute 25 mg psilocybin increased EEG signal diversity, lowered alpha power, and produced intense subjective effects, while one-month follow-up showed decreased axial diffusivity in overlapping prefrontal-striatal and prefrontal-thalamic tracts plus a decrease in network modularity relative to baseline. The strongest interpretive move is not that the brain became generically "more entropic." It is that acute cortical signal diversity predicted next-day psychological insight and one-month well-being, while the longer-lived brain changes were more anatomical than functional and were measured with enough caution that the paper does not fully hype itself into nonsense.

## Model definition

The paper contains learned statistical prediction components rather than a treatment-selection controller or large machine-learning model.

### Inputs
Acute resting-state EEG features, especially electrode-level Lempel-Ziv complexity across multiple post-dose timepoints; one-month diffusion and resting-state fMRI metrics such as axial diffusivity and network modularity; and participant-reported psychological outcomes including insight and well-being.

### Outputs
The predictive components estimate next-day psychological insight and one-month well-being change, and the correlational analyses link one-month imaging changes to contemporaneous well-being change.

### Training objective (loss)
The accessible full text indicates cross-validated predictive modeling, regression, correlation, and mediation-style path analysis. The exact optimization loss is not stated clearly in the inspected text slices, so I am not going to bluff a specific objective beyond out-of-sample prediction and regression fit.

### Architecture / parameterization
An exploratory multimodal statistical stack: linear mixed-effects models for dose-by-time effects, EEG cluster-based analyses, tract-level DTI comparisons, resting-state network modularity analyses, cross-validated predictive models using acute EEG features, and a regression-based mediation or path model linking entropy, next-day insight, and one-month well-being.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper asks whether a first high-dose psilocybin experience leaves durable brain changes in humans, and whether acute brain-state markers can predict later psychological change. That is a better question than simply asking whether psychedelics feel intense or whether "brain entropy" goes up on drug.

### 2. What is the method?
Participants completed two dosing sessions in fixed order, first 1 mg and then 25 mg psilocybin one month later. The authors measured acute resting-state EEG during dosing and measured diffusion MRI plus fMRI before and one month after each session, then related those neural measures to later insight, well-being, and cognitive-flexibility outcomes.

### 3. What is the method motivation?
The motivation is to bridge timescales. Acute psychedelic studies often stop at on-drug phenomenology, while long-term therapy papers often skip the mechanistic link between the acute state and later change. This paper tries to trace a path from acute cortical dynamics to delayed psychological and anatomical changes.

### 4. What data does it use?
Twenty-eight healthy adults, all psychedelic-naive, participated in a single-blind repeated-measures study. EEG was sampled during both dosing sessions, and diffusion MRI plus fMRI were acquired before dosing and one month after each session. Behavioral endpoints included subjective intensity, psychological insight, well-being, and an extradimensional set-shifting measure of cognitive flexibility.

### 5. How is it evaluated?
Evaluation uses linear mixed-effects models for acute EEG and behavioral dose-by-time effects, DTI tract analyses for one-month anatomical change, resting-state modularity analyses for one-month functional-network change, and correlational plus mediation-style models connecting acute EEG entropy to next-day insight and later well-being. The most relevant comparisons are 25 mg versus 1 mg and post-25 mg versus post-1 mg at the one-month horizon.

### 6. What are the main results?
Acute 25 mg psilocybin significantly increased EEG Lempel-Ziv complexity at one and two hours and significantly reduced alpha power, while 1 mg produced no comparable signal. At one month, axial diffusivity decreased in overlapping bilateral prefrontal-striatal and prefrontal-thalamic tracts, and the DTI effects survived free-water correction. Group-average long-term fMRI changes were modest, but decreased network modularity correlated with improved well-being. Psychological insight was higher at one day, two weeks, and one month after 25 mg versus 1 mg, well-being improved at two weeks and one month, and fewer extradimensional shift errors suggested better cognitive flexibility. Acute EEG entropy predicted next-day insight and one-month well-being, and the path model suggested that insight mediated part of the entropy-to-well-being relationship.

### 7. What is actually novel?
The useful novelty is the bridge across modalities and timescales in first-time psychedelic users. The paper does not only say that psilocybin acutely perturbs the brain, and it does not only say that people later report feeling better. It explicitly tests whether acute EEG complexity, delayed tract changes, delayed network integration, insight, and well-being line up in one mechanistic story.

### 8. What are the strengths?
- The multimodal design is genuinely useful: EEG during drug, DTI and fMRI at one month, and psychological measures across time.
- The 1 mg session gives a control condition that looks functionally inactive rather than theatrically placebo-like.
- The paper is unusually explicit that long-term fMRI effects were mostly weak, which makes the positive findings more trustworthy.
- Psychological insight is treated as a mechanistic mediator rather than as decorative psychedelic folklore.
- The one-month DTI and modularity findings connect reasonably well to prior depression-focused psilocybin work without pretending the healthy-volunteer sample is equivalent.

### 9. What are the weaknesses, limitations, or red flags?
- The study is fixed-order rather than counterbalanced, so practice and expectation cannot be fully killed.
- The sample is only 28 healthy volunteers, not a clinical population.
- The long-term fMRI story is mostly null or weak, which limits any claim of durable functional reorganization.
- Axial diffusivity is biologically ambiguous, and the authors themselves warn against overinterpreting it as clean neuroplasticity.
- The DTI tracts overlap substantially, so the anatomical specificity is less crisp than a superficial read might suggest.
- The paper still leans on an "entropic brain" framing even while its own results show that not all entropy metrics move together.

### 10. What challenges or open problems remain?
The main open problems are replication, causal interpretation, and clinical transfer. We still do not know whether the DTI changes reflect meaningful therapeutic plasticity, whether acute entropy is a cause or a proxy, or whether the same relationships hold in depressed or otherwise clinically relevant populations.

### 11. What future work naturally follows?
The obvious next steps are randomized or counterbalanced designs, larger samples, multi-shell diffusion methods, and direct comparison of healthy volunteers against treatment-seeking cohorts. It would also be valuable to test whether acute EEG features can predict who shows durable clinical benefit when psychotherapy or structured integration is part of the intervention stack.

### 12. Why does this matter for cabbageland?
Because it makes psychedelic mechanism talk a little less mushy. The paper suggests that acute signal diversity, next-day insight, delayed structural route changes, and longer-term well-being may be related, but not interchangeable. That is a more serious framing for biomarker work and interventional psychiatry than treating "entropy" as a magic one-word explanation.

### 13. What ideas are steal-worthy?
- Pair acute state markers with delayed anatomical endpoints instead of pretending one timescale explains everything.
- Treat insight as a testable mediator rather than as a poetic afterthought.
- Use low-dose controls to pressure-test whether an imaging effect is genuinely drug-linked.
- Stop treating all entropy metrics as one construct and explicitly compare which ones track subjective and behavioral change.
- Look for route-level structural change, not just acute functional fireworks, when reasoning about durable intervention effects.

### 14. Final decision
Preserve. This is not a clean proof of therapeutic neuroplasticity, but it is one of the better recent papers for separating acute psychedelic state markers from slower anatomical and behavioral consequences.
