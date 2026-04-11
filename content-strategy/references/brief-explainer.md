# Explainer Brief Guide

Everything you need to research, structure, and deliver an Explainer brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What an Explainer Is

An introductory post that teaches a concept to readers new to the agent skills space. The reader should finish understanding something they didn't understand before — and ideally be able to do something with that understanding.

Explainers are the on-ramp for the publication's audience. They bring in readers who've heard about agent skills but don't know where to start, and they build the shared vocabulary that makes Analysis and Teardown posts accessible. Without Explainers, the publication only speaks to people who already know what a SKILL.md file is.

**What an Explainer is not:** It's not a tutorial (tutorials teach how to do a specific task; explainers teach what something is and why it matters). It's not documentation (documentation is reference material; explainers build understanding through narrative). It's not an opinion piece (explainers should be factual and neutral).

**The accuracy bar for Explainers is the highest of any format.** Teardown readers can catch factual errors because they already know the space. Analysis readers can push back on weak arguments because they have their own data. Explainer readers can do neither. By definition they're reading the post because they don't know the topic yet, which means they have no baseline to catch a confidently stated error. A wrong sentence in an Explainer becomes part of the reader's mental model and stays there until something else corrects it. Verify every factual claim against a primary source, define every technical term correctly, and flag any uncertain claim rather than smoothing over it. Confident-sounding inaccuracy is the failure mode to avoid.

**The three-layer mix for Explainers.** Explainers lean heaviest on the information layer (what the thing is, how it works, why it exists) but still require analysis ("here's why it matters in context") and action ("here's what you can do with this understanding"). An Explainer that ends without a concrete next step for the reader has wasted the closing. The zero-to-one framing is the target: the reader starts at zero (doesn't know what a skill is) and ends at one (can install a skill, read a SKILL.md, understand the vocabulary, know what to do next).

**Length target: 1000-1500 words.** Explainers are shorter than the other formats because readers new to the topic have less patience for length. Scope the research to support this target. A brief rich enough for a 2500-word post is a brief that's going to lose material at the drafting stage.

**Explainers are the long-term traffic engine.** Of the four formats, Explainers are the most likely to rank in search engines over time and keep bringing in new readers months after publishing. Favour evergreen concepts over timely ones when proposing topics, and favour search-friendly titles over cute hooks. "What Are AI Agent Skills?" will bring in new readers for years. "The Three Most Confusing Things About This Week's ClawHub Update" will be dead in a month.

---

## Research Steps

**Before anything else: does this Explainer teach something the reader can't easily get from the official documentation?** A post that restates what's already in the ClawHub or OpenClaw docs, only worse, isn't worth writing. Explainers earn their place by closing a real explanatory gap — simplifying something the official docs over-complicate, connecting concepts the docs leave disconnected, adding examples the docs don't include, or explaining the "why" the docs skip past. If you can't finish the sentence "this Explainer is worth reading instead of the official docs because..." in one line, pick a different topic or a better frame. The failure mode here is the post that teaches nothing a motivated reader couldn't find in five minutes of official reading.

1. **Define the scope.** What exactly are we explaining? One concept per post. "What is a skill?" is a post. "Everything about agent skills" is a book chapter. If you can't define the scope in one sentence, the post is too broad.

2. **Lead with a use case or problem, not a definition.** The reader cares about what they can do, not what something is. "Here's how an agent checks your calendar" before "A skill is a reusable capability for your agent." Start with the thing the reader can picture, then explain the machinery behind it.

3. **Identify what the reader already knows.** Assume they've heard of AI agents but don't know specifics. No jargon without explanation. No assumed context. Every concept that can't be defined in one sentence from general computing knowledge gets explicitly defined in the brief.

4. **Identify what the post assumes vs what it teaches.** Every Explainer sits on top of some baseline knowledge and teaches new knowledge on top of that baseline. Be explicit about which concepts the post assumes the reader already knows (maybe from a previous Explainer) and which concepts the post teaches from scratch. If the assumed concept hasn't been covered in a previous Explainer, either cover it briefly in this post or flag it as a missing prerequisite that might need its own post first.

5. **Verify every claim.** This is the most accuracy-critical format. Readers have no baseline to catch errors — if you say ClawHub has 51,000 skills and the real number is 31,000, the reader won't know. Check every fact against primary sources:
   - ClawHub docs and CLI output for ClawHub-specific claims
   - OpenClaw docs for OpenClaw-specific claims
   - Official GitHub repos for version numbers, features, capabilities
   - Web search for third-party claims (note source URLs)
   
   If you're uncertain about a claim, flag it `[UNVERIFIED]` in the brief. Better to flag uncertainty than to write confident nonsense. Claude can re-verify web-sourced claims at drafting time, but CLI-sourced claims rely on Cambrian's numbers and Claude will trust them as provided.

6. **Verify comparisons on both sides.** If the explainer compares skills to MCP tools, or ClawHub to npm, or agent skills to browser extensions — the description of the thing you're comparing against must be accurate too. A wrong description of the comparison target is the same error as a wrong description of the thing you're explaining.

7. **Use real examples for every abstract concept.** "A skill is a reusable capability for your agent" is abstract. "Think of it as an app for your agent. Install the 'manage-calendar' skill and your agent suddenly knows how to check your calendar and schedule meetings" is concrete. Every abstract concept in the brief should have at least one concrete, relatable example attached to it. Examples should use real skills/repos from ClawHub, not made-up ones.

8. **Find the right level of detail.** Enough to be useful, not enough to overwhelm. If explaining SKILL.md structure, show the anatomy of a real one — but a simplified version, not a 200-line file dump. If explaining how to install a skill, show the command and what happens next — not the full dependency tree.

9. **Find real evidence of confusion.** Don't just speculate about what readers will misunderstand — go find evidence of what they actually do misunderstand. Look at Reddit threads where people ask the same question repeatedly, Discord conversations where the same answer gets given over and over, comments on relevant posts or docs, support issues in skill repos, Stack Overflow-style questions about the topic. Real misconceptions from real sources are stronger material than imagined ones. Capture the specific misunderstanding verbatim where possible. If you found something confusing when you first learned it, that counts as evidence too, but try to corroborate it with at least one external source.

10. **Propose a logical progression.** From no knowledge to basic competence. Each section should build on the previous one. A reader who skips a section should still be able to follow the next one. Map this out in the brief so Claude can see the intended structure. This is surfaced as a candidate structure — Claude may reshape it at drafting time.

11. **Define a "start here" next action.** What should the reader do in the next ten minutes if they want to try this for themselves? A good Start Here is specific, achievable in ten minutes, and produces a visible result the reader can see. "Install ClawHub" is too vague. "Run `clawhub install brw-homepage-audit` and open the SKILL.md file it installs" is specific, achievable, and gives the reader something concrete to look at. Favour the second shape. Explainers that end with "now you know what a skill is" are forgettable. Explainers that end with an action the reader can actually complete give the reader momentum, and readers with momentum become subscribers.

12. **Run the read-aloud test.** Could a non-technical reader follow this? If the brief itself uses jargon that would confuse a newcomer, the post will too. Catch this in the brief, not in the draft. If you need to re-read a sentence three times to parse it, rewrite it.

13. **Check what this explainer enables.** What can the reader do after reading this that they couldn't do before? This is the bridge to deeper content — if they understand what a skill is, they're ready for a Teardown. If they understand how to evaluate a SKILL.md, they're ready for Analysis. Note this in the brief so Claude can point to the next post.

14. **Collect quotable moments.** Explainers have fewer natural quotable moments than other formats because the content is factual rather than experiential. But surprising facts, "aha" moments from the research, or things that reframed your own understanding are worth capturing. See `brief-universal.md` for quotable moments guidance.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Title]

## Topic & Angle

**Working title:** [suggested title — Claude may adjust]
**Format:** Explainer
**Concept being explained:** [one sentence — what exactly is this post teaching?]
**Why now:** [timeliness — why explain this concept this week? Is it trending? Referenced in recent news?]
**The hook:** [the use case or problem that could open the post — why should the reader care?]
**What this explainer assumes:** [what the reader already knows before starting — be honest about the prerequisite. If the assumed concept hasn't been covered in a previous Explainer, flag it.]
**What this explainer enables:** [what can the reader do after reading this that they couldn't before?]
**Target audience:** [who is this for? assumed prior knowledge level]

---

## Market Context

[1-2 paragraphs. Why does this concept matter right now? What's happening in the agent skills space that makes understanding this useful? Keep it brief — this is the "why should I keep reading" not the full explanation. Include at least one or two source links Claude can use as starting points for deeper context research at drafting time.]

---

## Core Concept

[The main explanation. What is this thing? How does it work? Why does it exist?]

[Break this into logical sections. Each section should be self-contained but build on the previous one. Use subheadings to guide the reader through the progression. This is surfaced as candidate structure — Claude may reshape it at drafting time.]

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

[Things the reader will likely get wrong. Address them explicitly. This is where the explainer earns its credibility — by showing you understand what's confusing about this topic. Sourced from real evidence per research step 9 — link or quote the real confusion you found.]

1. [Misconception]: [why it's wrong, what's actually true, source of the real confusion if applicable]
2. [Misconception]: [why it's wrong, what's actually true, source of the real confusion if applicable]

---

## Start Here

[The reader's next action. What should they do in the next ten minutes? This should be specific and achievable — not "go explore ClawHub" but "run this command to install your first skill and try it on a simple task." See research step 11 for the shape of a good Start Here.]

---

## Caveats

[What this explainer doesn't cover. Edge cases, advanced topics, things that are out of scope. Be honest about the boundaries.]

---

## Quotable Moments

[Real moments from the research. Surprising facts, things that reframed your understanding, "aha" moments. Explainers have fewer natural quotable moments than other formats — that's fine. Don't fabricate them.]

---

## Candidate Framings

**These are suggestions, not prescriptions. Claude has the authority to pick a different framing at drafting time based on the raw material in the brief.**

- **Candidate opening hook:** [the use case or problem that could draw the reader in]
- **Candidate primary structure:** [the logical progression through the concept]
- **Alternative structure:** [in case the primary doesn't work]
- **Candidate closing:** [the "start here" action, or a forward-looking line about what comes next]
- **Bridge to deeper content:** [what post should the reader read next? Analysis, Teardown, Stack Play? This is Cambrian's suggestion — Claude will decide at drafting time whether to include it in the post.]

---

## Research Notes

[Source URLs for all verified claims. Primary sources consulted. Things that were checked and confirmed. Things that couldn't be verified and why.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The Explainer teaches something the reader can't easily get from official documentation. The "this Explainer is worth reading instead of the official docs because..." sentence is completable in one line.
- **[MANDATORY]** The concept is defined in one sentence. If it needs more, the scope is too broad.
- **[MANDATORY]** Every factual claim has been verified against a primary source. Source URLs are included in the Research Notes.
- **[MANDATORY]** Every technical term introduced has a correct definition. No approximations.
- **[MANDATORY]** Every abstract concept has at least one concrete, relatable example attached. Real skills/repos from ClawHub, not hypothetical ones.
- **[MANDATORY]** Comparisons (if any) are accurate on both sides. A wrong description of the comparison target is the same error as a wrong description of the thing being explained.
- **[MANDATORY]** The assumed reader knowledge level is explicitly stated in the Topic & Angle block. No jargon without definition.
- **[MANDATORY]** The assumed prior knowledge is explicit. If it references a concept not covered in a previous Explainer, the brief flags this and either covers the prerequisite briefly or suggests it as a future post.
- **[MANDATORY]** Common misconceptions are identified and grounded in real evidence per research step 9. If you can't find real evidence of confusion, you haven't thought about this topic from a newcomer's perspective.
- **[MANDATORY]** A "Start Here" next action is defined. The reader should know exactly what to do after reading, and the action should be specific, achievable in ten minutes, and produce a visible result.
- **[MANDATORY]** What this explainer enables is noted — the bridge to deeper content.
- **[MANDATORY]** The brief passes the read-aloud test. If you need to re-read a sentence three times, rewrite it.
- **[MANDATORY]** Uncertain claims are flagged `[UNVERIFIED]`. Explainer errors are the most damaging because readers have no baseline to catch them.
- **[MANDATORY]** Candidate framings and candidate structure are labelled as candidates. Claude has the authority to reshape the structure at drafting time.
- **[GUIDANCE]** The brief leads with a use case or problem, not a technical definition.
- **[GUIDANCE]** The logical progression is mapped out — each section builds on the previous one.
- **[GUIDANCE]** Examples use real skills/repos from ClawHub, not made-up ones.
- **[GUIDANCE]** The brief identifies where analogies break down. Every analogy has limits.
- **[GUIDANCE]** The scope of the research supports the 1000-1500 word target length. Don't produce a brief rich enough for a 2500-word post.
