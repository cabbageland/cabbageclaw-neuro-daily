Closed-loop and personalized targeting
Current synthesis
The good neuromodulation papers are converging on a stricter standard than the field used to tolerate.
If a paper claims precision stimulation, it should specify:
Target — what circuit, tract, node, or state variable is being targeted?
Readout — what signal says the target is engaged or the patient state changed?
Controller / selection logic — how does the intervention decide where, when, or how to stimulate?
Validation — what evidence shows the stimulation changed the intended signal or circuit, not just a downstream clinical score?
Pattern from recent papers
Stronger pattern
Personalized target discovery tied to symptom-linked physiology.
Explicit biomarker or state-estimation logic.
Evidence of target engagement beyond anatomy.
Closed-loop or adaptive rules that are actually implemented, not just proposed.
Willingness to show what the controller is optimizing.
Clear separation between targeting and state tracking as linked but distinct problems.
Mechanism papers that identify directional parameter effects instead of reporting generic “modulation.”
Weaker pattern
“Network-guided” targeting that never demonstrates network engagement.
“AI-guided” or “precision” branding with no real control logic.
Small open-label studies with huge claims and no serious comparator.
Reliance on average symptom change without state specificity or subgroup reasoning.
Cross-treatment network stories that infer causality from retrospective convergence without direct perturbation evidence.
Working judgment
Right now, invasive work is still ahead on mechanistic credibility because it can directly sense and perturb the relevant circuit. Noninvasive work is improving, especially when it uses online optimization or person-specific field/network modeling, but it still often lacks durable state readouts and sufficiently strong behavioral endpoints.
A useful distinction is emerging:
Targeting papers tell you where you are probably stimulating.
Biomarker papers tell you what state variable may matter.
Controller papers tell you how stimulation is adjusted online.
The best future work will have all three. Most current papers have only one, occasionally two.
Updated heuristic from recent papers
Prefer papers that make the following chain explicit:
symptom or state -> biomarker/readout -> target selection -> stimulation -> measured circuit change -> clinical or behavioral effect
And add one more filter:
Can the paper tell you whether failure came from the wrong target, the wrong state variable, or the wrong control rule?
If not, the paper is usually less useful than the title suggests.
Recent examples informing this heuristic
OCD invasive mapping paper: strong because it links symptom state, physiology, target search, and later implantation.
BNST-NAc depression DBS biomarker paper: strong because it gives a candidate state variable and shows it changes with stimulation state.
Precision TMS modeling paper: useful because it attacks the hidden assumption that a nominal cortical coordinate equals a stable network target across people.
Closed-loop tACS-fMRI paper: useful because it makes the control objective explicit, even if the setup is still operationally heavy.
tFUS corticothalamic mechanism paper: adjacent but valuable because it maps parameter regime to directional circuit effect.
