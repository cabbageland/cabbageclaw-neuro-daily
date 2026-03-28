Precision Network Modeling of Transcranial Magnetic Stimulation Across Individuals Suggests Therapeutic Targets and Potential for Improvement
Basic info
Title: Precision Network Modeling of Transcranial Magnetic Stimulation Across Individuals Suggests Therapeutic Targets and Potential for Improvement
Authors: Wendy Sun et al.
Year: 2025
Venue / source: Human Brain Mapping
Link:
Date surfaced: 2026-03-26
Why selected in one sentence: It is a useful targeting paper because it shows that common TMS placement rules do not reliably engage the same higher-order networks across people and offers an individual-network modeling workflow instead.
Quick verdict
Useful
This is not a clinical efficacy paper, and the title is slightly grander than the evidential reach. But the paper makes a real contribution to intervention logic: it explicitly models which networks standard and individualized dlPFC TMS targets hit in each person, and it shows that common heuristics often miss the intended network or hit mixed network territory. That matters if the field wants to stop pretending “left dlPFC” is a sufficiently precise target description.
One-paragraph overview
The authors combine precision network estimation with transcranial magnetic stimulation electric-field modeling to ask what functional networks are actually stimulated by common clinical dlPFC TMS targets. They compare scalp-landmark targets such as F3/F4, sgACC-anticorrelation targets, and individually optimized coil placements in a dlPFC search space. Across participants, the same nominal target often engages different mixtures of frontoparietal, salience/cingulo-opercular, default, and other association networks. Individual optimization improves spatial selectivity and intensity for the intended network, and the authors argue this can be done from a relatively low-burden single MRI session.
Model definition
Inputs
Individual MRI-derived cortical anatomy, precision network estimates from resting-state fMRI, modeled TMS coil position/orientation, electric-field simulations, and predefined search spaces/target network labels.
Outputs
Estimated network identity and selectivity of each candidate TMS target, modeled electric-field intensity distributions, and optimized coil placements for chosen target networks.
Training objective (loss)
No trainable predictive model in the standard machine-learning sense is the central contribution here. The accessible text describes optimization of coil placement for network selectivity and E-field intensity, but not a conventional learned loss function.
Architecture / parameterization
A modeling and search pipeline combining precision network mapping with subject-specific TMS electric-field simulation and target-selection heuristics/optimization inside dlPFC.
Key questions this summary must address
1. What problem is the paper trying to solve?
Clinical TMS targets are often defined too coarsely. The paper tries to determine which functional networks are actually being stimulated in each individual and whether targeting can be made more selective.
2. What is the method?
Estimate each subject’s higher-order networks, simulate TMS E-fields for standard and individualized targets, quantify overlap/selectivity across networks, and prospectively search for coil placements that better isolate chosen networks.
3. What is the method motivation?
If depression or cognitive symptoms relate to network dysfunction, then a target description like F3 or even “most anti-sgACC site” may still be too imprecise. Better network-level targeting could reduce variability and improve intervention logic.
4. What data does it use?
The accessible text indicates analyses in 15 participants for the main modeling work, plus feasibility work in participants with major depressive disorder using lower-burden single-session MRI data.
5. How is it evaluated?
By comparing network selectivity and modeled E-field intensity across target choices, by demonstrating between-subject variability in what standard targets hit, and by showing that individualized optimization can recover more selective placements.
6. What are the main results?
Left F3 and right F4 frequently target different networks; right F4 tends to favor a right-lateralized control network. sgACC-anticorrelation targeting often hits a ventral-striatal-coupled network but misses it in some individuals. Prospectively optimized targets can more selectively engage chosen networks, and single-session MRI appears sufficient to reproduce useful targeting information.
7. What is actually novel?
The novelty is not “TMS targets vary.” The useful novelty is the explicit combination of person-specific network maps with E-field modeling to quantify what a nominal TMS target actually stimulates and to prospectively optimize it.
8. What are the strengths?
Makes target ambiguity visible instead of hiding it under dlPFC shorthand.
Separates selectivity from intensity, which the field often conflates.
Offers a practical individualized targeting workflow rather than only criticism.
Includes translational feasibility framing using single-session MRI.
9. What are the weaknesses, limitations, or red flags?
Mostly a targeting/modeling paper, not evidence that these optimized targets improve clinical outcomes.
Small participant counts.
Functional network estimation and E-field simulation each carry their own assumptions and errors.
The accessible text does not fully expose all optimization details or failure cases.
“Therapeutic targets” in the title is still partly aspirational until tested prospectively against outcomes.
10. What challenges or open problems remain?
Whether improved modeled selectivity yields better symptoms, how stable targets are across sessions and disease states, and how much additional burden clinics can tolerate for individualized mapping.
11. What future work naturally follows?
Prospective trials comparing optimized versus standard targeting, repeated-session stability analyses, and integration with physiology-based readouts such as TMS-EEG or symptom-linked network biomarkers.
12. Why does this matter for cabbageland?
Because it sharpens a core practical question: if you claim network-targeted TMS, can you show which network you are actually hitting in this person? This paper gives a better way to ask and partially answer that question.
13. What ideas are steal-worthy?
Treat TMS targeting as network selection under E-field constraints, not just scalp coordinate choice.
Quantify both selectivity and intensity for each candidate target.
Use low-burden individualized imaging when possible rather than assuming high-burden pipelines are the only route to precision.
Retrospectively audit prior sessions to estimate what network was probably stimulated.
14. Final decision
Keep as targeting infrastructure and framing. It does not prove therapeutic superiority, but it is useful ammunition against lazy “precision TMS” claims and a plausible template for better targeting workflows.
