# Thalamofrontal synaptic weakening underlies short-term memory deficits from adolescent NMDAR hypofunction

## Basic info

* Title: Thalamofrontal synaptic weakening underlies short-term memory deficits from adolescent NMDAR hypofunction
* Authors: Jinseon Yu, In Sun Choi, Gyu Hyun Kim, Sangkyu Bahn, Jinmo Kim, Sungwon Bae, Taekwan Lee, Joon Ho Choi, Jun Soo Kwon, Minah Kim, Ji-Woong Choi, Kea Joo Lee, Jong-Cheol Rah
* Year: 2026
* Venue / source: Science Advances
* Link: https://doi.org/10.1126/sciadv.aee2152
* Date surfaced: 2026-09-30
* Why selected in one sentence: It turns schizophrenia-relevant thalamofrontal dysconnectivity from a broad imaging association into a projection-specific synaptic mechanism with behavioral and population-coding rescue.

## Quick verdict

* Highly relevant

This is a strong mechanism paper, with the usual translation caveat. The authors use adolescent repeated ketamine exposure in mice to model NMDAR hypofunction, then trace short-term-memory deficits to weakened mediodorsal thalamus to dorsomedial prefrontal cortex synapses. The most useful part is the causal closure: chemogenetically strengthening that thalamofrontal pathway restores synaptic dynamics, dmPFC population coding, and Y-maze alternation behavior. It is not a clinical treatment paper, but it gives a much cleaner circuit-level intervention hypothesis than another schizophrenia connectivity correlation.

## One-paragraph overview

The paper asks why thalamofrontal dysconnectivity, one of the more reliable schizophrenia-related circuit findings, might impair short-term memory. Mice received daily ketamine across an adolescent prefrontal maturation window, then were tested with delayed and spontaneous Y-maze tasks, novel object recognition, ex vivo slice physiology, optogenetic projection assays, in vivo thalamic stimulation and dmPFC single-unit recordings, chemogenetic manipulation, population decoding, and a thalamocortical network simulation. Repeated adolescent NMDAR antagonism produced durable short-term-memory deficits without a simple locomotion or anxiety explanation. The core mechanism was not gross synapse loss or altered intrinsic excitability, but reduced presynaptic release efficacy at mediodorsal thalamus to dmPFC synapses, with impaired frequency-dependent response suppression and degraded dmPFC direction coding during memory performance. Chemogenetic enhancement of MD-to-dmPFC projections with hM3Dq/C21 rescued the synaptic physiology, sharpened temporal responses, improved alternation performance, and restored population discriminability.

## Model definition

### Inputs
Repeated adolescent ketamine or vehicle exposure; short-term-memory task behavior; ex vivo dmPFC whole-cell recordings; optogenetic activation of corticocortical and MD-to-dmPFC terminals; in vivo single-unit recordings during MD stimulation and Y-maze performance; chemogenetic hM3Dq/C21 activation of MD-to-dmPFC neurons; and pseudo-population neural activity sampled from dmPFC units.

### Outputs
Short-term-memory performance, spontaneous and optogenetically evoked synaptic currents, release probability and optogenetically derived readily releasable pool estimates, frequency-dependent dmPFC firing suppression, stimulus-evoked temporal precision, single-neuron direction selectivity, LDA decoding performance for correct versus error or task-epoch activity, and thalamocortical network simulation responses.

### Training objective (loss)
The paper is not centered on a therapeutic machine-learning predictor. The learned component is linear discriminant analysis trained to distinguish population activity states, evaluated by auROC, leave-one-out, and repeated subsampling/cross-validation procedures. The thalamocortical simulation is a NEURON/Hodgkin-Huxley style model with hand-specified perturbations, including halving thalamocortical AMPA-mediated synaptic weights, rather than a fitted loss-driven model.

### Architecture / parameterization
The main architecture is a projection-specific causal physiology stack: adolescent NMDAR hypofunction perturbation, pathway-isolated synaptic readouts, in vivo thalamic stimulation, chemogenetic restoration, and neural decoding during memory behavior. The computational pieces are an LDA decoder over dmPFC pseudo-populations and a thalamocortical network simulation with pyramidal neurons, inhibitory cortical neurons, thalamocortical cells, and reticular thalamic nucleus cells.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Thalamofrontal dysconnectivity is repeatedly reported in schizophrenia and is linked to cognitive impairment, but the field still lacks a biological account of what fails at that connection and whether repairing it can restore memory-relevant coding.

### 2. What is the method?
The authors expose adolescent mice to repeated ketamine, then combine behavioral assays, slice electrophysiology, pathway-specific optogenetics, in vivo stimulation and single-unit recording, chemogenetic pathway enhancement, LDA decoding, and a thalamocortical simulation to test whether MD-to-dmPFC synaptic weakening causes short-term-memory deficits.

### 3. What is the method motivation?
Adolescence is a vulnerable window for prefrontal circuit maturation, schizophrenia commonly emerges around this developmental period, and NMDAR hypofunction is a central schizophrenia-relevant biological hypothesis. If that biology selectively weakens thalamofrontal signaling, then cognitive impairment should be tied to a modifiable projection-level defect rather than a vague whole-brain dysconnectivity label.

### 4. What data does it use?
The study uses primarily male mice treated with repeated ketamine beginning at three to four weeks of age, adult-treatment comparisons, behavioral Y-maze and novel-object-recognition data, ex vivo dmPFC recordings, optogenetic and chemogenetic viral manipulations, in vivo dmPFC single-unit recordings, electron microscopy, histology, and public Figshare data/code for reproducibility.

### 5. How is it evaluated?
Evaluation is layered. Behavior tests whether repeated adolescent ketamine impairs memory. Slice and in vivo physiology test whether synaptic release and thalamofrontal response dynamics are altered. Pathway comparisons test whether corticocortical inputs are spared while MD-frontal projections are vulnerable. Chemogenetic rescue tests causality. Population decoding tests whether the circuit manipulation restores memory-relevant neural representations.

### 6. What are the main results?
Repeated adolescent ketamine impaired reward-motivated delayed Y-maze performance, spontaneous alternation, and novel object recognition, with acute locomotion and anxiety-like confounds controlled. In dmPFC layer 2/3 pyramidal neurons, excitatory input frequency fell without clear postsynaptic amplitude or intrinsic excitability changes. Local corticocortical transmission was largely preserved, while MD-to-dmPFC thalamofrontal synapses showed reduced apparent release probability, attenuated short-term depression, weaker vesicle refilling, and delayed/broadened in vivo responses. Adult ketamine produced much weaker effects. Chemogenetic strengthening of MD-to-dmPFC projections restored synaptic dynamics, improved spontaneous alternation, and reversed the degradation of dmPFC direction-selective coding and LDA discriminability.

### 7. What is actually novel?
The novelty is the projection-specific causal chain. The paper does not merely say that schizophrenia-like NMDAR hypofunction affects prefrontal cortex. It isolates thalamofrontal presynaptic release as a vulnerable mechanism, tests developmental timing, and shows that strengthening that pathway rescues physiology, coding, and behavior.

### 8. What are the strengths?
- It connects molecular-developmental risk, circuit physiology, neural coding, and behavior in one design.
- It distinguishes MD-to-dmPFC thalamofrontal inputs from local corticocortical inputs instead of treating prefrontal excitation as one blob.
- The rescue experiment is much stronger than a correlational connectivity result.
- In vivo stimulation and task recordings keep the paper from being only a slice-physiology story.
- The population-decoding analysis links synaptic repair to memory-relevant representations, not just prettier electrophysiology.
- The paper releases source data, associated datasets, and MATLAB code through Figshare.

### 9. What are the weaknesses, limitations, or red flags?
- Ketamine-induced adolescent NMDAR hypofunction is a model, not schizophrenia.
- Chemogenetic hM3Dq/C21 enhancement is not a directly deployable human therapy.
- The study is primarily in male mice, so sex-specific vulnerability remains underexplored.
- Durability is unknown: acute chemogenetic rescue does not prove lasting repair.
- Other long-range inputs to dmPFC, especially hippocampal-prefrontal projections, may also matter.
- A patent application covers methods for enhancing thalamofrontal synaptic connectivity to improve memory and cognition, so intervention framing has a conflict-of-interest shadow.

### 10. What challenges or open problems remain?
The main challenge is translation. The field needs to know whether comparable thalamofrontal synaptic or physiological signatures can be measured in humans, whether they stratify cognitive impairment, and whether any plausible actuator can strengthen this pathway safely and durably without crude excitation.

### 11. What future work naturally follows?
Test sex differences, extend the timing analysis across developmental windows, measure other long-range prefrontal inputs, identify noninvasive or pharmacological ways to modulate thalamofrontal efficacy, and map the mouse mechanism onto human imaging, EEG/MEG, or intracranial readouts of thalamofrontal communication in psychosis-risk and schizophrenia cohorts.

### 12. Why does this matter for cabbageland?
Because it is the kind of mechanism that can discipline intervention design. "Thalamofrontal dysconnectivity" is too broad to target; reduced presynaptic efficacy in MD-to-dmPFC projections during a developmental vulnerability window is a much sharper hypothesis.

### 13. What ideas are steal-worthy?
- Treat developmental timing as part of mechanism, not only a demographic covariate.
- Separate local recurrent cortical inputs from long-range thalamic inputs when interpreting prefrontal dysfunction.
- Require rescue of coding and behavior, not just rescue of a synaptic readout.
- Use task-period population discriminability as a bridge between synaptic physiology and cognition.
- Think of psychiatric circuit targets as projection-specific control problems rather than region labels.

### 14. Final decision
Keep. This is a high-quality translational-mechanism note: not clinically ready, but unusually useful for turning a schizophrenia network association into a testable pathway-level intervention hypothesis.
