# Skill Ideas Research — 2026-04-08

Curated proposals ready for review and potential development. Sorted by impact rating (high first), then effort (low first).

## 🟢 High Impact, Low Effort

### Gmail Digest JSON Output — enhancement(github-growth-tracker)
**What it adds:** `--json` flag for structured output to match gmail-checker's dual format approach  
**API/Technical feasibility:** ✅ Easy - existing digest function just needs JSON serialization  
**Breaking change risk:** None - additive feature  
**Effort estimate:** Trivial (~15 minutes)  
**Impact rating:** Medium - consistency across tools  
**Recommendation:** ✅ Definitely worth building - simple consistency improvement  

### Skill Polisher Non-SKILL.md Files — enhancement(rebels-skill-polisher)  
**What it adds:** Extend polisher to clean up reference files, config examples, and README content for consistency  
**API/Technical feasibility:** ✅ Easy - leverage existing polishing rules on file types  
**Breaking change risk:** None - additive feature  
**Effort estimate:** Small (~1 hour)  
**Impact rating:** Medium - improves overall skill presentation  
**Recommendation:** ✅ Worth building - simple extension of existing functionality  

## 🟡 Medium Impact, Medium Effort  

### Gmail Body Snippet Preview — enhancement(rebels-gmail-checker)
**What it adds:** Fetch first ~200 chars of email body for context  
**API/Technical feasibility:** ✅ Easy - Gmail API `messages.get(format="full")` supports body extraction  
**Breaking change risk:** None - additive feature  
**Effort estimate:** Small (~30 minutes)  
**Impact rating:** Medium - significant UX improvement  
**Recommendation:** ✅ Worth building - users want email context without opening Gmail

### GitHub PR and Release Tracking — enhancement(github-growth-tracker)
**What it adds:** Track open PRs, recent releases, and contributor activity alongside current metrics  
**API/Technical feasibility:** ✅ Easy - GitHub REST API has PR/release endpoints  
**Breaking change risk:** None - optional feature  
**Effort estimate:** Small (~45 minutes)  
**Impact rating:** Medium - better engagement signals than just stars/forks  
**Recommendation:** ✅ Worth building - valuable engagement metrics

### Portability Checker Auto-Publish Fix — enhancement(agent-portability-checker)
**What it adds:** After auto-fixing, offer to bump version and publish directly to ClawHub  
**API/Technical feasibility:** ⚠️ Medium - requires `clawhub` CLI integration and conflict handling  
**Breaking change risk:** None - additive feature  
**Effort estimate:** Medium (~2 hours)  
**Impact rating:** Medium - streamlines publishing workflow  
**Recommendation:** ✅ Worth building if clawhub CLI is available - makes portable skills shippable faster

## 🟡 Medium Impact, High Effort

### Gmail Multi-Account Support — enhancement(rebels-gmail-checker)
**What it adds:** Support multiple accounts via credential files with naming pattern  
**API/Technical feasibility:** ✅ Easy - multiple OAuth credential files, account selection flag  
**Breaking change risk:** Low - new config format migration needed  
**Effort estimate:** Medium (~90 minutes)  
**Impact rating:** High - solves real user need (work + personal email)  
**Recommendation:** ✅ Worth building - high demand for multi-account support  

### Skill Polisher Batch Mode — enhancement(rebels-skill-polisher)
**What it adds:** Polish multiple skills at once from a skills directory  
**API/Technical failure:** ✅ Easy - iterate over SKILL.md files in directory  
**Breaking change risk:** None - additive feature  
**Effort estimate:** Medium (~1.5 hours) - handling approval workflow  
**Impact rating:** Medium - saves time for multiple skills  
**Recommendation:** ✅ Worth building - practical improvement for workflow

## 🔵 Lower Impact, Various Effort

### GitHub Webhook Integration — enhancement(github-growth-tracker)
**What it adds:** Real-time notifications via GitHub webhooks instead of polling  
**API/Technical feasibility:** ⚠️ Hard - requires public endpoint, webhook handling, state management  
**Breaking change risk:** Low - add-on feature  
**Effort estimate:** Large (~4+ hours)  
**Impact rating:** Low - cron polling sufficient for digest use case  
**Recommendation:** ❌ Not worth building now - overkill for digest workflow

### Gmail Send/Reply Action — enhancement(rebels-gmail-checker)
**What it adds:** Ability to send quick replies or compose emails from agent  
**API/Technical feasibility:** ⚠️ Hard - requires Gmail API send scopes, OAuth expansion, UI complexity  
**Breaking change risk:** Medium - new scopes and functionality  
**Effort estimate:** Large (~5+ hours)  
**Impact rating:** Medium - useful but complex to implement safely  
**Recommendation:** ❌ Defer - requires significant OAuth scope changes and careful handling

### Portability Checker Setup Script Generator — enhancement(agent-portability-checker)
**What it adds:** Auto-generate setup scripts for skills with credentials but no setup  
**API/Technical feasibility:** ⚠️ Medium - template-based generation for common OAuth flows  
**Breaking change risk:** Low - additive feature  
**Effort estimate:** Medium (~3 hours)  
**Impact rating:** Low - niche use case  
**Recommendation:** ❌ Defer - low impact compared to other enhancements

## 🟠 New Skills Research

### Invoice & Expense Processor
**Problem it solves:** Parse PDF/email invoices, extract structured data, categorize expenses, output CSV/JSON for accounting software  
**Target users:** Non-developers managing small business/personal finances  
**ClawHub gap analysis:** Limited invoice processing skills, mostly developer-focused PDF parsers  
**Open questions:** PDF parsing approach (OCR vs text extraction), email attachment support, accounting format targets  
**Feasibility:** Hard - PDF parsing is notoriously unreliable, multiple file formats, edge cases  
**MVP scope:** PDF invoices only, basic extraction, CSV output only  
**Effort vs Impact:** High effort (4+ hours) → Medium impact - PDF parsing too unreliable  
**Recommendation:** ❌ Not worth building - PDF parsing too unreliable for production use

### Content Repurposing Pipeline  
**Problem it solves:** Auto-generate Twitter threads, LinkedIn posts, newsletter snippets from long-form content  
**Target users:** Content creators, marketers, bloggers  
**ClawHub gap analysis:** No existing content repurposing skills, growing demand  
**Open questions:** Input format (URL vs file vs paste), output formats, template vs LLM-based  
**Feasibility:** Medium - depends on reliable content extraction and LLM quality  
**MVP scope:** Blog post → Twitter thread + LinkedIn post  
**Effort vs Impact:** Medium effort (3-4 hours) → High impact - valuable for creators  
**Recommendation:** ✅ Promising but needs validation - test content extraction quality first

### Competitor Watch
**Problem it solves:** Track competitor websites/social accounts for changes - new products, pricing, blog posts, hiring  
**Target users:** Businesses, product teams, marketers  
**ClawHub gap analysis:** No change monitoring skills, real need mentioned by multiple users  
**Open questions:** Change detection method, platform support, storage for history  
**Feasibility:** Medium - web scraping/challenging, needs robust change detection  
**MVP scope:** 3 websites, weekly digest, HTML diff + RSS where available  
**Effort vs Impact:** Medium effort (3+ hours) → High impact - valuable business use case  
**Recommendation:** ✅ Worth building if change detection proves reliable - validate with test sites first

## Research Summary

**Note:** No raw file found for 2026-04-07 (yesterday). Processed backlog of 10 ideas from 2026-04-04 that were still marked as "new".

## Priority Summary

**Top 3 ready to build:**
1. Gmail Digest JSON Output - Medium impact, trivial effort
2. Gmail Body Snippet Preview - Medium impact, small effort  
3. GitHub PR and Release Tracking - Medium impact, small effort

**Next considerations:**
4. Gmail Multi-Account Support - High impact, medium effort
5. Skill Polisher Batch Mode - Medium impact, medium effort

**New skills to validate:**
- Content Repurposing Pipeline (test content extraction first)
- Competitor Watch (test change detection reliability)

---

*Research completed: 2026-04-08 | Total ideas processed: 13 | Recommended: 8 | Deferred: 5*