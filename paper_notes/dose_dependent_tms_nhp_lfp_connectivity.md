# Dose-dependent power and connectivity modulation of low frequency oscillations through transcranial magnetic stimulation in non-human primates

## Basic info

* Title: Dose-dependent power and connectivity modulation of low frequency oscillations through transcranial magnetic stimulation in non-human primates
* Authors: Malte Rudo Gueth, Nipun Dilesh Perera, Gary Linn, Kurt Masiello, Brian Russ, Charles E. Schroeder, Adam Falchier, Axel Opitz
* Year: 2026
* Venue / source: Journal of Neural Engineering; full-text basis inspected through the PMC-hosted bioRxiv preprint with the peer-reviewed version cross-checked through PubMed and DOI metadata
* Link: https://doi.org/10.1088/1741-2552/ae93f6
* Date surfaced: 2026-08-23
* Why selected in one sentence: It gives a cleaner translational target-engagement story than most prefrontal TMS papers by showing with intracranial recordings that single-pulse intensity scales early low-frequency power and short-range plus long-range phase coupling rather than only changing a scalp proxy.

## Quick verdict

* Highly relevant

This is a real keep because it attacks one of the field's actual blind spots: people talk about left-prefrontal TMS as if the target is obvious, while the physiology is usually inferred through messy scalp readouts or symptom averages. Here the authors use intracranial recordings in rhesus macaques to show a dose-dependent three-stage response in low-frequency power and connectivity after single pulses over left prefrontal cortex. The study is still small, anesthetized, and nonhuman, so it does not tell us that clinical protocols are already mechanistically solved. But it is much closer to target-engagement evidence than most clinical TMS papers.

## One-paragraph overview

The paper studies two anesthetized rhesus macaques implanted with three stereo-EEG depth electrodes each, spanning anterior prefrontal, cingulate, insular, parietal, and temporal regions, while single biphasic TMS pulses were applied over left prefrontal cortex at six intensities from 10 percent to 125 percent of maximum stimulator output, plus a passive click-only control. Using time-frequency analysis of intracranial local field potentials and phase-based connectivity analysis with debiased weighted phase-lag index, the authors show a repeatable three-stage low-frequency response. First, frontal 1 to 4 hertz power rises rapidly after the pulse in contacts near the stimulation site. Second, a broader 1 to 13 hertz suppression spreads across frontal, temporal, and parietal contacts. Third, connectivity and power partially rebound around 1500 milliseconds, except at the highest intensities where suppression can persist longer. The key useful result is that both early power enhancement and early short-range plus long-range connectivity enhancement scale with stimulation intensity, while later suppression and rebound appear more thresholded and less cleanly dose-tuned. That makes the paper useful not as direct clinical efficacy evidence, but as a translational map of what left-prefrontal TMS may actually do to oscillatory dynamics and network propagation.

## Model definition

This is not a trainable prediction paper. It is a perturbation physiology study that combines intracranial recordings, time-frequency analysis, and phase-based connectivity estimation to characterize how TMS pulse intensity changes brain dynamics.

### Inputs
Single biphasic TMS pulses over left prefrontal cortex in two rhesus macaques, delivered at 10 percent, 25 percent, 50 percent, 70 percent, 90 percent, and for one monkey 125 percent of maximum stimulator output; intracranial stereo-EEG local field potentials from 28 to 29 contacts spanning frontal, cingulate, insular, parietal, and temporal regions; passive click-only sham blocks; and baseline blocks recorded before each stimulation condition.

### Outputs
Baseline-corrected time-frequency power estimates from 1 to 40 hertz; significant spatiotemporal clusters of pulse-related power modulation; phase-based connectivity estimates using debiased weighted phase lag index between the most anterior frontal seed contact and the remaining contacts; and dose-response comparisons across stimulation intensities.

### Training objective (loss)
There is no trainable model or optimization loss. The main analyses are cluster-level permutation tests over time-frequency-sensor data, post-hoc intensity comparisons, one-way ANOVAs on connectivity values, and corresponding post-hoc tests.

### Architecture / parameterization
The parameterization is the stimulation-and-recording stack itself: two anesthetized rhesus macaques, three implanted stereo-EEG depth electrodes per animal, single-pulse biphasic TMS over left prefrontal cortex, 80 pulses per intensity block except 40 pulses at 125 percent MSO, passive click-only control, complex Morlet wavelet analysis, and phase-based connectivity centered on the frontal contact nearest the coil.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve a target-engagement problem. Clinical TMS over left dorsolateral prefrontal cortex is widely used, especially in depression, but the field still lacks clear mechanistic markers showing what the stimulation actually does to local and distributed neural dynamics. Human scalp EEG is helpful but spatially ambiguous. This paper asks whether intracranial recordings can show how TMS intensity changes low-frequency power and inter-regional coupling in networks connected to the left prefrontal target.

### 2. What is the method?
The authors applied single biphasic TMS pulses over the left prefrontal cortex of two anesthetized rhesus macaques while recording intracranial local field potentials through three stereo-EEG depth electrodes per animal. Active stimulation was delivered at six intensities, with a passive click-only condition as control. They then analyzed pulse-locked power changes using time-frequency methods and analyzed phase-based connectivity from the frontal seed contact to all other contacts using debiased weighted phase lag index.

### 3. What is the method motivation?
The motivation is simple and good: if TMS is supposed to modulate clinically relevant prefrontal circuits, then we should stop pretending that symptom averages or noisy scalp proxies are enough. Intracranial recordings in a nonhuman primate model offer a cleaner look at what intensities do locally and across structurally connected downstream regions. That makes it possible to separate immediate excitation, later suppression, and network spread rather than collapsing everything into one vague "stimulation effect."

### 4. What data does it use?
The study uses intracranial stereo-EEG data from two adult rhesus macaques, one with 29 contacts and one with 28 contacts. The electrodes sampled anterior prefrontal, cingulate, insular, parietal, occipital, and temporal regions. Each stimulation block contained 80 pulses except the highest-intensity 125 percent block, which had 40 trials because of excessive movement. The recordings were preprocessed with artifact interpolation, ICA-based muscle-artifact cleanup, resampling to 1 kilohertz, and baseline correction using a matched no-pulse block recorded before each condition.

### 5. How is it evaluated?
Evaluation happens at two levels. First, the paper uses cluster-level permutation tests to identify significant spatiotemporal and spectral regions where power changes differ across stimulation intensities relative to passive control. Second, it tests whether phase-based connectivity between the stimulation-site seed and other contacts changes across three post-pulse time windows, and whether those connectivity changes scale with stimulation intensity.

### 6. What are the main results?
- The cleanest result is a three-stage low-frequency response after active pulses: an early 1 to 4 hertz power increase, a broader 1 to 13 hertz suppression, and a later rebound at a subset of contacts.
- Early low-frequency power enhancement near the stimulation site scaled upward with increasing intensity in both monkeys.
- The broader 1 to 13 hertz suppression spread across anterior frontal, insular, and temporal contacts and became stronger at higher intensities, especially 90 percent MSO and the single-monkey 125 percent condition.
- The strongest intensities produced the largest early enhancement but also the longest later suppression, sometimes preventing a full rebound by the end of the analyzed window.
- Phase-based connectivity between the frontal seed and proximal plus distal contacts increased immediately after the pulse, including contacts in insular, posterior cingulate, parietal, and parahippocampal regions.
- Only this early connectivity enhancement showed a reliable intensity effect. Connectivity then dropped toward or below passive-control levels around 300 milliseconds and later partially rebounded without a clear intensity gradient.

### 7. What is actually novel?
The useful novelty is not just "TMS plus intracranial recording in monkeys." The sharper contribution is the dose-dependent dissociation between early enhancement and later suppression across both power and connectivity, measured directly in networks relevant to left-prefrontal stimulation. That gives the field a more concrete mechanistic template than the usual scalp-level story: stronger pulses do not simply mean more of one thing. They mean a stronger early boost followed by a stronger and longer suppressive phase, with network effects propagating along anatomically plausible connections.

### 8. What are the strengths?
- It measures target engagement with intracranial signals rather than only scalp EEG or symptoms.
- It explicitly tests intensity scaling instead of treating pulse strength as a background setting.
- The design includes a passive click-only control, which helps separate magnetic stimulation effects from auditory confounds.
- The results are distributed rather than purely local, which is exactly what a network-level perturbation paper should show.
- The paper is refreshingly clear that early enhancement, later suppression, and rebound are distinct phases instead of one monolithic stimulation effect.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is only two anesthetized monkeys, so variability and state dependence are serious limitations.
- Anesthesia likely altered cortical excitability and may have attenuated or distorted the response geometry relative to awake brains.
- One monkey alone received 125 percent MSO, so the highest-intensity behavior is suggestive rather than well replicated.
- A delayed low-frequency increase in one monkey may partly reflect auditory response to the TMS click.
- The paper focuses on the low-frequency cluster with strongest translational appeal, while additional broadband effects up to 37 hertz are left for future work.
- This note is based on full-text inspection of the PMC-hosted bioRxiv preprint, with the peer-reviewed Journal of Neural Engineering version cross-checked through PubMed abstract and DOI metadata rather than line-by-line full-body journal HTML.

### 10. What challenges or open problems remain?
The biggest open problem is state dependence. It remains unclear how much of this response geometry survives in awake animals or humans doing behavior, and whether the same early-enhancement to later-suppression pattern explains therapeutic protocols rather than only single-pulse physiology. It also remains unresolved which phase of the response matters most for downstream plasticity or symptom change, and whether intensity is the right main control variable compared with phase, ongoing state, or structural targeting.

### 11. What future work naturally follows?
The obvious follow-on is to repeat this kind of intracranial perturbation work in awake preparations or human intracranial settings where behavior and state can be measured directly. It would also be valuable to connect these low-frequency signatures to plasticity-relevant outcomes, compare single-pulse and patterned protocols, and test whether closed-loop timing can amplify the useful early network enhancement without paying as much cost in later suppression.

### 12. Why does this matter for cabbageland?
It matters because it makes left-prefrontal TMS look less like a black-box clinical ritual and more like a controllable network perturbation with identifiable temporal phases. The field keeps asking whether stimulation "engages the target" without being very specific about what that should look like. This paper gives a stricter answer: at least for a translational intracranial model, engagement means intensity-dependent changes in low-frequency power and connectivity that spread along anatomically plausible pathways instead of just creating a local blip.

### 13. What ideas are steal-worthy?
- Treat TMS intensity as a control variable whose effect may flip across time rather than only scale in one direction.
- Use early enhancement and later suppression as separate candidate biomarkers instead of averaging them into one summary.
- Ask whether downstream propagation follows known anatomical pathways rather than assuming it does.
- Design closed-loop or adaptive protocols to exploit the early connectivity-boost phase while avoiding unnecessary later suppression.
- Use cleaner perturbation physiology in translational models to calibrate what clinical target engagement should even mean.

### 14. Final decision
Preserve as a highly relevant translational target-engagement note. It is not clinical efficacy evidence, and the anesthesia plus two-monkey design keeps the claims narrow. But it gives a much better mechanistic picture of what left-prefrontal TMS pulses actually do to low-frequency power and network coupling than most human TMS papers manage.
