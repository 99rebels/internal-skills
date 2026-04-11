# Cambrian Document Set — README

**Purpose:** This README orients Cambrian to the document set. Read this first, then the files it points to in the order described below. Total active reading per session is three documents plus one format brief per post.

---

## The Pipeline in One Paragraph

The Skill Economy is a weekly Substack newsletter covering the AI agent skills market. The content pipeline has three roles: Rian (editor, founder), Claude (writer, also sets post direction), and Cambrian (you, research agent). For every post, Rian and Claude agree on a topic, Claude produces a directed research brief (sometimes preceded by an exploratory brief for post types where the direction depends on the data), Cambrian runs the full research pass and produces a structured research brief as output, and Claude writes the final post from that brief. Cambrian's job is the hands-on research work that nobody else in the pipeline can do: installing and testing skills, reading source code, running workflows, verifying numbers, documenting quotable moments. Cambrian is not expected to set the post's direction independently; that work is done by Claude before the full research pass begins, under the new pipeline flow.

---

## The Document Set

Six files, organised by purpose.

### Read Once at Session Start (alignment)

1. **`cambrian-research-philosophy.md`** — The posture and positioning alignment document. Covers the publication's voice at the research level, the three-layer framework (information, analysis, action), the active-voice framing rule, the position-versus-outcome test, and the division of labour between Cambrian and Claude. Read this at the start of every research session. Short (about 1,800 words). Internalise the five rules on the quick reference card at the end.

2. **`brief-universal.md`** — The universal rules that apply to every brief regardless of format. Contains the division of labour in detail (section 0), the pipeline flow description (section 0.5), the three-layer framework (section 2), the universal brief checks, the data verification protocol, the flagging protocol, and the pre-handoff verification. Read this once at the start of a session and refer back to it throughout when checking specific rules.

### Reference During Research (per post)

3. **One of the four format briefs.** Pick the one that matches the post Cambrian is working on:

 - **`brief-stack-play.md`** — Stack Play format. Workflows combining 2-4 skills for a specific outcome. Includes the Human Touch protocol and the anti-hustle framing rules.
 - **`brief-teardown.md`** — Teardown format. Critical reviews of individual skills or small groups. Includes the unsafe-skill protocol and the multi-skill structure.
 - **`brief-analysis.md`** — Analysis format. Data-led, argument-led, or mixed posts about what's happening in the market and what it means. Includes both sub-type-specific and universal research steps.
 - **`brief-explainer.md`** — Explainer format. Introductions to core concepts for readers new to the space. Includes the highest accuracy bar of any format.

 Cambrian only reads the one relevant format brief per post, not all four. The format brief tells Cambrian how to research rigorously for that format. It defines the research steps, the brief structure Cambrian produces as output, and the pre-flight checks.

### Received From Claude (per post, post-specific)

4. **The directed research brief for the current post.** Claude produces this fresh for every post, using either the exploratory or directed brief template (those templates are Claude's references, not Cambrian's — Cambrian receives the filled-in version). The directed brief tells Cambrian what this specific post is about, what the spine is, what to focus on during research, and what the three-layer plan is.

 **Under the new pipeline flow, the directed brief takes precedence over the format brief's guidance where the two could conflict.** The format brief's language about "surfacing candidate framings" applies when Cambrian is operating without a directed brief, which is rare under the new flow. When a directed brief is in hand, follow it. Cambrian is executing Claude's direction, not inferring a direction from the research.

### Sometimes Received From Claude (pre-research, optional)

5. **An exploratory brief** may be sent before the directed brief for post types where the direction depends on the data. Typical for Teardowns and data-led Analysis. When Cambrian receives an exploratory brief, run a short, tightly-scoped research task and return findings rather than a full brief. Claude uses the findings to commit to a direction and then produces the directed brief for the full research pass.

 The exploratory brief itself tells Cambrian exactly what to do and what to return. No separate methodology document is needed.

---

## How the Documents Fit Together

A simple way to picture it:

- **brief-universal** is the constitution. It applies to every brief regardless of format.
- **cambrian-research-philosophy** is the alignment layer. It tells Cambrian why the work is done the way it is.
- **The format briefs** are the methodology for each specific format. Cambrian reads the one relevant to the current post.
- **The directed brief** is the instructions for the specific post. Fresh every time.

When there's a conflict between documents, the order of precedence is:

1. **The directed brief** for the current post takes highest precedence.
2. **The format brief** for the current post's format takes second priority.
3. **brief-universal** is the baseline when the format brief doesn't address something.
4. **cambrian-research-philosophy** shapes the posture of everything else but doesn't override specific rules.

---

## What Cambrian Does Not Need to Read

These files exist in the project but are not part of Cambrian's active workspace:

- `writers-voice-guide.md` — Written for Claude. Covers sentence-level craft and format-specific tonal notes for publishable prose. Not relevant to research documents.
- `writers-brief-skills-economy.md` — The Claude-facing brief for the whole publication. Claude reads this; Cambrian doesn't need to.
- `brief-exploratory-template.md` and `brief-directed-template.md` — Templates Claude uses to produce the briefs Cambrian receives. Cambrian receives the filled-in versions, not the templates.
- `session-handoff.md` — Written for new Claude instances picking up the project. Not relevant to Cambrian.
- `cambrian-brief-checklist.md` — Deprecated. Superseded by brief-universal plus the format briefs. Should be removed from the workspace if still present.

---

## Quick Start: What to Do When a New Post Arrives

1. Read the directed brief from Claude to understand what the post is about and what the three-layer plan is.
2. Identify the format (Stack Play, Teardown, Analysis, or Explainer) and load the relevant format brief.
3. Follow the research steps in the format brief, using the directed brief to focus Cambrian's attention on the right skills, workflows, data, or questions.
4. Produce a full research brief as output, following the brief structure defined in the relevant format brief.
5. Run the pre-flight checks from both brief-universal and the format brief before handoff.
6. Flag anything notable at the end of the brief: security findings, unexpected results, data that contradicts the directed brief's working interpretation, anything that changes the shape of the post.

That's the whole process.
