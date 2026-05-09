# Stable depression subtypes identified using functional connectome normative deviation models and their response to rTMS

## Basic info

* Title: Stable depression subtypes identified using functional connectome normative deviation models and their response to rTMS
* Authors: Chengfeng Chen, and colleagues
* Year: 2026
* Venue / source: Molecular Psychiatry
* Link: https://pubmed.ncbi.nlm.nih.gov/42098265/
* Date surfaced: 2026-05-09
* Why selected in one sentence: It is one of the cleaner recent attempts to connect individual connectome-level heterogeneity to actual rTMS response instead of treating subtyping as an aesthetic exercise.

## Quick verdict

* Highly relevant

This is a useful stratification paper because it does not stop at identifying imaging clusters. It defines individual deviation maps relative to a healthy normative connectome model, finds two reproducible depression subtypes, and then asks whether those subtypes differ in rTMS outcome. The result is still preliminary and narrower than the title might tempt people to claim, but it is much more interesting than black-box prediction without a heterogeneity frame.

## One-paragraph overview

The study analyzes functional-connectivity data from 1,204 patients spanning different depression states and 1,636 healthy controls. The authors fit normative connectome models in healthy controls, compute patient-specific deviation maps, and cluster those deviations into two reproducible biological subtypes. Subtype 1 showed hyperconnectivity in somatomotor and ventral-attention networks with hypoconnectivity in frontoparietal and default-mode systems, while subtype 2 showed the opposite pattern. Only subtype 2 showed significant anhedonia improvement after dorsolateral prefrontal repetitive transcranial magnetic stimulation, and similarity to subtype-2 deviation structure tracked better anhedonia response. The interesting point is not that there are exactly two depression biotypes forever. It is that deviation-from-norm structure may be a more treatment-relevant way to represent heterogeneity than raw symptom labels or mean connectivity alone.

## Model definition

This paper contains several learnable or parameterized model components.

### Inputs
Resting-state functional connectome features from 1,636 healthy controls to build normative models, resting-state functional connectome features from 1,204 patients with depression to compute individual deviation maps, and rTMS outcome measures including anhedonia change after dorsolateral prefrontal stimulation.

### Outputs
Patient-specific functional-connectome normative deviation maps, cluster assignments into two depression subtypes, subtype-similarity scores for individual patients, and associations between subtype structure and rTMS response.

### Training objective (loss)
The accessible abstract does not specify the exact loss functions for the normative-connectome model or the clustering objective beyond reporting k-means clustering. It is fair to infer that the clustering objective is a k-means distortion-minimization criterion, but the normative-model loss should be treated as unspecified from the accessible text.

### Architecture / parameterization
A normative modeling pipeline over functional connectomes followed by k-means clustering of individual deviation maps, plus correlational analyses linking subtype structure and subtype-related deviation changes to rTMS outcome.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression is heterogeneous, and that heterogeneity weakens one-size-fits-all stimulation logic. The paper tries to identify biologically informed subtypes that are stable enough to matter and then test whether subtype membership changes rTMS response.

### 2. What is the method?
Build normative functional-connectome models from healthy controls, convert each depressed patient into an individual deviation map relative to that norm, cluster those maps into subtypes, and test subtype-specific response to dorsolateral prefrontal rTMS.

### 3. What is the method motivation?
A deviation-from-norm representation may capture patient-specific pathology more directly than raw case-control averages. If those deviations sort patients into response-relevant groups, stimulation targeting and trial design could become less blunt.

### 4. What data does it use?
Resting-state functional connectivity from a large multisubject depression sample and a large healthy-control sample, plus symptom-response data after dorsolateral prefrontal rTMS. The accessible abstract does not provide enough detail to judge site structure, scanner heterogeneity, or protocol variability.

### 5. How is it evaluated?
By reproducibility of the two-subtype solution across clinical and methodological conditions, by subtype differences in network-deviation patterns, and by testing whether subtypes differ in anhedonia improvement after rTMS.

### 6. What are the main results?
Two reproducible subtypes emerged with opposing patterns across somatomotor, ventral-attention, frontoparietal, and default-mode networks. Only subtype 2 showed significant anhedonia improvement after rTMS, and greater similarity to subtype-2 deviation structure predicted better improvement.

### 7. What is actually novel?
The useful novelty is not merely clustering depression. It is the combination of normative deviation modeling with a treatment-response test, which gives the subtype idea at least some intervention relevance.

### 8. What are the strengths?
- Large sample relative to many connectome-stratification papers.
- Heterogeneity is represented at the individual-deviation level rather than hidden in averages.
- Response testing against rTMS makes the subtype claim more than descriptive.
- The network interpretation is legible enough to think about targeting and mechanism.

### 9. What are the weaknesses, limitations, or red flags?
- The accessible text does not show whether the normative model and subtype solution generalize cleanly across sites and acquisition pipelines.
- The response result seems strongest for anhedonia rather than broad syndrome remission.
- K-means-derived subtype stories can look stable until a genuinely independent dataset challenges them.
- It is still unclear whether this result should change target selection, protocol choice, or patient selection in practice.

### 10. What challenges or open problems remain?
The field still needs external validation, stronger protocol-specific analysis, and a more explicit mapping from subtype structure to intervention logic rather than post hoc response association.

### 11. What future work naturally follows?
Independent replication across sites, testing whether subtype assignment should change target or protocol, and comparison against simpler stratification baselines such as symptom dimensions or standard connectivity markers.

### 12. Why does this matter for cabbageland?
Because it is exactly the kind of paper that tries to make heterogeneity operational instead of rhetorical. It matters for personalized targeting, response prediction, and the larger question of whether connectome-level deviation maps can become useful control priors.

### 13. What ideas are steal-worthy?
- Represent patients as deviations from a normative connectome rather than only as raw cases.
- Test subtype claims against intervention response instead of stopping at clustering.
- Use network-level deviation patterns as candidate priors for target or protocol selection.
- Treat anhedonia-specific response effects as potentially more informative than undifferentiated total-score change.

### 14. Final decision
Keep. This is an early but worthwhile network-psychiatry paper that takes heterogeneity and treatment response more seriously than most subtype work.