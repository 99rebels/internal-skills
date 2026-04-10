# Analysis Brief Guide

Everything you need to research, structure, and deliver an Analysis brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What an Analysis Post Is

An examination of what's happening in the agent skills market and what it means. The reader should finish understanding something about this market they didn't understand before — a pattern, a trend, a structural dynamic, or a specific claim about where things are going.

Analysis is the format that most directly serves the publication's positioning as market intelligence for a frontier market. It's where the publication earns its identity as an analyst publication, not just a skill reviewer or a workflow tutorial.

**Two sub-types, often mixed:**

- **Data-led** — Starts with a specific question about the market, gathers data to answer it, and builds a narrative around what the numbers say. The data is the spine. "Who dominates the ClawHub leaderboard?" is a data-led question.
- **Argument-led** — Starts with a claim about the market, finds evidence to support it, and stress-tests it against counterarguments. The argument is the spine. "Agensi's Stripe integration will pressure other registries to add payments within 12 months" is an argument-led claim.
- **Mixed** — Most real Analysis posts will be both. Data supports the argument, and the argument gives meaning to the data. Label which is dominant when proposing the idea, so Rian knows the research workload.

Mixed briefs can start from either end: data-first (gather numbers, let them suggest a thesis) or thesis-first (state a claim, find data that tests it). Pick one and note the direction in the Topic & Angle section of the brief. This tells the writer how the argument was constructed and helps them decide whether to lead the post with data or with argument.

**What Analysis is not:** It's not a data dump. It's not an opinion piece with no evidence. It's not a list of interesting facts. Every Analysis post needs a spine — a single question, claim, or finding that the entire post serves.

---

## Research Steps

### For Data-Led Analysis (or mixed posts with a strong data component)

1. **Define the question.** What specific question are you answering? "What's happening in skills?" is not a question. "Do the most-downloaded skills on ClawHub actually have code, or are they instruction files?" is a question. Vague questions produce vague posts. If you can't state the question in one sentence, the post isn't ready to research.

2. **Identify data sources.** Before gathering anything, list what you need and where to get it. Common sources:
   - `clawhub search <query> --json` — skill listings by category, tag, or keyword
   - `clawhub inspect <slug> --json` — detailed skill metadata + security rating + download/install counts
   - `gh api repos/{owner}/{repo}` — GitHub stars, forks, issues, activity
   - `~/.openclaw/workspace/skills/ecosystem-radar/data/` — collected ecosystem data (daily pulses, trend data, platform tracking)
   - Web search for third-party reports, news, competitor data, market analysis
   - ClawHub leaderboard / category pages (via web fetch if CLI doesn't cover it)

3. **Gather the data.** Run the queries, scrape the pages, collect the numbers. Save raw data to `data/research/<post-slug>/raw/` so Claude can reference it during writing and Rian can verify claims. Don't just read numbers into memory — save them.

4. **Find the story.** Look for surprises, patterns, outliers, and contradictions in the data. The post should make the reader see something they didn't expect. "ClawHub has 48k skills" is a fact. "48k skills, but 12 authors publish 40% of the top-100 by downloads" is a story. The difference is the second one has a finding. Flag the most surprising or counter-intuitive data point — that's usually the spine of a data-led post.

5. **Check for counterexamples.** Any data point that contradicts your emerging narrative? Include it. A post that only presents confirming evidence reads like cherry-picking. The strongest analysis acknowledges what doesn't fit and explains why.

6. **Ensure apples-to-apples comparisons.** If comparing skills, make sure the metrics are measured the same way across all of them. ClawHub download counts include page views — call that out explicitly. GitHub stars and ClawHub downloads measure different things — don't conflate them.

7. **Verify freshness.** Timestamp everything. "As of April 14, 2026" on any number that could change. Skill metrics move fast — re-verify within 7 days of publish (same rule as Teardowns).

8. **Gather market context.** Even in data-led analysis, context strengthens the piece. What SaaS tools occupy this space? What's the pricing? What are competitors doing? A data point without market context is a number. A data point with market context is an insight.

9. **Provide raw data to the writer.** Include the raw data or a clear file path in the brief. Claude may want to interrogate the data differently than you did, or pull different comparisons. Don't just present conclusions — give the writer the inputs.

### For Argument-Led Analysis (or mixed posts with a strong argument component)

1. **State the thesis clearly.** One sentence. "Agensi's Stripe integration will pressure other registries to add payments by Q3" not "Payments are interesting." If the thesis needs three sentences, it's not tight enough. Distill it.

2. **Find supporting evidence.** Specific examples, data points, announcements, trends that support the claim. Minimum 3-4 distinct pieces of evidence. More is better. One data point is an anecdote. Three is a pattern. Five is hard to dismiss.

3. **Identify the strongest counterargument.** What would a smart skeptic say? Research this genuinely. If you can't find a good counterargument, the thesis is probably too obvious (and therefore not worth writing) or wrong (and you're not seeing the holes). The brief must acknowledge the counterargument and explain why the thesis still holds — or what would disprove it.

4. **Look for historical analogies.** Has this pattern played out before in other ecosystems? App stores, browser extensions, npm, WordPress plugins, mobile games, SaaS marketplaces? Historical parallels add credibility and give the reader a framework for understanding something new. "This looks like the early App Store in 2009" is a useful analogy. "This is unprecedented" usually isn't.

5. **Check for recency bias.** Is this claim based on one week's data or a real trend? One data point is an anecdote. Three is a pattern. Five over two months is a trend. Be honest about the strength of the evidence.

6. **Gather expert/builder context.** What are platform builders, skill authors, or commentators saying about this? Web search, Twitter/X, Discord conversations, blog posts. What's the prevailing opinion, and does the data agree or disagree?

7. **Avoid unfalsifiable predictions.** "The skills market will grow" is useless — every market grows until it doesn't. "Paid skills will emerge within 12 months and the first mover will be a registry, not a standalone platform" is a testable claim worth writing. The reader should be able to check back in six months and say "they were right" or "they were wrong."

8. **Flag strong vs speculative parts.** The writer needs to know where to be firm and where to hedge. If one piece of evidence is rock-solid and two are circumstantial, say so. Don't present equal confidence for unequal evidence.

### Universal Steps (both sub-types)

These steps apply to every Analysis brief regardless of sub-type. Complete them after the sub-type-specific steps above. Numbered 10-12 following data-led; argument-led briefs treat these as steps 9-11.

10. **Calibrate the audience.** Analysis posts serve different sub-audiences within the readership depending on the topic. Before finalising the brief, pick the specific sub-audience this post is pitched to. Candidates include:
    - Operators deciding what to build or automate
    - Founders scanning for unexplored market angles
    - Skill authors deciding what to publish and how
    - Platform builders and registry operators
    - Consultants and agencies advising clients on agent strategy

    Pick one as primary, optionally one as secondary. Note the choice in the Target audience field of the template and let it shape the synthesis section. An insight that lands with skill authors may not land with platform builders, and the "so what" section should be tuned to the primary audience.

11. **Write the "so what" synthesis.** Raw data or raw arguments without synthesis is a half-done brief. The brief must include a section that answers: what does this mean for the reader? What should an operator do with this information? If the answer is "nothing," the post probably isn't worth writing.

    Don't overreach. If the data only supports a narrow conclusion, don't pretend it supports a broader one. "Category X has more instruction-only skills than code-based ones" is honest. "The market is shifting away from code" is an overreach from the same data. Let the writer decide how far to stretch the conclusion, but give them an honest assessment of what the data actually supports.

12. **Identify the spine.** Every Analysis post needs a single element that carries the weight of the post. For data-led posts this is usually the most surprising finding. For argument-led posts it's usually the strongest or most counter-intuitive supporting point, or an unexpected counterargument that turned out to hold up, or a historical analogy that reframes how the reader sees the present. Flag this element explicitly in the Suggested Narrative Elements section of the brief so the writer knows what the post is really built around. If you can't identify a spine, the post probably isn't ready to write.

13. **Collect quotable moments.** Analysis posts can feel dry without them. Real moments from the research — a surprising number you found, a pattern that emerged unexpectedly, a data point that contradicted your assumption. Write them verbatim. See `brief-universal.md` for quotable moments guidance.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Title]

## Topic & Angle

**Working title:** [title]
**Format:** Analysis
**Sub-type:** [data-led / argument-led / mixed]
**Research direction:** [data-first / thesis-first — for mixed posts only]
**Why now:** [timeliness — why this analysis matters this week specifically]
**The question or thesis:** [one sentence — what is this post answering or arguing?]
**Target audience:** [specific sub-audience — see research step 10]
**Target audience (secondary):** [optional — if the post has a secondary audience]

---

## Market Context

[1-2 paragraphs on the broader market situation. What's happening in the agent skills space that makes this analysis relevant? This gives the writer the "why should I care" opening material.]

---

## Data and Evidence

*If the post is making a pure structural argument with no load-bearing quantitative findings, write "no significant quantitative data — see Argument Structure" in place of the subsections below and skip to the Argument Structure section. This should be rare. Most Analysis posts will have meaningful data even when the argument is the spine, and data almost always sharpens an argument. Only use this carve-out when the post genuinely doesn't lean on numbers.*

### Data Sources
- [Source 1]: [what it provided, timestamp]
- [Source 2]: [what it provided, timestamp]
- [Source 3]: [what it provided, timestamp]

### Key Findings

[Typically 3-5 findings. Add more if the data genuinely supports them, cut to fewer if the research only produced three strong ones. Don't pad to hit a number.]

1. **[Finding 1]:** [data point + what it means]
2. **[Finding 2]:** [data point + what it means]
3. **[Finding 3]:** [data point + what it means]

### The Most Surprising Finding
[Call out the single most counter-intuitive or unexpected data point. This is often the spine of the post.]

### Counterexamples and Complications
[Data points or evidence that don't fit the emerging narrative. Be honest about them. This is what separates analysis from cherry-picking.]

### What the Data Can't Tell Us
[Honest about the limitations. What questions remain unanswered? What would you need to know that isn't available?]

---

## Argument Structure (for argument-led or mixed posts)

**Thesis:** [one sentence]

**Supporting evidence:**
1. [Evidence point 1 — specific, sourced]
2. [Evidence point 2 — specific, sourced]
3. [Evidence point 3 — specific, sourced]
4. [Evidence point 4 — specific, sourced]

**Strongest counterargument:**
[What would a smart skeptic say? Why might this thesis be wrong?]

**Why the thesis still holds (or what would disprove it):**
[How do you address the counterargument? Or: what specific evidence would change your mind?]

**Historical analogy (if found):**
[Has this pattern played out before? In what market? What happened?]

**Strength of evidence:**
[Flag which parts are rock-solid vs circumstantial. Be honest. The writer needs to know where to be firm and where to hedge.]

**Testable prediction (if applicable):**
[A claim the reader can verify later. "If this analysis is right, we should see X within Y months."]

---

## So What Does This Mean

[The synthesis section. Step back from the data and arguments and answer: what should the reader do with this information? This is where the post earns its identity as market intelligence, not just interesting data.]

[Tune this section to the primary audience identified in research step 10. What does this mean for them specifically?]

[What should the reader pay attention to going forward? What's the signal to watch?]

---

## Caveats

[Honest limitations. What the data doesn't cover. What might change. Where the analysis might be wrong. Don't soften these — they're what make the analysis trustworthy.]

---

## Quotable Moments

[Real moments from the research. A surprising number you found. A pattern that emerged unexpectedly. Something that contradicted your assumption. Write them verbatim, unpolished. The writer decides what to use.]

---

## Suggested Narrative Elements

For the writer to use or ignore:

- **Primary angle:** [the spine of the post — the question or thesis that drives everything]
- **The spine:** [the single element that carries the post's weight — see research step 12]
- **Alternative angle:** [in case the primary doesn't work]
- **Hook idea:** [what opens the post — often the most surprising finding]
- **Closing idea:** [one memorable line — often the "so what" distilled]
- **Tone guidance:** [data-heavy and precise? argumentative and provocative? measured and analytical?]

---

## Research Notes

[Raw data file paths, additional observations, things that didn't fit elsewhere. The writer should be able to reconstruct the research from this section.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The question or thesis is stated in one clear sentence. If it needs more, the post isn't focused enough.
- **[MANDATORY]** The sub-type is labelled: data-led, argument-led, or mixed. The writer needs to know which lens to use.
- **[MANDATORY]** For mixed posts, the research direction is noted: data-first or thesis-first.
- **[MANDATORY]** Every number has been verified at the source and timestamped. "As of [date]" on any figure that could change.
- **[MANDATORY]** Comparisons are apples-to-apples. If comparing metrics across sources, the measurement methodology is noted.
- **[MANDATORY]** Raw data is provided or a clear file path is included. The writer should be able to interrogate the data independently.
- **[MANDATORY]** Counterexamples or complications are included. A post with only confirming evidence is cherry-picking.
- **[MANDATORY]** The "What the Data Can't Tell Us" section is present. Honest about limitations.
- **[MANDATORY]** The "So What Does This Mean" synthesis section is present and points toward something actionable. If the reader can't act on this information, the post needs a stronger synthesis.
- **[MANDATORY]** The synthesis is tuned to the primary audience. Not generic "readers should pay attention" — specific to the sub-audience identified in the brief.
- **[MANDATORY]** The spine is identified and flagged in the Suggested Narrative Elements. If you can't identify a single element that carries the post, it isn't ready.
- **[MANDATORY]** For argument-led posts making forward-looking claims, the prediction is falsifiable. The reader should be able to check back later and assess whether it held up. "The market will grow" is not a prediction. "Paid skills will emerge on ClawHub within 12 months" is.
- **[MANDATORY]** For argument-led posts making structural claims (about how the market is shaped today, not where it's going), the counterargument section is complete and substantive. Structural arguments don't need to be falsifiable in the predictive sense, but they do need to survive a smart reader pushing back.
- **[MANDATORY]** No unfalsifiable predictions. "The market will grow" is not a prediction. "Paid skills will emerge on ClawHub within 12 months" is.
- **[MANDATORY]** Historical analogies (if used) are accurate on both sides. A wrong description of the comparison market undermines the whole analogy.
- **[MANDATORY]** The brief flags which parts of the evidence are strong vs speculative. The writer needs to know where to be firm.
- **[GUIDANCE]** The brief provides enough raw material for the writer to reframe the narrative if the primary angle doesn't work. Analysis briefs should be rich enough to support multiple storylines.
- **[GUIDANCE]** The "So What" synthesis doesn't overreach. If the data supports a narrow conclusion, the synthesis should stay narrow. Don't ask the writer to make claims the evidence can't support.
- **[GUIDANCE]** Caveats are specific to this analysis, not generic disclaimers. "Data may be incomplete" is generic. "This analysis only covers ClawHub skills with 100+ downloads, so it misses the long tail of niche skills" is specific.
