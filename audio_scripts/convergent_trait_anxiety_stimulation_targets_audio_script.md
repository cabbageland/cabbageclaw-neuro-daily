Convergent Network Localization of Brain Stimulation Targets for Trait Anxiety.

This note was surfaced on July 25, 2026. The paper is by Shan Siddiqi, Julian Klingbeil, Ryan Webler, Ian Kratter, Daniel Blumberger, Michael Fox, Mark George, Jordan Grafman, Alvaro Pascual-Leone, Andrew Pines, Mark Richardson, Pratik Talati, Fidel Vila-Rodriguez, Jonathan Downar, Tamara Hershey, and Kevin Black. The published venue is the American Journal of Psychiatry, but the detailed inspection for this note used the full P M C hosted preprint text, whose P M C page explicitly says that the peer-reviewed journal version is now available.

Quick verdict. Highly relevant.

This is one of the stronger recent symptom-circuit papers in psychiatry because it does not ask us to trust one modality, one target, or one retrospective story. The paper makes several different natural experiments answer the same question and then checks whether they converge on one anxiety circuit. The confidence limit is not the core logic. The confidence limit is that the fully inspectable text in this run was the full preprint, not the full publisher version. Even so, the paper is strong enough to keep because it makes anxiety target discovery more causal and more clinically useful.

Here is the overview.

The paper tries to localize a brain-stimulation target for trait anxiety by forcing several natural experiments to converge on the same circuit instead of trusting any one alone. The authors combine scalp-based T M S datasets, lesion datasets, an individualized-connectivity T M S dataset, and subthalamic deep brain stimulation datasets across nine hundred and thirty-six people. They map the connectivity of sites that relieve anxiety or cause anxiety, control for depression, and ask whether the results converge.

They do. The combined circuit peaks in the right superior frontal gyrus and right lateral parietal lobe. Individualized T M S connectivity to that circuit predicts anxiety change. And S T N deep brain stimulation overlap with the circuit predicts anxiety worsening, even though the circuit was derived without subthalamic sites. The useful claim is not merely that anxiety has a network. The useful claim is that a trait-anxiety circuit can be localized in a way that is specific enough to propose new stimulation targets and to explain why some depression-oriented targets may worsen anxiety.

Now the model definition.

The paper does not center a trainable clinical model. The relevant machinery is multimodal circuit mapping plus out-of-sample validation.

The inputs are localized T M S sites, brain lesions, and S T N D B S sites, together with validated anxiety and depression measures, a normative functional connectome with one thousand people, and individualized resting-state functional M R I connectivity for the three D T M S cohort.

The outputs are dataset-level anxiety circuit maps, a convergent weighted-mean causal anxiety circuit, predicted anxiety change from T M S site connectivity to that circuit, and predicted anxiety outcomes from D B S site overlap with that circuit.

There is no trainable loss in the machine-learning sense. The analyses use voxel-wise partial correlations controlling for depression, spatial correlations between circuit maps, permutation tests against shuffled outcome-to-imaging assignments, and weighted averaging across datasets.

The architecture, if we want to use that word loosely, is a multimodal lesion-network and stimulation-site mapping framework. There are two scalp-target T M S datasets, two lesion datasets, one individualized-connectivity T M S dataset, and two S T N D B S validation datasets, all combined into a convergent causal anxiety circuit.

Now the key questions.

First, what problem is the paper trying to solve?

Brain stimulation can change anxiety, but the field still lacks a serious way to discover anxiety targets instead of recycling depression targets, fear-conditioning lore, or generic right-versus-left prefrontal habits. The paper asks whether a causal trait-anxiety circuit can be localized across several different natural experiments.

Second, what is the method?

The authors localize T M S sites, lesions, and D B S sites in standard space, estimate each site’s connectivity using a normative connectome or individualized resting-state functional M R I, and compare those connectivity maps with anxiety outcomes while controlling for depression. They then combine the resulting maps into a convergent anxiety circuit and validate it against independent individualized-connectivity T M S data and S T N D B S outcomes.

Third, what is the method motivation?

Any one modality has ugly confounders. Lesions are causal but opportunistic. T M S has intervention value but limited targeting precision. D B S reaches deep circuits but comes from different diseases and indications. If all of them converge on similar circuitry, the target-discovery claim becomes much harder to dismiss as one dataset’s accident.

Fourth, what data does it use?

Seven datasets totaling nine hundred and thirty-six individuals. These include two scalp-based D L P F C T M S datasets with one hundred and eleven combined participants, two lesion datasets with four hundred and fifty-one combined lesions, one individualized-connectivity T M S dataset with three hundred depression patients from the three D trial, and two Parkinson’s S T N D B S datasets totaling seventy-four patients for external validation.

Fifth, how is it evaluated?

The paper checks whether lesion and T M S maps resemble each other more than chance, whether the individualized-connectivity T M S map resembles the normative convergent map, whether T M S site connectivity to the circuit predicts anxiety change, whether D B S site overlap predicts anxiety change, and whether these effects are specific to trait rather than state anxiety.

Sixth, what are the main results?

The four initial T M S and lesion maps converge, with mean spatial cross-correlation around zero point five eight and permutation p equals zero point zero zero eight.

The combined T M S map and combined lesion map correlate at r equals zero point six eight with p equals zero point zero one.

In the individualized-connectivity T M S cohort, the derived map resembles the normative anxiety circuit at spatial r equals zero point three nine with p equals zero point zero two, and T M S site connectivity to the circuit predicts anxiety change at r equals zero point one four with p equals zero point zero two.

Negative connectivity to the anxiety circuit is associated with categorical anxiety worsening after T M S.

The convergent circuit peaks in the right superior frontal gyrus and right lateral parietal lobe, both surviving family-wise-error permutation testing.

Across two S T N D B S datasets, overlap with the anxiety circuit predicts anxiety worsening at r equals zero point three two with p equals zero point zero zero six.

Trait-versus-state specificity is also real. In the trait-anxiety analyses, lesion connectivity and D B S overlap track trait anxiety, not transient state anxiety, with key p values around zero point zero zero three.

Seventh, what is actually novel?

The novelty is not merely another anxiety network picture. The useful novelty is the convergence logic. The paper makes lesion mapping, scalp-target variability, individualized connectivity, and D B S outcomes answer the same question, then uses that convergence to nominate a new anxiety target instead of merely re-explaining an existing depression site.

Eighth, what are the strengths?

First, the paper is unusually strong on causal triangulation for a psychiatry target paper.

Second, it treats anxiety and depression as separable enough to test rather than as one blended symptom sludge.

Third, it checks trait versus state anxiety instead of assuming they are interchangeable.

Fourth, it turns anxiety worsening under stimulation into signal about the circuit instead of burying it as an annoying side effect.

Fifth, it benchmarks the circuit against alternative target-discovery strategies and reports that the convergent circuit outperforms those comparators.

Ninth, what are the weaknesses, limitations, or red flags?

This is still a natural-experiment synthesis rather than a prospective randomized trial of the newly proposed anxiety target.

The datasets are heterogeneous in imaging quality, site localization precision, diagnosis, and outcome measures.

Lesion analyses cannot use pre-lesion anxiety measurements and must assume that pre-lesion anxiety is randomly distributed with respect to lesion location.

The individualized-connectivity effect sizes are real but modest, and the paper itself notes that older low-resolution functional M R I in the three D trial may blunt personalization signal.

And again, my inspection used the full P M C preprint plus the peer-reviewed journal abstract and metadata, not the full publisher text.

Tenth, what challenges or open problems remain?

The obvious next challenge is whether directly stimulating the proposed right superior frontal target actually helps anxiety disorders prospectively, rather than only explaining existing variability. The field also still needs cleaner patient-level assignment rules, better anxiety side-effect monitoring in depression trials, and finer separation of rumination-like trait anxiety from more phasic fear or arousal states.

Eleventh, what future work naturally follows?

Prospective randomized trials targeting the right superior frontal and adjacent medial prefrontal circuit in primary anxiety disorders.

Patient-specific connectome-guided target optimization rather than one fixed target for everyone.

Studies that explicitly trade off antidepressant and anxiolytic circuit goals instead of assuming they point in the same direction.

And mechanistic work linking this trait-anxiety circuit to rumination, fear extinction, and other candidate processes rather than only symptom totals.

Twelfth, why does this matter for cabbageland?

Because it sharpens a recurring cabbageland problem. Symptom-specific target discovery needs something better than average depression outcomes plus retrospective storytelling. This paper suggests that anxiety may require its own target logic, may partly anti-align with some depression-optimized targets, and should be treated as a first-class circuit problem rather than as background mood noise.

Thirteenth, what ideas are steal-worthy?

Use convergence across lesions, T M S, and D B S as a target-discovery standard instead of trusting a single modality.

Treat anxiety worsening after stimulation as target information, not just safety paperwork.

Separate trait from state anxiety when building targets, biomarkers, or intervention logic.

And ask whether symptom-specific circuits for comorbid dimensions are anti-correlated, because that may explain why broad depression targeting so often disappoints.

Fourteenth, final decision.

Keep. This is one of the more convincing recent papers on how psychiatry brain-stimulation targets should be discovered. It does not yet prove that the proposed anxiety target works prospectively, but it makes the target-discovery standard meaningfully harder to fake.
