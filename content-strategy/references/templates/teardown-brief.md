# Research Brief: [Skill Name] — [Hook Title]

## Topic & Angle

**Working title:** [title]
**Format:** Teardown
**Why now:** [timeliness]
**The story:** [what's interesting about this skill? why should the reader care?]
**Target audience:** [who is this for?]

---

## Skill Under Review

**Name:** [display name]
**Slug:** [slug]
**Author:** [owner]
**Downloads:** [number]
**Stars:** [number]
**Installs:** [number]
**Download-to-install ratio:** [X:1]
**Code or instructions:** [code-based / instruction-only / hybrid]
**Published:** [date]

---

## What It Claims

[Paraphrase the summary/description]

---

## What It Actually Does

[After reading ALL files. Detailed description of the implementation. If code-based, describe the architecture. If instruction-only, describe the scope and quality of the instructions.]

---

## Installation & Setup

**Steps taken:**
1. [step]
2. [step]

**Issues encountered:** [any problems, missing deps, confusing setup]

**Time to set up:** [rough]

---

## Test Methodology

**What we tested:**
- [Specific test 1]
- [Specific test 2]
- [Specific test 3]

**Environment:** [OS, agent runtime, Python version, etc.]

**What we couldn't test:** [and why — e.g., no credentials, no browser, requires specific hardware]

---

## Test Results

### What Worked
- [Specific example with evidence — terminal output, screenshots, code snippets]
- [Another example]

### What Didn't
- [Specific example with evidence]
- [Another example]

### Edge Cases Tested
- [What happened with unusual inputs, large files, missing data, etc.]

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

---

## Comparison with Alternatives

| Feature | [This Skill] | [Alternative 1] | [Alternative 2] |
|---------|-------------|----------------|----------------|
| [Feature] | [X] | [X] | [X] |
| [Feature] | [X] | [X] | [X] |
| Price | Free | $X/mo | $X/mo |

---

## Verdict

**Recommendation:** ✅ Recommend / ⚠️ Conditional / ❌ Skip

**Best for:** [who should use this]

**Not for:** [who should avoid this]

**One-line take:** [the memorable summary]

---

## Caveats

[Honest limitations]

---

## Quotable Moments

Real moments from testing that make the post feel _tested_ not _researched_. Write these verbatim as they happen — don't polish or summarize. Include terminal output, exact error messages, surprising results, weird setup steps, or anything that made you go "huh" or "nice". Claude can invent plausible scenarios, but real ones are always better.

- [Verbatim moment — e.g., "The SKILL.md said 'just run clawhub install and you're good.' It wasn't. Three missing deps, a Python version conflict, and a config file that doesn't exist until you create it manually."]
- [Verbatim moment — e.g., "Asked it to process a PDF with a handwritten receipt. It extracted the vendor name correctly but listed 'total' as $0.00. Turns out it only handles printed invoices."]
- [Verbatim moment — e.g., terminal output snippet, exact error, surprising success]

---

## Suggested Narrative Elements

For Claude to use or ignore:

- **Hook angle:** [idea]
- **Surprise/reveal:** [what's unexpected about this skill?]
- **Contrast point:** [reframing idea]
- **Closing idea:** [memorable line]
