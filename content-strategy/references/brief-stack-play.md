# Stack Play Brief Guide

Everything you need to research, structure, and deliver a Stack Play brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What a Stack Play Is

A practical post showing how 2-4 skills combine into a workflow that delivers a specific, measurable outcome. The reader should be able to replicate it. Stack Plays are one of four formats in the rotation — they are not the default, and they must not read as hustle content.

**What a Stack Play is not.** It's not a hustle playbook. It's not a "make money with AI" post. It's not a tutorial for developers. It's not a pure review of a set of skills. Stack Plays are the format where the publication is most at risk of drifting into hustle content, and the discipline that prevents that is the three-layer framework applied strictly. A Stack Play without the information layer (what changed in the market) and the analysis layer (what this means and why it's an opportunity) is just a workflow description dressed up as a post, which is exactly the genre this publication is trying to avoid.

**The three-layer mix for Stack Plays.** Stack Plays lean heaviest on the action layer (the workflow, the strategy, the math) but absolutely require the information and analysis layers up front. The reader needs to be convinced the opportunity is real before they care about the workflow. Open with the market observation (what changed, why it matters, why now), ground it in data, explain the shape of the opportunity, and then walk through the workflow. Skip the setup and the workflow feels disembodied.

**The critical framing rule:** Stack Plays lead with market observation, not personal income claims. This is non-negotiable, and it applies to the candidate framings Cambrian surfaces as well as to the final post.

- ❌ Weak: "How I Made $800 Per Client With This Skill Stack"
- ✅ Strong: "The Local Business Web Agency Market Just Broke Open. Here's the 4-Skill Stack."

---

## Research Steps

1. **Before anything else: does this Stack Play have a real opportunity behind it?** Stack Plays need stakes. The stakes come from a genuine market opportunity that exists right now, not from the novelty of combining skills. If you can't finish the sentence "this Stack Play matters because..." in one line, the post isn't ready to research. Pick a different workflow or a different frame.

2. **Research the market first, before touching any skills.** Who serves this need today? What do they charge? What's the pain point? Why does this matter now? This is raw material for the information and analysis layers. Claude will do additional market context research at drafting time (historical parallels, cross-ecosystem patterns, wider market framing), but the brief provides the starting point so Claude can hit the ground running. Include at least one or two source links Claude can use to anchor the opening.

3. **Define the persona.** Specific, not generic. "Freelance web designers serving local trades businesses" not "anyone who wants to make money." Specific persona equals specific pricing, specific workflow, specific caveats.

4. **Select the skills.** 2-4 skills that form a coherent workflow. They should complement each other, not be a random list. Each skill should have a clear role in the stack.

5. **Test the combination end-to-end.** Install all skills and run the full workflow. The critical test: does the *stack* work, not just individual skills? Integration points are where things break. This is the kind of close-reading analytical work only Cambrian can do, because it requires running the stack in front of you. Document feasibility observations in detail — they're some of the most valuable things Cambrian provides that nobody else in the pipeline can produce independently.

6. **Document the workflow step-by-step.** Every step, every config, every input/output. Claude should be able to walk through the workflow from the brief alone without having run it. This is the action-layer raw material — without it, Claude has nothing to turn into a walkthrough.

7. **Identify the weakest skill.** Which skill is the limiting factor? Could it be replaced or removed? Note this in the brief with Cambrian's feasibility judgment. Claude may drop the weakest skill at drafting time if the post is stronger without it.

8. **Document workflow gaps.** If the stack requires the user to do something the skills don't handle (set up an account, buy a domain, write custom code), list it explicitly. These gaps are important for the Honest Caveats section and for the reader's expectations.

9. **Research SaaS alternative pricing.** What would a SaaS equivalent cost per month and per year? Gather real numbers from vendor websites with source links and timestamps. Verify pricing is current (within 30 days) at research time. Claude will re-verify at final draft time before publish — pricing is shared responsibility.

10. **Calculate per-client unit economics.** Revenue per client, costs per client (hosting, domains, tools, anything else), time per client in hours, effective hourly rate. Not just a total. The unit economics are where the post earns its credibility.

11. **Build both a conservative and an optimistic scenario.** Conservative is the realistic first-client case. Optimistic is the case for an experienced operator in a strong market. Claude will pick which to foreground at drafting time or use both depending on what the post needs.

12. **Acknowledge market dependency of pricing.** What you can charge in San Francisco is different from Ohio. Note this explicitly in the brief so Claude can include it in the post.

13. **Identify human touch points.** At least 4 specific, concrete things the human does that the skills can't. Not vague ("client relationships matter") but specific ("visit the client in person," "rewrite copy that sounds AI-generated"). The Human Touch section is non-negotiable — it's what separates the publication from hustle content, and it's what lets Claude land the confident analyst-advising posture without tipping into outcome promises.

    To generate strong human-touch points, work through these four categories and find at least one item in each:
    - **Taste and judgment.** What decisions does the skill make that a human would make differently? Where would the skill's default output feel off to someone with taste?
    - **Physical or in-person actions.** What can only happen face-to-face, in the physical world, or with real-world observation? Site visits, handshakes, noticing things a camera wouldn't catch.
    - **De-AI-ifying the output.** What in the skill's output would a careful reader clock as AI-generated? Copy that needs rewriting, stock photos that need replacing, voice that needs humanising.
    - **Compounding relationship work.** What does the human do now that pays off on the fifth, tenth, or twentieth client? Referrals, testimonials, reputation, repeat business, trust.

14. **Gather at least 3 specific caveats.** Specific to this stack, not generic disclaimers. "Setup takes time" is generic. "The contact form doesn't send emails without a separate backend" is specific.

15. **Collect quotable moments.** Surprising efficiencies, things that worked better than expected, things that didn't. Real, verbatim, unpolished. See `brief-universal.md` for quotable moments guidance.

    **For Stack Plays specifically, favour moments from the operator's lived workflow over moments from the build mechanics.** A reader can picture "the client stared at the scored report for a full ten seconds before saying anything." A reader cannot picture "the Vite build finished in 1.07 seconds." When in doubt, ask which moment a non-technical reader could react to emotionally.

16. **Surface candidate framings for the post.** Suggest one or two candidate framings Claude can consider at drafting time — labelled as candidates, not prescriptions. Claude has the authority to pick a different framing based on the raw material in the brief. Candidate framings should lead with market observation, not income claims. See the Candidate Framings section of the brief template below.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Title]

## Topic & Angle

**Working title:** [title — suggested, Claude may adjust]
**Format:** Stack Play
**Why now:** [what changed in the market that makes this stack valuable today]
**Target persona:** [specific — who this stack serves]
**The opportunity:** [one-sentence description of the market opportunity this stack captures]

---

## Market Context

[2-3 paragraphs on the market this stack operates in. Who serves this need today, what they charge, where the pain is, why it's relevant now. This is raw material for Claude's opening — the "why this matters" section. Keep it factual and specific. Include at least one or two source links Claude can reference. Claude will do additional market context research at drafting time; this section is the starting point, not the ceiling.]

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
[After reading ALL files — code, config, references. Be specific. This is Cambrian's close-reading analysis and it should reflect what only Cambrian can see, because Claude cannot install or run the skill.]

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

[Step-by-step walkthrough of the full stack in action. Every step, every config, every input/output. Claude should be able to walk through the workflow from this section alone, without having run it.]

### Feasibility Judgment
[Cambrian's judgment on the workflow from running it end to end. Where is it brittle? Where is it surprisingly smooth? Which steps took longer than documented? Which steps failed on the first attempt? This is close-reading analysis that only Cambrian can produce, and it's some of the most valuable material in the brief.]

### Where Testing Stopped
[If you couldn't test the full end-to-end (external deps, account requirements, etc.), flag exactly where.]

### Gaps in the Workflow
[What the user needs to do manually that the skills don't handle. Set up accounts, buy domains, write custom code, etc.]

### Weakest Skill
[Which skill is the limiting factor. Could it be replaced? Claude may drop it at drafting time if the post is stronger without it.]

---

## Unit Economics

### Conservative Scenario
- **What you'd charge:** [$X]
- **Time to deliver:** [X hours]
- **Effective hourly rate:** [$X/hr]
- **Skills cost:** [free / any paid components]
- **Other costs:** [hosting, domains, etc.]

### Optimistic Scenario
- **What you'd charge:** [$X]
- **Time to deliver:** [X hours]
- **Effective hourly rate:** [$X/hr]

### Market Pricing Context
[What SaaS tools charge for this, what freelancers/agencies charge, where this stack fits in the market]

### Pricing Caveats
[Pricing depends on market, client type, location, experience. What you can charge in one market is different from another.]

---

## SaaS Alternatives

| SaaS Tool | What It Does | Monthly Cost | Annual Cost | Free Tier? | Source URL | Verified (date) |
|-----------|-------------|-------------|-------------|------------|------------|-----------------|
| [Tool] | [brief] | $[X]/mo | $[X]/yr | [yes/no — what's included] | [url] | [date] |

### Key Differences: This Stack vs [SaaS Tool]
- Where the stack wins: [specific]
- Where the SaaS still wins: [specific]

**Note on pricing verification:** Pricing is shared responsibility. Cambrian sources pricing at research time with the source URL and a timestamp. Claude re-verifies at final draft time before publish. If the prices have moved by final draft, Claude will update them in the post.

---

## Human Touch

[At least 4 specific, concrete things the human does that the skills can't replace. Not vague. Specific actions, specific situations. Ensure at least one item from each of the four categories: taste/judgment, physical/in-person, de-AI-ifying output, compounding relationship work. See research step 13 for category definitions.]

---

## Caveats

[At least 3 specific caveats about this stack. What it doesn't do, what could go wrong, market conditions under which it wouldn't work. Not generic disclaimers.]

---

## Quotable Moments

[Real, verbatim moments from testing. Unpolished. Claude decides what to use at drafting time.]

---

## Candidate Framings

**These are suggestions, not prescriptions. Claude has the authority to pick a different framing at drafting time based on the raw material in the brief.**

- **Primary framing candidate:** [leads with market observation, not income. Should reference the Market Context section above. If it doesn't, something is inconsistent.]
- **Alternative framing candidate:** [a different angle Claude could take if the primary doesn't hold up in drafting]
- **Hook candidate:** [something that positions the post as market analysis, not hustle]
- **Closing candidate:** [one memorable line that lands the action layer]

**Consistency check:** the primary framing candidate should reference the Market Context section above. If the primary framing doesn't follow directly from the market context you researched, something is inconsistent and needs reconciling before handoff.

---

## Research Notes

[Additional observations, raw data paths, things that didn't fit elsewhere.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The candidate framings lead with market observation, not personal income claims. No "I made $X" framing in any of the candidates.
- **[MANDATORY]** There's a clear "why now" — something specific that changed in the market.
- **[MANDATORY]** The persona is specific, not generic.
- **[MANDATORY]** Every skill has been tested in the context of its role in the stack, not just individually.
- **[MANDATORY]** The workflow has been tested end to end and the feasibility judgment is documented.
- **[MANDATORY]** Workflow gaps are documented — what the user must do manually.
- **[MANDATORY]** The weakest skill in the stack is identified.
- **[MANDATORY]** Per-client unit economics are included (revenue, costs, time, effective hourly rate).
- **[MANDATORY]** Both conservative and optimistic pricing scenarios are present.
- **[MANDATORY]** Market dependency of pricing is acknowledged.
- **[MANDATORY]** Human Touch section has at least 4 specific, concrete recommendations covering all four categories (taste, physical, de-AI, relationship).
- **[MANDATORY]** At least 3 specific caveats (not generic disclaimers).
- **[MANDATORY]** All SaaS pricing sourced with source URLs and timestamps. Cambrian verifies within 30 days at research time; Claude re-verifies at final draft time.
- **[MANDATORY]** Both download and install counts are reported for every skill in the stack. If either is unavailable, flag it explicitly rather than leaving the cell blank.
- **[MANDATORY]** Candidate framings are labelled as candidates. Claude has the authority to pick a different framing.
- **[MANDATORY]** Market context section has enough content that Claude can write the cold-reader opening without additional research.
- **[GUIDANCE]** The market context section is separate from the workflow section — Claude needs raw material for the "why this matters" opening.
- **[GUIDANCE]** The brief includes an alternative candidate framing in case the primary one doesn't work.
- **[GUIDANCE]** Nothing in the brief reads as hustle content — no "you could be making $X," no inflated promises.
