# Claude Code Review — Freelance Forge Architecture

**Purpose:** Get Claude Code's perspective on the Freelance Forge architecture before implementation begins. This is a review pass, not a build pass. We want fresh eyes on the design, not scope creep.

**How to use this:** Give Claude Code access to all files in `freelance-forge/` and ask it to review the architecture and answer the questions below. Its answers may surface issues we haven't considered or confirm that the design is solid.

---

## Files to Review

```
freelance-forge/
├── architecture.md              # Main architecture doc (start here)
├── session-context.md           # How we got here, conversational decisions
└── subskills/
    ├── pipeline-tracker.md      # Sub-skill deep dive
    └── lead-qualifier.md        # Sub-skill deep dive (more to come)
```

---

## Review Questions

### Architecture-Level

1. **Does the overall architecture hold together?** Are there any logical gaps, circular dependencies, or assumptions that break down under scrutiny?

2. **Is the data flow realistic?** All sub-skills communicate through a Notion database. Are there scenarios where this pattern causes problems (e.g., race conditions, data conflicts, missing data between stages)?

3. **Is the schema-adaptive approach feasible at the described level?** Mapping user fields by type + name heuristics, then augmenting missing columns — does this work reliably with real Notion databases, or are there edge cases we're missing?

4. **Are the env var defaults sensible?** `FREELANCE_FORGE_CONFIG_DIR` defaults to `~/.freelance-forge/`, `FREELANCE_FORGE_REPORTS_DIR` defaults to `./freelance-forge-reports/`. Are there cross-platform issues (Windows paths, sandboxed environments)?

### Sub-Skill Design

5. **Lead Qualifier — is the research process realistic?** Web scraping → search → social → tech stack, with graceful handling of JS-rendered sites. Are we underestimating the complexity of this? What are the likely failure modes?

6. **Pipeline Tracker — is the setup flow too complex?** The discover → map → augment → save flow involves multiple Notion API calls and user confirmations. Is there a simpler approach that achieves the same result?

7. **Are the two sub-skills well-scoped relative to each other?** Does the Lead Qualifier try to do too much or too little? Does the Pipeline Tracker have the right responsibilities, or should some of its functions live elsewhere?

### Implementation Concerns

8. **What's the hardest technical challenge in this bundle?** If you were building this, what would worry you the most?

9. **Are there any dependencies or prerequisites we haven't accounted for?** Python packages, system tools, API rate limits, auth complexity.

10. **What would you change about the architecture?** Not nitpicks — substantive changes that would make the product better, simpler, or more robust. Assume the core concept (four sub-skills, Notion as hub, freelancer-focused) is fixed. Focus on structure and implementation approach.

### Cross-Agent Compatibility

11. **How would you approach making this work across OpenClaw AND Claude Code?** The current plan is env vars + SKILL.md standard. Are there platform-specific gotchas that would break this for Claude Code users? What about Codex CLI or Gemini CLI?

12. **The bundle manifest format** — `openclaw.bundle.json` works for OpenClaw. Claude Code uses `.claude-plugin/plugin.json`. Can these coexist cleanly? Are there conflicts?

### Scope & Priorities

13. **If you had to cut one sub-skill to ship faster, which would you cut and why?**

14. **If you had to add one thing to make this significantly better, what would it be?**

15. **Is the "report as file, Notion as metadata" pattern the right call?** Or should everything live in Notion? Or everything as files?

---

## Ground Rules for the Review

- **This is a review, not a redesign.** Flag problems, suggest alternatives, but don't rewrite the architecture.
- **The target user is fixed:** freelance web designers using Notion. Don't suggest broadening the audience.
- **The four sub-skills are fixed.** Don't suggest adding or removing sub-skills (though question 13 asks which to cut if forced).
- **Budget is a concern.** The user is a student. Flag anything that would be expensive to run (API costs, heavy compute, paid dependencies).
- **Scope creep is the enemy.** If a suggestion makes the product 20% better but doubles the build time, say so. We want to know the trade-off.
