# Sub-Skill Deep Dive: Lead Qualifier

**Parent:** Freelance Forge — `architecture.md`
**Version:** 0.1 — Design Phase
**Date:** 2026-04-25

---

## 1. Purpose

The Lead Qualifier researches a prospective client and produces a structured assessment that helps the freelancer decide whether to pursue the lead and how to approach them. It's the entry point of the Freelance Forge pipeline — every client relationship starts here.

**It does four things:**
1. **Research** — gather information about the company from public sources
2. **Assess** — score the lead's fit (1-10) based on research findings
3. **Report** — generate a full qualification brief with honest uncertainty flags
4. **Store** — create a pipeline row in Notion with summary data

---

## 2. When It Triggers

**Primary triggers:**
- "qualify this lead: [company/URL]"
- "research this company: [company/URL]"
- "score this prospect: [company/URL]"
- "check out [company/URL] for me"

**Context triggers** (where the intent implies qualification):
- "I got an email from [company] — should I pursue this?"
- "Someone mentioned [company] might need a website"
- "What do you think of this lead: [company/URL]"

---

## 3. Input

The user provides one or more of:
- Company name (e.g., "Acme Plumbing")
- Website URL (e.g., "https://acmeplumbing.ie")
- Domain name (e.g., "acmeplumbing.ie")

If only a company name is given, the agent should attempt to find the website before proceeding with research.

---

## 4. Research Process

### 4.1 Source Priority

Research should be conducted in this order, stopping early if sufficient information is gathered:

1. **Company website** (primary source)
   - Fetch and parse the homepage and key pages (About, Services, Contact)
   - Extract: company description, services offered, location, team size indicators, contact info
   - Note: site structure, navigation quality, mobile responsiveness indicators, loading speed

2. **Google/Bing search** (supplementary)
   - Search for: "[company name] [location]" to find reviews, news, social profiles
   - Search for: "site:[domain]" to discover indexed pages
   - Extract: Google Business profile if available, review ratings, recent news mentions

3. **Social media** (if easily discoverable)
   - LinkedIn company page: employee count, industry, recent posts
   - Facebook/Instagram: customer engagement, activity level, brand quality
   - Note: only if links are found on the website or in search results — don't go hunting

4. **Tech stack detection** (passive observation)
   - From the website's HTML: meta generator tags, CMS identifiers, framework hints
   - Common indicators: "Powered by WordPress", Shopify, Wix, Squarespace, custom
   - Note: this is passive observation from the source code, not active scanning

### 4.2 What to Collect

**Must collect (required for assessment):**
- What the company does (industry, services, products)
- Where they are (location, service area)
- How big they are (employee count range, revenue indicators if available)
- Their current website (URL, general quality assessment)
- Their current tech stack (if detectable)
- Contact information (email, phone, contact form)

**Nice to collect (strengthens assessment):**
- Social media presence (which platforms, activity level)
- Online reviews (Google, Trustpilot, etc.)
- Competitors in their space
- Recent news or changes (funding, expansion, rebrand)
- Marketing signals (running ads, content marketing, SEO investment)

**Cannot collect (note as unverified):**
- Actual budget or revenue
- Decision-making process
- Internal priorities or pain points
- Timeline for a potential project
- Previous experience with web designers

### 4.3 Research Quality Tiers

The report should indicate the quality of available information:

- **HIGH** — Full website with detailed About/Services pages, social profiles active, reviews available. Most findings are well-supported.
- **MEDIUM** — Basic website, limited social presence, some gaps. Key findings are supported but some assumptions were made.
- **LOW** — Minimal web presence, no social profiles, no reviews. Multiple assumptions required. Manual verification strongly recommended.

This tier applies to the overall assessment, not individual findings. Individual findings should each have their own confidence level.

---

## 5. Assessment & Scoring

### 5.1 Scoring Criteria (1-10)

The score reflects how good a fit this lead is for a freelance web designer. Each factor contributes to the overall score:

| Factor | Weight | What It Measures |
|---|---|---|
| **Need Signal** | High | Does their current website clearly need work? Are they visibly investing in marketing? |
| **Size Fit** | High | Are they the right size for a freelancer? (Not too big for a solo freelancer, not too small to afford one) |
| **Budget Signal** | Medium | Are there indicators they can afford professional web design? (Ad spend, team size, industry, location) |
| **Accessibility** | Medium | Can the freelancer realistically reach the decision maker? (Clear contact info, small team, local) |
| **Timing Signal** | Low | Are there indicators they're looking for web services now? (Job postings, recent funding, outdated site with active marketing) |

### 5.2 Score Interpretation

| Score | Meaning | Action |
|---|---|---|
| **8-10** | Strong lead — clear need, right size, budget likely | Pursue actively. Prioritise. |
| **6-7** | Good lead — fits well, some uncertainty | Pursue. Worth a discovery call. |
| **4-5** | Moderate — possible fit, significant unknowns | Pursue if capacity allows. Verify assumptions first. |
| **1-3** | Weak fit — too small, too big, or no clear need | Skip unless circumstances change. |

### 5.3 Scoring Honesty Rules

- **Never inflate the score.** A 5 is fine. Not every lead is an 8. Honest scores build trust with the freelancer.
- **State the reasoning.** Every score should have a brief explanation of what supports it.
- **Acknowledge the uncertainty.** If the score is based on assumptions, say which assumptions and how confident you are in each.
- **Score range, not exact number.** If there's significant uncertainty, present a range: "Score: 6-7 (hinges on budget — couldn't confirm)."
- **No score is better than a wrong score.** If there's genuinely not enough information to assess, say so: "Insufficient information to score. Recommend manual research before proceeding."

---

## 6. Report Structure

The full qualification report is saved as a markdown file. The Notion row stores a summary.

### 6.1 Report Template

```markdown
# Lead Qualification: [Company Name]

**Date:** [YYYY-MM-DD]
**Website:** [URL]
**Research Quality:** HIGH / MEDIUM / LOW

---

## Company Overview

[2-4 paragraphs covering: what they do, where they are, how big they are, their current market position. Written as a coherent summary, not bullet points.]

## Current Web Presence

**Website:** [URL]
**Platform:** [WordPress / Wix / Custom / Unknown]
**Quality Assessment:** [Brief assessment — is it functional? Outdated? Non-existent? Good but could be better?]

[Key observations about their current website: what works, what doesn't, what's missing.]

## Fit Assessment

**Score:** [X/10] or [X-Y/10 range]
**Verdict:** STRONG / GOOD / MODERATE / WEAK

**Reasoning:**
- Need Signal: [assessment with evidence]
- Size Fit: [assessment with evidence]
- Budget Signal: [assessment with evidence]
- Accessibility: [assessment with evidence]
- Timing Signal: [assessment with evidence]

## Key Findings

- [Finding 1 — specific, evidence-based]
- [Finding 2 — specific, evidence-based]
- [Finding 3 — specific, evidence-based]
- [Finding 4 — specific, evidence-based]
- [Finding 5 — specific, evidence-based]

## Unverified / Could Not Confirm ⚠️

[This section is NON-NEGOTIABLE. It must appear in every report.]

- "[What couldn't be verified] — [Why it couldn't be verified] — [How the freelancer could verify it]"
- "[Assumption made] — [What the assumption was based on] — [Alternative interpretations]"
- "[Requires conversation] — [What can only be learned by talking to the client]"

If the agent is highly confident about all findings (rare), this section should say:
"⚠️ All findings above were verified from public sources. Note that company information may have changed since this research was conducted."

## Recommendation

[2-3 sentences: what should the freelancer do with this lead? What's the suggested approach? What angle to take if they reach out?]

## Suggested Next Steps

1. [Specific action item]
2. [Specific action item]
3. [Specific action item]
```

### 6.2 What Goes in Notion vs. What Goes in the File

**File (full report):** Everything in the template above. This is the document the freelancer reads to understand the lead.

**Notion (summary row):**
- Company Name (title)
- Website (URL)
- Lead Score (number — the score, not the reasoning)
- Research Notes (rich text — a 2-3 sentence summary, not the full report)
- Status (select — "Lead")
- Budget Range (select — if a signal was detected, e.g., "£1-3K" or "Unknown")
- Service Type (multi_select — e.g., "Website Redesign", "New Website")
- Source (select — how the lead was found, if specified by user)

---

## 7. Notion Interaction

### 7.1 Prerequisite Check

Before writing to Notion, the Lead Qualifier must:
1. Check for `freelance-forge-config.json` in `$FREELANCE_FORGE_CONFIG_DIR`
2. If missing: run the Pipeline Tracker setup flow first (or instruct the user to set it up)
3. If present: load field mappings

### 7.2 Duplicate Check

Before creating a new pipeline row:
1. Search the pipeline database for an existing page with the same company name
2. If found: alert the user — "Acme Plumbing already exists in your pipeline (Status: Qualified, Score: 7). Want me to update the existing entry, or create a new one?"
3. If not found: proceed with creation

### 7.3 Creating the Pipeline Row

- Use `POST /pages` with the pipeline database as parent
- Map fields using the config's `fieldMappings`
- For shared fields (see Pipeline Tracker §3.5): if `researchNotes` and `discoveryNotes` map to the same property, prepend a label: "=== Research Notes ===\n[summary]\n\n=== Discovery Notes ===\n[notes]"

---

## 8. Optional: Email Draft

After the qualification report, offer to draft a first-contact email:

**Trigger:** User says yes, or the agent offers and user accepts.

**Rules:**
- Output in chat only — the user copies and sends
- Short (3-5 sentences max)
- Reference something specific from the research (shows it's not a generic template)
- Suggest a specific next step (discovery call, quick chat, etc.)
- Never be pushy or salesy — tone should be helpful and professional
- Include the freelancer's name placeholder if known, otherwise generic

**What NOT to include in the email:**
- The qualification score (internal tool, not client-facing)
- Negative observations about their current website (insulting the prospect is bad)
- Pricing (too early)
- Assumptions presented as facts

---

## 9. Edge Cases

| Scenario | Response |
|---|---|
| Company name only, no website found | Search for the website first. If still not found, ask the user. Don't proceed without at least a website or LinkedIn page. |
| Website is down or unreachable | Note it in the report. Attempt to find cached version or social media. Flag as a data quality issue. |
| Multiple companies with similar names | Present the options to the user, ask them to confirm which one. Don't guess. |
| Company is clearly too large (enterprise) | Still produce the report, but note in the assessment: "This appears to be a large organisation (500+ employees). They likely have an in-house team or agency relationship already. Pursuing this lead may require a different approach than typical freelance engagements." |
| Company is clearly too small (micro-business) | Still produce the report, but note budget reality: "Very small operation. May have limited budget for professional web design. Consider whether this is a good use of your time." |
| Very little web presence (LOW research quality) | Produce the report with heavy uncertainty flags. Recommend the freelancer do manual research before making contact. Don't inflate the score due to lack of contrary evidence. |
| Company is in a different country/region | Note the location. Consider timezone, language, and payment implications. Don't disqualify based on location alone. |
| Company already exists in pipeline | See §7.2. Offer to update or create new. |
| Config file doesn't exist | Trigger Pipeline Tracker setup. Don't try to create pipeline rows without a valid config. |
| Notion API error | Same error handling as Pipeline Tracker (see Pipeline Tracker §10). |

---

## 10. Shared Dependencies

**Reads from:**
- `freelance-forge-config.json` — database ID, field mappings
- Web (company website, search results, social media)

**Writes to:**
- Pipeline database in Notion — new page (or update existing)
- Report file in `$FREELANCE_FORGE_REPORTS_DIR/qualifications/[company-name].md`

**Depends on:**
- Pipeline Tracker — config file must exist before this sub-skill can write to Notion

**Does NOT depend on:**
- Proposal Builder, Project Onboarder (this runs first in the pipeline)
- Any other sub-skills

---

## 11. Design Decisions Specific to This Sub-Skill

### Why Research Before Scoring
The score should be evidence-based, not intuition-based. Gathering information first, then assessing, produces more reliable scores. The research section feeds directly into the assessment section.

### Why the Unverified Section Is Non-Negotiable
A freelancer might read the report and immediately pitch based on an assumption the agent made (e.g., "they have a £5K marketing budget"). If that assumption is wrong, the pitch falls flat and the freelancer looks bad. The unverified section prevents this by making every assumption visible.

### Why We Don't Score on Budget Alone
Budget is hard to determine from public sources. A company with no visible budget signals might still have money (they just don't advertise it). A company with visible ad spend might have no remaining budget for web design. The score considers budget as one factor among several, and flags it as uncertain.

### Why We Still Report on Low-Quality Leads
Even a score-3 lead might become a score-7 lead if circumstances change. Having the research on file means the freelancer can revisit later without re-researching. Also, the freelancer might have context the agent doesn't (e.g., "they're a friend of a friend").

### Why the Email Draft Is Optional and Separate
Not every qualified lead gets contacted immediately. Sometimes the freelancer wants to research further, or the lead isn't a priority right now. Making the email draft optional means the qualification flow isn't slowed down by an unnecessary step.

---

## 12. Claude Code Implementation Notes

### What's Fixed
- The research flow: website → search → social → tech stack (in order)
- The five scoring factors and their weights
- The report structure with mandatory unverified section
- Research quality tiers (HIGH/MEDIUM/LOW)
- The honest scoring rules (§5.3)
- Notion as metadata store, file as full report
- Duplicate checking before creating pipeline rows
- Email drafts are chat output only, optional

### What Claude Code Decides
- How to implement web fetching and parsing (library choices, error handling)
- The exact search queries to run
- How to detect tech stack from HTML (what to look for, how reliable the detection is)
- How to present the research quality tier
- The specific format of the Notion summary (how much to condense)
- File naming convention for reports
- How to handle rate limiting across multiple sources
- The tone and structure of the optional email draft
- How much detail to include in each report section (balance between thoroughness and readability)
