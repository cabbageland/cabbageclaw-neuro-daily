# A whole-brain modeling framework for tDCS montage optimization in drug-resistant epilepsy

## Basic info

* Title: A whole-brain modeling framework for tDCS montage optimization in drug-resistant epilepsy
* Authors: Borja Mercadal; Edmundo Lopez-Sola; Julia Makhalova; Francesca Pizzo; Ricardo Salvador; Fabrice Bartolomei; Giulio Ruffini
* Year: 2026
* Venue / source: medRxiv preprint
* Link: https://www.medrxiv.org/content/10.64898/2026.09.22.26363221v1.full
* Date surfaced: 2026-10-12
* Why selected in one sentence: It makes tDCS montage design a personalized network-dynamics problem instead of treating the induced electric field as the whole intervention.

## Quick verdict

* Highly relevant

This is a useful keep, with the usual preprint and small-n caveats. The paper is not clinical proof that neurotwin-optimized tDCS improves epilepsy outcomes, because the main optimization result is in silico and the retrospective clinical comparison has only six treated patients. But it is exactly the right kind of method paper for cabbageland: it couples a biophysical head model to a personalized seizure-spread model and shows that field-only optimization can miss the parcels that actually control propagation.

## One-paragraph overview

The paper introduces a "neurotwin" pipeline for multichannel tDCS in drug-resistant epilepsy. For each of 12 patients, the authors build a personalized finite-element head model from MRI and a personalized whole-brain model of seizure spread constrained by structural connectivity and SEEG. Candidate montages are then evaluated not only by whether they deliver an inhibitory field to clinician-defined epileptogenic regions, but by whether the resulting field suppresses seizure propagation inside the whole-brain model. The main result is not the trivial fact that the neurotwin loss can suppress simulated spread by construction; the useful result is that montages with similar aggregate fields can produce sharply different simulated network outcomes. The difference often lives in a small number of propagation-zone or off-target parcels, especially structurally central parcels whose inhibition can prevent spread and whose excitation can worsen it.

## Model definition

### Inputs

The pipeline uses patient-specific T1 MRI, diffusion MRI, SEEG recordings during spontaneous seizures, clinician-labeled epileptogenic zones and propagation zones, a 162-region Virtual Epileptic Patient cortical parcellation, structural connectivity from probabilistic tractography, and a lead-field model for candidate multichannel tDCS montages over 10-10 EEG electrode positions.

### Outputs

The pipeline emits optimized tDCS montages constrained to clinically realizable current limits, predicted electric-field distributions, simulated membrane-potential perturbations per parcel and neural population, model-predicted seizure-spread reduction, minimum parcel sets that explain differences between montages, and retrospective associations between predicted spread reduction and clinical seizure-frequency change.

### Training objective (loss)

Whole-brain model personalization optimizes global coupling and local excitability parameters so simulated SEEG functional connectivity matches empirical SEEG functional connectivity better than structural connectivity alone. Montage optimization minimizes a loss with a primary whole-brain-model term, the number of non-epileptogenic-zone parcels that still show seizure activity under stimulation, plus a secondary biophysical NERNI field term used to break ties and favor focal inhibitory field delivery.

### Architecture / parameterization

The system is a coupled digital-twin stack rather than a conventional learned classifier. It combines a SimNIBS finite-element head model, a patient-specific structural connectome, region-specific neural mass models for epileptogenic and non-epileptogenic parcels, simulated SEEG functional connectivity fitting, field-to-membrane-potential coupling, and differential-evolution search over multichannel tDCS electrode/current configurations.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Personalized tDCS for drug-resistant epilepsy usually optimizes where the electric field goes, then assumes that field delivery is a good proxy for intervention effect. That is too shallow. Epileptic activity spreads through a patient-specific network, and two montages that look similar at the target can differ at a few propagation-relevant parcels enough to change the simulated outcome.

### 2. What is the method?

The authors build a personalized neurotwin for each patient by pairing a biophysical head model with a personalized whole-brain seizure model. The head model estimates the normal electric field induced by a montage. The whole-brain model maps that field into membrane-potential perturbations in parcel-level neural mass models, simulates whether seizure activity spreads, and supplies the network term in the montage optimization loss. They compare this neurotwin optimization with conventional field-based optimization and with a field-only variant using WBM-derived target maps.

### 3. What is the method motivation?

The motivation is that tDCS efficacy should depend on network response, not just local field delivery. A montage can inhibit the clinically named target and still excite a parcel that makes propagation worse. Conversely, modest inhibition at a structurally central propagation parcel can matter more than stronger field at a less decisive region.

### 4. What data does it use?

The study uses retrospective data from 12 patients with drug-resistant epilepsy who had high-resolution anatomical MRI, diffusion MRI, and SEEG recordings during spontaneous seizures. Six of those patients also participated in an open-label clinical tDCS trial, which the authors use for a small retrospective comparison between model-predicted spread reduction and seizure-frequency change.

### 5. How is it evaluated?

Evaluation has several layers. First, each personalized WBM must fit empirical SEEG functional connectivity better than structural connectivity alone. Second, the neurotwin montages are compared against conventional biophysical montages and a WBM-target-map field-only variant. Third, single-parcel inhibition analyses test whether high-impact propagation parcels have distinctive connectome positions. Fourth, minimum-replacement-set analyses identify which parcels explain montage differences. Finally, six clinically treated patients provide a hypothesis-generating retrospective check against seizure-frequency change.

### 6. What are the main results?

Single-parcel inhibition shows a bimodal pattern: many parcels do little, while some propagation-zone parcels nearly abolish spread in the model. High-impact parcels tend to be structurally central, with positive associations for nodal strength, eigenvector centrality, and betweenness that survive adjustment for excitability and seizure-threshold proximity. The neurotwin and field-based pipelines deliver comparable epileptogenic-zone fields, but produce different montages and different simulated network outcomes. The WBM-target-map field-only control isolates the key point: even when target maps and aggregate field distributions are very similar, leaving out the network term can yield worse or even spread-increasing simulations. In six clinically treated patients, WBM-predicted spread reduction tracks seizure-frequency change in the expected direction, but not significantly.

### 7. What is actually novel?

The novelty is not "digital twins for epilepsy" in general. The useful move is embedding the whole-brain seizure model directly in the stimulation-optimization loss, so the objective becomes network response to a deliverable montage rather than electric-field resemblance to a target map. The minimum-replacement analysis is also valuable because it turns a black-box montage difference into a small set of propagation-zone or off-target parcels.

### 8. What are the strengths?

The paper has good mechanistic taste. It separates field targeting from network response, uses patient-specific imaging and SEEG rather than generic connectomes, tests a field-only WBM-target-map control, and is honest that optimization-by-construction is not the interesting result. It also localizes failure modes: insufficient inhibition of critical propagation parcels and active excitation of parcels that should have been spared.

### 9. What are the weaknesses, limitations, or red flags?

The clinical evidence is thin: the retrospective analysis has six patients, two responders, no significant correlations, and no ability to establish predictive accuracy. The WBM depends on SEEG, so the current pipeline applies mainly to patients already undergoing invasive presurgical evaluation. The coupling gain from electric field to neural-mass perturbation is calibrated rather than directly measured, and the optimization objective assumes that acute simulated spread reduction is a proxy for long-term clinical benefit. Several authors are affiliated with Neuroelectrics, which develops transcranial stimulation technology.

### 10. What challenges or open problems remain?

The biggest challenge is prospective validation. The model needs to show that neurotwin-optimized montages improve safety, seizure outcomes, or decision quality compared with strong field-based baselines. The second challenge is noninvasive personalization: if SEEG is required, the approach is useful but narrow. The third is objective design. Acute spread suppression may be a reasonable starting point, but plasticity, session schedule, seizure frequency over time, and adverse excitation of off-target parcels all need richer modeling.

### 11. What future work naturally follows?

The natural next step is the ongoing prospective trial testing whether neurotwin-informed montage design improves outcomes. After that, the right follow-ups are larger retrospective validation, uncertainty analysis over WBM parameters, comparison against simpler connectome-centrality heuristics, integration with scalp EEG or MEG personalization, and multi-objective losses that trade spread suppression against safety, focality, and predicted long-term plasticity.

### 12. Why does this matter for cabbageland?

It sharpens the intervention logic we care about. A stimulation target is not just a coordinate or a field maximum; it is a move in a patient-specific dynamical system. The paper gives a concrete implementation of that view and a useful warning: aggregate field metrics can look reassuring while the model says the montage is hitting the wrong network levers.

### 13. What ideas are steal-worthy?

- Put the disease-relevant dynamical model inside the optimization loss, not merely upstream as a target-map generator.
- Treat off-target excitation as an active failure mode, not just as wasted current.
- Use minimum-replacement or similar counterfactual analyses to explain why two stimulation patterns differ.
- Compare network-aware montages against field-only controls with matched target maps, not only against a straw baseline.
- Look for parcels whose centrality and dynamical state jointly determine whether stimulation can control propagation.

### 14. Final decision

Keep. This is not yet a clinical victory paper, but it is a strong mechanism-and-method paper. It makes personalized noninvasive stimulation more honest by forcing montage design to answer the real question: what does this field do to this patient's seizure network?
