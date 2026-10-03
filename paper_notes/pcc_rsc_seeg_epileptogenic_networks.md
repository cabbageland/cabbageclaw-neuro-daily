# Ictal Epileptogenic Network Differences in Posterior Cingulate Epilepsy Subtypes Based on SEEG

## Basic info

* Title: Ictal Epileptogenic Network Differences in Posterior Cingulate Epilepsy Subtypes Based on SEEG
* Authors: Zhaofen Yan, Yujiao Yang, Jing Wang, Qin Qin Deng, Minghui Wang, Huajun Yang, Jiali Pan, Jian Zhou, and colleagues
* Year: 2026
* Venue / source: CNS Neuroscience & Therapeutics
* Link: https://doi.org/10.1002/cns.71192
* Date surfaced: 2026-10-03
* Why selected in one sentence: It uses SEEG-derived directed network dynamics to distinguish retrosplenial from posterior cingulate epilepsy in a way that matters for surgical localization, propagation logic, and cognitive-risk preservation.

## Quick verdict

* Highly relevant

This is worth keeping because it is a small but unusually concrete network-intervention paper: seizure localization is tied to directed intracranial propagation rather than surface labels or descriptive semiology. The useful result is that retrosplenial cortex epilepsy preferentially recruits ipsilateral mesial temporal structures during propagation, while posterior cingulate cortex epilepsy looks more diffuse and less directionally organized. The study is retrospective, single-center, and small, so it is not a universal posterior-cingulate epilepsy rule, but the intervention logic is real.

## One-paragraph overview

The paper studies 18 patients with drug-resistant posterior cingulate epilepsy subtypes who underwent stereo-EEG, had at least two habitual seizures recorded, received posterior cingulate resection or PCC/RSC radiofrequency thermocoagulation, and achieved Engel I seizure freedom after more than one year. The authors split patients into retrosplenial cortex epilepsy and posterior cingulate cortex epilepsy, then compute gamma-band directed functional connectivity using the nonlinear h2 coefficient across preictal, ictal-onset, and early-propagation windows. In the propagation phase, RSC epilepsy shows a directional pathway toward ipsilateral mesial temporal and hippocampal structures, with ipsilateral mesial temporal nodes acting more like drivers and lateral temporal cortex acting more like a receiver. PCC epilepsy does not show the same consistent directional pattern. The strongest use of the paper is not that it produces a finished surgical algorithm; it shows how subtype-specific seizure propagation can be made more legible with SEEG network analysis.

## Model definition

This paper does not contain a learned prediction model, but it does define an analytic network model for ictal propagation.

### Inputs
Inputs include stereo-EEG recordings from 18 patients and 36 seizures, electrode-contact localization to PCC, RSC, ipsilateral and contralateral mesial temporal structures, ipsilateral lateral temporal cortex, ipsilateral lateral parietal cortex, and ipsilateral precuneus; three 5-second seizure windows covering preictal baseline, ictal onset, and early propagation; gamma-band activity from 30 to 80 Hz; neuropsychological memory testing; and surgical outcome information used to support the localization ground truth.

### Outputs
The analysis outputs directed functional connectivity matrices, node in-strength, node out-strength, total node strength, normalized node strength, driver-versus-receiver roles for each sampled region, group comparisons between RSC and PCC epilepsy, and associations between subtype-specific propagation and visual memory impairment.

### Training objective (loss)
There is no trainable loss. Directed coupling is estimated with the nonlinear h2 coefficient using 3-second sliding windows with 1.5-second overlap. Linear mixed-effects models are estimated with restricted maximum likelihood to test phase and group effects, followed by Type III ANOVA and Tukey-corrected pairwise comparisons where appropriate.

### Architecture / parameterization
The stack is a retrospective intracranial-network pipeline: hypothesis-driven SEEG implantation, electrode localization in MNI space, seizure segmentation into three early windows, gamma-band h2 directed connectivity, graph-theoretic node-strength metrics, and linear mixed-effects models over seven key regions. Anatomical labels and Engel I outcomes anchor the clinical grouping, while the connectivity model tries to separate subtype-specific propagation geometry.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Posterior cingulate epilepsy is difficult to localize because PCC and RSC seizures can produce overlapping semiology, impaired consciousness, automatisms, motor signs, and autonomic symptoms. The paper tries to determine whether seizure propagation networks distinguish RSC-origin from PCC-origin epilepsy in a way that could sharpen diagnosis and surgical decision-making.

### 2. What is the method?
The authors retrospectively analyze SEEG from patients with confirmed PCC or RSC seizure-onset zones. They compute gamma-band directed functional connectivity with h2 across preictal, onset, and propagation windows, derive graph metrics for region-level driver and receiver roles, and compare RSC versus PCC epilepsy with linear mixed-effects models.

### 3. What is the method motivation?
PCC and RSC differ in anatomy, cytoarchitecture, and connectivity. RSC has strong links to hippocampal and medial temporal memory systems, while PCC is more broadly connected with medial frontal, precuneus, temporoparietal, and sensorimotor-related systems. If those differences matter clinically, they should appear not only in anatomy but also in ictal propagation.

### 4. What data does it use?
The cohort includes 18 patients and 36 seizures from Sanbo Brain Hospital, recorded between 2012 and 2023. Eight patients had RSC epilepsy and ten had PCC epilepsy. All included patients had SEEG-confirmed onset, at least two complete habitual seizures, surgical or thermocoagulation treatment, more than one year of follow-up, and Engel Class I seizure-free outcome. Standard workup included clinical history, video-EEG, epilepsy MRI, PET, and Wechsler Memory Scale-IV testing.

### 5. How is it evaluated?
The paper evaluates whether directed connectivity and node-strength measures differ across seizure phases and subtypes. Within each subtype, it tests whether regions shift into driver or receiver roles during propagation. Between subtypes, it tests whether RSC and PCC epilepsy differ in propagation toward seven sampled regions, with special attention to ipsilateral hippocampal and mesial temporal structures.

### 6. What are the main results?
RSC epilepsy patients had poorer visual reproduction scores than PCC epilepsy patients among those with usable neuropsychological data. During propagation, ipsilateral mesial temporal structures in RSC epilepsy showed greater out-strength than in-strength, while ipsilateral lateral temporal cortex showed the opposite receiver-like profile. RSC epilepsy also showed stronger propagation toward ipsilateral mesial temporal and hippocampal structures than PCC epilepsy. PCC epilepsy did not show a consistent directional connectivity signature across the sampled regions.

### 7. What is actually novel?
The useful novelty is the subtype-specific propagation analysis. The paper does not just say that posterior cingulate epilepsy involves broad networks; it separates RSC and PCC origins and shows that one subtype has a more specific medial temporal recruitment pattern during early seizure spread.

### 8. What are the strengths?
The study uses intracranial data rather than scalp inference, includes seizure-free postoperative outcome as a clinical anchor, analyzes dynamic propagation instead of static connectivity alone, and links the RSC propagation pattern to a plausible visual-memory phenotype. It also uses a directed connectivity metric suited to nonlinear ictal SEEG and explicitly separates driver and receiver roles.

### 9. What are the weaknesses, limitations, or red flags?
The sample is only 18 patients from one center, and all RSC epilepsy patients were male. Electrode coverage was hypothesis-driven and did not sample the full brain, especially distal regions such as prefrontal and anterior cingulate cortex. The study lacks diffusion imaging, so it cannot directly test whether structural pathways explain the functional propagation pattern. The h2 directionality is still a signal-flow estimate, not causal proof in the intervention sense, and inclusion of only Engel I outcomes may bias the cohort toward clearer cases.

### 10. What challenges or open problems remain?
The main open problem is validation: whether the RSC-to-mesial-temporal propagation signature survives in larger, multicenter cohorts with broader electrode coverage and sex-balanced groups. Another open problem is actionability: whether this network signature changes surgical margins, thermocoagulation strategy, cognitive-risk counseling, or postoperative memory outcomes prospectively.

### 11. What future work naturally follows?
Combine SEEG with diffusion MRI to test anatomical-functional propagation models, include broader cingulate and prefrontal coverage, validate the signature prospectively, and ask whether preserving or interrupting specific RSC-hippocampal pathways changes seizure control and memory outcome. A stronger next step would turn the network signature into a preoperative decision aid and test it against expert localization alone.

### 12. Why does this matter for cabbageland?
It matters because it is a clean example of intervention-relevant network neuroscience. The paper turns a difficult localization problem into a directed propagation problem, and it ties network geometry to both surgical targeting and cognitive function. That is the kind of logic that transfers to neuromodulation: do not just name a region; ask how pathological activity flows through a patient-specific circuit.

### 13. What ideas are steal-worthy?
Treat seizure or symptom subtypes as propagation geometries, not just onset labels. Use postoperative outcome as a grounding signal for network interpretation. Separate driver and receiver roles across phases instead of averaging connectivity into one undifferentiated map. Link targeting decisions to cognitive-risk networks, especially when the propagation path involves hippocampal or retrosplenial memory systems.

### 14. Final decision
Preserve. The sample is too small to overclaim, but the mechanism is useful: RSC and PCC epilepsy appear to differ in early directed propagation, and the RSC-ipsilateral mesial temporal pathway is exactly the kind of circuit-level distinction that can improve localization, surgical planning, and future network-guided intervention design.
