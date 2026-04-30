# Target engagement in a head-to-head clinical trial of dysphoric versus anxiosomatic transcranial magnetic stimulation targets

## Basic info

* Title: Target engagement in a head-to-head clinical trial of dysphoric versus anxiosomatic transcranial magnetic stimulation targets
* Authors: Samantha Baldi et al.
* Year: 2026
* Venue / source: Neuropsychopharmacology
* Link: https://pubmed.ncbi.nlm.nih.gov/42014856/
* Date surfaced: 2026-04-30
* Why selected in one sentence: It directly tests whether symptom-specific circuit-TMS targets actually show distinct target engagement and whether the useful biomarker is induced connectivity change or baseline site-to-circuit architecture.

## Quick verdict

* Highly relevant

This is one of the more useful recent papers in circuit-targeted psychiatry because it is willing to report an awkward answer instead of pretending a clean personalization win. The target-engagement result is weaker than the field would like, but that is exactly why the paper is worth keeping. The strongest finding is that baseline connectivity from the chosen TMS site to the intended circuit predicts engagement and anxiety improvement better than pre-post connectivity change does.

## One-paragraph overview

The study analyzes a randomized head-to-head transcranial magnetic stimulation trial in thirty-six patients with depression and anxiety, with twenty-nine contributing pre and post treatment MRI. Patients received thirty sessions at either a dorsolateral prefrontal target meant to modulate a dysphoric symptom circuit or a dorsomedial prefrontal target meant to modulate an anxiosomatic circuit. The authors ask three sensible questions: whether the chosen target selectively changes its intended circuit, whether baseline connectivity from the stimulation site predicts that change, and whether either measure predicts symptom improvement. The sharp result is that both circuits showed connectivity decreases, but these changes were not cleanly target-specific and did not track symptom response. By contrast, stronger baseline site-to-circuit connectivity predicted greater connectivity change and better anxiety improvement, especially in the anxiosomatic arm.

## Model definition

### Inputs
Baseline resting-state functional connectivity from each individualized TMS site to the intended symptom circuit, plus pre and post treatment circuit connectivity estimates, treatment arm, and clinical symptom ratings.

### Outputs
Predicted circuit engagement, defined as pre to post change in average circuit connectivity, and associations with depression and anxiety symptom improvement.

### Training objective (loss)
There is no trainable predictive model described in the accessible abstract. The main analyses use group comparisons and Spearman partial correlations controlling for covariates.

### Architecture / parameterization
A circuit-targeted randomized clinical trial with individualized MRI-guided targeting and resting-state functional-connectivity analyses rather than a machine-learned model.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Circuit-based TMS often claims symptom specificity, but it is still unclear whether different targets actually engage distinct circuits in a measurable and clinically relevant way.

### 2. What is the method?
Randomize patients to two individualized TMS targets, measure resting-state connectivity before and after treatment, quantify target-circuit engagement, and test whether either induced connectivity change or baseline site connectivity predicts symptom improvement.

### 3. What is the method motivation?
If symptom-specific targeting is real, then target-specific circuit changes should appear after treatment, and pretreatment circuit architecture should plausibly constrain who responds.

### 4. What data does it use?
Thirty-six patients with depression and anxiety were randomized; twenty-nine had usable pre and post MRI. The intervention was thirty TMS sessions at either a dorsolateral prefrontal dysphoric target or a dorsomedial prefrontal anxiosomatic target, with Beck Depression Inventory and Beck Anxiety Inventory outcomes.

### 5. How is it evaluated?
By comparing connectivity change within the intended circuits across target groups, correlating baseline site connectivity with connectivity change, and correlating both biomarkers with symptom improvement while controlling for covariates.

### 6. What are the main results?
Connectivity decreased within both symptom circuits, but not in a clearly target-specific way, and those changes did not predict symptom improvement. Stronger baseline site connectivity to the targeted circuit predicted greater connectivity change and better anxiety improvement, with the clearest effect in the anxiosomatic target group.

### 7. What is actually novel?
The novelty is not that functional connectivity matters again. It is that the paper separates induced target engagement from baseline architectural suitability and shows that the latter may be the more informative biomarker.

### 8. What are the strengths?
- Randomized head-to-head target comparison instead of one-arm post hoc storytelling.
- Direct test of target engagement rather than only symptom change.
- Useful negative result on induced connectivity as a biomarker.
- Clinically relevant distinction between dysphoric and anxiosomatic targeting logic.

### 9. What are the weaknesses, limitations, or red flags?
- The MRI subset is small.
- The strongest biomarker effect appears mainly in the anxiosomatic arm.
- Resting-state connectivity remains an indirect measure of target engagement.
- The accessible text does not fully resolve preprocessing and multiplicity sensitivity.

### 10. What challenges or open problems remain?
Prospective validation in larger cohorts, better individual mapping of dysphoric circuitry, state-dependent engagement measures beyond resting-state MRI, and stronger mediation tests linking circuit change to symptom change.

### 11. What future work naturally follows?
Use baseline connectivity prospectively to constrain target selection, test richer engagement readouts such as concurrent TMS-EEG or symptom-time-series coupling, and explicitly model symptom-domain heterogeneity rather than expecting one depression target to do everything.

### 12. Why does this matter for cabbageland?
Because it sharpens a central intervention question: maybe the right biomarker is not how much connectivity changed after treatment, but whether the chosen site was structurally and functionally well positioned to move the intended circuit in the first place.

### 13. What ideas are steal-worthy?
- Separate baseline target suitability from induced target engagement.
- Treat negative target-engagement results as informative rather than embarrassing.
- Build personalization logic around site-to-circuit architecture, not just post-treatment averages.
- Keep symptom-domain-specific targets, but demand evidence that their circuit maps are individually stable enough to target.

### 14. Final decision
Keep. This is a useful reality-check paper for precision TMS. It weakens some easy target-engagement claims while strengthening the better idea that baseline site-to-circuit architecture may be the real biomarker to preserve.