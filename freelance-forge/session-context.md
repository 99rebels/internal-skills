# Freelance Forge — Session Context Notes

**For:** Next Cambrian session picking up this project
**Date:** 2026-04-25

## Read These First
1. `projects/freelance-forge/architecture.md` — the full design doc
2. `memory/2026-04-25.md` — today's memory log
3. `skills/idea-generator/ideas/raw/2026-04-25-freelance-forge.md` — scope decisions

## How We Got Here (the evolution, not just the destination)

This started as two separate ideas (API Forge + Schema Mapper) and evolved through three pivots:

**Pivot 1:** Rian said "I want something truly impressive, these are still pretty small skills." That pushed us from infrastructure tools to workflow automation.

**Pivot 2:** Discovered ClawHub supports `bundle-plugin` format (multi-skill packages). Examined NPD Validator (8-subagent pipeline) as proof of concept. Realised bundles enable multi-agent workflow orchestration — first real "applications" in the skill ecosystem.

**Pivot 3:** Explored "Agency in a Box" concept. Sub-niched to freelance web designers. Rian got the "holy shit" moment here.

## Key Conversational Nuances Not Fully in the Architecture Doc

### On Pipeline Tracker (the most important addition)
This was Rian's idea pattern, not mine. He asked "is that a CRM or does Notion do that?" — which led to realising the Pipeline Tracker is the glue that makes this feel like ONE product, not four separate skills. It's the "command center." The demo moment is "show me my pipeline" — one command, your entire freelance business at a glance.

### On Schema-Adaptive Notion
This ties back to the original Schema Mapper idea. Rian asked "would we be getting the user's current schema of their pipeline page?" — yes. The Pipeline Tracker reads the user's existing Notion database, maps our concepts (status, score, dates) to their field names, and adapts. If they call their stages "Hot/Warm/Cold" instead of "Lead/Qualified/Active" — the agent works with that. This is Schema Mapper as a *feature*, not a product. Rian liked this connection.

### On the Follow-Up Workflow
Rian proposed this specifically: "say we send a proposal and they don't get back within 5 days, the pipeline tracker flags it and offers to draft a follow-up." The key is: NO auto-send. Agent flags, agent drafts. Human reviews and sends. The pipeline database stores Proposal Date and Last Follow-Up, so the agent always has the context to write a good follow-up without the user re-explaining.

### On Emails
Rian was clear: don't send automatically. But DO draft on the user's request. The agent has all the company info (from Lead Qualifier) and proposal context (from Proposal Builder) stored in the Notion row. So when asked "draft a follow-up for Acme," it reads the row and has everything it needs.

### On What We Cut and Why
- **Invoice generation:** Rian said "not convinced on the invoice, the tracker part is pretty cool though." We kept the tracker, cut the invoices. Risk of getting money stuff wrong. Wrong focus for v1.
- **Email sending:** Rian explicitly said "not doing it automatically, it would be done on the user's request."
- **Asset generation:** Rian said "we have to be careful about what we take on here." We kept only lightweight text-based assets (project brief, checklist, sitemap). NOT logos, designs, or brand guidelines.
- **Project Onboarder email:** Rian was unsure about sending a welcome email. We kept it as a draft only.
- **Endpoint registry (API Forge):** The LLM already knows most APIs well enough. Schema mapping is where the real value is. Cut for v1.

### On Bundles on Agensi
Agensi supports plugin bundles natively ("a plugin is a package that bundles one or more skills"). This is how we'll sell it paid. ClawHub gets the free listing, Agensi gets the paid listing. Both support the format.

### On the Install Script Architecture
The install script places each sub-skill as a standalone SKILL.md in the user's skills directory. This is critical because the skill matcher can only discover skills in the standard location. If sub-skills are buried in nested folders, they won't be triggered when the user says "qualify this lead" weeks later.

### On the Model Situation
- GLM-5.1 has been added to openclaw.json and set as the GLM alias
- Anthropic (Sonnet) was removed from agent defaults to prevent accidental switching
- The architecture doc was written on Sonnet but the content is fine — it's structural, not creative
- Gateway needs a restart to pick up the GLM-5.1 config change

## What Rian Wants Next
1. Review the architecture doc (already pushed to GitHub)
2. Sub-skill deep dives — each one as a detailed brief
3. Handoff to Claude Code for implementation
4. Rian specifically said: "don't give Claude Code too many 'do this' instructions — it should use the design docs as its source of truth. Add broad guardrails but let Claude Code do its thing."
5. SEO Agency bundle logged for future exploration (separate project, not Freelance Forge)

## Competition Context
- Regression Guard was submitted to Agensi competition
- Freelance Forge is the next competition entry — much more ambitious
- Rian wants to charge for this on Agensi
