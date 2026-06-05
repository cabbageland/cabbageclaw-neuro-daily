# Thalamic stimulation induced changes in network connectivity and excitability in epilepsy

## Basic info

* Title: Thalamic stimulation induced changes in network connectivity and excitability in epilepsy
* Authors: Nicholas M. Gregg, Gabriela Ojeda Valencia, Tereza Pridalova, Harvey Huang, Vaclav Kremen, Brian N. Lundstrom, Jamie J. Van Gompel, Kai J. Miller, Gregory A. Worrell, Dora Hermes
* Year: 2025
* Venue / source: medRxiv preprint
* Link: https://www.medrxiv.org/content/10.1101/2024.03.03.24303480v2
* Date surfaced: 2026-06-04
* Why selected in one sentence: It gives thalamic deep brain stimulation for epilepsy a rapid electrophysiological readout of seizure-network engagement instead of waiting months for seizure-count feedback.

## Quick verdict

* Highly relevant

This is a strong mechanistic keep because it attacks one of the real problems in epilepsy deep brain stimulation: the clinical outcome is sparse, delayed, and patient-specific, so optimization is miserably slow. The paper uses stereotactic EEG, single-pulse stimulation, pulse evoked potentials, and interictal epileptiform discharge rates to ask whether thalamic high-frequency stimulation is engaging and modulating the patient’s seizure network. The caveat is that this is a retrospective ten-patient cohort during clinical sEEG monitoring, not an outcomes trial. It is a biomarker and target-engagement paper, not proof that the biomarker-guided strategy improves long-term seizure control.

## One-paragraph overview

The study analyzes ten people with drug-resistant focal epilepsy who underwent clinical stereotactic EEG and thalamic high-frequency deep brain stimulation. The authors use single-pulse electrical stimulation before and after thalamic high-frequency stimulation to measure pulse evoked potentials, treating baseline PEP amplitude as a map of thalamocortical effective connectivity and post-stimulation amplitude change as a readout of network excitability. They also track interictal epileptiform discharge rates during stimulation. The main result is that more than 1.5 hours of active thalamic high-frequency stimulation reduced pulse evoked potential amplitudes in connected regions, with the strength of modulation tied to baseline connectivity, while immediate interictal-discharge suppression appeared only when stimulation engaged the seizure network strongly enough. The useful lesson is not “thalamus good.” It is that thalamic DBS needs a patient-specific network-engagement assay, and PEPs may provide one.

## Model definition

### Inputs
Patient-specific stereotactic EEG recordings, clinically selected thalamic stimulation contacts, single-pulse electrical stimulation responses, high-frequency thalamic stimulation exposure, baseline seizure-network hypotheses, and automated interictal epileptiform discharge detections.

### Outputs
Pulse evoked potential amplitude maps, changes in effective connectivity and excitability after thalamic stimulation, network-specific engagement estimates, and changes in interictal epileptiform discharge rate during high-frequency stimulation.

### Training objective (loss)
There is no central trainable model with an optimization loss. The automated IED classifier is used as a measurement tool, while the scientific objective is to estimate whether stimulation engages and modulates the seizure network quickly enough to guide personalization.

### Architecture / parameterization
A clinical sEEG stimulation-mapping pipeline: single-pulse stimulation maps thalamocortical effective connectivity through PEPs, high-frequency thalamic DBS perturbs the network, and pre-post PEP amplitude plus concurrent IED-rate changes serve as electrophysiological biomarkers of engagement and excitability.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Epilepsy DBS is hard to optimize because seizure networks are patient-specific, seizures are intermittent, and clinical response can take weeks or months to observe. The paper tries to provide a rapid electrophysiological biomarker for target engagement and network modulation during the invasive monitoring window.

### 2. What is the method?
The authors retrospectively analyze ten drug-resistant focal-epilepsy patients undergoing clinical sEEG. They deliver single-pulse stimulation to map pulse evoked potentials before and after thalamic high-frequency stimulation, then compare PEP amplitude changes and interictal epileptiform discharge rates as network-level readouts.

### 3. What is the method motivation?
If thalamic DBS works through seizure-network modulation, then target and parameter selection should be guided by whether stimulation actually engages that patient’s seizure network. Waiting for seizure-frequency outcomes is too slow; PEPs and IED rates may provide faster circuit-level evidence.

### 4. What data does it use?
Ten individuals with drug-resistant focal epilepsy undergoing clinical stereotactic EEG at Mayo Clinic, with patient-specific thalamic leads selected for clinical seizure-network hypotheses, single-pulse stimulation recordings, high-frequency thalamic stimulation trials, and automated IED measurements.

### 5. How is it evaluated?
By testing whether PEP amplitudes change after thalamic high-frequency stimulation, whether modulation depends on baseline thalamocortical connectivity, whether stimulation duration matters, and whether IED rates are suppressed when the seizure network is strongly engaged.

### 6. What are the main results?
- Thalamic high-frequency stimulation delivered for more than 1.5 active hours significantly reduced PEP amplitudes in connected regions.
- Shorter stimulation exposure did not produce reliable effective-connectivity changes.
- The degree of PEP modulation correlated with baseline thalamocortical connectivity strength.
- IED rates were acutely suppressed only when thalamic stimulation strongly engaged the seizure network.
- PEP maps exposed distinct thalamocortical engagement patterns across thalamic subfields and patients.

### 7. What is actually novel?
The novelty is using PEP-based effective-connectivity mapping as a rapid, patient-specific target-engagement and excitability biomarker for thalamic DBS in epilepsy, paired with IED-rate modulation as a complementary acute readout.

### 8. What are the strengths?
- The paper addresses a real bottleneck in DBS optimization rather than adding another average-effect stimulation claim.
- sEEG gives direct access to distributed patient-specific seizure-network recordings.
- PEPs are a plausible causal-connectivity readout because they are evoked by stimulation rather than inferred only from spontaneous correlation.
- The distinction between subacute PEP changes and acute IED suppression is useful.
- The findings connect thalamic target engagement to network specificity instead of treating thalamic nuclei as generic coordinates.

### 9. What are the weaknesses, limitations, or red flags?
- The cohort is small and retrospective.
- Stimulation parameters and thalamic targets are heterogeneous because the study is embedded in clinical care.
- The paper does not establish long-term seizure outcome benefit from PEP-guided optimization.
- IED suppression is a useful biomarker, but it is not identical to seizure reduction.
- Industry ties and licensed intellectual property are disclosed, so device-translation enthusiasm should be read with normal skepticism.

### 10. What challenges or open problems remain?
The big open question is whether PEP-guided target and parameter selection improves durable seizure outcomes. The field still needs prospective trials, stronger links between PEP/IED biomarkers and clinical response, and closed-loop or adaptive workflows that can use these biomarkers safely outside the short sEEG window.

### 11. What future work naturally follows?
Prospective biomarker-guided thalamic DBS studies, comparison of PEP-based targeting against anatomy-only targeting, durability testing of PEP changes, integration with chronic sensing devices, and adaptive stimulation policies that combine evoked connectivity with ongoing epileptiform activity.

### 12. Why does this matter for cabbageland?
Because it is exactly the kind of intervention logic we care about: do not just stimulate a named node, measure whether the patient-specific pathological network was engaged and whether its excitability changed. This is a sharper template for personalized neuromodulation than most target-location papers.

### 13. What ideas are steal-worthy?
- Use evoked responses as a target-engagement assay before trusting a stimulation target.
- Separate network engagement, excitability modulation, and clinical outcome instead of collapsing them into one success story.
- Treat stimulation duration as a mechanistic variable, not merely a protocol detail.
- Combine slower neuroplasticity-facing biomarkers with acute pathological-activity biomarkers.
- Use the invasive monitoring window to learn patient-specific control structure before chronic therapy begins.

### 14. Final decision
Preserve. This is not an efficacy proof, but it is a very useful biomarker-design paper for personalized epilepsy neuromodulation and for the broader question of how to make delayed-response DBS less blind.
