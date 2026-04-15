Causal connectivity maps derived from single-pulse interleaved TMS functional MRI.

Basic info. Title: Causal connectivity maps derived from single-pulse interleaved TMS functional MRI. Authors: Lison Bossus and colleagues. Year: 2026. Venue: Scientific Reports. Why selected: it tries to turn image-guided TMS from resting-connectivity inference into stimulation-evoked causal circuit mapping.

Quick verdict. Highly relevant. This is one of the better recent targeting-method papers because it makes a more causal move than the usual correlational network-mapping workflow. The useful claim is not that it finds a clinically validated psychiatric target. The useful claim is that personalized TMS plus interleaved functional MRI can generate reproducible downstream circuit maps after controlling for pain, motion, and somatosensory confounds.

One-paragraph overview. The paper aims to map causal downstream responses to personalized cortical stimulation sites rather than relying only on resting-state functional connectivity. In more than eighty participants, the authors selected left-hemisphere targets intended to engage either subgenual anterior cingulate cortex or basolateral amygdala and then delivered single-pulse TMS during functional MRI. They quantified event-related blood-oxygen-level-dependent responses and residualized major nuisance factors such as head motion, pain, and somatosensory effects. The main result is that frontal targets aimed at subgenual circuits elicited subgenual and distributed downstream responses, while ventrolateral targets aimed at amygdala circuits elicited negative amygdala responses and broad downstream engagement. The most useful output is the public causal-connectivity map resource.

Model definition. This paper does not present a trainable predictive model in the accessible abstract text. It presents a personalized targeting-and-measurement pipeline that produces stimulation-evoked circuit maps.

Inputs. Individualized cortical TMS targets intended to engage either subgenual anterior cingulate cortex or basolateral amygdala, single-pulse TMS events delivered during functional MRI, and nuisance variables including motion, pain, and somatosensory measures.

Outputs. Voxelwise event-related blood-oxygen-level-dependent maps, region-of-interest response estimates, and publicly shared causal-connectivity maps linking cortical stimulation sites to downstream circuit responses.

Training objective, or loss. No trainable optimization loss is described in the accessible abstract. The work is based on event-related imaging analysis rather than supervised model training.

Architecture or parameterization. Personalized connectivity-guided target selection combined with interleaved single-pulse TMS and voxelwise functional MRI response mapping.

What problem is the paper trying to solve? Most neuroimaging-based targeting methods are correlational, so they cannot show what downstream circuit activity is actually evoked when a cortical site is stimulated.

What is the method? The authors chose personalized left-hemisphere cortical targets designed to engage either subgenual anterior cingulate cortex or basolateral amygdala. They delivered single-pulse TMS during functional MRI, built voxelwise event-related response maps, and controlled for motion, pain, and somatosensory confounds.

What is the method motivation? If the field wants causal circuit claims, it should measure stimulation-evoked downstream responses rather than only infer them from resting connectivity.

What data does it use? The abstract reports more than eighty participants, individualized TMS target locations, event-related functional MRI responses, and confound measures related to pain and somatosensory experience.

How is it evaluated? Evaluation is based on voxelwise and region-of-interest TMS-evoked responses, with group-level analyses that residualize nuisance factors. The authors also compare downstream patterns associated with the two target classes.

What are the main results? Stimulation of frontal targets intended for subgenual circuits produced responses in subgenual anterior cingulate and other distributed regions. Ventrolateral targets intended for amygdala circuits produced negative responses in the amygdala and broader downstream engagement. The abstract also reports that region-of-interest analyses did not show strong between-target differences across participants, which is an important caution against overselling target specificity.

What is actually novel? The most novel piece is the attempt to build and share causal-connectivity maps from personalized single-pulse TMS functional MRI at scale, with explicit confound control.

What are the strengths? It makes a causal-measurement move rather than stopping at correlation. It uses personalized targets. And it explicitly controls for several obvious non-neural confounds.

What are the weaknesses, limitations, or red flags? Blood-oxygen-level-dependent signal remains indirect. The lack of strong region-of-interest separation between the two target classes tempers any simple story about clean circuit selectivity. This is also a mapping paper rather than a demonstration that the maps improve clinical outcomes. And I only inspected abstract-level text.

What challenges or open problems remain? The next challenge is to connect these causal maps to actual treatment optimization and to determine how stable they are within individuals across sessions and brain states.

What future work naturally follows? Prospective trials could test whether TMS targets selected using these causal maps outperform targets selected from resting connectivity alone.

Why does this matter for cabbageland? Because intervention logic should be justified mechanistically rather than by decorative network rhetoric. This paper is useful as an infrastructure step toward more causal targeting logic.

What ideas are steal-worthy? Use stimulation-evoked maps as a pressure test for correlational targeting hypotheses. Publish reusable circuit-response maps. And make confound control explicit in perturbation-imaging studies.

Final decision. Keep. Strong methods value and good causal-targeting infrastructure value.
