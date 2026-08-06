# Depression Improvement Correlates With Lower TMS Intensity in a Randomized Trial With Real-Time E-Field Modeling

## Basic info

* Title: Depression Improvement Correlates With Lower TMS Intensity in a Randomized Trial With Real-Time E-Field Modeling
* Authors: Prem Ganesh, Hakjoo Kim, Jamie Kweon, Mark A. Halko, Kevin A. Caulfield, Joshua C. Brown
* Year: 2026
* Venue / source: Human Brain Mapping
* Link: https://doi.org/10.1002/hbm.70607
* Date surfaced: 2026-08-06
* Why selected in one sentence: It is a rare prospective paper that treats TMS dose as an estimated cortical-field-delivery problem rather than motor-threshold folklore, and it suggests that lower prefrontal field strength may actually work better.

## Quick verdict

* Highly relevant

This is a real keep because it attacks a modifiable clinical lever that the field still handles sloppily. The useful contribution is not just that E-field modeling improves biophysical precision over a flat `120% rMT` rule. It is that the better-outcome signal points toward *lower* DLPFC field strength, which directly challenges the lazy "more intensity is probably better" reflex. The caveat is equally important: this is a small secondary analysis without randomized intensity assignment, so it is a strong hypothesis-sharpening paper, not a dosing guideline.

## One-paragraph overview

The paper takes MRI, neuronavigation, and finite-element modeling seriously enough to separate machine output from estimated cortical dose in accelerated iTBS for depression. Twenty-eight participants with major depressive disorder from a randomized, double-blind, placebo-controlled single-day accelerated TMS trial had usable MRI for subject-specific modeling. During planning, the authors used a real-time spherical head model to adjust left DLPFC stimulation so that estimated field strength matched the motor-cortex field at resting motor threshold. Offline SimNIBS finite-element simulations were then used to quantify how much cortical-field precision this individualized approach gained over the conventional `120% rMT` rule, and whether any intensity description actually tracked symptom change. The paper matters because the individualized method was more precise, the required DLPFC intensity varied wildly across people, and lower modeled DLPFC field strength, not higher `%rMT`, tracked better depression improvement.

## Model definition

This paper does not present a trainable clinical predictor. The relevant modeling stack is a real-time neuronavigation E-field estimator paired with offline subject-specific finite-element simulation and downstream association analyses.

### Inputs
T1-weighted MRI, Freesurfer and CAT12 tissue segmentations, motor-cortex hotspot localization, resting motor threshold determination, structural/anatomical left DLPFC target definition, coil position/orientation, maximum stimulator output settings, and pre/post QIDS-SR16 symptom scores.

### Outputs
Estimated M1 and DLPFC cortical E-field strengths, subject-specific `%rMT` needed to achieve motor-equivalent DLPFC stimulation, precision comparisons between individualized dosing and the conventional `120% rMT` rule, and correlations between intensity metrics and depression improvement.

### Training objective (loss)
There is no trainable model with a conventional optimization loss. The real-time planning stack uses a spherical head model for immediate E-field estimation, while the offline analysis uses finite-element simulation and statistical association rather than predictive training.

### Architecture / parameterization
A two-layer biophysical modeling workflow: real-time E-field estimation inside the Nexstim neuronavigation system for prospective dose selection, followed by subject-specific SimNIBS finite-element modeling to estimate cortical field strength at M1 and DLPFC under different dosing rules.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Depression TMS dosing is still mostly expressed as a fixed percentage of resting motor threshold, even though that number is only a proxy for cortical stimulation and may translate poorly from M1 to DLPFC. The paper asks whether individualized E-field estimation gives a more meaningful dose measure and whether dose precision matters for clinical outcome.

### 2. What is the method?
Prospectively use real-time E-field guidance to set DLPFC stimulation so that estimated field strength matches the field recorded at M1 during motor-threshold determination, then retrospectively validate that choice with subject-specific finite-element simulations and compare it against the standard `120% rMT` rule.

### 3. What is the method motivation?
If anatomy varies a lot across patients, the same `%rMT` can produce meaningfully different cortical fields at the prefrontal target. A precision-dosing method should therefore estimate target field directly instead of assuming the motor-threshold percentage carries over cleanly.

### 4. What data does it use?
The analysis comes from a McLean Hospital IRB-approved randomized, double-blind, placebo-controlled trial in major depressive disorder. Thirty participants completed the single-day accelerated iTBS protocol, two were excluded for unusable MRI, and the final modeling sample was 28. All subjects had structural MRI, motor-threshold determination, subject-specific DLPFC targeting, and baseline plus one-week QIDS-SR16 scores.

### 5. How is it evaluated?
The paper evaluates three things. First, how much individualized motor-equivalent dosing varies across patients. Second, whether real-time E-field-guided dosing better approximates motor-equivalent DLPFC stimulation than the conventional `120% rMT` rule. Third, whether delivered `%rMT`, DLPFC-to-M1 field ratio, or absolute DLPFC field strength correlates with symptom improvement.

### 6. What are the main results?
Required DLPFC intensity to achieve motor-equivalent field strength ranged from 49.7% to 150.4% rMT, with more than half the sample requiring less than 100% rMT. Real-time E-field guidance reduced mean absolute deviation from the motor-equivalent target from 0.293 to 0.170 and cut root mean square error from 24.55 V/m to 12.75 V/m, which the paper reports as 48.1% better precision than the flat `120% rMT` rule. Delivered `%rMT` did not correlate with QIDS-SR16 improvement, but both the DLPFC-to-M1 field ratio and absolute DLPFC field strength showed negative correlations with improvement at `rho = -0.49, P = .008`, meaning lower modeled prefrontal field strength tracked better outcome.

### 7. What is actually novel?
The novelty is not merely adding another modeling flourish to TMS. It is prospectively using real-time E-field guidance during treatment planning, then tying that dosing precision to subject-specific finite-element validation and to a clinically provocative outcome signal that points away from "higher is better."

### 8. What are the strengths?
First, it measures the right thing more directly than most TMS dosing papers. Second, it compares a practical clinic-facing real-time method against a subject-specific FEM reference instead of arguing in the abstract. Third, it exposes a clinically actionable dissociation: `%rMT` is not outcome-relevant here, modeled field strength is. Fourth, the paper is honest about its limitations rather than pretending this already settles dosing.

### 9. What are the weaknesses, limitations, or red flags?
The clinical association analysis is retrospective and exploratory, not a randomized dose comparison. The sample is small. The DLPFC target is anatomical rather than connectivity-guided. The real-time spherical model and the offline FEM stack are still models rather than direct physiological measurements. The accelerated one-day protocol may also limit generalization to standard multiweek courses.

### 10. What challenges or open problems remain?
The field still needs prospective randomized testing of different E-field dosing targets, ideally something like 80%, 100%, and 120% of motor-equivalent field strength. It also needs to know whether the inverse intensity-outcome relationship survives larger samples, different depression subtypes, different target definitions, and standard multi-session courses.

### 11. What future work naturally follows?
Run a true randomized dosing trial, combine this framework with connectivity-based target selection, test whether lower-field benefits generalize beyond single-day accelerated iTBS, and compare real-time spherical planning against richer online modeling or physiological readouts that could ground truth field estimates more directly.

### 12. Why does this matter for cabbageland?
Because it sharpens a real intervention lever rather than decorating the problem. If depression TMS effectiveness depends on actual cortical field delivery rather than inherited `%rMT` convention, then a lot of current personalization work is optimizing the wrong variable. This is exactly the kind of paper that makes targeting, control, and adaptive neuromodulation logic less mushy.

### 13. What ideas are steal-worthy?
Treat dose as estimated field at target, not machine-output percentage. Separate geometry questions from dose questions instead of collapsing them into one targeting story. Use practical real-time approximations prospectively, then audit them offline with richer biophysical models. And stop assuming that the best clinical regime must be the highest tolerable intensity.

### 14. Final decision
Preserve. This is one of the better recent papers for making TMS dose legible as a precision-control variable rather than a hand-me-down heuristic. It is not definitive enough for clinical rule-making, but it is strong enough to change what future dosing papers should have to prove.
