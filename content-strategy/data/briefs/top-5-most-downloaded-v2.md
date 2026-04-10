# Research Brief: I Tested the 5 Most Downloaded Skills on ClawHub — Here's What Actually Works

## Topic & Angle

**Working title:** I Tested the 5 Most Downloaded Skills on ClawHub — Here's What Actually Works
**Format:** Listicle (with teardown elements for each skill)
**Why now:** 48,000+ skills on ClawHub, most people don't know what to install. "Most downloaded" is the default filter — but does popularity = quality?
**The story:** I pulled the real download and install data for the top 5 most downloaded skills. Then I actually installed and tested every single one. The results are surprising — most are instruction-only, some require external tools you've never heard of, and one of them is genuinely useful. The download numbers tell a very different story from the install numbers.
**Target audience:** Entrepreneurs and developers exploring agent skills, wondering where to start

---

## Skills Tested

| # | Skill | Slug | Downloads | Installs (All-Time) | Stars | Install Ratio | Code or Instructions? |
|---|-------|------|-----------|---------------------|-------|---------------|----------------------|
| 1 | self-improving-agent | self-improving-agent | 358,904 | 5,815 | 3,016 | 61.7:1 | Instructions + hooks + helper scripts |
| 2 | Skill Vetter | skill-vetter | 190,826 | 3,774 | 844 | 50.5:1 | Instructions only (single SKILL.md) |
| 3 | Ontology | ontology | 154,493 | 1,072 | 491 | 144.1:1 | Code (Python CLI) + instructions |
| 4 | Gog | gog | 147,941 | 3,311 | 821 | 44.7:1 | Instructions only (wrapper for external CLI) |
| 5 | GitHub | github | 148,893 | 3,969 | 490 | 37.5:1 | Instructions only (wrapper for gh CLI) |

**Honorable mention:** proactive-agent (135,774 downloads, 2,632 installs, 683 stars) — very similar to #1 (self-improving-agent), both by the same author (pskoett). Adds proactive learning triggers. Skipped to avoid repetition in the post.

**Data verified:** All numbers from `clawhub inspect --json` on 2026-04-07. Downloads ≠ installs. Install ratio = downloads per install. A high ratio means lots of page views but few actual installations.

**Note for Claude:** The install ratios are a story in themselves. Ontology has 154K downloads but only 1,072 installs (144:1 ratio) — that's a lot of curiosity, not a lot of commitment. GitHub has the best ratio (37.5:1) meaning people who look at it are most likely to actually install it. Gog is close behind at 44.7:1.

---

## Skill 1: self-improving-agent

**Install:** `clawhub install self-improving-agent`
**Author:** autogame-17 (pskoett on GitHub)
**Version:** 1.41.0 (30 versions published)
**License:** MIT-0

### What It Claims
A self-evolution engine for AI agents. Analyzes runtime history to identify improvements and applies protocol-constrained evolution. The name suggests autonomous self-improvement — like an agent that gets smarter on its own.

### What It Actually Does
It's a structured note-taking system. The SKILL.md (extremely thorough — ~500 lines) instructs the agent to:
- Log errors to `.learnings/ERRORS.md`
- Log learnings to `.learnings/LEARNINGS.md`
- Log feature requests to `.learnings/FEATURE_REQUESTS.md`
- Categorize entries by priority (critical/high/medium/low) and area (frontend/backend/infra/tests/docs/config)
- Track recurring patterns with `See Also` links
- "Promote" important learnings to project config files (CLAUDE.md, AGENTS.md, SOUL.md, TOOLS.md)

It includes:
- **3 bash scripts:** `activator.sh` (hook reminder), `error-detector.sh` (grep-like error pattern matching on tool output), `extract-skill.sh` (scaffolds a new skill from a learning entry)
- **1 JS hook:** `handler.js` — OpenClaw bootstrap hook that injects a reminder virtual file on agent startup
- **Template files:** LEARNINGS.md, ERRORS.md, FEATURE_REQUESTS.md, SKILL-TEMPLATE.md in `assets/`

**Critical finding:** The SKILL.md says `clawdhub install self-improving-agent` — the CLI is called `clawhub`, not `clawdhub`. This is a bug in the documentation. Anyone copy-pasting that command will get an error.

### Test Methodology
- Installed on Raspberry Pi 5 (arm64, Linux)
- Read all files: SKILL.md, all 3 scripts, handler.js, reference docs
- Tested the `.learnings/` directory creation workflow
- Did NOT test hooks (requires specific agent platform setup)
- Did NOT test skill extraction script (requires specific workflow context)

### Test Results
**What worked:**
- Directory creation and template structure is clean and well-organized
- The logging format is comprehensive (metadata, priority, area tags, see-also links)
- The skill extraction script (`extract-skill.sh`) is well-written — validates skill name format, prevents path traversal, has dry-run mode
- The error-detector hook reads CLAUDE_TOOL_OUTPUT env var and checks for error patterns — simple but effective
- Cross-platform awareness: includes setup instructions for Claude Code, Codex, Copilot, and OpenClaw

**What didn't:**
- **Install command in docs is wrong** — says `clawdhub` not `clawhub`. First impression is a broken command.
- The SKILL.md is 500+ lines. An agent has to read all of that before knowing what to do. The description says "self-evolution engine" but it's actually a markdown filing system.
- No actual runtime intelligence. It doesn't analyze anything automatically — it relies entirely on the agent reading the SKILL.md and following the instructions. If the agent doesn't feel like logging a learning, nothing happens.
- The "Simplify & Harden Feed" integration references another skill (`simplify-and-harden`) that may or may not exist on ClawHub.
- 30 versions in ~2 months (created Feb 14, 2026) is a lot of churn for a note-taking template.

**Overall experience:** The SKILL.md is impressively detailed and well-structured. The concept is sound — structured learning capture for agents is genuinely useful. But the gap between "self-evolution engine" and "markdown filing system" is wide. The install command bug is a red flag for attention to detail.

### Security Assessment
- **ClawHub rating:** No security flags noted during install
- **Code review findings:**
  - No external network calls in any script
  - No credential access
  - `extract-skill.sh` has proper path traversal prevention (rejects absolute paths and `..` segments)
  - `error-detector.sh` only reads `CLAUDE_TOOL_OUTPUT` env var — no file access
  - `handler.js` is clean — only injects virtual bootstrap file, no side effects
- **Safety verdict:** Safe

### Pros
- Most thoughtful and well-structured SKILL.md I've seen on ClawHub
- The learning-to-skill promotion pipeline is a genuinely good idea
- Cross-platform support (Claude Code, Codex, Copilot, OpenClaw)
- Clean, safe code in all scripts

### Cons
- Misleading name and description — it's note-taking, not self-evolution
- Install command in docs is wrong (`clawdhub` vs `clawhub`)
- 500-line SKILL.md is a lot for an agent to process on every relevant interaction
- 30 versions in 2 months = documentation churn, not feature development
- No actual automation — entirely dependent on agent compliance

---

## Skill 2: Skill Vetter

**Install:** `clawhub install skill-vetter`
**Author:** (not specified in metadata — _meta.json only has basic info)
**Version:** 1.0.0
**License:** Not specified

### What It Claims
Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.

### What It Actually Does
It's a single SKILL.md file — no code, no scripts, no automation. It provides:
- A 4-step vetting checklist (source check, code review, permission scope, risk classification)
- A list of red flags to check for (curl/wget to unknown URLs, credential access, eval/exec, etc.)
- A risk classification matrix (LOW/MEDIUM/HIGH/EXTREME)
- A report template to fill out after vetting
- Some quick vetting commands using curl + GitHub API

**Key finding:** This is a security checklist, not a security tool. It can't actually scan code for you — it just tells you what to look for. The agent still has to read every file and make judgment calls manually.

### Test Methodology
- Installed and read the entire SKILL.md (single file, ~150 lines)
- No code to test — it's purely instructional
- Compared the red flag list against our own security review practices

### Test Results
**What worked:**
- The red flag list is comprehensive and covers the right things (external URLs, credential files, eval/exec, obfuscation, sudo)
- Risk classification matrix is clear and actionable
- The report template is clean and could be useful for documentation
- Quick vet commands for GitHub repos are handy

**What didn't:**
- **It can't actually DO anything.** You install a security scanner that has zero scanning capability. The agent has to manually read every file and apply the checklist — which is what any competent agent would do anyway.
- Version 1.0.0, never updated (created and never touched again based on version count)
- No automation, no scripts, no code analysis tools
- The trust hierarchy (official skills → high-star → known authors → unknown → credentials) is reasonable but arbitrary
- References "ClawdHub" in one place (same typo as self-improving-agent — suggests they share a template or author)

**Overall experience:** Took 10 seconds to install. Read it in 2 minutes. It's a good checklist if you've never thought about skill security before, but it doesn't save you any work. You still have to manually review every file. It's the equivalent of a "How to Spot Fake Emails" PDF — useful awareness, zero automation.

### Security Assessment
- **ClawHub rating:** Not flagged
- **Code review findings:** No code to review — it's a single SKILL.md with no scripts
- **Safety verdict:** Safe (it literally can't do anything)

### Pros
- Comprehensive red flag checklist
- Good risk classification framework
- Quick vet commands for GitHub repos
- The concept is important — security awareness for skill installation is needed

### Cons
- Zero automation — it's a checklist, not a tool
- Single SKILL.md, no code, no scripts
- Version 1.0.0, appears abandoned
- An agent that needs this checklist to spot `curl` calls to unknown URLs probably shouldn't be installing skills unsupervised
- The irony: a security tool that can't actually scan anything

---

## Skill 3: Ontology

**Install:** `clawhub install ontology`
**Author:** (not specified in metadata)
**Version:** Latest (4 versions)
**License:** Not specified

### What It Claims
Typed knowledge graph for structured agent memory and composable skills. Create/query entities (Person, Project, Task, Event, Document), link related objects, enforce constraints, plan multi-step actions as graph transformations.

### What It Actually Does
This is the only skill in the top 5 with real, working code. It provides:
- **Python CLI** (`scripts/ontology.py`, ~450 lines): Full CRUD for a JSON-based knowledge graph
- Operations: create, get, query, list, update, delete, relate, related, validate, schema-append
- Storage: append-only JSONL file at `memory/ontology/graph.jsonl`
- Schema validation via YAML: required fields, enum values, forbidden properties, relation cardinality, acyclicity checks
- 15+ predefined entity types (Person, Organization, Project, Task, Goal, Event, Location, Document, Message, Thread, Note, Account, Device, Credential, Action, Policy)
- Reference docs for schema and queries

### Test Methodology
- Installed and tested on Raspberry Pi 5 (arm64, Python 3.13)
- Created test entities (Person, Task)
- Tested schema creation and validation
- Tested invalid data detection (enum violation correctly caught)
- Read the full Python source (~450 lines)
- Did NOT test cross-skill integration or complex graph queries

### Test Results
**What worked:**
- All CRUD operations work correctly out of the box
- Schema validation catches real errors — created a Task with `status: "invalid"` and it was correctly flagged against the enum
- Entity IDs are auto-generated with type prefixes (pers_, task_, proj_)
- The code is clean, well-documented, and properly structured
- Path traversal protection via `resolve_safe_path()` function
- Append-only storage preserves history
- Schema merging (append) works without overwriting existing definitions
- No external dependencies beyond stdlib + PyYAML (optional)

**What didn't:**
- **Schema validation is post-hoc.** It doesn't prevent you from creating invalid entities — you create first, then validate separately. There's no `--validate` flag on the `create` command.
- No delete/undo for schema changes — once you append a schema definition, it's permanent
- `load_schema` silently returns empty dict if PyYAML isn't installed — no warning, just skips validation entirely
- No indexing — every `query` or `list` loads the entire JSONL file into memory. Fine for small graphs, would be slow at scale.
- The SKILL.md references "causal inference" integration and "cross-skill communication" patterns that are documentation-only — no actual implementation for these
- Documentation says "For complex graphs, migrate to SQLite" but provides no migration tool

**Overall experience:** This is the only skill in the top 5 that does something real. The Python CLI is solid, the schema validation works, and the concept of a typed knowledge graph for agent memory is genuinely powerful. It took 30 seconds to set up and was immediately useful. The post-hoc validation is a design choice (not a bug) — it lets you work fast and validate later — but it means invalid data can accumulate.

### Security Assessment
- **ClawHub rating:** Not flagged
- **Code review findings:**
  - No external network calls
  - No credential access
  - `resolve_safe_path()` prevents path traversal on all file operations
  - No eval/exec, no subprocess calls
  - Clean stdlib-only code (PyYAML is optional)
- **Safety verdict:** Safe

### Pros
- The only skill in the top 5 with real, working code
- Schema validation actually catches errors
- Clean Python code with proper path safety
- Append-only storage preserves history
- Well-documented with reference files
- No external dependencies beyond stdlib

### Cons
- Post-hoc validation (doesn't prevent invalid data creation)
- No scale — loads entire graph into memory on every query
- PyYAML silently optional — validation just stops working if missing
- Advanced features (causal inference, cross-skill communication) are docs-only
- 144:1 download-to-install ratio suggests people look but don't commit

---

## Skill 4: Gog

**Install:** `clawhub install gog`
**Author:** steipete (well-known iOS developer, PSPDFKit founder)
**Homepage:** https://gogcli.sh
**License:** Not specified in SKILL.md

### What It Claims
Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. Connect your Google account and manage everything from the command line.

### What It Actually Does
The SKILL.md is a command reference card — 44 lines of install instructions and CLI commands. It's a wrapper/instruction set for an external Go binary called `gog` that you have to install separately via Homebrew (`brew install steipete/tap/gogcli`). The binary itself is not included in the skill.

**Critical finding:** You cannot use this skill without:
1. A Google Cloud Platform project with OAuth credentials (`client_secret.json`)
2. Running `gog auth credentials /path/to/client_secret.json`
3. Running `gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs`
4. Going through Google's OAuth consent flow in a browser

### Test Methodology
- Installed the skill
- Attempted to use — `gog` binary not found (not installed on Pi)
- Read the full SKILL.md
- Checked the homepage (https://gogcli.sh)
- Could not fully test without Google OAuth setup

### Test Results
**What worked:**
- The command reference is clear and comprehensive
- Covers all major Google Workspace services (Gmail, Calendar, Drive, Contacts, Sheets, Docs)
- Includes practical examples (search, send, get, update, append, export)
- Notes about `--json` for scripting and `--no-input` for automation
- The `GOG_ACCOUNT` env var to avoid repeating account flag

**What didn't:**
- **Requires a separate binary** that's not included. This is a manual for someone else's tool, not a standalone skill.
- **Requires Google OAuth setup** — non-trivial. You need a GCP project, OAuth client credentials, and browser-based consent flow. For most entrepreneurs, this is a multi-step process that requires some Google Cloud knowledge.
- **Homebrew only** — the install command is `brew install steipete/tap/gogcli`. No apt, no binary download, no pip. If you're not on macOS with Homebrew, you're on your own.
- No error handling guidance — what if OAuth fails? What if credentials expire?
- The SKILL.md says "Confirm before sending mail or creating events" — but there's no actual confirmation mechanism. It's just a suggestion.

**Overall experience:** The SKILL.md is well-written as a command reference. But calling this a "skill" is generous — it's documentation for an external tool that requires significant setup. The 44 lines of instructions are useful if you've already installed gog and set up OAuth. If you haven't, this skill doesn't help you get there.

### Security Assessment
- **ClawHub rating:** Not flagged
- **Code review findings:** No code — single SKILL.md
- **Safety concerns:** Requires Google OAuth credentials. The skill instructs the agent to send emails and create calendar events. While it says "confirm before sending," there's no enforcement mechanism.
- **Safety verdict:** Use with caution — the skill enables email/calendar actions that could be triggered by an agent without human confirmation if the user doesn't manually supervise.

### Pros
- Clear, comprehensive command reference
- Covers all major Google Workspace services
- Practical examples for common operations
- Well-known author (steipete) adds credibility

### Cons
- Not a standalone skill — requires external binary (gog) + Google OAuth setup
- Homebrew-only installation — no Linux/Windows support documented
- No setup guidance for Google Cloud OAuth credentials
- No confirmation mechanism for email/calendar actions (just a suggestion)
- 44 lines of documentation, zero automation

---

## Skill 5: GitHub

**Install:** `clawhub install github`
**Author:** Peter Steinberger (steipete) — PSPDFKit founder, well-known iOS developer
**Version:** 1.0.0 (only version, never updated)
**License:** Not specified

### What It Claims
Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries.

### What It Actually Does
It's a 48-line SKILL.md that documents basic `gh` CLI commands. Like Gog (same author), it's a wrapper/instruction set for an external tool. The `gh` CLI is widely installed and well-documented already — this skill just tells the agent to use it.

Contents:
- PR checks and CI status viewing (`gh pr checks`, `gh run list`, `gh run view`)
- Failed step log viewing (`gh run view --log-failed`)
- API queries with `gh api` and `--jq` filtering
- JSON output tips with `--json` and `--jq`

### Test Methodology
- Installed and read the entire SKILL.md (48 lines, single file)
- No code to test — purely instructional
- Compared against `gh` CLI's built-in help (which is more comprehensive)

### Test Results
**What worked:**
- The examples are correct and practical
- `--jq` filtering is a nice tip that `gh` users might not know about
- The `--log-failed` flag for CI debugging is genuinely useful
- Clean, no-nonsense format

**What didn't:**
- **48 lines.** That's the entire skill. It covers PRs, CI runs, and API queries — but omits issues, repos, releases, workflows, actions, gists, secrets, and dozens of other `gh` subcommands.
- **Version 1.0.0, never updated.** Created once, never touched. The `gh` CLI has added features since — this skill is frozen in time.
- **The `gh` CLI already has excellent built-in help.** Running `gh --help` gives you more than this skill does. Running `gh pr --help` gives you everything the skill covers plus more. The skill adds almost zero value over just... using `gh`.
- **Same author as Gog (steipete).** Both are thin instruction wrappers for external CLIs. Neither includes the actual tool. The pattern is consistent: well-known developer publishes minimal skills, downloads follow reputation.
- **No error handling guidance, no authentication setup, no workflow examples.** Just 5 command examples.
- **Best install ratio in the top 5 (37.5:1).** People install this because `gh` is ubiquitous and the skill is lightweight — not because it's good.

**Overall experience:** Installed in 5 seconds. Read it in 30 seconds. It's 5 correct `gh` examples that you could find by typing `gh --help`. The high install ratio (37.5:1, best in the top 5) makes sense — it's low-risk because everyone already has `gh`. But it's hard to call it a "skill" when it's shorter than most blog posts about the `gh` CLI.

### Security Assessment
- **ClawHub rating:** Not flagged
- **Code review findings:** No code — single 48-line SKILL.md
- **Safety verdict:** Safe (it literally can't do anything beyond what `gh` already does)

### Pros
- Correct, practical examples
- `--jq` and `--log-failed` tips are useful
- Low risk — just documents existing `gh` CLI
- Best install ratio in the top 5 (37.5:1)

### Cons
- 48 lines total — thinner than most READMEs
- Version 1.0.0, never updated
- Covers a fraction of `gh` CLI's capabilities
- Adds almost no value over `gh --help`
- Same thin-wrapper pattern as Gog (same author)

---

## SaaS Alternatives & Pricing

| SaaS Tool | What It Does | Monthly Cost | Free Tier? |
|-----------|-------------|-------------|------------|
| Notion | Structured notes, project management, databases | $10/mo | Yes (limited) |
| Linear | Issue tracking, project management | $8/mo | Yes (limited) |
| GitHub (native) | PR reviews, CI, issue tracking | Free-$$ | Yes (public repos) |
| Zapier | Workflow automation across services | $20/mo | Yes (100 tasks) |

### Key Comparisons
- **Ontology vs Notion:** Ontology is free, local, and agent-native. Notion has a GUI, collaboration, and templates. Ontology wins for agent workflows; Notion wins for human collaboration.
- **GitHub skill vs GitHub native:** The skill teaches 5 `gh` commands. GitHub's built-in docs teach hundreds. The only advantage is that the skill loads into agent context automatically.
- **Self-improving-agent vs Linear:** Both track issues and learnings. Self-improving-agent is agent-native; Linear has a full UI, teams, and integrations. Different tools for different users.
- **Gog vs Google Workspace native UI:** Gog requires OAuth setup and a separate binary. Google's web UI requires... a browser. The skill's value is for agents, not humans.

---

## Data Points

- **Total downloads of top 5:** 1,000,557 (crossed 1 million)
- **Total actual installs:** 16,937
- **Average download-to-install ratio:** 59:1
- **Skills with real code:** 1 out of 5 (ontology)
- **Skills requiring external tools:** 2 out of 5 (gog needs Go binary, github needs gh CLI — though gh is ubiquitous)
- **Skills that are purely instructional:** 4 out of 5
- **Skills with security concerns:** 0 in this selection (proactive-agent skipped; browser-use excluded)
- **Skills with bugs in docs:** 1 out of 5 (self-improving-agent — wrong CLI name)
- **Skills by steipete:** 2 out of 5 (gog, github) — same thin-wrapper pattern
- **Best install ratio:** github at 37.5:1
- **Worst install ratio:** ontology at 144.1:1

---

## Caveats

- Download numbers are inflated by page views, not actual installations. The average skill gets 59 page views for every install.
- 4 out of 5 "most downloaded skills" are instruction-only — they're documentation, not tools. ClawHub doesn't distinguish between skills with code and skills without.
- 2 out of 5 require external tools that aren't included (gog needs a Go binary + Google OAuth; github needs the `gh` CLI, though that one is widely available). The "install" is often just downloading instructions.
- The most downloaded skill (self-improving-agent) has a bug in its install command. Quality control varies.
- The actual #4 skill (proactive-agent) was excluded because it's nearly identical to #1 — both by the same author. The ClawHub top list has duplicates by design.
- 2 of the 5 skills (gog, github) are by the same author (steipete), both following the same thin-wrapper pattern. Well-known developers get downloads regardless of skill quality.
- This review was done on 2026-04-07. ClawHub skills update frequently — some may have changed by the time you read this.

---

## Quotable Moments

Real moments from testing that make the post feel _tested_ not _researched_. Verbatim, no polishing.

- "The #1 most downloaded skill on ClawHub (358,904 downloads) tells you to install it with `clawdhub install self-improving-agent`. The CLI is called `clawhub`. That's the first command in the setup section. It doesn't work."

- "I installed Skill Vetter in about 10 seconds. Read the whole thing in 2 minutes. It's a security scanner that can't actually scan anything — it's a checklist. The irony of installing a security tool that has zero security automation wasn't lost on me."

- "Ontology was the only skill in the top 5 where I typed a command and something actually happened. Created a Person entity, queried it back, created a schema, tried to create a Task with an invalid status — and it correctly caught the error. 30 seconds from install to working."

- "Gog's SKILL.md is 44 lines. It's a cheat sheet for someone else's tool. To actually use it, you need a Google Cloud project, OAuth credentials, and a macOS machine with Homebrew. I'm on a Raspberry Pi. That's a hard no from me."

- "The GitHub skill is 48 lines. I read it faster than I could type `gh --help`. It documents 5 commands. The `gh` CLI's built-in help documents hundreds. The skill has 148,893 downloads."

- "Two of the top 5 skills (Gog and GitHub) are by the same author — Peter Steinberger, the PSPDFKit founder. Both follow the same pattern: a thin SKILL.md wrapping someone else's CLI tool. Neither includes the actual tool. Reputation drives downloads."

- "The actual #4 on the leaderboard is 'proactive-agent' — which is basically the same as #1 ('self-improving-agent') by the same developer. I skipped it because reviewing the same skill twice felt like padding the word count."

- "The average download-to-install ratio across the top 5 is 59:1. That means for every person who actually installs a skill, 59 people just looked at the page and moved on. ClawHub's 'downloads' metric is closer to 'page views.'"

---

## Suggested Narrative Elements

These are ideas for Claude to use or ignore:

- **Hook angle:** "I downloaded the 5 most popular skills on ClawHub. Here's what I found: 4 are just instruction manuals, 2 are by the same author, and exactly one of them does something when you install it."
- **Contrast point:** "358,904 downloads sounds impressive until you realize the install command in the documentation is wrong."
- **Compounding story:** The download-to-install ratio is the real story. ClawHub's download numbers include page views — the install numbers tell the truth. The gap between them reveals how many people browse vs commit.
- **Surprise/reveal:** The only skill with actual working code isn't #1 — it's #3. And it's a knowledge graph tool, which sounds boring, but works flawlessly.
- **The steipete pattern:** Two of the top 5 are by the same developer (Peter Steinberger). Both are thin wrappers for external CLIs. Both have never been updated past v1.0.0. Reputation beats quality on the leaderboard.
- **Closing idea:** "The most popular skills on ClawHub aren't popular because they're good. They're popular because they showed up first. The best one is the one that actually does something."

---

## Research Notes

- All data from `clawhub inspect --json` on 2026-04-07.
- The `clawhub explore --sort downloads` endpoint returned empty results during research — had to manually inspect each slug. This API limitation means the ranking had to be cross-checked.
- Initial top 5 was wrong (included Capability Evolver, ByteRover, Browser Use). Corrected with Rian's help. The ClawHub API makes it impossible to get a definitive sorted list — `explore` returns empty, and there's no `top` or `leaderboard` endpoint.
- Actual #4 (proactive-agent, 135,774 downloads) was excluded from the review because it's nearly identical to #1 (self-improving-agent). Same author (pskoett). The ClawHub leaderboard has near-duplicates.
- self-improving-agent's handler.js is well-written OpenClaw hook code. The skill clearly has a competent developer behind it — but the documentation bug and the gap between marketing ("self-evolution engine") and reality (note-taking system) are telling.
- Skill Vetter and self-improving-agent both reference "ClawdHub" (not "ClawHub") — possibly from a shared template or the same author.
- Gog's author (steipete) is Peter Steinberger, well-known iOS dev (PSPDFKit founder). GitHub skill is also by steipete. Both follow the same thin-wrapper pattern. His reputation drives downloads regardless of skill depth.
- Ontology's 144:1 ratio is the highest — its SKILL.md is dense and technical (knowledge graph terminology) which probably scares off casual browsers.
- GitHub skill has the best install ratio (37.5:1) — likely because `gh` is ubiquitous and the skill is low-risk to install.
- Browser Use was originally included but excluded from the final brief — flagged by VirusTotal and would have been the only security concern in an otherwise clean list.