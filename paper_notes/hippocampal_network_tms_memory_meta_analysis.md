# A meta-analysis suggests that TMS targeting the hippocampal network selectively improves episodic memory

## Basic info

* Title: A meta-analysis suggests that TMS targeting the hippocampal network selectively improves episodic memory
* Authors: Jonathan M. Voss, Samuel J. Tompary, and colleagues
* Year: 2026
* Venue / source: eLife
* Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC13175575/
* Date surfaced: 2026-05-15
* Why selected in one sentence: It is one of the clearest recent tests of whether connectivity-guided noninvasive stimulation produces domain-selective cognitive effects rather than generic uplift.

## Quick verdict

* Highly relevant

This is better than the average memory-stimulation meta-analysis because it asks a sharper question than whether TMS "works." It asks whether hippocampal-network targeting yields selective effects on episodic memory, and whether those effects depend on task structure in a way that fits the proposed circuit. That makes it much more useful for targeting logic.

## One-paragraph overview

This meta-analysis reviews hippocampal indirectly targeted stimulation, meaning repetitive transcranial magnetic stimulation delivered to parieto-occipital cortical sites selected for connectivity with hippocampal networks. Across 38 analyzable studies, 1,009 participants, and 253 effects, the pooled effect on episodic memory was moderate and clearly positive, while effects on non-memory cognitive tasks were near zero. Effects were stronger for recollection-oriented memory tests than for recognition formats, and stronger when stimulation occurred before the task rather than between encoding and retrieval. The paper does not prove every hippocampal-network TMS protocol is mechanistically clean, but it does suggest that a connectivity-guided target class can produce relatively selective behavioral effects when the assay matches hippocampal-network function.

## Model definition

### Inputs
Study-level and effect-level metadata from HITS experiments, including task type, timing of stimulation, targeting method, stimulation parameters, population type, and reported memory or non-memory outcomes.

### Outputs
Pooled standardized effect sizes for episodic-memory and non-memory outcomes, plus moderator estimates for factors such as recollection versus recognition task format and timing of stimulation.

### Training objective (loss)
This is not a predictive model in the usual machine-learning sense. The core estimation objective is meta-regression over Hedges' g effect sizes, with cross-validated lasso used for moderator selection.

### Architecture / parameterization
A statistical meta-analysis and meta-regression framework with random effects by study and lasso-based factor selection for candidate moderators.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to determine whether hippocampal-network-targeted TMS reliably improves episodic memory and whether any benefit is selective enough to support a real network-based intervention claim.

### 2. What is the method?
Systematically review HITS studies, transform outcomes into standardized effect sizes, estimate pooled effects for episodic-memory and non-memory tasks, and test moderators tied to task format and stimulation design.

### 3. What is the method motivation?
If hippocampal-network targeting is meaningful, effects should look selective for hippocampal-network-dependent behavior rather than like diffuse cognitive activation.

### 4. What data does it use?
Thirty-eight studies included in the meta-analysis, spanning healthy and clinical populations, with 1,009 subjects and 253 statistical comparisons.

### 5. How is it evaluated?
Through pooled Hedges' g estimates, sensitivity analyses with outlier removal, direct comparison of memory versus non-memory domains, and moderator analyses on study design factors.

### 6. What are the main results?
The pooled episodic-memory effect was Hedges' g of 0.44 with a strong confidence interval above zero. Non-memory effects were near zero. Recollection-format tasks showed larger gains than recognition tasks, and pre-task stimulation outperformed post-encoding stimulation.

### 7. What is actually novel?
The useful novelty is the selectivity claim: the paper argues that connectivity-guided hippocampal-network stimulation affects the cognitive domain and task format most plausibly tied to that network.

### 8. What are the strengths?
- Much stronger synthesis than isolated positive memory-TMS papers.
- Explicitly compares episodic-memory effects against non-memory outcomes.
- Moderator analyses map onto plausible mechanism questions.
- Includes both healthy and clinical studies.

### 9. What are the weaknesses, limitations, or red flags?
- Meta-analysis inherits the heterogeneity and quality limits of the source literature.
- A moderate pooled effect can hide design fragility.
- Network targeting is mostly indirect and cortical, so hippocampal engagement is inferred rather than directly measured in most studies.
- Publication bias and small-study effects remain a standing concern even when sensitivity analyses look decent.

### 10. What challenges or open problems remain?
Prospective head-to-head comparisons of targeting strategies, better verification of actual network engagement, durability of effects, and stronger clinical trials in memory-impaired populations.

### 11. What future work naturally follows?
Use mechanistically matched memory tasks in intervention trials, pair stimulation with direct network-state measurement, and test whether individualized connectivity targeting improves effect size or reliability.

### 12. Why does this matter for cabbageland?
Because it is a rare case where network-guided noninvasive stimulation looks selectively tied to a function rather than globally activating cognition. That is exactly the sort of paper that helps separate real targeting logic from loose connectome branding.

### 13. What ideas are steal-worthy?
- Judge network-targeted stimulation by task selectivity, not just average improvement.
- Use recollection-heavy assays when the mechanism claim is hippocampal-network function.
- Treat timing relative to encoding and retrieval as part of the mechanism, not just protocol detail.
- Always compare against non-target cognitive domains when claiming specificity.

### 14. Final decision
Keep. This is a strong synthesis note for network-guided TMS because it argues for selective function-level effects, not just another modest average cognitive benefit.
