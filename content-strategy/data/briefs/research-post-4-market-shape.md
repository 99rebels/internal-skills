# Research Brief: The Skills Market Already Split. Here's the Half That's Yours.

## Topic & Angle

**Working title:** "The Skills Market Already Split. Here's the Half That's Yours."
**Format:** Analysis
**Sub-type:** Mixed (argument-led with data support)
**Research direction:** Thesis-first (the directed brief committed to a framing; Cambrian's research tested it against available evidence)
**Why now:** The SKILL.md standard is roughly four months old (Anthropic's initial spec was late 2025; first marketplace adoption was early 2026). The enterprise layer has been building in parallel. The split is recent enough that no one has drawn the map clearly for operators — and recent enough that the "where to stand" question is still answerable. This is a keystone post that sets the editorial position for the next several weeks.
**The question or thesis:** The agent skills market has already split into two parallel layers that use different formats, serve different buyers, and don't interoperate — and for operators, the leverage is in the open layer, composing free skills into services rather than selling individual skills.
**Target audience:** Operators — freelancers, solo developers, and small agency owners who want to use agent skills to deliver paid work but aren't sure where to start or what the opportunity actually looks like.
**Target audience (secondary):** Skill authors trying to decide whether to sell skills as products or use them as inputs to services.

---

## Market Context

Four months ago, there was no standardised format for extending AI coding agents. Anthropic published the SKILL.md spec, and within weeks, it was supported by Claude Code, OpenClaw, Cursor, Codex CLI, and others. The standard caught fire: ClawHub (the primary registry) now hosts tens of thousands of skills, and Vercel's skills.sh has millions of weekly installs.

Simultaneously, enterprise vendors — Salesforce, Oracle, Google Cloud, Anthropic itself — began building their own agent capability layers. These use proprietary formats, serve corporate procurement channels, and don't interoperate with the open SKILL.md ecosystem.

The two layers formed in parallel, largely without comment from the analyst or operator community. Most coverage has focused on individual platforms or individual skills. Nobody has drawn the full map and named the split for an operator audience.

Key source links for Claude's additional context:
- Snyk ToxicSkills research: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- arXiv security study: https://arxiv.org/abs/2601.10338
- Agensi marketplace: https://www.agensi.io/skills
- ClawHub: https://clawhub.ai
- Vercel skills.sh leaderboard: https://skills.sh
- Agensi monetization guide: https://www.agensi.io/learn/monetize-ai-agent-expertise-skills
- Agensi "How marketplaces work": https://www.agensi.io/learn/how-ai-agent-skill-marketplaces-work

---

## Data and Evidence

### Data Sources

- **ClawHub live site** (Apr 17, 2026): Verified no pricing page (404), no commercial features visible, no premium tier. JS-rendered skills count could not be scraped — previous data of "48,000+" from prior research is the best available figure but could not be independently re-verified today. [FLAG: ClawHub count not re-verified. Use "tens of thousands" or note the 48K figure is from prior research.]
- **Agensi live site** (Apr 17, 2026): Skill count, pricing, revenue split, categories, skill requests page, leaderboard, learn articles.
- **Vercel skills.sh leaderboard** (Apr 17, 2026): Updated install counts for top skills.
- **Snyk "ToxicSkills" research** (published Feb 2026): Primary source verified at https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- **arXiv security paper** (published Jan 15, 2026): Verified at https://arxiv.org/abs/2601.10338
- **OpenClaw GitHub API** (Apr 17, 2026): Verified star count, repo metadata.
- **Ecosystem radar reports** (Apr 6, Apr 11, Apr 16, 2026): Platform tracking, new entrants, enterprise moves.
- **Hacker News API** (Algolia): Searched for operator examples, Show HN posts, relevant comments.
- **Agensi learn articles** (Mar 15–Apr 16, 2026): Monetization guide, marketplace explainer, SKILL.md explainer, Env Doctor case study.

### Key Findings

**1. The open layer is enormous relative to the commercial layer.**

ClawHub hosts tens of thousands of skills (48,000+ per prior research, not re-verified today). Vercel skills.sh's top skill families have cumulative installs in the millions (Microsoft Azure: 3.8M; pbakaus/impeccable: ~900K across variants; larksuite/cli: ~1.17M across variants; xixu-me/skills: 400.5K; coreyhaines31/marketingskills: ~304K across variants). The `find-skills` CLI tool had 235K+ weekly installs at last check (exploratory pass data).

Against this: Agensi, the only working commercial marketplace for SKILL.md skills, has **197 skills** as of April 17, 2026 (confirmed from the live "All Skills" page showing "All Skills (197)"). This is up from 196 the previous day. Growth is essentially flat — roughly one skill per day or less.

The volume ratio between free/open skills and commercially listed skills is at least 250:1, likely much higher. Commercial skill-selling is a rounding error in the open layer.

**2. The commercial layer has a dual model, not just one-time sales.**

Agensi has two revenue channels:
- **One-time skill purchases**: Creators keep 80%, Agensi takes 20%. Prices range from free to $15-20 for specialised skills. Buyer-fingerprinted downloads. (Source: Agensi monetization article, Apr 15, 2026; Agensi marketplace explainer, Mar 20, 2026)
- **Pro subscription**: $9/month (or $90/year early-bird, regular annual $190). Provides MCP server access to load and use any skill from the marketplace on demand. Works with 20+ agents. (Source: web search citing agensi.io/pro; the page itself is JS-rendered and could not be directly fetched)

[FLAG: The brief mentioned "$0.50 per sale" in addition to the 80/20 split. I could not verify this from any Agensi article I accessed. Their own monetization guide and marketplace explainer only mention the 80/20 split. The $0.50 may exist on the Pro page or in their terms of service (not checked). Recommend Claude verify before using.]

**3. Local businesses are commissioning branded skills — but as products, not compositions.**

Agensi's marketplace includes a notable cluster of white-label skills from local service businesses:
- AI Plumbing Services Tool — F&P Plumbing
- AI Automotive Sales Tool — Grand Subaru
- AI HVAC Services Tool — GR Heating & Cooling
- AI HVAC Services Tool — Oasis Air Arizona
- AI Roofing Services Tool — Four Peaks Roofing Pros
- AI Event Planning Tool — Clearwater Events
- AI Cleanroom Solutions Tool — Cleanroom Design
- AI Facilities Management Tool — CPL Group
- AI Engineering & Workforce Solutions Tool — Advantage Technical
- AI Digital Solutions Tool — Erodex
- AI Digital Marketing Tool — Spark Media
- AI Business Solutions Tool — Rostrup

These are custom, branded skills commissioned by real businesses. They represent genuine demand from non-technical businesses for AI-powered customer-facing tools. However, they are **single custom products**, not compositions of free skills. The businesses are paying for bespoke builds, not assembling free skills into workflows.

This is an important nuance: demand exists, but it's manifesting as product commissions, not as skill composition. The "compose free skills" thesis isn't wrong, but the market hasn't discovered it yet — businesses are going direct to custom builds.

**4. Security concerns are real and quantified.**

Two independent studies with different methodologies both found significant security issues:

**Snyk ToxicSkills** (Feb 2026):
- Sample: 3,984 skills from ClawHub and skills.sh (as of Feb 5, 2026)
- 13.4% (534 skills) had at least one CRITICAL-level security issue
- 36.82% (1,467 skills) had at least one security flaw (any severity)
- 76 confirmed malicious payloads (credential theft, backdoor installation, data exfiltration)
- 8 malicious skills still live on ClawHub as of publication
- Methodology: mcp-scan engine (multi-model analysis + deterministic rules), human-in-the-loop review
- Source: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/

**arXiv "Agent Skills in the Wild"** (Jan 15, 2026):
- Sample: 42,447 skills collected from two major marketplaces; 31,132 analyzed using SkillScan
- 26.1% of skills contained at least one vulnerability across 14 distinct patterns
- Data exfiltration: 13.3%; privilege escalation: 11.8%
- 5.2% exhibited high-severity patterns strongly suggesting malicious intent
- Skills with executable scripts 2.12x more likely to contain vulnerabilities (OR=2.12, p<0.001)
- Detection: 86.7% precision, 82.5% recall
- Source: https://arxiv.org/abs/2601.10338

Both studies are from Jan-Feb 2026. The security landscape may have improved since (ClawHub added moderation policies visible at clawhub.ai/about; Agensi runs 8-point security scans). But the baseline is concerning and should be referenced accurately.

**5. The enterprise layer is real but sealed off from operators.**

From the exploratory findings and ecosystem radar tracking:
- **Salesforce AgentExchange**: Proprietary agent format, partner-only access, enterprise procurement
- **Oracle AI Agents**: Proprietary format, Oracle Cloud integration
- **Google Cloud Vertex AI Agent Builder**: Proprietary, Google Cloud-native
- **Anthropic enterprise moves**: Procurement and partner programs (not a marketplace for third-party SKILL.md skills)
- **Microsoft Copilot Studio**: Proprietary agent format, M365/Power Platform integration

None of these use SKILL.md. None interoperate with ClawHub, Agensi, or skills.sh. None are accessible to individual operators without enterprise partnerships.

OpenClaw itself sits in the open layer: 359,215 GitHub stars as of Apr 17, 2026 (verified via GitHub API). Created Nov 24, 2025. MIT license. Its massive adoption validates the open standard but doesn't bridge the enterprise gap.

**6. Skills4Agents and other potential commercial platforms have not shipped.**

Skills4Agents (skills4agents.com): Still in waitlist as of Apr 17, 2026. "Coming soon" messaging, no skills listed, no pricing page. The skills shown on the homepage appear to be demo/placeholder content.

No other significant new commercial skill marketplace has emerged since the exploratory pass on Apr 16, 2026.

### The Most Surprising Finding

**The operator examples gap.** The directed brief asked for 3-4 concrete examples of operators using composed skills to do real, paid, practical work in the last 60 days. Despite extensive searching across Hacker News (multiple query combinations via Algolia API), Reddit (blocked from access), Medium, dev.to, web search (20+ queries), and Agensi's own content, **I could not find a single clear, documented example of an operator composing free skills from ClawHub or skills.sh into a workflow that delivers paid services to a client.**

This absence is itself significant data. It means the "compose free skills to deliver work" thesis, while logically sound, is **aspirational rather than demonstrated**. The market has the supply (tens of thousands of free skills) but the demand-side awareness and composition patterns haven't materialised publicly yet.

What I did find (see Counterexamples section below) are adjacent signals — people using AI coding tools for client work, people building skills for professional use cases, and businesses commissioning custom skills — but none are the specific pattern the post's argument rests on.

### Counterexamples and Complications

**1. Adjacent but not matching — AI agency using coding tools (not skills) for client work:**

Jignesh Mandana (HN comment, Apr 8, 2026, on "Ask HN: Who is hiring?") runs "Pixel Elevate, an AI automation agency" and has "built and delivered systems for clients across the US, UK, and Canada." He uses "Aider + Claude Code + Cursor as daily drivers." This is a real operator doing paid AI work — but he's using the coding tools directly, not composing skills from marketplaces. The skills-as-composition pattern isn't visible in his description.

**2. Adjacent but not matching — skill builders with professional use cases:**

- Matt Berg / recodelabs (Show HN, Jan 22, 2026): Built a Lima devbox skill and wrote: "this really hits home for me that Agent Skills is really all you need. Instead of writing a guide or wrapping this up in a app/TUI just bake any knowledge or process you want to automate and share into a skill." He clearly grasps the composition vision but describes building skills, not composing them for client work.
- vassiliylakhonin (Show HN, Feb 18, 2026): Built a nonprofit logic model skill for grant workflows. Professional domain (NGO grant writing), but again: building a skill, not composing skills into a service delivery workflow.

**3. Supporting the thesis — local businesses commissioning custom skills:**

The Agensi white-label skills (plumbing, HVAC, roofing, etc. — listed in Finding 3 above) show that non-technical businesses see value in AI-powered skills. But they're treating skills as custom products, not as compositions of free skills. This supports the broader "demand exists" claim but undercuts the "composition is the play" claim by showing that the market's first instinct is to commission custom builds.

**4. Enterprise adoption of OpenClaw — but not skill composition:**

Faraday Future is integrating OpenClaw into the FX Aegis robot for autonomous food delivery (from Apr 16 ecosystem radar report). This is enterprise adoption of the open agent, but it's a single embedded use case, not skill composition.

### What the Data Can't Tell Us

- **Actual install vs. page-view ratios on ClawHub**: We know from prior research that download counts include listing page views, not just installations. The real install base is unknown.
- **How many operators are composing skills privately without publishing about it**: The absence of public examples doesn't prove the absence of private practice. Operators doing client work may not be blogging about it.
- **Agensi's actual revenue and transaction volume**: We have skill counts and pricing but no sales data.
- **The enterprise layer's actual skill volume**: Enterprise agents exist (Salesforce, Oracle, etc.) but there's no public data on how many "skills" or "actions" they contain or how widely they're deployed.
- **Whether the Feb 18 vs early March launch date discrepancy for Agensi matters**: The brief says "Reddit post Feb 18 was the anchor." The evidence suggests the marketplace itself launched in early March, but the concept or domain may have existed earlier. This is a factual detail, not a load-bearing claim for the post's argument.

---

## Argument Structure (for argument-led or mixed posts)

**Thesis:** The agent skills market has already split into two parallel layers that use different formats, serve different buyers, and don't interoperate — and for operators, the leverage in the open layer is in composing free skills into services, not selling individual skills.

**Supporting evidence:**

1. **The split is real and structural.** Enterprise layer (Salesforce, Oracle, Google Cloud, Anthropic partner programs) uses proprietary formats, serves corporate procurement, and is sealed off from individual operators. Open layer (ClawHub, skills.sh, Agensi, OpenClaw, Claude Code) uses SKILL.md and is accessible to anyone. No interoperation between the two. No enterprise player has adopted SKILL.md. (Sources: exploratory findings, ecosystem radar reports, live site checks Apr 17, 2026)

2. **The open layer dwarfs the commercial layer.** ClawHub: tens of thousands of skills. Agensi (the only working commercial marketplace): 197 skills. skills.sh: millions of weekly installs, all free. The commercial skill-selling volume is negligible relative to the open flow. (Sources: ClawHub, Agensi live site, skills.sh, Apr 17, 2026)

3. **Demand from non-technical businesses exists but manifests as custom commissions, not skill composition.** Local businesses (plumbing, HVAC, roofing, automotive, etc.) are commissioning branded skills on Agensi — real money changing hands for real business needs. But they're buying custom products, not assembling free skills. The demand is there; the composition pattern hasn't been discovered yet. (Source: Agensi skills listing, Apr 17, 2026)

4. **Anthropic created the standard and stepped back from the commercial layer.** The SKILL.md spec came from Anthropic, but Anthropic's own enterprise moves are procurement and partner services, not a marketplace for third-party skills. The standard-setter isn't trying to own the commercial layer, which keeps the space open. (Sources: exploratory findings, Agensi articles citing Anthropic)

5. **Security concerns create a trust gap that composition can address.** 13.4% of skills (Snyk) or 26.1% (arXiv) have security issues. An operator who vets and composes skills into a trusted workflow provides value that downloading individual skills from a marketplace doesn't. The security data makes composition not just a convenience play but a trust play. (Sources: Snyk Feb 2026, arXiv Jan 2026)

**Strongest counterargument:**

**The composition thesis is aspirational, not demonstrated.** I could not find a single documented example of an operator composing free skills into a paid workflow. The market has supply (thousands of free skills) but no visible pattern of demand-side composition. The brief's own analysis layer says "the supply side has outpaced the demand-side awareness" — but this is an inference, not evidence. The counterargument is: maybe the composition play doesn't exist yet because the skills aren't good enough, composable enough, or the workflow orchestration isn't mature enough. Maybe the real play IS selling individual skills (Agensi's model), and the composition thesis is a theory that won't materialise for 12-18 months or longer.

This counterargument is strong and honest. The post needs to account for it. The thesis holds as a structural observation (the split is real, the open layer is where operators live) but the "composition is the leverage" claim has weaker evidential footing than the brief assumes. Recommend Claude considers hedging this claim or reframing it as "here's where the leverage will be" rather than "here's where the leverage is."

**Historical analogy (if found):**

The brief says Claude will handle historical framing. I'll surface candidates:
- **npm (2010-2012):** Early npm had thousands of free packages and almost no paid ones. The composition play (assembling free packages into applications) far outstripped the individual-package-selling play. The money was in what you built with packages, not in selling packages. This is the closest parallel.
- **WordPress plugins (2005-2010):** Free plugins dominated. The money was in composing plugins into client websites (agencies), not in selling individual plugins. Premium plugins eventually emerged but were always a fraction of the ecosystem's value.
- **Mobile App Store (2008-2010):** Different pattern — paid apps were central from the start. Not a good parallel for skills.

**Strength of evidence:**

- **Rock-solid:** The two-layer split exists and is structural (multiple sources, cross-verified). Agensi's 197-skill count (live site). Snyk and arXiv security numbers (primary sources). OpenClaw GitHub stars (API-verified). Skills4Agents still in waitlist (live site). No ClawHub commercialization signals (404 on pricing page).
- **Strong:** The open-layer-dwarfs-commercial-layer argument (multiple data points, consistent direction). The local-business demand signal (Agensi listings). Anthropic's non-involvement in the commercial layer (consistent across sources).
- **Moderate:** The composition-as-leverage claim (logically sound, supported by historical analogies, but NOT demonstrated by current operator examples). The "demand-side awareness gap" claim (inference from absence of examples, not positive evidence).
- **Weak/Unverified:** The $0.50 per sale fee on Agensi (could not find in any accessible source). The exact ClawHub skill count (could not re-verify today).

**Testable prediction:**

If this analysis is right, within 6 months (by October 2026) we should see: (a) at least one publicly documented case study of an operator composing free skills into a paid workflow, (b) the first "skill stack" templates or workflow recipes appearing on ClawHub or similar platforms, or (c) a services marketplace where operators sell outcomes built on composed skills rather than selling individual skills. If none of these materialise, the composition thesis needs revisiting.

---

## Candidate "So What" Synthesis

For the primary audience (operators — freelancers, solo devs, small agencies):

The map has been drawn while you weren't looking. There are two markets, and only one of them is yours. The enterprise layer (Salesforce, Oracle, Google Cloud) is real and growing, but it's not accessible to you — proprietary formats, partner-only access, corporate procurement. Forget it. The open layer (ClawHub, skills.sh, OpenClaw, Claude Code) is where you live, and inside it, the opportunity isn't what the early hype suggests.

The obvious play — "sell skills on a marketplace" — is tiny. Agensi, the only marketplace that actually works, has 197 skills after two months. The real volume is in the tens of thousands of free skills flowing through the open layer. The gap is between that massive supply and the almost-zero awareness on the demand side that these are composable building blocks for real services.

The local businesses commissioning custom skills on Agensi (plumbers, HVAC companies, roofing firms) prove that non-technical businesses want AI-powered services. They're just going about it the expensive way — commissioning bespoke builds instead of composing free skills. An operator who figures out composition first has a structural advantage.

For the secondary audience (skill authors):

The same data suggests a portfolio strategy: build free skills for reach and reputation, and use those skills as inputs to service offerings rather than trying to sell them individually at $5-15 on a 197-skill marketplace.

---

## Candidate Action Layer

1. **Stop watching the enterprise layer.** It's interesting context but it's not your market. The formats don't interoperate, the access is sealed, and the buyers aren't your buyers.

2. **Reframe skills as inputs, not products.** The person who composes a free code-review skill + a free deployment-checklist skill + a free security-audit skill into a "launch readiness audit" service for $500 wins more than the person who sells one of those skills for $9 on Agensi.

3. **Watch the local-business signal.** The white-label skills on Agensi (plumbing, HVAC, roofing) show that non-technical businesses will pay for AI-powered services. These businesses don't know about ClawHub or skills.sh. The operator who bridges that gap has first-mover advantage in a vertical.

4. **Vet aggressively.** With 13-26% of skills having security issues, composition without vetting is liability. The operator's value isn't just in assembling skills — it's in curating and vetting them so the client doesn't have to.

5. **Come back for the next posts.** This post draws the map. The Explainer (week 2) will show readers how to evaluate skills. The Stack Play (week 4) will demonstrate a concrete composed workflow in a specific vertical. The map is the setup; the Stack Play is the first payoff.

---

## Caveats

1. **The operator examples gap is the biggest caveat.** The "compose free skills to deliver paid work" thesis is logically sound and historically grounded (npm, WordPress parallels) but has zero documented real-world examples as of April 17, 2026. The post should be honest about this. If the thesis were "the App Store model will work for skills," the evidence would be stronger than it is for "composition is the play." Recommend the post frame composition as an emerging opportunity rather than a proven pattern.

2. **Agensi's $0.50 per sale fee is unverified.** The directed brief mentions "80% to creators + 20% to Agensi + $0.50 per sale." I verified the 80/20 split from multiple Agensi articles but could not find the $0.50 fee mentioned anywhere. It may exist on the JS-rendered Pro page or in their terms of service (not checked). Do not use without verification.

3. **ClawHub skill count could not be re-verified today.** Previous data of "48,000+" is the best available. The site is fully JS-rendered and the API's listing endpoint returned empty results. The count could have changed significantly. Use "tens of thousands" for safety or note the figure's provenance.

4. **The security data is from Jan-Feb 2026.** Both the Snyk and arXiv studies are three months old. ClawHub has since added moderation policies (visible at clawhub.ai/about) and Agensi runs security scans. The current security landscape may be better — or worse. The numbers are accurate as snapshots but may not reflect the current state.

5. **The Agensi launch date in the exploratory findings appears incorrect.** The brief says "Reddit post Feb 18 was the anchor." Evidence suggests the marketplace launched in early March 2026 (a March 17 Reddit post says "two weeks ago"; by March 11 it had 100 skills; Agensi's learn articles started March 15-20). The Feb 18 date may refer to when the concept was first posted, not the marketplace launch. This is a minor factual detail but should be corrected if the post references a specific launch date.

6. **Vercel skills.sh numbers are from the live leaderboard but methodology is opaque.** The install counts are visible but it's unclear whether they represent unique installs, total installs, or some other metric. They're directionally useful but shouldn't be treated as precise.

7. **The "demand-side awareness gap" is an inference from absence, not positive evidence.** I couldn't find operators composing skills, but that doesn't mean nobody is. Private operators doing client work may not publish about it. The gap is real as a public phenomenon but may not reflect private practice.

---

## Quotable Moments

1. **"All Skills (197)"** — The literal text on Agensi's browse page as of April 17, 2026. Against ClawHub's tens of thousands and skills.sh's millions of installs, 197 is the number that makes the "commercial skill-selling is tiny" claim visceral.

2. **"Agent Skills is really all you need. Instead of writing a guide or wrapping this up in a app/TUI just bake any knowledge or process you want to automate and share into a skill."** — Matt Berg / recodelabs (Show HN, Jan 22, 2026). This is the composition vision articulated clearly by a builder, even though he was describing building rather than composing.

3. **The white-label skills cluster.** Seeing "AI Plumbing Services Tool — F&P Plumbing" and "AI HVAC Services Tool — GR Heating & Cooling" alongside code-review and testing skills on the same marketplace is jarring. It shows the market pulling in two directions simultaneously — developer tooling and local business services — without either side noticing the other.

4. **"13.4% (534 skills) had at least one CRITICAL-level security issue"** — Snyk ToxicSkills. Nearly one in seven skills on the open layer has a critical security problem. This is the number that makes the "operator as curator" value proposition concrete.

5. **"The SKILL.md ecosystem is at that same early stage"** — Agensi's own monetization guide (Apr 15, 2026), comparing the skills market to early mobile app stores and WordPress themes. When the marketplace itself says "we're early," the reader should pay attention.

---

## Candidate Framings

**These are suggestions, not prescriptions. Claude has the authority to pick a different framing at drafting time based on the raw material in the brief.**

- **Candidate primary framing:** The market already split and most operators don't know it. Two maps, two formats, two buyer types — and you only need to care about one. Inside that one, the leverage isn't where the hype is (selling skills) — it's in composing free skills into services.
- **Candidate spine:** The ratio — 197 commercial skills against tens of thousands of free ones. That single number makes the "don't sell skills, compose them" argument viscerally clear.
- **Alternative framing:** If the operator examples gap makes Claude uncomfortable with the composition thesis, an alternative frame is: "Here's the map. The enterprise layer is sealed off. The open layer is enormous but chaotic and insecure. Someone needs to make sense of it. That someone could be you." This drops the composition claim and leads with the curation/trust opportunity instead.
- **Candidate hook:** Open with the split — "Four months ago there was one market. Now there are two, and they don't talk to each other." Counter-intuitive because most coverage treats it as one space.
- **Candidate closing:** "The map is drawn. The next few posts show you how to walk it." Sets up the editorial calendar and gives the reader a reason to subscribe.
- **Tone guidance:** Measured and committed, per the directed brief. The finding is interesting because it's counterintuitive and already done, not because it's breaking news. Voice of reason looking at a chaotic space and saying, calmly, here's what actually happened and here's where to stand. Don't oversell the composition thesis — hedge honestly where the evidence is thin.

---

## Research Notes

### Numbers Requiring Claude's Re-verification at Draft Time

- **Agensi $0.50 per sale fee**: Could not verify. Check agensi.io/pro (JS-rendered) or Agensi terms of service.
- **ClawHub total skill count**: Could not re-verify today. "48,000+" is from prior research. Consider re-checking via the ClawHub API or site closer to publish date.
- **Vercel skills.sh `find-skills` weekly install count**: Was 235K+ in exploratory pass. May have changed.

### Agensi Pro Details (from web search, citing agensi.io/pro)

- $9/month or $90/year (early-bird pricing)
- Regular annual price: $190/year
- Early subscribers locked in at $9/month forever
- Provides MCP server access to all marketplace skills on demand
- Works with 20+ agents (Claude Code, Cursor, Codex CLI, VS Code, Gemini CLI)
- Individual skills still available as one-time purchases (separate from Pro)
- Source: web search result (primary page is JS-rendered, could not fetch directly)

### Vercel skills.sh Leaderboard (Apr 17, 2026, live site)

Top entries by install count:
- Microsoft Azure (multiple skill families): 3.8M cumulative
- Microsoft GitHub Copilot for Azure: 2.1M
- pbakaus/impeccable (multiple variants): ~900K cumulative
- larksuite/cli (multiple variants): ~1.17M cumulative
- xixu-me/skills: 400.5K
- coreyhaines31/marketingskills (multiple variants): ~304K cumulative
- skillssh/skills: 74.0K

### OpenClaw GitHub (verified Apr 17, 2026 via GitHub API)

- Stars: 359,215
- Description: "Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞"
- Created: Nov 24, 2025
- Last updated: Apr 17, 2026
- Open issues: 18,989

Note: Agensi's articles cite "247K+ GitHub stars" for OpenClaw — this is stale data. The actual count is 359K+. The discrepancy suggests Agensi's articles were written with data from several weeks ago.

### Agensi Launch Date Correction

The exploratory findings' Feb 18 anchor date appears to be incorrect for the marketplace launch. Evidence:
- Mar 11 Reddit post: Agensi already had 100 skills
- Mar 17 Reddit post: "launched two weeks ago" → implies ~Mar 3 launch
- Agensi learn articles: first published Mar 15, 2026 ("Create SKILL.md from Scratch")
- Agensi marketplace explainer: published Mar 20, 2026
- Agensi monetization guide: published Apr 15, 2026
- Agensi SKILL.md explainer: published Apr 13, 2026

The Feb 18 date may refer to an earlier concept post or domain registration. The marketplace itself appears to have launched in early March 2026.

### Searches Performed (for traceability)

- Web search: 20+ queries covering Agensi, ClawHub, skills.sh, operator examples, security data, enterprise players, Snyk, new entrants. Search API hit daily quota (20 requests) partway through.
- HN Algolia API: 12+ queries across stories and comments, various date filters and keyword combinations.
- Direct web fetches: Agensi (homepage, skills, pro, learn articles, requests, leaderboard), ClawHub (homepage, skills, about, pricing, API), skills.sh (leaderboard), Skills4Agents, Snyk blog, arXiv, Medium, dev.to.
- GitHub API: OpenClaw repo stats.
- ClawHub CLI: search commands (limited by lack of --json flag and empty listing API response).

### Files Consulted

- `exploratory-post-4-market-shape.md` — full 17-player table, timeline, patterns
- `brief-analysis.md` — research methodology and brief structure
- `brief-universal.md` — division of labour, pipeline flow
- `cambrian-research-philosophy.md` — five rules, posture alignment
- `cambrian-readme.md` — pipeline overview
- Ecosystem radar reports: Apr 6, Apr 11, Apr 16, 2026
- Ecosystem radar known-findings.json

### What I'd Research With More Time/Access

- **Reddit threads**: Reddit blocked all access (403). The r/claude, r/ClaudeAI, and r/Entrepreneur subreddits likely contain operator examples that I couldn't access.
- **Twitter/X**: No access. Operator stories are likely shared there.
- **YouTube**: No comprehensive search. Walkthrough videos of composed skill workflows may exist.
- **LinkedIn**: No comprehensive search. Agency/freelancer posts about AI skill workflows may exist.
- **Agensi Pro page**: JS-rendered, couldn't fetch. May contain the $0.50 fee details and more precise Pro feature breakdown.
- **Agensi terms of service**: Not checked. May contain fee structure details.
- **ClawHub API listing endpoint**: Returned empty results. The total count may be accessible via a different endpoint or with authentication.
