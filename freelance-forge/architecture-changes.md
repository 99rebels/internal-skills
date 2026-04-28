# Freelance Forge — Architecture Update Log

**Date:** 2026-04-28
**Author:** Cambrian
**Trigger:** Product changes since initial design phase; architecture docs out of sync with implementation

---

## Changes Made

This log tracks every divergence between the architecture documents and the current implementation state.

---

### 1. Directory Structure (storage.md, architecture.md, README.md, setup.md)

**What changed:**
- Removed `reports/proposals/` and `reports/projects/` directories
- Added `reports/clients/<slug>/` as the per-client container
- Qualification reports start flat in `reports/qualifications/` (staging zone)
- When a lead is added to pipeline, report moves to `reports/clients/<slug>/qualification-<date>.md`
- All subsequent files (proposal, brief, checklist, sitemap) go into `reports/clients/<slug>/`

**Why:** Consolidates all client files in one place. Qualification stays flat until the freelancer commits to pursuing the lead — no abandoned client folders.

**Files updated:**
- `storage.md` §2 — directory structure diagram
- `architecture.md` §7.1 — bundle file layout
- `architecture.md` §6.5 — report generator description
- `README.md` — directory structure section
- `setup.md` — mkdir commands (already done)

### 2. Database Schema Change: `research_quality` → `data_confidence` (storage.md, lead-qualifier.md)

**What changed:** The `leads` table column `research_quality` was renamed to `data_confidence` during implementation.

**Why:** "Data confidence" is more precise — it reflects confidence in the gathered data, not the quality of the research process itself.

**Files updated:**
- `storage.md` §3.1 — schema DDL, column description
- `lead-qualifier.md` §6.2 — database column list
- `lead-qualifier.md` §4.3 — research quality tiers reference
- `architecture.md` §5.1 — database writes description

### 3. Database Schema Addition: `pitch_notes` column (storage.md, lead-qualifier.md, architecture.md)

**What changed:** A `pitch_notes TEXT` column was added to the `leads` table.

**Purpose:** Stores a structured pros/cons list derived from the qualification report. Used when drafting emails or preparing for a pitch. Format: `**Pros:** ...\n**Cons:** ...`

**Files updated:**
- `storage.md` §3.1 — add column to schema DDL
- `lead-qualifier.md` §7.3 — add to "Creating the Lead Row" step
- `architecture.md` §5.1 — add to database writes list

### 4. Follow-Up Email Talking Points (pipeline-tracker.md)

**What changed:** The follow-up email draft now includes structured "context points" alongside the draft (reference, tone check, next step, if they say no). Previously it was just a brief draft with no structured breakdown.

**Why:** The freelancer may want to write their own version. The structured points explain *why* the draft is written that way, so they can adopt the strategy in their own voice. Mirrors the talking points format already used by the Lead Qualifier's first-contact email.

**Files updated:**
- `pipeline-tracker.md` §6 — follow-up email draft section
- `pipeline-tracker.md` §15 — Claude Code implementation notes

### 5. Web Research: Content-Type Check (architecture.md)

**What changed:** The web research helper now checks the HTTP `Content-Type` header before extracting content. Non-HTML responses (JSON, images, PDFs) are skipped with a note rather than being marked `accessible: true`.

**Why:** A JSON API response was being marked as accessible because the text extraction produced >200 chars. This could confuse the Lead Qualifier's flow logic.

**Files updated:**
- `architecture.md` §6.2 — web research helper description

### 6. Web Research: Phone Regex Hardening (architecture.md)

**What changed:** The phone number regex now filters out false positives (IP addresses, ISO dates, bare digit strings) before returning results.

**Why:** The original regex was too loose — matching things like `86.45.109.96` (an IP address) as a phone number. This would produce false contact info in qualification reports.

**Files updated:**
- `architecture.md` §6.2 — web research helper description

### 7. Error Handling: FK Constraint Translation (architecture.md, storage.md)

**What changed:** The database helper CLI now catches `FOREIGN KEY constraint failed` errors and translates them to human-readable messages (e.g., "Lead not found (id: ...)") instead of leaking raw SQLite errors.

**Why:** Per the design principle: "Error handling should suggest the fix, not just report the error."

**Files updated:**
- `architecture.md` §10 — implementation notes
- `storage.md` §5.2 — key design decisions

### 8. Template Error Handling (architecture.md)

**What changed:** The template CLI now catches `FileNotFoundError` and prints a clean one-line error instead of a Python traceback.

**Files updated:**
- `architecture.md` §10 — implementation notes

### 9. Config Default: `currency` → "EUR" (storage.md)

**What changed:** The default currency was changed from "GBP" to "EUR" to reflect the target market (Ireland).

**Files updated:**
- `storage.md` §4 — config file example

### 10. Proposal File Naming (proposal-builder.md, project-onboarder.md, architecture.md)

**What changed:** Proposal files now use `proposal-<date>.md` inside the client folder instead of `<slug>-<date>.md` in a flat proposals directory. Same for qualification reports (`qualification-<date>.md`).

**Files updated:**
- `proposal-builder.md` §8 — output file path
- `project-onboarder.md` §3 — proposal file read path
- `project-onboarder.md` §9 — output file paths
- `architecture.md` §5.2 — Stage 2 data flow

### 11. Lead Qualifier: Client Folder Migration (lead-qualifier.md, architecture.md)

**What changed:** When adding a lead to the pipeline, the Lead Qualifier now creates a `reports/clients/<slug>/` directory and moves the qualification report into it (renaming from `<company-slug>-<date>.md` to `qualification-<date>.md`). This is the "commitment point" — adding to pipeline = creating a client folder.

**Files updated:**
- `lead-qualifier.md` §7.3 — expanded to include folder creation and report migration
- `architecture.md` §5.1 — Stage 1 data flow

### 12. Playwright: Now Required, Not Optional (setup.md, README.md)

**What changed:** While Playwright is still technically optional (the fallback HTTP fetch works), the setup flow now strongly recommends it and the Lead Qualifier produces meaningfully worse results without it. The setup doc was already updated to ask the user explicitly.

**Status:** No doc changes needed — already handled in setup.md Step 8.

### 13. Project Path Reference (project-onboarder.md, architecture.md, storage.md)

**What changed:** The `project_path` column in the leads table now points to `reports/clients/<slug>/` instead of `reports/projects/<slug>/`.

**Files updated:**
- `storage.md` §3.1 — column comment
- `project-onboarder.md` §5 — project brief links section
- `project-onboarder.md` §9 — output file paths
- `architecture.md` §5.3 — Stage 3 data flow
