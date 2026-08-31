# Methodological reliability and stability of individualized alpha frequencies: Implications for future precise neuromodulation

## Basic info

* Title: Methodological reliability and stability of individualized alpha frequencies: Implications for future precise neuromodulation
* Authors: Chuanliang Han, Zihua Jiang, Xiran Liang, Yingxin Gong, Shaojia Huang, Weiwen Xiang, Yuchen Lin, Xixi Zhao
* Year: 2026
* Venue / source: NeuroImage
* Link: https://doi.org/10.1016/j.neuroimage.2026.122173
* Date surfaced: 2026-08-31
* Why selected in one sentence: It audits whether individualized alpha frequency is stable enough to deserve precision-neuromodulation status instead of treating personalization as a free rhetorical upgrade.

## Quick verdict

* Highly relevant

This is a cautious preserve because it goes after a real upstream bottleneck in personalized stimulation: whether the supposed target frequency is actually reliable. This note is based on **abstract-only inspection after 10 full-text acquisition attempts** across the PubMed landing page, PubMed formatted route, DOI landing page, direct ScienceDirect HTML route, direct ScienceDirect PDF route, Elsevier API route, Crossref metadata route, JoVE visualize route, ResearchGate mirror route, and author-page search surfaces. Metadata routes marked the paper open access, but the article body remained blocked or challenge-protected in this environment, so confidence is good on the high-level design and headline result and capped on estimator detail and statistics.

## One-paragraph overview

The paper asks a simple but uncomfortable question for personalized neuromodulation: is individualized alpha frequency actually a stable personal coordinate, or is it partly a measurement artifact of state and method? Using resting-state EEG from 67 healthy individuals under eyes-open and eyes-closed conditions, plus 238 longitudinal sessions from 21 people recorded monthly over up to 16 months, the authors compare multiple alpha-frequency estimation methods. The abstract reports a clear pattern: alpha peak estimation is unstable under eyes-open conditions but robust under eyes-closed conditions, cross-method agreement is high when a prominent alpha peak exists, and both alpha frequency and alpha power remain stable over extended periods once that condition is satisfied. The value is not another claim that personalization works. The value is a quality gate for when personalization even deserves the name.

## Model definition

This paper does not present a learned predictive model. The relevant machinery is a signal-estimation and reliability-comparison pipeline across recording conditions and repeated sessions.

### Inputs
Resting-state EEG recorded under eyes-open and eyes-closed conditions from 67 healthy individuals, plus 238 longitudinal resting-state EEG sessions from 21 individuals collected roughly monthly over up to 16 months, together with multiple individualized-alpha estimation methods.

### Outputs
Individualized alpha-frequency estimates, comparisons of estimator consistency across methods, condition-dependent reliability of alpha-peak estimation, and longitudinal stability measures for alpha frequency and alpha power.

### Training objective (loss)
There is no trainable loss exposed in the accessible abstract. The practical objective is to estimate alpha frequency robustly and test its reliability across conditions, methods, and time.

### Architecture / parameterization
A resting-state EEG methods study comparing multiple individualized-alpha estimation approaches under eyes-open versus eyes-closed conditions, plus longitudinal repeated-measures stability analysis.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to solve a quiet validity problem in precision neuromodulation. Many tACS and some TMS studies talk as if individualized alpha frequency is a clean personal target, but that assumption depends on whether the alpha peak is actually measurable and stable enough to function as a control variable.

### 2. What is the method?
The authors record resting-state EEG from healthy participants under eyes-open and eyes-closed conditions, then estimate alpha frequency with multiple methods. They also follow a longitudinal subset monthly and ask whether the estimated alpha frequency and alpha power stay stable over extended periods.

### 3. What is the method motivation?
If the target frequency itself is unstable, then "personalized frequency" may just be decorated measurement noise. Before arguing about which individualized frequency to stimulate, the field should establish when the parameter is reliable enough to deserve personalization language at all.

### 4. What data does it use?
The abstract reports resting-state EEG from 67 healthy individuals in eyes-open and eyes-closed conditions, plus 238 sessions from 21 individuals in a longitudinal monthly design averaging 11.3 sessions per participant over a mean duration of 10.3 months and up to 16 months.

### 5. How is it evaluated?
It is evaluated by comparing alpha-peak estimation under eyes-open versus eyes-closed conditions, comparing estimates across multiple methods, and measuring longitudinal stability of alpha frequency and alpha power across repeated sessions.

### 6. What are the main results?
The accessible abstract reports four main results. First, alpha peak estimation is unstable under eyes-open conditions. Second, it is robust under eyes-closed conditions. Third, when participants have a prominent alpha peak, different estimation methods produce highly consistent frequency estimates. Fourth, both alpha frequency and alpha power remain remarkably stable over extended periods in the longitudinal sample.

### 7. What is actually novel?
The useful novelty is not another individualized-stimulation claim. It is a reliability audit of the parameter that personalized-frequency neuromodulation keeps treating as already solved. That is more valuable than one more positive protocol paper built on unexamined target selection.

### 8. What are the strengths?
It asks the right humiliating question for a fashionable personalization story. The design compares eyes-open and eyes-closed states directly, includes multiple estimation methods rather than a single favored pipeline, and adds a meaningful longitudinal component instead of pretending one resting snapshot settles the issue.

### 9. What are the weaknesses, limitations, or red flags?
This is still an abstract-only preserve despite 10 full-text acquisition attempts, so the exact estimator families, reliability coefficients, prominence thresholds, and statistical handling are hidden. The sample is healthy rather than clinical. And the study does not itself test whether the more reliable estimation conditions translate into better stimulation outcomes.

### 10. What challenges or open problems remain?
The main open problems are whether the same stability pattern holds in clinical populations, how much individualized alpha drifts within a day or across symptom states, whether weak-peak participants should be excluded or handled with uncertainty-aware targeting, and whether stable eyes-closed estimates actually outperform simpler fixed-frequency baselines in intervention trials.

### 11. What future work naturally follows?
The obvious next steps are to test the same reliability logic in depression and other patient groups, compare baseline eyes-closed individualized-alpha targeting against fixed-frequency and online-adaptive strategies, and formalize peak-quality thresholds or confidence intervals before calling a frequency "personalized."

### 12. Why does this matter for cabbageland?
Because cabbageland cares about intervention logic that survives contact with measurement reality. If the supposedly individualized frequency is condition-fragile, then the real engineering problem is not choosing a prettier number. It is proving that the number exists robustly enough to guide control.

### 13. What ideas are steal-worthy?
Treat target-estimation quality as a hard prerequisite for personalization claims. Prefer eyes-closed acquisition and explicit peak-prominence checks when alpha frequency is the control variable. And when the peak is weak or state-dependent, consider uncertainty-aware or online-adaptive targeting instead of forcing a single baseline frequency to impersonate precision.

### 14. Final decision
Preserve, with explicit confidence limits. Even from abstract-only inspection after 10 full-text acquisition attempts, this looks like one of the more useful recent methods papers for keeping personalized-frequency neuromodulation honest. The access limits keep confidence capped, but the framing and the headline result are strong enough to save.
