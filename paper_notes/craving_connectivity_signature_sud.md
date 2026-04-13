# Brain Functional Connectivity Signatures of Craving Across Substance Use Disorders: A Transdiagnostic Approach

## Basic info

* Title: Brain Functional Connectivity Signatures of Craving Across Substance Use Disorders: A Transdiagnostic Approach
* Authors: Justin Böhmer, Luisa-Felicitas Esch, Katharina Eidenmueller, Richard O. Nkrumah, Lea Wetzel, Pablo Reinhardt, Norman Zacharias, Georg Winterer, Patrick Bach, Rainer Spanagel, Gabriele Ende, Wolfgang H. Sommer, Henrik Walter
* Year: 2026.
* Venue / source: bioRxiv preprint.
* Link: https://www.biorxiv.org/content/10.64898/2026.04.02.716016v1
* Date surfaced: 2026-04-13.
* Why selected in one sentence: It tries to derive a transdiagnostic network biomarker of craving instead of staying trapped in single-substance silos.

## Quick verdict

* Useful

This is worth keeping because the authors at least attempt the right abstraction level. Instead of building a craving model inside one diagnosis and pretending it generalizes, they use connectome-based predictive modeling across cannabis, opioid, and tobacco use disorders and then test the resulting network in external alcohol and smoking datasets. The main caveat is that this remains resting-state prediction, so it is still much closer to biomarker association than intervention-ready mechanism.

## One-paragraph overview

The paper uses resting-state functional MRI to build a distributed predictive network for subjective craving across multiple substance use disorders. In a transdiagnostic training sample of seventy-eight participants with cannabis, opioid, or tobacco use disorder, the authors apply connectome-based predictive modeling to identify a network whose connectivity predicts self-reported craving. Computational lesion analysis suggests important contributions from the right medial orbitofrontal cortex, right dorsal posterior cingulate cortex, and left lateral medial frontal gyrus. The authors then test the network in two external settings: alcohol-dependent patients and smokers. According to the abstract, the network predicts distinct cognitive and motivational craving components in alcohol dependence and also predicts abstinence-related craving and within-person craving change in smokers.

## Model definition

### Inputs
Resting-state functional MRI connectivity features from individuals with substance use disorders.

### Outputs
Predicted self-reported craving levels or craving-related components, plus in external data the ability to predict abstinence-related craving and within-person changes in craving state.

### Training objective (loss)
The abstract does not specify the exact loss or fitting objective. It states that connectome-based predictive modeling was used to identify a distributed network predictive of craving.

### Architecture / parameterization
A connectome-based predictive modeling framework operating on distributed functional connectivity features, followed by computational lesion analyses to identify influential nodes.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Craving is a central relapse-relevant construct across substance use disorders, but reliable biomarkers at the individual level remain weak. The paper tries to identify a functional-connectivity signature of craving that generalizes across substances.

### 2. What is the method?

The authors use connectome-based predictive modeling on resting-state functional MRI in a transdiagnostic sample, then test the identified network in independent external datasets.

### 3. What is the method motivation?

If craving reflects partly shared circuitry across substance classes, then a cross-diagnosis network may be more useful than diagnosis-specific models that overfit narrow cohorts.

### 4. What data does it use?

The training sample includes seventy-eight individuals with cannabis, opioid, or tobacco use disorder. External validation used one alcohol-dependence dataset with forty-one participants and one smoker dataset with twenty-eight participants.

### 5. How is it evaluated?

Evaluation focuses on whether the derived craving network predicts self-reported craving in the transdiagnostic sample and whether that prediction generalizes to external datasets and to different aspects of craving.

### 6. What are the main results?

The authors report that the distributed craving network reliably predicted self-reported craving in the transdiagnostic sample. The network generalized to alcohol-dependent patients, where it predicted distinct cognitive and motivational components of craving, and to smokers, where it predicted abstinence-related craving and within-subject craving change between sated and craving states.

### 7. What is actually novel?

The main novelty is the transdiagnostic framing plus external generalization, not the basic use of connectome-based predictive modeling itself.

### 8. What are the strengths?

The paper aims above single-disorder biomarker provincialism.

External validation is the correct move and is still missing from many neuroimaging biomarker papers.

The lesion analysis adds at least some network interpretation instead of leaving the result as a black-box edge list.

### 9. What are the weaknesses, limitations, or red flags?

Resting-state functional-connectivity prediction remains associational and vulnerable to preprocessing, site effects, and leakage problems.

Sample sizes are not huge, especially in the external datasets.

The network being predictive does not mean its nodes are causal intervention targets.

The abstract does not provide robustness checks, permutation details, or effect-size calibration.

### 10. What challenges or open problems remain?

The major open problem is whether the identified network predicts longitudinal outcomes such as relapse, treatment response, or stimulation sensitivity. Another is whether the signature remains stable across scanners, pipelines, and more heterogeneous clinical cohorts.

### 11. What future work naturally follows?

The obvious next step is prospective testing against relapse or treatment trajectories. A stronger next step would be to combine the network with perturbational or longitudinal data to move from biomarker association toward mechanism.

### 12. Why does this matter for cabbageland?

Because transdiagnostic psychiatry is only useful when it produces better intervention or prediction logic rather than broader vagueness. This paper is not there yet, but it is closer than diagnosis-silo work that rediscovers the same craving story separately for every substance.

### 13. What ideas are steal-worthy?

One steal-worthy idea is to evaluate craving-related biomarkers across substances by default rather than treating each drug class as a separate universe.

Another is to distinguish cognitive and motivational components of craving during validation, not just a single scalar score.

A third is to use lesion-style network ablation for interpretation, while staying honest that interpretability is not causality.

### 14. Final decision

Keep as a useful adjacent network-psychiatry note. It is stronger than ordinary resting-state biomarker packaging, but it is still several steps away from intervention-ready mechanism.
