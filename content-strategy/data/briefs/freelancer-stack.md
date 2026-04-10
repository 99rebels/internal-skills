# Research Brief: 5 Free Agent Skills That Replace Your Entire Freelancer SaaS Stack

## Topic & Angle

**Working title:** 5 Free Agent Skills Every Freelancer Should Install
**Format:** Listicle
**Why now:** Freelancers are drowning in SaaS subscriptions ($100-200+/mo) that don't integrate with each other. The agent skills ecosystem on ClawHub (13,000+ skills) has matured enough to offer credible replacements for the core freelancer workflow — email, meetings, proposals, tasks, and invoicing — all unified under one agent.
**The story:** A freelancer's credit card is a graveyard of productivity subscriptions. Each tool solves one problem, but together they create a worse problem: fragmentation. You're the integration layer — manually copying data between apps. These 5 free ClawHub skills replace that fragmented stack with a single, unified agent that understands context across all of them.
**Target audience:** Freelancers, agency owners, independent consultants, solo professionals. People who pay for multiple SaaS tools and feel the pain of switching between them daily.

---

## Skills Tested

| # | Skill | Slug | Downloads | Stars | Installs | Code or Instructions? |
|---|-------|------|-----------|-------|----------|----------------------|
| 1 | GOG | gog | 147,434 | 819 | 3,303 | Code (Go CLI, `gog` binary) |
| 2 | AI Meeting Notes | ai-meeting-notes | 7,634 | 15 | 54 | Instruction-only |
| 3 | AI Proposal Generator | ai-proposal-generator | 3,693 | 7 | 14 | Instruction-only (HTML/CSS templates) |
| 4 | Task Planner | task-planner | 1,828 | 2 | 20 | Code (bash + Python script) |
| 5 | Invoice Extractor | invoice-extractor | 25 | 0 | 0 | Code (Python script, 580+ lines) |

**Note:** Invoice Extractor is our own skill (rebels/invoice-extractor, published under "99rebels"). Very new (published today), so low download numbers. But thoroughly tested — 100% accuracy on 8 test documents. Be transparent about this in the post.

---

## Skill 1: GOG — Your Entire Google Workspace, Conversationally

**Install:** `clawhub install gog`

### What It Claims
Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

### What It Actually Does
A Go-based CLI tool (`gog`) that provides unified access to Google Workspace services. After a one-time OAuth setup (requires a Google Cloud project + OAuth credentials), it gives your agent the ability to:

- **Gmail:** Search emails, read, draft, and send. Uses `gog gmail search`, `gog gmail send`.
- **Calendar:** List events, create events, check availability across calendars.
- **Drive:** Search files, manage documents.
- **Contacts:** List and search contacts.
- **Sheets:** Read, write, append, and clear spreadsheet cells. Full JSON support for values.
- **Docs:** Export documents to text, read content.

The skill is a thin SKILL.md wrapper around the `gog` CLI binary (installed via Homebrew: `brew install steipete/tap/gogcli`). All actual functionality is in the binary. The SKILL.md provides agent instructions for common commands and usage patterns.

### Security Assessment
- **Code review:** The SKILL.md is minimal (just command references). The actual binary is from a well-known developer (Peter Steinberger, 58K+ GitHub followers, creator of PSPDFKit). Open source.
- **Network calls:** Connects only to Google APIs via OAuth2. No third-party servers.
- **File access:** Reads/writes only to specified paths (Google API responses to stdout, files you explicitly target).
- **Companion skills:** None.
- **Safety verdict:** ✅ Safe. Battle-tested (147K downloads, 819 stars), from a reputable developer.

### Pros
- Most popular productivity skill on ClawHub by a wide margin
- Covers 6 Google services in one tool — no need for separate integrations
- Real code, not just instructions — reliable and deterministic
- By a well-known, trusted developer
- Enables conversational email triage, scheduling, and document management

### Cons
- Requires OAuth setup (Google Cloud project, OAuth client credentials) — not trivial for non-technical users
- Requires the `gog` binary to be installed (via Homebrew)
- No built-in intelligence — it's a CLI wrapper, the agent provides the "smart" layer
- Google account required (it doesn't replace Google, just gives agent access to it)

---

## Skill 2: AI Meeting Notes — Client Call Notes in 10 Seconds

**Install:** `clawhub install ai-meeting-notes`

### What It Claims
"Messy notes → Clear action items. Instantly." Paste any meeting notes, transcript, or text and get summaries, action items with owners and deadlines, auto-saved and searchable.

### What It Actually Does
This is an **instruction-only skill** — no code, just a comprehensive SKILL.md that tells the agent how to process meeting notes. It's extremely well-crafted and specific:

- **Input:** Any text — messy handwritten notes, Otter.ai/Fireflies transcripts, Zoom exports, email threads, Slack conversations, VTT/SRT subtitle files.
- **Processing:** The agent extracts: meeting title, date, attendees, summary (2-3 sentences), action items (with @owner and deadline), decisions made, open questions, next steps.
- **Output format:** Strict single-message format with numbered action items, a summary card, and a prompt to add items to a to-do list.
- **File saving:** Creates `meeting-notes/YYYY-MM-DD_topic.md` files in the workspace.
- **To-do tracking:** Built-in task tracker that manages `todo.md` — supports "done 3", "show todos", "todo check" (daily review), overdue alerts, filtering by owner.
- **Search:** Can reference previous meetings by topic, owner, date range, or keyword.
- **Customization:** Optional `PREFERENCES.md` file for output format, sections to include, action item style, etc.
- **Examples:** Includes two detailed input/output examples (transcript and messy notes).

The skill includes example files (input-transcript.md, input-messy-notes.md, output-example.md) and templates (TODO-template.md, PREFERENCES-template.md).

### Security Assessment
- **Code review:** No code at all — pure instruction. No scripts, no binaries.
- **Network calls:** None (instructions only).
- **File access:** Creates `meeting-notes/` directory and `todo.md` in workspace. No access to files outside expected paths.
- **Companion skills:** None explicitly required, but references `ai-daily-briefing` as an optional integration.
- **Safety verdict:** ✅ Safe. Instruction-only, no code execution.

### Pros
- Zero setup — just paste notes and go
- Exceptionally well-documented SKILL.md with strict output format enforcement
- Built-in to-do tracker eliminates need for a separate task app
- Works with any text input — transcripts, messy notes, email threads, Slack exports
- Searchable archive of past meetings with owner/action item filtering
- By the same author as AI Proposal Generator (they integrate)

### Cons
- No audio recording — you still need to take notes or use a transcription tool
- No real-time meeting bot (unlike Otter.ai/Fireflies which join calls automatically)
- Instruction-only means quality depends entirely on the LLM following the instructions
- No calendar integration for scheduling follow-ups (would need to pair with GOG)

---

## Skill 3: AI Proposal Generator — From Meeting Notes to Signed Proposals

**Install:** `clawhub install ai-proposal-generator`

### What It Claims
Generate professional HTML proposals from meeting notes. 5 styles (Corporate, Entrepreneur, Creative, Consultant, Minimal), 6+ color themes, Design Wizard for custom templates. Integrates with ai-meeting-notes.

### What It Actually Does
An instruction-only skill with **real HTML/CSS templates**. The workflow:

1. **Context gathering:** Searches `meeting-notes/` for client name, checks for client history, loads pricing from `proposals/SERVICES.md`.
2. **Draft generation:** Creates a markdown draft using one of 5 style templates.
3. **Editing:** Supports "edit [section]", "make it more formal", "change price to $5,000".
4. **Finalization:** Generates a polished HTML file using a base template + CSS theme.

**Templates (5 styles):**
- **Corporate:** Formal, structured — 11 sections (Cover, Executive Summary, Company Overview, etc.). Best for enterprise/B2B.
- **Entrepreneur:** Bold, direct — 7 sections (The Problem, The Solution, What You Get, etc.). Best for startups/SMBs.
- **Creative:** Visual, portfolio-focused — 9 sections (The Vision, Your Challenges, The Work, etc.). Best for agencies/designers.
- **Consultant:** Advisory, expertise-led — 9 sections (Situation Analysis, Key Challenges, Engagement Options, etc.). Best for consultants/coaches.
- **Minimal:** Clean, no-fluff — 6 sections (Project Overview, Scope, Timeline, Investment, Terms, Accept). Best for freelancers/quick quotes.

**CSS Themes (6):** Ocean Blue, Ember Orange, Forest Green, Slate Dark, Royal Purple, Trust Navy. Each is a well-crafted CSS file with CSS custom properties, gradients, and responsive design.

**HTML template:** A professional `proposal-template.html` with:
- Responsive layout (800px max-width, mobile breakpoints)
- Print styles (clean page breaks, hidden CTA buttons)
- 5 style classes (`.proposal-corporate`, `.proposal-entrepreneur`, etc.) with distinct typography
- Google Fonts integration (Inter, Playfair Display, JetBrains Mono)
- CSS theme injection via `{{theme_css}}` placeholder
- Mustache-style templating for content

**Design Wizard:** A 6-step guided flow for creating custom templates (business type → clients → tone → sections → style → color theme).

**Integration with ai-meeting-notes:** Explicitly pulls context from `meeting-notes/` folder. The "proposal from [file]" trigger reads meeting notes to extract client needs, pain points, budget signals.

### Security Assessment
- **Code review:** No executable code. Only markdown templates, CSS files, and an HTML template. All static content.
- **Network calls:** None. The HTML template references Google Fonts CDN (standard web practice).
- **File access:** Creates `proposals/` directory tree. No access to unexpected paths.
- **Companion skills:** Integrates with `ai-meeting-notes` (same author, Jeff J Hunter). Optionally references `ai-daily-briefing`.
- **Safety verdict:** ✅ Safe. Static templates only, no code execution.

### Pros
- Real HTML/CSS output — not just text, but actual professional-looking proposals
- 5 distinct styles cover most freelancer/consultant use cases
- The Minimal template is perfect for freelancers sending quick project quotes
- Explicit integration with ai-meeting-notes creates a seamless meeting → proposal pipeline
- Print-ready and PDF-exportable
- Custom theme support
- Design Wizard for non-designers

### Cons
- No e-signature or proposal tracking (unlike Proposify which shows when clients view/sign)
- No payment integration (no Stripe/PayPal buttons in proposals)
- No client portal or analytics (no open rates, time-to-sign metrics)
- HTML output requires the agent to fill Mustache-style templates — quality depends on LLM
- Google Fonts CDN dependency (minor, but requires internet for rendering)

---

## Skill 4: Task Planner — Local Task Management, Zero Cloud

**Install:** `clawhub install task-planner`

### What It Claims
Professional local task manager. Manage tasks, set priorities, track deadlines. 100% private, no cloud sync. Supports bilingual EN/CN.

### What It Actually Does
A **code-based skill** with a bash script (`scripts/script.sh`, ~150 lines) that wraps Python for JSON manipulation. Stores all data in `~/.task-planner/tasks.json`.

**Commands:**
- `add "Task text" --priority high|medium|low --due YYYY-MM-DD` — Add a task
- `list --status pending|done|all --priority high|medium|low` — List tasks with formatted table output
- `done <id>` — Mark task as complete

**Technical details:**
- Bash 4+ wrapper that calls embedded Python 3 (no external dependencies beyond standard library)
- Tasks stored as JSON array with fields: id, text, priority, status, due, created
- Auto-increments IDs
- Sorted output by priority (high→medium→low) then ID
- Priority validation (only accepts high/medium/low)
- Data directory: `~/.task-planner/` (respects `TASK_PLANNER_DIR` env var)
- MIT-0 license

**Limitations:**
- Only 3 commands (add, list, done) — no edit, no delete, no search, no categories, no tags
- No recurring tasks
- No due date reminders (just stores the date)
- Bilingual documentation (EN/CN) — some docs are primarily in Chinese
- 19 versions but the core functionality is minimal

### Security Assessment
- **Code review:** Clean bash script with embedded Python. No obfuscation. Uses `set -euo pipefail` (proper error handling). Only standard library Python.
- **Network calls:** None. Explicitly states "does NOT make any network calls or cloud sync."
- **File access:** Only reads/writes `~/.task-planner/tasks.json`. No access outside this directory.
- **Companion skills:** SKILL.md footer mentions "calendar, timer, note-taker" as related skills but no installs or imports.
- **Safety verdict:** ✅ Safe. Minimal code, no network, local-only storage.

### Pros
- Completely local — zero cloud, zero privacy concerns
- No dependencies (standard bash + Python 3)
- Clean, simple interface
- 19 versions shows active maintenance
- MIT-0 licensed

### Cons
- Very basic — only add/list/done. No edit, delete, search, or filter
- No natural language interface beyond what the agent provides
- Small user base (1.8K downloads, 2 stars)
- Bilingual docs may confuse English-only users
- ai-meeting-notes already includes a to-do tracker that's more feature-rich

**Honest assessment:** This is the weakest pick in the stack. ai-meeting-notes already has a built-in to-do tracker with more features (owner tracking, overdue alerts, filtering, daily review). Consider whether to keep task-planner or reframe the narrative to acknowledge that meeting-notes handles task tracking too. Alternatively, position task-planner as the "project-level" task management while meeting-notes handles "meeting-level" action items.

---

## Skill 5: Invoice Extractor — Turn Receipts Into Structured Expense Data

**Install:** `clawhub install invoice-extractor`

### What It Claims
Extract structured data from invoices and receipts (PDFs and images). Output JSON, CSV, or build a running expense ledger. Auto-categorize spending. Export to accounting platforms.

### What It Actually Does
A **code-based skill** with a substantial Python script (`scripts/extract.py`, ~580 lines) that handles PDF extraction, CSV ledger management, and platform-specific exports.

**Core capabilities:**
1. **PDF extraction:** Uses pdfplumber (primary) or PyPDF2 (fallback) to extract text from PDF invoices. Handles multi-page PDFs, encrypted PDFs (with password).
2. **Image invoices:** Relies on the agent's `image` tool for OCR/extraction from photos.
3. **Hybrid approach:** The script extracts raw text from PDFs, but the **agent** (LLM) does the actual parsing into structured JSON — because LLMs understand varied invoice formats better than regex.
4. **Ledger management:** Full CRUD on a CSV-based expense ledger with:
   - Add entries (with duplicate detection via SHA-256 hash of vendor+date+total)
   - View/filter entries (by date, category, vendor)
   - Edit entries (vendor, total, date, description, category, currency, subtotal, tax)
   - Delete entries (with automatic renumbering)
   - Undo last add (one-level undo)
   - Category summaries (by week/month/year)
5. **Auto-categorization:** Keyword matching against vendor/description in `expense-config.json`. Built-in categories: software, travel, office, utilities, food, professional.
6. **Platform export:** Built-in CSV export formats for Xero, FreeAgent, Wave, and generic. Custom export presets supported.
7. **Batch processing:** Scan a folder of PDFs/images, process all, present summary, confirm once.
8. **Edge cases:** Handles ambiguous dates (DD/MM vs MM/DD), missing fields, credit notes/refunds, non-invoice PDFs, very small receipts, encrypted PDFs.
9. **Backups:** Automatic rotated backups of ledger (keeps last 5).

**Data safety:**
- Always confirms with user before adding to ledger ("Add to ledger? (yes/edit/skip)")
- Duplicate detection prevents double-counting
- Date normalization to YYYY-MM-DD
- Currency normalization (€ → EUR, £ → GBP, $ → USD)
- Config file with defaults (currency: EUR, tax rate: 23%, date format: DD/MM/YYYY)

### Security Assessment
- **Code review:** Clean Python 3 code. No obfuscation. Standard library only (csv, json, hashlib, shutil, argparse, datetime, pathlib, io, re, os, sys). No external network calls. No credential handling.
- **Network calls:** None. All processing is local.
- **File access:** Reads PDFs/images from user-specified paths. Reads/writes ledger CSV in `data/` subdirectory. Reads config from skill directory.
- **Companion skills:** None.
- **Safety verdict:** ✅ Safe. Clean code, no network, no credential handling, user-confirmed writes.

### Pros
- Real, substantial code (580+ lines, well-structured)
- Hybrid approach (script for extraction, LLM for parsing) is smart — leverages strengths of both
- Duplicate detection prevents double-counting
- Export to real accounting platforms (Xero, FreeAgent, Wave)
- Edit/delete/undo commands added in v1.2.0
- Handles edge cases thoroughly (ambiguous dates, credit notes, encrypted PDFs)
- Config-driven categorization with customizable keywords
- 100% accuracy on 8 test documents (invoices + receipts in various formats)
- Batch processing for folders of receipts

### Cons
- Very new (published today) — low download numbers, no community yet
- Requires pdfplumber (`pip install pdfplumber`) for best PDF extraction
- No actual invoice creation/sending — only extraction from existing invoices
- No payment tracking (who has paid, who hasn't)
- CSV-based ledger (not a database) — fine for freelancers, not for high volume
- Auto-categorization is keyword-based, not ML-based — may miss some vendors

---

## SaaS Alternatives & Pricing

Verified April 2026 from official pricing pages.

### Email & Calendar

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| Superhuman (email) | AI-powered email client | $25/mo (Starter), $33/mo (Business) | No (14-day trial) |
| Calendly (scheduling) | Meeting scheduling links | $10/mo (Standard), $16/mo (Teams) | Yes (1 event type) |
| Gmail | Email + Calendar | $0 (personal) / $7.20/mo (Workspace) | Yes |

### Meeting Notes

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| Otter.ai | Meeting transcription + notes | ~$17/mo (Pro), ~$33/mo (Business) | Yes (300 min/mo) |
| Fireflies.ai | Meeting transcription + notes | ~$10/mo (Pro) | Yes (limited) |

### Invoicing & Expenses

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| FreshBooks | Invoicing, expenses, time tracking | $12.90/mo (Lite), $20+ (Plus) | Yes (limited) |
| Wave | Invoicing + accounting | $0 | Yes |
| Expensify | Expense tracking | $5/mo (Collect), $9/mo (Teams) | Yes (limited) |

### Task Management

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| Todoist | Task management | ~$5/mo (Pro) | Yes (5 projects) |
| Notion | All-in-one workspace | $10/mo (Plus) | Yes (limited) |
| Asana | Project management | ~$11/mo (Premium) | Yes (limited) |

### Proposals

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| Proposify | Proposal software + e-signatures | ~$49/mo (Basic) | No (14-day trial) |
| HoneyBook | Client management + proposals | $8-33/mo | No (7-day trial) |
| Canva | Design + proposals | $13/mo (Pro) | Yes (limited) |

### Combined Freelancer SaaS Stack (Typical)

| Tool | Category | Monthly Cost |
|------|----------|-------------|
| Superhuman | Email | $25 |
| Calendly | Scheduling | $10 |
| Otter.ai | Meeting notes | $17 |
| Todoist Pro | Tasks | $5 |
| FreshBooks Plus | Invoicing | $20 |
| Proposify Basic | Proposals | $49 |
| **Total** | | **$126/mo ($1,512/yr)** |

Even a modest stack (Gmail free + Calendly free + Otter free + Todoist free + FreshBooks Lite) runs ~$13/mo with significant limitations.

---

## Data Points

- **Total savings (premium stack):** ~$126/month, ~$1,512/year
- **Total savings (modest stack):** ~$13-40/month
- **Skills tested:** 5 installed, 5 code-reviewed (2 code-based, 2 instruction-only, 1 hybrid)
- **Security issues found:** 0 — all 5 skills are clean
- **Total ClawHub downloads across 5 skills:** ~160,613
- **Notable ratios:** GOG alone has 147K downloads (91% of total).

---

## Caveats

**Setup is not trivial.** These skills require OpenClaw running on a self-hosted machine. GOG requires Google Cloud OAuth setup (create project, enable APIs, get credentials). This is not a one-click install like signing up for SaaS.

**No real-time meeting recording.** ai-meeting-notes processes text you paste — it doesn't join your Zoom calls or record audio. You still need to take notes (or use Otter/Fireflies for transcription, then paste the transcript). This is a real gap vs dedicated meeting tools.

**No proposal tracking/analytics.** AI Proposal Generator creates beautiful HTML proposals but has no way to track if the client opened them, how long they spent reading, or when they signed. Proposify and HoneyBook offer these features.

**No payment processing.** None of these skills handle actual money movement. You can't collect payments, set up recurring billing, or manage client payment status through them.

**Quality depends on the LLM.** All five skills rely on the agent's LLM to produce good output. The instructions and templates are excellent, but results vary by model and context window.

**Task Planner is basic.** It's the weakest link — only 3 commands, minimal features. ai-meeting-notes already includes a superior to-do tracker. This is acknowledged honestly.

**Expense Tracker Pro is instruction-only.** It relies entirely on the agent's LLM for categorization accuracy and data persistence. If the agent's memory is cleared or context is compacted, expense data could be lost. There's no backup mechanism beyond what the agent manages.

**You still need Google Workspace.** GOG connects to Google — you need a Google account. The skills don't replace the underlying services, they give your agent access to them.

---

## Suggested Narrative Elements

### Hook Angle
"Your freelancer stack costs $126/month and none of the tools talk to each other. Here are 5 free skills that do."

Or: "You're not a productivity app collector. You're a freelancer who needs to get paid. Here's a stack that actually works together."

### The Compounding Story
The real power isn't any single skill — it's how they connect:
1. Client emails you → GOG surfaces it with context
2. You schedule a call → GOG checks both calendars, sends invite
3. You have the call → ai-meeting-notes extracts action items
4. Client wants a proposal → ai-proposal-generator reads the meeting notes and generates a professional proposal
5. You get the job, receive an invoice → invoice-extractor processes it into your expense ledger

The data flows naturally between skills. No copy-paste, no context switching, no "export from Tool A and import into Tool B."

### Contrast Point
"Something faster than a beautiful interface: not needing one at all." (From the reference article — this line works well here too.)

Or for proposals specifically: "Proposify charges $49/month for proposal templates. This skill gives you 5 templates, 6 color themes, and a Design Wizard — and it reads your meeting notes to write the content."

Or for expense tracking: "The fastest way to log an expense isn't opening an app and filling a form. It's saying 'coffee $4.75' to your agent while you're walking out of the café."

### The Honest Pivot
Acknowledge what SaaS still does better:
- Real-time meeting transcription (Otter/Fireflies join calls automatically)
- Proposal tracking and e-signatures (Proposify shows open rates)
- Payment processing (FreshBooks, Stripe)
- Mobile apps with push notifications

The skills aren't trying to replace every feature. They're replacing the **subscription layer** on top of services you already use.

### Closing Idea
"The skills are free. The agent is open source. The only cost is an afternoon of setup — and the freedom to stop paying for tools that don't talk to each other."

Or: "Five skills. Zero subscriptions. One agent that remembers what happened in the meeting, what you proposed, and how much you spent on coffee this month."

---

## Research Notes

### Why These 5 (Selection Rationale)

The original candidate pool included ~50 skills across 6 categories. Selection criteria:
1. **Real functionality** (code or excellent instructions — no vaporware)
2. **Coherent story** (skills should form a pipeline, not a random collection)
3. **Freelancer pain points** (email, meetings, proposals, tasks, invoicing)
4. **Download credibility** (GOG and ai-meeting-notes have strong numbers)

**Rejected alternatives:**
- `summarize-pro` (8.8K downloads) — good skill but too general, doesn't fit the freelancer workflow narrative
- `rebels-invoice-extractor` (25 downloads) — our own skill, excluded per credibility rules
- `smart-expense-tracker` (526 downloads) — similar to expense-tracker-pro but lower downloads
- `expense-log` (239 downloads) — interesting but too new and low downloads
- `brainz-tasks` (1.7K downloads) — requires Todoist account, adds a dependency
- `freelance-proposal-engine` (1.1K downloads) — Upwork/Fiverr focused, too narrow
- `contract-generator` (1.2K downloads) — interesting but contracts are a less frequent need than proposals
- `toggl-cli` (1.2K downloads) — requires Toggl account, doesn't reduce subscriptions
- `client-tracker` (377 downloads) — CRM for freelancers, but too new and low downloads

### Author Overlap
ai-meeting-notes and ai-proposal-generator are both by Jeff J Hunter (jeffjhunter.com). They explicitly integrate — the proposal generator pulls context from meeting notes files. This is a genuine compounding relationship, not just a marketing claim.

### GOG's Dominance
GOG has 147K downloads — more than the other 4 skills combined (13K total). It's the #1 productivity skill on ClawHub by a huge margin. This is worth mentioning as social proof.

### The Task Planner Problem
Task Planner is the weakest pick. Consider two approaches:
1. **Keep it** and position as "local-first task management" that complements meeting-notes' action items (meeting-level vs project-level)
2. **Drop it** and use only 4 skills, with meeting-notes' built-in to-do tracker covering task management

Recommendation: **Keep it** but be honest about its limitations. The 5-skill list is stronger for the listicle format, and the "local-only, zero-cloud" angle is genuinely differentiating vs Todoist/Asana.

### Potential Post Structure (for Claude)

1. **Opening:** The freelancer SaaS stack problem ($126/mo, fragmented)
2. **GOG:** Email + Calendar — the communication hub
3. **ai-meeting-notes:** Meeting notes → action items (the workflow engine)
4. **ai-proposal-generator:** Meeting notes → professional proposals (the money maker)
5. **Task Planner:** Local task management (the privacy play)
6. **Expense Tracker Pro:** Natural language expense logging (the finance layer)
7. **The Stack Effect:** How they compound together
8. **Honest Caveats:** What SaaS still does better
9. **Getting Started:** Install commands, setup overview
10. **Closing:** The cost of fragmentation vs the price of setup

### Word Count Target
2000-2500 words. Each skill gets ~200-300 words. The opening/closing/caveats get ~500 words total.
