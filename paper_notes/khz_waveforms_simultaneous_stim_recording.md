# Direct delivery of modulated kilohertz frequency waveforms enable simultaneous electrical stimulation and recording with minimal-artifact

## Basic info

* Title: Direct delivery of modulated kilohertz frequency waveforms enable simultaneous electrical stimulation and recording with minimal-artifact
* Authors: Thomas Eggers, Emma Acerbo, Neal Laxpati, Claire-Anne Gutekunst
* Year: 2026
* Venue / source: Journal of Neural Engineering
* Link: https://doi.org/10.1088/1741-2552/ae7765
* Date surfaced: 2026-06-30
* Why selected in one sentence: It attacks a real closed-loop neuromodulation bottleneck by trying to make stimulation and recording coexist without letting artifact theater impersonate physiology.

## Quick verdict

* Highly relevant

This is a preserve note because it goes after a boring but decisive infrastructure problem. Closed-loop stimulation rhetoric gets flimsy fast if the recording channel is mostly artifact and cleanup folklore. This note is based on **abstract-only inspection after 10 full-text acquisition attempts** across the PubMed landing page, PubMed DOI route, DOI landing page, direct publisher HTML route, direct publisher PDF route, Crossref full-text metadata links, OpenAlex open-access lookup, OpenClaw web-fetch route, exact-title search, and author-page / mirror search. The paper appears to be CC BY, but the publisher route was blocked by bot protection in this environment, so implementation-detail confidence is still capped.

## One-paragraph overview

The paper proposes delivering amplitude-modulated kilohertz waveforms directly through implanted electrodes, calling the approach premodulated temporal interference because the modulation is created in the stimulator hardware rather than by field interaction in tissue. The abstract describes benchtop tests, in vivo parameter sweeps, and NEURON simulations using an MRG axon model. The useful result is not that the waveform is magically better at everything. It is narrower and more practical: hardware-generated intermodulation artifacts can be reduced substantially by using parallel stimulators and separate electrodes, amplifier-induced intermodulation still matters, and in one tested pathway the premodulated waveform evokes neural responses similar to conventional square pulses while making linear-filter-based artifact rejection more plausible. That makes this more of a recording-while-stimulating platform note than a new therapeutic claim.

## Model definition

This paper does not present a learned predictive model, but it does include a biophysical simulation model that matters for the intervention logic.

### Inputs
Benchtop stimulation-and-recording setups, implanted-electrode delivery of amplitude-modulated kilohertz waveforms, comparison square-pulse stimulation, recording hardware that can introduce intermodulation artifacts, and simulation inputs for an MRG axon model in the NEURON environment.

### Outputs
Artifact characteristics under different hardware configurations, evoked neural-response thresholds or comparable response measures under premodulated temporal interference versus square pulses, and simulated response thresholds from the MRG axon model.

### Training objective (loss)
There is no trainable loss described in the accessible abstract. The practical objective is to minimize stimulation artifact while preserving meaningful neural activation and recording compatibility.

### Architecture / parameterization
Hybrid methods stack: benchtop hardware measurements, in vivo stimulation experiments, and a conductance-based MRG axon simulation in NEURON, all centered on directly delivered amplitude-modulated kilohertz waveforms and explicit comparison against conventional pulse stimulation.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

It is trying to solve a measurement problem that sits directly underneath closed-loop neuromodulation: how to stimulate electrically while still being able to observe neural responses without drowning in artifact.

### 2. What is the method?

Deliver premodulated amplitude-modulated kilohertz waveforms through implanted electrodes, measure artifact behavior on the bench, compare evoked responses against square pulses in vivo, and use an MRG axon simulation to check whether threshold behavior looks consistent with the experimental findings.

### 3. What is the method motivation?

Kilohertz waveforms occupy spectral territory that can, in principle, be filtered away more cleanly than conventional pulse artifacts. If that works in practice, stimulation and recording can coexist more honestly, which matters for adaptive control and for any attempt to study direct stimulation responses rather than only delayed downstream effects.

### 4. What data does it use?

The accessible abstract indicates benchtop measurements, in vivo experiments in one tested neural pathway, and NEURON simulations using an MRG axon model. The abstract does not expose the full species, sample-size, or recording-stack detail.

### 5. How is it evaluated?

By testing whether intermodulation artifacts can be reduced under different hardware setups, whether amplifier behavior creates additional phantom artifacts, whether premodulated temporal interference evokes comparable neural responses to square pulses, and whether the simulation mirrors the in vivo threshold results.

### 6. What are the main results?

Using parallel stimulators and separate electrodes substantially reduces hardware-based intermodulation. The recording amplifier itself can still introduce another source of intermodulation artifact. In the single tested pathway, premodulated temporal interference produced neural responses similar to conventional square pulses, and the MRG axon simulation reproduced the same threshold pattern qualitatively enough to support the mechanism story.

### 7. What is actually novel?

The novelty is not just “kilohertz waveforms again.” It is the explicit reframing of modulated kilohertz stimulation as a simultaneous stimulation-and-recording method, with hardware intermodulation treated as the real enemy and with direct implanted delivery rather than only noninvasive deep-target branding.

### 8. What are the strengths?

It targets a real bottleneck instead of a decorative one.

It combines bench, in vivo, and simulation evidence rather than relying on only one layer.

It identifies both stimulator-side and amplifier-side artifact sources, which is more useful than pretending the waveform alone solves the problem.

And it keeps the comparison against conventional pulses in view instead of grading itself on a self-chosen artifact metric.

### 9. What are the weaknesses, limitations, or red flags?

This is still an abstract-only keep despite 10 full-text attempts, so exact waveform parameters, sample size, statistics, and recording details remain underexposed.

The abstract only claims response similarity in a single tested pathway, which is a narrow base for broad platform conclusions.

Artifact suppression that works in one hardware stack may fail in another.

And comparable threshold behavior does not by itself prove equivalent safety, selectivity, or information yield for real closed-loop deployment.

### 10. What challenges or open problems remain?

The big open problem is generalization across pathways, amplifiers, electrode geometries, and chronic recording conditions. Another is whether the same approach remains stable enough for online biomarker tracking rather than only short proof-of-principle recordings.

### 11. What future work naturally follows?

Test the approach across more neural pathways and hardware stacks, benchmark real-time biomarker recovery during stimulation, compare it against smarter pulse-artifact cancellation methods, and connect the recording advantage to an actual adaptive-control task instead of stopping at feasibility.

### 12. Why does this matter for cabbageland?

Because cabbageland cares about control logic that can survive contact with measurement reality. If a stimulation method cannot support credible recording during stimulation, then a lot of “adaptive” language is just theater. This paper matters because it tries to make the instrumentation stack less fake.

### 13. What ideas are steal-worthy?

Treat artifact geometry and amplifier behavior as core parts of intervention design, not afterthought cleanup.

Use spectral separation strategically when the goal is simultaneous stimulation and sensing.

And evaluate new stimulation waveforms by whether they improve observability for control, not only by whether they can excite tissue.

### 14. Final decision

Keep as a highly relevant methods note. The full paper could still disappoint on quantitative detail, but the framing is good, the bottleneck is real, and the abstract-level results are useful enough to preserve with explicit confidence limits.
