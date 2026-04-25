# Sub-Skill Deep Dive: Pipeline Tracker

**Parent:** Freelance Forge — `architecture.md`
**Version:** 0.2 — Design Phase
**Date:** 2026-04-25

---

## 1. Purpose

The Pipeline Tracker is the foundation of Freelance Forge. It owns the Notion database that serves as the freelancer's CRM, and it's the first sub-skill to run during setup. Every other sub-skill depends on the config file it creates.

**Three core functions:**
1. **Setup** — discover or create the Notion pipeline database, map the user's schema, save config
2. **Track** — show pipeline status, update lead stages, provide summaries
3. **Alert** — flag overdue proposals and follow-ups, offer to draft follow-up emails

---

## 2. When It Triggers

- "show my pipeline" / "pipeline update" / "pipeline summary"
- "update [client] to [status]" / "mark [client] as [status]"
- "any overdue follow-ups" / "check my follow-ups"
- "set up freelance forge" / "set up my pipeline"
- Also triggered implicitly when other sub-skills discover the config file doesn't exist

---

## 3. Setup Flow

### 3.1 Prerequisites

The sub-skill needs a Notion integration token. If `NOTION_TOKEN` env var is missing, display clear setup instructions (how to create an integration at notion.so/my-integrations, how to set the env var, and how to share the database with the integration in Notion). Then stop — don't proceed without a valid token.

Check for existing config at `$FREELANCE_FORGE_CONFIG_DIR/freelance-forge-config.json`. If it exists and is valid, skip to the tracking functions.

### 3.2 Database Discovery

Ask the user if they have an existing client pipeline or CRM database in Notion.

**If yes:** Search their workspace for databases (`POST /search`), present a list, let them pick one. Fetch the schema of the selected database (`GET /databases/{id}`).

**If no:** Skip to §3.4 to create a new one.

### 3.3 Schema Mapping & Augmentation

This is the critical setup step. The goal: map the user's existing database fields to our concepts, identify gaps, and offer to fill them.

**Mapping approach:** Inspect each property in the user's database and attempt to match it to our required concepts using property type and name heuristics (e.g., a `title` property → Company Name, a `select` with status-like values → Status, a `number` with score-like name → Lead Score). The full mapping list is in the architecture doc §4.1.

**Augmentation:** After mapping, identify which required concepts have no matching property. Present a clear summary to the user showing what mapped successfully and what's missing. Offer to add the missing columns via `PATCH /databases/{id}`. Emphasise that existing properties and data will not be touched.

If the user's database is too simple and several concepts would need to share a single field (e.g., one "Notes" field for research, discovery, and proposal notes), track this in the config under `sharedFields` so other sub-skills are aware.

**If the user declines augmentation:** Save the partial mapping. Note which features will be limited without the missing fields. The sub-skill should still work, just with reduced functionality.

### 3.4 Creating a New Database

If the user doesn't have an existing database, create one with the full default schema (see architecture doc §4.2). Ask the user for a name (default: "Client Pipeline") and whether they want to customise the status values before creation.

Default status options: Lead → Qualified → Proposal Sent → Onboarding → Active → Complete → Lost

### 3.5 Config File

Save `freelance-forge-config.json` to `$FREELANCE_FORGE_CONFIG_DIR/`. The config stores:
- The pipeline database ID
- Field mappings (our concept → their property name + type)
- Shared fields tracking (which concepts share a single Notion property)
- User preferences (currency, follow-up threshold days, default status options)

The exact config structure is defined in architecture doc §4.4. All sub-skills read this file to know which Notion properties to read/write.

### 3.6 Post-Setup

Confirm setup is complete. Briefly tell the user what they can do now and how to get started. Don't over-explain — they'll figure it out.

---

## 4. Pipeline Summary

When the user asks to see their pipeline, query the database and present a grouped, scannable digest. Key principles:

- **Group by status** — each stage as a section
- **Compact** — company name, score (if available), and one relevant data point (proposal date, days since last action, etc.)
- **Flag overdue items** — any lead in "Proposal Sent" past the follow-up threshold gets a visual indicator
- **Sort within groups** — by lead score descending if available
- **Handle unknown statuses** — if the user has status values we don't recognise, show them under a catch-all group rather than hiding them

The follow-up checker (§6) runs automatically as part of the pipeline summary. No separate trigger needed.

---

## 5. Status Updates

Parse the company name and target status from the user's request. Search the database for a matching page (exact match first, then fuzzy). Present the match for confirmation if ambiguous.

**Special case:** updating to "Lost" (or equivalent negative status) requires explicit user confirmation before proceeding. This is a meaningful signal that shouldn't happen by accident.

**Special case:** updating to "Active" should check whether a project database is linked. If not, flag it — the Project Onboarder may not have been run yet.

Keep the confirmation output minimal — one line is sufficient.

---

## 6. Follow-Up Checker

**Timing:** The follow-up check runs automatically whenever the pipeline summary is shown (§4). It can also be triggered directly ("any overdue follow-ups?").

**No cron for v1.** The user sees overdue items when they check their pipeline. Proactive alerts would require cron setup and risk being annoying. This can be a v2 feature.

**Logic:** Query for leads with status "Proposal Sent" (or the mapped equivalent). Compare their `proposalDate` or `lastFollowUp` to the current date. Flag any where the elapsed days exceed the `followUpDays` preference (default: 5). Sort by most overdue first.

**Offer to draft:** For each overdue lead, offer to draft a follow-up email in chat. If the user accepts, read the lead's full pipeline row for context and write a short, professional follow-up that references specific details from the proposal. Tone: helpful, not pushy. Include a clear next step.

---

## 7. Query Variants

Beyond the default summary, support these common queries:
- **Filtered by status:** "show me all leads in [status]"
- **Filtered by score:** "show me my best leads" (score above a threshold)
- **Filtered by date:** "leads from this week" (creation date range)
- **Single lead detail:** "tell me about [client]" (full row details)

---

## 8. Notion API Calls

The Pipeline Tracker uses these Notion API operations:
- `POST /search` — find databases during setup
- `GET /databases/{id}` — read schema during setup
- `POST /databases` — create new database
- `PATCH /databases/{id}` — augment existing database with missing properties
- `POST /databases/{id}/query` — query/filter pipeline pages
- `PATCH /pages/{id}` — update page properties (status changes)

It does NOT create pages (that's handled by Lead Qualifier, Proposal Builder, etc.).

---

## 9. Error Handling Principles

Errors should be helpful and actionable, not just informative. General patterns:

- **Missing token** → clear setup instructions with the exact URL and steps
- **Invalid token (401)** → direct the user to check at notion.so/my-integrations
- **Database not found** → list available databases so the user can pick
- **Integration not connected to database** → explain how to add the connection in Notion
- **Rate limited (429)** → wait and retry automatically
- **Config corrupted** → offer to re-run setup
- **Empty pipeline** → suggest adding leads via the Lead Qualifier
- **Ambiguous company name** → present matching options for disambiguation

---

## 10. Design Decisions

### Why Discover Existing Database First
Most freelancers already track clients somewhere. Forcing a fresh database means migration or dual systems. Augmenting their existing setup is lower friction.

### Why Augment, Don't Replace
The user's existing data and workflow are preserved. We add what's missing, never modify or remove what exists. If their stages are "New/Contacted/Won/Lost" instead of our defaults, we work with that.

### Why "Lost" Requires Confirmation
Accidental status changes are easy in chat ("mark Baker as lost" when you meant "qualified"). One extra confirmation prevents data issues.

### Why Follow-Up Is Attached to Pipeline Summary
The natural moment to surface overdue items is when the user is already looking at their pipeline. A separate check requires a separate thought. Passive awareness beats proactive nagging for v1.

### Why No Cron
Cron adds setup complexity and unprompted alerts can feel annoying. The user checks their pipeline when they want to. If they want proactive alerts, that's an easy v2 addition.

---

## 11. Claude Code Implementation Notes

### What's Fixed
- The setup flow order: token check → discover/map → augment → save config
- Schema augmentation approach (add missing properties, never modify existing)
- The `sharedFields` concept for databases with fewer columns than we need
- Config file structure (architecture doc §4.4)
- "Lost" status requires confirmation
- Follow-up check runs as part of pipeline summary, no cron in v1
- Email drafts are chat output only
- The three core functions: setup, track, alert

### What Claude Code Has Freedom On
- The exact SKILL.md structure, wording, and sections
- How to present the database list and mapping summary during setup
- The specific pipeline summary format (should be compact and scannable, but the exact layout is up to you)
- Fuzzy matching logic for company names
- Error message wording (should be helpful and actionable — follow the principle, not specific text)
- Rate limiting and retry strategy
- How to handle session-level caching of database queries
- How to adapt output for different chat platforms
- The tone and content of drafted follow-up emails
