# Universal Brief Guide

Rules that apply to every brief regardless of format. For format-specific research steps, brief structure, and pre-flight checks, see the relevant format file:

- `brief-stack-play.md` — Stack Play briefs
- `brief-teardown.md` — Teardown briefs
- `brief-analysis.md` — Analysis briefs
- `brief-explainer.md` — Explainer briefs

Also reference `strategy-update-v2.md` for format definitions, framing rules, and publication positioning. For the publication's voice, posture, and writing principles, see `writers-voice-guide.md`. For Cambrian's research philosophy and alignment with the publication's posture, see `cambrian-research-philosophy.md`. For the templates Claude uses to direct Cambrian's research under the new pipeline flow, see `brief-exploratory-template.md` and `brief-directed-template.md`.

---

## 0. The Division of Labour (read this first)

The content pipeline has three roles and a clear division of labour. Understanding this division is the first thing a good brief reflects, because the brief is the handoff artefact between roles.

**Cambrian (you) is the researcher.** Cambrian installs, tests, and inspects skills inside the OpenClaw environment. Cambrian reads source code, runs security assessments, verifies install and download numbers via `clawhub inspect`, pulls GitHub stats via the CLI, tests workflows end to end, documents quotable moments from the research experience, and provides the raw material for every post. Cambrian is the only role in the pipeline with hands on the actual skills, and the value Cambrian provides is that nobody else can see what Cambrian sees.

**Claude is the writer.** Claude takes Cambrian's research brief and turns it into a published post. Claude does not install or test skills, but does have web search, web fetch, and code execution, which means Claude can verify any claim that exists on the public internet, pull GitHub stats independently, re-verify SaaS pricing at final draft time, research historical parallels and market context, and synthesise across findings. Claude owns the interpretive spine of the post: the frame, the argument, the analytical claim, and the action-layer advice that the post is built around.

**Rian is the editor.** Rian picks topics from Cambrian's proposals, reviews drafts, and approves for publishing. Rian is the middleman between Cambrian and Claude and the final editorial authority.

**The division of analytical work is specific and matters.** Both Cambrian and Claude do interpretive work, and they do different kinds:

- Cambrian does the close-reading analysis that's local to the research moment. What does this specific file do? What's notable about this skill's structure? What happened when the workflow was run end to end? What's the feasibility judgment on this specific workflow step? These are analytical claims that require being in front of the code or the running skill, and Cambrian is the only role in the pipeline that can make them.
- Claude does the synthesising analysis that steps back from individual findings to the wider frame. What pattern do these findings fit? What does this mean in the context of the market? What's the spine of the post? What's the action layer the reader should walk away with? These are interpretive claims that require stepping back from the research moment, which is Claude's job.

**What this means for the brief.** Cambrian owns the information layer fully and provides strong raw material for the analysis and action layers, but Cambrian does not need to prescribe the final analytical spine or the final narrative angle of the post. Claude will take the raw material and build the spine at drafting time. The briefs are research hand-offs plus light interpretive scaffolding, not fully-shaped post plans. Specifically:

- **Cambrian provides:** install/download/install counts, security findings, code quality assessments, test results, quotable moments, workflow observations, feasibility judgments, candidate analytical framings (labelled as candidates, not prescriptions), and any context that's only accessible inside the OpenClaw environment.
- **Claude produces at drafting time:** the final spine, the final narrative angle, the historical or market context research, the synthesising analysis across findings, the action-layer advice, and the published prose.
- **Shared responsibility:** SaaS pricing verification (Cambrian sources at research time with timestamp, Claude re-verifies at final draft time), GitHub stats verification (Cambrian pulls at research time, Claude can re-verify via the GitHub API as needed), and topic selection (Cambrian proposes, Rian picks, Claude flags if research is thin for the chosen angle).

The rest of this guide and the format-specific guides reflect this division. Under the new pipeline flow (see section 0.5), Claude typically locks in the post's direction before Cambrian starts the full research pass, which means Cambrian's research is executing against a direction rather than proposing one. For post types that don't need an exploratory phase, Cambrian may never need to surface candidate framings because Claude has already committed to one. For post types where the direction is set after an exploratory pass, Cambrian surfaces findings that Claude uses to commit to a direction. In both cases, Cambrian's research is the input to Claude's analysis, not a substitute for it.

The language about "surfacing candidate framings" in the format-specific guides applies when Cambrian is operating without a directed brief — either during an exploratory phase, or in the (rarer) case where research happens before direction is locked. When a directed brief is in hand, the format brief's guidance on surfacing candidates is superseded by the directed brief's commitment to a specific framing.

---

## 0.5 The Pipeline Flow

The Skill Economy's content pipeline runs in stages. Understanding the stages is important because they determine what kind of brief Cambrian receives and what kind of research pass is expected.

### The Three Brief Types

Cambrian can receive three kinds of brief from Claude during the pipeline:

1. **Exploratory brief** — A short, tightly-scoped research task that happens before the post's direction is locked in. The exploratory brief tells Cambrian to go look at a specific area, pull specific data or inspect specific skills, and return findings rather than a full brief. Claude uses the findings to commit to a direction. Not every post needs an exploratory phase. See `brief-exploratory-template.md` for the shape of an exploratory brief.

2. **Directed brief** — The document Claude produces after locking in a direction (either from exploratory findings, or directly from the topic for post types that don't need an exploratory phase). The directed brief tells Cambrian what the post is about, what to focus on, and what the three-layer plan is. It's specific to the post and it's written fresh for every post. See `brief-directed-template.md` for the shape of a directed brief.

3. **Format brief** — The permanent reference documents for research methodology. `brief-universal.md` (this document) plus the four format-specific guides: `brief-stack-play.md`, `brief-teardown.md`, `brief-analysis.md`, `brief-explainer.md`. The format briefs describe how Cambrian researches rigorously — the research steps, the security protocol, the brief structure for the full research brief output, and the pre-flight checks. They don't change from post to post. Cambrian reads them once and applies them consistently across all research work.

### How They Fit Together

The typical flow for a post is:

1. **Topic agreement.** Claude and Rian agree on a working topic and format together. The title is tentative at this stage and may shift after research.

2. **Exploratory phase (sometimes).** For post types where the direction depends on what the data shows — typically Teardowns and data-led Analysis — Claude produces an exploratory brief. Cambrian runs a short research pass and returns findings. Claude reviews the findings and decides whether the original direction holds up or needs to pivot.

3. **Directed brief.** Claude produces a directed brief that tells Cambrian exactly what to focus on during the full research pass. This includes the three-layer plan (information, analysis, action), the specific research focus, what to watch for, and any out-of-scope items. Rian reviews the directed brief before it goes to Cambrian, because this is the document that commits to the post's direction.

4. **Full research pass.** Cambrian reads the directed brief alongside the relevant format brief (stack-play, teardown, analysis, or explainer). The format brief tells Cambrian how to research rigorously. The directed brief tells Cambrian what to focus on. Cambrian executes the research and produces a full research brief as output, following the structure defined in the format brief.

5. **Writing.** Claude writes the post from the full research brief, doing any drafting-time research needed for historical parallels, market context, or verification.

### When the Exploratory Phase Is Needed

Not every post needs an exploratory phase. The test is whether Claude can set a useful direction without first seeing the data.

- **Exploratory phase typically needed:** Teardowns (spine depends on what testing reveals), data-led Analysis (spine depends on what the numbers show).
- **Exploratory phase sometimes needed:** Stack Plays (if the specific skills are unknown in advance), mixed Analysis posts (if the data shape matters).
- **Exploratory phase rarely needed:** Explainers (the concept is usually known in advance), argument-led Analysis (the thesis is usually set before research).

If the working topic can be turned into a clear directed brief without seeing data first, skip the exploratory phase and go straight to the directed brief.

### Conflict Resolution

If there's any conflict between the directed brief and the format brief for a specific post, the directed brief takes precedence. The format brief is generic guidance for how to research that format. The directed brief is specific to this post and reflects Claude's commitment to a direction. When they disagree, follow the directed brief.

Example: the format brief for Teardowns says Cambrian should "surface candidate framings for Claude to consider." The directed brief for a specific Teardown says "the framing is locked: the spine is X, focus on documenting the evidence that supports X." Cambrian follows the directed brief. The format brief language about surfacing candidates applies when no directed brief has locked the framing — which is no longer the default under the new flow.

---

## 1. Pre-Ideation Reminders

Run these before proposing ideas to Rian. They shape which ideas are worth proposing in the first place.

- **[MANDATORY]** Check the rotation. What format was the last post? What format is due next? The rotation is four formats (Analysis, Teardown, Stack Play, Explainer) and no format should appear twice in a row. Propose ideas that respect the rotation.
- **[MANDATORY]** Check the archive for duplicate coverage. Has any of this ground already been covered in a previous post? If yes, either pick a different angle or justify why this post adds something new.
- **[MANDATORY]** Propose ideas across multiple formats. Do not default to Stack Plays. When Rian asks "what should we write about this week?", present four options, one per format, or at minimum three formats represented.
- **[GUIDANCE]** Label each idea with its format and a one-line rationale explaining why it's worth writing. If an idea doesn't have a clear rationale, it's probably not strong enough.
- **[GUIDANCE]** For Analysis ideas, note whether the angle is data-led, argument-led, or mixed. This affects the research workload and helps Rian pick based on what's practical for the week.
- **[GUIDANCE]** Scan for timely hooks. Did something happen in the ecosystem this week that an idea could attach to? News, a registry change, a notable skill launching, a security incident. Timely hooks beat evergreen ideas for engagement.

---

## 2. The Three-Layer Framework

Every post in The Skill Economy operates on three layers, and every brief should provide raw material for all three. This is the organising principle behind every format and it's the thing that most distinguishes this publication from hustle content, from dry analysis, and from straight tutorials.

**Information.** What is happening in the market. Raw material: data, facts, context, numbers, test results, source code observations. This is the layer Cambrian owns most completely, because it comes directly from testing and inspecting skills. Every brief should have the information layer fully populated with verified data.

**Analysis.** What the information means. Interpretation, pattern, structural claim, implication. Cambrian provides candidate interpretations local to the research (this skill does X, which suggests Y about the category), but the final synthesising interpretation across findings happens at the writing stage. The brief should surface the raw material for analysis (surprises, counterexamples, patterns, comparisons) without locking in the final analytical claim.

**Action.** What the reader should do about it. Specific strategies, workflows, niches, positions, things to avoid, things to pursue. This is the layer most analyst publications skip by default and the layer most hustle publications botch. The Skill Economy claims this layer by grounding every action-layer claim in the information and analysis layers beneath it. The brief should provide raw material the writer can use to produce actionable advice: workflow observations, feasibility judgments, market gaps noticed during research, specific recommendations (install this, don't install that), and anything else that points toward what the reader should do.

**The rule for briefs:** every brief provides raw material for all three layers. The format determines which layer gets the most weight. Explainers lean on the information layer heaviest. Stack Plays lean on the action layer heaviest. Teardowns and Analysis lean on the analysis layer heaviest. But no format is allowed to skip any layer entirely, because the reader should finish every post knowing what's happening, what it means, and what to do about it.

**How this applies to what Cambrian provides versus what Claude produces:**

- Information layer: Cambrian provides this completely. The brief should have all verified numbers, all test results, all source code findings, and all context that only lives inside the OpenClaw environment.
- Analysis layer: Cambrian provides candidate interpretations and close-reading observations. Claude produces the final synthesising claim at drafting time, grounded in Cambrian's raw material.
- Action layer: Cambrian provides the raw material (workflow observations, what worked, what didn't, feasibility judgments, specific recommendations from testing). Claude produces the final action-layer advice at drafting time, grounded in Cambrian's research and any additional market context Claude gathers.

---

## 3. Universal Brief Checks

Run these on every brief. If any mandatory item fails, the brief is not ready.

### Structural Integrity

- **[MANDATORY]** Every skill mentioned in the brief has been installed, code-reviewed, and security-assessed according to the safety protocol. No exceptions.
- **[MANDATORY]** No orphaned references. Every skill named in the brief body is consistent with the skills listed in the skills table. No leftover mentions from earlier drafts.
- **[MANDATORY]** Every numeric claim (download counts, install counts, pricing figures, market sizes) has a source or is clearly labelled as an estimate.
- **[MANDATORY]** If the brief includes pricing for SaaS alternatives, those prices have been verified against current sources within the last 30 days. Cambrian sources pricing during research with a timestamp. Claude re-verifies at final draft time before publish. Pricing is shared responsibility.
- **[MANDATORY]** No self-contradictions. If a skill is in the rejected alternatives list, it is not also in the final stack. If the brief says X, it doesn't also say not-X somewhere else.

### Three-Layer Completeness

- **[MANDATORY]** The brief provides raw material for all three layers (information, analysis, action). No layer is empty, though the weighting varies by format.
- **[MANDATORY]** The information layer is fully populated with verified data. This is Cambrian's primary responsibility and the layer no other role can produce.
- **[MANDATORY]** The analysis layer includes candidate interpretations and close-reading observations from the research experience. These are surfaced as candidates, not prescriptions — Claude will produce the final synthesising claim at drafting time.
- **[MANDATORY]** The action layer includes raw material the writer can use to produce actionable advice: workflow observations, feasibility judgments, specific recommendations from testing, market gaps noticed during research, or whatever else points toward what the reader should do.

### Honesty Bar

- **[MANDATORY]** Every tested skill has an honest caveats section. "What it doesn't do" is as important as "what it does."
- **[MANDATORY]** If a skill disappoints, say so. If a claim in the skill's own description doesn't hold up on testing, the brief documents the gap.
- **[GUIDANCE]** The brief does not soft-ball praise. Avoid "powerful" and "comprehensive" as filler adjectives. Replace with specific things the skill actually does well.
- **[GUIDANCE]** The brief does not overstate what the writer will be able to conclude. If the data is thin or the testing is incomplete, flag it rather than hiding it.

### Quotable Moments

- **[MANDATORY]** The brief includes at least two or three quotable moments from the research. These are one of the most valuable things Cambrian provides because nobody else in the pipeline has hands on the skills at the moment something notable happens.
- **[GUIDANCE]** Quotable moments favour the reader's experience over the builder's experience. "The install command in the docs doesn't work" is better than "the build finished in 1.07 seconds." The first is something a reader can react to. The second is something only a developer cares about.
- **[GUIDANCE]** Quotable moments are written verbatim, not polished. Claude decides what to polish at drafting time.

### Candidate Framings (not prescriptions)

- **[MANDATORY]** The brief surfaces one or more candidate framings for the post — ways the research could be turned into a spine at drafting time. These are surfaced as candidates, explicitly labelled as such, and Claude has the authority to pick a different framing if the research supports it.
- **[MANDATORY]** If the post is a Stack Play, the candidate framings lead with market observation, not personal income claims. See `brief-stack-play.md` for detail. This rule is non-negotiable even though framings are now suggested rather than prescribed.
- **[GUIDANCE]** The brief includes one or two alternative framings in case the primary one doesn't hold up in drafting. Claude may pick any of them or invent a different one based on the raw material.

### Active-Voice Market Framing

- **[MANDATORY]** Findings are framed as active market events, not conditional possibilities. "The skill ecosystem crossed 350,000 packages in two months" is active. "The skill ecosystem might be growing quickly" is conditional. The Skill Economy writes as if the market is forming (see `writers-voice-guide.md` for the full posture), and the briefs should match that posture in how they describe findings.
- **[GUIDANCE]** Conditional framing is allowed when the data genuinely supports uncertainty ("this might be a pattern or it might be noise, the dataset is small"), but it should be labelled as uncertainty about the specific claim, not as general hedging about the market.

### Cold-Reader Context

- **[MANDATORY]** Every brief includes enough market context in the Market Context or Why Now section that Claude can produce a cold-reader opening without doing additional research. The opening of every post has to work for a reader arriving at the publication for the first time, and the raw material for that opening should be in the brief, not something Claude is expected to research independently.
- **[GUIDANCE]** Cold-reader context includes: what changed in the market recently, why this post matters this week specifically, what a reader would need to know to understand why the finding matters, and one or two source links Claude can use to anchor the opening.
- **[GUIDANCE]** Claude is still expected to research deeper historical and market context at drafting time (App Store comparisons, historical analogies, cross-ecosystem patterns). The brief provides the starting point, not the full context.

### Voice and Positioning

- **[GUIDANCE]** The brief's own voice is neutral and practical. It's a research document, not a draft post. It should read like an analyst's notes, not like marketing copy.
- **[GUIDANCE]** Nothing in the brief reads as hustle content. No "you could be making $X," no inflated promises, no "this one weird trick."
- **[GUIDANCE]** The brief respects the publication's position as market intelligence for a frontier market. Even if the post is practical, the framing is analytical.

---

## 4. Data Verification Protocol

No hallucinated data. Every number, claim, and fact in a brief must be traceable to a source. This applies to ALL formats.

**Before submitting any brief, verify:**

1. **Download/install numbers** — If from ClawHub, run `clawhub inspect <slug> --json` yourself. Don't rely on memory or cached data. Numbers change. This is Cambrian's primary source and Claude cannot independently verify it at the CLI level, so the brief needs to include the numbers inline with timestamps rather than just a file reference.
2. **GitHub stats** — Run `gh api repos/{owner}/{repo}` to confirm stars/forks. Don't estimate. Claude can re-verify these independently via the GitHub public API, but Cambrian should still pull them at research time.
3. **Ecosystem-radar data** — Check the timestamp on the data file. If it's more than a few days old, run a fresh collect before using it. Include the relevant numbers inline in the brief with timestamps — Claude cannot access the ecosystem-radar files directly and will be relying on Cambrian's numbers.
4. **SaaS pricing** — Check the actual pricing page. Verify within the last 30 days. Pricing changes frequently. Don't rely on memory or "I saw it last month." Pricing is shared responsibility: Cambrian sources at research time with timestamp and source link, Claude re-verifies at final draft time before publish.
5. **Web-sourced claims** — If a claim comes from a web search, note the source URL in the brief so Claude can reference it and Rian can verify.
6. **Calculated figures** — If you're computing something (savings, margins, ratios), show the math in the brief. Claude should see the inputs, not just the output.
7. **Quotes or statements attributed to people/orgs** — Verify via primary source if possible.
8. **Timestamp everything** — "As of [date]" on any data point that could change.

**Claude-side verification at drafting time.** Claude is responsible for re-verifying the following before a post ships: SaaS pricing (mandatory, 30-day window), ClawHub skill counts if the number is load-bearing in the post (mandatory, 7-day window for headline figures), and any market context claim that Claude is researching independently at drafting time. Claude cannot re-verify anything that requires CLI access or the OpenClaw environment — those claims rely on Cambrian's numbers and are trusted at handoff.

**Red flags that need extra verification:**
- Any number that seems surprisingly high or low
- Claims about platform features or capabilities ("ClawHub now supports X")
- Competitive comparisons ("cheaper than Y", "faster than Z")
- Market size or growth rate claims
- Anything attributed to "reports say" or "sources indicate"

**If you can't verify a data point, flag it explicitly** in the brief with `[UNVERIFIED]` and explain why. Claude and Rian can decide whether to include it or cut it. Never silently include unverified data.

---

## 5. When to Flag Issues to Rian

Don't interrupt research mid-flow. If something isn't working, note it and keep going. Flag everything at the end when you deliver the brief.

**Flag at the end of the brief (don't stop research for these):**
- A skill fails the security review (external calls to unknown domains, credential exfiltration, obfuscated code). Note it in the brief and let Rian decide whether we still cover it. Mark the top of the brief so the security finding is the first thing Rian sees.
- A tested skill doesn't do what it claims and the gap is large. Note the gap honestly — don't paper over it.
- You discover a security issue in a popular skill. Document it, note it in the brief.
- Data is too thin to support the idea. Finish what you can, note what's missing, and flag it.
- You can't verify a key data point. Mark it `[UNVERIFIED]` in the brief and explain why.
- Research reveals the topic was already covered well recently. Note it and suggest an alternative angle.

**The pattern:** finish the brief, include all notes and caveats, then present the whole thing to Rian with any concerns highlighted. Never stop mid-research to ask — just note problems and keep moving. We can always go back after.

**One exception: actively dangerous skills.** If continuing the research is itself a risk (a skill that runs malicious code on install, a skill that attempts to exfiltrate credentials the moment it loads, a skill that writes outside its sandbox in ways that could damage the testing environment, or similar), stop and flag immediately. The note-and-continue rule assumes the research itself is safe to continue. When it isn't, safety comes first, and Rian would rather be pinged mid-stream than discover the incident after the fact. These cases should be rare. Use judgement: the default is "note and continue," the exception is "stop and flag," and the line is whether continuing the research causes harm.

---

## 6. Idea Pipeline and Cross-Referencing

Before proposing ideas, check what's already been covered and what's in the pipeline. This prevents repetition and helps Rian see the full picture.

**What to check:**
- Published posts — titles and formats (track in `data/completed-ideas.md` or equivalent)
- Pipeline ideas — titles and formats that have been proposed but not written yet
- Format rotation — what format was last, what's due next

**Update the pipeline when:**
- Rian picks an idea from a proposal → move from pipeline to "in progress"
- A post is published → move to completed, record format and date
- An idea is dropped → remove or archive it with a note

**When proposing ideas to Rian:** he may ask to see the pipeline. Be ready to show what's been published, what's in progress, and what's queued. This helps avoid repeating formats or topics.

**The rotation check is part of this:** before proposing, confirm the last format used and ensure you're proposing across formats, not defaulting to one.

---

## 7. Post-Brief Updates

Claude may come back with questions during writing. Since Rian is the middleman between Cambrian and Claude:

- If Claude needs clarification, answer directly by updating the brief
- If the question reveals a gap in the research, do the additional research and update the brief
- If Rian flags something as inaccurate during review, re-verify before responding
- If the angle needs to change, assess whether existing research still supports it or if more work is needed

**Brief versioning:** when updating a brief after initial delivery, don't overwrite the original. Save as a new version and note what changed. Keep originals available in case we need to go back.

**Expected post-handoff pattern.** Because Claude owns the final analytical spine and the drafting-time research, it's expected (not exceptional) that Claude will do additional research at drafting time — verifying market context, checking historical parallels, re-running pricing, and occasionally asking Cambrian for a specific additional data point. If Claude's additional research surfaces something that changes the shape of the post, that's a signal the post is going to be stronger, not a signal the brief was incomplete. The brief is the starting point, not the ceiling.

---

## 8. Raw Data Storage

During research, you'll collect raw data (API responses, terminal output, web pages). Store it so it's traceable if needed later.

**Where:** `data/research/<post-slug>/`
- `raw/` — API responses, terminal output, scraped data
- `notes.md` — observations, things that didn't make the brief

**Why:** Claude may reference it during writing. Rian may verify a claim. Published data should be traceable.

**Note on Claude's access:** Claude cannot access the OpenClaw environment where `clawhub inspect` output lives. Any raw data Claude needs to reference has to be either included inline in the brief (preferred) or accessible via a public URL that Claude can web-fetch. File paths to local storage on the research environment are not accessible from Claude's side.

---

## 9. Minor Brief Inclusions

These are small things to include in every brief:

- **Skill version tested** — one line per skill (from `clawhub inspect` or skill metadata). If a newer version exists that wasn't tested, note it.
- **Testing environment** — hardware/OS/runtime (currently: Raspberry Pi 5, arm64, Linux 6.12, OpenClaw). Static for now but include it so the brief is self-contained.
- **Research date** — when the research was conducted. Numbers and data go stale.

---

## 10. Pre-Handoff Verification

Run these last, before sending the brief to the writer. The final QA pass.

- **[MANDATORY]** All mandatory items from this universal guide are satisfied.
- **[MANDATORY]** All mandatory items from the relevant format guide are satisfied.
- **[MANDATORY]** The brief is saved in the correct location (`data/briefs/`) with a descriptive filename.
- **[MANDATORY]** The brief has a clear "format" label. If it's an Analysis post, is it data-led, argument-led, or mixed?
- **[MANDATORY]** The three-layer framework is reflected in the brief. All three layers have raw material, weighted appropriately for the format.
- **[MANDATORY]** Candidate framings are labelled as candidates, not prescriptions. Claude has the authority to pick a different framing at drafting time.
- **[MANDATORY]** Cold-reader context is sufficient for Claude to produce the opening without additional research.
- **[GUIDANCE]** Do a final scan for leftover placeholder text, half-written sections, or TODO markers.
- **[GUIDANCE]** Read the brief through in one sitting. If something reads awkwardly or feels thin, fix it now rather than letting the writer flag it later.
- **[GUIDANCE]** Ask yourself: if I gave this brief to Claude with no additional context, could Claude produce a strong post by doing reasonable drafting-time research on top of the raw material provided? If the answer is no, the brief isn't ready.

---

## Quick Reference Card

For when you need the short version. Every brief must have:

1. A clearly labelled format (Analysis, Teardown, Stack Play, or Explainer)
2. All tested skills passed through the safety protocol
3. Raw material for all three layers (information, analysis, action)
4. No orphaned references or self-contradictions
5. Verified numeric claims with timestamps
6. Honest caveats that are actually honest
7. At least two quotable moments
8. Candidate framings (labelled as candidates) with at least one primary and one alternative
9. Active-voice market framing (market events, not conditional possibilities)
10. Enough cold-reader context that Claude can write the opening without additional research

If any of those ten items is missing or weak, the brief is not ready. Fix it before handoff.
