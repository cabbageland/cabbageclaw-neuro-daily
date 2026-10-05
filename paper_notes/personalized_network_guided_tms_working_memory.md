# Personalized Network-Guided Neuromodulation Enhances Human Working Memory

## Basic info

* Title: Personalized Network-Guided Neuromodulation Enhances Human Working Memory
* Authors: Ahsan Khan, Hongming Li, Camille Blaine, Julie Grier, Ethan Hammett, Almaris Figueroa-Gonzalez, Sarai Garcia, Romain Duprat, Justin Reber, Joseph Deluisi, Christos Davatzikos, Theodore D. Satterthwaite, Yong Fan, Desmond J. Oathes
* Year: 2026
* Venue / source: Advanced Science / PMC full text
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13336854/
* Date surfaced: 2026-10-05
* Why selected in one sentence: It combines individualized functional-network targeting, simultaneous TMS-fMRI, real-time brain-state decoding, and a crossover stimulation test instead of treating TMS frequency or target as one-size-fits-all settings.

## Quick verdict

* Highly relevant

This is a strong keep for personalized noninvasive neuromodulation logic, with one big caveat: it is still a small healthy-adult proof of concept, not clinical evidence. The useful part is the full stack. The paper maps participant-specific working-memory networks, uses a decoder to pick each person's better frequency among 5, 10, and 20 Hz, and then tests optimal versus suboptimal stimulation across repeated sessions. The decoder was not operationally solid enough for every participant, which keeps the result honest rather than fatal.

## One-paragraph overview

The paper asks whether TMS can improve working memory more reliably when both target and frequency are individualized. Nineteen healthy adults completed baseline resting and N-back fMRI, personalized functional-network mapping, an interleaved TMS-fMRI session testing 5, 10, and 20 Hz stimulation, and a randomized crossover phase with three sessions of the individually selected optimal frequency and three sessions of suboptimal frequency. The core result is that optimal-frequency stimulation improved delayed matching-to-sample reaction time at longer delays without hurting accuracy, while a processing-speed control task did not move. The important lesson is not that the authors found a magic frequency. It is that frequency only mattered in interaction with person-specific target and state readout.

## Model definition

### Inputs
The main learned decoder uses fMRI functional signatures extracted from personalized functional networks. Each sample is a time sequence of weighted mean time courses from the individualized network components, especially networks relevant to working memory. The broader intervention pipeline also uses resting-state fMRI, N-back task fMRI, simultaneous TMS-fMRI responses to 5, 10, and 20 Hz stimulation, and behavioral performance during the N-back frequency-selection session.

### Outputs
The decoder outputs a two-class brain-state prediction, operationalized as the probability that the participant is in a 2-back working-memory state rather than the comparison state. That readout is then used to classify tested stimulation frequencies as optimal or suboptimal for a participant. The pipeline also emits individualized cortical TMS targets derived from connectivity to working-memory-relevant personalized functional networks.

### Training objective (loss)
The LSTM decoder is trained with softmax cross-entropy between predicted and true brain-state labels. The implementation uses ADAM with learning-rate decay. The baseline decoder is trained on an independent 90-participant N-back fMRI dataset, then fine-tuned in staged versions using previously collected TMS-fMRI data, with the paper explicitly stating that incoming participants were not used to fine-tune the decoder applied to them.

### Architecture / parameterization
The brain-state decoder is an LSTM recurrent neural network with two hidden LSTM layers of 128 hidden nodes each and a fully connected two-output classifier. Personalized functional networks are computed with spatially regularized non-negative matrix factorization. Target selection uses decoder sensitivity analysis to identify working-memory-relevant networks, then subject-specific connectivity maps constrained by group-level high-connectivity and TMS-accessibility masks. The stimulation parameter tested is frequency within the predefined set of 5, 10, and 20 Hz.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It tries to solve the reproducibility problem in cognitive TMS: the same nominal target and frequency can have different effects across people because working-memory network topography and stimulation response vary individually.

### 2. What is the method?
The authors build personalized functional networks from resting and task fMRI, identify individualized TMS targets connected to working-memory-relevant networks, use simultaneous TMS-fMRI to test 5, 10, and 20 Hz stimulation, and classify each participant's better and worse frequency using decoder output plus a predefined behavioral fallback. Participants then receive both optimal and suboptimal stimulation in a randomized crossover schedule.

### 3. What is the method motivation?
If stimulation effects depend on a person's current network organization and state response, then fixed-frequency TMS is under-specified. The method is motivated by turning target selection and frequency selection into measured quantities instead of inherited defaults.

### 4. What data does it use?
The final analysis uses 19 healthy right-handed adults, ages 18 to 38, after 27 were recruited and 23 completed all visits. Each participant contributed structural MRI, resting-state fMRI, N-back task fMRI, simultaneous TMS-fMRI, delayed matching-to-sample performance, and a processing-speed control task. The baseline decoder was trained on an independent 90-participant N-back fMRI dataset acquired at the same institution and scanner.

### 5. How is it evaluated?
The evaluation has several layers: decoder separation of optimal and suboptimal frequency conditions during TMS-fMRI, N-back performance and balanced integration score during selection, delayed matching-to-sample reaction time and accuracy across optimal versus suboptimal neuromodulation days, a processing-speed control task, post-neuromodulation TMS-fMRI readouts, and an exploratory test of whether a particular frequency band explains the effect.

### 6. What are the main results?
The decoder output was higher for optimal than suboptimal stimulation during the selection session, t(18) = 6.80, p < 0.001, Cohen's d = 1.56. During neuromodulation, optimal stimulation produced faster delayed matching-to-sample responses from Day 1 to Day 3 at 4 s and 12 s delays, while suboptimal stimulation did not. On Day 3, 4 s delay reaction time was faster under optimal than suboptimal stimulation, and 4 s delay accuracy was also higher under optimal stimulation. The processing-speed control task showed no stimulation-specific interaction, and frequency by itself did not explain the behavioral effect.

### 7. What is actually novel?
The novelty is not personalized targeting alone or frequency tuning alone. The useful novelty is putting individualized network target selection, real-time state decoding, empirical frequency selection, and a repeated-session crossover behavioral test into one intervention pipeline.

### 8. What are the strengths?
The paper uses full-stack measurement rather than decorative personalization language. It includes participant-specific network targets, simultaneous TMS-fMRI readout, an active suboptimal-frequency comparator, repeated stimulation sessions, a transfer from N-back selection to delayed matching-to-sample testing, and a processing-speed control task. It also reports the operational decoder weakness instead of hiding it.

### 9. What are the weaknesses, limitations, or red flags?
The sample is small and healthy, with N = 19 instead of the planned larger enrollment. In 9 of 19 participants, the decoder did not produce a reliable real-time discriminative output after the random loop, so frequency selection needed a behavioral fallback. There is no true sham or no-stimulation neuromodulation arm, only an active suboptimal-frequency comparator. The optimal frequency is only the best within 5, 10, and 20 Hz, not a global optimum. The most clinically important question, whether this works in impaired or psychiatric populations, remains untouched.

### 10. What challenges or open problems remain?
The field still needs robust real-time decoders, cheaper sensing routes than TMS-fMRI, prospective replication, test-retest stability of selected frequencies, sham-controlled clinical translation, and better separation of trait-like individual frequency preference from task-state-specific network alignment.

### 11. What future work naturally follows?
Run a larger preregistered sham-controlled replication, test clinical or cognitively impaired cohorts, compare decoder-guided selection against simpler behavioral selection, measure whether the selected frequency remains stable across days and tasks, and port the state readout to EEG, fNIRS, or another deployable modality.

### 12. Why does this matter for cabbageland?
Because it gives a concrete example of what personalized neuromodulation should mean: specify the target network, measure the evoked state, choose parameters empirically, and test whether the chosen settings actually transfer to behavior. It is exactly the antidote to target-name folklore and universal-frequency cargo culting.

### 13. What ideas are steal-worthy?
- Treat frequency as a person-and-state parameter, not as a universal label.
- Use a richer modality to discover the control target, then later search for cheaper proxies.
- Separate target selection from frequency selection instead of pretending one personalized coordinate solves the whole intervention.
- Include an active "bad personalized" comparator so the study tests whether personalization did anything beyond stimulation exposure.
- Report decoder failure modes as part of the engineering result.

### 14. Final decision
Preserve. This is not mature clinical neuromodulation, but it is a genuinely useful proof of concept for individualized target-frequency-state interaction in noninvasive brain stimulation.
