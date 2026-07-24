Subthreshold violations of trajectory predictions are sensitive to T M S of cerebellum Crus one and two.

This note was surfaced on July 24, 2026. The paper is by Ellen Joos, Camille Scherer, Philippe Isope, Jack Foucher, and Anne Giersch, and it appeared in NeuroImage Reports.

Quick verdict. Useful.

This is a mechanistic perturbation paper worth preserving because it does not merely decorate itself with predictive-processing language. It creates a subthreshold trajectory violation, records electroencephalography, and perturbs right cerebellar Crus one and two with sham-controlled intermittent theta-burst stimulation. The main caution is that the T M S story is modest and order-dependent. The strongest effect is a neural modulation in perturbed trials, not a robust overall behavioral intervention effect. I inspected the accessible full text through P M C, so the caveats here come from the paper itself rather than from abstract fog.

One-paragraph overview.

The paper studies a visual collision illusion in which two briefly contacting moving squares can be perceived as separated by a gap. The authors ask whether the illusion depends on millisecond-scale trajectory prediction and sensory checking. To stress that claim, they introduce a subtle trajectory violation less than sixty milliseconds before the collision, measure electroencephalography, and apply neuronavigated intermittent theta-burst stimulation to right cerebellar Crus one and two in a sham-versus-verum crossover. The trajectory perturbation reliably reduces the illusion rate and increases a late positive event-related potential over C P 4. Verum cerebellar stimulation modulates that signal on perturbed trials, but the effect appears only when verum is delivered in the second session. So the useful result is not that cerebellar T M S cleanly changes conscious perception. The useful result is that subthreshold trajectory checking looks real, cerebellar involvement remains plausible, and the neural signal is more convincing than the behavioral intervention claim.

Now the model definition.

Inputs.

Visual trials in which two squares move toward collision with either unperturbed or subtly perturbed trajectories, contact durations of seventeen, thirty-three, or two hundred milliseconds, sham versus verum cerebellar intermittent theta-burst stimulation, pre-versus-post intervention timing, and electroencephalography recordings.

Outputs.

Behavioral reports of whether the squares touched or did not touch, illusion rates across conditions, and event-related potential amplitudes, especially the late positive signal over C P 4 during perturbed trials.

Training objective, or loss.

There is no trainable predictive model in the machine-learning sense. The paper uses Bayesian statistical analyses with minimally informative priors to estimate condition effects, odds ratios, credible intervals, and intervention interactions.

Architecture and parameterization.

A within-subject psychophysics and electroencephalography experiment with M R I guided cerebellar intermittent theta-burst stimulation in sham-versus-verum crossover order, analyzed with Bayesian models of behavioral and electrophysiological effects rather than with a learned classifier or decoder.

Now the key questions.

First, what problem is the paper trying to solve?

The paper tries to determine whether a visual collision illusion depends on automatic millisecond-scale trajectory prediction and whether cerebellar circuitry contributes to detecting tiny violations of that predicted motion.

Second, what is the method?

The authors recruit healthy adults, run a visual task where two squares move toward each other, insert subthreshold trajectory violations shortly before collision, record electroencephalography, and compare sham versus verum intermittent theta-burst stimulation over right cerebellar Crus one and two in a crossover design.

Third, what is the method motivation?

If the illusion relies on predictive checking rather than passive sensory registration, then a tiny trajectory irregularity should disrupt the illusion, and cerebellar perturbation should modulate the neural signature of that disruption.

Fourth, what data does it use?

The study recruited twenty-four healthy young adults. After exclusions for task compliance, abnormal perception profiles, and acquisition issues, the main behavioral and electroencephalography analyses were conducted on nineteen participants, with sixteen participants contributing to the behavioral and event-related-potential correlation analyses.

Fifth, how is it evaluated?

Evaluation is done by comparing illusion rates and event-related-potential amplitudes across non-perturbed versus perturbed trials, pre-versus-post intervention time points, sham versus verum stimulation, and session order. The paper reports Bayesian effect sizes, odds ratios, credible intervals, and posterior probabilities.

Sixth, what are the main results?

The subthreshold trajectory perturbation reliably reduces the illusion rate relative to non-perturbed trials.

Perturbed trials produce higher late positive C P 4 amplitudes than non-perturbed trials, in the rough window from point one five seconds to two seconds after contact.

There is no convincing overall behavioral effect of verum cerebellar stimulation on perturbed trials.

On perturbed trials, electroencephalography amplitudes increase after verum T M S relative to before verum T M S, and the intervention-by-time interaction is strong.

That electroencephalography increase appears only when verum T M S is applied in the second session, which makes the intervention result order-dependent and therefore less clean than it first sounds.

Seventh, what is actually novel?

The novelty is not just another cerebellar T M S study or another predictive-processing argument. The useful novelty is combining a subthreshold sensory prediction violation, electroencephalography measurement, and sham-controlled cerebellar intermittent theta-burst stimulation inside the same millisecond-scale task.

Eighth, what are the strengths?

The paper actually perturbs the claimed predictive process instead of merely inferring it from behavior.

Full task logic, T M S targeting, and result caveats are visible in accessible full text.

The cerebellar stimulation is M R I guided and neuronavigated rather than hand-waved.

The authors separate behavioral and neural effects instead of forcing a fake unified success story.

Bayesian analysis is a reasonable choice for a small exploratory dataset and makes the uncertainty visible.

Ninth, what are the weaknesses, limitations, or red flags?

The sample is small, with nineteen analyzed participants in the main datasets.

The T M S effect is stronger in event-related potentials than in behavior, which limits intervention-level conclusions.

The clearest intervention effect is order-dependent, appearing only when verum T M S is delivered in the second session.

This is a healthy-young-adult psychophysics study, not a clinical perturbation paper.

The task is narrow and somewhat idiosyncratic, so generalization to broader predictive-processing or neuromodulation settings is unearned.

Tenth, what challenges or open problems remain?

The biggest open problems are replicating the order-sensitive event-related-potential effect in a larger sample, clarifying whether the cerebellum is specifically necessary rather than merely part of a broader circuit, and showing whether stronger or differently timed stimulation changes behavior more convincingly.

Eleventh, what future work naturally follows?

Larger preregistered replications, active-control stimulation sites, online or phase-specific perturbation rather than a brief offline intermittent theta-burst block, patient-population extensions for disorders with altered predictive processing, and integration with whole-brain perturbation models would all follow naturally.

Twelfth, why does this matter for cabbageland?

Because it is a good example of how to make a mechanistic claim earn its keep. If you want to talk about prediction, state checking, or cerebellar timing in intervention logic, this paper shows a better standard: perturb the stream, perturb the putative predictor, record the neural consequence, and do not pretend the behavioral story is cleaner than it is.

Thirteenth, what ideas are steal-worthy?

Use subthreshold task violations to assay whether a proposed predictive computation is actually live.

Treat neural sensitivity and behavioral sensitivity as separable readouts instead of demanding they move together immediately.

Use cerebellar timing machinery as a candidate component in rapid sensory regularity checking, but require perturbational evidence before saying so loudly.

Prefer papers that leave visible where the mechanism stops being demonstrated and starts being conjectured.

Fourteenth, final decision.

Preserve. This is not a must-read or a clinically decisive paper, but it is a useful mechanistic note because it actually stresses the prediction claim and surfaces a cerebellum-sensitive event-related-potential effect without pretending the behavioral intervention result is already settled.
