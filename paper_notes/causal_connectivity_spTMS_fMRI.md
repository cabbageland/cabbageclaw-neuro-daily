# Causal connectivity maps derived from single-pulse interleaved TMS/fMRI

## Basic info

* Title: Causal connectivity maps derived from single-pulse interleaved TMS/fMRI
* Authors: Lison Bossus et al.
* Year: 2026.
* Venue / source: Scientific Reports.
* Link: https://pubmed.ncbi.nlm.nih.gov/41571696/
* Date surfaced: 2026-04-15.
* Why selected in one sentence: It is a useful methods paper because it tries to turn image-guided TMS from resting-connectivity inference into stimulation-evoked causal circuit mapping.

## Quick verdict

* Highly relevant

This is one of the better recent targeting-method papers because it makes a more causal move than the usual correlational network-mapping workflow. The useful claim is not that it finds a clinically validated psychiatric target. The useful claim is that personalized TMS plus interleaved fMRI can generate reproducible downstream circuit maps after controlling for pain, motion, and somatosensory confounds.

## One-paragraph overview

The paper aims to map causal downstream responses to personalized cortical stimulation sites rather than relying only on resting-state functional connectivity. In more than eighty participants, the authors selected left-hemisphere targets intended to engage either subgenual anterior cingulate cortex or basolateral amygdala and then delivered single-pulse TMS during fMRI. They quantified voxelwise TMS-evoked BOLD responses and residualized major nuisance factors such as head motion, pain, and somatosensory effects. The main result is that frontal targets aimed at subgenual circuits elicited subgenual and distributed downstream responses, while ventrolateral targets aimed at amygdala circuits elicited negative BOLD responses in the amygdala and broad downstream engagement. The most useful output is the public causal-connectivity map resource, not a claim that the psychiatric targeting problem is solved.

## Model definition

This paper does not present a trainable predictive model in the accessible abstract text. It presents a personalized targeting-and-measurement pipeline that produces stimulation-evoked circuit maps.

### Inputs
Individualized cortical TMS targets selected to engage either subgenual anterior cingulate cortex or basolateral amygdala, single-pulse TMS events delivered during fMRI, and nuisance variables including motion, pain, and somatosensory measures.

### Outputs
Voxelwise event-related BOLD maps, region-of-interest response estimates, and publicly shared causal-connectivity maps linking cortical stimulation sites to downstream circuit responses.

### Training objective (loss)
No trainable optimization loss is described in the accessible abstract. The work is based on event-related imaging analysis rather than supervised model training.

### Architecture / parameterization
Personalized connectivity-guided target selection combined with interleaved single-pulse TMS and voxelwise fMRI response mapping.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

The paper tries to address a persistent weakness in human circuit mapping: most neuroimaging-based targeting methods are correlational, so they cannot show what downstream circuit activity is actually evoked when a cortical site is stimulated.

### 2. What is the method?

The authors chose personalized left-hemisphere cortical targets designed to engage either subgenual anterior cingulate cortex or basolateral amygdala. They then delivered single-pulse TMS during fMRI, built voxelwise event-related response maps, and statistically controlled for motion, pain, and somatosensory confounds to isolate stimulation-specific effects.

### 3. What is the method motivation?

If the field wants causal circuit claims, then it should measure stimulation-evoked downstream responses rather than only infer them from resting connectivity or structural pathways. Interleaved TMS/fMRI offers a direct if still imperfect way to do that in humans.

### 4. What data does it use?

The accessible abstract reports more than eighty participants. It includes individualized TMS target locations, event-related fMRI responses, and confound measures related to pain and somatosensory experience. The target families are chosen to engage either subgenual-anterior-cingulate-linked or basolateral-amygdala-linked circuits.

### 5. How is it evaluated?

Evaluation is based on voxelwise and ROI-level TMS-evoked BOLD responses, with group-level analyses that residualize nuisance factors. The authors also compare downstream patterns associated with the two personalized target classes.

### 6. What are the main results?

Stimulation of frontal targets intended for subgenual circuits produced responses in subgenual anterior cingulate and other distributed cortical and subcortical regions. Ventrolateral targets intended for amygdala circuits produced negative BOLD responses in the amygdala and broader downstream engagement. The abstract also reports that ROI analyses did not show strong between-target differences across participants, which is an important caution against overselling target specificity.

### 7. What is actually novel?

The most novel piece is the attempt to build and share causal-connectivity maps from personalized spTMS/fMRI at scale, with explicit confound control. That is more useful than another paper that just says a target is connected to an interesting region at rest.

### 8. What are the strengths?

It makes a causal-measurement move rather than stopping at correlation.

It uses personalized targets rather than one generic coordinate.

And it explicitly controls for several of the most obvious non-neural confounds in TMS/fMRI.

### 9. What are the weaknesses, limitations, or red flags?

BOLD remains an indirect signal, so causal here means stimulation-evoked circuit response, not microscopic mechanism.

The lack of strong ROI separation between the two target classes tempers any simple story about clean circuit selectivity.

This is also still a mapping paper rather than a demonstration that the maps improve clinical outcomes.

And because I only inspected abstract-level text, I cannot judge individual-level reliability, preprocessing details, or exact reproducibility metrics.

### 10. What challenges or open problems remain?

The next challenge is to connect these causal maps to actual treatment optimization: which map features predict response, side effects, or state-dependent efficacy? Another challenge is determining how stable these maps are within individuals across sessions and brain states.

### 11. What future work naturally follows?

Prospective trials could test whether TMS targets selected using these causal maps outperform targets selected from resting connectivity alone. It would also be useful to estimate how individual brain state or symptom state changes the evoked map.

### 12. Why does this matter for cabbageland?

Because cabbageland is interested in interventions that can be justified mechanistically rather than by decorative network rhetoric. This paper is useful as an infrastructure step toward more causal targeting logic.

### 13. What ideas are steal-worthy?

One idea is to treat stimulation-evoked maps as a pressure test for correlational targeting hypotheses.

Another is to publish reusable circuit-response maps instead of keeping targeting logic buried inside single-study narratives.

A third is to make confound control explicit in perturbation-imaging studies rather than assuming the audience will ignore pain and somatosensory artifacts.

### 14. Final decision

Keep. Strong methods value, good causal-targeting infrastructure value, and worth citing whenever resting-connectivity targeting is being treated as if it were enough.