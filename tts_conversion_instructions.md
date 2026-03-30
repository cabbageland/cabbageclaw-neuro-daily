# TTS Conversion Instructions for Research Summaries and Document Narration

## Purpose

Convert any input document into a spoken-audio-friendly script that is:
- easy for a text-to-speech model to read correctly,
- easy for a listener to follow in one pass,
- faithful to the source,
- stripped of visual-only clutter,
- reduced in redundancy,
- and structured for oral comprehension rather than page layout.

The goal is **not** to preserve the original writing style. The goal is to preserve the **information** while reformatting it for listening.

---

## Core Principle

Treat the source document as material for a spoken briefing, not as text to be read aloud verbatim.

A good TTS script should sound like:
- a competent narrator speaking to a human listener,
- with clear transitions,
- explicit labels,
- low ambiguity,
- short memory burden,
- and no visual artifacts.

---

## Fixed Opening and Closing Rules

## Rule 0A. Always use the standard opening line

Every Neuro Daily script must begin with:

**Welcome to the [MONTH DATE] Neuro Daily at Cabbageland!**

Replace `[MONTH DATE]` with a spoken-friendly date.

Examples:
- “Welcome to the March twenty-eighth Neuro Daily at Cabbageland!”
- “Welcome to the April second Neuro Daily at Cabbageland!”

Use spoken date style rather than purely visual date style.

---

## Rule 0B. Always use the standard closing line

Every Neuro Daily script must end with:

**Your reporter, Cabbage Claw. Salute!**

Do not paraphrase this closing unless the user explicitly asks for a different sign-off.

---

## Primary Objectives

When converting a document to TTS-friendly format, optimize for:

1. **Speakability** 
 The script should sound natural when read aloud.

2. **Listenability** 
 A listener should understand the structure without seeing the text.

3. **Fidelity** 
 Do not invent content. Preserve meaning, claims, uncertainty, and hierarchy.

4. **Compression of redundancy** 
 Remove repeated claims, repeated titles, repeated summaries, and repeated category labels unless repetition is functionally useful.

5. **TTS robustness** 
 Prevent the model from reading URLs, raw citations, strange symbols, formatting marks, table artifacts, or other junk aloud.

6. **Audio flow** 
 Prefer phrasing that sounds smooth and natural in speech, even when a more literal written phrasing also exists.

---

## Non-Negotiable Rules

## Rule 1. Preserve meaning, not formatting

Do not preserve:
- raw headers,
- bullet indentation,
- visual emphasis markers,
- citation syntax,
- table layout,
- hyperlinks,
- numbered references,
- inline markdown artifacts.

Do preserve:
- claims,
- evidence level,
- ranking,
- comparisons,
- uncertainty,
- distinctions between strong and weak evidence,
- conclusions,
- and source-dependent caveats.

---

## Rule 2. Convert written structure into spoken structure

Replace document-style organization with narration-style organization.

Preferred spoken structure:

1. Fixed opening line
2. Main pattern or top-line conclusion
3. Ranked items or major sections
4. Synthesis or takeaway
5. Uncertainty or inspection notes
6. Fixed closing line

Do not mechanically preserve every original section if multiple sections say the same thing.

---

## Rule 3. Remove redundancy aggressively

If the same information appears in:
- overview,
- executive summary,
- ranked list,
- conclusion,
- takeaway,
- category calls,

then combine them.

Keep only the version that best serves spoken comprehension.

### Remove or merge repeated content such as:
- the same paper title appearing in three different sections,
- the same “why it matters” claim repeated in overview and ranking,
- the same takeaway repeated in conclusion and summary,
- category labels that add no new information.

### Keep repetition only when it helps the listener:
- first mention of an item,
- transition into a ranked section,
- restatement of a major conclusion at the end.

Preserving content does **not** mean preserving redundancy.

---

## Rule 4. Make titles explicitly speakable

When introducing a paper, report, section, or named item, use spoken framing such as:

- “The first paper is directly relevant, titled, ...”
- “The second paper is titled, ...”
- “Another important study is titled, ...”
- “The report’s main section is called, ...”

Do not just drop titles into the paragraph without spoken framing.

### Preferred pattern
**[ordinal or role] + [relevance label if needed] + “titled” + quoted title**

Example:
- The second paper is directly relevant, titled, “Personalizing neuromodulation for chronic pain: A connectivity-guided randomized trial.”

This reduces listener confusion and helps TTS pacing.

---

## Rule 5. Replace visual shorthand with spoken equivalents

Convert abbreviations and symbols into spoken-friendly language when needed.

Examples:
- “rTMS” → “repetitive transcranial magnetic stimulation” on first mention
- “DBS” → “deep brain stimulation” on first mention
- “fMRI” → “functional MRI” on first mention
- “EEG” → “electroencephalography” on first mention if the audience may benefit
- “M1” → “primary motor cortex”
- “DLPFC” → “dorsolateral prefrontal cortex”
- “3T” → “three-tesla”
- “OFF” → “off”
- “7×7” → “seven by seven”

After first expansion, shortened forms may be reused if they remain easy to follow.

---

## Rule 6. Eliminate raw link and citation noise

Never leave in:
- full URLs
- bare hyperlinks
- DOI strings
- citation brackets
- markdown links
- reference superscripts
- raw footnote markers
- repository paths
- file paths
- inline HTML
- LaTeX fragments
- figure callouts unless verbally necessary

### Replace with:
- nothing, if the link is not needed for listening,
- or a spoken source summary, such as:
 - “This was inspected through the full text.”
 - “This was inspected at abstract level.”
 - “This was based on a preprint abstract and methods excerpt.”

The listener needs source confidence, not a readout of web garbage.

---

## Rule 7. Convert bullets into oral prose

Bullets should usually become short spoken paragraphs.

Bad for TTS:
- fragmented bullet points
- nested bullets
- bullet lists with repeated sentence stems

Better for TTS:
- one sentence of setup,
- then one paragraph per item,
- or one spoken list with explicit transitions:
 - “First...”
 - “Second...”
 - “Third...”
 - “Finally...”

---

## Rule 8. Shorten sentence length for audio

Prefer:
- short to medium sentences
- one claim per sentence
- one causal link per sentence
- one comparison per sentence

Avoid:
- long stacked clauses
- parenthetical overload
- multiple semicolons
- excessive appositives
- citation interruptions

### Practical target
Most sentences should be understandable in one breath.

---

## Rule 9. Use explicit spoken transitions

Listeners cannot see section breaks. Therefore transitions must be audible.

Use phrases like:
- “Here is the ranked list.”
- “The broader takeaway is simple.”
- “Why it matters:”
- “The main novelty is this.”
- “Inspection notes and uncertainty.”
- “Now for the most relevant paper.”
- “A final point.”

Do not rely on formatting alone to communicate structure.

---

## Rule 10. Reduce section count

For TTS, fewer sections are usually better.

### Preferred section template
1. Fixed opening
2. Ranked discussion
3. Synthesis takeaway
4. Uncertainty notes
5. Fixed closing

### Avoid unnecessary fragmentation
Do not separately keep all of these unless each adds real new information:
- short overview
- ranked list
- most relevant paper
- novelty section
- category calls
- takeaway
- conclusion
- inspection notes

That structure often repeats the same substance in different wrappers.

---

## Rule 11. Preserve uncertainty explicitly

Uncertainty should not be removed during cleanup.

Always preserve:
- evidence level
- whether the source was abstract-only
- whether full text was accessible
- whether claims are broad or fine-grained
- whether a result is preliminary
- whether translational relevance is weak

### Preferred spoken style
- “Confidence is good on the broad design, but not on every fine-grained quantitative detail.”
- “This was inspected at abstract level, so confidence is limited on implementation details.”
- “The concept is clear, but long-term safety data are not there yet.”

---

## Rule 12. Distinguish evidence from interpretation

When the document includes interpretation, mark it clearly as interpretation.

Use phrases like:
- “The useful read here is...”
- “The broader implication is...”
- “My synthesis is...”
- “This matters because...”

Do not blur factual reporting and interpretive judgment into a single vague claim.

---

## Rule 13. Keep rankings and labels, but simplify them

Labels such as:
- directly relevant
- adjacent inspiration
- weak but interesting
- negative result
- mechanistic
- preclinical

are useful for listeners, but only once.

Do not restate the same relevance label repeatedly unless it supports navigation.

Example:
- “The third paper is adjacent inspiration, titled...”

That is enough. No need to repeat “adjacent inspiration” again in a later category section.

---

## Rule 14. Preserve all content only when explicitly required

If the user says:
- “do not delete any contents,”

then preserve all information, but still:
- rewrite for speech
- merge repeated statements
- reorganize sections
- remove TTS-hostile artifacts

Preserving content does **not** mean preserving redundancy.

---

## Rule 15. Convert tables into narrated summaries

If the input contains a table, do not read row by row unless the table itself is the point.

Instead:
- identify what the table is trying to communicate
- summarize the dimensions
- then narrate the important contrasts

### Example
Instead of:
- “Column one is title, column two is method, column three is metric...”

Say:
- “The table compares methods across dataset, metric, and performance. The main pattern is that Method A leads on accuracy, while Method B is more stable across cohorts.”

Read cells one by one only if the user specifically wants that.

---

## Rule 16. Convert equations, symbols, and code-like strings only when necessary

For TTS:
- omit formulas unless they are central
- paraphrase mathematical content into words
- avoid raw symbolic readout when possible

Examples:
- “p less than zero point zero five”
- “A weighted sum of reconstruction loss and adversarial loss”
- “The model optimizes a contrastive objective”

Do not force TTS to read ugly raw notation unless the notation itself matters.

---

## Rule 17. Expand dates and numbers into spoken form when helpful

For better audio:
- “March 28th” → “March twenty-eighth”
- “14 patients” → “fourteen patients”
- “1 year” → “one year”
- “3-T MRI” → “three-tesla MRI”

Use spoken-number style when it improves clarity.

---

## Rule 18. Avoid stacked quotes and punctuation traps

TTS models often stumble on:
- heavy quotation marks
- nested parentheses
- slash-heavy constructions
- acronym clusters
- em dashes everywhere
- semicolon chains

Rewrite these into cleaner speech.

Example:
- Bad: “FLOATES—relay-wire-inspired, minimally invasive-ish, DBS-adjacent stimulation—shows...”
- Better: “FLOATES is a relay-wire-inspired deep-stimulation concept. It is minimally invasive in concept, but still early.”

---

## Rule 19. Prefer oral emphasis over typographic emphasis

Do not rely on:
- bold
- italics
- all caps
- parentheses
- underlines

Use spoken emphasis instead:
- “The key point is...”
- “The main limitation is...”
- “What matters most here is...”
- “The useful part is not X. The useful part is Y.”

---

## Rule 20. End with a clean synthesis

A TTS script should usually end with:
- the main conclusion
- the main uncertainty
- or the key action point

followed by the fixed closing line:
**Your reporter, Cabbage Claw. Salute!**

Do not end with:
- a dangling bullet
- a raw citation
- a file link
- a URL
- or a metadata stub

---

## Rule 21. Prefer spoken-natural phrasing over technically literal compounds

When a phrase is technically correct but awkward to hear, rewrite it into the most natural spoken equivalent without changing meaning.

Examples:
- “three-tesla magnetic-resonance-imaging-compatible system” 
 → “an MRI-compatible three-tesla system”
- “pulse-generator-plus-lead system” 
 → “a fully implanted deep brain stimulation system”

Choose speech-natural phrasing over literal but clunky noun piles.

---

## Rule 22. Avoid hyphen-stacking overload

Text can tolerate dense compound modifiers. Speech usually cannot.

Bad for audio:
- “deep-stimulation relay-wire-inspired minimally invasive device concept”

Better for audio:
- “a minimally invasive relay-wire concept for deep stimulation”

Break dense compound phrases into simpler units.

---

## Rule 23. Remove text-only stylistic quirks

Phrases that work on the page may sound awkward aloud.

Examples:
- “noninvasive-ish” 
 → “not fully invasive, but not truly noninvasive either”
- “decorative personalization rhetoric” 
 → “weak personalization claims,” if a plainer spoken register is better

Do not preserve page-level cleverness if it degrades audio flow.

---

## Rule 24. Optimize for mouthfeel, not just correctness

When choosing between two equally accurate phrasings, prefer the one that:
- has fewer stacked modifiers
- has cleaner rhythm
- is easier to parse on first hearing
- and does not force the listener to backtrack mentally

A phrase can be technically correct and still be bad audio.

---

## Rule 25. Preserve skepticism, but control theatricality

Critical interpretation is good for audio when it is precise.

Preferred:
- “This is more an engineering direction than translational evidence.”
- “The targeting logic is still weak.”
- “The result is interesting, but clinically limited.”

Avoid:
- “hand-wavy nonsense”
- “cute but flimsy”
- “noninvasive-ish,” if it pulls attention away from substance

The tone should be sharp, not performative.

---

## Rule 26. Do a final voice pass

After structural conversion is complete, do one final pass only for oral flow.

Check for:
- clunky compounds
- acronym piles
- awkward hyphen chains
- phrases that look good in text but sound bad aloud
- and lines that require too much listener parsing effort

This pass should improve rhythm, clarity, and speakability without adding or removing substantive content.

That last pass is the difference between “TTS-compatible” and “actually pleasant to hear.”

---

# Recommended Output Templates

## Template A: Research Paper Roundup

### Opening
- fixed opening line: “Welcome to the [MONTH DATE] Neuro Daily at Cabbageland!”
- one sentence on the strongest overall pattern

### Ranked discussion
For each item:
- ordinal position
- relevance label if useful
- title
- why it matters
- one or two sentences on evidence strength or limitation

### Synthesis
- one paragraph combining the broad takeaway
- what is worth preserving
- what is cautionary
- what is still speculative

### Inspection notes and uncertainty
- source depth
- confidence level
- what was and was not verified

### Closing
- fixed closing line: “Your reporter, Cabbage Claw. Salute!”

---

## Template B: Single-Paper TTS Summary

### Opening
- fixed opening line if used in Neuro Daily format
- title
- one-sentence judgment of what the paper is doing

### Problem
- what question it addresses
- why that question matters

### Method
- what data, setup, or intervention was used

### Main findings
- the strongest results only

### Why it matters
- mechanistic, clinical, or methodological significance

### Limits
- sample size
- evidence depth
- generalizability
- uncertainty

### Final takeaway
- one clean concluding paragraph

### Closing
- fixed closing line if the piece is formatted as a Neuro Daily segment

---

## Template C: General Document or Memo

### Opening frame
- fixed opening line if the output is explicitly a Neuro Daily
- what the document is about
- what the listener should pay attention to

### Main body
- grouped by topic, not by original formatting

### Synthesis
- the central point
- the practical implication

### Uncertainty or caveats
- what is tentative
- what remains unresolved

### Closing
- fixed closing line if the output is explicitly a Neuro Daily

---

# Editing Heuristics

## Heuristic 1. Merge “overview” with “takeaway” if they say the same thing
If both sections summarize the same conclusions, combine them into one spoken synthesis.

## Heuristic 2. Merge “ranked list” and “category calls” if category labels already appear in the item intros
No need for a separate category recap.

## Heuristic 3. Fold “most relevant paper” into the first ranked entry unless that paper needs deeper expansion
Keep a separate deep-dive only if it adds substantial new detail.

## Heuristic 4. Keep uncertainty as a separate ending section
This is useful in audio because it cleanly signals epistemic limits.

## Heuristic 5. Replace repeated title mentions with pronouns or role labels after the first clear introduction
After first mention:
- “this paper”
- “the trial”
- “the preprint”
- “the first study”

Avoid rereading long titles unnecessarily.

## Heuristic 6. Prefer one clean synthesis paragraph over multiple recap sections
If summary, takeaway, conclusion, and category calls all point to the same conclusion, collapse them.

## Heuristic 7. Split clunky noun chains during the final voice pass
If a phrase is hard to say or hard to hear, rewrite it even if it is technically fine in print.

## Heuristic 8. Treat the opening and closing as fixed anchors
No matter how much internal structure changes, keep the standard opening and closing lines unchanged unless the user asks otherwise.

---

# What to Remove or Rewrite

## Remove entirely
- raw URLs
- markdown links
- citation brackets
- figure numbers unless essential
- image captions with no narrative value
- file paths
- GitHub paths
- visual separators
- repeated headers that add no meaning

## Rewrite
- acronyms on first use
- symbols
- tables
- bullets
- ranking labels
- references to “above,” “below,” “left,” “right”
- phrases like “as shown in Figure 2”

Replace visual references with spoken references:
- “later in the paper”
- “in the results section”
- “the main comparison”
- “the authors’ central experiment”

---

# Tone Guidelines

Use a tone that is:
- clear
- confident
- compact
- spoken
- non-performative

Avoid sounding like:
- a chatbot
- a legal disclaimer
- a paper abstract pasted into speech
- a person reading bullet points without comprehension

Good TTS prose sounds like someone who already understood the material and is now briefing another person.

---

# Quality Checklist

Before finalizing a TTS conversion, check:

- Does the script start with “Welcome to the [MONTH DATE] Neuro Daily at Cabbageland!”?
- Does the script end with “Your reporter, Cabbage Claw. Salute!”?
- Does the script sound like speech rather than a document?
- Are raw links and citation artifacts gone?
- Are long titles introduced clearly?
- Is redundancy reduced?
- Are section transitions audible?
- Are abbreviations expanded where needed?
- Are uncertainty and evidence level preserved?
- Is clunky technical phrasing smoothed out for speech?
- Can a listener follow the hierarchy without seeing the page?
- Would the script still make sense if heard only once?

If the answer to any of these is no, revise.

---

# Minimal Instruction Block for Reuse

Use this when you want a compact prompt for future conversions:

Convert the input into a TTS-friendly spoken script. Always begin with “Welcome to the [MONTH DATE] Neuro Daily at Cabbageland!” and always end with “Your reporter, Cabbage Claw. Salute!” Preserve the meaning, evidence, ranking, and uncertainty, but rewrite the structure for listening rather than reading. Remove raw links, citations, markdown artifacts, file paths, and other visual-only clutter. Expand abbreviations on first mention when helpful. Introduce titles explicitly in spoken form. Reduce redundancy aggressively by merging overview, takeaway, category labels, and repeated summaries when they contain the same information. Use clear spoken transitions and short-to-medium sentences. Prefer speech-natural phrasing over technically literal but clunky compounds. Do a final voice pass to smooth rhythm, reduce stacked modifiers, and improve oral flow. The final script should sound natural when read aloud and should be easy to follow in one pass.

---

# Strong Default Conversion Policy

Unless the user says otherwise, apply these defaults:

- use the fixed Neuro Daily opening
- preserve information, not formatting
- compress redundancy
- expand important acronyms on first mention
- remove links and citation noise
- replace bullets with spoken prose
- introduce titles with spoken framing
- smooth clunky technical phrasing for audio
- end with synthesis plus uncertainty
- use the fixed Neuro Daily closing

For paper notes specifically, preserve the note’s substantive structure unless the user asks for a shorter briefing. If the note is organized around explicit questions, keep that question-by-question structure in the audio script. Do not delete content just to make the script shorter. Only deduplicate material when the same point is truly repeated.

---

# One-Sentence Standard

A successful TTS conversion is not a document read aloud. It is a spoken briefing built from the document, framed by a fixed opening and closing that make it sound like a proper Neuro Daily broadcast.
