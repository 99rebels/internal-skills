# Research Brief: Freelance Forge — Internal Teardown

> **Classification:** Internal brief — not for publication. This is a forensic evaluation to determine whether the bundle clears the bar for a future Stack Play. Treat every finding with the same rigour as a published teardown.

---

## Topic & Angle

**Format:** Teardown (internal)
**Why now:** Bundle is at a publishable state — this evaluation determines readiness.
**Stakes:** If the bundle doesn't deliver on its claims, a Stack Play about it is dishonest. If it does, it's the strongest Stack Play candidate we've evaluated — a real, functional product with genuine freelancer value.
**Target audience:** Freelance web designers and developers running agent-powered workflows.

---

## Product Under Review

**Name:** Freelance Forge
**Price:** $19 one-time
**Author:** Internal (evaluated as unsigned per brief instructions)
**Install method:** `bash install.sh` (or `PowerShell install.ps1` on Windows)
**Code or instructions:** Hybrid — 4 SKILL.md files (agent instructions) + 3 Python shared modules + 7 reference templates + 2 install scripts
**Version tested:** Bundle source at `~/.openclaw/workspace/projects/freelance-forge/bundle/` (NOT the installed version — see critical finding §1)
**Research date:** 2026-04-28
**Environment:** Raspberry Pi 5, arm64, Linux 6.12, OpenClaw, Python 3.13

### File Inventory

| Component | Files | Lines (source) | Lines (installed) |
|---|---|---|---|
| SKILL.md files | 4 | 922 lines, 5,631 words | 1,146 lines (differs) |
| Python shared modules | 4 | 1,421 lines | 1,856 lines (differs) |
| Reference templates | 7 | 382 lines | — |
| Install scripts | 2 | 187 lines | — |
| README | 1 | 73 lines | — |
| Architecture docs (not in bundle) | 3 | 1,275 lines | — |
| Subskill design docs (not in bundle) | 4 | 1,194 lines | — |
| **Bundle total** | **18** | **~3,500** | — |

---

## What It Claims

The README makes these claims:

1. **"Handle the full pre-build workflow"** — lead qualification, proposal generation, project onboarding, and pipeline management.
2. **"Zero setup"** — install script handles everything.
3. **"No API keys"** — no external services required.
4. **"No cloud"** — everything runs locally with SQLite.
5. **"Optional Playwright"** — works without it but recommends it for JS-rendered sites.
6. **"Specifies what it could not verify"** — the bundle's differentiating claim, built into the Lead Qualifier.
7. **"One-time $19"** — no subscription.

The architecture doc adds:
- **"Four tightly composed skills"** sharing a single pipeline database.
- **"The agent is the orchestrator"** — skills don't pass data programmatically; the LLM reads context and drives the workflow.

---

## What It Actually Does

### Architecture

The bundle is a four-skill agent workflow with a shared SQLite backend:

- **Lead Qualifier** (`lead-qualifier/SKILL.md`): Researches a company via web scraping, produces a qualification report with a 1-10 fit score, writes a summary row to the pipeline DB. Uses `web_research.py` for fetching and `db_helper.py` for storage.
- **Proposal Builder** (`proposal-builder/SKILL.md`): Reads lead data from the DB, generates a proposal document from a Jinja-lite template (`templates.py`), writes the proposal to a report file and updates the lead's status.
- **Project Onboarder** (`project-onboarder/SKILL.md`): Reads lead/proposal context, generates a project brief, onboarding checklist, and sitemap from templates. Pre-populates tasks in the DB.
- **Pipeline Tracker** (`pipeline-tracker/SKILL.md`): CRUD for leads, tags, tasks, and activity log. Pipeline view, search, stale-lead detection, CSV/JSON export.

The three Python modules handle the code-heavy work:
- `db_helper.py` (955 lines): SQLite ORM-ish wrapper with CLI shim. Schema creation, migrations, CRUD, export.
- `web_research.py` (303 lines): Web fetching (Playwright + HTTP fallback), HTML parsing, company info extraction, tech stack detection, contact extraction.
- `templates.py` (156 lines): Minimal template renderer supporting `{{var}}` interpolation and `{{#section}}` blocks.

### Composition Model

The four skills share `pipeline.db` and `config.json`. They do NOT pass data to each other programmatically. The LLM reads previous outputs (qualification reports, proposals) and the DB row to provide context. This is by design — the architecture doc explicitly states "the agent is the orchestrator."

**Assessment:** This is appropriate for agent skills. The LLM is the integration layer. Programmatic composition would over-engineer something the agent handles naturally. However, it means the bundle's "tight composition" claim is aspirational rather than technical — the skills are four tools sharing a database, with the LLM providing the glue. The README implies more integration than exists in the code.

---

## Installation & Setup

**Steps taken (following the README's install script):**

1. Ran `bash install.sh` from the bundle directory.
2. Script detected `~/.claude/skills/` as the target skills directory.

**Issues encountered:**

### CRITICAL: Install script installs to wrong directory for OpenClaw

The `detect_skills_dir()` function checks for directories in this order:
1. `$HOME/.openclaw/skills/`
2. `$HOME/.claude/skills/`

OpenClaw's actual skills directory is `$HOME/.openclaw/workspace/skills/` — which is NOT checked. On Rian's machine, the script found `~/.claude/skills/` (from a previous Claude Code install) and installed the skills there instead of `~/.openclaw/workspace/skills/`. An OpenClaw-only user with no Claude Code installation would see the script fail to detect any directory and fall through to the manual prompt.

**Impact:** For OpenClaw users (the primary target), the install script either installs to the wrong place or prompts for manual input. The README's "zero setup" claim is broken for the largest agent platform.

**Time to set up:** ~3 seconds (when it works). The script is fast and idempotent. Re-running overwrites skills and shared scripts without touching data.

**What works correctly:**
- Data directory creation (`~/.freelance-forge/` with subdirectories)
- Shared script installation
- Reference template installation
- Python module verification
- Idempotent re-runs (data never touched)
- Windows PowerShell equivalent (`install.ps1`)
- `$FREELANCE_FORGE_CONFIG_DIR` env var support for custom paths
- Auto-creates SQLite database and config.json on first use

---

## Test Results

### Test 1: Web Research — Clean Modern Site (stripe.com)

**Method:** `python3 -m web_research "https://stripe.com" --no-playwright`

**Result:** ✅ Worked correctly.
- Correctly identified the site as Next.js (from `/_next/` asset signatures)
- Extracted title, meta description, 9 headings
- Found YouTube social link
- Correctly flagged: "No email or phone number found in body text"
- Correctly flagged: "No meta description tag found" — wait, this is WRONG. Stripe DOES have a meta description, and the extraction found it. Let me correct: the extraction DID find the meta description (`"Stripe is a financial services platform..."`) but the `missing` array showed `"No email or phone number found in body text"`. So meta description was NOT flagged as missing. Correct behaviour.

**Crawl test (installed version only — not in bundle):**
- Discovered 100 pages via homepage link extraction
- Crawled 4 pages (homepage + contact + services + pricing)
- Merged extraction across all pages
- Found email `sales@stripe.com` on the contact page
- Correctly reported which pages were and weren't crawled

### Test 2: Web Research — JS-Rendered SPA (react-weather-eta.vercel.app)

**Method:** Without Playwright, then with Playwright.

**Result (no Playwright):** ✅ Correctly identified as inaccessible.
```json
{
  "accessible": false,
  "notes": ["HTTP fetch returned empty/minimal body — likely a JS-rendered shell. Install Playwright for better coverage."]
}
```
Exit code 2 (signals inaccessibility to caller).

**Result (with Playwright):** ✅ Accessed successfully, rendered the JS content.
- **BUT:** The phone regex matched timestamps from the weather widget: `"2026-04-28 18"`, `"2026-04-28 21"`, `"2026-04-29 00"`, `"2026-04-29 03"` — these are NOT phone numbers.
- The installed version's `_filter_phone()` function would reject these (bare digits check), but the bundle version does NOT have this filter.

### Test 3: Web Research — Deliberately Messy Site

**Method:** Served a deliberately bad HTML file (no meta description, broken image, marquee tag, vague service descriptions, no contact form).

**Result:** ⚠️ Partial success.
- ✅ Correctly extracted the email (`joe@joesplumbing.ie`) and one phone number (`087 654 3210`)
- ✅ Correctly flagged "No meta description tag found" in the `missing` array
- ✅ Correctly tagged as "local-business" (phone + address-related keywords)
- ⚠️ Missed the second phone number (`01 234 5678`) — only captured one of two
- ⚠️ Did NOT flag: broken image, missing contact form, vague services, no about page, no pricing, marquee tag (1990s HTML indicating outdated site). The `missing` array only checks for meta description and email/phone presence.
- ⚠️ The short-content version (< 200 chars) was incorrectly flagged as a JS-rendered shell (see below).

### Test 4: Accessible Threshold

**Method:** Served a page with exactly 150 chars of text content.

**Result:** ❌ Incorrectly marked as inaccessible.
```json
{
  "accessible": false,
  "notes": ["HTTP fetch returned empty/minimal body — likely a JS-rendered shell. Install Playwright for better coverage."]
}
```
A page with 150 chars of real content gets told it's a "JS-rendered shell" — this is a misleading error message. The threshold (`len(result.text) > 200`) is too aggressive, and the fallback message assumes JS rendering when the real issue is short content. A real small business site (e.g., a tradesperson's landing page) could have < 200 chars of unique text and would be incorrectly flagged.

### Test 5: Full Pipeline Flow

**Method:** Added a lead → updated with discovery notes → set status to proposal_sent → added 6 tasks → checked activity log → viewed pipeline → exported CSV.

**Result:** ✅ Full pipeline works correctly.
- Lead created with all fields populated
- Tags attached correctly (3 tags: wordpress, local-business, food-service)
- Status transitions logged (lead → proposal_sent)
- Discovery notes and proposal summary stored
- 6 tasks created and listed
- Activity log captured 13 entries for a single lead through the pipeline
- Pipeline view correctly grouped by status
- CSV export produced clean, usable output

### Test 6: Stress Test (20+ Leads)

**Method:** Created 20 leads with randomised scores (2-9) and statuses (lead, qualified, proposal_sent, onboarding).

**Result:** ✅ Performance is solid.
- Pipeline view: 52ms
- Stale check: 54ms
- Activity log (30 days): 53ms
- Search: 54ms
- Export CSV: 54ms
- All operations well under 100ms. SQLite handles this scale easily.

### Test 7: Edge Cases

| Test | Result |
|---|---|
| Add lead with no optional args | ✅ Creates lead with null fields. Valid — some fields are optional. |
| Update non-existent lead | ✅ Clean error: `error: Lead nonexistent-id not found` |
| Duplicate lead (same company name) | ⚠️ **Creates a second lead.** No uniqueness constraint on company name. The SKILL.md says to check for duplicates before inserting, but the DB doesn't enforce it. |
| Search empty query | ⚠️ Returns all leads (LIKE match on everything). No validation. |
| Export empty pipeline | ✅ Creates empty CSV file. No crash. |
| Template with missing context vars | ✅ Renders empty string for missing vars. No crash. |

### Test 8: Install Script (Claude Code Path)

**Method:** Ran `install.sh` on a machine with `~/.claude/skills/` present.

**Result:** ✅ Installed correctly to `~/.claude/skills/` for each of the four skills. This is the correct path for Claude Code. The issue is specifically with OpenClaw's path (`~/.openclaw/workspace/skills/`), not Claude Code's path.

---

## Code Quality Assessment

### Python Modules

- **Lines of code:** 1,421 (bundle) / 1,856 (installed)
- **Language:** Python 3.10+ (uses match statements, type union syntax)
- **Dependencies:** `requests`, `beautifulsoup4` (required); `playwright` (optional, recommended)
- **Code organization:** Clean. Three modules with clear separation of concerns. Good docstrings and module-level documentation.
- **Error handling:** Good in most areas. Network failures in `web_research.py` are caught gracefully (never raises, always returns a `FetchResult`). DB operations use proper try/except. The installed version adds better error messages for foreign key violations (e.g., "Lead not found" instead of raw "FOREIGN KEY constraint failed").
- **Documentation:** Good. Every module has a module-level docstring explaining purpose, usage, and CLI invocation. The CLI shim has proper argparse help text.
- **Tests included:** ❌ No test files. No unit tests, no integration tests. This is a significant gap for a product that handles pipeline data.

### SKILL.md Files

- **Instruction quality:** Very high. Detailed step-by-step flows, explicit CLI commands with example output, clear guard clauses, honest scoring rules. The Lead Qualifier's SKILL.md is particularly well-written — the "scoring honesty rules" section and the mandatory unverified section are strong.
- **Practical or theoretical:** Highly practical. Every SKILL.md includes concrete CLI commands, example output, and edge case handling. Not aspirational — these are instructions that work if followed.

### Reference Templates

- **Quality:** Good. The proposal template covers all standard sections (scope, timeline, investment, terms). The onboarding checklist is thorough (assets, access, information, approvals). Email drafts are short and well-structured with adaptation notes.
- **Limitation:** Single template for each type. No industry-specific variants. The template renderer is minimal enough that agents can adapt on the fly, but users who want a different proposal structure would need to create their own templates.

### Install Scripts

- **Quality:** Adequate. Standard bash/PowerShell with error checking (`set -euo pipefail`). Idempotent. Clear output.
- **Bug:** OpenClaw skills directory path is wrong (see Installation & Setup).

---

## Security Assessment

**ClawHub rating:** N/A (not on ClawHub)

**Code review findings:**
- **Credential access:** ✅ None. Does not read `.env`, tokens, API keys, browser cookies, or credential files. The only credential-adjacent access is reading `$FREELANCE_FORGE_CONFIG_DIR` env var.
- **External network calls:** ✅ Only to user-provided URLs via `web_research.py`. The module fetches the exact URL the user asks it to research. No telemetry, no phone-home, no analytics. User-Agent string identifies as `FreelanceForge/1.0`.
- **File system scope:** ✅ Stays within `~/.freelance-forge/` (or `$FREELANCE_FORGE_CONFIG_DIR`). Reads from and writes to this directory tree only. Does not access files outside its scope.
- **Obfuscated code:** ✅ None. All code is readable Python. No base64, no eval(), no minification.
- **Companion skill installation:** ✅ None. The install script copies its own skills; it does not install any third-party skills or dependencies.

**Safety verdict:** ✅ Safe

**Researcher's own assessment:** This is one of the cleanest codebases I've reviewed. No red flags in any security category. The bundle does exactly what it says and nothing else. No hidden behaviour.

---

## Comparison with Alternatives

| Feature | Freelance Forge | Bonsai | HoneyBook | Dubsado | DIY (Spreadsheets) |
|---|---|---|---|---|---|
| **Lead qualification** | ✅ Automated research + scoring | ❌ Manual CRM entry | ❌ Manual CRM entry | ❌ Manual CRM entry | ❌ Manual |
| **Proposal generation** | ✅ Template-based + LLM | ✅ Template-based | ✅ Template-based | ✅ Template-based | ❌ Manual |
| **Project onboarding** | ✅ Checklists + task pre-pop | ⚠️ Basic | ⚠️ Basic | ⚠️ Basic | ❌ Manual |
| **Pipeline management** | ✅ SQLite + CLI | ✅ CRM pipeline | ✅ CRM pipeline | ✅ CRM pipeline | ⚠️ Spreadsheets |
| **Invoicing** | ❌ Not included | ✅ Built-in | ✅ Built-in | ✅ Built-in | ⚠️ Manual |
| **Payment processing** | ❌ Not included | ✅ Stripe integration | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Contract signing** | ❌ Not included | ✅ Built-in | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Scheduling** | ❌ Not included | ✅ Built-in | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Client portal** | ❌ Not included | ✅ Built-in | ✅ Built-in | ✅ Built-in | ❌ Manual |
| **Team collaboration** | ❌ Single-user | ✅ Multi-seat | ✅ Multi-seat | ✅ Multi-seat | ⚠️ Manual sharing |
| **Data ownership** | ✅ Local SQLite | ❌ Cloud | ❌ Cloud | ❌ Cloud | ✅ Local |
| **AI-powered research** | ✅ Web scraping + LLM | ❌ None | ❌ AI templates only | ❌ None | ❌ None |
| **Price** | $19 one-time | $15-59/mo | $29-109/mo | $335-525/yr | $0 |

**Pricing sources** (all fetched 2026-04-28):
- Bonsai: <https://www.hellobonsai.com/pricing>
- HoneyBook: <https://www.honeybook.com/pricing>
- Dubsado: <https://www.dubsado.com/pricing>

**Where Freelance Forge Wins:**
- **Lead qualification with automated research.** No competitor does this. The web research module genuinely gathers information about a prospect's business, tech stack, and online presence, then scores fit. This is the bundle's strongest differentiator.
- **Price.** $19 one-time vs $180-1,308/year for SaaS. Over 2 years, that's ~95-99% cheaper.
- **Data ownership.** Local SQLite means the freelancer owns their data. No vendor lock-in, no data extraction risk, no "we changed our pricing model and deleted your old projects."
- **AI-powered workflow.** The LLM integration means every output is adapted to the specific client. Proposals reference discovery call notes, not generic templates. Qualification reports highlight what's verifiable and what's not.

**Where Alternatives Still Win:**
- **Invoicing and payments.** This is the biggest gap. Bonsai, HoneyBook, and Dubsado all handle the money — invoicing, payment processing, reminders, late payment tracking. Freelance Forge doesn't touch this. A freelancer using Freelance Forge still needs a separate tool (or manual process) to get paid.
- **Contract signing.** No e-signature capability. The proposal is a markdown file, not a signable document.
- **Client portal.** Clients can't self-serve, check project status, or download deliverables.
- **Team collaboration.** Single-user by design. No multi-seat, no role-based access, no shared pipeline view.
- **Scheduling.** No calendar integration or booking system.
- **Reliability.** SaaS tools have uptime SLAs, backups, and support. Freelance Forge is a SQLite file on the freelancer's machine — if the machine dies and there's no backup, the pipeline is gone. No mention of backup strategy in the documentation.

**Fair pricing read:** At $19, Freelance Forge covers the pre-build workflow that SaaS tools either don't cover at all (lead qualification with research) or cover as part of a much more expensive package. The $19 is honestly priced for what it does. The gap is not in the pre-build workflow — it's in the post-build workflow (invoicing, payments, contracts). The bundle is a pre-build tool, not a full business management platform. The README doesn't overclaim here, which is honest.

---

## The "Specifies What It Could Not Verify" Claim — Deep Dive

This is the load-bearing claim of the bundle. The evaluation:

### Infrastructure Level (code)
The `web_research.py` module provides two mechanisms for honest reporting:
1. **`accessible` flag:** When a page can't be fetched or parsed, `accessible` is `false` with an explanatory note. The caller (LLM) is supposed to communicate this to the user, not fabricate content.
2. **`missing` array:** Lists things the page SHOULD have but doesn't (no meta description, no email, no phone). This feeds into the Unverified section of the qualification report.
3. **`confidence` field on each fact:** Every extracted fact is tagged HIGH/MEDIUM/LOW confidence, and the source section is recorded (e.g., `<title>`, `meta[description]`).

**Assessment:** The infrastructure genuinely supports honest reporting. The code doesn't fabricate — it either finds data on the page or reports that it couldn't find it.

### Behavioural Level (SKILL.md instructions)
The Lead Qualifier SKILL.md is explicit:
- "This section is NON-NEGOTIABLE. It must appear in every report." (referring to the Unverified section)
- "Never inflate the score."
- "State the reasoning."
- "Acknowledge the uncertainty."
- The subskill design doc clarifies: "The 'Unverified' section should focus on things that *should* have been verifiable but couldn't be confirmed — not obvious unknowables like budget."

**Assessment:** The instructions are strong and specific. A competent LLM will follow them. The scoring honesty rules are well-designed (the score is a single integer in the DB, but the report carries nuance).

### The Gap
The Unverified section is **written by the LLM, not enforced by code**. There is no code that checks whether the Unverified section appears in the generated report. If the LLM decides to skip it, gloss over it, or confabulate, the code won't catch it.

This is by design — the bundle is agent-driven. But it means the claim's reliability depends on:
1. The agent platform's compliance rate with SKILL.md instructions
2. The LLM's willingness to say "I don't know" (which varies by model)

**Verdict:** The claim is **well-supported by infrastructure** and **well-instructed in the SKILL.md**. For most agent platforms with competent LLMs, this works as advertised. The risk is that a weaker LLM or a less compliant agent platform might produce confident-but-wrong reports. The bundle cannot prevent this — it can only make it easy for good agents to be honest.

**Tested against a hard case:** The deliberately messy site (Test 3) — the extraction correctly identified what was there (email, phone, title) and correctly flagged what was missing (meta description). A competent LLM would produce an honest Unverified section from this output. The infrastructure did its job.

---

## Skill Composition Assessment

**Question:** Are the four skills genuinely composed, or four standalone tools sharing a database?

**Answer:** They share a database and the LLM orchestrates. This is appropriate but the README's "tight composition" language overstates it.

**Evidence:**
- The Proposal Builder's SKILL.md instructs the agent to: "Read the lead's qualification report" and "Read the lead's row from the database." It doesn't call a Proposal Builder API that receives lead data. The agent reads files manually.
- The Project Onboarder's SKILL.md instructs: "Read the lead's qualification report and the proposal" before proceeding. Again, manual file reading by the agent.
- There is no programmatic data flow between skills. Each skill reads from the DB independently.

**Is this a problem?** No — in an agent context, the LLM IS the integration layer. This is how agent skills work. The skills are well-designed for this model. The concern is only with the README's framing: "four tightly composed skills" implies more technical integration than exists. "Four skills that share a pipeline database and are designed to be used in sequence" would be more accurate.

**What would tight composition look like?** The Proposal Builder could read the qualification report path from the DB (`proposal_builder.py --from-lead <id>`), or the Pipeline Tracker could trigger the Proposal Builder when status changes. But this would over-engineer the agent workflow and reduce flexibility.

---

## Implementation Quality Across Skills

| Skill | Quality | Assessment |
|---|---|---|
| **Lead Qualifier** | **Strong** | Most complex skill. Thorough research process, honest scoring rules, clear edge case handling. The crawl feature (installed version) is a significant upgrade. Well-designed scoring criteria with weighted factors. |
| **Pipeline Tracker** | **Strong** | Comprehensive CRUD, good search, sensible activity logging. The installed version's "deep view" (§B) is a useful addition — shows full lead dossier in one view. Good confirmation requirements for destructive actions (status → lost, status → active without tasks). |
| **Proposal Builder** | **Adequate** | Mostly template-driven with agent adaptation. Works correctly. The template renderer handles the mechanics; the LLM provides the content. Less code, less complexity — appropriate for what it does. |
| **Project Onboarder** | **Adequate** | Similar to Proposal Builder. The onboarding checklist is thorough and practical. Task pre-population is useful. The sitemap generation template is a nice touch. |

**Unevenness:** The Lead Qualifier and Pipeline Tracker carry more weight (more code, more complexity, more edge case handling). The Proposal Builder and Project Onboarder are lighter — they rely more on the LLM and templates. This is not a flaw — it's the right distribution of complexity. The two most-used skills (qualify and track) are the strongest.

---

## Critical Issues (Must Fix Before Stack Play)

### 1. Install Script: Wrong OpenClaw Skills Directory
**Severity:** High — breaks "zero setup" claim for the primary target platform.
**Detail:** `detect_skills_dir()` checks `~/.openclaw/skills/` but OpenClaw uses `~/.openclaw/workspace/skills/`. On machines with Claude Code installed, it silently installs to the wrong directory.
**Fix:** Add `~/.openclaw/workspace/skills/` to the detection list, ideally as the first check.

### 2. Source/Bundle Drift
**Severity:** High — the bundle source does not match what's actually deployed.
**Detail:** The installed shared modules and SKILL.md files have diverged significantly from the bundle source. Key differences:
- `research_quality` → `data_confidence` (column rename in db_helper.py)
- `pitch_notes` column added
- Report directory structure changed: `reports/proposals/<slug>-<date>.md` → `reports/clients/<slug>/proposal-<date>.md`
- `reports/projects/<slug>/` → `reports/clients/<slug>/`
- Web research module gained: crawl mode, sitemap parsing, page discovery, phone filtering, content type checking, business page classification, multi-page merge
- Pipeline Tracker gained: deep view (§B), filtered views, enhanced follow-up drafting with context points
- Lead Qualifier updated for crawl mode
- `$SKILL_DATA_DIR` env var support added
- Foreign key error messages improved
- `templates.py` error handling improved

**Fix:** Sync the bundle source with the installed version. The installed version is the better version — it has bug fixes, new features, and better error handling.

### 3. Phone Regex False Positives (Bundle Version)
**Severity:** Medium — produces incorrect data in qualification reports.
**Detail:** The bundle's `web_research.py` uses `r"\+?\d[\d\s\-().]{7,}\d"` which matches timestamps, dates, and other digit sequences. The installed version's `_filter_phone()` function fixes this with IP rejection, date rejection, bare-digits rejection, and minimum-length filtering.
**Fix:** Include the installed version's `_filter_phone()` function in the bundle.

---

## Should-Fix Issues

### 4. Accessible Threshold Too Aggressive
**Severity:** Medium — produces misleading error messages.
**Detail:** Pages with < 200 chars of text content are flagged as "likely a JS-rendered shell" — a misleading diagnosis for genuinely short pages (small business landing pages, under-construction sites). The threshold also means a real site with minimal content gets exit code 2, which the caller interprets as "couldn't access" rather than "accessed but content was thin."
**Fix:** Lower the threshold to ~100 chars, or change the message to distinguish between "empty body" and "thin body."

### 5. Duplicate Lead Prevention
**Severity:** Low — the SKILL.md instructs the agent to check, but the DB doesn't enforce uniqueness.
**Detail:** The `leads` table has no UNIQUE constraint on `company_name`. Two leads with the same name can coexist. The SKILL.md says to check for duplicates before inserting, but if the agent skips this step (or a user interacts with the DB directly), duplicates accumulate silently.
**Fix:** Add a UNIQUE constraint on `company_name` (or `company_name + website`) and handle the IntegrityError in the `add_lead()` function.

### 6. No Tests
**Severity:** Low — the code works but has no safety net.
**Detail:** No unit tests, no integration tests. For a product that manages pipeline data (a freelancer's business data), this is a gap. A schema migration bug or a query regression could corrupt data silently.
**Fix:** At minimum, add tests for the DB schema, CRUD operations, and the web research extraction logic.

---

## What This Tells You (Candidate Synthesis)

Freelance Forge is a genuinely useful product that solves a real problem: the pre-build workflow for freelance web designers is underserved by both SaaS tools (which focus on invoicing/payments, not lead qualification) and DIY approaches (which don't scale). The bundle's strongest feature — automated lead research with honest uncertainty reporting — is something no competitor offers at any price point.

The bundle's weakness is not in what it does but in the gap between what it does and what a freelancer needs to run a full business. After the proposal is signed and the project is onboarded, the freelancer still needs invoicing, payment processing, contract signing, and client communication tools. Freelance Forge hands off at exactly the point where the freelancer's workflow gets most complicated.

The "specifies what it could not verify" claim is well-supported by infrastructure but depends on the LLM's compliance. This is the right design for an agent skill — the code provides the data, the LLM provides the judgment. But it means the bundle's reliability varies by agent platform and model.

The source/bundle drift is the most concerning finding. The installed version is significantly better than the bundle source — it has the crawl feature, phone filtering, improved error handling, and a cleaner report structure. But the bundle that a customer would download doesn't include any of these improvements. This needs to be fixed before publication.

---

## What Should You Actually Do (Candidate Action Layer)

**Before publishing a Stack Play:**
1. Fix the install script's OpenClaw path detection
2. Sync the bundle source with the installed version (the installed version is the canonical one)
3. Add the phone filter to the bundle's web_research.py
4. Consider adding tests for the DB layer

**When writing the Stack Play:**
1. Lead with the lead qualification feature — it's the bundle's strongest differentiator
2. Be honest about the gap: this is a pre-build tool, not a full business management platform
3. The pricing comparison is the strongest argument — $19 vs $300+/year for SaaS
4. Don't oversell the "tight composition" — it's four tools sharing a database with the LLM as orchestrator
5. The "specifies what it could not verify" claim is worth featuring but be precise about what it means: the code provides honest data, the LLM writes honest reports, but neither is infallible

**For Rian specifically:**
- The installed version (what you've been using) is the good version. The bundle source needs to catch up.
- Consider whether to include the crawl feature in the published bundle — it's a significant upgrade that makes the Lead Qualifier genuinely useful on modern multi-page sites.
- Consider adding a backup recommendation to the documentation — SQLite files can be lost, and the pipeline data has real business value.

---

## Verdict

**Recommendation:** ⚠️ Install with caveats

**Best for:** Freelance web designers and developers who use agent-powered workflows (OpenClaw, Claude Code) and want automated lead research, qualification scoring, and proposal generation. Solo operators who value data ownership and don't want to pay monthly for a CRM they barely use.

**Not for:** Freelancers who need invoicing, payment processing, contract signing, or client portals (use Bonsai/HoneyBook/Dubsado instead or alongside). Teams (single-user by design). Freelancers who don't use AI agents (the skills require an agent runtime).

**One-line take:** A genuinely useful pre-build workflow toolkit with the best lead qualification feature in the agent skills space, held back from a clean recommendation by an install script bug and a significant gap between the bundle source and the actually-deployed version.

**Writer guidance:** Praise the lead qualification feature and the honest-uncertainty architecture — these are the bundle's genuine strengths. Criticise the install bug (it's fixable but embarrassing for a product that claims "zero setup"). Note the source/bundle drift as a pre-publication issue, not a product flaw. The pricing comparison writes itself — $19 vs $300+/year is a strong argument. Be precise about the gap: this tool ends where the hard part of freelancing begins (getting paid). Don't call it "comprehensive" or "powerful" — call it specific and honest, because that's what it is.

---

## Caveats

1. **The bundle source evaluated here is NOT the installed version.** The installed version (what Rian has been using) is significantly more capable — it includes the crawl feature, phone filtering, and improved error handling. The evaluation above covers the bundle source because that's what a customer would download. The installed version would score higher on several criteria.

2. **The "specifies what it could not verify" claim was not tested with a live LLM flow.** The infrastructure supports honest reporting (verified via code review and module testing), but the actual Unverified section in a qualification report is written by the LLM. Testing this would require running the full Lead Qualifier skill end-to-end with an LLM, which is beyond the scope of this code-level teardown.

3. **No ClawHub inspection available.** The bundle is not on ClawHub, so download/install counts and security ratings are not available. The comparison table uses SaaS pricing, not skill ecosystem metrics.

4. **The README says "zero setup" but the install script has a bug.** The README's claim is aspirational — it would be accurate once the install script is fixed.

5. **No backup strategy documented.** A freelancer's pipeline database has real business value. The documentation doesn't mention backups, and SQLite on a single machine is a single point of failure.

6. **Single-user design.** The bundle doesn't support multi-user scenarios (shared pipeline, role-based access, team views). This is a design choice, not a flaw, but it limits the addressable market.

---

## Quotable Moments

1. **Install script output showing wrong directory:**
```
Skills directory: /home/rianoleary/.claude/skills
```
The script found Claude Code's directory instead of OpenClaw's workspace. On an OpenClaw-only machine, this would fail entirely.

2. **Phone regex matching timestamps as phone numbers:**
```json
"phones": [
  "2026-04-28 18",
  "2026-04-28 21",
  "2026-04-29 00",
  "2026-04-29 03"
]
```
A weather app's timestamps reported as contact phone numbers. The installed version's filter catches this; the bundle version doesn't.

3. **Short content page marked as "JS-rendered shell":**
```json
{
  "accessible": false,
  "notes": ["HTTP fetch returned empty/minimal body — likely a JS-rendered shell. Install Playwright for better coverage."]
}
```
150 chars of real HTML content, and the tool tells the user to install Playwright. A small business landing page would trigger this.

4. **The full pipeline activity log — 13 entries for one lead:**
```
lead_created → lead_scored → tag_added (×3) → proposal_created → status_changed → task_created (×6)
```
The activity logging is comprehensive and useful. Every action is tracked with timestamps.

5. **Crawl feature discovering 100 pages on stripe.com:**
```
Crawl source: homepage_links
Total discovered: 100
Pages crawled: 4 (homepage, contact, services, pricing)
```
The crawl feature (installed version) is genuinely useful — it discovered, prioritised, and extracted from the most relevant business pages automatically.

6. **Performance at scale:**
```
Pipeline view: 52ms
Stale check: 54ms
Activity log (30 days): 53ms
Search 'test': 54ms
Export CSV: 54ms
```
All operations under 55ms with 21 leads. SQLite is more than sufficient.

---

## Candidate Framings

**Candidate central frame:** Freelance Forge proves that agent skills can do something SaaS tools don't — genuinely automated lead research with honest uncertainty reporting — but the gap between the source code and the shipping product is a warning about the maturity of the skills-as-products category.

**Candidate hook moment:** The install script installs to the wrong directory on the primary target platform, and the bundle a customer downloads is missing features that the developer has already built and is using daily.

**Alternative frame:** At $19, Freelance Forge covers the pre-build workflow that freelancers pay $300-1,300/year for in SaaS tools — but it stops exactly where freelancing gets hardest.

**Surprise or reveal:** The "specifies what it could not verify" claim is real — the code genuinely supports honest reporting — but it's the LLM, not the code, that writes the actual Unverified section. The claim's reliability varies by agent platform and model.

**Closing candidate:** Freelance Forge is the best pre-build toolkit in the agent skills space. It's also a reminder that "install and go" still means "install, fix the install script, and go."

---

## Research Notes

### Raw Data Paths
- Bundle source: `~/.openclaw/workspace/projects/freelance-forge/bundle/`
- Installed shared modules: `~/.freelance-forge/shared/`
- Installed skills: `~/.openclaw/workspace/skills/{lead-qualifier,proposal-builder,project-onboarder,pipeline-tracker}/`
- Installed data: `~/.freelance-forge/`
- Architecture docs: `~/.openclaw/workspace/projects/freelance-forge/{architecture.md,design-philosophy.md,storage.md}`
- Subskill design docs: `~/.openclaw/workspace/projects/freelance-forge/subskills/`
- Consolidated repo: `~/internal-skills/freelance-forge/`

### What the Installed Version Has That the Bundle Doesn't
- `--crawl` mode in web_research.py (sitemap parsing, page discovery, multi-page merge)
- `_filter_phone()` function for phone number validation
- Content-type checking in HTTP fetch (skips non-HTML responses)
- WordPress sitemap fallback (`/wp-sitemap.xml`)
- Business page classification (contact, about, services, testimonials, pricing, blog)
- `data_confidence` column (renamed from `research_quality`)
- `pitch_notes` column
- `$SKILL_DATA_DIR` env var support
- Client folder structure (`reports/clients/<slug>/` instead of separate proposal/project dirs)
- Deep view in Pipeline Tracker (§B)
- Filtered pipeline views
- Enhanced follow-up email drafting with context points
- Foreign key error messages ("Lead not found" instead of raw SQL error)
- Template renderer error handling for missing files

### DB Schema (as created by installed version)
Tables: `leads`, `tags`, `lead_tags`, `activity_log`, `tasks`
Indexes: 10 indexes on leads, activity, and tasks tables
Foreign keys: CASCADE on delete (lead_tags → leads, tasks → leads, activity → leads)
UUIDs for primary keys
Timestamps: ISO 8601 with timezone

### Config File
Default config: `{"currency": null}` (bundle version has `"currency": "GBP"`)
The installed version removed the GBP default — more neutral.

### Line Count Summary
- Bundle Python: 1,421 lines
- Installed Python: 1,856 lines (+393 lines, +27.6%)
- Bundle SKILL.md: 922 lines
- Installed SKILL.md: 1,146 lines (+224 lines, +24.3%)
- Architecture docs (not shipped): 1,275 lines
- Subskill docs (not shipped): 1,194 lines

### Pricing Data (sourced 2026-04-28)
- Bonsai: $9-59/month (annual) or $15-59/month (monthly). 4 tiers.
- HoneyBook: $29-109/month (annual). 3 tiers. Free trial available.
- Dubsado: $335-525/year. 2 tiers. Start free, upgrade when ready.
- DIY: $0 but significant time cost. No automation, no research, no templates.
