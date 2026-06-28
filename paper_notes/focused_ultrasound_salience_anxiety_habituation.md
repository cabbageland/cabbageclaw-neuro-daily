# Focused Ultrasound Neuromodulation of Salience Network Hubs Selectively Enhances Anxiety-Relevant Autonomic Habituation in Humans

## Basic info

* Title: Focused Ultrasound Neuromodulation of Salience Network Hubs Selectively Enhances Anxiety-Relevant Autonomic Habituation in Humans
* Authors: Jennifer Legon, Yunruo Ni, Wynn Legon
* Year: 2026
* Venue / source: Biological Psychiatry Global Open Science
* Link: https://pubmed.ncbi.nlm.nih.gov/42281605/
* Date surfaced: 2026-06-28
* Why selected in one sentence: It is a rare anxiety-relevant human ultrasound paper that earns attention by finding a narrow, multimodally constrained effect instead of pretending deep-target stimulation changed everything at once.

## Quick verdict

* Highly relevant

This is a strong mechanistic keep because the paper is more disciplined than the usual salience-network neuromodulation story. I could inspect the full PMC text here, and the main result is selective rather than inflated: low-intensity focused ultrasound to anxiety-relevant anterior-insula and anterior-midcingulate targets steepened early electrodermal habituation relative to sham, while electromyogram and EEG habituation stayed null. That is exactly why the paper is worth preserving. It gives a causal hint about salience-autonomic regulation without overselling itself as an anxiety-treatment breakthrough.

## One-paragraph overview

The study asks whether anxiety-relevant salience-network hubs causally shape habituation to repeated aversive sensory probes and whether habituation slope is a more informative marker than response magnitude. Forty healthy adults completed a single-blind, sham-controlled crossover protocol with MRI/CT-guided low-intensity focused ultrasound targeted to the right anterior insula, the anterior midcingulate cortex, or sham on separate visits. Before stimulation, higher trait anxiety predicted weaker startle electromyogram habituation, but not EEG or electrodermal habituation. After stimulation, both active targets selectively enhanced early-window electrodermal habituation relative to sham, while EMG and EEG slopes remained unchanged. The useful residue is simple: this is not evidence for broad anxiolysis, but it is credible evidence that network-informed ultrasound can selectively perturb an autonomic adaptation channel linked to salience processing.

## Model definition

This paper does not contain a central trainable predictive model.

### Inputs
Low-intensity focused ultrasound condition, including right anterior-insula targeting, anterior-midcingulate targeting, or sham; participant trait and state anxiety scores; and repeated acoustic-startle recordings from electromyography, EEG, and electrodermal response channels before and after stimulation.

### Outputs
Early- and late-window habituation slopes for EMG, EEG, and electrodermal responses, plus estimated relationships between those slopes, anxiety measures, and stimulation condition.

### Training objective (loss)
There is no learnable model with a training loss. The core analyses use Theil-Sen slope estimation, Spearman and repeated-measures correlations, and linear mixed-effects models on habituation trajectories.

### Architecture / parameterization
Single-blind, sham-controlled, within-subject crossover human perturbation study using MRI/CT-informed acoustic modeling, 40-second low-intensity focused ultrasound exposures, and mixed-effects analysis of multimodal startle-habituation dynamics.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to test whether anxiety-relevant salience-network targets actually causally influence sensory/autonomic habituation in humans, instead of leaving that claim at the level of correlational imaging rhetoric.

### 2. What is the method?
Participants completed three randomized sessions, one each for right anterior-insula ultrasound, anterior-midcingulate ultrasound, and sham. In each session, the authors recorded 12 repeated acoustic-startle trials before and about 5 minutes after stimulation, then estimated early- and late-window habituation slopes for EMG, EEG, and electrodermal responses.

### 3. What is the method motivation?
If anxiety partly reflects impaired filtering and persistent salience/autonomic mobilization, then salience-network perturbation should change habituation dynamics in measurable ways. The paper treats habituation slope, not raw amplitude, as the candidate biomarker.

### 4. What data does it use?
The accessible full text reports 40 healthy adults, mean age 26.2 years, in a four-visit protocol. The analyzed data include structural MRI and CT for targeting/acoustic modeling, trait and state anxiety scores, and pre/post startle responses measured with EMG, EEG, and electrodermal recordings.

### 5. How is it evaluated?
The authors evaluate whether pre-LIFU habituation slopes relate to trait or state anxiety, then test whether pre-to-post slope changes differ between active stimulation and sham, separately for early and late windows and for each physiological channel.

### 6. What are the main results?
- Higher trait anxiety predicted weaker EMG habituation before stimulation, with modest but significant correlations in both early and late windows.
- State anxiety did not reliably predict habituation in any channel.
- Ultrasound to either the anterior insula or anterior midcingulate cortex significantly increased early-window electrodermal habituation relative to sham.
- Ultrasound did not significantly change EMG or EEG habituation relative to sham.
- EMG and EEG habituation were correlated with each other, while electrodermal habituation was relatively dissociable.
- Mean response magnitudes were less informative than habituation slopes for both anxiety associations and stimulation effects.

### 7. What is actually novel?
The novelty is not merely that focused ultrasound reached deep or hard-to-access anxiety circuitry. The useful novelty is the selective causal profile: the paper uses multimodal habituation slopes and finds a specific autonomic effect rather than a generic all-channel enhancement story. It also frames the anterior-insula target as a network-informed anxiety convergence zone rather than pretending the sonication footprint is a perfect point target.

### 8. What are the strengths?
- Full text was accessible, so the design and discussion could be inspected beyond the abstract.
- Within-subject crossover plus sham control is much better than a loose pre/post feasibility story.
- The paper uses individualized MRI/CT targeting and acoustic modeling rather than hand-wavy atlas aiming.
- It measures somatic, cortical, and autonomic channels together instead of collapsing everything into one vague biomarker.
- The null results are reported plainly, which makes the positive electrodermal finding more believable.

### 9. What are the weaknesses, limitations, or red flags?
The study is still a healthy-volunteer mechanistic experiment, not a patient trial or treatment study. It is single-blind rather than clearly double-blind. The active effect is narrow, confined to early electrodermal habituation, so anyone trying to spin this as a general anxiety intervention paper is getting ahead of the data. The right anterior-insula target also overlaps a broader salience-network territory including inferior frontal and superior temporal cortex, so the causal claim is network-informed rather than parcel-pure.

### 10. What challenges or open problems remain?
The field still needs replication in anxious patient populations, better tests of whether these habituation markers predict symptoms or treatment response, stronger sham/blinding validation, and more explicit state-dependent stimulation logic rather than one fixed post-stim assay.

### 11. What future work naturally follows?
Test the same perturbation logic in anxiety disorders, link baseline EMG or electrodermal habituation to clinical heterogeneity, compare salience-target ultrasound against other perturbation modalities, and ask whether autonomic-habituation markers can support adaptive or closed-loop intervention timing.

### 12. Why does this matter for cabbageland?
Because it is a good example of how to evaluate anxiety neuromodulation without collapsing into fantasy. The paper separates channels, tolerates nulls, and suggests that autonomic adaptation may be easier to move than cortical or somatic readouts. That is much more useful than another omnibus “salience network modulation improved anxiety” claim.

### 13. What ideas are steal-worthy?
- Treat habituation slope as a more serious perturbation-readout candidate than mean response amplitude.
- Use multimodal channels to test whether an intervention effect is selective or global.
- Accept network-informed targeting language when the acoustic footprint makes point-target certainty unrealistic.
- Pair clinical-theory claims about anxiety with body-channel readouts instead of only symptom scales or generic fMRI differences.

### 14. Final decision
Keep. This is one of the better recent human ultrasound papers for anxiety-relevant mechanism because it makes a constrained causal claim that survives contact with its own null results. It is not treatment proof, but it is real signal.
