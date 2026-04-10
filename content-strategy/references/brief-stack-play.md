# Stack Play Brief Guide

Everything you need to research, structure, and deliver a Stack Play brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What a Stack Play Is

A practical post showing how 2-4 skills combine into a workflow that delivers a specific, measurable outcome. The reader should be able to replicate it. Stack Plays are one of four formats in the rotation — they are not the default, and they must not read as hustle content.

**The critical framing rule:** Stack Plays lead with market observation, not personal income claims. The body can be identical under both frames — the difference is the entry point.

- ❌ Weak: "How I Made $800 Per Client With This Skill Stack"
- ✅ Strong: "The Local Business Web Agency Market Just Broke Open. Here's the 4-Skill Stack."

---

## Research Steps

1. **Research the market first, before touching any skills.** Who serves this need today? What do they charge? What's the pain point? Why does this matter now? This feeds the framing — without a clear "why now," the post has no spine.

2. **Define the persona.** Specific, not generic. "Freelance web designers serving local trades businesses" not "anyone who wants to make money." Specific persona = specific pricing, specific workflow, specific caveats.

3. **Select the skills.** 2-4 skills that form a coherent workflow. They should complement each other, not be a random list. Each skill should have a clear role in the stack.

4. **Test the combination end-to-end.** Install all skills and run the full workflow. The critical test: does the *stack* work, not just individual skills? Integration points are where things break.

5. **Document the workflow step-by-step.** Every step, every config, every input/output. A reader should be able to follow this.

6. **Identify the weakest skill.** Which skill is the limiting factor? Could it be replaced or removed? Note this in the brief.

7. **Document workflow gaps.** If the stack requires the user to do something the skills don't handle (set up an account, buy a domain, write custom code), list it explicitly.

8a. **Research SaaS alternative pricing.** What would a SaaS equivalent cost per month and per year? Gather real numbers from vendor websites. Verify pricing is current (within 30 days) and note the source and date for each figure. Never rely on memory for SaaS pricing because it changes frequently.

8b. **Calculate per-client unit economics.** Revenue per client, costs per client (hosting, domains, tools, anything else), time per client in hours, effective hourly rate. Not just a total. The unit economics are where the post earns its credibility.

8c. **Build both a conservative and an optimistic scenario.** Conservative is the realistic first-client case. Optimistic is the case for an experienced operator in a strong market. The writer can pick which to foreground or use both.

8d. **Acknowledge market dependency of pricing.** What you can charge in San Francisco is different from Ohio. Note this explicitly so the writer can include it in the post.

9. **Identify human touch points.** At least 4 specific, concrete things the human does that the skills can't. Not vague ("client relationships matter") but specific ("visit the client in person," "rewrite copy that sounds AI-generated"). This section is non-negotiable — it's what separates the publication from hustle content.

    To generate strong human-touch points, work through these four categories and find at least one item in each:
    - **Taste and judgment.** What decisions does the skill make that a human would make differently? Where would the skill's default output feel off to someone with taste?
    - **Physical or in-person actions.** What can only happen face-to-face, in the physical world, or with real-world observation? Site visits, handshakes, noticing things a camera wouldn't catch.
    - **De-AI-ifying the output.** What in the skill's output would a careful reader clock as AI-generated? Copy that needs rewriting, stock photos that need replacing, voice that needs humanising.
    - **Compounding relationship work.** What does the human do now that pays off on the fifth, tenth, or twentieth client? Referrals, testimonials, reputation, repeat business, trust.

11. **Gather at least 3 specific caveats.** Specific to this stack, not generic disclaimers. "Setup takes time" is generic. "The contact form doesn't send emails without a separate backend" is specific.

12. **Collect quotable moments.** Surprising efficiencies, things that worked better than expected, things that didn't. Real, verbatim, unpolished. See `brief-universal.md` for quotable moments guidance.

    **For Stack Plays specifically, favour moments from the operator's lived workflow over moments from the build mechanics.** A reader can picture "the client stared at the scored report for a full ten seconds before saying anything." A reader cannot picture "the Vite build finished in 1.07 seconds." When in doubt, ask which moment a non-technical reader could react to emotionally.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Title]

## Topic & Angle

**Working title:** [title]
**Format:** Stack Play
**Why now:** [what changed in the market that makes this stack valuable today]
**Target persona:** [specific — who this stack serves]
**The story:** [the narrative arc — why should the reader care?]

---

## Market Context

[2-3 paragraphs on the market this stack operates in. Who serves this need today, what they charge, where the pain is, why it's relevant now. This is the writer's raw material for the opening — the "why this matters" section. Keep it factual and specific.]

---

## Skills in the Stack

| # | Skill | Slug | Role in Stack | Downloads | Installs | Security Rating |
|---|-------|------|--------------|-----------|----------|----------------|
| 1 | [Name] | [slug] | [what it does in the workflow] | [number] | [number] | [rating] |
| 2 | ... | | | | | |

---

## Skill 1: [Name]

**Install:** `clawhub install [slug]`
**Version tested:** [version]
**Research date:** [date]

### What It Claims
[Paraphrase]

### What It Actually Does
[After reading ALL files — code, config, references. Be specific.]

### Security Assessment
- **ClawHub rating:** [rating from inspect]
- **Code review findings:** [specific — external calls, credential access, obfuscation, companion skill installs]
- **Safety verdict:** [safe / use with caution / unsafe]

### Role in the Stack
[Why this skill, what it contributes, how it connects to the others]

### Pros
- [Honest, specific pro]

### Cons
- [Honest, specific con]

---

[Repeat for each skill]

---

## The Workflow

[Step-by-step walkthrough of the full stack in action. Every step, every config, every input/output. If the reader were to follow this, they should be able to replicate the outcome.]

### Where Testing Stopped
[If you couldn't test the full end-to-end (external deps, account requirements, etc.), flag exactly where.]

### Gaps in the Workflow
[What the user needs to do manually that the skills don't handle. Set up accounts, buy domains, write custom code, etc.]

### Weakest Skill
[Which skill is the limiting factor. Could it be replaced?]

---

## Unit Economics

### Conservative Scenario
- **What you'd charge:** [€/$X]
- **Time to deliver:** [X hours]
- **Effective hourly rate:** [€/$X/hr]
- **Skills cost:** [free / any paid components]
- **Other costs:** [hosting, domains, etc.]

### Optimistic Scenario
- **What you'd charge:** [€/$X]
- **Time to deliver:** [X hours]
- **Effective hourly rate:** [€/$X/hr]

### Market Pricing Context
[What SaaS tools charge for this, what freelancers/agencies charge, where this stack fits in the market]

### Pricing Caveats
[Pricing depends on market, client type, location, experience. What you can charge in one market is different from another.]

---

## SaaS Alternatives

| SaaS Tool | What It Does | Monthly Cost | Annual Cost | Free Tier? |
|-----------|-------------|-------------|-------------|------------|
| [Tool] | [brief] | $[X]/mo | $[X]/yr | [yes/no — what's included] |

### Key Differences: This Stack vs [SaaS Tool]
- Where the stack wins: [specific]
- Where the SaaS still wins: [specific]

---

## Human Touch

[At least 4 specific, concrete things the human does that the skills can't replace. Not vague. Specific actions, specific situations. Ensure at least one item from each of the four categories: taste/judgment, physical/in-person, de-AI-ifying output, compounding relationship work. See research step 9 for category definitions.]

---

## Caveats

[At least 3 specific caveats about this stack. What it doesn't do, what could go wrong, market conditions under which it wouldn't work. Not generic disclaimers.]

---

## Quotable Moments

[Real, verbatim moments from testing. Unpolished. The writer decides what to use.]

---

## Suggested Narrative Elements

For the writer to use or ignore:

- **Primary angle:** [leads with market observation, not income]
- **Alternative angle:** [in case the primary doesn't work]
- **Hook idea:** [something that positions the post as analysis, not hustle]
- **Closing idea:** [one memorable line]

**Consistency check:** the primary angle should reference the Market Context section above. If the primary angle doesn't follow directly from the market context you researched, something is inconsistent and needs reconciling before handoff.

---

## Research Notes

[Additional observations, raw data paths, things that didn't fit elsewhere.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The narrative angle leads with market observation, not personal income claims. No "I made $X" framing.
- **[MANDATORY]** There's a clear "why now" — something specific that changed in the market.
- **[MANDATORY]** The persona is specific, not generic.
- **[MANDATORY]** Every skill has been tested in the context of its role in the stack, not just individually.
- **[MANDATORY]** Workflow gaps are documented — what the user must do manually.
- **[MANDATORY]** The weakest skill in the stack is identified.
- **[MANDATORY]** Per-client unit economics are included (revenue, costs, time, effective hourly rate).
- **[MANDATORY]** Both conservative and optimistic pricing scenarios are present.
- **[MANDATORY]** Market dependency of pricing is acknowledged.
- **[MANDATORY]** Human Touch section has at least 4 specific, concrete recommendations.
- **[MANDATORY]** At least 3 specific caveats (not generic disclaimers).
- **[MANDATORY]** All pricing verified within the last 30 days against current sources.
- **[MANDATORY]** Both download and install counts are reported for every skill in the stack. If either is unavailable, flag it explicitly rather than leaving the cell blank.
- **[GUIDANCE]** The market context section is separate from the workflow section — the writer needs raw material for the "why this matters" opening.
- **[GUIDANCE]** The brief includes an alternative narrative angle in case the primary one doesn't work.
- **[GUIDANCE]** Nothing in the brief reads as hustle content — no "you could be making $X," no inflated promises.
