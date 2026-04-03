# Individualized non-invasive deep brain stimulation of the basal ganglia using transcranial ultrasound stimulation

## Basic info

* Title: Individualized non-invasive deep brain stimulation of the basal ganglia using transcranial ultrasound stimulation
* Authors: Ghazaleh Darmani, Hamidreza Ramezanpour, Can Sarica, Regina Annirood, Talyta Grippe, Jean-Francois Nankoo, Anton Fomenko, Brendan Santyr, Ke Zeng, Artur Vetkas, Nardin Samuel, Benjamin Davidson, et al.
* Year: 2025
* Venue / source: Nature Communications
* Link: https://www.nature.com/articles/s41467-025-57883-7
* Date surfaced: 2026-04-03
* Why selected in one sentence: It is one of the rare human ultrasound neuromodulation papers that can show direct deep-target physiological engagement rather than inferring it indirectly.

## Quick verdict

* Highly relevant

This is not proof that transcranial ultrasound can replace implanted deep brain stimulation, and the title overshoots what the evidence can support. But the paper is still unusually valuable because it combines individualized targeting, direct local field potential recording from the deep target, safety work around implanted leads, and a target-specific behavioral assay. That is a much stronger mechanistic package than the usual noninvasive-deep-stimulation pitch.

## One-paragraph overview

The paper tests whether individualized transcranial ultrasound stimulation can modulate the human globus pallidus internus, a canonical deep brain stimulation target, with direct physiological evidence rather than only indirect readouts. In movement-disorder patients who already had implanted globus pallidus internus DBS leads, the authors used subject-specific acoustic simulations to position ultrasound, then recorded local field potentials wirelessly from the implanted device before, during, and after sonication. Theta-burst ultrasound increased theta power during stimulation, while ten-hertz ultrasound increased beta power, with effects lasting up to forty minutes. In a separate healthy cohort, sonication of the globus pallidus internus prolonged stop-signal reaction times, whereas stimulation of the pulvinar used as an active control site did not, which supports at least some target specificity.

## Model definition

This paper is not centered on a trainable predictive model.

### Inputs
Individual structural imaging for acoustic simulation and targeting, transcranial ultrasound stimulation parameters, local field potential recordings from implanted globus pallidus internus leads in movement-disorder patients, and stop-signal task behavior in healthy participants.

### Outputs
Changes in local field potential power within the globus pallidus internus, especially theta and beta bands, plus behavioral changes in stop-signal performance during target versus control-site stimulation.

### Training objective (loss)
No learnable model or explicit optimization loss is the scientific core of the paper. The main optimization is engineering-style targeting via individualized acoustic simulation rather than statistical model training.

### Architecture / parameterization
A translational neuroengineering design combining subject-specific acoustic modeling, transcranial ultrasound stimulation, implanted deep-brain electrophysiology, and a behavioral assay of response inhibition.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The problem is whether a noninvasive modality can actually reach and modulate a deep human basal-ganglia target with credible evidence. Ultrasound neuromodulation often claims deep precision, but most papers cannot directly show what happened at the target.

### 2. What is the method?
The method has two arms. In patients with Parkinson disease or dystonia who already had globus pallidus internus DBS implants, the authors used personalized acoustic simulations to target the globus pallidus internus and recorded local field potentials from the implanted system before, during, and after ultrasound. In healthy participants, they sonicated the globus pallidus internus during a stop-signal task and compared the behavioral effect against pulvinar stimulation as an active control.

### 3. What is the method motivation?
If ultrasound is going to matter for neuromodulation, the field needs direct evidence of deep-target engagement and some target specificity, not just generic statements that behavior changed after sonication. The authors are trying to supply that missing translational link.

### 4. What data does it use?
The accessible abstract and article text describe ten individuals with movement disorders and fifteen healthy participants. The patient arm uses local field potential recordings from globus pallidus internus DBS leads plus individualized MRI-based targeting simulations. The healthy-participant arm uses behavioral data from a stop-signal task during sonication of the globus pallidus internus or pulvinar.

### 5. How is it evaluated?
It is evaluated by comparing ultrasound versus sham effects on local field potential power in the deep target, checking persistence of those effects after stimulation, assessing behavioral consequences for response inhibition, and using a control target to probe specificity. The paper also includes ex vivo safety and feasibility work around DBS leads.

### 6. What are the main results?
Theta-burst ultrasound increased theta-band power during stimulation, and ten-hertz ultrasound increased beta-band power, with some effects lasting up to forty minutes after sonication. In healthy participants, globus pallidus internus stimulation prolonged stop-signal reaction times, implying impaired response inhibition, while pulvinar stimulation did not. The authors also report that simulations and safety analyses kept estimated heating and acoustic metrics within accepted bounds.

### 7. What is actually novel?
The novelty is not just that ultrasound was aimed at a deep structure. The useful novelty is direct deep-target human electrophysiology during individualized ultrasound targeting, plus a behavioral specificity check against a control site. That is much closer to real target-engagement evidence than indirect imaging or scalp recordings alone.

### 8. What are the strengths?
- Direct local field potential readout from the deep target.
- Subject-specific acoustic simulation rather than generic one-size-fits-all targeting.
- Includes both physiological and behavioral evidence.
- Uses a control target in the healthy cohort instead of relying only on sham.
- Explicitly addresses safety around implanted DBS hardware.

### 9. What are the weaknesses, limitations, or red flags?
- The title overstates the case by calling this non-invasive deep brain stimulation rather than a mechanistic ultrasound-targeting study.
- The sample is still small.
- Movement-disorder patients with existing DBS hardware are a special population, not a generic translational bridge to psychiatry.
- The behavioral effect is impairment on a stop-signal task, which is useful mechanistically but not therapeutic evidence.
- I did not inspect the full PDF end to end, so confidence should remain bounded on fine-grained statistics and protocol edge cases.

### 10. What challenges or open problems remain?
The field still needs replication, stronger dose-response mapping, clearer parameter-to-direction rules, broader circuit testing, and evidence that target engagement translates into useful therapeutic control rather than merely measurable perturbation. It also needs more honest language about what counts as equivalence to implanted stimulation.

### 11. What future work naturally follows?
Larger mechanistic studies across additional targets, disease-specific therapeutic trials built on verified target engagement, multimodal readouts linking local field potential changes to network effects, and adaptive parameter selection that uses direct physiology rather than static preset protocols.

### 12. Why does this matter for cabbageland?
Because it is one of the cleaner recent examples of a neuromodulation paper earning its deep-target claim. It sharpens the bar for what ultrasound papers should show if they want to be taken seriously: real target engagement, target specificity, safety work, and a mechanism-first framing.

### 13. What ideas are steal-worthy?
- Use direct physiology at the target whenever possible instead of treating indirect readouts as sufficient proof.
- Treat individualized acoustic simulation as part of the intervention logic, not as a cosmetic targeting add-on.
- Pair target-engagement evidence with a target-specific behavioral assay.
- Separate the claim that a target was modulated from the much stronger claim that the modality is therapeutically equivalent to implanted DBS.

### 14. Final decision
Keep. This is one of the better translational ultrasound neuromodulation papers in the recent stream because it demonstrates real deep-target engagement in humans. Keep the note, but keep the skepticism too: target engagement is not yet therapeutic validation.
