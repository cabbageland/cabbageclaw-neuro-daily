# Individualized Connectivity-Guided Versus Conventional Targeting of Accelerated Theta-Burst Stimulation in Depression: A Randomized, Double-Blind, Parallel-Design Trial

## Basic info

* Title: Individualized Connectivity-Guided Versus Conventional Targeting of Accelerated Theta-Burst Stimulation in Depression: A Randomized, Double-Blind, Parallel-Design Trial
* Authors: M. Li, Z. Wu, X. Lu, A. Zalesky, X. Cheng, Y. Zhang, R. F. H. Cash, F. Jin, S. Jia, Y. Xiao, G. Zhong, X. Zhang, W. Yue, Z. Yang, T. Jiang, H. Yan
* Year: 2026
* Venue / source: The American Journal of Psychiatry
* Link: https://doi.org/10.1176/appi.ajp.20251084
* Date surfaced: 2026-08-12
* Why selected in one sentence: It is a rare direct clinical comparison of 5-centimeter, functional-connectivity-guided, and structural-connectivity-guided accelerated iTBS, and it suggests the early precision win may belong to structural guidance rather than default FC hype.

## Quick verdict

* Highly relevant

This is an abstract-only preserve after **10 full-text acquisition attempts**, so confidence is lower than for a normal full-text keep. It is still worth preserving because head-to-head comparisons of competing precision-targeting logics are rare, and the accessible result is sharper than the field's usual connectivity-guided victory speech. The useful surprise is that structural-connectivity guidance gets the cleaner early antidepressant win, while functional-connectivity guidance looks slower and less dominant than branding would predict.

## One-paragraph overview

This single-center, randomized, double-blind, three-arm trial asked whether individualized sgACC-based targeting improves antidepressant response over the conventional 5-centimeter rule in accelerated intermittent theta-burst stimulation for depression. Adults ages 18 to 65 years with major depressive disorder or bipolar II depression and at least one antidepressant failure were assigned to receive 20 iTBS sessions over 2 weeks using robotic neuronavigation with one of three target rules: 5-centimeter targeting, resting-state functional-connectivity targeting defined by negative connectivity with the subgenual anterior cingulate cortex, or structural-connectivity targeting defined by probabilistic tractography to the sgACC. In the modified intention-to-treat sample of 119 participants, structural-connectivity guidance beat the 5-centimeter arm on the primary week-2 HAM-D percentage-reduction endpoint, and by week 6 both structural and functional guidance beat the 5-centimeter arm. By week 12, the between-group differences were no longer significant. That makes the paper useful because it turns "precision targeting" into a more discriminating question about which connectivity logic, if any, actually changes outcome timing and magnitude.

## Model definition

This paper does not present a trainable clinical predictor. The relevant computational machinery is the target-selection stack: resting-state functional-connectivity mapping, diffusion-informed probabilistic tractography, and robotic neuronavigation inside a three-arm randomized treatment comparison.

### Inputs
Structural and resting-state neuroimaging used to derive sgACC-related functional-connectivity and structural-connectivity target sites, participant diagnosis and treatment-resistance status, robotic neuronavigation coordinates, and longitudinal depression ratings.

### Outputs
Target coordinates under three competing targeting rules, delivered accelerated iTBS sessions, and longitudinal percentage reduction in 17-item HAM-D scores plus secondary symptom, cognitive, and safety outcomes.

### Training objective (loss)
There is no trainable model with a conventional optimization loss in the accessible text. The paper uses predefined connectivity-derived targeting rules and downstream randomized-group statistical comparisons.

### Architecture / parameterization
A single-center, randomized, double-blind, parallel three-arm accelerated iTBS trial comparing 5-centimeter targeting, sgACC-negative resting-state functional-connectivity targeting, and sgACC-oriented structural-connectivity targeting with robotic neuronavigation.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
The paper is trying to test whether "precision TMS" means anything more than prettier imaging rhetoric. The real problem is that the standard left DLPFC 5-centimeter rule ignores anatomy and connectivity variation, but many individualized targeting papers then smuggle in only one favored precision logic and never compare it directly against plausible alternatives.

### 2. What is the method?
The method is a three-arm randomized comparison inside the same accelerated iTBS protocol. Participants received 20 sessions over 2 weeks using robotic neuronavigation, with targets chosen either by the 5-centimeter rule, by resting-state functional connectivity showing negative coupling to the sgACC, or by structural connectivity to the sgACC from probabilistic tractography.

### 3. What is the method motivation?
If depression-relevant circuit engagement actually matters, then a target chosen from person-specific connectivity should outperform a crude scalp geometry rule. The stronger motivation, though, is more specific: different connectivity notions may not be equivalent, so the paper asks whether functional and structural guidance buy the same kind of benefit or different ones.

### 4. What data does it use?
The accessible abstract says the trial enrolled adults ages 18 to 65 years with major depressive disorder or bipolar II depression and at least one antidepressant failure between February 2023 and March 2025. One hundred twenty-three were randomized, and 119 entered modified intention-to-treat analysis, split across the 5-centimeter, structural-connectivity-guided, and functional-connectivity-guided arms.

### 5. How is it evaluated?
The primary endpoint is percentage reduction in 17-item HAM-D score at week 2. Secondary outcomes include HAM-D percentage reduction at weeks 6 and 12, response or remission, self-reported symptoms, cognitive-battery performance, and adverse events. The accessible text reports least-squares mean differences and effect sizes between arms.

### 6. What are the main results?
- Structural-connectivity-guided iTBS beat the 5-centimeter arm on the primary week-2 endpoint, with a least-squares mean difference of 8.79 percentage points and Cohen's `d = 0.70`.
- At week 6, both structural-connectivity-guided and functional-connectivity-guided targeting beat the 5-centimeter arm, with the structural arm again numerically stronger (`d = 1.03` versus `d = 0.75`).
- By week 12, the between-group differences were no longer significant.
- Adverse events were comparable across groups, and the abstract reports no seizures or mania.

### 7. What is actually novel?
The main novelty is not merely individualized targeting. It is the direct comparison of **two different individualized connectivity logics** against the same conventional baseline inside one accelerated protocol. That matters because it exposes that structural guidance may carry a different and possibly earlier signal than the field's default functional-connectivity story.

### 8. What are the strengths?
- The trial is randomized, double-blind, and parallel rather than a loose retrospective targeting comparison.
- All three groups share the same accelerated treatment scaffold, which helps isolate target-selection logic from schedule theatrics.
- The comparison is clinically useful because it pits precision methods against an actual conventional baseline rather than against narrative vagueness.
- The inclusion of both major depressive disorder and bipolar II depression makes the cohort more intervention-relevant than a hyper-curated single-diagnosis niche, even if it also raises subgroup questions.

### 9. What are the weaknesses, limitations, or red flags?
- This is an **abstract-only** preserve after 10 full-text attempts, so the paper's real reliability ceiling is lower than usual.
- It is single-center, which limits robustness against site-specific workflow and patient-selection effects.
- The accessible text does not expose the exact imaging preprocessing, tractography constraints, statistical-model specification, or response/remission tables.
- The week-12 washout of between-group significance raises a durability question.
- Because all arms receive active iTBS, the paper compares targeting logics rather than demonstrating absolute efficacy over sham.

### 10. What challenges or open problems remain?
The obvious open problems are whether the structural-versus-functional difference replicates across sites, whether certain subgroups preferentially benefit from one targeting logic, how durable the acute gains are, and whether the imaging burden is justified when deployed in routine care rather than tightly managed trial settings.

### 11. What future work naturally follows?
Run a larger multisite replication with explicit subgroup analyses, open the target-derivation pipeline to reproducibility scrutiny, compare durability-optimized continuation strategies after acute acceleration, and test whether target logic should be chosen adaptively based on phenotype, anatomy, or circuit readout rather than treated as one-size-fits-all.

### 12. Why does this matter for cabbageland?
Because a lot of "precision neuromodulation" talk still treats functional-connectivity targeting as a sacred object rather than a testable design choice. This paper matters because it forces a better question: if you are going to personalize, which connectivity geometry actually earns the complexity tax, and on what timescale?

### 13. What ideas are steal-worthy?
- Compare competing precision logics directly instead of benchmarking one favored personalization story against a straw-man baseline.
- Treat structural and functional target definitions as potentially dissociable intervention hypotheses, not interchangeable signs of sophistication.
- Read acute and medium-term benefit separately; the best early target may not be the same as the best durability target.
- Make baseline choice explicit, because beating a folk geometric rule is informative but not the end of the personalization argument.

### 14. Final decision
Preserve, but with confidence discounted because this is an abstract-only note after 10 full-text access attempts. The trial is still strategically valuable because direct randomized targeting comparisons are scarce, and the accessible result complicates the lazy assumption that sgACC-negative functional connectivity is automatically the precision winner.
