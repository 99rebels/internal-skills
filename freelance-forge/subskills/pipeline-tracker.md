# Sub-Skill Deep Dive: Pipeline Tracker

**Parent:** Freelance Forge — `architecture.md`
**Version:** 0.1 — Design Phase
**Date:** 2026-04-25

---

## 1. Purpose

The Pipeline Tracker is the command center of Freelance Forge. It sets up and maintains a Notion database that serves as the freelancer's CRM — tracking leads from first contact through project completion. It's the first sub-skill to run (setup), and the one that ties all other sub-skills together through shared Notion data.

**It does three things:**
1. **Setup** — discover or create the Notion pipeline database, handle schema mapping
2. **Track** — show pipeline status, update lead stages, provide summaries
3. **Alert** — flag overdue proposals and follow-ups, offer to draft follow-up emails

---

## 2. When It Triggers

**Primary triggers:**
- "show my pipeline"
- "pipeline update" / "pipeline summary"
- "update [client] to [status]" / "mark [client] as [status]"
- "any overdue follow-ups" / "check my follow-ups"
- "set up freelance forge" / "set up my pipeline"

**Also triggers as a dependency:**
- Other sub-skills need the config file to exist before they can write to Notion. If the config doesn't exist, the Pipeline Tracker's setup flow should be invoked.

---

## 3. Setup Flow

This is the most important part of the Pipeline Tracker. It runs on first use and creates the foundation everything else depends on.

### 3.1 Pre-check

1. Check for `NOTION_TOKEN` env var
2. If missing: display setup instructions and stop
   ```
   To get started, you need a Notion integration token:
   
   1. Go to https://www.notion.so/my-integrations
   2. Create a new integration (name it "Freelance Forge")
   3. Copy the token
   4. Set it as an environment variable:
      export NOTION_TOKEN=ntn_xxxxxxxx
   
   Then share the pipeline database with your integration in Notion:
   - Open the database → ⋯ menu → Connections → Add connection → "Freelance Forge"
   ```

3. Check for existing config at `$FREELANCE_FORGE_CONFIG_DIR/freelance-forge-config.json`
4. If config exists: load it, confirm it's valid, skip to §3.5

### 3.2 Database Discovery

1. Ask the user: "Do you have an existing client pipeline or CRM database in Notion?"
2. **If no:** skip to §3.3 (create new)
3. **If yes:** 
   - Use the Notion API to search for databases in the user's workspace (`POST /search` with filter `type: database`)
   - Present a numbered list of available databases (name + number of properties)
   - User selects by number or name
   - Fetch the full schema of the selected database (`GET /databases/{id}`)

### 3.3 Schema Mapping

Once we have the database schema (either existing or about to be created):

1. **Inspect each property** and attempt to map it to our required concepts:

   | Our Concept | Look For (property types + name heuristics) |
   |---|---|
   | Company Name | `title` property |
   | Status | `select` property with status-like values |
   | Lead Score | `number` property with score-like name |
   | Website | `url` property |
   | Contact Email | `email` property |
   | Research Notes | `rich_text` or `textarea` with notes-like name |
   | Discovery Notes | `rich_text` or `textarea` with discovery/intake-like name |
   | Proposal Summary | `rich_text` or `textarea` with proposal-like name |
   | Proposal Date | `date` property with proposal/sent-like name |
   | Last Follow-Up | `date` property with follow-up-like name |
   | Next Action | `rich_text` or `textarea` with action/next-like name |
   | Budget Range | `select` property with budget-like name or values |
   | Service Type | `multi_select` or `select` with service/type-like name |
   | Source | `select` with source/referral/channel-like name |
   | Contact Name | `rich_text` with name/contact-like name |

2. **Identify gaps** — which required concepts have no matching property
3. **Identify matches** — which properties were successfully mapped

4. **Present the mapping to the user:**
   ```
   Here's how I'd map your database "Client Pipeline":
   
   ✅ Name → Company Name (title)
   ✅ Stage → Status (select: New, Contacted, Proposal, Active, Done, Lost)
   ✅ URL → Website (url)
   ⚠️  Notes → Research Notes (rich_text) — will share this field for research & discovery
   ❌ Missing: Lead Score (number)
   ❌ Missing: Proposal Date (date)
   ❌ Missing: Last Follow-Up (date)
   ❌ Missing: Budget Range (select)
   
   I can add the 4 missing columns to your existing database. 
   Your existing data and columns won't be affected.
   
   Should I go ahead?
   ```

5. **User confirms** → add missing properties via `PATCH /databases/{id}` with only the new properties in the body
6. **User declines** → save the partial mapping, note which features will be limited without the missing fields

### 3.4 Create New Database (if user doesn't have one)

1. Ask the user for a database name (default: "Client Pipeline")
2. Create the database via Notion API with the full default schema (see architecture.md §4.2)
3. Default status options: Lead → Qualified → Proposal Sent → Onboarding → Active → Complete → Lost
4. Ask the user if they want to customise the status values before we create it

### 3.5 Save Config

Write `freelance-forge-config.json`:

```json
{
  "version": "1.0.0",
  "notion": {
    "pipelineDatabaseId": "abc-123",
    "fieldMappings": {
      "companyName": { "property": "Name", "type": "title" },
      "status": { "property": "Stage", "type": "select", "values": ["New", "Contacted", "Proposal", "Active", "Done", "Lost"] },
      "leadScore": { "property": "Score", "type": "number" },
      "researchNotes": { "property": "Notes", "type": "rich_text" },
      "discoveryNotes": { "property": "Notes", "type": "rich_text" },
      "proposalSummary": { "property": "Notes", "type": "rich_text" },
      "proposalDate": { "property": "Date", "type": "date" },
      "lastFollowUp": { "property": "Follow Up", "type": "date" },
      "nextAction": { "property": "Next", "type": "rich_text" },
      "website": { "property": "URL", "type": "url" },
      "contactEmail": { "property": "Email", "type": "email" },
      "contactName": { "property": "Contact", "type": "rich_text" },
      "budgetRange": { "property": "Budget", "type": "select" },
      "serviceType": { "property": "Service", "type": "multi_select" },
      "source": { "property": "Source", "type": "select" },
      "projectLink": { "property": "Project", "type": "relation" }
    },
    "sharedFields": ["researchNotes", "discoveryNotes", "proposalSummary"]
  },
  "preferences": {
    "currency": "GBP",
    "followUpDays": 5,
    "defaultStatusOptions": ["Lead", "Qualified", "Proposal Sent", "Onboarding", "Active", "Complete", "Lost"]
  }
}
```

**Note on shared fields:** If the user's database has fewer fields than we need, some concepts may share a single field. The `sharedFields` key tracks this so other sub-skills know that "research notes" and "discovery notes" will both write to the same Notion property.

### 3.6 Post-Setup Confirmation

```
✅ Pipeline Tracker is set up!

Your database: "Client Pipeline" (connected)
Config saved to: ~/.freelance-forge/freelance-forge-config.json

You can now:
- "Show my pipeline" — see all leads grouped by stage
- "Update Acme to Qualified" — move a lead to a new stage
- "Any overdue follow-ups?" — check for leads needing attention
- "Qualify this lead: example.com" — run the Lead Qualifier (requires lead-qualifier skill)
```

---

## 4. Pipeline Summary

**Trigger:** "show my pipeline", "pipeline update", "what's in my pipeline"

### Process
1. Read all pages from the pipeline database (`POST /databases/{id}/query`)
2. Group by status value
3. For each lead, extract: Company Name, Status, Lead Score (if mapped), Proposal Date (if mapped), Last Follow-Up (if mapped)
4. Present as a compact digest

### Output Format (chat)
```
📊 Pipeline Summary — 8 leads

🔴 Proposals Sent (2)
  1. Acme Plumbing — Score: 7 — Sent 3 days ago
  2. Baker & Co — Score: 5 — Sent 8 days ago ⚠️ overdue

🟡 Qualified (3)
  3. Creative Studios — Score: 8
  4. Dublin Dental — Score: 6
  5. Green Gardens — Score: 7

🟢 Active (1)
  6. TechStart — Score: 9 — Started 2 weeks ago

⚪ Lead (2)
  7. Fresh Bakery — Score: 4
  8. Metro Hotel — Score: 6

⚠️ 1 overdue follow-up (Baker & Co — 3 days past threshold)
```

### Notes
- Sort each group by Lead Score (highest first) if mapped
- Flag any leads past the follow-up threshold
- If a status value doesn't match any of our known stages, show it under "Other"
- Keep it compact — the user scans this, they don't study it

---

## 5. Status Update

**Trigger:** "update [client] to [status]", "mark [client] as [status]", "move [client] to [status]"

### Process
1. Parse the company name and target status from the user's request
2. Search the pipeline database for a matching page (`POST /databases/{id}/query` with title filter)
3. If no match found: fuzzy search — try partial match, ask user to confirm
4. If match found: update the Status property (`PATCH /pages/{id}`)
5. Handle special cases:
   - Updating to "Lost": ask for confirmation before proceeding
   - Updating to "Active": check if a project database is linked (flag if not)

### Output
```
✅ Updated Acme Plumbing → Proposal Sent
```

Simple, one line. The user doesn't need a paragraph for a status change.

---

## 6. Follow-Up Checker

**Trigger:** "any overdue follow-ups", "check my follow-ups", "who needs a follow-up"

### Process
1. Read all pipeline pages with status "Proposal Sent" (or equivalent mapped value)
2. For each, compare `proposalDate` (or `lastFollowUp`) to current date
3. Flag any where days elapsed > `followUpDays` threshold (default: 5)
4. Sort by days overdue (most overdue first)
5. For each overdue lead, offer to draft a follow-up email

### Output
```
⚠️ Overdue Follow-Ups (2)

1. Baker & Co — 3 days overdue (proposal sent 8 days ago)
   - Score: 5, Budget: £2-5K, Service: Website Redesign
   - Draft follow-up? → "yes for Baker"

2. Fresh Bakery — 1 day overdue (proposal sent 6 days ago)
   - Score: 4, Budget: unknown, Service: New Website
   - Draft follow-up? → "yes for Fresh"
```

### Follow-Up Email Draft

If user says yes, draft a follow-up email **in chat**:
- Read the lead's full pipeline row for context (research notes, proposal summary, score)
- Generate a short, professional follow-up email (3-5 sentences max)
- Reference specific details from the proposal (shows the freelancer was paying attention)
- Never be pushy — the tone should be helpful, not desperate
- Include a clear next step ("Would it be useful to jump on a 15-min call to discuss any questions?")

---

## 7. Pipeline Digest Variants

**By status:** "show me all leads in [status]" — filtered query
**By score:** "show me my best leads" — filter by Lead Score > threshold
**By date:** "leads from this week" — filter by creation date
**Single lead:** "tell me about [client]" — fetch and display full row details

---

## 8. Notion API Calls Used

| Operation | API Call | When |
|---|---|---|
| Search databases | `POST /search` | Setup — finding user's databases |
| Get database schema | `GET /databases/{id}` | Setup — reading field structure |
| Create database | `POST /databases` | Setup — new database creation |
| Update database (add properties) | `PATCH /databases/{id}` | Setup — adding missing columns |
| Query database | `POST /databases/{id}/query` | Summary, follow-up check, status search |
| Update page | `PATCH /pages/{id}` | Status updates |
| Create page | `POST /pages` | (Not used by Pipeline Tracker — other sub-skills create pages) |

---

## 9. Shared Dependencies

**Reads from:**
- `freelance-forge-config.json` — database ID, field mappings, preferences

**Writes to:**
- `freelance-forge-config.json` — created during setup
- Pipeline database in Notion — status updates, follow-up dates

**Does NOT depend on:**
- Other sub-skills (it's the foundation, they depend on it)
- Any external services besides Notion

---

## 10. Error Handling

| Error | Response |
|---|---|
| `NOTION_TOKEN` not set | Show setup instructions (see §3.1) |
| Token invalid (401) | "Your Notion token appears to be invalid. Check it at https://www.notion.so/my-integrations" |
| Database not found | "I can't find a database with that name. Here are the available databases:" + list |
| Integration not connected to database | "Your integration doesn't have access to that database. Open it in Notion → ⋯ → Connections → Add 'Freelance Forge'" |
| Rate limited (429) | "Notion rate limited. Waiting 60 seconds and retrying..." |
| Config file corrupted | "Your config file seems corrupted. Want me to re-run setup?" |
| No leads in pipeline | "Your pipeline is empty. Add leads using the Lead Qualifier." |
| Ambiguous company name (multiple matches) | "Found 2 matches for 'Baker'. Did you mean: 1. Baker & Co, 2. Baker Street Dental?" |

---

## 11. Design Decisions Specific to This Sub-Skill

### Why Setup Asks About Existing Databases First
Most freelancers who'd use this already track clients somewhere. Forcing them to start fresh means migrating data or running two systems. Discovering their existing database and augmenting it is lower friction.

### Why "Lost" Status Requires Confirmation
Changing a lead to "Lost" is a meaningful signal. The freelancer might accidentally say "mark Acme as lost" when they meant "mark Acme as qualified." One extra confirmation prevents data loss.

### Why Follow-Up Threshold Is Configurable
5 days works for most freelancers, but some respond faster (2-3 days) and some give clients longer (7-10 days). Making it configurable via `followUpDays` in preferences means it adapts to the freelancer's style.

### Why Pipeline Summary Is Compact
The user checks their pipeline multiple times a day. A wall of text every time would be annoying. Compact format = quick scan. If they want details on a specific lead, they ask for it.

---

## 12. Claude Code Implementation Notes

### What's Fixed
- The setup flow (§3): discover → map → augment → save config
- The three core functions: setup, summary, status update, follow-up checker
- The config file structure (§3.5)
- Schema augmentation approach (add missing, never modify existing)
- "Lost" status confirmation
- Email drafts are chat output only

### What Claude Code Decides
- Exact SKILL.md wording and structure
- How to present the database list during setup
- Fuzzy matching logic for company names
- The specific follow-up email tone and structure
- How to handle rate limiting and retries
- Whether to cache database queries within a session
- How to format the pipeline summary for different chat platforms (Slack vs terminal vs Discord)
- The exact error messages (should be helpful and specific, just follow the pattern in §10)
