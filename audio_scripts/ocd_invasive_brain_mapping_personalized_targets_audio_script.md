Invasive Brain Mapping Identifies Personalized Therapeutic Neuromodulation Targets for Obsessive-Compulsive Disorder
Basic info
Title: Invasive Brain Mapping Identifies Personalized Therapeutic Neuromodulation Targets for Obsessive-Compulsive Disorder
Authors: A. Moses Lee, Audrey Kist, John Alvarez, Kristin K. Sellers, Ankit N. Khambhati, Leo P. Sugrue, Lee B. Reid, Kelly Kadlec, Joline M. Fan, Anusha B. Allawala, Caroline A. Racine, Tenzin Norbu, Dani Astudillo, Alexandra G. Tremblay-McGaw, Natalie Becker, Ahmad Alhourani, Philip A. Starr, Edward F. Chang, Andrew D. Krystal, et al.
Year: 2025
Venue / source: medRxiv preprint; later updated in Translational Psychiatry
Link:
Date surfaced: 2026-03-25
Why selected in one sentence: It is one of the clearest recent examples of personalized circuit therapeutics where target selection, biomarker logic, and stimulation-induced circuit modulation are all made explicit.
Quick verdict
Must read
This is still a single-patient proof of concept, so no one should confuse it with settled evidence. But the paper does something many neuromodulation studies merely gesture at: it maps candidate sites, identifies a symptom-linked physiological signal, shows that the chosen stimulation sites suppress that signal, and then carries those sites into chronic DBS. If you care about mechanism-aware psychiatric neuromodulation, this is unusually concrete.
One-paragraph overview
The authors implanted temporary stereoelectroencephalography electrodes across cortico-striato-thalamo-cortical (CSTC) regions in a patient with severe treatment-refractory OCD, then used a multi-day inpatient stimulation-mapping protocol to identify sites that acutely improved symptoms. They found two right ventral capsule targets that reduced OCD symptoms during sham-controlled testing. Intracranial recordings suggested that high-frequency activity in orbitofrontal and related CSTC regions tracked symptom severity, and stimulation at the selected ventral capsule sites suppressed orbitofrontal high-frequency activity while showing structural and electrophysiological connectivity to those cortical regions. Those personalized targets were then implanted for chronic DBS, and combined stimulation produced an early clinical improvement.
Model definition
This paper does not present a major trainable predictive model for the intervention itself.
Inputs
Intracranial EEG/LFP recordings from implanted sEEG electrodes, symptom self-reports via visual analog scales, anatomical imaging, tractography, and stimulation parameters during mapping.
Outputs
Symptom-linked electrophysiological correlations, target rankings for stimulation sites, evoked-potential connectivity estimates, and acute symptom changes during stimulation.
Training objective (loss)
No explicit learnable control model or biomarker model with a stated optimization loss was described in the accessible text.
Architecture / parameterization
Mostly a stimulation-mapping and biomarker-identification workflow rather than a trainable ML architecture.
Key questions this summary must address
1. What problem is the paper trying to solve?
DBS for OCD works inconsistently across targets and patients. The paper tries to solve the targeting problem by identifying individualized therapeutic stimulation sites rather than assuming one standard anatomical target fits everyone.
2. What is the method?
Implant temporary electrodes across candidate OCD circuit nodes, run staged stimulation mapping with increasing rigor, correlate intracranial physiology with symptom severity, test whether candidate stimulation suppresses the symptom-linked physiology, then implant the top chronic DBS targets.
3. What is the method motivation?
OCD is heterogeneous, current DBS targets are variably effective, and anatomy alone does not guarantee target engagement. If symptoms arise from person-specific CSTC dysfunction, stimulation should be personalized by function as well as location.
4. What data does it use?
A single highly refractory OCD patient; 12 sEEG electrodes with 16 contacts each; symptom ratings during a 10-day inpatient stay; intracranial electrophysiology; evoked responses; diffusion MRI tractography; early chronic DBS follow-up.
5. How is it evaluated?
Acute symptom changes under active versus sham stimulation, electrophysiological correlations between symptom severity and local high-frequency activity, stimulation-induced suppression of high-frequency activity, evoked-potential connectivity, and early clinical response after chronic implantation.
6. What are the main results?
Two right ventral capsule targets produced the strongest acute symptom reduction in sham-controlled testing. Orbitofrontal and related CSTC high-frequency activity correlated with OCD severity. Therapeutic ventral capsule stimulation suppressed orbitofrontal high-frequency activity, and combined chronic stimulation produced a rapid early Y-BOCS improvement.
7. What is actually novel?
Not “DBS for OCD.” The novelty is the workflow: invasive mapping of multiple candidate OCD circuit nodes within one patient, explicit symptom-linked biomarker identification, and use of those results to guide multi-site personalized chronic DBS.
8. What are the strengths?
Mechanism and intervention logic are aligned.
Includes sham-controlled acute testing rather than pure anecdote.
Links target selection to both physiology and tractography.
Uses downstream circuit suppression as evidence of engagement, not just symptom report.
Carries mapping results into chronic implantation rather than stopping at exploratory physiology.
9. What are the weaknesses, limitations, or red flags?
n=1. That is the whole problem.
The protocol may favor targets with rapid effects and miss slower but valuable sites.
Biomarker generalization across OCD phenotypes is unknown.
Acute symptom ratings during provocation are useful but still vulnerable to context effects.
Early chronic response is encouraging, not definitive.
10. What challenges or open problems remain?
Generalizing the workflow beyond one patient, determining which biomarkers are portable across patients, reducing the burden of invasive mapping, and deciding when multi-site stimulation is actually worth the added surgical and programming complexity.
11. What future work naturally follows?
Small cohorts with the same protocol, head-to-head comparison versus standard VC/NAc targeting, longer-term follow-up, and attempts to derive less invasive predictors of the same therapeutic sites or engagement biomarkers.
12. Why does this matter for cabbageland?
Because it is a serious example of circuit therapeutics instead of decorative personalization rhetoric. It suggests a workflow for psychiatric neuromodulation where target choice is justified by symptom-linked physiology and demonstrated engagement, not just historical habit.
13. What ideas are steal-worthy?
Treat personalized target selection as a staged search problem with sham-controlled pruning.
Use symptom-linked physiological suppression as a target-engagement criterion.
Combine anatomy, evoked connectivity, and ongoing biomarker modulation rather than trusting any single view.
Consider multi-site stimulation when one tract/node does not appear sufficient to suppress the relevant circuit state.
14. Final decision
Preserve and revisit. This is one of the better recent exemplars of mechanism-aware psychiatric neuromodulation, but its evidential strength is still proof-of-concept rather than generalizable clinical standard.
