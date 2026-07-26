Proximity to an S G C D L P F C Individualized Functional Target and outcomes in large r T M S clinical trials for treatment-resistant depression.

This note was surfaced on July 26, 2026. The paper is by Elizabeth Gregory, Shan Siddiqi, Michael Fox, Daniel Blumberger, Jonathan Downar, Zafiris Daskalakis, Katharine Dunlop, and Fidel Vila-Rodriguez. The fully inspectable text in this run was the twenty-seven-page bioRxiv preprint. A peer-reviewed version later appeared in Brain Stimulation.

Quick verdict. Highly relevant.

This is one of the more useful recent negative papers in precision neuromodulation because it attacks a cherished claim with a dataset large enough to be annoying. The paper does not prove individualized targeting is worthless. But it does show that when clinicians are already using a strong neuronavigated group target, simple proximity to a patient-specific connectivity target does not obviously explain who gets better.

Here is the overview.

The paper asks a blunt question. If individualized functional targets inside left D L P F C really matter for depression T M S, should patients do better when the clinically applied target lands closer to those individualized targets?

To test that, the authors retrospectively analyze five hundred and one patients from the THREE-D and CARTBIND depression trials. Everyone received four to six weeks of left D L P F C stimulation targeted with neuronavigation to the same optimized group coordinate. From each person’s baseline resting-state functional M R I, the authors compute two individualized functional targets. One is based on subgenual cingulate connectivity. The other is based on the broader causal depression circuit.

Most individualized targets turn out to be already close to the actual group target. And that closeness does not predict percent H R S D change, response, remission, or target-connectivity effects. The useful claim is not that personalization is impossible. The useful claim is that the field has not yet earned the right to treat individualized connectivity targeting as an established clinical advantage.

Now the model definition.

This paper does not center a trainable predictive model. It centers an individualized target-localization pipeline plus outcome association tests.

The inputs are baseline T one and ten-minute resting-state functional M R I scans, a left D L P F C search mask, an S G C seedmap, a causal depression circuit map, neuronavigated treatment-target coordinates, stimulation protocol metadata, and baseline and end-of-treatment H R S D scores.

The outputs are two individualized target coordinates per patient, one S G C-derived and one causal-circuit-derived, plus the Euclidean distance from those targets to the clinically applied group target, target-connectivity estimates, and associations with antidepressant outcome.

There is no machine-learning loss in the ordinary sense. The core procedure selects clusters of the most anticorrelated or correlated voxels within D L P F C and then tests whether distance to those selected targets relates to symptom change.

The architecture, loosely speaking, is a seedmap-based individualized targeting pipeline. The authors construct S G C-weighted and causal-circuit-weighted timeseries, compute voxelwise connectivity within a D L P F C search region, threshold to the top zero point five percent of candidate voxels, take the largest cluster, and use its center of gravity as the individualized target.

Now the key questions.

First, what problem is the paper trying to solve?

Precision-T M S work keeps claiming that patient-specific connectivity targets inside left D L P F C should improve antidepressant outcomes, but much of that claim still rests on small studies, indirect comparisons, or mixed-up effects of targeting, protocol, and patient selection. This paper asks whether proximity to individualized connectivity-derived targets actually predicts outcome inside two large clinical-trial datasets where stimulation was already neuronavigated to a strong group target.

Second, what is the method?

The authors retrospectively analyze the TWO cohorts. THREE-D contributes three hundred and thirty-seven patients and CARTBIND contributes one hundred and sixty-four. Everyone receives four to six weeks of left D L P F C stimulation at one hundred and twenty percent of resting motor threshold. Using baseline resting-state scans, the authors compute individualized targets from subgenual-cingulate logic and from causal-depression-circuit logic, then test whether shorter distance from the applied target to either individualized target predicts better outcome.

Third, what is the method motivation?

If individualized connectivity targeting is genuinely clinically important, then the patients whose delivered target sits closer to their own optimal cortical entry point should tend to do better. The paper also asks whether a broader circuit-derived target works better than the classic subgenual-cingulate story.

Fourth, what data does it use?

The analytic sample includes five hundred and one patients after excluding twenty-four for high framewise displacement. Baseline resting-state scans are ten minutes long with three hundred volumes, acquired on three-tesla scanners with single-echo protocols and relatively large voxels. Clinical outcome is H R S D change, plus response and remission.

Fifth, how is it evaluated?

The main tests are Spearman correlations between individualized-target distance and percent H R S D change, plus t tests comparing responders versus non-responders and remitters versus non-remitters. The authors also test target functional connectivity itself, vary cluster thresholds, try an alternate searchlight localization method, and probe whether scanner site, cohort, signal quality, or stimulation protocol explains the null.

Sixth, what are the main results?

Most individualized targets are already close to the actual group target. Median distance is twelve point eight millimeters for the S G C-derived target and thirteen point eight millimeters for the causal-circuit-derived target. Seventy-four percent of S G C targets and sixty-nine percent of causal-circuit targets fall within twenty millimeters of the stimulated site.

Distance does not predict outcome. H R S D change is not significantly correlated with S G C-target distance, where rho equals zero point zero two and p equals zero point six, or causal-circuit-target distance, where rho equals zero point zero five and p equals zero point three.

There is also no meaningful responder or remitter separation by distance. Group-target functional connectivity itself is similarly unhelpful, with no significant correlation to H R S D change for either approach.

The two individualized-target frameworks also collapse toward each other more than their branding suggests. Their whole-brain connectivity maps are strongly inversely related, and the individualized targets themselves sit close together for most patients, with median separation around seven point nine millimeters.

Sensitivity analyses do not rescue the story. Changing thresholding, localization method, signal-quality handling, cohort, site, or treatment assignment does not create a positive proximity effect.

Seventh, what is actually novel?

The novelty is not another pretty subgenual-cingulate targeting narrative. The useful novelty is the scale and the willingness to publish a clinically inconvenient null. The paper stress-tests two individualized-targeting frameworks inside large neuronavigated trial datasets and finds that the expected proximity advantage basically does not show up.

Eighth, what are the strengths?

The sample is much larger than the small retrospective studies that helped build the personalization story.

The analysis directly compares two target definitions instead of pretending one biomarker is obviously correct.

Because everyone was already treated with neuronavigation to a strong group target, the test is harder and more clinically relevant than comparing an individualized method against a sloppy scalp heuristic.

And the authors run enough sensitivity analyses that the null cannot be dismissed as one arbitrary threshold choice.

Ninth, what are the weaknesses, limitations, or red flags?

This is retrospective, not a prospective randomized head-to-head test of individualized versus group targeting.

The imaging quality is a serious limitation. The scans are single-echo, only ten minutes long, and use fairly large voxels, which is a bad combination for stable individualized target estimation in D L P F C and especially ugly around subgenual signal.

The group target may already have been close enough to most individualized targets that there was not much usable variation left to detect a proximity effect.

The accessible full text in this run was the bioRxiv preprint rather than the full peer-reviewed publisher article.

And the paper does not solve electric-field variability prospectively. It mainly argues that field spread and less focal coil geometry may blur any targeting advantage.

Tenth, what challenges or open problems remain?

The main unresolved question is whether individualized targeting truly fails, or whether current clinical functional M R I quality is simply too noisy and too short to estimate useful patient-level targets reliably. The field also still needs to separate targeting effects from protocol intensity, plasticity differences, coil focality, and symptom heterogeneity.

Eleventh, what future work naturally follows?

Run a prospective randomized trial that compares a high-quality neuronavigated group target against individualized targets derived from better imaging, ideally with longer and possibly multi-echo resting-state scans.

Integrate electric-field modeling prospectively rather than treating it as after-the-fact decoration.

Test whether individualized targeting matters only in specific depression biotypes or symptom dimensions rather than in average major-depression outcomes.

And compare targeting gains against other individualization levers, especially plasticity enhancement and dosing logic.

Twelfth, why does this matter for cabbageland?

Because precision-neuromodulation claims keep getting louder than their calibration. This paper is valuable exactly because it says a decent group target may already buy most of the practical benefit that personalized-connectivity marketing likes to attribute to itself. That does not end the targeting question, but it forces the field to prove that personalization adds something real on top of competent neuronavigation and not just on top of weak comparators.

Thirteenth, what ideas are steal-worthy?

Benchmark individualized-target methods against a genuinely good group target, not just against Beam F three or other weak heuristics.

Treat scan reliability as part of the causal question, because a personalization method that needs unrealistic imaging quality is not yet clinically ready.

And use large nulls as design guidance. If most individualized targets cluster inside the same T M S electric field, then the next gain may come from symptom-specific circuits, e-field shaping, or plasticity control rather than another prettier coordinate map.

Fourteenth, final decision.

Keep. This is not a final verdict against individualized targeting, but it is a strong and badly needed calibration paper. If future precision-T M S claims cannot outperform this null on better data and in prospective designs, they are still mostly branding.
