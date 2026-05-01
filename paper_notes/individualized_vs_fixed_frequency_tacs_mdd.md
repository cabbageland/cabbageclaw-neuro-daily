# Differential effects of individualized vs. fixed-frequency tACS on clinical and EEG outcomes in major depressive disorder

## Basic info

* Title: Differential effects of individualized vs. fixed-frequency tACS on clinical and EEG outcomes in major depressive disorder
* Authors: Dan Li et al.
* Year: 2026
* Venue / source: Journal of Affective Disorders
* Link: https://pubmed.ncbi.nlm.nih.gov/41690627/
* Date surfaced: 2026-05-01
* Why selected in one sentence: It directly tests whether individualized alpha-frequency transcranial alternating current stimulation in depression actually beats a simple fixed-frequency protocol.

## Quick verdict

* Highly relevant

This is worth preserving mainly because the result is usefully unspectacular. The paper asks a real question about personalization, uses a randomized double-blind design, and fails to show a clear clinical advantage for individualized alpha frequency over fixed ten-hertz stimulation. The absence of a sham arm keeps the mechanistic EEG findings from carrying too much weight, but the negative result itself is valuable because it narrows what future personalization claims need to prove.

## One-paragraph overview

The study randomized seventy-two outpatients with major depressive disorder into four active transcranial alternating current stimulation arms that crossed frequency choice, fixed ten hertz versus individualized alpha frequency, with administration intensity, once daily versus twice daily. Over two weeks, participants completed twenty sessions and underwent EEG before and after treatment, followed by two weeks of clinical follow-up. The authors report no significant clinical superiority for individualized-alpha stimulation and no significant administration-frequency difference either, although fixed-frequency and higher-administration arms showed favorable symptom trends. EEG analyses found reduced parietal alpha power spectral density in the higher-frequency-administration condition and enhanced frontal functional connectivity in the fixed-frequency groups. The useful read is that protocol-dependent physiological changes exist, but the personalization story is not clinically earned yet.

## Model definition

This paper contains analysis and prediction-style EEG comparisons, but no clearly defined primary trainable treatment-selection model in the accessible abstract.

### Inputs
Resting-state EEG acquired before and after treatment, clinical depression ratings, stimulation protocol assignment, and frequency-condition labels such as fixed ten hertz versus individualized alpha frequency.

### Outputs
Clinical symptom change and EEG-derived outcomes, especially parietal alpha power spectral density and frontal functional-connectivity measures.

### Training objective (loss)
The accessible abstract does not describe a trainable predictive model or optimization loss.

### Architecture / parameterization
A randomized double-blind four-arm intervention study comparing stimulation protocol variants rather than a single learnable model.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Transcranial alternating current stimulation for depression often leans on the intuition that matching stimulation frequency to an individual’s alpha rhythm should improve efficacy. The paper tests whether that intuition holds up in a randomized comparison.

### 2. What is the method?

Patients were assigned to one of four active tACS conditions: once-daily fixed ten-hertz, once-daily individualized alpha frequency, twice-daily fixed ten-hertz, or twice-daily individualized alpha frequency. They completed twenty sessions over two weeks with EEG recorded before and after treatment.

### 3. What is the method motivation?

If depression-relevant oscillatory dysfunction differs across individuals, then tailoring stimulation frequency to each person’s alpha rhythm might produce better engagement than a one-size-fits-all frequency.

### 4. What data does it use?

The accessible abstract reports seventy-two outpatients with major depressive disorder in a randomized double-blind design, with pre-treatment and post-treatment EEG plus clinical outcome tracking over a four-week study period.

### 5. How is it evaluated?

By comparing symptom improvement and EEG changes across the four active treatment conditions, focusing on frequency choice and administration intensity.

### 6. What are the main results?

No significant clinical differences were observed between individualized-alpha and fixed-frequency groups, or between twice-daily and once-daily administration. There were favorable symptom trends for fixed-frequency and higher-administration groups. EEG analyses showed reduced parietal alpha power in the higher-administration condition and enhanced frontal connectivity in the fixed-frequency groups.

### 7. What is actually novel?

The useful novelty is not the claim that tACS helps depression. It is the direct randomized test of individualized alpha frequency against a fixed-frequency baseline within the same trial structure.

### 8. What are the strengths?

- It asks a real personalization question rather than assuming one.
- The study is randomized and double-blind.
- It combines clinical outcome readouts with EEG changes.
- The negative or nonconfirmatory result is more informative than another uncontrolled personalization success story.

### 9. What are the weaknesses, limitations, or red flags?

- There is no sham arm, so active-versus-nonspecific improvement cannot be separated cleanly.
- The sample is moderate but still not large for a four-arm design.
- EEG changes do not rescue the absence of clear clinical superiority.
- The accessible abstract leaves important details unclear, including montage specifics, responder definitions, and multiplicity handling.

### 10. What challenges or open problems remain?

The main open problem is identifying what kind of personalization, if any, actually matters for tACS in depression. Frequency matching alone may be too shallow. Targeting, state dependence, symptom subtype, and longitudinal adaptation may matter more.

### 11. What future work naturally follows?

A sham-controlled trial that combines frequency choice with individualized targeting or state-triggered delivery would be more informative. It would also help to test whether baseline EEG features prospectively predict which protocol, if any, benefits a given patient.

### 12. Why does this matter for cabbageland?

Because it is exactly the kind of paper that keeps personalization claims honest. If individualized alpha frequency cannot beat a fixed ten-hertz protocol in a randomized comparison, then future tACS work needs a stronger mechanistic argument than “personalized equals better.”

### 13. What ideas are steal-worthy?

- Treat negative personalization results as valuable constraints, not disappointments.
- Separate the questions of frequency personalization, spatial targeting, and delivery schedule instead of bundling them into one vague precision claim.
- Use EEG changes as mechanistic clues, but do not let them substitute for clinical evidence.

### 14. Final decision

Keep as a highly relevant skepticism-preserving note. The paper does not prove a better tACS protocol, but it usefully weakens a common personalization shortcut and points toward more substantive intervention logic.
