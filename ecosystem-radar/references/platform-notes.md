# Platform Notes

Technical details for each tracked marketplace.

## ClawHub
- **Access:** CLI (`clawhub` command, installed with OpenClaw)
- **Auth:** Token stored from `clawhub login`
- **Strategy:** We don't track totals (explore is unreliable). Instead we inspect specific skills for download/star/version counts.
- **Tracked skills (market indicators):** self-improving-agent, ontology, obsidian, agent-browser, api-gateway, mcpporter, prismfy-search, baidu-search
- **Your skills:** github-growth-tracker, rebels-gmail-checker, rebels-skill-polisher
- **Data available per skill:** downloads, installsCurrent, stars, comments, versions, updatedAt
- **Limitations:** No reliable total skill count. Rate limited (~900 req/hour).
- **Payments:** None as of April 2026

## Agensi (agensi.io)
- **Access:** Web scraping only (no public API)
- **Features:** Leaderboard, weekly winners, skill requests, referral program
- **Payments:** **Confirmed** — Stripe integration (stripe-terms page exists, commission/payout terms found)
- **Categories:** Frontend & Design, Testing & QA, DevOps, Code Review, Documentation, Productivity, Data Engineering, API Development
- **Data extraction:** Parse `/skills` page for skill links, filter out category navigation links
- **Limitations:** JS-rendered site. Counts may be approximate. No individual skill stats visible on listing page.
- **Your skills:** github-growth-tracker, gmail-checker are listed

## GitHub — Platform Adoption Tracking
- **Access:** GitHub REST API (unauthenticated, 60 req/hour)
- **What it measures:** User adoption of skill-consuming platforms
- **Tracked repos:**
  - openclaw/openclaw — the agent runtime
  - openclaw/clawhub — the skill marketplace
  - anthropics/claude-code — Claude Code (if public)
  - openai/codex — Codex CLI (if public)
- **Data available:** stars, forks, open issues, latest release tag, push timestamp
- **Why track:** Skills need platforms. More users = bigger marketplace. Star growth rate > absolute count.
- **Limitations:** Unauthenticated = 60 req/hour. Some repos may not be public.

## Disabled Platforms

### OpenAgentSkill (openagentskill.com)
- **Status:** Disabled — JS-rendered Next.js site returns ~6 slugs from server HTML
- **Why disabled:** No real API (docs page shows format but endpoint returns 404). Server-side HTML is too sparse for meaningful extraction.
- **Revisit if:** They add a working API or we implement headless browsing.

### SkillsMP (skillsmp.com)
- **Status:** Disabled — Cloudflare blocks all automated access (403)
- **Why disabled:** Despite having a free API key, Cloudflare challenge wall blocks requests from non-browser clients. Site appears to be primarily a GitHub scraper with limited unique value.
- **Revisit if:** They provide API access that works server-side, or we implement cookie-based auth.

### LobeHub Skills (lobehub.com/skills)
- **Status:** Disabled — no clear public REST API
- **Scale:** 169,000+ skills indexed (largest directory by count)
- **Why disabled:** More of an aggregator than a marketplace. No API.
- **Revisit if:** They add an API or we implement a viable scrape strategy.
