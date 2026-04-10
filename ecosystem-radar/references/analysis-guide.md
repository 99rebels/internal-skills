# Analysis Guide

How to interpret ecosystem data and produce useful trend reports.

## Growth Indicators

### Strong Growth Signal
- Skill download counts increasing 15%+ over 5 days on any tracked skill
- ClawHub velocity (unique slugs) growing steadily
- Agensi adding 3+ new skills per run
- GitHub star growth accelerating across platform repos
- New platforms appearing
- Existing platforms adding payment features

### Flat / Slow Signal
- Download counts stable (<5% change over 5 days)
- No new platforms detected
- No payment feature changes
- Same top skills dominating (low churn)
- GitHub star growth linear (not accelerating)

### Contraction Signal (Rare)
- Download counts decreasing across multiple skills
- Platforms shutting down or going dormant
- Skills being removed from marketplaces
- Negative community sentiment

## Payment Tracking

### Payment Adoption Stages
1. **No payments** — pure open sharing (most platforms currently)
2. **Tips/donations** — optional support
3. **Freemium** — basic free, premium paid
4. **Full marketplace** — all skills can be priced, platform takes commission
5. **SaaS marketplace** — recurring subscriptions, usage billing

**Current status (Apr 2026):**
- Agensi: Stage 3-4 (Stripe confirmed, commission/payout terms detected)
- ClawHub: Stage 1 (no payments)
- Others: Unknown

### What to Watch For
- Any platform moving from Stage 1 → 2+ (the inflection point)
- Commission rates appearing (tells you about platform maturity)
- "Creator economy" features being added (payouts, analytics, dashboards)

## Platform Adoption (GitHub Stars)

### Why This Matters
Skills need platforms to run on. More users on Claude Code/OpenClaw/Codex = bigger potential market for skill creators.

### What to Track
- **Absolute stars** — which platforms have the most users?
- **Star growth rate** — which platforms are growing fastest? (percentage change)
- **Release velocity** — how often are platforms updating? (active development = healthy ecosystem)
- **Issue count trends** — growing issues = growing pains (usually good for early market), shrinking = maturing

### Key Comparison
Compare growth rates, not absolute numbers. A platform with 10k stars growing 20%/week is more interesting than one with 100k stars growing 2%/week.

## ClawHub Velocity

### How It Works
We run 20 broad search queries, each returning up to 200 results, then deduplicate slugs. This gives us ~1,733 unique skills (not a true total, but a consistent sample).

### What Changes Mean
- **Unique slugs increasing** → new skills being published (marketplace growing)
- **Unique slugs stable** → flat growth or churn balancing new additions
- **Unique slugs decreasing** → skills being removed/deprecated faster than new ones

## Agensi Skill Diffing

Each run stores the full list of skill slugs. Between runs we can detect:
- **New skills added** → marketplace is growing
- **Skills removed** → possible quality pruning or developers leaving
- **Net change** → overall trajectory

## News & Sentiment (Deep Reports)

### Deduplication Rules
**This is the most important section for token efficiency.**

1. Read `data/last-report.json` BEFORE searching — check `articleHeadlines` to skip already-reported articles
2. Read `data/known-findings.json` BEFORE reporting any fact — if the finding exists and hasn't changed, don't report it again
3. Run ALL 16 search queries for full coverage, then deduplicate results by headline/URL
4. When reporting, only include: genuinely new articles, updated facts (version changes, payment changes), and new platforms
5. If nothing new happened, say so explicitly: "No significant developments since last report."

### What to Look For
- **Platform announcements** — new features, skill stores, payment integrations
- **Funding rounds** — money flowing into agent tooling = market confidence
- **Community activity** — blog posts, Twitter/X discussions, Hacker News threads
- **Competitive moves** — Cursor, Windsurf, etc. adding skill/rule support

### How to Report
- Don't just list articles — extract the *signal*: "Cursor added a rules marketplace" is a signal. "Blog post about Claude Code" is not.
- Prioritize: payment announcements > new platforms > feature updates > community chatter
- If nothing notable happened, say so — don't invent trends from noise.

## Trend Reporting Style

- Be specific: "47 new skills on ClawHub in 3 days" not "skills are growing"
- Use directional arrows: ↑ ↓ →
- Contextualize: "15% growth in 5 days" means more than "15% growth"
- Compare platforms: "Claude Code stars growing 3x faster than OpenClaw" (relative > absolute)
- Flag uncertainty: "Approximate count due to scrape limitations"
- Don't over-interpret single data points — trends need 3+ data points
