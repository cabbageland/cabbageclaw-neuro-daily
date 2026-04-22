# Model-based analysis of stop-signal data reveals robust neural and clinical correlates of evidence accumulation but not inhibition

## Basic info

* Title: Model-based analysis of stop-signal data reveals robust neural and clinical correlates of evidence accumulation but not inhibition
* Authors: not fully extracted from accessible source text
* Year: 2026
* Venue / source: Neuropsychopharmacology
* Link: https://www.nature.com/articles/s41386-026-02401-6
* Date surfaced: 2026-04-22
* Why selected in one sentence: It is a useful computational psychiatry correction because it argues that broad decision-efficiency variables explain more of the neural and clinical signal than the field’s usual inhibitory-control metric.

## Quick verdict

* Useful

This is not a stimulation paper, but it is good intervention-adjacent cleanup. The paper makes a simple and uncomfortable point: when you fit a richer mechanistic model to stop-signal performance, the clinically meaningful signal seems to live more in evidence accumulation and response-caution variables than in canonical inhibition speed. If that holds up, a lot of psychiatry’s inhibition language is partly measurement laziness.

## One-paragraph overview

Using the large longitudinal IMAGEN cohort, the authors apply the RDEX-ABCD model, a racing diffusion ex-Gaussian framework, to stop-signal task behavior at ages nineteen and twenty-three. They relate the resulting latent decision-process parameters to substance use with elastic-net regression and identify predictive functional-connectivity patterns with connectome-based predictive modeling. The central result is that conventional inhibition-focused parameters were weakly linked to substance use and brain connectivity, while more general decision-making variables such as evidence accumulation efficiency, response caution, and go-failure probability carried stronger neural and clinical signal. The paper matters because it challenges a default interpretation that poor stop-signal performance mainly means bad inhibition.

## Model definition

### Inputs
Stop-signal task performance data from the IMAGEN cohort, collected longitudinally at ages nineteen and twenty-three, along with whole-brain functional connectivity features derived from neuroimaging.

### Outputs
Latent computational parameters describing decision and stopping processes, plus predictions of substance-use outcomes and connectivity-based predictions of those latent parameters.

### Training objective (loss)
The paper uses the RDEX-ABCD cognitive process model to fit latent task parameters, then elastic-net regression and connectome-based predictive modeling for downstream prediction. The accessible text does not provide the full optimization details for each stage.

### Architecture / parameterization
A hybrid racing diffusion ex-Gaussian cognitive model for stop-signal behavior, combined with elastic-net regression and connectome-based predictive modeling over whole-brain connectivity.

## Key questions this summary must address

### 1. What problem is the paper trying to solve?
It is trying to determine which latent cognitive processes measured by stop-signal behavior actually relate to substance-use vulnerability and its neural correlates.

### 2. What is the method?
Fit a richer mechanistic stop-signal model to behavior in a large longitudinal cohort, then test how the resulting latent parameters relate to substance use and distributed brain connectivity.

### 3. What is the method motivation?
Standard stop-signal reaction time compresses several processes into one number. If the clinically meaningful signal comes from broader decision dynamics rather than pure inhibition, then the usual metric is conceptually misleading.

### 4. What data does it use?
The IMAGEN longitudinal youth cohort, with more than one thousand participants, stop-signal task data at ages nineteen and twenty-three, and associated neuroimaging-derived functional connectivity.

### 5. How is it evaluated?
By relating model parameters to substance-use outcomes via elastic-net regression and by identifying predictive whole-brain connectivity patterns with connectome-based predictive modeling.

### 6. What are the main results?
Parameters indexing inhibitory control had weak or no meaningful links to substance use and only weak connectivity associations. In contrast, evidence accumulation efficiency, decision threshold, and go-failure-related parameters were stronger predictors of cannabis and cigarette use and had clearer network correlates.

### 7. What is actually novel?
The novelty is the computational reframing. The paper shows that a more mechanistic decomposition of stop-signal behavior changes the apparent psychiatric story.

### 8. What are the strengths?
- Large longitudinal cohort.
- Clear mechanistic modeling upgrade over raw SSRT.
- Uses distributed connectivity rather than only local activation stories.
- Clinically useful negative result against overinterpreting inhibition measures.

### 9. What are the weaknesses, limitations, or red flags?
- Relevance to neuromodulation is indirect.
- Findings are tied to one task family and one cohort.
- The paper may still overinherit assumptions from the chosen cognitive model.
- Substance-use vulnerability is broader than the modeled task variables, so causal interpretation remains limited.

### 10. What challenges or open problems remain?
Testing whether the same latent-variable shift holds across other tasks, cohorts, and psychiatric phenotypes, and whether interventions can selectively move the more relevant evidence-accumulation variables.

### 11. What future work naturally follows?
Revisit cognitive-control intervention papers with richer latent-variable models, connect these variables to stimulation targets or network states, and test whether treatment effects track evidence accumulation more than classic inhibition metrics.

### 12. Why does this matter for cabbageland?
Because it sharpens the language around what an intervention might actually be trying to change. “Improving inhibition” may be too blunt if the real lever is broader decision efficiency or response caution.

### 13. What ideas are steal-worthy?
- Do not trust legacy behavioral summary metrics if richer latent models change the story.
- Use computational decompositions to clean up psychiatric mechanism claims.
- Link intervention goals to latent processes, not just task labels.
- Treat negative findings on canonical metrics as useful, not disappointing.

### 14. Final decision
Keep as adjacent infrastructure. It is not a treatment paper, but it improves how future psychiatry and neuromodulation claims should be framed.