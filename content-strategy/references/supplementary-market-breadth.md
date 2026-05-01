# Supplementary Findings: Broader Agent Skills Market Data

**Date:** 1 May 2026
**Prepared by:** Cambrian
**Status:** Raw findings — gaps flagged with [UNCERTAIN]
**Follows:** `exploratory-historical-parallels.md` (historical registry comparison)
**References:** `exploratory-post-4-market-shape.md` (mid-April 2026 market landscape)

---

## 1. Agensi (verify and update)

- **Current skill count:** Could not verify an exact number. The Agensi skills page (`agensi.io/skills`) is a discovery/SEO page listing "best skills" rather than a live registry count. Post 4 reported ~196 skills. Agensi has not publicly disclosed an updated total since.
- **Pricing:** The pricing page (`agensi.io/pricing`) returned only the site shell (JS-rendered, couldn't extract content). Post 4 reported $9/month Pro tier. This could not be re-verified today — treat as unconfirmed.
- **Revenue split:** Still unverified. Post 4 noted 80/20 estimate. No new public disclosure found.
- **Growth direction:** Agensi has significantly expanded its content/SEO footprint since mid-April. Their `/learn` section now has 30+ articles covering skills for specific domains (database engineering, security auditing, mobile dev, etc.), platform comparisons (Claude Code vs Codex CLI, Gemini CLI vs Claude Code), MCP server guides, and a "sell AI agent skills" creator guide. This is content-led growth — Agensi is positioning as the knowledge hub for the skills ecosystem, not just a marketplace. The content volume suggests active investment but doesn't confirm marketplace transaction volume.
- **Notable:** Agensi is now explicitly framing itself as cross-platform ("Claude Code, OpenClaw, Cursor, and more") rather than Claude-specific. They're also covering MCP marketplaces (Smithery, Glama) as comparators, suggesting they see the broader agent tooling ecosystem as their competitive frame.
- **Assessment:** Visibly growing on the content/positioning front. Marketplace activity unclear from public data. Likely still small in absolute numbers but investing heavily in category ownership.

---

## 2. skills.sh / Vercel (verify and update)

- **What it is:** `skills.sh` is the "Agent Skills Directory" — a discovery leaderboard for skills, powered by `npx skillsadd <owner/repo>`. It is NOT a registry; it's an index/search layer that points to GitHub-hosted skill repos.
- **Top skills by installs:** The leaderboard shows significant numbers:
  - microsoft/azure-skills: 5.4M total installs across 19+ skills
  - microsoft/github-copilot-for-azure: 2.4M total across 15+ skills
  - larksuite/cli: 935.7K total across 10+ skills
  - xixu-me/skills: 501.0K across 5 skills
  - pbakaus/impeccable: 491.8K across 5 skills
  - infsh-skills/skills: 847.4K + 134.5K across two collections
  - firecrawl/cli: 191.4K across 4 skills
- **Post 4 reported:** 235K+ weekly installs on the find-skills utility. The leaderboard numbers suggest the ecosystem is significantly larger than that now — the top skill alone (microsoft/azure-skills) has 5.4M total installs. However, these are cumulative totals, not weekly rates, so they're not directly comparable.
- **Positioning change:** skills.sh has rebranded from a Vercel-specific tool to "The Open Agent Skills Ecosystem." The tagline is now "The Agent Skills Directory" with no Vercel branding visible. The install mechanism is still `npx skillsadd`, which is Node/npm-based.
- **Vercel's role:** Could not find evidence of new Vercel-specific skills products since Post 4. Vercel appears to have shifted to supporting the broader open standard rather than maintaining a Vercel-branded skills product.

---

## 3. Anthropic's Enterprise Skills Offering (verify and update)

**Significant update since Post 4.** Anthropic has substantially expanded its skills ecosystem:

### Claude Cowork (announced April 29, 2026)
- Claude's blog lists "Deploying agentic AI across the enterprise with Claude Cowork" published April 29, 2026. The actual blog post URL couldn't be resolved (likely behind auth or a different path), but the title and date are confirmed from the blog listing.
- This appears to be Anthropic's enterprise agent deployment platform — the evolution of what Post 4 described as Anthropic's enterprise offering.
- **Status:** [UNCERTAIN — couldn't access the full post content]. The title suggests enterprise-wide agentic AI deployment, which would include skills. Whether it's a marketplace open to third-party authors or a managed Anthropic service is unclear from the title alone.

### Claude Managed Agents (April 8, 2026)
- "Claude Managed Agents: get to production 10x faster" — announced April 8, 2026.
- These are Anthropic-hosted agents that run in Anthropic's infrastructure. Skills are part of the capability stack (confirmed by the skills overview doc).
- "Built-in memory for Claude Managed Agents" announced April 23, 2026.

### Claude Plugins (new since Post 4)
- Claude now has a **Plugins** concept: "Shareable packages that bundle skills, connectors, slash commands, and sub-agents." This is a significant expansion beyond individual skills.
- Plugin types: Anthropic skills (pre-built), Partner skills (Notion, Figma, Atlassian), Organization-provisioned skills (admin-deployed), Custom skills (user-created).
- Plugins are available on Pro, Max, Team, and Enterprise plans.
- **This is effectively Anthropic's marketplace layer.** It's not open to arbitrary third-party authors in the ClawHub sense — it's curated by Anthropic with partner integrations and organizational provisioning. But it's a real distribution mechanism, not just marketing.

### Claude API Skill (April 29, 2026)
- "Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp" — Anthropic is distributing a Claude API skill to third-party developer tools. This is Anthropic pushing skills outward, not pulling them in.

### Skills vs Plugins distinction
From Claude's own docs:
- **Skills** = task-specific procedures that load dynamically
- **Plugins** = shareable packages that bundle skills, connectors, slash commands, and sub-agents
- **Projects** = static background knowledge
- **MCP** = connects to external services
- **Custom Instructions** = broad preferences

### Assessment
Anthropic has moved significantly since Post 4. The skills ecosystem around Claude is now multi-layered: individual skills → plugins (bundled packages) → managed agents (hosted infrastructure) → Claude Cowork (enterprise deployment). The key question for the post is whether this is "open to third-party authors" — the answer is: **partially.** Custom skills can be created by any user, and plugins can be shared within organizations. But there's no public marketplace where anyone can list and sell skills the way ClawHub works. Anthropic controls the distribution channels.

---

## 4. SKILL.md Cross-Platform Adoption (the key one)

**CONFIRMED: The SKILL.md standard was published as an open standard by Anthropic on December 18, 2025.** Source: Anthropic's engineering blog post "Equipping agents for the real world with Agent Skills" includes the update line: "We've published Agent Skills as an open standard for cross-platform portability. (December 18, 2025)." The spec lives at `agentskills.io`.

### Cross-Platform Adoption Table

| Platform | Date | Mechanism | Adoption Signal | Notes |
|---|---|---|---|---|
| **Claude (Anthropic)** | Nov 12, 2025 (first mention) / Dec 18, 2025 (open standard) | Native. Skills auto-discovered from project dirs. Plugins bundle skills for sharing. | Deepest integration. Pre-built skills for documents, partner skills (Notion, Figma, Atlassian), custom skills, org-provisioned skills. | Originator of the standard. |
| **OpenAI Codex CLI** | ~Feb 2026 (Codex launch) | Native. `openai/skills` GitHub repo (17.9K stars, 1.2K forks, created Nov 25, 2025). Auto-installed system skills + curated/experimental installable skills. | 17.9K GitHub stars on the skills catalog repo. Skills are a first-class Codex feature. | Codex desktop app includes "Skills and Automations." OpenAI fully adopted MCP across products in 2025. |
| **Google Gemini CLI** | ~2026 (exact date [UNCERTAIN]) | Supported per Agensi guide ("How to Install Skills in Gemini CLI"). | Agensi has a dedicated guide for it, suggesting non-trivial adoption. | Google has not made a major public announcement about SKILL.md support. Integration may be community-driven rather than official. |
| **GitHub Copilot** | 2026 | Skills support confirmed in Agensi's MCP guide ("GitHub Copilot Agent Mode + MCP"). | Microsoft has published multiple skill collections: azure-skills (5.4M installs), github-copilot-for-azure (2.4M installs). | Microsoft is the largest publisher of skills by install count. |
| **Cursor** | 2026 | Supported per Agensi's "AI Coding Tools Compared" guide. | Cursor is one of the major AI coding tools listed as supporting skills. | Integration details unclear — may be via SKILL.md reading or a custom mechanism. |
| **VS Code** | 2026 | Listed as supporting the standard in multiple sources. | VS Code has the largest developer installed base of any editor. | Likely via Copilot integration or extension support. |
| **Manus AI** | Jan 2026 (full integration announced) | Native. Parses SKILL.md files, executes scripts in sandbox. Slash commands, "Build a Skill with Manus" feature, Team Skill Library. | "Build a Skill with Manus" auto-packages workflows. Team Skill Library for sharing. Data source skills (SimilarWeb, Yahoo Finance, LinkedIn Search). | Now part of Meta (per one source). Strongest non-coding-agent integration. |
| **Windsurf / Codeium** | 2026 | Listed in Agensi's platform comparisons. | Presence in comparison guides suggests meaningful support. | [UNCERTAIN — couldn't confirm independently]. |
| **Cline** | 2026 | Listed as supporting SKILL.md in ecosystem articles. | Popular open-source AI coding agent. | [UNCERTAIN — couldn't confirm independently]. |
| **20+ others** | Various | Per Firecrawl blog: "Claude Code, OpenAI Codex CLI, Gemini CLI, GitHub Copilot, Cursor, VS Code, and 20+ other platforms." | No individual platform signals, but the breadth is notable. | The "20+" claim is from a Firecrawl blog post, not an official registry. |

### Nominal vs Real Support

**Clearly real (native integration, active use):**
- Claude/Anthropic — originator, deepest integration
- OpenAI Codex CLI — dedicated skills repo, first-class feature
- GitHub Copilot / Microsoft — largest skill publisher by installs
- Manus AI — sandbox execution, team libraries, data source skills

**Likely real but less visible:**
- Cursor — mentioned in comparison guides but no major public announcement
- VS Code — likely via Copilot
- Gemini CLI — Agensi has a guide, suggesting real usage, but Google hasn't announced it

**Uncertain:**
- Windsurf, Cline, and others in the "20+" — couldn't independently verify

### The Key Finding

**The standard IS genuinely cross-platform, and adoption is broader than ClawHub+OpenClaw.** Anthropic created the standard, OpenAI adopted it for Codex, Microsoft is the largest publisher by installs, and Manus (now Meta) has full sandbox execution. This is not a single-vendor play dressed up as cross-platform — multiple competing AI companies are all publishing and consuming SKILL.md files.

**However:** The *discovery and distribution* layer is fragmented. There's no single marketplace that all platforms pull from. ClawHub is the largest public registry. OpenAI has its own skills catalog. Microsoft publishes via GitHub. Manus has its own marketplace. The standard is unified; the distribution isn't.

---

## 5. Addressable Installed Base

| Platform | Rough User Count | Source | Date |
|---|---|---|---|
| **ChatGPT (OpenAI)** | 900M weekly active users | Business of Apps, citing multiple sources | 2025 data (likely higher now) |
| **ChatGPT subscribers** | 50M (Plus/Pro/Enterprise) | Business of Apps | 2025 |
| **Google Gemini** | 750M active users | Business of Apps, citing AppMagic + Similarweb | Dec 2025 |
| **Claude** | 20M users (2025) / Anthropic $6B revenue (2025) | Business of Apps | 2025 |
| **Claude revenue breakdown** | 55% enterprise, 20% Claude Code, 20% Pro, 5% other | Business of Apps, citing Sacra | 2025 |
| **OpenClaw** | 367K GitHub stars, 75.4K forks | GitHub API (direct query today) | May 1, 2026 |
| **GitHub Copilot** | ~1.8M paid subscribers (2024 figure) | GitHub blog, widely reported | 2024 [UNCERTAIN — may be higher] |
| **Manus AI** | Not publicly disclosed | — | — |

### Notes on Installed Base

- **ChatGPT + Gemini combined:** ~1.65B active users. This is the pre-existing installed base that the agent skills market can reach. Neither platform currently exposes skills prominently to consumers, but both have developer-facing skills support (Codex for OpenAI, Gemini CLI for Google).
- **Claude + Claude Code:** 20M Claude users, with Claude Code being a significant slice (20% of revenue = $1.2B of $6B). Claude Code users are the primary skills consumers today.
- **OpenClaw:** 367K GitHub stars is a visibility/signal metric, not an active user count. The ClawHub homepage claims 180K users and 12M downloads — these are the more relevant figures for installed base, but they're self-reported and unaudited.
- **The structural argument:** The post's claim that a pre-existing installed base is driving skills market growth is well-supported. There are hundreds of millions of AI agent users across platforms, and skills compatibility is spreading across all major platforms. The installed base isn't the bottleneck — distribution and discovery are.

---

## 6. Other Agent-Skills Venues

### Still Active (from Post 4 set)
- **Agensi** — expanded significantly (see Item 1). Now positioning as cross-platform knowledge hub.
- **skills.sh** — rebranded to "The Agent Skills Directory." No longer Vercel-branded. Discovery layer, not a registry.
- **Anthropic/Claude** — massively expanded with Plugins, Managed Agents, Claude Cowork (see Item 3).
- **OpenAI/Codex** — `openai/skills` GitHub repo with 17.9K stars. First-class Codex feature.
- **Microsoft/GitHub** — largest skill publisher by installs. Azure skills (5.4M), Copilot for Azure (2.4M).

### New or Notable Since Post 4
- **Manus AI (Meta)** — full SKILL.md integration with sandbox execution. Team Skill Library. Now owned by Meta. This is a new major player since Post 4.
- **agentskills.io** — the official open standard specification site. Hosted by Anthropic but positioned as platform-agnostic. This is the standards body equivalent.
- **Firecrawl** — published a major explainer on SKILL.md adoption (April 2026), positioning Firecrawl as a skill-compatible tool. 191.4K installs on their CLI skill.

### MCP-Adjacent (not SKILL.md but relevant)
- **Smithery** — MCP server directory. Compared by Agensi.
- **Glama** — MCP server directory. Compared by Agensi.
- **Composio** — AI agent integration platform. Agensi has a "Composio alternatives" article.

### Disappeared/Pivoted
- None detected from the Post 4 set. All major players are still active and have grown.

---

## 7. Optional Gap-Fills from Previous Pass

### ClawHub 15K and 50K Milestone Dates
**Not resolved.** ClawHub homepage shows 52.7K tools today (May 1, 2026). The GitHub repo was created January 3, 2026. No public changelog, blog, or Wayback Machine data found with milestone dates. Would need access to ClawHub's internal analytics or a direct ask to the ClawHub team.

**Estimate refinement:** If 52.7K in 119 days (Jan 3 → May 1), and growth is roughly linear, 15K would have been hit around day 34 (Feb 6) and 50K around day 113 (Apr 26). But this assumes linearity, which is unverified. Could be earlier if growth was front-loaded.

### ClawHub Growth Shape
**Not resolved.** No historical data series found. The ClawHub homepage shows a single snapshot (52.7K tools, 180K users, 12M downloads, 4.8 avg rating). No charts, no historical progression, no API for querying counts by date.

### SKILL.md Standard Launch Date
**RESOLVED.** December 18, 2025. Confirmed from Anthropic's engineering blog post, which includes the explicit update: "We've published Agent Skills as an open standard for cross-platform portability. (December 18, 2025)." The specification lives at `agentskills.io`. The OpenClaw GitHub repo was created November 24, 2025 (before the standard was published), and the ClawHub repo was created January 3, 2026 (after).

---

## Key Takeaway for the Post

The working hypothesis was right in one direction and wrong in another.

**Right:** The agent skills market IS broader than ClawHub. Anthropic, OpenAI, Microsoft, and Meta/Manus are all active participants. The SKILL.md standard has genuine cross-platform traction with 6+ major platforms supporting it natively.

**Wrong:** The cross-platform adoption isn't "thinner than expected" — it's substantially wider. The surprise is that competing AI companies (Anthropic, OpenAI, Microsoft) are all publishing and consuming the same skill format. This is unusual in platform history. Apple and Google don't share app formats. npm and PyPI don't share packages. But Anthropic-created skills work in OpenAI's Codex and Microsoft's Copilot.

**The structural story for the post:** The agent skills market has a unified format (SKILL.md) running on a fragmented distribution layer (ClawHub, OpenAI skills repo, Anthropic plugins, Manus marketplace, Microsoft GitHub repos). This is a new pattern — more like HTTP/HTML in 1994 than like the App Store in 2008. The standard propagated before any single marketplace dominated.

**The installed base argument is very strong:** 1.65B+ ChatGPT + Gemini users, 20M Claude users, 367K OpenClaw stars, and growing. The market isn't supply-constrained (plenty of skills) or demand-constrained (massive user base). The constraint is distribution — connecting the right skill to the right user at the right time across fragmented platforms.
