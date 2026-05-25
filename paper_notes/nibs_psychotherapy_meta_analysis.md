# Noninvasive brain stimulation combined with evidence-based psychotherapy for psychiatric disorders: A meta-analysis of optimal implementation parameters

## Basic info

* Title: Noninvasive brain stimulation combined with evidence-based psychotherapy for psychiatric disorders: A meta-analysis of optimal implementation parameters
* Authors: Lysianne Beynel, Eva Wiener, Neil Baker, Ethan Greenstein, Andrada D. Neacsiu, Eudora Jones, Brian Gindoff, Sunday M. Francis, Cecilia Neige, Marine Mondino, Simon W. Davis, Bruce Luber, Sarah H. Lisanby, Zhi-De Deng
* Year: 2026
* Venue / source: medRxiv
* Link: https://doi.org/10.64898/2026.02.19.26346650
* Date surfaced: 2026-05-25
* Why selected in one sentence: It is one of the better attempts to turn “psychotherapy plus stimulation” from vague synergy talk into an implementation-parameter question.

## Quick verdict

* Useful

This is not a clean mechanistic paper, and the heterogeneity is substantial. But it is still worth keeping because it gives the combination-treatment literature a more disciplined shape. The useful residue is not just that combinations work a bit better overall. It is that the benefit appears concentrated in specific implementation choices, especially repetitive transcranial magnetic stimulation, non-concurrent scheduling, human-delivered psychotherapy, and cognitive behavioral therapy.

## One-paragraph overview

The paper systematically reviews randomized controlled trials comparing active noninvasive brain stimulation plus evidence-based psychotherapy against sham stimulation plus psychotherapy across psychiatric disorders. Twenty-eight trials and thirty-one treatment arms were included. Overall, the active combinations modestly outperformed sham combinations, but with substantial heterogeneity. Moderator analyses suggest that not all combinations are equally plausible: repetitive transcranial magnetic stimulation looked better than transcranial direct current stimulation, non-concurrent delivery looked better than concurrent delivery, and human-delivered psychotherapy looked better than computerized formats. That does not prove circuit-level synergy, but it does make the design space less mushy.

## Model definition

This paper does not contain a trainable clinical model. The relevant analytic machinery is meta-analytic effect estimation and moderator analysis.

### Inputs
Randomized trial-level data on diagnosis, stimulation modality, temporal relationship between stimulation and psychotherapy, psychotherapy type and delivery format, symptom outcomes, and protocol-integrity variables.

### Outputs
Pooled effect sizes for clinical improvement and moderator estimates for which implementation parameters are associated with larger or smaller combined-treatment effects.

### Training objective (loss)
The paper uses meta-analytic statistical estimation rather than a predictive learning objective. The accessible full text does not expose a machine-learning loss because none is central here.

### Architecture / parameterization
A systematic review and meta-analysis with subgroup and moderator analyses across randomized controlled trials.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
Many papers claim that psychotherapy and brain stimulation should be synergistic, but the actual implementation variables are all over the place. The paper asks which combination designs look most credible when randomized trials are pooled.

### 2. What is the method?
The authors searched multiple databases through February 2025, included randomized controlled trials comparing active stimulation-plus-psychotherapy against sham-plus-psychotherapy, and then meta-analyzed overall effects and key moderators.

### 3. What is the method motivation?
If psychotherapy engages plasticity-relevant circuits and stimulation can alter excitability or state, then timing, modality, and psychotherapy integrity should matter. The paper tries to extract that signal from a messy literature.

### 4. What data does it use?
Twenty-eight trials, thirty-one treatment arms, and one thousand five hundred six total participants across multiple psychiatric diagnoses and noninvasive stimulation modalities.

### 5. How is it evaluated?
By pooled symptom-improvement effect sizes and moderator analyses for stimulation modality, timing relative to psychotherapy, psychotherapy type, delivery format, diagnosis, and reporting of treatment integrity.

### 6. What are the main results?
The overall active-versus-sham combination effect was modest but significant. Repetitive transcranial magnetic stimulation showed a clearer benefit than transcranial direct current stimulation. Non-concurrent delivery, meaning before or after psychotherapy rather than during it, looked more effective. Human-delivered psychotherapy and cognitive behavioral therapy showed the clearest positive signals. Significant effects by diagnosis were strongest for anxiety disorders.

### 7. What is actually novel?
The novelty is the implementation focus. Instead of treating all combined protocols as the same intervention family, the paper asks which scheduling and delivery choices actually matter.

### 8. What are the strengths?
Randomized-trial-only inclusion, clinically relevant moderator questions, and an explicit focus on psychotherapy integrity rather than treating the psychological component as a black box.

### 9. What are the weaknesses, limitations, or red flags?
Heterogeneity is substantial. Many included trials are likely small. Treatment fidelity reporting is weak, which is a real problem for any psychotherapy-plus-device literature. And meta-analytic moderator results are only as trustworthy as the underlying trial quality and category definitions.

### 10. What challenges or open problems remain?
We still do not know whether the apparent benefit reflects true mechanistic complementarity, better patient engagement, expectancy differences, or a subset of well-designed protocols floating a noisy field. Timing logic also remains surprisingly unresolved.

### 11. What future work naturally follows?
Larger pre-registered trials that manipulate timing explicitly, preserve psychotherapy fidelity, and collect mechanistic markers rather than only symptom endpoints. Anxiety-focused and OCD-relevant combinations deserve especially careful follow-up.

### 12. Why does this matter for cabbageland?
Because combination-treatment rhetoric is everywhere, but usable design rules are rare. This paper helps narrow the plausible recipe for CBT-plus-stimulation work and highlights fidelity as a neglected variable rather than background paperwork.

### 13. What ideas are steal-worthy?
Treat timing as a first-class design variable. Track psychotherapy fidelity seriously. And stop assuming that concurrent delivery is automatically the most “state-dependent” or therefore the best.

### 14. Final decision
Keep, but as an implementation-framing paper rather than a mechanistic proof of synergy.
