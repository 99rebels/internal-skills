# Content Research — "The Skills Economy"

Guide an AI agent in researching and producing data-rich research briefs for weekly content about AI agent skills. The briefs are handed off to Claude for the final writing pass.

## What This Skill Is (and Isn't)

This skill covers **research, testing, and data gathering**. It does NOT cover final prose writing — that's Claude's job.

**This skill does:**
- Ideation and topic selection
- Skill installation, code review, and testing
- Security auditing
- Data collection (downloads, pricing, features, comparisons)
- Producing a structured research brief

**Claude does:**
- Taking the research brief and writing the final post
- Voice, flow, narrative arc, hooks, closings
- Making it read like a Substack post, not a technical report

## Research Accuracy Rules (for Cambrian)

- **Never carry stale numbers.** If you don't have a verified source for a statistic, look it up fresh. Don't reuse numbers from memory or previous sessions without re-verifying.
- **Verify via `clawhub inspect --json`** for any skill-specific data (downloads, installs, stars). Web search data is often inaccurate or outdated.
- **If you can't verify a number, say so.** Use "approximately X" or "as of [date], ClawHub reports X" and note the source. Don't present guesses as facts.
- **Ask Rian to confirm rankings.** The ClawHub explore API is unreliable for sorted lists. If you're unsure about the top N, ask Rian to cross-check before finalizing.
- **Date-stamp all data.** Every brief should note when data was collected so readers (and future-you) know if it might be stale.

## Content Credibility Rules

- **Every claim must come from the research brief.** Do not fabricate test results, download numbers, quotes, or experiences. If the brief doesn't contain it, don't write it.
- **Use the Quotable Moments section verbatim.** These are real moments from actual testing. They make the post feel genuine. Do not invent plausible-sounding alternatives.
- **Don't embellish data.** If the brief says 148,893 downloads, don't round to "nearly 150,000" without indicating it's rounded. Don't add "it felt slow" if the brief doesn't say that.
- **When in doubt, attribute.** If you're generalizing from the brief's data, frame it as interpretation ("the data suggests") not fact ("it's clear that").
- **Never include our own skills in content posts** unless Rian explicitly approves it. The posts are honest reviews — mentioning our own skills looks biased and undermines trust.
- **Disclose if a skill was built by us** when it's relevant context (e.g., a teardown comparison of invoice skills where ours is one of them).
- **Prioritize third-party skills** — there are 48,000+ options. Find the genuinely best ones.

**The division of labor:**
- **Cambrian (this agent):** Researcher. Tests skills, gathers data, documents findings.
- **Claude:** Writer. Takes the research brief and produces the final post.
- **Rian:** Editor. Reviews Claude's draft, provides feedback, approves for publishing.

## When to Use This Skill

Activate when the user:
- Asks "what should we write about this week?"
- Asks to research a specific skill or topic
- Asks to produce a research brief
- Asks to check published content status

## Background

ClawHub has 48,000+ skills. Most are low quality or dangerous (2,371 flagged in recent audit). Nobody is doing honest, tested reviews or practical "how to automate X" content. This skill fills that gap.

For full strategic context, read `references/strategy.md`.

## Content Formats

Two types of research brief, each with a template in `references/templates/`:

| Format | Brief Template | Final Post Trigger |
|---|---|---|
| Skill Teardown | `references/templates/teardown-brief.md` | Reviewing a single skill (or comparison of 2-3 similar skills) |
| Workflow Listicle | `references/templates/listicle-brief.md` | Showcasing a stack of 2-5 skills that automate a painful workflow |

**Cadence:** One post per week, alternating teardowns and listicles.

---

## ⚠️ Skill Safety Protocol — READ BEFORE TESTING

**Non-negotiable. Every skill reviewed must go through this process.**

### 1. Pre-Install Check
Run `clawhub inspect <skill-slug> --json` and note: security rating, downloads, stars, install count, owner, tags, summary.

### 2. Skip Dangerous Skills
Any rating of `"dangerous"` or `"critical"` → **do not install.** Note it in the brief as skipped with the reason.

### 3. Install
`clawhub install <slug>` — install to the default location.

### 4. Code Review — Before Running Anything
Read **all** files. Look for:
- **Credential exfiltration:** reading env vars, config files, SSH keys, `~/.aws`, `~/.ssh`, `~/.config`, `~/.openclaw/credentials`, `~/.npm`, `~/.gitconfig`
- **External network calls:** API requests to unknown endpoints
- **File system access:** writes/reads outside expected skill paths
- **Obfuscated code:** base64 payloads, `eval()`/`exec()` on untrusted input, encoded strings
- **Companion skill installation:** skills that try to install other skills during setup

### 5. Post-Test Cleanup
Delete all installed skill files after testing: `rm -rf ~/.openclaw/workspace/skills/<slug>`

### 6. No Real Credentials
Never store real API keys, OAuth tokens, or credentials for testing. Mock the data.

### 7. Document Everything
Every brief MUST include a security section per skill with: ClawHub rating, code review findings, external calls, and safety verdict.

---

## Ideation Process

**Interactive, not automated.** Wait for the user to ask.

When asked ("what should we write about?"):
1. Check `data/completed-ideas.md` and `data/published.json` — avoid repeats
2. Research sources: ClawHub trending, `ecosystem-radar` data, category gaps, seasonal relevance
3. Present 3-5 ideas, each with:
   - Working title
   - Format (teardown/listicle)
   - Proposed skills to test
   - SaaS alternatives to compare against
   - Why it's timely
   - The narrative angle (what's the story?)
4. Wait for user to pick

**Key principle for listicles:** Skills should form a **coherent stack**, not a random list. They should compound together and tell a story. E.g., GOG (email) + Summarize (content) + Briefing (morning dashboard) = "your morning routine, unified."

Log all ideas to `data/ideas.md`.

## Research Brief Structure

The research brief is the handoff document. It should be **data-rich, structured, and honest**. It is NOT a draft — it's raw material for Claude to work with.

Every brief must include:

1. **Topic & Angle** — what the post is about and why now
2. **Skills Tested** — slug, download count, stars, install count
3. **For each skill:**
   - What it claims to do
   - What it actually does (after reading code)
   - Is it code-based or instruction-only?
   - Test methodology (what was tested, how)
   - Test results (what worked, what didn't, specific examples)
   - Security findings
   - Honest pros and cons
   - Install command
4. **SaaS Alternatives** — real pricing, real feature comparison
5. **Data Points** — savings calculations, download ratios, category gaps
6. **Caveats** — where the skills fall short, what SaaS still does better
7. **Target Audience** — who this is for
8. **Suggested Narrative Elements** — hooks, contrast points, memorable angles (but let Claude decide the actual prose)

## Producing the Brief

Follow the appropriate template from `references/templates/`:
- `teardown-brief.md` for skill teardowns
- `listicle-brief.md` for workflow listicles

Save briefs to: `data/briefs/<topic-slug>.md`

## The Writing Handoff

When the research brief is complete:

1. Save to `data/briefs/`
2. Tell Rian the brief is ready
3. Rian sends the brief to Claude with context: "Write a blog post based on this research brief. Target audience: entrepreneurs and developers. Voice: practical, opinionated, first person plural. Aim for Substack quality — hooks, narrative flow, contrast lines, memorable closings. Include install commands for each skill."
4. Claude writes the draft
5. Rian reviews and edits
6. When approved, update `data/ideas.md` status and `data/published.json`

## Reference Examples

Claude's example of the target writing quality is saved at:
- `references/examples/saas-listicle-claude.md` — ideal listicle style and structure

Use this as a calibration reference when writing briefs — not to copy, but to understand what Claude needs to produce the final post.

## Content Tracking

- **`data/ideas.md`** — Content backlog. Statuses: `idea` → `researching` → `briefing` → `writing` → `published`
- **`data/completed-ideas.md`** — Archive of finished posts (prevents duplicates)
- **`data/published.json`** — Published posts with id, title, format, date, platforms, URL, skills covered
- **`data/briefs/`** — Research briefs (input for Claude's writing pass)

**Before starting anything new:** Read `data/completed-ideas.md` and `data/published.json` to avoid repeating topics, angles, or skills.

## Workflow

1. **Ideation** → user asks, research sources, present 3-5 ideas → user picks
2. **Research** → mark as `researching`, install/test skills, run safety protocol
3. **Brief** → mark as `briefing`, produce structured research brief using template
4. **Handoff** → mark as `writing`, Rian sends brief to Claude for writing pass
5. **Review** → Rian reviews Claude's draft, requests edits if needed
6. **Publish** → mark as `published`, update `data/published.json` and `data/completed-ideas.md`
