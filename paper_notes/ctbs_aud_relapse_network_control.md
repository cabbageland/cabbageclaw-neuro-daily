# Optimizing brain functional-structural architecture with cTBS to reduce relapse in alcohol use disorder: a randomized controlled trial

## Basic info

* Title: Optimizing brain functional-structural architecture with cTBS to reduce relapse in alcohol use disorder: a randomized controlled trial
* Authors: Zhou-Kang Wu, Jing-Nan Zhao, Ning-Ning Zeng, Liang-Jie-Cheng Huang, Ying-Ying Li, Guang-Heng Dong, Min Wang, Jian-Zhong Di, Hui Zheng
* Year: 2026
* Venue / source: Molecular Psychiatry
* Link: https://doi.org/10.1038/s41380-026-03747-5
* Date surfaced: 2026-07-16
* Why selected in one sentence: It is one of the rare fresh addiction-neuromodulation trials that pairs a randomized one-year relapse endpoint with a structurally constrained network-control story, even if the mechanistic stack is more ambitious than the sample really supports.

## Quick verdict

* Highly relevant

This is worth preserving because it has a real longitudinal endpoint instead of just a pre-post craving graph and a motivational speech about circuits. The paper's best claim is the one-year relapse hazard ratio, not the decorative tail of transcriptomics and cross-species mapping that comes afterward. The main caveat is that the sample is still small, the short-term AUDIT and craving outcomes are mostly flat, and the mechanistic analysis stack is doing a lot of work for fifty participants.

## One-paragraph overview

The study tests whether right-dorsolateral-prefrontal continuous theta-burst stimulation can reduce relapse risk in alcohol use disorder and whether any effect can be framed as improved top-down control over subcortical systems. Fifty participants were randomized to active or sham cTBS over two weeks, with pre-post clinical scales, resting-state fMRI, diffusion MRI, and one-year relapse follow-up. The headline result is that active cTBS was associated with lower relapse risk over one year, with a hazard ratio of 0.426, even though short-term AUDIT and craving scores did not show significant group interactions. The mechanistic story is that active stimulation increased a relapse-protective prefrontal-subcortical ALFF component and reduced the control energy required for frontoparietal-to-subcortical transitions on a structural-connectome-constrained network-control model. That is more specific than the average addiction-stimulation paper, but it is still a small F4-targeted trial whose mechanistic layers should be treated as exploratory rather than settled.

## Model definition

This paper contains a multistage analytical stack rather than one single learned model.

### Inputs
Pre- and post-intervention resting-state fMRI ALFF features from 246 Brainnetome regions, participant-specific diffusion-MRI-derived structural connectomes, relapse labels over one-year follow-up, and clinical measures including AUDIT, craving, stress, impulsivity, withdrawal, sleep, and habit-reward-fear scales.

### Outputs
Five NMF-derived neural-oscillation components, TabPFN relapse-risk predictions, estimated control-energy costs for transitions from the frontoparietal network to other functional systems, and transcriptomic/cross-species maps linked to the spatial pattern of cTBS-related control-energy change.

### Training objective (loss)
The paper does not optimize one unified loss across the whole pipeline. NMF decomposes ALFF features into components while balancing reconstruction error and stability, with k set to 5 after repeated initializations. TabPFN is used as a classifier on the component-expression weights to predict relapse, evaluated with ROC metrics and stratified 5-fold cross-validation rather than custom hyperparameter tuning. The network-control analysis is not trained in the usual machine-learning sense; it computes minimum control energy under a linear state-space model constrained by each participant's structural connectome. The transcriptomic analysis uses partial least squares regression to maximize covariance between gene-expression structure and the control-energy change map.

### Architecture / parameterization
A multimodal pipeline: rs-fMRI preprocessing and ALFF extraction, NMF component discovery over 246 regional features, TabPFN plus SHAP for relapse prediction and feature ranking, deterministic tractography-based structural-connectome construction, linear network control theory for frontoparietal-to-target-state transitions, then imaging-transcriptomic partial least squares and TransBrain cross-species phenotype mapping.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Alcohol use disorder has high relapse rates, and addiction neuromodulation papers often promise circuit repair without showing either durable clinical benefit or a plausible route from scalp target to craving-related circuitry. This paper tries to address both problems at once.

### 2. What is the method?
Run a single-center randomized double-blind sham-controlled cTBS trial over the right DLPFC, collect pre-post clinical and imaging data, model relapse-associated resting-state patterns with NMF plus TabPFN, estimate structurally constrained frontoparietal control energy with network control theory, and then relate the resulting spatial effect map to gene-expression and murine-homology analyses.

### 3. What is the method motivation?
The stated motivation is that alcohol relapse reflects weak top-down control over bottom-up reward and salience systems. If cTBS helps, the authors want the benefit to show up not just in questionnaires, but in how easily a frontoparietal control system can theoretically regulate subcortical circuitry.

### 4. What data does it use?
Fifty adults with alcohol use disorder, aged 18 to 60, with final analyzed groups of 29 active and 21 sham participants. Each participant had baseline and post-intervention clinical assessments, resting-state fMRI, structural MRI, diffusion MRI, and relapse follow-up at 1, 3, 6, 9, and 12 months.

### 5. How is it evaluated?
Clinical scales are tested with repeated-measures ANOVA. Relapse is evaluated with a Cox proportional hazards model over one year. NMF components are fed into a TabPFN classifier with ROC and 5-fold cross-validation. Network control theory estimates frontoparietal-to-network transition energies before and after intervention, followed by regression and mediation tests linking energy change to AUDIT change.

### 6. What are the main results?
The active cTBS group had lower one-year relapse risk than sham, with a hazard ratio of 0.426 and a 95 percent confidence interval of 0.189 to 0.964. Short-term AUDIT and craving scores did not show significant time-by-group interactions, while perceived stress did improve. A prefrontal-subcortical ALFF component labeled C1 predicted relapse with AUC 0.906 and mean cross-validated AUC 0.878, and active cTBS increased C1 expression. Active stimulation also decreased frontoparietal-to-subcortical and frontoparietal-to-ventral-attention control energy, and the frontoparietal-to-subcortical reduction mediated AUDIT change. Gene-expression enrichment and TransBrain mapping then linked that effect map to neuroplasticity-related pathways and murine infralimbic and prelimbic regions.

### 7. What is actually novel?
The useful novelty is not "we used a lot of tools." It is combining a randomized addiction-neuromodulation trial with a genuine one-year relapse endpoint and a structurally constrained pathway-specific control model from stimulation target to subcortical circuitry. The transcriptomic and mouse-homology tail is newer packaging, but not the main reason to keep the paper.

### 8. What are the strengths?
- The trial is randomized, sham-controlled, and follows relapse for a full year instead of stopping at immediate symptom drift.
- The paper distinguishes durable relapse outcomes from short-term questionnaire change instead of conflating them.
- The network-control analysis is at least specific about which pathway changed: frontoparietal to subcortical, and frontoparietal to ventral attention.
- The mechanistic claims are tied to participant-specific structural connectomes rather than only to generic resting-state connectivity rhetoric.
- The authors surface several limitations directly, including sample size and exploratory mechanism status.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is small and unbalanced, with only 50 analyzed participants and wide uncertainty around the relapse hazard ratio.
- There was no significant short-term group interaction on AUDIT or craving, so the clinical picture is weaker than the headline relapse result alone suggests.
- The target was the scalp F4 location, not an individualized task-, connectome-, or physiology-guided site.
- The NMF, TabPFN, network-control, transcriptomic, and cross-species stack is too large for the sample to inspire full confidence, even with cross-validation.
- The network-control pipeline was not preregistered, and the authors explicitly call the mechanistic insights exploratory.
- Blinding integrity was not formally evaluated, which matters in a stimulation study where sensory differences can leak.
- The transcriptomic analysis uses healthy-donor AHBA expression maps, not disease-state or within-subject molecular data.

### 10. What challenges or open problems remain?
The obvious open problems are replication in larger multicenter cohorts, testing maintenance schedules, and comparing F4 targeting against individualized network-guided targeting. A second problem is deciding whether network-control metrics add enough practical value to justify the machinery relative to simpler and more robust biomarkers. A third is causal validation: the paper still infers pathway improvement rather than directly measuring stimulation-evoked propagation.

### 11. What future work naturally follows?
Run a larger preregistered trial with balanced groups and explicit blinding checks. Compare standard F4 targeting against subject-specific structural or functional targets. Add direct perturbation validation such as TMS-EEG, TMS-fMRI, or stimulation-evoked connectivity measures. Test whether maintenance cTBS or combination treatment can convert the relapse signal into clearer symptom-level change.

### 12. Why does this matter for cabbageland?
Because it is a relatively serious interventional psychiatry paper in a lane that is often sloppy. It treats relapse as the outcome that matters, not just immediate self-report drift, and it tries to quantify a specific control path from a cortical target into subcortical addiction circuitry. That does not make it precision therapy yet, but it is closer to useful intervention logic than the average addiction-rTMS paper.

### 13. What ideas are steal-worthy?
- Judge addiction-neuromodulation papers by time-to-relapse and durable outcomes, not just post-treatment craving snapshots.
- If a stimulation paper claims top-down control, force it to specify which pathway is supposed to get easier to regulate.
- Use structurally constrained network metrics as one candidate bridge between scalp target and downstream circuit effect, but keep them on a short evidential leash.
- Treat transcriptomic and cross-species overlays as hypothesis generators after the main clinical and circuit claims are already credible, not as substitutes for credibility.

### 14. Final decision

Preserve. This is not clean proof of precision neuromodulation for alcohol use disorder, and the mechanistic stack clearly outruns the sample. But the paper earns archive status because the clinical endpoint is real, the circuit story is more explicit than usual, and the combination is strong enough to serve as a future benchmark for addiction-neuromodulation claims.
