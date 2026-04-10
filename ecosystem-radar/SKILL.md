---
name: ecosystem-radar
description: Monitor the agent skill marketplace ecosystem. Track platform growth, payment adoption, platform health, and news to spot monetization trends. Use when checking market trends, ecosystem health, or getting an ecosystem pulse.
metadata: { "openclaw": { "emoji": "📡" } }
---

# Ecosystem Radar

Track the agent skill marketplace ecosystem — growth, payment adoption, platform health, and news. The goal is to spot trends that indicate a monetization market is forming around agent skills.

## When to Use

- User asks about skill marketplace trends or ecosystem health
- Running a scheduled pulse or deep report
- Checking if new marketplaces or payment features have appeared
- Looking for news about OpenClaw, Claude Code, Codex, or the broader skills ecosystem

## Active Platforms

| Platform | Data Source | What We Track |
|----------|------------|---------------|
| ClawHub | CLI (`clawhub inspect` + `clawhub search`) | Specific skill downloads, stars |
| Agensi | Web scrape | Total skill count, new skills (via slug diff), payment status |
| GitHub | GitHub API | Stars/forks for openclaw, clawhub, claude-code, codex repos |

**Disabled:** OpenAgentSkill (JS-rendered, unreliable), SkillsMP (Cloudflare blocked), LobeHub (no API).

## Modes

### `pulse` — Daily check

Numbers snapshot + change detection. Run daily via cron.

**Steps:**
1. Run `python3 scripts/collect.py --output data/latest-raw.json`
   - Fetches data from all enabled platforms, writes full snapshot to `data/latest-raw.json` (overwritten each run)
   - Also appends a compact entry to `data/daily.json` (overwrites today's entry if it already exists)
2. Run `python3 scripts/generate_latest.py --raw data/latest-raw.json --prev data/latest.json --output data/latest.json --daily data/daily.json`
   - Compares current against previous `latest.json` for tracked skills and github repos
   - When `--daily` is provided, also computes yourSkills deltas against yesterday's entry in daily.json
3. Read `data/latest.json`
4. If it has `"changes"`, format them and send to Slack
5. If no changes, send minimal pulse or skip (agent's judgment)

**Pulse format (Slack):**
```
📡 Ecosystem Pulse — Apr 4, 2026
─────────────────────────────────

📊 CLAWHUB
  self-improving-agent    347k dl  ↑245  ⭐2,956
  ontology                150k dl  →

─────────────────────────────────

⭐ YOUR SKILLS
  gmail-checker    59 dl  ↑3
  github-tracker   51 dl  →

─────────────────────────────────

🏪 MARKETPLACES
  Agensi    80 skills
  Cursor    featured (free)

─────────────────────────────────

🐙 GITHUB
  openclaw 347k  |  claude-code 108k  |  codex 73k

─────────────────────────────────
```

No alerts.

Rules:
- One code block for the entire pulse. Use emoji section anchors + dividers.
- Only show skills that changed (↑/↓). Skip unchanged in the tracked list.
- Abbreviate large numbers (347,883 → 347k).
- Mark your skills with `*` so they stand out.
- If first run ever (no previous data): "Baseline set — first trend comparison tomorrow."
- If nothing changed at all: send a one-liner or skip entirely.

### `deep` — Full analysis (every 5 days)

Trend report with history analysis + news/sentiment scan + marketplace discovery. Run every 5 days via cron.

**Deduplication is critical.** Read `data/known-platforms.json`, `data/known-findings.json`, and `data/last-report.json` BEFORE searching or analyzing. Only report genuinely new information. Never repeat findings from previous reports.

**Steps:**
1. Run all `pulse` steps first
2. Run `python3 scripts/watch.py --output data/watch/TIMESTAMP.json`
3. **Load dedup state:** Read `data/known-platforms.json`, `data/known-findings.json`, and `data/last-report.json`
4. Run `python3 scripts/trends.py` to compute growth metrics from `data/daily.json` → writes `data/trends.json`
5. Read `data/trends.json` for pre-computed growth data (7d/30d/90d windows)
6. Read `references/analysis-guide.md` for interpretation framework
7. **News & sentiment scan:** Use `web_search` with ALL queries from `config.json > watch > searchQueries` and `newsQueries` (16 total — full coverage is important). Then:
   - Collect all article headlines and URLs from search results
   - **Deduplicate:** remove articles already in `data/last-report.json > articleHeadlines`
   - **Check known-findings:** skip facts already recorded in `data/known-findings.json`
   - Only report genuinely new articles and findings
   - Look for: platform updates, new marketplace launches, funding, adoption signals, Alpha→Beta transitions
8. **Marketplace discovery:** Compare search results against `data/known-platforms.json`.
   - If a platform name/URL appears in search results and is already in `known-platforms.json` → skip (not new)
   - If it's NOT in `known-platforms.json` → genuinely new, flag as 🆕 NEW and add to the file
   - Check for status changes: did any known platform go dormant? add payments? change version stage?
9. **Analyze trends across all data:**
   - Read `data/trends.json` for computed growth metrics instead of calculating manually
   - ClawHub: download growth rates for tracked skills (from trends.json)
   - Agensi: skill count trajectory + new skill slugs (from trends.json)
   - GitHub: star growth rates across platforms (from trends.json)
   - Payments: any changes since last deep report
   - Compare key numbers against `data/last-report.json > keyNumbers` — only report notable deltas
10. Write report to `data/reports/YYYY-MM-DD.md`
11. **Update dedup state:**
    - Update `data/known-platforms.json` with any new platforms or status changes
    - Update `data/known-findings.json` with new facts (version changes, payment changes, market shifts). Update existing findings if underlying data changed (e.g. Codex went from alpha to beta)
    - Overwrite `data/last-report.json` with compact summary of THIS report (article headlines, key numbers, new platforms found)
12. Send summary to Slack channel

**Deep report structure:**
```markdown
# 📡 Ecosystem Radar — Deep Report #N

**Date:** YYYY-MM-DD
**Period:** Last N days (X data points)

## Executive Summary
[2-3 sentences on overall direction. What changed THIS report vs last?]

## 🆕 New This Report
[ONLY genuinely new findings: new platforms, payment changes, version transitions,
 major news. If nothing new, say "No significant changes since last report."]

## ClawHub Trends
[Download trajectories for tracked skills — only if notable]

## Agensi Growth
[Skill count changes — only if notable]

## Platform Adoption (GitHub)
[Star/fork growth — only if notable (>5% change or new entrant)]

## Payment & Monetization Watch
[ONLY if payment status changed since last report]

## News & Sentiment
[Deduplicated. Only articles/findings not in previous reports]

## Marketplace Status
[Full table of ALL known platforms from known-platforms.json.
 Update status field if anything changed. This replaces the discovery section.]

## Summary
[One-paragraph read on: is the market growing? Are payments spreading? What's the overall direction?]
```

## Files

- `config.json` — Platform defs, tracked skills, search queries, Slack channel
- `scripts/collect.py` — Fetch from ClawHub + Agensi + GitHub → raw JSON. Also appends compact entry to `data/daily.json`.
- `scripts/watch.py` — Check payment features on known platforms
- `scripts/generate_latest.py` — Raw → compact summary + change detection. Supports `--daily` for yourSkills deltas.
- `scripts/trends.py` — Computes growth metrics (7d/30d/90d windows) from `data/daily.json`. Run before deep reports.
- `data/daily.json` — Append-only compact entries, one per day. Source of truth for all historical data and trend computation.
- `data/latest-raw.json` — Most recent full collection snapshot (overwritten each run). Used by generate_latest.py for pulse deltas.
- `data/trends.json` — Pre-computed growth metrics (7d/30d/90d windows). Updated by deep report via trends.py.
- `data/latest.json` — Compact summary (for pulse comparison)
- `data/watch/` — Timestamped watch results
- `data/reports/` — Deep analysis reports (markdown)
- `data/known-platforms.json` — Permanent record of ALL discovered platforms (never pruned)
- `data/known-findings.json` — Persistent fact store for key assertions (never pruned)
- `data/last-report.json` — Compact summary of most recent report (overwritten each deep run)
- `references/platform-notes.md` — Per-platform technical details
- `references/analysis-guide.md` — How to interpret trends

## Important Notes

- **Token efficiency:** Scripts do the heavy lifting. LLM reads compact `data/latest.json` for pulse, plus `data/trends.json` for deep reports.
- **Deduplication is critical:** Always read `known-platforms.json`, `known-findings.json`, and `last-report.json` before starting a deep report. Never repeat findings from ANY previous report — these files are your long-term memory.
- **First 2-3 pulses have no comparison data** — this is normal. Trends need 3+ data points.
- **Agensi slug diffing** — `daily.json` stores full slug lists per day. `trends.py` computes which slugs appeared in each window by comparing lists between entries.
- **GitHub API is unauthenticated** — 60 req/hour. We track 8 repos = 16 calls per run. More than enough.
- **News search is LLM-only** — happens during deep reports, not in scripts. Use `web_search` directly. Run ALL 16 queries for full coverage, then deduplicate results.
- **known-findings.json is long-term memory** — it persists across ALL reports. A finding recorded in report #1 won't repeat in report #5. Only update a finding when the underlying fact changes (e.g. Codex goes from alpha to beta).
- **known-platforms.json is permanent** — never prune entries, only add new ones or update status fields. A platform discovered in report #1 stays recorded forever.
- **last-report.json is short-term** — overwritten each deep report. Used for dedup of article headlines and key numbers between consecutive reports.
- **daily.json is the single source of truth** for historical data. `collect.py` appends to it after every run (overwrites today's entry if it already exists). Deep reports and `trends.py` read from it.

## Adding a New Platform

1. Add entry to `config.json > platforms` (start with `enabled: false`)
2. Add collector to `scripts/collect.py`
3. Update `scripts/generate_latest.py` to include in summaries
4. Update `references/platform-notes.md`
5. Test with `python3 scripts/collect.py --platform <name>`
6. Enable in config
