# Transcranial alternating current stimulation can disrupt or reestablish neural entrainment in parkinsonian motor cortex

## Basic info

* Title: Transcranial alternating current stimulation can disrupt or reestablish neural entrainment in parkinsonian motor cortex
* Authors: Authors not fully recovered during this inspection pass from the accessible PMC manuscript text
* Year: 2026
* Venue / source: Brain Stimulation
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13037566/
* Date surfaced: 2026-05-26
* Why selected in one sentence: It gives a mechanistic dose-response account of when transcranial alternating current stimulation suppresses versus reinforces pathological beta locking in a parkinsonian primate model.

## Quick verdict

* Useful

This is not a clinical efficacy paper, but it is one of the cleaner recent mechanism papers for noninvasive oscillatory control. The interesting claim is that weak fields can disrupt endogenous beta synchronization while stronger or frequency-matched fields can instead entrain and reinforce it. That matters because it turns tACS parameter choice into a state-competition problem, not just a “more current equals more effect” problem.

## One-paragraph overview

The paper records single-unit spiking in motor cortex, premotor cortex, and supplementary motor area in three MPTP-parkinsonian rhesus macaques during transcranial alternating current stimulation. The stimulation is delivered across a range of current amplitudes and frequencies, with special focus on beta-matched sixteen-hertz stimulation. The authors examine how spike timing locks to the external stimulation phase and how that locking interacts with the animals’ endogenous beta rhythm. The main pattern is a dose-dependent reversal. Stronger fields produce entrainment to the applied rhythm, but weak fields can disrupt existing beta synchronization and shift preferred spiking phase instead of simply amplifying the same oscillation. The preserve-worthy part is the mechanistic framing that low-intensity stimulation can compete with, rather than merely overwrite, pathological network timing.

## Model definition

### Inputs
Applied tACS frequency, tACS current amplitude, stimulation montage, estimated cortical electric field, and single-unit recordings from motor cortical regions in parkinsonian non-human primates.

### Outputs
Phase-locking values, preferred spiking phase relative to stimulation, and frequency- and intensity-dependent changes in neural entrainment or desynchronization.

### Training objective (loss)
There is no trainable predictive model here. The paper is an experimental electrophysiology study with phase-locking and dose-response analyses.

### Architecture / parameterization
A stimulation-and-recording experimental setup in parkinsonian non-human primates using cortical arrays, artifact-cleaned electrophysiology, and phase-locking analysis across multiple tACS intensities and frequencies.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The field wants to use tACS to modulate pathological oscillations in Parkinson disease, but it still does not have a clean mechanistic account of how stimulation intensity and frequency interact with ongoing beta rhythms at the single-neuron level.

### 2. What is the method?
Record cortical single units in parkinsonian primates during tACS, vary intensity and frequency, estimate local electric fields, and quantify how spike timing locks to stimulation versus endogenous oscillatory activity.

### 3. What is the method motivation?
If pathological beta synchrony is the intervention target, then the critical question is not merely whether tACS changes activity. It is whether the stimulation weakens, shifts, or reinforces pathological timing, and under what field regime.

### 4. What data does it use?
Single-unit recordings from three MPTP-parkinsonian rhesus macaques with motor cortical arrays spanning primary motor, premotor, and supplementary motor regions during resting recordings and multiple tACS conditions.

### 5. How is it evaluated?
By computing phase-locking values, preferred spiking phases, and dose-response patterns across stimulation intensities, frequencies, and montages, while estimating the electric fields reaching cortex.

### 6. What are the main results?
Beta-matched stimulation can strongly entrain neurons when the electric field is strong enough, but weak-field stimulation can instead disrupt endogenous beta synchronization and alter phase preference. Frequency matching matters, because sixteen-hertz stimulation aligned with the endogenous rhythm produced the clearest entrainment pattern. The overall result is that tACS effects are not monotonic. The same modality can either suppress or reestablish locking depending on parameter regime.

### 7. What is actually novel?
The valuable novelty is the explicit mechanistic split between weak-field desynchronization and strong-field entrainment in a parkinsonian primate cortex, measured at the spike-timing level rather than inferred from coarse behavior alone.

### 8. What are the strengths?
- Uses a disease-relevant primate model rather than only healthy-human EEG.
- Measures single-unit timing, which is closer to the actual control problem.
- Treats dose dependence seriously instead of flattening all tACS into one effect.
- Gives a plausible explanation for why tACS studies can appear inconsistent across parameter regimes.

### 9. What are the weaknesses, limitations, or red flags?
- This is still not a behavioral or clinical efficacy study.
- The work is cortical and acute, not a full long-horizon network-therapy demonstration.
- The sample is only three animals.
- Motor-cortex beta physiology in MPTP primates is relevant, but it is not the whole Parkinson disease intervention landscape.

### 10. What challenges or open problems remain?
We still need state-aware dosing rules, translation from measured cortical field to practical human montages, and evidence that the desynchronizing regime improves behavior without creating other timing problems.

### 11. What future work naturally follows?
Closed-loop tACS that estimates endogenous beta state before choosing amplitude or phase, tests that connect desynchronization to motor benefit, and cross-modal studies linking spike-level effects to field models and human biomarkers.

### 12. Why does this matter for cabbageland?
Because it sharpens the intervention logic for oscillatory control. It says weak stimulation may be useful precisely because it competes with ongoing pathological timing instead of bulldozing the network with a stronger external rhythm.

### 13. What ideas are steal-worthy?
- Treat weak-field stimulation as competitive phase control, not just low-power entrainment.
- Separate desynchronization goals from entrainment goals at the parameter-design level.
- Ask whether the clinically useful regime is the one that nudges phase variability rather than maximizes locking.
- Use spike-timing evidence to constrain human tACS theory instead of building from scalp folklore alone.

### 14. Final decision
Keep as mechanistically useful noninvasive stimulation work. It is not clinical proof, but it does improve the control story.