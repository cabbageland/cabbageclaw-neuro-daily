# rTMS Modulates Static and Dynamic Brain Functional Networks in Children with Autism Spectrum Disorder: An EEG Microstate Study

## Basic info

* Title: rTMS Modulates Static and Dynamic Brain Functional Networks in Children with Autism Spectrum Disorder: An EEG Microstate Study
* Authors: Jiannan Kang and colleagues
* Year: 2026
* Venue / source: Brain Topography
* Link: https://pubmed.ncbi.nlm.nih.gov/42105161/
* Date surfaced: 2026-05-10
* Why selected in one sentence: It is a decent example of using network-level EEG readouts to inspect what stimulation changed, even if the clinical case is still thin.

## Quick verdict

* Useful

This is not a must-read autism-treatment paper. The sample is small, the target logic is conventional, and the accessible abstract does not make a strong behavioral-efficacy case. Still, it is worth keeping because it reports a useful split: standard microstate temporal summaries were mostly negative, while static connectivity and dynamic complexity shifted after active stimulation. That makes it more informative than a simple symptom-before-versus-after study.

## One-paragraph overview

The paper randomizes thirty-two children with autism spectrum disorder to active or sham one-hertz dorsolateral prefrontal repetitive transcranial magnetic stimulation over nine weeks, with resting-state EEG and behavioral assessment before and after treatment. The analysis combines microstate temporal parameters, weighted phase-lag-index functional connectivity, and fuzzy-entropy measures of dynamic complexity. Intrinsic features of Microstate B were associated with social relating deficits. Active stimulation did not show clear interaction effects in standard microstate timing metrics, but it did increase static connectivity strength and dynamic complexity across microstates. The useful read is that network integration and flexibility may move even when more familiar microstate summary statistics do not.

## Model definition

This paper does not present a trainable predictive model. It uses EEG feature extraction and group comparison.

### Inputs
Resting-state EEG from thirty-two children with autism spectrum disorder, active versus sham one-hertz dorsolateral prefrontal rTMS assignment, and behavioral assessments before and after a nine-week intervention.

### Outputs
Microstate temporal parameters, weighted phase-lag-index static functional connectivity, fuzzy-entropy dynamic-complexity measures, and associations with behavioral deficits.

### Training objective (loss)
No trainable loss is described. The accessible text describes feature extraction plus randomized-group comparison.

### Architecture / parameterization
A multimodal EEG-analysis stack combining microstate metrics, static connectivity based on weighted phase-lag index, and dynamic complexity based on fuzzy entropy.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
rTMS has been explored for autism spectrum disorder, but it is still unclear what large-scale network changes, if any, accompany stimulation in this population.

### 2. What is the method?
Randomize children with autism spectrum disorder to active or sham dorsolateral prefrontal one-hertz rTMS, record resting-state EEG before and after nine weeks, and analyze microstates, static connectivity, and dynamic complexity.

### 3. What is the method motivation?
If stimulation changes clinically relevant network function, standard symptom scales alone may miss the mechanism. EEG-based network metrics can at least test whether stimulation shifts integration or flexibility.

### 4. What data does it use?
Thirty-two pediatric autism participants with resting-state EEG and behavioral assessments in an active-versus-sham randomized design.

### 5. How is it evaluated?
By comparing pre-to-post changes in EEG microstate features, connectivity, and complexity between active and sham groups, and by relating baseline microstate features to social deficits.

### 6. What are the main results?
Microstate B features were associated with social relating deficits. Standard microstate temporal parameters did not show significant interaction effects, but active rTMS increased static connectivity strength and dynamic complexity across microstates.

### 7. What is actually novel?
The main novelty is the combination of microstates, connectivity, and complexity in a sham-controlled pediatric rTMS study. The paper is more interesting for measurement framing than for target novelty.

### 8. What are the strengths?
- Sham-controlled randomized design.
- Uses multiple EEG views rather than relying on a single summary metric.
- Treats network flexibility as a candidate stimulation readout.
- Pediatric neuromodulation papers with any mechanistic readout are still relatively uncommon.

### 9. What are the weaknesses, limitations, or red flags?
- Thirty-two participants is small.
- The mechanistic meaning of increased connectivity and fuzzy-entropy complexity is still underspecified.
- The target and protocol logic are not especially personalized.
- The accessible abstract does not establish a strong symptom-linked causal story.

### 10. What challenges or open problems remain?
The field still needs better target justification, stronger linkage between EEG changes and behavioral benefit, and serious work on heterogeneity rather than treating autism as one stimulation problem.

### 11. What future work naturally follows?
Larger trials with individualized target logic, longitudinal EEG-state tracking, and explicit tests of whether baseline network features predict who benefits.

### 12. Why does this matter for cabbageland?
Because it is a useful reminder that stimulation readouts should not collapse onto one fashionable metric. If microstate duration is flat but complexity and connectivity move, the measurement framework may need to be richer.

### 13. What ideas are steal-worthy?
- Compare multiple network readouts instead of trusting one EEG summary family.
- Treat dynamic complexity as a candidate response marker, but only with skepticism and better linkage to mechanism.
- Use sham-controlled designs even in small pediatric neuromodulation work.
- Look for which metrics are actually sensitive to intervention, not just historically popular.

### 14. Final decision
Keep as a secondary note. It is more useful for readout design than for making strong clinical claims.
