# Target- and network-specific downstream effects of personalized precision transcranial magnetic stimulation: Evidence from concurrent functional neuroimaging

## Basic info

* Title: Target- and network-specific downstream effects of personalized precision transcranial magnetic stimulation: Evidence from concurrent functional neuroimaging
* Authors: Maximilian Lueckel, Angela Radetz, Umair Hassan, Kenneth Yuen, Florian Müller-Dahlhaus, Raffael Kalisch, Til Ole Bergmann
* Year: 2026
* Venue / source: bioRxiv, version 1, posted November 24, 2026; not peer reviewed
* Link: https://doi.org/10.64898/2026.11.10.765235
* Date surfaced: 2026-11-25
* Why selected in one sentence: It tests individualized connectivity/E-field targeting against nearby active control placements while measuring downstream responses, making target specificity harder to confuse with generic TMS co-stimulation.

## Quick verdict

* Highly relevant

Preserve for its counterfactual design, not as an antidepressant efficacy result. In healthy adults, negative-connectivity target stimulation changes sgACC/vmPFC BOLD more than nearby control stimulation, but the comparison with positive-connectivity targets is limited by unequal fields and connectivity separation. This is full-text inspection of the main PDF, including Methods, Results, Discussion, Table 1, and figure captions; supplementary material and data/code were not audited.

## One-paragraph overview

Twenty healthy adults received single-pulse TMS during fMRI at four individualized placements: left prefrontal targets negatively or positively connected to an sgACC/vmPFC network seed, plus a nearby active control for each. Connectivity maps were combined with gyral accessibility and simulated electric fields to optimize coil position/orientation; controls were designed to engage the target cluster less while remaining perceptually comparable. Negative-connectivity target stimulation produced more negative downstream sgACC/vmPFC BOLD than its control, whereas positive-target comparisons were not significant. The target–control contrast, unlike the individual condition maps, resembled a convergent depression circuit. The experiment supports specificity of the selected stimulation configuration; it does not isolate connectivity sign from anatomy/dose, measure neuronal inhibition directly, or show clinical benefit.

## Model definition

### Inputs

Individual anatomical and resting-state MRI; a normative sgACC/vmPFC connectivity map used as a weighted seed, excluding dorsal PFC; individual sulcal-depth maps; candidate coil positions/orientations; head models for SimNIBS 4.0 electric-field simulation. Outcome models use event-related fMRI, stimulation condition, and subjective unpleasantness/loudness ratings.

### Outputs

Individual negative- and positive-FC target clusters, optimized coil placements and nearby controls, proposed stimulation intensities, modeled field distributions, condition-specific BOLD contrast maps, target–control differences, and spatial correlations with a previously reported depression circuit. There is no trained symptom predictor, stimulation policy, or online state estimator.

### Training objective (loss)

This is map estimation plus numerical targeting optimization, not a supervised predictive learner. Main Methods say target placement maximizes both field magnitude within the target cluster and overlap between the whole-brain FC map and field map. Control selection uses an inverted FC map while seeking proximity and low field in the original target cluster. The exact scalar score/weighting is not specified in the inspected main text; the linked supplementary download failed, so it is not reconstructed here. Outcome GLMs model pulse events convolved with a canonical hemodynamic response and estimate condition contrasts; no classification or therapeutic reward objective is defined.

### Architecture / parameterization

A staged pipeline: weighted-seed FC estimation → sulcal-depth weighting and largest-cluster selection in left dorsal PFC → individualized finite-element field modeling and coil-placement search → event-related first-level GLMs → within-subject group contrasts. The nominal field target is 100 V/m, constrained by hardware and tolerability. This is a static targeting/measurement stack, not a dynamical control model.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Connectivity-guided TMS is clinically motivated, but remote responses alone do not show that precisely hitting an individualized target matters. The necessary comparison is with a nearby placement that stimulates the neighborhood and creates similar peripheral sensations without engaging the selected cluster as strongly.

### 2. What is the method?

Use resting-state MRI to identify individual negatively connected DLPFC and positively connected dorsomedial-PFC clusters relative to the weighted sgACC/vmPFC seed. Optimize each coil placement and its nearby control using modeled fields. Deliver 65 single biphasic pulses per run, with 10–15-second jittered intervals; two low-intensity prepulses precede each main pulse to limit startle. Target/control order is counterbalanced within sessions and positive/negative session order across sessions, separated by at least two days. Compare downstream event-related BOLD, controlling for unpleasantness and loudness.

### 3. What is the method motivation?

A nominal cortical coordinate ignores the spatial footprint of the actuator. Combining connectivity with fields asks which network is actually exposed; active neighboring controls ask whether exposing that configuration adds a specific downstream effect. Together these are more informative than a condition-versus-rest activation map.

### 4. What data does it use?

Twenty healthy adults without psychiatric/neurological histories: 15 female, mean age 25.35 years, range 20–32. Data include anatomy, resting-fMRI connectivity, modeled fields, concurrent TMS-fMRI, navigation, and subjective ratings. Table 1 reports n = 20 for both negative-FC conditions, n = 19 for the positive target, and n = 18 for its control; tests use complete pairs. Exclusion reasons were not independently checked because the supplement was unavailable. There are no depression symptoms, treatment-response labels, EEG measurements, or longitudinal treatment outcomes in this experiment.

### 5. How is it evaluated?

Paired target–control contrasts and the target-type × FC-valence interaction are evaluated with group GLMs. Whole-brain inference uses cluster-level FWE correction with an uncorrected p < .001 cluster-forming threshold. Independently defined sgACC/vmPFC ROIs provide adjusted contrasts, with Bonferroni correction. Spatial resemblance to the depression circuit uses 10,000 spin rotations and correction across seven maps. Field separation and sensory ratings are also compared. There is no held-out clinical prediction evaluation or prospective state-triggered control test.

### 6. What are the main results?

- **Negative-target specificity:** Adjusted negative-target minus nearby-control BOLD beta differences were −1.03 in sgACC (adjusted CI [−1.69, −0.36], pBonf = .003) and −1.80 in vmPFC ([−3.00, −0.59], pBonf = .004). These are model beta contrasts, not percent neuronal suppression.
- **Positive-target comparison:** No significant whole-brain target–control difference; adjusted ROI differences were 0.26 for sgACC (pBonf = .752) and −0.16 for vmPFC (pBonf > .99). This is a null result, not an equivalence demonstration.
- **Interaction:** With n = 18 complete cases, the adjusted target-type × valence contrast was significant in sgACC (pBonf = .015) and vmPFC (pBonf = .009).
- **Unequal effective exposure:** Mean modeled field in the intended cluster was 79.83 V/m for negative-target stimulation versus 68.34 V/m for positive-target stimulation. The paired difference was 10.6 V/m, pBonf = .047. Controls produced 31.31 and 34.58 V/m in their corresponding negative and positive clusters, respectively.
- **Spatial correspondence:** Negative target–control and valence-interaction maps correlated with the depression circuit at r = .50 and .51 (both pBonf < .001); the positive target–control map was anticorrelated (r = −.28, pBonf = .005). Individual condition maps did not survive corrected spatial testing. A significant spatial correlation of an unthresholded contrast can coexist with a nonsignificant whole-brain activation contrast; these are different tests.

### 7. What is actually novel?

The useful increment is the joint precision-targeting and neighboring-active-control experiment, with concurrent measurement of its downstream difference. Remote TMS responses, FC-guided targeting, and anticorrelated-network hypotheses already exist. The authors claim a first direct test of this specific target-specificity question; that priority claim was not independently established here.

### 8. What are the strengths?

Within-person counterbalanced perturbations, explicit target sparing by controls, realistic field models, sensory measurements and covariate adjustment, and independent ROI tests. The paper shows that much of the brain-wide response is shared across conditions, making the contrast—not the prettiest condition map—the informative object. Spatial inference accounts for cortical autocorrelation rather than treating every vertex as independent. The main text openly discusses weaker positive-target exposure and inconsistent directions in earlier studies.

### 9. What are the weaknesses, limitations, or red flags?

- Small healthy-young-adult sample; nearly 80 runs are repeated observations, not 80 independent participants. Clinical and developmental generalization remain untested.
- FC sign, cortical location/network identity, and field exposure change together. The experiment causally perturbs configurations; it does not independently manipulate connectivity sign.
- Positive-target fields were lower, target–control FC separation was smaller, and that arm had fewer complete observations. A negative-versus-positive efficacy ranking would overread the comparison.
- No significant sensory-rating differences were detected, but that is not formal sensory equivalence or proof all peripheral confounding was removed. Active controls also stimulate cortex: the contrast is relative engagement, not stimulation versus nothing.
- Negative BOLD is not a direct readout of inhibitory neurons or reduced excitatory firing. No clear local BOLD response was detected at the directly stimulated site, limiting the chain of mechanistic measurement.
- Repeated therapeutic stimulation, clinical mediation, state dependence, and durability were not evaluated. Exact optimization weights, supplementary exclusions/procedures, raw data, and code remain unaudited in this read.

### 10. What challenges or open problems remain?

Determine whether effects replicate in depression, survive equalized effective fields, and predict individual clinical outcomes. Establish scan/target reliability and response heterogeneity rather than relying on group maps. Separate an FC-sign hypothesis from geometry, network identity, physiological state, and dose. A static downstream BOLD contrast does not establish reachability of a desired brain state or controllability over time.

### 11. What future work naturally follows?

Prospectively compare field-matched negative and positive targets with comparably separated local controls. Measure held-out target–control responses across sessions and brain states before asking whether they predict treatment benefit. Add EEG or intracranial measurements where appropriate to test the neuronal interpretation of the BOLD sign. In patients, compare competing targeting rules and test whether circuit engagement mediates—not merely correlates with—symptom improvement.

### 12. Why does this matter for cabbageland?

It supplies an empirical validation contract for personalized stimulation models: predict the incremental response over a carefully designed alternative configuration, not just a resting-state correlation or generic evoked map. Its anatomy/connectivity/field/outcome decomposition is useful for multimodal targeting, but it earns neither a closed-loop label nor a therapeutic-mechanism conclusion. The missing state-estimation and clinical layers should remain explicit.

### 13. What ideas are steal-worthy?

- Optimize an informative control alongside the proposed target; quantify both target engagement and target sparing.
- Register field magnitude, network overlap, sensory exposure, and intended downstream response as separate quantities.
- Validate model predictions on within-person target–control response differences, including failed predictions and uncertainty.
- Test baseline state as a moderator only after establishing target specificity; do not infer a state-aware policy from a static map.
- Keep spatial circuit resemblance, local physiology, and clinical improvement as separate endpoints with separate evidence requirements.

### 14. Final decision

Preserve as a strong targeting-method and network-perturbation note, with a moderate evidential ceiling. It supports specific downstream BOLD engagement by the tested negative-FC configuration relative to a neighboring control. It does not establish universal superiority of negative connectivity, neuronal inhibition, depression efficacy, or a validated controller.
