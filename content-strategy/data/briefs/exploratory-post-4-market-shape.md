# Exploratory Findings: The Shape of the Skills Market Right Now

**Date:** 16 April 2026
**Format:** Analysis (argument-led with data support)
**Status:** Exploratory pass — raw findings for directed brief input

---

## 1. Player Table

| # | Name | URL | Launch/Announcement | Positioning | Pricing | Relationship to Skills | 3rd-Party Authorship | Apparent Size/Traction | Differentiation |
|---|------|-----|---------------------|-------------|---------|----------------------|---------------------|----------------------|-----------------|
| 1 | **Anthropic Agent Skills (architecture)** | anthropic.com/engineering | Oct 16, 2025 | The originating architecture. Anthropic's engineering blog introduced skills as organized folders of instructions, scripts, and resources for Claude agents. | N/A — it's an architecture, not a product | Origin point. The spec that everything else builds on. | N/A — Anthropic-authored spec, donated to open standard | N/A | The origin. Every other player either uses this standard or competes with it. |
| 2 | **Anthropic Open Standard** | agentskills.io | Dec 18, 2025 | Anthropic open-sourced the Agent Skills standard, making it cross-platform. Enables skills reuse across Claude, Codex, Cursor, etc. | N/A — open standard | The moment skills became a portable ecosystem, not a Claude feature. | Open standard — anyone can build to it | N/A | "Build once, deploy everywhere." The standardization that made a marketplace ecosystem possible. |
| 3 | **Salesforce AgentExchange** | agentexchange.salesforce.com | March 4, **2025** | "The trusted marketplace for Agentforce." A marketplace for AI-driven digital labor embedded in Salesforce platform. | Enterprise contracts (part of Salesforce licensing) | **Pre-dates the skills architecture by 7 months.** Uses Salesforce's own "actions," "topics," and "templates" — not SKILL.md. | Partners only (Salesforce Partner Org required). Apex development expertise needed. | 200+ initial partners at launch (Google Cloud, DocuSign, Box, etc.) | First-mover enterprise agent marketplace. Embedded natively in Salesforce, not standalone. Uses its own format, not SKILL.md. |
| 4 | **Oracle AI Agent Marketplace** | oracle.com/artificial-intelligence/ai-agents | Oct 15, 2025 | Embedded within Oracle Fusion Cloud Applications. Partner-built, Oracle-validated AI agents for enterprise workflows. | Enterprise contracts (bundled with Oracle Fusion) | Enterprise "AI agents" — not SKILL.md skills. Uses Oracle AI Agent Studio. | Partners only. Validated by Oracle. | 100+ AI agents from 20+ vendors at launch (Accenture, Deloitte, etc.) | Natively embedded in Oracle Fusion. Validation + compliance first. Not open ecosystem. |
| 5 | **Google Cloud AI Agent Marketplace** | cloud.google.com/partners/ai-agent-marketplace | Announced at Google Cloud Next '25 (~April 2025); features available Oct 14, 2025 | Partner-built, Google Cloud-validated agents discoverable through Google Cloud Marketplace. | Enterprise contracts (through Google Cloud Marketplace) | Enterprise "AI agents" — Google-validated. Not SKILL.md. | Partners only. | Not disclosed | Leverages existing Google Cloud Marketplace infrastructure. Validation + cloud integration. |
| 6 | **Vercel skills.sh** | skills.sh | Jan 20, 2026 | "The open agent skills ecosystem." CLI-based directory for installing skill packages across 16+ agents. Positioned as "npm for agent skills." | Free. No payments. | **True SKILL.md ecosystem.** CLI tool (`npx skills add <owner/repo>`) installs skills across Claude Code, Cursor, Copilot, Codex, etc. | Yes — open. Anyone can publish a repo as a skill. | Top skill: 20K+ installs. `find-skills` utility: 235K+ weekly installs. Microsoft Azure skills: 3.8M total. Coreyhaines marketing skills: 154K total. | Distribution infrastructure, not a marketplace. "npm for skills" — installs from GitHub repos. No payments, no review gate. Pure distribution. |
| 7 | **Agensi** | agensi.io | ~Feb 18, 2026 (Reddit post inviting creators) | "The marketplace for AI agent skills built on the open SKILL.md standard. Buy once, install instantly, own forever." | **Paid.** Individual purchases (creator-set pricing). Agensi takes 20% + $0.50/sale. Creators earn 80%. **Agensi Pro:** $9/month (or $90/year) for unlimited catalog access via MCP. | **True SKILL.md ecosystem.** First consumer-facing paid marketplace. Security review on every skill. | Yes — open to creators. Security scan + admin review before listing. | 196 skills (Apr 16). Growing 21% in 5 days. Confirmed Stripe payments. Categories: frontend, testing, devops, code review, docs, productivity, data eng, API dev. | First-mover paid consumer marketplace. Security-reviewed. One-time purchase model (not subscription per skill). IP protection via buyer fingerprinting. MCP-based Pro tier. |
| 8 | **GitHub Copilot Skills** | code.visualstudio.com/docs/copilot/customization/agent-skills | Dec 2025 (VS Code v1.108) | Experimental agent skills support in VS Code. Loads skills from `.github/skills/` folders. | Free (part of Copilot subscription) | **True SKILL.md ecosystem.** Embedded in Copilot, not a standalone marketplace. Repos become skill hubs. | Yes — open. Any workspace can have `.github/skills/` folder. | Copilot Skills Challenge ongoing. 184K+ discussions. | Skills are embedded in the developer workflow (VS Code), not browsed on a marketplace. Repos ARE the distribution channel. |
| 9 | **OpenAI Codex/ChatGPT Skills** | community.openai.com | Dec 12, 2025 (per Simon Willison) | OpenAI adopted Anthropic-style skills system for Codex CLI and ChatGPT. Skills stored in `/home/oai/skills/` and `~/.codex/skills/`. | Free (part of OpenAI subscription) | **True SKILL.md ecosystem.** Adopted the open standard. | Yes — open. | Not quantified | Cross-ecosystem validation — when OpenAI adopts your competitor's standard, it's become the industry default. |
| 10 | **ClawHub** | clawhub.ai | March 23, 2026 | "A versioned registry for AI agent skills. Versioned like npm, searchable with vectors, no gatekeeping." | Free. No payments. No premium tier detected. | **True SKILL.md ecosystem.** The registry for OpenClaw. CLI-based install. | Yes — open. `clawhub publish` to list. | ~1,733+ skills indexed (sample, not total). 48K+ total per API. Security reviews present. | Versioned registry (like npm). Staff picks + popular rankings. No payments. "No gatekeeping" positioning. |
| 11 | **Anthropic Claude Marketplace** | claude.com | March 6, 2026 | B2B procurement marketplace for third-party software that integrates with Claude. "Simplify software procurement for enterprises." | Enterprise contracts. Anthropic takes no commission. Enterprises can use Anthropic spending commitments. | **NOT a skills marketplace.** It's an enterprise procurement channel for Claude-powered SaaS products (Snowflake, GitLab, Harvey AI, Replit, Lovable, Rogo). | Anthropic-curated partners only. Initial 6 partners. | 6 partners at launch (limited preview). Plans to expand. | Enterprise procurement simplification, not skills discovery. Uses Anthropic spending commitments as purchasing power. |
| 12 | **Anthropic Claude Partner Network** | claude.com/partners | March 12, 2026 | Partner program for enterprises adopting Claude. $100M investment in 2026 for training, technical support, joint marketing. | Free membership. $100M Anthropic investment in partner support. | **NOT a skills marketplace.** It's a professional services/partner program (like AWS Partner Network). | Partners only (consultancies, professional services firms, AI specialists). | Partners include Accenture (training 30K professionals), Deloitte, Infosys. Scaling partner team 5x. | Enterprise implementation support. Certifications (Claude Certified Architect). Services Partner Directory. Not a marketplace for skills. |
| 13 | **Skills4Agents** | skills4agents.com | Pre-launch (waitlist as of Apr 2026) | "Built for the Claude Agent ecosystem. The marketplace where AI expertise meets demand." Creator-focused monetization. | **Planned paid.** Free + Premium ($10-$500/skill) + Enterprise (custom). Creators keep 85%. | **Planned SKILL.md ecosystem.** Claude-focused, not cross-platform (from their positioning). | Planned — open to creators. Currently waitlist. | Not yet launched. No skills listed. | Creator-first revenue model (85% to creators). Claude-specific, not cross-platform. Still vapor — no live product. |
| 14 | **AgentFX Directory** | agentfx.directory | Unknown (live as of Apr 2026) | "The AI Agent Component Library." Curated, verified, production-tested skills from the Hyper AI ecosystem. | Unclear — no pricing visible on site. May be free (marketing play for Hyper's ecosystem). | **SKILL.md-adjacent.** Skills derived from agents running in production on Hyper platform. | Likely curated/first-party (from Hyper's ecosystem). Not open submission visible. | ~11 skills visible (arbitrage, trading, marketing, dev). Small, curated. | Production-tested skills from real agent workflows. Vertical focus (marketing + trading). Small but quality-focused. |
| 15 | **claudeskillsmarket.com** | claudeskillsmarket.com | Unknown (live as of Apr 2026) | "Discover, share, and commission Claude AI skills." Third-party site with free skills, courses, guides, use cases. | Free skills visible. Has "Courses" and "Jobs" sections suggesting monetization elsewhere. | **SKILL.md ecosystem.** Claude-specific. | Appears open — has free skills section. | Unknown — JS-rendered, limited content extracted. | Third-party, not Anthropic. Combines skills marketplace with courses/guides/jobs — broader play. Claude-specific. |
| 16 | **SkillsMP** | skillsmp.com | Unknown (live as of Apr 2026) | Directory/aggregator. "145,964+ skills" across Tools, Development, Data & AI, Business, Content & Media. | Free. No payments. Cloudflare-blocks automated access. | **Broad skills directory** — likely aggregates from GitHub and other sources. | Likely automated aggregation, not manual submission. | 145,964+ skills (but this is aggregated, not hosted). | Scale play — biggest number but lowest curation. More of a search engine for skills than a marketplace. |
| 17 | **agentskill.sh** | agentskill.sh | Unknown (live as of Apr 2026) | Directory/aggregator. 110K+ skills indexed. | Free. No payments. | Broad skills directory. | Likely automated aggregation. | 110K+ skills. | Similar to SkillsMP but smaller. |

---

## 2. Chronological Timeline

| Date | Event | Significance |
|------|-------|-------------|
| **March 4, 2025** | Salesforce launches AgentExchange | **First enterprise agent marketplace.** Pre-dates the skills architecture by 7 months. Uses Salesforce's own format, not SKILL.md. 200+ partners. |
| **~April 2025** | Google Cloud AI Agent Marketplace announced at Next '25 | Enterprise agent marketplace, Google-validated. Not SKILL.md. |
| **October 14, 2025** | Google Cloud AI Agent Marketplace features go live | |
| **October 15, 2025** | Oracle launches AI Agent Marketplace at AI World | 100+ agents, 20+ vendors. Embedded in Oracle Fusion. Not SKILL.md. |
| **October 16, 2025** | **Anthropic publishes Agent Skills architecture** | **The origin point.** Engineering blog post introduces SKILL.md as a way to give Claude domain-specific expertise. |
| **December 12, 2025** | OpenAI adopts skills system for Codex CLI and ChatGPT | Cross-ecosystem validation. The standard is becoming universal. |
| **December 18, 2025** | **Anthropic open-sources Agent Skills standard** | **The ecosystem becomes possible.** Skills become portable across platforms. |
| **December 2025** | GitHub Copilot adds experimental agent skills in VS Code v1.108 | Skills embedded in the world's largest developer IDE. |
| **January 20, 2026** | **Vercel launches skills.sh** | First distribution infrastructure for the open standard. "npm for skills." 235K+ weekly installs of find-skills utility within days. |
| **~February 18, 2026** | **Agensi launches** (Reddit post) | **First paid consumer marketplace for skills.** Stripe integration. Security review. 80/20 revenue split. |
| **March 6, 2026** | Anthropic launches Claude Marketplace (B2B) | Enterprise procurement channel for Claude-powered SaaS. NOT a skills marketplace. 6 initial partners. |
| **March 12, 2026** | Anthropic launches Claude Partner Network ($100M) | Professional services partner program. NOT a skills marketplace. |
| **March 23, 2026** | **ClawHub launches** | OpenClaw's skill registry. Free. Versioned like npm. "No gatekeeping." |
| **~March 2026** | OpenAI Codex gets GPT-5.2-Codex model | Optimized for agentic coding with skills. |
| **Pre-launch (Apr 2026)** | Skills4Agents in waitlist | Planned creator marketplace. 85% creator revenue. Not yet live. |

---

## 3. Observations

### Patterns Across the Set

- **Two distinct market strata are forming, but they're not what the brief hypothesised.** The split isn't "free vs paid" — it's **enterprise (closed ecosystems)** vs **consumer/open (SKILL.md ecosystem)**. The enterprise players (Salesforce, Oracle, Google Cloud) built their own agent marketplaces *before* the SKILL.md standard existed and use their own formats. The consumer/open ecosystem (ClawHub, Agensi, Vercel skills.sh, GitHub Copilot) all use the open SKILL.md standard. These two layers don't interoperate.

- **Enterprise players pre-dated the standard.** Salesforce AgentExchange (March 2025) is seven months older than the skills architecture (Oct 2025). Oracle and Google Cloud also pre-date it. The enterprise layer formed independently, around proprietary agent platforms, not around SKILL.md. This means the skills architecture hasn't disrupted the enterprise layer — it grew alongside it in a parallel universe.

- **The commercial middle layer is Agensi and only Agensi.** Within the SKILL.md ecosystem, exactly one player has working payments: Agensi. No other open-ecosystem player charges for skills. Vercel skills.sh is free distribution. ClawHub is free. GitHub Copilot skills are embedded. This is a striking concentration of commercial power in a single early player.

- **Timeline is unprecedented, confirming the hypothesis.** The open standard is ~4 months old (Dec 18, 2025). In that time: Vercel built skills.sh, Agensi launched and grew to 196 skills, ClawHub launched with 1,733+ indexed skills, and Skills4Agents is in waitlist. The speed of marketplace formation is unlike prior package ecosystems (npm took ~2 years to get critical mass; PyPI took ~3).

- **Anthropic is curiously absent from the commercial skills layer.** Anthropic created the architecture, open-sourced it, launched a B2B procurement marketplace, and committed $100M to a partner network — but none of these are a third-party skills marketplace. Anthropic has not built or launched a marketplace where outside authors can sell SKILL.md skills. They created the gold rush and then stood back from the claim staking.

### Gaps in the Market

- **No enterprise SKILL.md marketplace exists.** The enterprise players use proprietary formats, not SKILL.md. There's no "Agensi for enterprises" — a paid, curated, compliance-focused SKILL.md marketplace for corporate buyers. This is arguably the biggest gap: the enterprise demand for agent capabilities is proven (Salesforce, Oracle, Google Cloud all built their own), but no one has built it on the open standard.

- **No security/compliance-focused SKILL.md player.** Agensi does security review, but it's a lightweight scan + admin check, not a SOC2/ISO-compliant offering. Given the ecosystem tracker's finding that 2,371 skills were flagged as dangerous, there's a trust gap that no one is filling with a serious security-first posture.

- **No vertical-specific SKILL.md marketplaces.** AgentFX dabbles (marketing + trading), but there's no dedicated marketplace for legal skills, medical skills, financial skills, etc. on the open standard. The enterprise players serve verticals but on proprietary platforms.

- **No "App Store for Agents" moment.** The consumer layer is fragmented: ClawHub for OpenClaw, skills.sh for CLI distribution, Agensi for paid, GitHub for Copilot, Claude/ChatGPT/Codex for their own platforms. No single discovery layer dominates.

### Surprises Relative to Working Hypothesis

- **Salesforce predates everything.** The brief hypothesised the market is ~4 months old. The enterprise agent marketplace layer is actually ~13 months old (March 2025). It just uses a different definition of "skill" (Salesforce actions/templates vs SKILL.md).

- **Anthropic's enterprise play is not a skills marketplace.** Two separate enterprise offerings (Claude Marketplace for procurement, Partner Network for services), neither of which is a marketplace for third-party SKILL.md skills. The brief assumed Anthropic had "an enterprise product that involves skills in some form" — the answer is: they have enterprise products that involve *agents*, not *skills* in the SKILL.md sense. The distinction matters.

- **Agensi is bigger and more sophisticated than expected.** 196 skills in ~2 months, Stripe integration, Pro tier ($9/month for unlimited access), IP protection, security review, 80/20 revenue split, MCP-based distribution. This isn't a weekend project — it's a real business being built.

- **Vercel's skills.sh is the npm analogy, not ClawHub.** The brief didn't mention Vercel. But skills.sh has 235K+ weekly installs of its discovery utility and is the primary distribution channel for skills across platforms. ClawHub is an OpenClaw-specific registry. skills.sh is the cross-platform distributor. The analogy isn't "ClawHub is npm" — it's "skills.sh is npm, ClawHub is a language-specific package manager."

- **Skills4Agents is vapor.** Frequently mentioned in articles as a "creator marketplace" but it's still in waitlist. No live product. No skills listed. The articles describing it as a functioning marketplace are recycling its marketing copy.

- **The "market" is actually two markets.** The SKILL.md ecosystem (consumer/open) and the enterprise agent ecosystem (closed/proprietary) are not the same market. They share a concept ("give AI agents specialized capabilities") but they use different formats, serve different buyers, and have different distribution channels. Writing about them as one market would be inaccurate.

---

## 4. ClawHub's Commercialisation Posture

**No commercialisation detected.** ClawHub's positioning is explicitly anti-gatekeeping: "Versioned like npm, searchable with vectors, no gatekeeping." No paid tier, no premium features, no enterprise version, no commission on skills, no monetisation roadmap visible on the public site or in documentation.

This is notable because ClawHub sits at the center of the SKILL.md ecosystem (it's the registry for OpenClaw, the platform with 358K+ GitHub stars) but captures zero revenue from the skills flowing through it. Agensi, a third-party marketplace, monetises skills that may have been discovered or built on ClawHub. ClawHub is the infrastructure layer that others commercialise on top of.

No public roadmap statements about future monetisation were found.

---

## 5. Unanswered Questions for Directed Brief

1. **Salesforce AgentExchange format compatibility.** Does AgentExchange support or plan to support SKILL.md? If Salesforce adopts the open standard, the two market layers would converge. This would be a significant finding but requires more research (beyond public materials — may need to check Salesforce docs or dev forums).

2. **Vercel skills.sh commercialisation plans.** Vercel has 235K+ weekly installs on a free product. Is there a paid tier coming? A premium registry? This is the highest-traffic skills distribution channel and its monetisation plans would reshape the market.

3. **Anthropic's long-term marketplace strategy.** Anthropic built the standard but isn't building a skills marketplace. Will they? The Claude Marketplace (B2B) could potentially host skills in the future. Anthropic's roadmap here is the biggest unknown.

4. **Agensi's actual revenue and transaction volume.** We know 196 skills and Stripe integration, but not GMV, active buyers, or average transaction size. This data isn't public and would require creator surveys or Agensi disclosure.

5. **Skills4Agents launch date.** Currently in waitlist. When it launches, it adds a second paid consumer marketplace. The competitive dynamics between Agensi and Skills4Agents (85% vs 80% creator revenue, Claude-only vs cross-platform) would be significant.

6. **Claude Marketplace (B2B) expansion plans.** Currently 6 partners. Will Anthropic add SKILL.md skills to this marketplace? If so, it becomes an enterprise distribution channel for the open standard.

7. **Precise Agensi launch date.** Reddit post is Feb 18, 2026, but the site may have been live earlier. The actual "first day of operation" isn't confirmed.

---

## 6. Blockers/Issues

- **Web search rate limits.** Hit daily quota on Gemini API. Some searches couldn't be completed. The remaining gaps (above) may be fillable with additional search budget.
- **Ecosystem tracker search API 503.** The tracker's deep report #4 notes "Web search API currently unavailable (503 errors). No fresh news analysis possible this report." This limited the tracker's ability to surface new players in the most recent period.
- **Claude Marketplace vs claude skills market naming confusion.** Anthropic's official "Claude Marketplace" (B2B procurement) is frequently conflated in search results with third-party sites like claudeskillsmarket.com. Required manual disambiguation.
- **Enterprise player data is thin on skills.** Salesforce, Oracle, and Google Cloud publish press releases and partner counts, not detailed marketplace metrics. Understanding their actual transaction volume or skill quality would require access to their platforms.
- **Agensi's JS-rendered site.** The /pro page returns no useful content via fetch. Pricing details came from search synthesis, not direct site scraping. May want to verify with a browser session in the directed research pass.

---

## 7. Data Verification Notes

- [VERIFIED] Salesforce AgentExchange launch date: March 4, 2025 — confirmed via Salesforce press release and multiple tech news sources.
- [VERIFIED] Oracle AI Agent Marketplace: October 15, 2025 — confirmed via Oracle press release from AI World.
- [VERIFIED] Anthropic Agent Skills architecture: October 16, 2025 — confirmed via Anthropic engineering blog.
- [VERIFIED] Open standard release: December 18, 2025 — confirmed via multiple sources.
- [VERIFIED] Vercel skills.sh: January 20, 2026 — confirmed via Snyk blog and dev blog posts.
- [VERIFIED] Anthropic Claude Marketplace: March 6, 2026 — confirmed via SiliconANGLE, VentureBeat, Bloomberg.
- [VERIFIED] Anthropic Claude Partner Network: March 12, 2026 — confirmed via Forbes, Investing.com, Anthropic press release.
- [VERIFIED] ClawHub launch: March 23, 2026 — confirmed via Economic Times India.
- [VERIFIED] Google Cloud AI Agent Marketplace: announced ~April 2025 at Next '25; features live Oct 14, 2025 — confirmed via Google Cloud blog and ARNnet.
- [APPROXIMATE] Agensi launch: ~February 18, 2026 — based on Reddit post. Actual site launch may differ.
- [UNVERIFIED] Skills4Agents: No confirmed launch date. Still in waitlist.
- [UNVERIFIED] claude skills market (.com): Third-party site. No launch date found. No clear relationship to Anthropic.
- [UNVERIFIED] AgentFX Directory: Live but no launch date or pricing model found.
- [UNVERIFIED] Agensi Pro pricing: $9/month from search synthesis, not directly confirmed on the (JS-rendered) site.
- [UNVERIFIED] Agensi revenue split: 80% creator / 20% Agensi + $0.50 from search synthesis, not directly confirmed.

---

*End of exploratory findings. Ready for directed brief.*
