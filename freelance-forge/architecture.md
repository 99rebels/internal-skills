# Freelance Forge — Architecture Document

**Version:** 0.1 — Design Phase
**Date:** 2026-04-25
**Author:** Cambrian (design) → Claude Code (implementation)
**Status:** Draft — pending review

---

## 1. Overview

### What It Is

Freelance Forge is a multi-skill bundle that automates the client lifecycle for freelance web designers. One install gives the agent four workflow skills: lead qualification, proposal generation, project onboarding, and pipeline tracking — all connected through a Notion workspace.

### Target User

Freelance web designers and small web design studios (1-3 people). They use Notion (or are willing to), hate admin work, and want to spend more time designing and less time managing leads, writing proposals, and tracking where clients are in the pipeline.

### The Problem

Every freelancer does the same repetitive work: research a lead, score whether they're worth pursuing, write a proposal, set up the project, track where everyone is, remember to follow up. It's not creative work. It's process work. Agents are perfect for process work.

### What Makes This Different

- **Workflow, not tool.** Each sub-skill is independently useful, but together they form a complete pipeline. No other bundle on ClawHub does this.
- **Schema-adaptive.** Works with the user's existing Notion setup instead of forcing a specific database structure.
- **Agent assists, never replaces.** The human is the designer and the relationship holder. The agent handles the process.

---

## 2. Architecture Principles

### 2.1 Notion Is the Single Source of Truth

All persistent data lives in Notion. There are no shared state files between sub-skills. When Lead Qualifier finishes, it writes to Notion. When Proposal Builder starts, it reads from Notion. The database is the communication layer.

**Why:** Eliminates state management complexity. The user can see and edit everything. No sync issues. No file corruption. Works across sessions naturally.

### 2.2 Each Sub-Skill Works Standalone

The install script places each sub-skill in a standard skills/ directory. Each has its own SKILL.md with a description that makes it independently discoverable by the skill matcher. A user can install the bundle and only ever use the Lead Qualifier if they want.

**Why:** The skill matcher scans SKILL.md descriptions. If a sub-skill is buried in a nested folder, it won't be triggered when the user says "qualify this lead" three weeks later.

### 2.3 Schema-Adaptive, Not Schema-Imposed

On first run, the Pipeline Tracker discovers the user's existing Notion database schema and maps our concepts (status, lead score, dates) to their field names. If they don't have a pipeline database, we create one with sensible defaults.

**Why:** "Works with your existing setup" is more attractive than "set up our specific database structure." Zero friction onboarding.

### 2.4 Agent Drafts, Human Decides

The agent never sends emails, never creates invoices, never commits to deadlines, never contacts clients directly. It drafts emails for review. It suggests follow-ups. It flags overdue proposals. The human clicks send.

**Why:** Trust boundary. The freelancer's client relationships are their most valuable asset. The agent should support those relationships, not risk them.

### 2.5 Lightweight Assets Only

The agent generates text-based, structured, verifiable assets: project briefs, checklists, sitemaps, email drafts, proposal documents. It does NOT generate logos, brand guidelines, design mockups, or any visual creative work.

**Why:** LLMs are good at structured text. They are not good at visual design. Generating bad creative work is worse than generating none.

---

## 3. Data Flow

### 3.1 The Client Lifecycle

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌────────────────┐
│   Lead      │     │   Proposal       │     │   Onboarding     │     │   Active       │
│   Qualifier │────▶│   Builder        │────▶│   (Project       │────▶│   Project      │
│             │     │                  │     │    Onboarder)     │     │   + Tracker    │
└─────────────┘     └──────────────────┘     └──────────────────┘     └────────────────┘
     │                      │                        │                        │
     ▼                      ▼                        ▼                        ▼
  Notion Pipeline DB — one row per lead, updated at each stage
```

### 3.2 Data Flow Per Stage

**Stage 1: Lead Qualification**
- **Input:** Company name, website URL, or domain
- **Process:** Web research (company site, social, tech stack, site quality)
- **Output:** Qualification score (1-10), research notes, added to Notion pipeline as "Lead"
- **Notion writes:** New page in pipeline database (Company Name, Website, Lead Score, Research Notes, Status = Lead)

**Stage 2: Proposal Generation**
- **Input:** Discovery call notes (user provides), pipeline data (read from Notion)
- **Process:** Combines research + discovery → scoped proposal (deliverables, timeline, pricing)
- **Output:** Proposal document (markdown), pipeline status updated to "Proposal Sent"
- **Notion reads:** Lead's pipeline row (research notes, score, budget range)
- **Notion writes:** Proposal Summary, Proposal Date, Status = Proposal Sent

**Stage 3: Project Onboarding**
- **Input:** Client name (from pipeline), confirmed scope
- **Process:** Creates Notion project database, generates project brief + onboarding checklist + sitemap draft
- **Output:** Notion project database, project brief doc, checklist, sitemap
- **Notion reads:** Pipeline row for client details
- **Notion writes:** New project database, links project to pipeline row, Status = Active

**Stage 4: Pipeline Management**
- **Input:** User requests ("show my pipeline", "update Acme to Active")
- **Process:** Reads pipeline database, provides summaries, flags overdue items, updates statuses
- **Output:** Pipeline summary, status updates, follow-up reminders
- **Notion reads:** Pipeline database (filtered views)
- **Notion writes:** Status updates, follow-up dates

### 3.3 Cross-Stage Data Dependencies

```
Lead Qualifier creates the pipeline row.
    ↓
Proposal Builder reads that row for research context.
    ↓
Project Onboarder reads that row for client details + links the new project DB.
    ↓
Pipeline Tracker monitors all rows for overdue items and status consistency.
```

No sub-skill reads another sub-skill's output files. Everything flows through Notion.

---

## 4. Notion Integration

### 4.1 Schema Discovery

On first run of the Pipeline Tracker (or any sub-skill that needs Notion access):

1. **Check for existing config** — if `freelance-forge-config.json` exists in the workspace, load the schema mapping and skip discovery.
2. **If no config:** Ask the user: "Do you have an existing client pipeline or CRM database in Notion?"
3. **If yes:** User provides database ID or name → agent fetches schema via Notion API (`GET /databases/{id}`).
4. **Agent identifies field mappings** by inspecting property types and names:
   - Title property → Company Name
   - Select property with status-like values → Status field
   - Number property → Lead Score
   - Date properties → Proposal Date, Follow-up dates
   - Rich text / textarea properties → Research Notes, Discovery Notes
   - URL property → Website
   - Email property → Contact Email
5. **Present mapping to user:** "Here's how I'd map your database fields:" → user confirms or adjusts.
6. **Save config** to `freelance-forge-config.json`.

### 4.2 Default Pipeline Schema

If the user doesn't have an existing database, create one with these properties:

| Property | Type | Purpose |
|---|---|---|
| Company Name | title | Client/lead identifier |
| Website | url | Company website |
| Contact Name | rich_text | Primary contact |
| Contact Email | email | Primary contact email |
| Status | select | Pipeline stage |
| Lead Score | number | Qualification score (1-10) |
| Budget Range | select | Estimated budget tier |
| Service Type | multi_select | Type of project |
| Source | select | How they found us |
| Research Notes | rich_text | From Lead Qualifier |
| Discovery Notes | rich_text | From user (post-call) |
| Proposal Summary | rich_text | From Proposal Builder |
| Proposal Date | date | When proposal was sent |
| Last Follow-Up | date | Most recent follow-up |
| Next Action | rich_text | What to do next |
| Project Link | relation | Links to project database |

**Default Status options:** Lead → Qualified → Proposal Sent → Onboarding → Active → Complete → Lost

### 4.3 Default Project Schema

Created per-client during onboarding:

| Property | Type | Purpose |
|---|---|---|
| Task Name | title | Individual task/milestone |
| Status | select | Task status |
| Priority | select | High / Medium / Low |
| Due Date | date | Deadline |
| Assignee | people | Who's responsible |
| Notes | rich_text | Task details |
| Deliverable | checkbox | Is this a deliverable? |

### 4.4 Configuration File

Stored at `~/.openclaw/workspace/freelance-forge-config.json`:

```json
{
  "notion": {
    "pipelineDatabaseId": "notion-db-id",
    "projectsDatabaseId": null,
    "fieldMappings": {
      "companyName": { "property": "Name", "type": "title" },
      "status": { "property": "Stage", "type": "select", "values": ["Lead", "Qualified", "Proposal Sent", "Onboarding", "Active", "Complete", "Lost"] },
      "leadScore": { "property": "Score", "type": "number" },
      "researchNotes": { "property": "Notes", "type": "rich_text" },
      "discoveryNotes": { "property": "Discovery", "type": "rich_text" },
      "proposalSummary": { "property": "Proposal", "type": "rich_text" },
      "proposalDate": { "property": "Sent Date", "type": "date" },
      "lastFollowUp": { "property": "Follow Up", "type": "date" },
      "nextAction": { "property": "Next", "type": "rich_text" },
      "website": { "property": "URL", "type": "url" },
      "contactEmail": { "property": "Email", "type": "email" },
      "budgetRange": { "property": "Budget", "type": "select" },
      "serviceType": { "property": "Service", "type": "multi_select" },
      "projectLink": { "property": "Project", "type": "relation" }
    }
  },
  "preferences": {
    "currency": "GBP",
    "followUpDays": 5,
    "proposalTemplate": "default"
  }
}
```

This file is the bridge between our abstract concepts and the user's actual Notion setup. Every sub-skill reads this file to know which Notion properties to read/write.

### 4.5 Notion API Approach

- Use the official Notion API (bearer token auth)
- The user provides their own Notion integration token during setup
- Token stored in OpenClaw credentials (not in the config file or code)
- API calls through simple Python scripts using `requests` (no heavy SDK)

---

## 5. Sub-Skill Architecture

### 5.1 Lead Qualifier

**Trigger phrases:** "qualify this lead", "research this company", "score this prospect"

**Input:** Company name, website URL, or domain

**Process:**
1. Research the company: website content, tech stack (if detectable), social presence, industry
2. Assess fit: do they need web design services? Are they the right size? Is there budget signal?
3. Score 1-10 with brief reasoning
4. Write to Notion pipeline (new row with research notes)
5. Offer to draft a qualification summary or follow-up email

**Output:**
- Qualification score + reasoning (displayed to user)
- New Notion pipeline row
- Optional: draft email for first contact

**Notion interaction:**
- Reads config for field mappings
- Creates new page in pipeline database
- Writes: Company Name, Website, Lead Score, Research Notes, Status = Lead

**Edge cases:**
- Very little web presence → flag as "limited info, manual research recommended"
- Company is clearly too small/large for freelancer scope → note in score reasoning
- Already exists in pipeline → alert user, offer to update existing row instead

---

### 5.2 Proposal Builder

**Trigger phrases:** "build a proposal", "write a proposal for", "create proposal from discovery"

**Input:** Client name (to look up in pipeline) + discovery call notes (user pastes or references a file)

**Process:**
1. Read the client's pipeline row for context (research notes, lead score, budget range, service type)
2. Combine pipeline data + discovery notes
3. Generate scoped proposal:
   - Executive summary (why this project, what problem we're solving)
   - Scope of work (specific deliverables, what's included, what's not)
   - Timeline (phases, milestones, estimated dates)
   - Pricing (broken down by deliverable or phase)
   - Terms (revisions, payment schedule, assumptions)
4. Save proposal as markdown file
5. Update pipeline: Proposal Summary, Proposal Date, Status = Proposal Sent

**Output:**
- Proposal markdown file
- Pipeline status updated
- Optional: draft email with proposal attached/linked

**Notion interaction:**
- Reads: client's pipeline row
- Writes: Proposal Summary, Proposal Date, Status

**Edge cases:**
- No discovery notes provided → prompt user to provide them, offer to generate a discovery template
- No pipeline row for this client → suggest running Lead Qualifier first, or create a minimal row
- Pricing: agent should present ranges based on service type and scope, not exact figures. The freelancer sets the final price.

---

### 5.3 Project Onboarder

**Trigger phrases:** "set up project for", "onboard this client", "start project"

**Input:** Client name (from pipeline)

**Process:**
1. Read the client's pipeline row for project details
2. Create a Notion project database for this client
3. Generate project brief:
   - Client overview
   - Project scope (from proposal/discovery)
   - Key contacts
   - Timeline and milestones
   - Technical requirements (hosting, CMS, integrations)
4. Generate onboarding checklist:
   - Assets needed (logos, brand guidelines, content, photos, hosting access, domain access)
   - Accounts to set up (hosting, CMS, analytics, email)
   - Stakeholder contacts
   - Preferences (color preferences, reference sites, competitor sites)
5. Generate sitemap/IA draft from discovery notes
6. Link project database to pipeline row
7. Update pipeline Status = Active

**Output:**
- Notion project database (linked to pipeline)
- Project brief (markdown or Notion page)
- Onboarding checklist (markdown or Notion page)
- Sitemap/IA draft
- Optional: draft welcome email with checklist for client

**Notion interaction:**
- Reads: client's pipeline row
- Creates: new project database in Notion
- Writes: updates pipeline row with project link and status

**Edge cases:**
- Pipeline row missing proposal data → use whatever's available, flag gaps
- Client already has a project database → ask if user wants to use existing or create new
- Very large project → suggest phased onboarding (brief first, detailed sitemap later)

---

### 5.4 Pipeline Tracker

**Trigger phrases:** "show my pipeline", "pipeline update", "update [client] to [status]", "any overdue follow-ups"

**Input:** Various — status updates, pipeline queries, follow-up requests

**Process:**
1. **Pipeline summary:** Read all pipeline rows, group by status, present as a digest
2. **Status update:** Change a specific client's pipeline status
3. **Follow-up check:** Compare Proposal Date / Last Follow-Up to current date, flag items overdue by configured threshold (default 5 days)
4. **Follow-up draft:** For overdue items, offer to draft a follow-up email using the client's pipeline data
5. **Setup:** On first run, discover or create the pipeline database schema (see §4.1)

**Output:**
- Pipeline digest (grouped by status, with key details)
- Status updates written to Notion
- Overdue follow-up alerts
- Optional: draft follow-up emails

**Notion interaction:**
- Reads: full pipeline database (or filtered queries)
- Writes: status updates, follow-up dates
- Creates: pipeline database (if new setup)

**Edge cases:**
- Empty pipeline → "No leads in pipeline. Run Lead Qualifier to add your first lead."
- Many overdue items → prioritize by lead score
- Status inconsistency (e.g., "Active" but no linked project) → flag to user

---

## 6. Shared Components

These are utilities referenced by multiple sub-skills, not sub-skills themselves.

### 6.1 Notion API Helper

A Python module that handles:
- Reading the config file for database IDs and field mappings
- Creating pages in Notion databases
- Updating pages (changing status, adding notes)
- Querying databases (filter by status, sort by date)
- Fetching database schema for discovery

### 6.2 Web Research Helper

Used by Lead Qualifier:
- Fetch and parse a company's website
- Extract basic info (company description, services, contact info)
- Detect tech stack indicators (CMS, hosting, frameworks)
- Find social media profiles

### 6.3 Config Manager

Used by all sub-skills:
- Load `freelance-forge-config.json`
- Validate that required fields exist
- Provide sensible defaults for missing optional fields
- Handle first-run setup (no config exists yet)

### 6.4 Template System

Used by Proposal Builder and Project Onboarder:
- Read template markdown files from `references/`
- Inject dynamic data (company name, dates, scope details)
- Output completed documents

Templates are starting points, not rigid forms. The agent should adapt content based on the specific client context, not fill in blanks mechanically.

---

## 7. Bundle Structure

### 7.1 File Layout

```
freelance-forge/
├── openclaw.bundle.json          # Bundle manifest
├── openclaw-install.sh           # Install script
├── README.md                     # User-facing documentation
│
├── skills/
│   ├── lead-qualifier/
│   │   └── SKILL.md              # Lead qualification skill
│   ├── proposal-builder/
│   │   └── SKILL.md              # Proposal generation skill
│   ├── project-onboarder/
│   │   └── SKILL.md              # Project onboarding skill
│   └── pipeline-tracker/
│       └── SKILL.md              # Pipeline management skill
│
├── scripts/
│   ├── notion_api.py             # Notion API helper module
│   ├── web_research.py           # Web research helper
│   ├── config_manager.py         # Config file manager
│   └── templates.py              # Template rendering
│
└── references/
    ├── proposal-templates/
    │   └── default.md            # Default proposal template
    ├── email-drafts/
    │   ├── welcome.md            # Client welcome draft
    │   ├── asset-request.md      # Asset request draft
    │   ├── follow-up-proposal.md # Proposal follow-up draft
    │   └── project-kickoff.md    # Project kickoff draft
    ├── onboarding-checklists/
    │   └── default.md            # Standard onboarding checklist
    └── pipeline-schema/
        └── default.md            # Default pipeline database schema reference
```

### 7.2 Bundle Manifest

```json
{
  "name": "freelance-forge",
  "displayName": "Freelance Forge — Lead to Launch",
  "version": "1.0.0",
  "description": "Complete freelance web designer toolkit — qualify leads, generate proposals, onboard clients, and track your pipeline. All connected through Notion.",
  "type": "bundle",
  "bundle": {
    "format": "skill-collection",
    "skills": [
      {
        "name": "lead-qualifier",
        "path": "skills/lead-qualifier/SKILL.md",
        "description": "Research and score prospective clients"
      },
      {
        "name": "proposal-builder",
        "path": "skills/proposal-builder/SKILL.md",
        "description": "Generate scoped proposals from discovery notes"
      },
      {
        "name": "project-onboarder",
        "path": "skills/project-onboarder/SKILL.md",
        "description": "Set up Notion projects, briefs, and checklists"
      },
      {
        "name": "pipeline-tracker",
        "path": "skills/pipeline-tracker/SKILL.md",
        "description": "Notion CRM setup and pipeline management"
      }
    ],
    "scripts": [
      "scripts/notion_api.py",
      "scripts/web_research.py",
      "scripts/config_manager.py",
      "scripts/templates.py"
    ]
  },
  "install": {
    "script": "openclaw-install.sh"
  }
}
```

### 7.3 Install Script Behavior

The `openclaw-install.sh` script should:

1. Copy each sub-skill's SKILL.md to the user's skills directory (standalone, discoverable)
2. Copy shared scripts to a `freelance-forge/` directory within the skills folder
3. Copy reference files (templates, checklists) alongside the scripts
4. Print setup instructions (how to get a Notion API token, how to run first-time setup)
5. Do NOT create the Notion database — that happens on first run of Pipeline Tracker
6. Do NOT ask for credentials — those are handled per-sub-skill at runtime

---

## 8. Design Decisions

### Why Notion Over Alternatives
- Most freelancers already use it (or can start for free)
- Flexible database structure (we don't impose a rigid schema)
- API is well-documented and reliable
- Visual — users can see their pipeline as a Kanban board, table, calendar
- No additional cost (Notion free tier is sufficient)

### Why Drafts, Not Sends
- Client relationships are the freelancer's most valuable asset
- An agent sending an email to the wrong person, with wrong info, or at the wrong time could damage a relationship permanently
- Drafting is valuable (saves time writing) without the risk of sending

### Why Each Sub-Skill Standalone
- The skill matcher can only find skills in the standard skills/ directory
- Nested sub-skills would be invisible to the agent after the bundle is installed
- Users should be able to use just one piece if that's all they need

### Why No Invoice Generation (v1)
- Invoices involve money. Getting them wrong has real consequences.
- Requires payment API integration (Stripe, Xero, GoCardless) which is a separate scope.
- The pipeline tracker shows where clients are — the freelancer can generate invoices themselves using the pipeline data as reference.

### Why No Automated Scheduling
- Automated follow-up reminders are fine ("flag overdue items"). Automated actions (send email after 5 days) cross the trust boundary.
- The agent should inform and suggest, never act autonomously on client communication.

### Why Schema-Adaptive
- Forcing a specific Notion structure means every user has to either migrate or maintain two databases.
- Most freelancers who'd use this already have a Notion setup. Asking them to change it is friction.
- Schema discovery is a one-time setup that then works transparently.

---

## 9. Constraints & Boundaries

### The Agent Must Never
- Send emails or messages to clients
- Generate or modify invoices or financial documents
- Commit to deadlines, pricing, or scope on behalf of the freelancer
- Access client accounts (Notion, hosting, email) directly
- Delete data from the user's Notion workspace
- Share client information across different leads/clients

### What Requires User Confirmation
- Creating a new Notion database (confirm name, confirm workspace)
- Changing a lead's status to "Lost" (irreversible signal)
- Any action that writes to the user's Notion workspace (except status updates which are routine)
- First-time schema mapping (user must confirm field mappings)

### Scope Boundaries
- Single freelancer / small studio (1-3 people), not enterprise
- Web design projects only (not general freelancing, not app development)
- Notion as the only supported workspace tool (no Airtable, Monday, Trello integration in v1)
- English language only (v1)

---

## 10. Implementation Notes for Claude Code

### General Guidance
- Each SKILL.md should be self-contained — it should work if installed alone, without the other sub-skills present
- Shared scripts should handle graceful degradation (if config file doesn't exist, prompt for setup instead of crashing)
- Keep Notion API calls minimal — fetch what's needed, don't pull entire databases when a filtered query works
- All user-facing output should be concise and actionable — freelancers are busy, they want the answer, not a wall of text
- Error handling should suggest the fix, not just report the error ("Notion token not found. Run `export NOTION_TOKEN=...` or add it to your credentials.")

### What Claude Code Has Freedom On
- Exact SKILL.md structure and wording (follow the SKILL.md standard, but the specific sections and phrasing are up to you)
- Script implementation details (language, libraries, error handling approach)
- Template content and structure
- How to present pipeline summaries and digests
- The specific questions asked during first-run setup
- How to handle edge cases not explicitly listed above

### What Should Stay Fixed
- The four sub-skills and their responsibilities (§5)
- Notion as the single source of truth (§2.1)
- Schema-adaptive approach (§4.1)
- Draft-only email policy (§2.4)
- The constraints and boundaries (§9)
- The config file structure (§4.4)
- Each sub-skill working standalone after install

---

## 11. Future Considerations (v2+)

- **Xero/Stripe invoice generation** — read pipeline data, generate invoices in accounting software
- **Calendar integration** — detect discovery call scheduling, deadline tracking
- **Multi-provider pipeline** — support Airtable, Monday.com, Google Sheets as alternatives to Notion
- **Automated follow-up sequences** — configurable, user-approved sequences (not autonomous)
- **Portfolio case study generator** — after project completion, generate a case study from project data
- **Retention/upsell suggestions** — based on completed project history, suggest relevant additional services
- **Multi-language support**
- **Agency-scale** — multiple team members, role-based views, assignment tracking
