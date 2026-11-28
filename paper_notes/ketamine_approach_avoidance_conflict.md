# Ketamine promotes strategic and efficient approach-avoidance conflict resolution

## Basic info

* Title: Ketamine promotes strategic and efficient approach-avoidance conflict resolution
* Authors: Stefan Vestring; Samuel Pfauth; Viktoria Galuba; Gabriel Burgos Kim; Dominik R. Bach; Felix Mülsch; Feres Mocayar Marón; Katharina Domschke; Dominique Endres; Claus Normann; Juan Carlos Baldermann
* Year: 2026
* Venue / source: Communications Medicine; published November 20, 2026
* Link: https://www.nature.com/articles/s43856-026-01998-5
* Date surfaced: 2026-11-28
* Why selected in one sentence: It separates approach frequency, sensitivity to potential loss, action timing, and earned reward after ketamine, supplying a testable behavioral bridge for intervention research without actually establishing plasticity or psychotherapy synergy.

## Quick verdict

* Highly relevant

Keep for experimental design and computational-psychiatry framing, not as proof of an antidepressant mechanism. The randomized ketamine–lorazepam crossover finds different behavioral profiles despite both drugs increasing approach; the fixed-first unmedicated baseline makes those baseline contrasts less secure. Motor acceleration is part of the result and a competing explanation for improved reward collection, not an inconvenient nuisance to omit.

## One-paragraph overview

Thirty-four healthy adults completed a virtual-predator task without medication and then after intranasal racemic ketamine or oral lorazepam, with the two drug visits randomized and counterbalanced. Participants could collect rewards but risk losing tokens while outside a safe location; learned threat probability and explicitly displayed loss magnitude varied independently. Ketamine increased earned tokens, increased sensitivity to explicit losses, reduced the decline in approach with increasing threat, and shortened approach and withdrawal latencies. Lorazepam also increased approach but less selectively. This is an informative behavioral perturbation experiment. It does not measure neural plasticity, identify a circuit, establish durable clinical benefit, or test ketamine combined with CBT, exposure, or hypnosis.

## Model definition

### Inputs

Trial-level drug condition, standardized threat probability, standardized loss magnitude, their interactions, and participant identity. Additional analyses examine drug-session order and repetition. The task contains 24 training trials and 240 test trials per visit.

### Outputs

Explanatory estimates of approach probability, net token gain, approach latency, and withdrawal latency. These are fitted behavioral outcome models, not a prospective treatment-response biomarker or stimulation policy.

### Training objective (loss)

The authors specify a logit-link generalized linear mixed-effects model for binary approach and linear mixed-effects models for continuous outcomes. Bernoulli-logit and Gaussian likelihoods are the corresponding model-family objectives; the main text does not specify the exact optimizer or maximum-likelihood versus restricted-likelihood settings. Do not reinterpret this as reinforcement-learning parameter estimation. Analysis code was not audited.

### Architecture / parameterization

Condition × threat × loss regressions with participant random intercepts and reported random slopes. Control is the initial reference; models are rerun with ketamine as reference for active-drug contrasts. There is a reproducibility ambiguity: the manuscript names MATLAB `fitglm` for its GLMMs, although random-effects modeling normally requires a different function. Confirm the actual implementation before reusing coefficients or reproducing the random-effects structure.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?

Does ketamine merely increase approach, or alter the balance between threat, potential loss, movement timing, and successful reward collection? That distinction matters because indiscriminate disinhibition and useful engagement can produce similar approach rates but different outcomes.

### 2. What is the method?

Three visits separated by seven days: unmedicated control first, then 50 mg intranasal R-/S-ketamine and 1 mg oral lorazepam in randomized, counterbalanced order. Behavioral testing occurred 90–150 minutes after administration. Drug assignment was concealed until the session; behavioral collection personnel were blinded, but participants and physicians were not. The virtual task independently varies threat probability and loss magnitude, permitting separate condition interactions.

### 3. What is the method motivation?

Reward gain is an outcome; approach rate is only one contributor. Explicit loss cues and learned probabilistic threats can influence decisions differently. Including latency also exposes an important alternative: moving back to safety faster changes the actual exposure to danger even if risk preferences are unchanged.

### 4. What data does it use?

All 34 healthy adults completed every condition; ages 22–31, 24 female and 10 male. Participants had no lifetime neurological/psychiatric disorder or regular medication use and underwent extensive medical screening. This is a selected healthy sample, not treatment-resistant depression, adolescence, or a psychotherapy cohort. Paired-associative-stimulation/tDCS assessments occurred after the behavioral tasks and are reserved for a separate report; they do not establish a physiological mediator here.

### 5. How is it evaluated?

Within-person contrasts and condition interactions in mixed-effects regressions. The main text states a Bonferroni threshold of p < .0125 across four outcomes. Post-hoc checks examine correct button direction, drug order, and drug-condition versus repetition models. There is no held-out prediction test, clinical response endpoint, long-term follow-up, or independent replication cohort. Some displayed interactions, including p = .023, do not meet the stated corrected threshold and should not be promoted as corrected-significant findings.

### 6. What are the main results?

- **Token gain:** 57% higher after ketamine than control and 33% higher than lorazepam; respectively p < .001 and p = .009. These are relative task-performance differences, not symptom-response rates.
- **Approach:** both drugs increased approach versus control; the active-drug difference in average approach was not significant, p = .145. Ketamine's more useful distinction was its interaction profile: greater explicit-loss sensitivity and reduced threat-related decline in approach.
- **Timing:** ketamine shortened approach latency versus control and lorazepam, p < .001 and p = .009; withdrawal was faster than both, p < .001. Less time outside safety can itself improve reward yield.
- **Checks:** correct-direction rates did not significantly differ. Adding drug order preserved the gain differences; drug condition fit better than repetition alone, ΔAIC = 19. Those analyses support but do not eliminate the fixed-first baseline confound.

### 7. What is actually novel?

The useful contribution is a subacute, active-comparator behavioral dissociation: similar average approach increases conceal different loss/threat sensitivity and reward efficiency. The paper does not newly establish ketamine's molecular mechanism, prove an optimal decision policy, or identify a therapeutic learning window. “Value-guided” is an interpretation of the behavioral interactions, not a fitted latent value-learning mechanism.

### 8. What are the strengths?

Within-subject randomized active-drug comparison; complete follow-through; independent task manipulation of two decision variables; multiple behavioral endpoints including timing; explicit consideration of order and practice. Lorazepam helps distinguish increased approach from increased task performance, although it is not a neutral placebo.

### 9. What are the weaknesses, limitations, or red flags?

- **Causal identification:** unmedicated baseline always precedes both drugs. Counterbalancing the drug visits cannot fully identify a drug-versus-baseline effect independently of practice. No credible placebo condition was included.
- **Subjective state:** participants/physicians were unblinded; mood, dissociation, and anxiety ratings were not collected systematically. The presumed post-dissociative window is not a demonstrated state-matched comparison.
- **Mechanism:** no reported neural, plasticity, or circuit mediator. Faster movement mechanically reduces threat exposure; no yoked-exposure manipulation or mediation analysis isolates cognitive reweighting from that benefit.
- **Statistics:** 34 people, not thousands of independent subjects despite many trials. Random slopes are not validated patient stratification. The named fitting function and multiple-testing language merit implementation-level checking.
- **Generality:** one subacute time point while drug remains active, narrow healthy cohort, no clinical treatment, psychotherapy, repeated dosing, or durable outcome. Anatomical targeting, neural controllability, and clinical benefit are not evaluated.

### 10. What challenges or open problems remain?

Does the profile persist after clearance, generalize to patients with excessive avoidance, and predict useful learning rather than merely performance during drug action? Are inferred threat beliefs, explicit value sensitivity, and motor speed separately identifiable? Would reduced threat weighting become harmful in environments where probabilistic warnings are reliable?

### 11. What future work naturally follows?

Fully counterbalance control and active sessions with a credible blinding strategy; collect subjective-state and pharmacokinetic measures; manipulate or yoke time at risk to dissociate movement from decision effects. Add a generative choice/latency model with recovery checks. In a patient study, randomize psychotherapy presence or timing and test durable learning and symptom outcomes. Task improvement alone is not evidence that therapy should be delivered in this specific window.

### 12. Why does this matter for cabbageland?

It supplies an unusually concrete intermediate assay for interventional psychiatry: test whether an intervention changes how people engage with threat and reward, rather than calling all engagement “plasticity.” It also cautions against treating a combined behavioral–physiological study program as if its unreported physiology already explains the behavioral result.

### 13. What ideas are steal-worthy?

- Independently vary uncertainty and explicit consequence, then score actual utility as well as engagement.
- Include action timing whenever the environment makes exposure duration consequential.
- For ketamine/CBT or neuromodulation/exposure combinations, separate acute performance, retained learning, and clinical benefit with different endpoints.
- Compare subgroup and individual effects only after establishing model identifiability and reliability; random-effect estimates alone do not justify personalized treatment.

### 14. Final decision

Preserve as **Highly relevant** experimental-design and computational-psychiatry material, with clinical inference sharply bounded. It earns a behavioral intervention result, not causal plasticity, precision targeting, or combination-treatment efficacy.

Access record: publisher main full text inspected through Methods, Results, Discussion, and figure captions. Supplementary PDFs/tables and the registry were not independently checked; analysis code and the [shared Figshare data](https://doi.org/10.6084/m9.figshare.33176237) were not audited. Numerical claims above are main-text/caption reports, not a reanalysis.
