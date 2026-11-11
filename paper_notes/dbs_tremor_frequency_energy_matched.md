# No Additional Benefit of 185 Hz Versus 130 Hz at Equivalent Energy in Deep Brain Stimulation for Tremor: A Randomized Prospective Clinical Trial

## Basic info

* Title: No Additional Benefit of 185 Hz Versus 130 Hz at Equivalent Energy in Deep Brain Stimulation for Tremor: A Randomized Prospective Clinical Trial
* Authors: Christina van der Linden; Peer Trapp; Till A. Dembek; Charlotte Schedlich-Teufer; Gregor A. Brandt; Hannah Jergas; Gereon R. Fink; Veerle Visser-Vandewalle; Michael T. Barbe; Jan Niklas Petry-Schmelzer
* Year: 2026
* Venue / source: Movement Disorders Clinical Practice; published online November 2, 2026
* Link: https://doi.org/10.1002/mdc3.70886
* Date surfaced: 2026-11-11
* Why selected in one sentence: It tests whether a common DBS frequency escalation buys more acute tremor suppression once delivered electrical energy is matched, providing a concrete baseline-design lesson for intervention optimization.

## Quick verdict

* Highly relevant

Preserve for programming evidence and experimental design, not as proof that frequency is biologically irrelevant. Randomized frequency order, blinded examination, objective accelerometry, and energy-matched comparisons make this more informative than an uncontrolled parameter sweep. The absence of consistent superiority is credible within the tested acute setting; post-hoc equivalence with a wide margin does not establish universal interchangeability.

## One-paragraph overview

Adults already receiving DBS for essential tremor (ET; VIM/posterior subthalamic area) or Parkinson's disease (PD; STN) underwent two acute stimulation series, at 130 and 185 Hz, in randomized order. Contacts and pulse width stayed fixed while current increased through predefined steps designed to permit both equal-energy and equal-current comparisons. Across the analyzed 29 ET and 30 PD hemispheres, energy tracked tremor improvement, but the higher frequency did not consistently improve tremor at matched energy. This narrows an actionable programming question without explaining the cellular mechanism, demonstrating long-term benefit, or validating an adaptive controller.

## Model definition

### Inputs

The principal statistical model receives frequency, within-subject-centered total electrical energy delivered (TEED), their interaction, and hemisphere identity. Outcomes come from repeated accelerometric tremor measurements relative to stimulation-off baseline. TEED is computed from contact currents, frequency, pulse width, and measured contact impedances. Imaging supports lead reconstruction, not a learned target-selection model.

### Outputs

Estimated frequency and energy associations with relative total tremor improvement, interaction effects, confidence intervals, and significance tests, fitted separately for ET and PD. Additional analyses compare paired settings, clinical subscores, side-effect thresholds, and bootstrapped median differences. There is no trained symptom decoder, online state estimator, policy, or individualized response predictor.

### Training objective (loss)

The analysis uses a linear mixed-effects regression: `tremor improvement ~ frequency * centered TEED + (1 | patient-hemisphere)`. The accessible main methods do not specify the fitting criterion or ML versus REML, so an exact likelihood/loss cannot be reported. Exploratory paired Wilcoxon tests use Benjamini-Hochberg correction; exploratory equivalence assesses whether 90% bootstrap confidence intervals from 10,000 resamples lie within ±20 percentage points of relative tremor improvement. None of these is prospective policy optimization.

### Architecture / parameterization

A fixed-effects frequency/energy interaction with a random intercept for each investigated hemisphere; separate disease-cohort fits. A deterministic energy calculation uses `TEED = sum(I_contact^2 × frequency × pulse width × impedance_contact)`. A previously validated accelerometric tremor score is the primary measurement, not a newly learned biomarker.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Clinicians sometimes increase DBS frequency beyond 130 Hz for tremor, but holding current constant also increases delivered energy. Does 185 Hz outperform 130 Hz when that resource difference is controlled?

### 2. What is the method?

Single-center, prospective, double-blind, within-participant comparison with balanced-block randomization of frequency-series order. Pulse width is fixed at 60 microseconds; contact choice is held constant within testing. Current rises through predefined steps until persistent side effects or the protocol limit. Tremor is recorded during standardized rest, provocation, posture, movement, and drawing tasks; accelerometry supplies the primary endpoint and blinded ratings provide complementary assessments.

### 3. What is the method motivation?

Frequency is not an independent dose knob. At fixed current, pulse width, and impedance, 185 versus 130 Hz increases modeled TEED by about 42%. Conversely, energy matching requires lower current at 185 Hz: approximately `sqrt(130/185) = 0.838` times the 130-Hz current when other factors are equal. That makes a clinically meaningful resource-matched comparison, but it does not hold spatial recruitment or charge per pulse constant.

### 4. What data does it use?

Eighteen ET participants were enrolled; one was excluded from the primary accelerometry analysis, leaving 29 analyzed hemispheres. Twenty-five PD participants supplied 30 hemispheres. These are not 59 independent patients. Testing occurred April 2023–August 2024 in adults with DBS implanted for at least three months and substantial stimulation-off tremor. PD assessments followed at least 12 hours without dopaminergic medication. Most recordings used finger accelerometry; wrist measurements substituted for three hemispheres after finger-sensor failure.

### 5. How is it evaluated?

Primary endpoint: between-frequency difference in accelerometric total tremor improvement relative to baseline, at matched TEED. Mixed-effects analysis spans repeated energy steps; exploratory analyses compare individual equal-energy and equal-current steps. Secondary measures include tremor components, clinical ratings, rigidity/finger tapping in PD, maximum tolerated benefit, and side-effect thresholds. After amplitude adjustments the protocol waits at least 60 seconds; frequency series are separated by 10–30 minutes until tremor returns to baseline. This is an acute physiological/programming experiment, not chronic real-world outcome evaluation.

### 6. What are the main results?

- Frequency effects in the primary mixed models were not significant: ET estimate −0.040, 95% CI −0.092 to 0.012, p=0.135; PD −0.026, CI −0.083 to 0.030, p=0.359. Energy effects were positive in both cohorts; frequency-by-energy interactions were not significant. These are model coefficients, not a claim that every individual responds identically.
- Pairwise accelerometry showed no consistent total-tremor advantage for 185 Hz. Some equal-current differences in PD rigidity/finger tapping did not persist under energy matching; those are not the primary tremor endpoint.
- Exploratory equivalence was broadly compatible with the ±20-percentage-point margin, but the highest ET energy step had only four observations and its confidence interval extended beyond the margin toward 185 Hz. Do not turn the abstract's equivalence language into an exception-free result.
- Persistent side effects began at lower current with 185 Hz: ET medians 2.5 versus 3.0 mA; PD 3.5 versus 4.5 mA. Energy thresholds did not differ significantly. Lower current thresholds are not evidence of improved energy efficiency or safety.

### 7. What is actually novel?

The useful contribution is a prospective, blinded, energy-controlled comparison of two common frequencies across two tremor-target cohorts. It is stronger evidence for a programming baseline than a new network-control theory or discovery of the mechanism of tremor suppression.

### 8. What are the strengths?

- Randomized frequency order and objective primary measurement reduce expectation and order confounding.
- Equal-energy and equal-current comparisons expose the dependence of interpretation on the comparison budget.
- Repeated dose-response sampling is more informative than comparing two arbitrarily optimized settings.
- Explicit tolerability measurements prevent efficacy from being considered without the usable stimulation range.
- Full main text and primary tables are openly accessible through PMC, allowing scrutiny beyond the headline.

### 9. What are the weaknesses, limitations, or red flags?

- Originally powered for superiority, not equivalence; the ±20-point exploratory margin can hide clinically consequential differences.
- The matched-energy intervention changes frequency and current together. TEED equality does not ensure equal neural recruitment, network engagement, battery drain, or long-term tissue effects.
- TEED itself includes frequency, introducing partial collinearity. A nonsignificant frequency term cannot prove the absence of frequency-specific biology.
- Hemisphere-level random intercepts handle repeated measurements within a hemisphere. My additional concern: the stated model does not explicitly add a patient-level effect linking bilateral hemispheres, so residual dependence may remain.
- Fixed ascending current order, possible incomplete washout, active contralateral stimulation, and untested blinding success leave design limitations.
- Single center, modest cohorts, sparse high-energy observations, and near-ceiling suppression constrain heterogeneity inference. No reliably frequency-preferring subgroup was identified; that is not proof none exists.
- Only 130 and 185 Hz, acute tremor, and these targets/cohorts were tested. Chronic habituation, other symptom domains, developmental populations, and psychiatric DBS are not covered.

### 10. What challenges or open problems remain?

Distinguish temporal pattern effects from energy and recruitment geometry, determine whether acute similarity survives chronic use, and find reproducible individual exceptions without post-hoc subgroup fishing. Objective tremor measurement is useful feedback, but this experiment does not establish a causal neural-state biomarker or explain the network mechanism.

### 11. What future work naturally follows?

Run a prespecified chronic crossover study with justified noninferiority/equivalence bounds, patient-level clustering, home tremor measurements, functional outcomes, and adverse-effect assessment. Compare policies at matched energy and matched tolerability while recording actual device consumption. Mechanistic work should measure circuit engagement rather than infer axonal saturation from a behavioral plateau.

### 12. Why does this matter for cabbageland?

It supplies a concrete fairness test for adaptive stimulation and parameter optimization: a clever policy must beat a well-programmed conventional baseline under explicit resource and tolerability constraints. The clinical result also checks theoretical control narratives—improving a modeled control cost is not the same as improving the symptom at a comparable biological dose.

### 13. What ideas are steal-worthy?

- Report a response surface over frequency and current, then compare its equal-energy and equal-tolerability contours.
- Separate physical dose, actuator geometry, measured neural state, and behavioral endpoint in both experiments and models.
- Include matched-resource conventional stimulation before crediting an adaptive policy with temporal specificity.
- Preserve individual trajectories and cluster uncertainty by patient, especially when bilateral targets contribute observations.

### 14. Final decision

**Preserve as highly relevant clinical/translational evidence and a baseline-design reference.** Inspection used primary PMC full-text XML via Europe PMC: abstract, main methods, results, Tables 1 and associated figure captions, discussion, and limitations. The complete supplementary files, raw data, and analysis implementation were not independently acquired or reproduced. The axonal-overwriting/saturation explanation in the discussion remains interpretation, not a mechanism measured by this trial. Open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13728422/.
