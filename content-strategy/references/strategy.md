# Content Strategy — "The Skills Economy"

## Context

ClawHub has 48,000+ skills. Most are low quality or dangerous (2,371 flagged in recent audit). Nobody is doing honest, tested reviews or practical "how to automate X" content in this space. The content operation is designed to fill that gap and build audience, credibility, and domain authority.

## Target Audience

**Primary:** Entrepreneurs, freelancers, small business owners, agency operators
**Secondary:** Developers exploring agent skills, AI builders

These are people who want practical outcomes — save time, save money, automate workflows — not ecosystem analysis. They'll find us through search and social, stay because the content is genuinely useful.

## Content Formats

### Format 1: Skill Teardowns
"I tested X skill — here's what actually works"

**Structure:**
- Hook: the problem the skill claims to solve
- What it does (brief, factual)
- Installation & setup experience
- Testing methodology (what we tested, how)
- What works well (specific examples)
- What doesn't (honest gaps)
- Security/quality assessment
- Verdict: recommend, conditionally recommend, or skip
- CTA: link to ClawHub skill page

**Rules:**
- Always actually install and test — never review based on reading the SKILL.md
- Be honest about failures — that's what builds trust
- Include screenshots/terminal output as evidence
- Compare against alternatives if they exist

### Format 2: Workflow Listicles
"X free AI skills that automate [painful workflow]"

**Structure:**
- Hook: the pain point (time spent, money wasted, frustration)
- The skill stack: 2-5 skills that solve the problem end-to-end
- How each skill contributes (brief, specific)
- How to set up the workflow
- Real results / time saved / money saved
- CTA: install links for each skill

**Rules:**
- Every skill must be tested in combination, not individually
- Calculate actual time/money savings if possible
- Be realistic — don't overstate what the skills can do
- Include caveats and gotchas

## Publishing

**Primary:** Substack — canonical source, subscriber ownership, discoverability through Substack's recommendation network
**Secondary:** LinkedIn (shortform hook posts linking to Substack) — audience building, professional reach
**Syndication:** dev.to (cross-posts linking back to Substack) — catches developer audience

**Strategy:** Build an owned subscriber list on Substack. Use LinkedIn hooks to drive traffic. Use dev.to for broader reach. All roads lead back to Substack — no SEO work for third-party platforms.

**Cadence:** One post per week, alternating between teardowns and listicles

## Content Ideation

**Interactive, not automated.** Rian asks "what should we write about this week?" → I research trending skills, ecosystem data, and generate 3-5 ideas with angles.

**Sources for ideas:**
- Ecosystem radar data (trending downloads, new skills, growth patterns)
- ClawHub explore/search for specific categories
- Real problems Rian encounters building skills
- User pain points from skill reviews/comments
- Gap analysis: crowded categories vs underserved ones
- Seasonal relevance (tax season, new year planning, etc.)

**Cron-assisted monitoring (optional):** A light weekly check that notes:
- Skills with big download spikes
- New skills in high-value categories
- Ecosystem news worth writing about
- This feeds into ideation but doesn't auto-generate content

## Skill Safety Protocol

When testing skills for reviews, safety is non-negotiable:

1. **Pre-install check:** Run `clawhub inspect` and review the security rating
2. **Skip suspicious skills:** Any rating of "dangerous" or "critical" — do not install
3. **Review the code:** Before running, read all scripts and check for:
   - Credential exfiltration (reading env vars, config files, ssh keys)
   - External network calls (API requests to unknown endpoints)
   - File system access outside expected paths
   - obfuscated code or encoded payloads
4. **Sandbox consideration:** If available, run skills in a sandboxed environment
5. **Post-test cleanup:** Delete all installed skill files after testing
6. **Never store credentials:** Don't set up OAuth or API keys for testing — mock the data if needed
7. **Document safety findings:** Include security assessment in every teardown

## Brand & Voice

**Tone:** Practical, honest, concise. Not hype-driven. "I tested this for 2 hours so you don't have to" energy.

**What we are:**
- Honest reviewers who actually test things
- Practical guides for non-technical users
- A quality filter in a noisy marketplace

**What we are NOT:**
- A ClawHub promotional channel (we review skills across platforms)
- A dev tutorial blog (we focus on outcomes, not code)
- A hype machine (we're honest about what doesn't work)

## Data & Tracking

### Content Calendar
Track ideas, drafts, and published posts:
- `data/ideas.md` — content backlog with status (idea → researching → drafting → published)
- `data/published.json` — published posts with platform, date, URL, topic, skills covered

### Metrics (early stage)
- Substack subscribers (primary metric — you own this list)
- Substack open rates / read ratios
- LinkedIn engagement (comments, shares, click-throughs to Substack)
- dev.to views and reactions
- Inbound interest (people reaching out, referencing posts)

## Platform Setup (TODO)

- [x] Substack account
- [x] LinkedIn account
- [x] dev.to account
- [ ] First post published
- [ ] LinkedIn posting cadence established
- [ ] dev.to cross-posting workflow tested

## First Post Ideas

1. "I Tested Every Expense Tracking Skill on ClawHub — Here's What Actually Works" (teardown comparison — draws on our invoice-extractor expertise)
2. "5 Free AI Skills That Replace €50/Month in SaaS Subscriptions" (listicle — high shareability)
3. "The ClawHub Security Problem: I Audited 50 Random Skills" (if we have data to back it up — strong HN/Reddit potential)

## Relationship to Other Skills

This content skill connects to:
- **ecosystem-radar** — source of market data and trending insights
- **invoice-extractor** — our own builds are content opportunities
- **agent-portability-checker** — used during skill testing for safety reviews
- **skill-polisher** — could be a teardown subject itself
