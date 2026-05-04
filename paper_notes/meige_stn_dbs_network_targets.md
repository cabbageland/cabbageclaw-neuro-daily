# Subthalamic nucleus deep brain stimulation in Meige syndrome: mapping the optimal stimulation sites and network targets

## Basic info

* Title: Subthalamic nucleus deep brain stimulation in Meige syndrome: mapping the optimal stimulation sites and network targets
* Authors: Wentao Zheng et al.
* Year: 2026
* Venue / source: Journal of Neurosurgery
* Link: https://pubmed.ncbi.nlm.nih.gov/42066342/
* Date surfaced: 2026-05-04
* Why selected in one sentence: It is a stronger-than-usual targeting paper because it combines local stimulation mapping, network mapping, and external validation in a rare-disease DBS setting.

## Quick verdict

* Useful

This is a solid translational targeting paper with better validation behavior than a lot of connectomic DBS mapping work. The best part is that it does not stop at a pretty sweet spot and then declare victory. It tests both local and network models in an independent cohort. The main limitation is that the network layer still relies on modeled stimulation effects and normative functional connectivity, so the mechanistic story remains suggestive rather than causal.

## One-paragraph overview

The study retrospectively analyzes long-term outcomes from sixty-five patients with Meige syndrome who underwent bilateral subthalamic nucleus deep brain stimulation across two centers. The authors use local stimulation modeling to identify an optimal subthalamic target zone and whole-brain connectivity mapping to identify network patterns associated with better motor outcomes, then test whether those patterns generalize to an independent validation cohort. Their central result is that good outcomes cluster in the dorsolateral sensorimotor subregion of subthalamic nucleus, extending toward associative territory, and that favorable stimulation patterns show positive connectivity to cerebellum and negative connectivity to somatosensory cortex. That does not prove circuit mechanism, but it is useful targeting evidence with more discipline than the average one-cohort map.

## Model definition

### Inputs
Patient-specific electrode locations, modeled local stimulation effects, and connectivity estimates linking those stimulation sites to distributed brain networks, together with clinical outcome scores.

### Outputs
Predicted or associated clinical improvement, plus inferred optimal local stimulation sites and favorable whole-brain connectivity patterns.

### Training objective (loss)
The accessible abstract does not specify an explicit optimization loss. The main learnable components are mapping models that relate local stimulation geometry and distributed connectivity patterns to clinical improvement and are then evaluated by correlation with outcomes in validation data.

### Architecture / parameterization
A connectomic DBS-mapping pipeline using Lead-Group Toolbox, DBS Sweet Spot Mapping Explorers, and DBS Network Mapping Explorers to estimate local sweet spots and network patterns associated with response.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Meige syndrome can respond to subthalamic deep brain stimulation, but optimal targeting within subthalamic nucleus and across distributed networks remains unclear. The paper tries to make targeting more explicit and more generalizable.

### 2. What is the method?

Retrospective two-center outcome analysis, local sweet-spot modeling, network-connectivity mapping, internal cross-validation, and external validation in an independent patient cohort.

### 3. What is the method motivation?

If response depends on both precise local engagement and broader circuit modulation, then target definition should include both anatomical and network structure rather than relying on one alone.

### 4. What data does it use?

Sixty-five bilateral subthalamic deep brain stimulation cases for Meige syndrome, with a training cohort of fifty patients and an independent validation cohort of fifteen patients, plus long-term motor outcome measurements using Burke-Fahn-Marsden Dystonia Rating Scale movement scores.

### 5. How is it evaluated?

By associating modeled local and network features with clinical improvement, then testing whether the sweet-spot and connectivity models correlate with outcomes in the independent validation cohort.

### 6. What are the main results?

Mean motor-score reductions were about sixty-three percent in the training cohort and fifty-six percent in the validation cohort. Optimal local effects were centered in dorsolateral sensorimotor subthalamic nucleus, extending toward associative territory. Better outcomes were linked to positive connectivity with cerebellum and negative connectivity with somatosensory cortex. Both local and network models retained significant correlations with outcome in the external cohort.

### 7. What is actually novel?

The paper's novelty is mainly procedural and translational: combining local and network mapping in Meige syndrome and validating both against an independent cohort rather than presenting a single-cohort connectomic story.

### 8. What are the strengths?

- Rare-disease DBS cohort with reasonably large sample for the indication.
- Local and network targeting are integrated rather than treated as competitors.
- External validation is a real strength.
- The result is concrete enough to inform programming and future targeting hypotheses.

### 9. What are the weaknesses, limitations, or red flags?

- Retrospective design.
- Network effects are inferred from modeled stimulation and normative connectivity, not directly measured patient-specific circuit dynamics.
- The validation cohort is still small.
- Correlation with outcome is useful but not the same as a causal targeting test.

### 10. What challenges or open problems remain?

The next challenge is to move from retrospective mapping to prospective targeting and programming tests, ideally with patient-specific physiology or imaging that can verify whether the inferred network really mediates benefit.

### 11. What future work naturally follows?

Prospective targeting studies, patient-specific connectivity modeling, adaptive programming tied to physiological markers, and cross-syndrome comparisons of whether dorsolateral subthalamic plus cerebellar-sensorimotor network logic generalizes beyond Meige syndrome.

### 12. Why does this matter for cabbageland?

Because it is a decent example of how connectomic targeting should be done if one insists on doing it at all: local anatomy, distributed network framing, and at least some attempt at out-of-sample validation.

### 13. What ideas are steal-worthy?

- Demand external validation for sweet-spot and network maps.
- Treat local target and network target as linked objects, not separate stories.
- Use network maps to generate programming hypotheses, not just paper figures.
- Be explicit that normative connectivity is a scaffold, not a mechanistic endpoint.

### 14. Final decision

Keep as a useful translational targeting note. Better than average mapping work, but still not enough to claim closed-loop or circuit-causal precision.