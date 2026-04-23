# Residential Therapy With Navigated Transcranial Magnetic Stimulation for Combat-Related PTSD

## Basic info

* Title: Residential Therapy With Navigated Transcranial Magnetic Stimulation for Combat-Related PTSD
* Authors: Mark S. George et al.
* Year: 2026
* Venue / source: JAMA Network Open
* Link: https://doi.org/10.1001/jamanetworkopen.2026.5110
* Date surfaced: 2026-04-23
* Why selected in one sentence: It is a sham-controlled PTSD trial where TMS targeting was individualized anatomically and connectomically inside an intensive real-world treatment program rather than bolted onto a thin outpatient protocol.

## Quick verdict

* Highly relevant

This is one of the more useful recent psychiatric TMS papers because it combines individualized targeting with an actual randomized sham design and nontrivial follow-up. The main problem is interpretability, because both arms also received a very strong residential therapy package, so the paper shows incremental benefit of navigated TMS inside a treatment stack rather than isolated stimulation efficacy. Still, that is better evidence than the usual open-label targeting rhetoric.

## One-paragraph overview

The paper tests whether navigated TMS adds benefit to an intensive residential treatment program for combat-related PTSD. Participants received thirty days of standard residential care built around prolonged exposure and daily psychotherapeutic augmentation, then were randomized to active versus sham navigated TMS delivered daily for up to twenty sessions. The targeting was individualized using structural and functional MRI and delivered with robotic stereotaxy. Both groups improved substantially, which is unsurprising given the treatment context, but active TMS still produced superior symptom relief on PTSD scales at end of treatment and showed better durability on some follow-up measures. The practical read is that individualized TMS may offer real added value, but the paper does not isolate which part of the targeting package matters most.

## Model definition

### Inputs
Structural and functional MRI were used to define individualized TMS targets for each participant. The accessible abstract does not describe a trainable predictive model beyond the targeting workflow itself.

### Outputs
Personalized stimulation targets for navigated TMS delivery. The main study outputs are clinical outcomes, especially PTSD and depression symptom scores, not model predictions.

### Training objective (loss)
Not applicable from the accessible text. This appears to be an individualized imaging-guided targeting workflow rather than a supervised predictive model paper.

### Architecture / parameterization
No explicit learnable architecture is described in the accessible abstract. The relevant parameterization is the individualized anatomical and connectomic targeting plus robotic stereotactic delivery.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Combat-related PTSD remains hard to treat, and standard therapies leave many patients with persistent symptoms. The paper asks whether individualized navigated TMS can add clinically meaningful benefit when layered on top of intensive residential care.

### 2. What is the method?
A randomized, blinded, active-versus-sham clinical trial in which both groups received the same residential treatment program, while the stimulation arm received individualized MRI-guided navigated TMS and the control arm received sham TMS.

### 3. What is the method motivation?
The motivation is that TMS effects may depend heavily on where stimulation lands. Using structural and functional MRI plus robotic stereotaxy is meant to make targeting more precise than generic scalp-coordinate placement.

### 4. What data does it use?
The abstract reports one hundred nineteen randomized participants drawn from military personnel with moderate to extreme PTSD severity, treated in a residential military mental health facility.

### 5. How is it evaluated?
The main outcome is change in PTSD Checklist for DSM-5 scores from baseline to end of treatment. Secondary outcomes include CAPS-5 clinician-rated PTSD severity and PHQ-9 depression scores across treatment and follow-up.

### 6. What are the main results?
- Both active and sham groups improved relative to baseline.
- Active TMS outperformed sham on PCL-5 and CAPS-5 at end of treatment.
- Some follow-up measures suggested better durability for active TMS, including PCL-5 and PHQ-9.
- Reliable change analyses also favored active TMS on one-month PTSD symptom durability.

### 7. What is actually novel?
The novelty is not that TMS can help PTSD. It is the combination of individualized anatomical plus connectomic targeting, robotic delivery, and testing inside a serious sham-controlled residential-treatment design.

### 8. What are the strengths?
- Real randomized sham-controlled design.
- Reasonable sample size for a neuromodulation psychiatry trial.
- Individualized targeting rather than generic placement.
- Follow-up rather than end-of-treatment only.
- Residential program context reduces the complaint that treatment exposure was weak or inconsistent.

### 9. What are the weaknesses, limitations, or red flags?
- The residential treatment package was so strong that the marginal contribution of stimulation remains hard to parse mechanistically.
- I did not inspect the full paper, so exact stimulation protocol details and subgroup effects remain uncertain.
- This does not prove that the connectomic targeting logic itself, as opposed to better overall care plus some stimulation, is the key active ingredient.
- Military residential cohorts may not generalize cleanly to broader PTSD populations.

### 10. What challenges or open problems remain?
We still need cleaner tests that separate target choice, stimulation dose, therapy context, and patient subtype. More work is also needed on which imaging features actually determine the best target for a given symptom cluster.

### 11. What future work naturally follows?
Head-to-head comparisons of generic versus individualized targets, target-level mediation analyses, stratification by trauma phenotype and comorbidity, and trials that use online biomarkers rather than static MRI alone.

### 12. Why does this matter for cabbageland?
It matters because it treats psychiatric TMS as a targeting problem embedded in a treatment system, not just as a coil plus symptom scale. That makes it much closer to the intervention-design questions that actually matter.

### 13. What ideas are steal-worthy?
- Test stimulation inside realistic treatment stacks instead of pretending context does not matter.
- Treat individualized targeting as a concrete design choice that must beat simpler baselines.
- Separate immediate symptom change from durability, because persistence may be the more informative outcome.
- Use better delivery precision when arguing for circuit-specific psychiatry effects.

### 14. Final decision
Keep. This is not a clean mechanistic proof of connectomic targeting, but it is a serious clinical neuromodulation study with better targeting logic than most PTSD TMS papers.
