# Teardown Brief Guide

Everything you need to research, structure, and deliver a Teardown brief. For universal rules that apply to all formats, see `brief-universal.md`.

---

## What a Teardown Is

A critical review of an individual skill or a small group of related skills. The reader should finish knowing whether the skill is safe, whether it actually does what it claims, and whether it's worth their time. Teardowns are one of four formats in the rotation — they're the credibility receipt that proves we actually test things.

**What a Teardown is not.** It's not a product review. It's not a tutorial. It's not a vendor puff piece. It's an honest assessment with a clear verdict. If a skill is bad, say so. If it's good but limited, say that. If it's dangerous, say that loudly. The credibility of the publication rests on Teardowns being trustworthy.

**The three-layer mix for Teardowns.** Teardowns lean heaviest on the analysis layer (interpreting what the test revealed, understanding what the finding means) with a strong action layer (install this, don't install that). Information plays a supporting role, usually in the form of download counts, install counts, code quality assessment, and security findings. The reader should finish a Teardown knowing whether the skill is safe, whether it does what it claims, whether it's worth their time, and what they should do about it.

**Single vs multi-skill teardowns.** Pick single-skill when the skill is significant enough on its own (by downloads, notoriety, security concern, or genuine utility) to carry the whole post. Pick multi-skill when the frame only emerges through comparison. The canonical example is Post 1 (the top-5 teardown), where the download-to-install ratio only became an insight because it was computed across a set. If you're unsure, default to single-skill: it's tighter, faster to research well, and avoids the risk of a multi-skill post that reads as five reviews strung together instead of one argument with five data points.

---

## Research Steps

**Before anything else: does this teardown have stakes?** A teardown without stakes is a review, and the publication doesn't publish reviews. Stakes come from one of the following: a surprising finding (good or bad), a security concern, a contradiction between the skill's claims and its reality, a pattern visible only across a set of skills, or a real warning readers need to hear. A skill that is fine, safe, and does roughly what it says on the tin probably doesn't need a teardown. Pick a different skill, or combine it with others into a multi-skill post that has a frame. If you can't finish the sentence "this teardown matters because..." in one line, the teardown isn't ready to research.

1. **Select the skill.** ClawHub search, category browsing, or Rian's suggestion. Prefer skills with meaningful downloads (not 5-download curios) unless there's a specific reason to review a niche skill — e.g., it's the only option in a category, it's trending, or there's a safety concern.

2. **Inspect before install.** Run `clawhub inspect <slug> --json`. Record the security rating, download count, install count, download-to-install ratio, author, and published date. These numbers go in the brief with timestamps. Claude cannot access the ClawHub CLI and will be relying on these numbers as provided.

3. **Read every file.** Install (or read via API) and go through every file in the skill. SKILL.md, any scripts, config files, references, companion files. No skimming. If the skill has 12 files, read all 12. The brief should reflect full reading, not skimming, and the close-reading findings are one of the most valuable things Cambrian provides because nobody else in the pipeline sees the source.

4. **Code review.** For code-based skills specifically:
   - **External network calls** — does it reach out to any URLs? Which ones? Why?
   - **Credential access** — does it read or write to credential files, `.env`, tokens, API keys?
   - **File system scope** — does it stay within expected paths or access things outside its scope?
   - **Obfuscation** — any base64 encoding, eval(), minified code, or techniques that hide what the code does?
   - **Companion skill installation** — does it try to install other skills as dependencies? Which ones?
   
   This is non-negotiable. Even if the ClawHub security rating says "safe," do your own review. Ratings can lag behind new versions.

5. **Assess code quality.** For code-based skills: lines of code, language, dependencies, organization, error handling, documentation quality, tests included. For instruction-only skills: instruction clarity, file count, word count, practical vs theoretical. This is close-reading analytical work that Cambrian is best positioned to do because the code is in front of you at this stage.

6. **Install and run the skill.** Follow the installation steps exactly as documented. Note every deviation from what the SKILL.md claims. If the docs say "just run clawhub install and you're good" and it takes 3 config files and a Python venv, document that gap — it's quotable.

7. **Test declared functionality.** If the skill claims to do X, verify X works. Test the core workflow end-to-end. If the skill claims multiple features, test each one. If something couldn't be tested (no credentials, no browser, requires specific hardware), document exactly why.

8. **Test edge cases.** What happens with:
   - Malformed or unusual inputs
   - Missing data or empty files
   - Larger-than-expected inputs
   - Inputs the skill wasn't designed for
   
   Edge cases are where you find the real quality of a skill. A skill that handles the happy path but breaks on weird inputs is a different product than one that degrades gracefully.

9. **Compare to alternatives.** What SaaS tool or other skill does the same thing? Build a comparison table. Note where the skill wins and where the alternative still wins. Include pricing with source URLs and timestamps. Claude will re-verify SaaS pricing at final draft time — pricing is shared responsibility.

10. **Identify a candidate central frame.** What's the single insight or pattern that could make this teardown worth reading? Good frames are data points, contradictions, or surprises. "This skill has 50k downloads but it's just a text file" is a frame. "We reviewed a skill" is not. Surface this as a candidate for Claude to consider, not as a prescribed spine — Claude will decide the final frame at drafting time.

11. **Identify a candidate hook moment.** One specific, surprising thing from testing that could open the post. It should be concrete and verifiable. This is separate from the candidate central frame — the central frame is what the post argues, the hook moment is how the post opens, and sometimes they're the same thing and sometimes they're not. A post with a hook but no frame is a curiosity. A post with a frame but no hook is an essay nobody reads past the first paragraph. Both need to be present, even if they overlap.

12. **Collect quotable moments.** Real, verbatim moments from testing — exact terminal output, surprising results, weird setup steps, things that made you go "huh" or "nice." Write them unpolished. Claude decides what to use at drafting time. Quotable moments from testing are one of the most valuable things Cambrian provides because nobody else in the pipeline has hands on the skills at the moment something notable happens.

    **For Teardowns specifically, favour moments a general reader can react to emotionally over moments only a developer cares about.** A reader can picture "the install command for the most-downloaded skill on the registry is misspelled on line one" or "the top result in the productivity category turns out to be a single text file with forty words in it." A reader cannot picture "the Python import block uses a relative path instead of a namespace import." When in doubt, ask whether a non-technical reader would laugh, wince, or recognise the moment. If they wouldn't, the moment is probably only quotable inside the code review, not inside the post.

---

### Protocol: When a Skill Fails Security Review

An unsafe skill is not a reason to abandon a teardown. Unsafe skills with real download numbers are among the highest public-interest posts the publication can produce, and the agent skills ecosystem has no other trusted source for this kind of warning (see: ClawHavoc, early 2026, 1,400+ malicious skills removed). If security assessment reveals a skill is unsafe:

1. **Note the finding and continue the research.** Don't interrupt the research loop to flag. Rian would rather see the full characterisation of the issue in one go than a vague mid-stream alert.
2. **Complete the rest of the research as normal.** Install in an isolated environment if necessary, read every file, test what can be tested safely, document the security issues in forensic detail.
3. **Flag to Rian at the end, as part of the brief handoff.** Mark the brief clearly at the top so the security finding is the first thing Rian sees. The editorial decision on timing, disclosure, and framing belongs to Rian and he'll make it from the finished research, not a partial view.
4. **The verdict in the final brief is ❌ Skip**, and the writer guidance should treat the post as a public-safety warning, not a routine pass. Flag this explicitly in the writer guidance box.
5. **Do not install the skill on production systems, and do not run untrusted code without isolation.** Stating the obvious, but worth having in writing.

The actively-dangerous exception (where continuing the research is itself a risk) is covered in `brief-universal.md` section 5.

---

## Brief Structure

Use this structure when writing the brief. Adapt headings if the specific post calls for it, but the content below should all be present.

```markdown
# Research Brief: [Skill Name] — [Candidate Hook Title]

## Topic & Angle

**Working title:** [suggested title — Claude may adjust]
**Format:** Teardown
**Why now:** [timeliness — why review this skill this week?]
**Stakes:** [one sentence — why does this teardown matter?]
**Target audience:** [who is this for?]

---

> **Single vs multi-skill teardowns.** For a single-skill teardown, fill in the Skill Under Review block once. For a multi-skill teardown (2-5 skills), start with the Skills Under Review summary table below, then repeat the detailed per-skill sections (What It Claims, What It Actually Does, Installation & Setup, Test Results, Code Quality, Security, Comparison, Verdict) once for each skill. The synthesis sections (What This Tells You, What Should You Actually Do, Caveats) appear once at the end.

## Skills Under Review (multi-skill only)

| # | Skill | Slug | Install | Downloads | Installs | Ratio | Security | One-line verdict |
|---|-------|------|---------|-----------|----------|-------|----------|------------------|
| 1 | [Name] | [slug] | `clawhub install [slug]` | [N] | [N] | [X:1] | [rating] | [verdict] |
| 2 | ... | | | | | | | |

---

## Skill Under Review

**Name:** [display name]
**Slug:** [slug]
**Install:** `clawhub install [slug]`
**Author:** [owner]
**Downloads:** [number] (as of [date])
**Installs:** [number] (as of [date])
**Download-to-install ratio:** [X:1]
**Code or instructions:** [code-based / instruction-only / hybrid]
**Published:** [date]
**Version tested:** [version]

---

## What It Claims

[Paraphrase the summary/description. What does the skill say it does?]

---

## What It Actually Does

[After reading ALL files. Detailed description. If code-based, describe the architecture and what the code actually does. If instruction-only, describe the scope and quality of the instructions. This section is Cambrian's close-reading analysis and it should reflect what only Cambrian can see, because Claude cannot install or run the skill.]

---

## Installation & Setup

**Steps taken:**
1. [step]
2. [step]

**Issues encountered:** [any problems, missing deps, confusing setup, deviations from what the docs claim]

**Time to set up:** [rough estimate]

---

## Test Methodology

**What we tested:**
- [Specific test 1]
- [Specific test 2]
- [Specific test 3]

**Environment:** [OS, agent runtime, Python version — currently: Raspberry Pi 5, arm64, Linux 6.12, OpenClaw]

**What we couldn't test:** [and why — e.g., no credentials, no browser, requires specific hardware]

**Research date:** [date]

---

## Test Results

### What Worked
- [Specific example with evidence — terminal output, file output, observable behaviour]
- [Another example]

### What Didn't
- [Specific example with evidence — exact error, unexpected behaviour, missing functionality]
- [Another example]

### Edge Cases Tested
- [What happened with unusual inputs, large files, missing data, etc.]
- [Note which edge cases were tested and which couldn't be tested]

---

## Code Quality Assessment

**For code-based skills:**
- Lines of code: [rough]
- Language: [language]
- Dependencies: [external deps beyond stdlib]
- Code organization: [clean / messy / well-structured]
- Error handling: [present / absent / basic]
- Documentation: [good / minimal / none]
- Tests included: [yes / no]

**For instruction-only skills:**
- Instruction quality: [clear / vague / comprehensive]
- File count: [X files]
- Word count: [rough]
- Practical or theoretical: [actually useful / aspirational]

---

## Security Assessment

- **ClawHub rating:** [rating]
- **Code review findings:**
  - Credential access: [none / reads X / writes Y]
  - External network calls: [none / calls to X endpoints]
  - File system access: [within expected paths / accesses X outside]
  - Obfuscated code: [none / found X]
  - Companion skill installation: [none / tries to install X]
- **Safety verdict:** [safe / use with caution / unsafe]
- **Researcher's own assessment:** [does the ClawHub rating match your findings? note any discrepancies]
- **ClawHavoc echo:** [If findings resemble patterns from the ClawHavoc incident (early 2026, 1,400+ malicious skills removed), note the parallel here. Cambrian doesn't need to establish a causal link, just flag the resemblance so Claude can decide whether to reference it in the post.]

---

## Comparison with Alternatives

| Feature | [This Skill] | [Alternative 1] | [Alternative 2] |
|---------|-------------|----------------|----------------|
| [Feature] | [X] | [X] | [X] |
| [Feature] | [X] | [X] | [X] |
| Price | Free | $X/mo | $X/mo |

### Where This Skill Wins
- [Specific, honest advantage]

### Where Alternatives Still Win
- [Specific, honest disadvantage]

**Note on pricing:** SaaS pricing in this table is sourced at research time with source URLs and timestamps. Claude re-verifies at final draft time. Pricing is shared responsibility.

---

## Verdict

**Recommendation:** ✅ Recommend / ⚠️ Conditional / ❌ Skip

**Best for:** [who should use this — be specific]

**Not for:** [who should avoid this — be specific]

**One-line take:** [the memorable summary — Cambrian's close-reading judgment]

**Writer guidance:** [which aspects to praise, which to criticise. If the verdict is mixed, note what the balance is. Surface this as context for Claude, not as a prescription — Claude will decide the final tone at drafting time. If everything is equally good or bad, the teardown has no stakes.]

---

[Repeat the per-skill sections above for each skill in a multi-skill teardown. Use the Skills Under Review summary table at the top to index them.]

---

## What This Tells You (Candidate Synthesis)

[Step back from the individual review and identify the larger pattern or insight. What does this skill tell us about the market, the category, or the state of agent skills in general? This is Cambrian's candidate interpretation — Claude will produce the final synthesising claim at drafting time, possibly the same as this candidate and possibly different based on the raw material.]

---

## What Should You Actually Do (Candidate Action Layer)

[Concrete next steps for the reader. If the verdict is ✅, how should they get started? If ⚠️, what should they watch out for? If ❌, what's the alternative they should use instead? This is raw material for Claude's action layer — Claude will shape the final advice based on this and any additional market context research.]

---

## Caveats

[Honest limitations. What the skill doesn't do. What might change. What the testing couldn't cover. Don't sugarcoat.]

---

## Quotable Moments

[Real, verbatim moments from testing. Unpolished. Include terminal output, exact errors, surprising results, weird setup steps. Claude decides what to use at drafting time.]

---

## Candidate Framings

**These are suggestions, not prescriptions. Claude has the authority to pick a different framing at drafting time based on the raw material in the brief.**

- **Candidate central frame:** [the single insight or pattern that could make this teardown worth reading — see research step 10]
- **Candidate hook moment:** [the specific, surprising thing from testing that could open the post — see research step 11]
- **Alternative frame:** [a different angle Claude could take if the primary doesn't hold up in drafting]
- **Surprise or reveal:** [what's unexpected about this skill?]
- **Closing candidate:** [one memorable line that could end the post]

---

## Research Notes

[Additional observations, raw data paths, things that didn't fit elsewhere.]
```

---

## Pre-Flight Checks

Run these before handing off the brief. These are in addition to the universal checks in `brief-universal.md`.

- **[MANDATORY]** The teardown has stakes. The "this teardown matters because..." sentence is completable in one line.
- **[MANDATORY]** The skill has been installed successfully, or the installation failure is documented as part of the teardown.
- **[MANDATORY]** Every file in the skill has been read. The brief should reflect full reading, not skimming.
- **[MANDATORY]** Every declared feature has been tested where possible, or the reason it couldn't be tested is documented.
- **[MANDATORY]** Security assessment is complete — all five categories checked (credential access, external calls, file system scope, obfuscation, companion installs).
- **[MANDATORY]** The ClawHub security rating is noted alongside Cambrian's own assessment. Flag any discrepancies.
- **[MANDATORY]** Both download and install counts are reported. Download-to-install ratio is calculated. All numbers timestamped.
- **[MANDATORY]** Download and install counts verified within the last 7 days before publish. Skill metrics move faster than SaaS pricing, and a stale number is a visible credibility hit. Re-verify at the final draft stage if the numbers are load-bearing in the post.
- **[MANDATORY]** Edge cases were tested, not just the happy path.
- **[MANDATORY]** A candidate central frame is identified — the single insight that could make this teardown worth reading. Surfaced as a candidate, not a prescription.
- **[MANDATORY]** A candidate hook moment is identified — concrete, surprising, verifiable. Surfaced as a candidate, not a prescription.
- **[MANDATORY]** The verdict (✅/⚠️/❌) is consistent with the detailed findings. If the findings are mixed, the verdict is mixed.
- **[MANDATORY]** A candidate "What This Tells You" synthesis is present — Cambrian's interpretive take that Claude will refine or replace at drafting time.
- **[MANDATORY]** A candidate "What Should You Actually Do" action layer is present — raw material Claude will shape into final advice.
- **[MANDATORY]** Writer guidance on what to praise vs criticise is included — the teardown needs stakes.
- **[MANDATORY]** Alternatives are compared with a table. Where the skill wins and where it doesn't are both honest.
- **[GUIDANCE]** The comparison with alternatives includes pricing sourced with URLs and timestamps. Pricing is shared responsibility with Claude at final draft time.
- **[GUIDANCE]** The brief doesn't soft-ball praise. Avoid "powerful" and "comprehensive" as filler adjectives. Replace with specific things the skill actually does well.
