# Circuit-targeted modulation of anxiety symptoms in individuals with major depression: A randomized head-to-head TMS trial

## Basic info

* Title: Circuit-targeted modulation of anxiety symptoms in individuals with major depression: A randomized head-to-head TMS trial
* Authors: Joseph J. Taylor et al.
* Year: 2026
* Venue / source: Molecular Psychiatry
* Link: https://pubmed.ncbi.nlm.nih.gov/41912790/
* Date surfaced: 2026-03-31
* Why selected in one sentence: It is a rare prospective test of a symptom-specific connectome targeting hypothesis in depression rather than another retrospective precision-TMS claim.

## Quick verdict

* Highly relevant

This is one of the cleaner recent psychiatry neuromodulation papers because it prospectively tests whether two connectome-derived targets shift different symptom dimensions. The effect is real enough to keep, but the evidence is still moderate rather than decisive: the sample is small, both arms improved depression similarly, and this is still target-level stratification rather than patient-specific individualized optimization. Still, it is better than decorative precision rhetoric.

## One-paragraph overview

The trial randomized adults with major depressive disorder who also had substantial anxiety symptoms to thirty TMS sessions at one of two circuit-derived targets: a dysphoric target near the conventional left dorsolateral prefrontal cortex site and an anxiosomatic dorsomedial target. The key claim was not that one target would beat the other on global improvement, but that the symptom mix improved would differ by circuit. That is broadly what they found: both targets improved depression similarly, while the anxiosomatic target improved anxiety more strongly. The useful contribution is that symptom-selective targeting was tested prospectively rather than reverse-engineered after treatment.

## Model definition

### Inputs
Baseline diagnosis of major depressive disorder with moderate-to-severe depressive and anxiety symptoms, assignment to one of two predefined TMS target coordinates, and repeated symptom measurements using the Beck Depression Inventory and Beck Anxiety Inventory across a thirty-treatment course.

### Outputs
Changes in depressive versus anxiety symptom burden, including relative improvement in BDI versus BAI and between-target comparisons of symptom reduction.

### Training objective (loss)
There is no learnable predictive model at the center of the accessible paper text. The core intervention logic is target assignment and symptom comparison, not model fitting.

### Architecture / parameterization
A randomized head-to-head clinical trial comparing two connectome-derived TMS target locations, one dysphoric and one anxiosomatic.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Standard TMS targeting for depression is too coarse. The paper asks whether different symptom dimensions within depression, especially anxiety versus dysphoric burden, map onto different stimulation targets strongly enough to matter prospectively.

### 2. What is the method?
Randomize adults with depression and clinically meaningful anxiety to thirty TMS treatments delivered either to a dysphoric target near conventional left dlPFC or to an anxiosomatic dorsomedial target, then compare the balance of improvement across depression and anxiety scales.

### 3. What is the method motivation?
Retrospective connectomic work has suggested that different brain circuits may preferentially modulate different symptom clusters. If true, target choice should not be treated as one-size-fits-all even inside one diagnostic label.

### 4. What data does it use?
The accessible abstract reports forty adults aged eighteen to sixty-five with major depressive disorder, Beck Depression Inventory score at least twenty, and Beck Anxiety Inventory score at least sixteen. Analyzable groups in the abstract are sixteen participants for the dysphoric target and twenty for the anxiosomatic target.

### 5. How is it evaluated?
By comparing within-arm and between-arm changes in BDI and BAI, including the ratio of depression improvement to anxiety improvement and the absolute magnitude of anxiety reduction after controlling for depression change.

### 6. What are the main results?
Both targets improved depressive symptoms by roughly similar percentages, fifty-five versus fifty-four percent. Anxiety improved more with the anxiosomatic target, fifty-eight versus thirty-six percent, and that difference remained significant after controlling for depression change. The ratio of BDI to BAI improvement also differed significantly between targets.

### 7. What is actually novel?
The novelty is not that TMS can help depression. The useful novelty is the prospective, randomized test of a symptom-circuit hypothesis that had previously been supported mainly by retrospective connectomic analysis.

### 8. What are the strengths?
- Prospective randomized design rather than retrospective targeting storytelling.
- Symptom-dimension framing is more precise than treating depression as one undifferentiated score.
- Head-to-head target comparison is more informative than target-versus-sham for this particular question.
- The result is mechanistically suggestive without pretending that one target is globally superior.

### 9. What are the weaknesses, limitations, or red flags?
- Small sample and likely limited power for finer subgroup or moderation claims.
- Not truly personalized targeting at the patient level; it is still a two-target protocol.
- Accessible text does not expose durability, adverse-event nuances, or target-engagement measures.
- Conflict-of-interest profile around connectivity-based targeting intellectual property deserves awareness, even if it does not invalidate the result.

### 10. What challenges or open problems remain?
Whether baseline symptom structure or baseline connectivity can be used to assign patients prospectively, whether these effects replicate in larger cohorts, and whether symptom-selective targeting can improve overall treatment efficiency rather than just rebalance symptom domains.

### 11. What future work naturally follows?
Larger stratified trials, patient-specific connectome-informed targeting, repeated target-engagement measurements, and designs that explicitly assign target based on pretreatment symptom or network phenotype.

### 12. Why does this matter for cabbageland?
Because it is a better version of a precision-neuromodulation claim. It operationalizes the idea that different symptoms may live on partially separable circuits and then tests that idea prospectively instead of merely drawing post hoc network maps.

### 13. What ideas are steal-worthy?
- Treat target selection as symptom-dimension selection rather than diagnosis-only selection.
- Use head-to-head target comparisons to test circuit specificity directly.
- Separate anxiety and depressive symptom change instead of collapsing them into one omnibus outcome.
- Demand prospective tests when connectomic targeting claims start sounding too smooth.

### 14. Final decision
Keep. This is not the final proof of precision psychiatry, but it is a real and nontrivial step toward symptom-specific circuit targeting in TMS.