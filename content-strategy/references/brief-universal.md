# Universal Brief Guide

Rules that apply to every brief regardless of format. For format-specific research steps, brief structure, and pre-flight checks, see the relevant format file:

- `brief-stack-play.md` — Stack Play briefs
- `brief-teardown.md` — Teardown briefs
- `brief-analysis.md` — Analysis briefs (coming soon)
- `brief-explainer.md` — Explainer briefs (coming soon)

Also reference `strategy-update-v2.md` for format definitions, framing rules, and publication positioning.

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

## 2. Universal Brief Checks

Run these on every brief. If any mandatory item fails, the brief is not ready.

### Structural Integrity

- **[MANDATORY]** Every skill mentioned in the brief has been installed, code-reviewed, and security-assessed according to the safety protocol. No exceptions.
- **[MANDATORY]** No orphaned references. Every skill named in the brief body is consistent with the skills listed in the skills table. No leftover mentions from earlier drafts.
- **[MANDATORY]** Every numeric claim (download counts, install counts, pricing figures, market sizes) has a source or is clearly labelled as an estimate.
- **[MANDATORY]** If the brief includes pricing for SaaS alternatives, those prices have been verified against current sources within the last 30 days. Do not rely on memory for SaaS pricing. It changes frequently.
- **[MANDATORY]** No self-contradictions. If a skill is in the rejected alternatives list, it is not also in the final stack. If the brief says X, it doesn't also say not-X somewhere else.

### Honesty Bar

- **[MANDATORY]** Every tested skill has an honest caveats section. "What it doesn't do" is as important as "what it does."
- **[MANDATORY]** If a skill disappoints, say so. If a claim in the skill's own description doesn't hold up on testing, the brief documents the gap.
- **[GUIDANCE]** The brief does not soft-ball praise. Avoid "powerful" and "comprehensive" as filler adjectives. Replace with specific things the skill actually does well.
- **[GUIDANCE]** The brief does not overstate what the writer will be able to conclude. If the data is thin or the testing is incomplete, flag it rather than hiding it.

### Quotable Moments

- **[GUIDANCE]** The brief includes at least two or three quotable moments from the research. Real, specific, surprising things that happened. Not generic observations.
- **[GUIDANCE]** Quotable moments favour the reader's experience over the builder's experience. "The install command in the docs doesn't work" is better than "the build finished in 1.07 seconds." The first is something a reader can react to. The second is something only a developer cares about.
- **[GUIDANCE]** Quotable moments are written verbatim, not polished. The writer decides what to polish.

### Narrative Angle

- **[MANDATORY]** The brief includes a suggested narrative angle for the writer, but does not over-prescribe the prose. The writer's job is to decide the hook, the voice, and the structure. The researcher's job is to give the writer enough to work with.
- **[MANDATORY]** If the post is a Stack Play, the suggested narrative angle leads with market context, not personal income claims. See `brief-stack-play.md` for detail.
- **[GUIDANCE]** The brief includes one or two alternative angles in case the primary one doesn't work. The writer may pick a different one.

### Voice and Positioning

- **[GUIDANCE]** The brief's own voice is neutral and practical. It's a research document, not a draft post. It should read like an analyst's notes, not like marketing copy.
- **[GUIDANCE]** Nothing in the brief reads as hustle content. No "you could be making $X," no inflated promises, no "this one weird trick."
- **[GUIDANCE]** The brief respects the publication's position as market intelligence for a frontier market. Even if the post is practical, the framing is analytical.

---

## 3. Data Verification Protocol

No hallucinated data. Every number, claim, and fact in a brief must be traceable to a source. This applies to ALL formats.

**Before submitting any brief, verify:**

1. **Download/install numbers** — If from ClawHub, run `clawhub inspect <slug> --json` yourself. Don't rely on memory or cached data. Numbers change.
2. **GitHub stats** — Run `gh api repos/{owner}/{repo}` to confirm stars/forks. Don't estimate.
3. **Ecosystem-radar data** — Check the timestamp on the data file. If it's more than a few days old, run a fresh collect before using it.
4. **SaaS pricing** — Check the actual pricing page. Verify within the last 30 days. Pricing changes frequently. Don't rely on memory or "I saw it last month."
5. **Web-sourced claims** — If a claim comes from a web search, note the source URL in the brief so Claude can reference it and Rian can verify.
6. **Calculated figures** — If you're computing something (savings, margins, ratios), show the math in the brief. Claude should see the inputs, not just the output.
7. **Quotes or statements attributed to people/orgs** — Verify via primary source if possible.
8. **Timestamp everything** — "As of [date]" on any data point that could change.

**Red flags that need extra verification:**
- Any number that seems surprisingly high or low
- Claims about platform features or capabilities ("ClawHub now supports X")
- Competitive comparisons ("cheaper than Y", "faster than Z")
- Market size or growth rate claims
- Anything attributed to "reports say" or "sources indicate"

**If you can't verify a data point, flag it explicitly** in the brief with `[UNVERIFIED]` and explain why. Claude and Rian can decide whether to include it or cut it. Never silently include unverified data.

---

## 4. When to Flag Issues to Rian

Don't interrupt research mid-flow. If something isn't working, note it and keep going. Flag everything at the end when you deliver the brief.

**Flag at the end of the brief (don't stop research for these):**
- A skill fails the security review (external calls to unknown domains, credential exfiltration, obfuscated code). Note it in the brief and let Rian decide whether we still cover it.
- A tested skill doesn't do what it claims and the gap is large. Note the gap honestly — don't paper over it.
- You discover a security issue in a popular skill. Document it, note it in the brief.
- Data is too thin to support the idea. Finish what you can, note what's missing, and flag it.
- You can't verify a key data point. Mark it `[UNVERIFIED]` in the brief and explain why.
- Research reveals the topic was already covered well recently. Note it and suggest an alternative angle.

**The pattern:** finish the brief, include all notes and caveats, then present the whole thing to Rian with any concerns highlighted. Never stop mid-research to ask — just note problems and keep moving. We can always go back after.

**One exception: actively dangerous skills.** If continuing the research is itself a risk (a skill that runs malicious code on install, a skill that attempts to exfiltrate credentials the moment it loads, a skill that writes outside its sandbox in ways that could damage the testing environment, or similar), stop and flag immediately. The note-and-continue rule assumes the research itself is safe to continue. When it isn't, safety comes first, and Rian would rather be pinged mid-stream than discover the incident after the fact. These cases should be rare. Use judgement: the default is "note and continue," the exception is "stop and flag," and the line is whether continuing the research causes harm.

---

## 5. Idea Pipeline and Cross-Referencing

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

## 6. Post-Brief Updates

Claude may come back with questions during writing. Since Rian is the middleman between Cambrian and Claude:

- If Claude needs clarification, answer directly by updating the brief
- If the question reveals a gap in the research, do the additional research and update the brief
- If Rian flags something as inaccurate during review, re-verify before responding
- If the angle needs to change, assess whether existing research still supports it or if more work is needed

**Brief versioning:** when updating a brief after initial delivery, don't overwrite the original. Save as a new version and note what changed. Keep originals available in case we need to go back.

---

## 7. Raw Data Storage

During research, you'll collect raw data (API responses, terminal output, web pages). Store it so it's traceable if needed later.

**Where:** `data/research/<post-slug>/`
- `raw/` — API responses, terminal output, scraped data
- `notes.md` — observations, things that didn't make the brief

**Why:** Claude may reference it during writing. Rian may verify a claim. Published data should be traceable.

---

## 8. Minor Brief Inclusions

These are small things to include in every brief:

- **Skill version tested** — one line per skill (from `clawhub inspect` or skill metadata). If a newer version exists that wasn't tested, note it.
- **Testing environment** — hardware/OS/runtime (currently: Raspberry Pi 5, arm64, Linux 6.12, OpenClaw). Static for now but include it so the brief is self-contained.
- **Research date** — when the research was conducted. Numbers and data go stale.

---

## 9. Pre-Handoff Verification

Run these last, before sending the brief to the writer. The final QA pass.

- **[MANDATORY]** All mandatory items from this universal guide are satisfied.
- **[MANDATORY]** All mandatory items from the relevant format guide are satisfied.
- **[MANDATORY]** The brief is saved in the correct location (`data/briefs/`) with a descriptive filename.
- **[MANDATORY]** The brief has a clear "format" label. If it's an Analysis post, is it data-led, argument-led, or mixed?
- **[GUIDANCE]** Do a final scan for leftover placeholder text, half-written sections, or TODO markers.
- **[GUIDANCE]** Read the brief through in one sitting. If something reads awkwardly or feels thin, fix it now rather than letting the writer flag it later.
- **[GUIDANCE]** Ask yourself: if I gave this brief to a competent writer with zero context, could they produce a strong post from it? If the answer is no, the brief isn't ready.

---

## Quick Reference Card

For when you need the short version. Every brief must have:

1. A clearly labelled format (Analysis, Teardown, Stack Play, or Explainer)
2. All tested skills passed through the safety protocol
3. No orphaned references or self-contradictions
4. Verified numeric claims with timestamps
5. Honest caveats that are actually honest
6. At least two quotable moments
7. A suggested narrative angle that fits the format's framing rules
8. A "so what" synthesis that points toward something the reader can act on

If any of those eight items is missing or weak, the brief is not ready. Fix it before handoff.
