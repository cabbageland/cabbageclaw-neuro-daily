# Cortical vs Subcortical Recordings to Drive Closed-Loop Deep Brain Stimulation in Essential Tremor

## Basic info

* Title: Cortical vs Subcortical Recordings to Drive Closed-Loop Deep Brain Stimulation in Essential Tremor
* Authors: Brandon Parks et al.
* Year: 2026
* Venue / source: Neuromodulation
* Link: https://pubmed.ncbi.nlm.nih.gov/42017861/
* Date surfaced: 2026-04-24
* Why selected in one sentence: It compares where the adaptive biomarker should come from in chronic tremor DBS and argues, with real long-term home use, that cortical sensing may beat thalamic sensing.

## Quick verdict

* Highly relevant

This is a small study, but it asks a sharper question than most adaptive-DBS papers. Instead of assuming the right biomarker lives near the stimulated target, it compares cortical and subcortical recording sources in real use over time. The sample is tiny, so the result is not settled doctrine, but the design logic is excellent.

## One-paragraph overview

The paper studies closed-loop DBS for essential tremor using a long-term implantable system and asks whether movement-linked control is better driven by sensorimotor cortical recordings or subcortical recordings from the thalamic region. Four participants used the system chronically, including months of home deployment. The authors report that cortical desynchronization markers tracked movement better, performed more consistently over time, and produced the most practical closed-loop solution in their experience. The useful point is broader than essential tremor alone: adaptive stimulation depends heavily on where you measure state, not just where you stimulate.

## Model definition

### Inputs
Chronic neural recordings from sensorimotor cortical strip electrodes and thalamic DBS-related recordings, along with movement-linked surrogate markers of tremor state.

### Outputs
A control signal for modulating DBS delivery in response to detected movement-linked neural signatures.

### Training objective (loss)
The accessible abstract does not specify a formal trainable loss. The system appears to use patient-specific desynchronization signatures as control biomarkers rather than a separately described learned model.

### Architecture / parameterization
A closed-loop DBS control pipeline comparing cortical-strip versus subcortical neural sensing to trigger or modulate stimulation based on movement-linked signatures.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Conventional DBS is always on, but adaptive DBS needs a reliable neural marker. The paper tries to determine whether that marker should come from cortex or from subcortical recordings near the stimulation site.

### 2. What is the method?
Implement chronic closed-loop DBS in essential tremor with an implantable pulse generator, derive patient-specific desynchronization markers from cortical and subcortical motor regions, and compare their performance over long-term use.

### 3. What is the method motivation?
A useful adaptive biomarker should track the movement state that matters for stimulation control and remain stable outside the clinic. Signal source matters for both requirements.

### 4. What data does it use?
Four implanted participants with essential tremor, followed with chronic use up to eighteen months post implantation and home deployment over months.

### 5. How is it evaluated?
By biomarker performance, longitudinal stability, clinical efficacy retention, and qualitative patient experience during extended home use.

### 6. What are the main results?
Cortical sensorimotor recordings outperformed thalamic recordings, remained more consistent over time, and supported maintained clinical efficacy in chronic closed-loop use. Patient feedback was mostly positive, though stimulation cessation also exposed failure modes and user-experience issues.

### 7. What is actually novel?
The main novelty is not closed-loop DBS itself. It is the direct comparison of cortical versus subcortical recording sources in long-term real-world use, with a clear practical recommendation.

### 8. What are the strengths?
- Asks a genuinely useful measurement-design question.
- Uses chronic home deployment rather than only lab sessions.
- Compares competing biomarker substrates directly.
- Preserves focus on longitudinal stability, not only peak decoding.

### 9. What are the weaknesses, limitations, or red flags?
- Four participants is extremely small.
- The abstract does not expose the exact decoding metrics or failure distributions.
- Essential tremor may not generalize cleanly to other disorders.
- Movement-linked surrogates are not the same as direct symptom-state estimation.

### 10. What challenges or open problems remain?
Scaling beyond four participants, handling day-to-day variability, reducing negative experiences during stimulation cessation, and deciding when symptom-linked rather than movement-linked biomarkers are preferable.

### 11. What future work naturally follows?
Larger chronic cohorts, hybrid cortical-plus-subcortical controllers, better user-facing transition logic, and comparison against symptom-state biomarkers rather than only movement surrogates.

### 12. Why does this matter for cabbageland?
Because it pushes adaptive stimulation toward the right systems question: what variable are you measuring, where do you measure it, and will it still work outside the clinic months later?

### 13. What ideas are steal-worthy?
- Compare candidate sensing substrates directly instead of assuming local is better.
- Evaluate biomarkers on longitudinal stability, not only offline decoding.
- Use patient experience during home use as controller feedback, not just anecdote.
- Separate movement proxies from symptom-state variables in adaptive design.

### 14. Final decision
Keep. Small but high-value, because it sharpens adaptive-DBS sensing logic instead of adding another generic closed-loop success story.