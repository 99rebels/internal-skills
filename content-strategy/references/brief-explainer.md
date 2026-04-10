# Explainer Brief Guide

Everything you need to research, structure, and deliver an Explainer brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What an Explainer Is

An introductory post that teaches a concept to readers new to the agent skills space. The reader should finish understanding something they didn't understand before — and ideally be able to do something with that understanding.

Explainers are the on-ramp for the publication's audience. They bring in readers who've heard about agent skills but don't know where to start, and they build the shared vocabulary that makes Analysis and Teardown posts accessible. Without Explainers, the publication only speaks to people who already know what a SKILL.md file is.

**What an Explainer is not:** It's not a tutorial (tutorials teach how to do a specific task; explainers teach what something is and why it matters). It's not documentation (documentation is reference material; explainers build understanding through narrative). It's not an opinion piece (explainers should be factual and neutral).

---

## Research Steps

1. **Define the scope.** What exactly are we explaining? One concept per post. "What is a skill?" is a post. "Everything about agent skills" is a book chapter. If you can't define the scope in one sentence, the post is too broad.

2. **Lead with a use case or problem, not a definition.** The reader cares about what they can do, not what something is. "Here's how an agent checks your calendar" before "A skill is a reusable capability for your agent." Start with the thing the reader can picture, then explain the machinery behind it.

3. **Identify what the reader already knows.** Assume they've heard of AI agents but don't know specifics. No jargon without explanation. No assumed context. Every concept that can't be defined in one sentence from general computing knowledge gets explicitly defined in the brief.

4. **Verify every claim.** This is the most accuracy-critical format. Readers have no baseline to catch errors — if you say ClawHub has 48,000 skills and the real number is 31,000, the reader won't know. Check every fact against primary sources:
   - ClawHub docs and CLI output for ClawHub-specific claims
   - OpenClaw docs for OpenClaw-specific claims
   - Official GitHub repos for version numbers, features, capabilities
   - Web search for third-party claims (note source URLs)
   
   If you're uncertain about a claim, flag it `[UNVERIFIED]` in the brief. Better to flag uncertainty than to write confident nonsense.

5. **Verify comparisons on both sides.** If the explainer compares skills to MCP tools, or ClawHub to npm, or agent skills to browser extensions — the description of the thing you're comparing against must be accurate too. A wrong description of the comparison target is the same error as a wrong description of the thing you're explaining.

6. **Use real examples for every abstract concept.** "A skill is a reusable capability for your agent" is abstract. "Think of it as an app for your agent. Install the 'manage-calendar' skill and your agent suddenly knows how to check your calendar and schedule meetings" is concrete. Every abstract concept in the brief should have at least one concrete, relatable example attached to it.

7. **Find the right level of detail.** Enough to be useful, not enough to overwhelm. If explaining SKILL.md structure, show the anatomy of a real one — but a simplified version, not a 200-line file dump. If explaining how to install a skill, show the command and what happens next — not the full dependency tree.

8. **Anticipate confusion points.** What will readers misunderstand? What's counterintuitive? What seems like it should work but doesn't? Address these explicitly in the brief. If you found something confusing when you first learned it, the reader will too.

9. **Propose a logical progression.** From no knowledge to basic competence. Each section should build on the previous one. A reader who skips a section should still be able to follow the next one. Map this out in the brief so the writer can see the intended structure.

10. **Define a "start here" next action.** What should the reader do in the next ten minutes if they want to try this for themselves? Explainers that end with "now you know what a skill is" are forgettable. Explainers that end with "here's how to install your first one" give the reader momentum.

11. **Run the read-aloud test.** Could a non-technical reader follow this? If the brief itself uses jargon that would confuse a newcomer, the post will too. Catch this in the brief, not in the draft. If you need to re-read a sentence three times to parse it, rewrite it.

12. **Check what this explainer enables.** What can the reader do after reading this that they couldn't do before? This is the bridge to deeper content — if they understand what a skill is, they're ready for a Teardown. If they understand how to evaluate a SKILL.md, they're ready for Analysis. Note this in the brief so the writer can point to the next post.

13. **Collect quotable moments.** Explainers have fewer natural quotable moments than other formats because the content is factual rather than experiential. But surprising facts, "aha" moments from the research, or things that reframed your own understanding are worth capturing. See `brief-universal.md` for quotable moments guidance.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Title]

## Topic & Angle

**Working title:** [title]
**Format:** Explainer
**Concept being explained:** [one sentence — what exactly is this post teaching?]
**Why now:** [timeliness — why explain this concept this week? Is it trending? Referenced in recent news?]
**The hook:** [the use case or problem that opens the post — why should the reader care?]
**Target audience:** [who is this for? assumed prior knowledge level]
**What this explainer enables:** [what can the reader do after reading this that they couldn't before?]

---

## Market Context

[1-2 paragraphs. Why does this concept matter right now? What's happening in the agent skills space that makes understanding this useful? Keep it brief — this is the "why should I keep reading" not the full explanation.]

---

## Core Concept

[The main explanation. What is this thing? How does it work? Why does it exist?]

[Break this into logical sections. Each section should be self-contained but build on the previous one. Use subheadings to guide the reader through the progression.]

### [Section 1: The Foundation]
[The most basic version of the concept. What it is in one paragraph, with a concrete example.]

### [Section 2: How It Works]
[The mechanics. Step by step, how does this actually work? Use real examples, not hypothetical ones.]

### [Section 3: Why It Matters]
[What problems does this solve? What would be harder without it? What does the landscape look like with it vs without it?]

---

## Real Examples

[At least 2-3 real examples from the actual ecosystem. Point to specific skills on ClawHub, real SKILL.md files, real workflows. Abstract explanations without concrete examples are forgettable.]

**Example 1:** [name, slug, what it demonstrates]
**Example 2:** [name, slug, what it demonstrates]
**Example 3:** [name, slug, what it demonstrates]

---

## Comparison (if applicable)

[If the explainer compares this concept to something else — skills vs MCP tools, ClawHub vs npm, agent skills vs browser extensions — lay out the comparison clearly. Accuracy on BOTH sides is critical.]

| Aspect | [This Concept] | [Comparison Target] |
|--------|----------------|---------------------|
| [Aspect] | [description] | [description] |
| [Aspect] | [description] | [description] |

**Key differences:** [what makes them genuinely different, not just different names for the same thing]

**Where the analogy breaks down:** [every analogy has limits. Note where this one stops being useful.]

---

## Common Misconceptions

[Things the reader will likely get wrong. Address them explicitly. This is where the explainer earns its credibility — by showing you understand what's confusing about this topic.]

1. [Misconception]: [why it's wrong, what's actually true]
2. [Misconception]: [why it's wrong, what's actually true]

---

## Start Here

[The reader's next action. What should they do in the next ten minutes? This should be specific and achievable — not "go explore ClawHub" but "run this command to install your first skill and try it on a simple task."]

---

## Caveats

[What this explainer doesn't cover. Edge cases, advanced topics, things that are out of scope. Be honest about the boundaries.]

---

## Quotable Moments

[Real moments from the research. Surprising facts, things that reframed your understanding, "aha" moments. Explainers have fewer natural quotable moments than other formats — that's fine. Don't fabricate them.]

---

## Suggested Narrative Elements

For the writer to use or ignore:

- **Opening hook:** [the use case or problem that draws the reader in]
- **Primary structure:** [the logical progression through the concept]
- **Alternative structure:** [in case the primary doesn't work]
- **Closing idea:** [the "start here" action, or a forward-looking line about what comes next]
- **Bridge to deeper content:** [what post should the reader read next? Analysis, Teardown, Stack Play?]

---

## Research Notes

[Source URLs for all verified claims. Primary sources consulted. Things that were checked and confirmed. Things that couldn't be verified and why.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The concept is defined in one sentence. If it needs more, the scope is too broad.
- **[MANDATORY]** Every factual claim has been verified against a primary source. Source URLs are included in the Research Notes.
- **[MANDATORY]** Every technical term introduced has a correct definition. No approximations.
- **[MANDATORY]** Every abstract concept has at least one concrete, relatable example attached. Real skills/repos, not hypothetical ones.
- **[MANDATORY]** Comparisons (if any) are accurate on both sides. A wrong description of the comparison target is the same error as a wrong description of the thing being explained.
- **[MANDATORY]** The assumed reader knowledge level is explicitly stated. No jargon without definition.
- **[MANDATORY]** Common misconceptions are identified and addressed. If you can't think of any, you haven't thought about this topic from a newcomer's perspective.
- **[MANDATORY]** A "Start Here" next action is defined. The reader should know exactly what to do after reading.
- **[MANDATORY]** What this explainer enables is noted — the bridge to deeper content.
- **[MANDATORY]** The brief passes the read-aloud test. If you need to re-read a sentence three times, rewrite it. The brief should be clear enough that a non-technical person could follow it.
- **[MANDATORY]** Uncertain claims are flagged `[UNVERIFIED]`. Explainer errors are the most damaging because readers have no baseline to catch them.
- **[GUIDANCE]** The brief leads with a use case or problem, not a technical definition. The reader cares about what they can do, not what something is.
- **[GUIDANCE]** The logical progression is mapped out — each section builds on the previous one.
- **[GUIDANCE]** Examples use real skills/repos from ClawHub, not made-up ones.
- **[GUIDANCE]** The brief identifies where analogies break down. Every analogy has limits.
