# Toward Individualized Deep Brain Stimulation: A Stereoelectroencephalography-Based Workflow for Neurostimulation Target Identification

## Basic info

* Title: Toward Individualized Deep Brain Stimulation: A Stereoelectroencephalography-Based Workflow for Neurostimulation Target Identification
* Authors: Jeremy Saal, Kelly Kadlec, Anusha B. Allawala, Lucille Johnston, Ryan B. Leriche, Ritwik Vatsyayan, Yiyuan Han, Audrey Kist, Tommaso Di Ianni, Heather E. Dawes, Edward F. Chang, A. Moses Lee, Andrew D. Krystal, Khaled Moussawi, Prasad Shirvalkar, Kristin K. Sellers
* Year: 2026
* Venue / source: Neuromodulation: Journal of the International Neuromodulation Society
* Link: https://pubmed.ncbi.nlm.nih.gov/41389045/
* Date surfaced: 2026-06-16
* Why selected in one sentence: It turns individualized DBS from vague precision rhetoric into a sham-aware sEEG testing workflow with explicit power logic for choosing chronic implant targets.

## Quick verdict

* Highly relevant

This is one of the better recent workflow papers in interventional psychiatry because it asks a neglected operational question instead of advertising another favorite target. The useful contribution is not a miraculous efficacy result. It is a testing protocol: use inpatient sEEG, sham variability, effect-size estimates, tolerability gates, and trial-count planning to decide which stimulation sites deserve chronic implantation. The main caveat is that the sample is still small and mixed across indications, and the whole framework assumes that rapid symptom improvement during acute testing is a meaningful guide to longer-term benefit.

## One-paragraph overview

The paper describes a statistics-driven workflow for using temporary inpatient stereoelectroencephalography, or sEEG, to identify personalized deep brain stimulation targets before chronic implantation. Fourteen participants across major depressive disorder, chronic pain, and obsessive-compulsive disorder underwent about ten days of inpatient monitoring with symptom provocation, sham trials, and stimulation testing across candidate sites. The authors formalize this into a decision tree that prioritizes safety and tolerability first, then uses sham-driven estimates of response variability to determine how many trials are needed per site. The headline result is not that they found one magic target. It is that sham trial variability predicts stimulation-response variability well enough to power the search. In their data, about ten sham trials were needed to estimate baseline variability robustly, and for effect sizes of about 1.1 or larger, around ten trials per stimulation site should usually be enough for a reasonably powered within-person decision.

## Model definition

This paper does not present a trainable predictive model. The relevant machinery is a clinical testing workflow plus statistical power estimation.

### Inputs
Symptom-provocation trials, sham and active stimulation trials delivered through temporary sEEG contacts, indication-specific visual analog symptom ratings, anatomical localization of implanted contacts, and stimulation safety and tolerability information.

### Outputs
Candidate therapeutic stimulation sites for chronic DBS implantation, effect-size estimates for each site, sham-variability estimates, and recommended trial counts needed to test a site with usable statistical power.

### Training objective (loss)
There is no learnable loss. The central quantitative logic is power analysis and effect-size estimation based on within-participant symptom change and sham-trial variability.

### Architecture / parameterization
A staged sEEG-to-DBS clinical workflow with a stimulation testing decision tree, fixed-parameter early site screening, sham-controlled repeated trials, and post hoc power calculations to guide target selection.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
DBS for complex neuropsychiatric disorders still has a personalization problem. Chronic devices can only cover a few sites, revision surgeries are costly and risky, and a lot of target choice still depends on prior anatomical fashion more than on direct patient-specific evidence.

### 2. What is the method?
Temporarily implant sEEG leads across candidate disease-network regions, perform symptom provocation when needed, run safety and tolerability testing, compare sham and active stimulation trials, estimate effect sizes site by site, and use those statistics to decide which site merits chronic implantation.

### 3. What is the method motivation?
If neuropsychiatric symptoms emerge from partly individualized network dysfunction, then target choice should be tested in the actual patient rather than inherited from group-average folklore. But that testing only becomes useful if it is rigorous enough to resist side-effect unblinding, noisy symptom ratings, and underpowered enthusiasm.

### 4. What data does it use?
Fourteen participants tested over about ten inpatient days: six with major depressive disorder, six with chronic pain, and two with obsessive-compulsive disorder. Symptom ratings were indication-specific visual analog scores collected before, during, and after sham or active stimulation.

### 5. How is it evaluated?
By estimating stimulation-induced symptom change effect sizes across candidate sites, testing whether sham response variability predicts stimulation-response variability, bootstrapping how many sham trials are needed for stable variability estimates, and translating those estimates into trial-count recommendations per stimulation site.

### 6. What are the main results?
- Stimulation effect sizes ranged from strongly negative to strongly positive, which is exactly why formal site testing matters.
- Sham-trial standard deviation predicted stimulation-response variability well, with leave-one-out cross-validated linear regression R squared of 0.67 and permutation p less than 0.001.
- Roughly ten sham trials were needed to estimate sham variability robustly.
- For effect sizes of about 1.1 or larger, roughly ten trials per stimulation site were enough for a reasonably powered paired comparison.
- The resulting decision tree gives practical rules for safety testing, rejecting poorly tolerated sites, and narrowing the search space before chronic implantation.

### 7. What is actually novel?
The novelty is not another target atlas. The useful novelty is converting individualized DBS search into a sham-aware, power-aware workflow that tries to make target selection statistically legible instead of surgically intuitive.

### 8. What are the strengths?
- Directly relevant to depression, OCD, and broader interventional psychiatry target-selection logic.
- Uses sham variability as an operational planning signal rather than as a mere control nuisance.
- Admits that inpatient target search is a biased and underpowered process unless formalized.
- Bridges anatomy, symptom provocation, and trial design rather than pretending any one of those is enough.
- Full text was accessible through the PMC-hosted preprint, so the summary is based on direct article inspection rather than metadata alone.

### 9. What are the weaknesses, limitations, or red flags?
- The sample is small and mixes three indications with different symptom dynamics.
- The framework assumes that acute symptom improvement during sEEG testing is a meaningful proxy for chronic stimulation benefit, which may miss slower-acting targets.
- Visual analog symptom ratings are useful but noisy, and symptom provocation can drift across days.
- Untested stimulation parameters at a rejected site could still have worked better than the explored settings.
- The workflow is likely hard to scale if psychiatric DBS expands beyond highly specialized centers.

### 10. What challenges or open problems remain?
The main unresolved question is long-horizon validity: do the acute sites this workflow selects actually outperform standard implantation choices after blinded chronic follow-up? Another open problem is how to combine this kind of patient-specific testing with tractography, state estimation, and symptom-domain modeling without exploding the search space.

### 11. What future work naturally follows?
Prospective validation against long-term chronic outcomes, integration with tractography and volume-of-activated-tissue models, explicit modeling of state-dependent stimulation effects, and more efficient search strategies such as Bayesian optimization over site and parameter space.

### 12. Why does this matter for cabbageland?
Because this repo keeps asking for intervention logic that survives contact with actual testing. This paper says personalization should not mean "we liked a circuit story." It should mean "we tested candidate sites in this person, measured sham variability, and had enough trials to justify the choice."

### 13. What ideas are steal-worthy?
- Use sham-trial variability early to plan how much evidence a site needs.
- Hold some stimulation parameters fixed initially so the target-location question does not dissolve into a giant underpowered search.
- Treat safety, tolerability, and blinding risk as part of target-selection logic rather than as afterthoughts.
- Use acute-response workflows as a way to generate patient-specific priors for later closed-loop or tract-informed optimization.

### 14. Final decision
Keep. This is not a triumphalist efficacy paper, which is part of why it is valuable. It gives individualized DBS a more serious experimental grammar and makes target selection look more like evidence generation than prestige neurosurgery.
