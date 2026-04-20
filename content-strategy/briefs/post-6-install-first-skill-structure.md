# Post 6: How to Install Your First Agent Skill (Start to Finish)

**Format:** Explainer (practical, step-by-step)
**Working title:** How to Install Your First Agent Skill (Start to Finish)
**Target length:** 1,200-1,500 words
**Publish date:** Tuesday 21 April 2026
**Post 5 (what skills are / why they matter) publishes next week — retro-link later

---

## 1. Opening (~150-200 words)

- AI agents can learn new tricks through small installable packages called "skills." Think of them as apps for your AI — install a weather skill and your agent knows how to check forecasts; install an invoice skill and it can parse your receipts.
- A full explainer on *what* skills are and why the market is forming is coming next week. This post is about getting one running now.
- Promise: by the end, you'll have installed a working skill and used it on a real task. Takes about 20 minutes.

## 2. Before You Start (~150-200 words)

- **What you need:**
  - Node.js installed (most developers already have this — check with `node --version`)
  - An AI agent platform that supports skills. The main ones: **OpenClaw**, **Claude Code**, **Microsoft Copilot** (VS Code, Cloud Agent, or CLI), **Cursor**, **Codex CLI**, **ChatGPT agent mode**, **Claude agent mode** (web).
  - ~20 minutes and a real task you'd like to speed up.
- **What "skill-capable" means:** not every AI tool supports skills. The ones listed above do. If you're using ChatGPT or Claude's web interface, check whether you have access to their agent mode — that's where skills are supported.
- **One tool does all the installing.** Regardless of which platform you're running, the install mechanism is the same: a single CLI tool called `clawhub` handles downloading skills and placing them in the right directory for your platform.

## 3. Step 1: Install the ClawHub CLI (~100-150 words)

- One-time setup. Open your terminal and run:
  ```
  npm install -g clawhub
  ```
- If you don't have Node.js, install it from [nodejs.org](https://nodejs.org) first. (Most developers already do.)
- Verify it worked: `clawhub --cli-version` — should print a version number (currently 0.9.0).
- That's it. This CLI is how you search for, install, update, and manage skills on any platform. It's the same tool whether you're on OpenClaw, Claude Code, or Copilot.

## 4. Step 2: Pick a Skill (~150-200 words)

- Browse skills at [clawhub.ai](https://clawhub.ai) or search from the terminal: `clawhub search <keyword>`.
- **What to look for:**
  - **Download count** — higher means more people have tried it
  - **Reviews** — read them if available
  - **Last update** — recently updated skills are more likely to work with current platforms
  - **Security rating** — ClawHub reviews skills for safety; look for the security badge
- **Start simple.** Pick something lightweight with an obvious, visible result so you can immediately tell whether it's working. A weather skill, a summariser, or a simple utility. Avoid complex multi-step skills for your first install — you want to confirm the process works before adding complexity.
- **Security note:** if a skill has no reviews, no recent updates, and no security rating, skip it for your first install. There are over 50,000 skills on ClawHub and most are fine, but the registry is open — pick a well-reviewed one while you're getting the hang of things.

## 5. Step 3: Install the Skill (~250-350 words)

- This is where the magic happens. One command, different target directory depending on your platform.

**OpenClaw:**
```
clawhub install <skill-name>
```
Installs to `~/.openclaw/workspace/skills/<skill-name>/`. No flags needed — this is the default. Skills are picked up automatically by the agent.

**Claude Code:**
```
clawhub --workdir ~/.claude --dir skills install <skill-name>
```
Installs to `~/.claude/skills/<skill-name>/`. Claude Code auto-detects skills in this directory. **One gotcha:** if the `~/.claude/skills/` directory didn't exist before, you'll need to restart Claude Code so it starts watching it. After the first time, future installs are picked up immediately without restarting.

**Microsoft Copilot:**
```
clawhub --workdir ~/.copilot --dir skills install <skill-name>
```
Installs to `~/.copilot/skills/<skill-name>/`. Copilot also accepts `~/.claude/skills/` and `~/.agents/skills/` as valid personal skill directories — all three work. In VS Code, no restart needed. In Copilot CLI, run `/skills reload` if you're in an active session.

**What "success" looks like.** After running the command, you should see:
```
✔ OK. Installed <skill-name> -> <path>/<skill-name>
```
If you see that confirmation line, the skill is installed. The directory will contain at minimum a `SKILL.md` file — that's the instruction file the agent reads.

## 6. Step 4: Use It on Real Work (~150-200 words)

- Don't test with a toy prompt. The whole point is to feel the difference between an agent without the skill and an agent with it.
- **Example with a weather skill:** ask your agent "What's the weather in Dublin this weekend?" Before the skill, it would give you a generic answer or say it can't check live data. With the skill installed, it should use the skill's instructions to fetch and report real weather data.
- **How to tell it worked:** the agent references the skill by name or follows the skill's instructions without you having to spell out what to do. If you find yourself explaining *how* to do the task, the skill probably isn't loaded.
- **If it didn't work:** see the pitfalls section below.

## 7. Common Pitfalls (~200-250 words)

- **"I ran the install command and nothing happened"** — you may be in the wrong directory, or the `--workdir`/`--dir` flags might be pointing somewhere unexpected. Check the output path in the confirmation line. Also make sure you have Node.js installed (`node --version`).
- **"My agent doesn't see the skill"** — this is the most common issue and the fix depends on your platform:
  - **Claude Code:** if `~/.claude/skills/` didn't exist before this install, restart Claude Code. After the first restart, future installs are live-reloaded.
  - **Copilot CLI:** run `/skills reload` in your active session.
  - **Copilot in VS Code:** skills should be picked up automatically. If not, reload the VS Code window (Cmd+Shift+P → "Reload Window").
  - **OpenClaw:** should work immediately. If not, check the agent is running and the skill directory is correct.
- **"The skill installed but doesn't do what I expected"** — skill listing pages can be optimistic. Open the `SKILL.md` file in the installed directory and read what it actually covers versus what the ClawHub page claims. The SKILL.md is the source of truth.
- **"I got a permissions error"** — some skills need access to specific tools (like shell commands). Check the SKILL.md for prerequisites. If the skill's frontmatter includes `allowed-tools: shell`, review the skill's scripts before approving.
- **Security gut check** — if a skill asks for credentials, writes files outside its own directory, or makes network calls to unknown domains, pause and review the SKILL.md carefully before continuing.

## 8. What's Next (~100-150 words)

- You've installed one skill. Try a second from a different category — see how they compose together.
- Browse ClawHub for skills that match your actual work. The search function (`clawhub search <keyword>`) is your friend.
- **Copilot users note:** Copilot CLI also supports *plugins* — installable bundles that package skills, agents, hooks, and MCP configs together. Browse plugins with `copilot plugin marketplace browse`. Plugins are a more heavyweight option; individual skills are the simpler starting point.
- Subscribe CTA.
- **Next week:** a full explainer on what agent skills are, why the market is forming at this pace, and where it's heading.

---

## Notes for Claude

- **All install commands and paths verified** by Cambrian on 2026-04-20. Tested `clawhub install` to all three target directories (OpenClaw, Claude Code, Copilot) on Raspberry Pi 5, arm64, Linux 6.12. Confirmed SKILL.md lands correctly in each location.
- **clawhub CLI version at time of testing:** 0.9.0 (installed via `npm install -g clawhub`).
- **Claude Code live reload detail** confirmed from official docs at <https://code.claude.com/docs/en/skills>: "Creating a top-level skills directory that did not exist when the session started requires restarting Claude Code."
- **Copilot CLI `/skills reload`** confirmed from official docs at <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills>.
- **Copilot accepts three personal skill directory paths:** `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` — confirmed from <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>.
- **Copilot plugins** are a separate mechanism from individual skill installs. Plugin install via `copilot plugin install PLUGIN-NAME@MARKETPLACE-NAME`. Default marketplaces: `copilot-plugins` and `awesome-copilot`. Source: <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing>. Brief mention only in "What's Next" — don't let it bloat the post.
- **No Post 5 link.** Post stands alone. One-paragraph explanation of skills at the top. Next week's explainer can be retro-linked once published.
- **Tone:** practical, direct, assume zero prior knowledge of skills. Reader wants to follow along and get a result. No hustle framing.
- **Word target:** 1,200-1,500. This is a short practical post.
- **Running example:** suggest a weather skill as the through-line example — lightweight, obvious visible result, easy to verify it's working. Claude can pick a specific one at drafting time or we can specify one.
- **Post 5 should be edited after publishing** to add the `{{INSTALL_POST_URL}}` link in the "How to Install" section, pointing to this post.
