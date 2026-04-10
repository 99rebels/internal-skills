---
name: idea-generator
description: Log and track skill ideas for later research and development. Use when Rian proposes a skill idea, asks to brainstorm skills, says "skill idea", "what if we built", "could we make a skill for", "log this idea", or discusses potential agent skills to create. Also use when reviewing the idea pipeline or discussing what to build next.
---

# Skill Ideas Pipeline

Manage the flow from raw idea to researched, buildable proposal.

## Idea Capture

When Rian shares a skill idea, log it to today's raw file:

```
ideas/raw/YYYY-MM-DD.md
```

Format each entry as:

```markdown
## 🔵 <Short Title>
What it is: <Brief summary of the idea as shaped through our conversation>
Origin: <How the idea came up — one line>
Type: new | enhancement(<existing-skill-name>)
Source: conversation | ecosystem-radar | clawhub-gap | user-request | self-initiated
Open questions: <Things we haven't figured out yet>
Status: new
```

### Fields explained

**Type** (required):
- `new` — a brand new skill idea
- `enhancement(<skill-name>)` — an improvement to an existing published skill. Include the ClawHub slug or local skill name

**Source** (required):
- `conversation` — came up organically while chatting with Rian
- `clawhub-gap` — identified from ClawHub market analysis (missing niche, underserved category)
- `user-request` — requested by a user or community member
- `self-initiated` — agent identified the opportunity independently
- `ecosystem-radar` — spotted via ecosystem-radar trend data (future: auto-generated)

**Status lifecycle:**
- `new` → just logged, waiting for research
- `researched` → nightly cron investigated and added to researched.md
- `picked-up` → Rian chose to build this
- `shipped` → published and live
- `deferred` → viable but deprioritized (include reason)
- `discarded` → not worth pursuing (include reason)

Rules:
- We brainstorm together — ideas evolve through conversation. The entry should capture where the idea landed, not just how it started
- Give your honest opinions in the conversation as we go, but the raw entry reflects the collaborative result
- If we keep discussing an idea, update the existing entry — do not duplicate
- Open questions are prompts for the nightly research pass to investigate
- Keep entries concise — no walls of text
- Create a new raw file each day if it does not exist

## Idea Research (Nightly Cron)

A cron job runs at midnight to research new ideas. You do not do this manually — it happens automatically.

When the nightly cron fires:
1. Read today's raw file
2. For each `status: new` entry, branch based on **Type**:

### Type: new (brand new skill)
Research:
- Check ClawHub for gaps and competition
- Assess feasibility (easy/medium/hard)
- Identify real user demand
- Discard ideas that are too vague, already well-covered, or technically impractical
- For promising ones, add to `ideas/researched.md` with:
  - Problem it solves
  - Target users
  - ClawHub gap analysis
  - Answers to the open questions
  - Feasibility (easy/medium/hard)
  - MVP scope for v1
  - **Effort vs Impact rating:** effort (low/medium/high) + impact (low/medium/high)
  - Honest recommendation — is this worth building?

### Type: enhancement (existing skill)
Research:
- Read the existing skill's SKILL.md and scripts
- Check API support for the proposed feature
- Assess breaking change risk (will this break existing users?)
- Estimate effort (trivial / small / medium / large)
- For promising ones, add to `ideas/researched.md` with:
  - What the enhancement adds
  - API/technical feasibility
  - Breaking change risk (none / low / medium / high)
  - Effort estimate (trivial / small / medium / large)
  - **Impact rating:** how much does this improve the skill for users? (low/medium/high)
  - Whether it fits the skill's current scope or should be a separate skill
  - Honest recommendation — is this worth the effort?

3. Mark processed entries as `status: researched` in the raw file
4. Do NOT delete entries from raw files

## File Structure

```
ideas/
├── raw/
│   └── YYYY-MM-DD.md    ← daily idea log
├── researched.md         ← curated proposals ready to build
└── shipped.md            ← (auto-created) record of ideas that shipped
```

## Reviewing Ideas

When Rian wants to review or pick an idea to build:
1. Read `ideas/researched.md`
2. Sort by impact rating (high first), then by effort (low first) — highest impact, lowest effort at the top
3. Present the top options concisely with effort/impact ratings
4. When Rian picks one, update the raw entry status to `picked-up`, then move to the skill creation flow
5. When a skill is published, update status to `shipped` and move the entry to `ideas/shipped.md`

## Weekly Priority Summary

Every Monday, present Rian with the top 3 highest-priority unshipped ideas from `ideas/researched.md`.

Priority formula: **high impact + low effort** ranks first. Break ties by recency (newer ideas first).

Format:
```
📋 Weekly Idea Priority (Apr 7, 2026)

1. 🔵 <Title> — enhancement(<skill>)
   Impact: high | Effort: small | Status: researched
   <One-line summary>

2. 🔵 <Title> — new
   Impact: medium | Effort: medium | Status: researched
   <One-line summary>

3. 🔵 <Title> — enhancement(<skill>)
   Impact: medium | Effort: trivial | Status: researched
   <One-line summary>

12 ideas total: 3 shipped, 2 picked-up, 5 researched, 2 deferred
```

Rules:
- Only include ideas with `status: researched` that haven't been picked up or shipped yet
- Skip deferred/discarded unless Rian asks
- Include a pipeline count at the bottom for context
