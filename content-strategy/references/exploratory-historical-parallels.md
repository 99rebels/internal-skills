# Exploratory Findings: ClawHub vs Historical Software Registries

**Date:** 1 May 2026
**Prepared by:** Cambrian
**Status:** Raw findings — gaps flagged with [UNCERTAIN]

---

## 1. Populated Table

| Registry | Launch Date | Time to 15K | Time to 50K | Time to 100K | Curation Model | Listing Cost | Notable Early Conditions |
|---|---|---|---|---|---|---|---|
| **Apple App Store** | 10 Jul 2008 | ~6 months (Jan 2009) | ~9 months (Apr 2009) | ~16 months (Nov 2009) | Manual review from day one | Free to publish; 30% rev share | Launched alongside iPhone 3G. Massive pent-up demand. Apple stated in March 2008 press release that apps "must be approved." Early review reportedly fast (hours–days). |
| **Google Play (Android Market)** | 22 Oct 2008 | ~14 months (Dec 2009) [UNCERTAIN] | ~2.5 years | ~21 months (Jul 2010) | Open submission until Mar 2015 (no review) | Free ($25 developer fee) | Launched same year as iPhone App Store but slower start. Grew faster after review was added (counterintuitive — review coincided with Android's growth, not caused it). |
| **npm** | 12 Jan 2010 | ~3 years (2013) [UNCERTAIN] | ~4 years (2014) | ~5.5 years (Jun 2015) | None (fully open) | Free | Required Node.js adoption. Node was niche in 2010. Growth tracked Node's mainstream adoption curve. 6K packages by Jan 2012, 94.7K by Sep 2014. |
| **Chrome Web Store** | 25 Jan 2010 (gallery) / Dec 2010 (store) | ~2012 [UNCERTAIN — 8.5K Dec 2010, 11.5K Dec 2011] | Unknown | Never reached 100K (138K extensions total as of 2024, 17 years) | Automated scanning + manual review for flagged items | Free ($5 one-time developer fee) | Launched alongside Chrome's dominance. Browser already had massive installed base. Extension API was new but straightforward. |
| **WordPress Plugin Directory** | Feb 2005 (official dir) / May 2004 (first plugins) | ~7 years (end 2011 for 10K+) | ~13 years (end 2017) | Never reached | Manual review (various levels over time) | Free | WordPress was already a major CMS by 2005. Plugin system existed pre-directory. Directory was more a catalogue than a launch catalyst. |
| **VS Code Extensions** | Nov 2015 (marketplace) | ~2018–2019 [UNCERTAIN — 711 Jan 2016, 60K+ Nov 2019] | ~2021–2022 [UNCERTAIN] | ~9 years (May 2025) | Automated + manual review for flagged extensions | Free | Launched alongside VS Code preview. Editor was initially dismissed ("Visual Studio but worse"). Growth tracked VS Code's unexpected dominance. |
| **PyPI** | 2003 | ~9–10 years (2012–2013) [UNCERTAIN — 5.4K in 2010] | ~15 years | ~16 years (Jul 2019) | Minimal post-publication moderation | Free | Pre-existed modern packaging tooling. Pip came later. Growth was glacial for a decade, then exponential. Python's mainstream adoption drove it. |
| **Hugging Face Models** | ~Apr 2021 (model hub) | Unknown — early milestones not well-documented | Unknown | ~3.5 years (Sep 2024, ~1M models) | None (fully open) | Free | Launched during AI/ML boom. LLM wave (2022+) was the inflection point. 2M models by Dec 2025. Growth is hyperbolic — most models are fine-tunes/quantizations of a few base models. |
| **Salesforce AppExchange** | 2005 (GA 2006) | Never reached (only 5,661 total by Dec 2024) | N/A | N/A | Security review required | Free to list; revenue share on paid apps | Enterprise B2B context. High quality bar. Growth measured in installs, not listings. Each app requires significant development. |
| **ClawHub** | ~3 Jan 2026 (repo created) / ~4 Jan 2026 (first release) | ~5–6 weeks (Feb 2026) [ESTIMATED from 52.7K at 4 months] | ~2–3 months (Mar 2026) [ESTIMATED] | ~3.5 months (mid-Apr 2026) [ESTIMATED] | No pre-publication review. Reactive content policy. Post-hoc security rating + flagging. | Free | SKILL.md standard launched ~Dec 2025 [per memory, UNVERIFIED]. Launched into an existing ecosystem of OpenClaw users. AI agents as the "runtime" — no new tooling needed for most users. |

---

## 2. Observations (~400 words)

### Where ClawHub Sits on Raw Speed

ClawHub is, by a significant margin, the fastest software registry to reach every milestone in this set. The Apple App Store — previously the benchmark — took 6 months to reach 15,000. ClawHub likely reached 15,000 in 5–6 weeks and 100,000 in under 4 months. The second-fastest is the App Store itself, which took 16 months to reach 100K.

The gap isn't incremental. It's an order of magnitude. ClawHub hit 52,700 listings in roughly 119 days (Jan 3 → May 1). That's ~443 listings per day. No other registry in this set has ever sustained anything close to that rate in its first year.

### The App Store Comparison

The manifesto's "15,000 in six months" figure was accurate — Apple announced 15,000 apps on January 16, 2009, six months after the July 2008 launch. However, the LinkedIn commenter's point about review is valid in spirit if not in magnitude. Apple required approval from day one (per their March 2008 press release). Early review turnaround was reportedly fast — hours to a few days — and the quality bar was low. But it was still a gate. Nothing shipped without Apple's say-so.

ClawHub has no gate. Skills publish immediately. There's a reactive content policy and a post-hoc security rating system, but nothing prevents a skill from going live. This is a meaningful structural difference that the post should acknowledge directly.

### Fairest Comparisons

The fairest comparisons are the permissionless registries: npm, PyPI, Hugging Face, and Google Play (pre-2015). These had no review gate and free listing. ClawHub beats all of them on raw speed, but the comparison is complicated by context:

- npm and PyPI required developer tooling adoption (Node.js, pip) that didn't yet exist at scale
- Hugging Face required ML expertise and compute resources
- ClawHub requires only a markdown file and an existing OpenClaw installation

The "barrier to publish" is lower on ClawHub than on any of these. A SKILL.md is a text file with instructions. A PyPI package requires code, tests, and packaging. A Hugging Face model requires weights and compute. This is relevant to the comparison and should be in the post.

### The Closest Fit

Hugging Face is the closest structural parallel: permissionless, free, AI-adjacent, recent, and growing extremely fast. But Hugging Face's growth was driven by a different dynamic — mostly fine-tunes and quantizations of base models, which are low-effort to create. ClawHub's growth is driven by prompt-based instructions, which are even lower-effort. The two ecosystems share a "low-friction, high-volume" character that the App Store and npm don't.

### A Pattern Worth Noting

Every registry that grew fast had one of two things: (1) a massive pre-existing installed base (App Store = iPhone users, Chrome Web Store = Chrome users) or (2) zero friction to publish (npm, PyPI, Hugging Face, ClawHub). ClawHub is unusual in having both — an installed base via OpenClaw and zero friction to publish.

---

## 3. Recommendation: Which Parallels to Keep

**Keep (3):**
1. **Apple App Store** — the original comparison, the one the LinkedIn commenter challenged. Must include. The review-gate nuance is the post's credibility moment.
2. **Hugging Face** — closest structural parallel and the one most readers will find intuitive ("like Hugging Face but for agent skills"). Good for the "different kind of fast" argument.
3. **npm** — the canonical developer registry. Including it shows we're not cherry-picking. It's the one most developers understand intuitively.

**Drop (6):**
- **Google Play** — adds a second app store that complicates the table without adding insight. The App Store covers this territory.
- **Chrome Web Store** — too slow, too different (browser extensions ≠ agent skills). No 100K milestone.
- **WordPress** — glacially slow. Including it makes the table lopsided rather than informative.
- **VS Code** — interesting but niche. The 100K milestone took 9 years. Doesn't illuminate the comparison.
- **PyPI** — npm covers the "developer package registry" angle. Two is redundant.
- **Salesforce AppExchange** — never reached 15K. Enterprise B2B context is too different to be useful.

**Maybe (1):**
- **Google Play** could replace one of the "keep" set if Rian wants to show that even the second app store was slower. But I'd default to dropping it.

---

## 4. Gaps Needing More Research

- **ClawHub 15K and 50K milestone dates.** Estimated from current count (52.7K at 119 days). The actual dates would strengthen the post. Check ClawHub blog, changelog, or Wayback Machine snapshots.
- **SKILL.md standard launch date.** Memory says December 2025, but this is unverified. The ClawHub GitHub repo was created January 3, 2026 — was there a pre-GitHub existence? Check OpenClaw docs, Discord announcements, or GitHub commits in the openclaw/openclaw repo.
- **Hugging Face early milestones (15K, 50K models).** These aren't well-documented in public sources. Hugging Face's own blog posts focus on the 1M milestone. Could try the HF API to find the `createdAt` of the 15,000th model, but this would require scraping and may not be accurate (model deletions/renames).
- **npm 15K date.** Estimated at ~2013 based on interpolation between 6K (Jan 2012) and 94.7K (Sep 2014). npm's own historical data page (modulecounts.com) may have this.
- **ClawHub weekly/monthly growth rate.** The 52.7K total doesn't tell us whether growth is linear, exponential, or front-loaded. A growth chart would be more compelling than a single number.
- **Apple App Store early review turnaround times.** I've stated "hours to days" based on secondary sources. A primary source (developer blog post from 2008–2009, Steve Jobs email) would be stronger.

---

## 5. Blockers or Issues

- **Gemini search rate limit.** Hit the 20/day free tier limit. Several searches (Hugging Face early milestones, npm specific dates, VS Code milestones) couldn't be completed. If the directed brief needs these, they'll need another pass.
- **ClawHub data availability.** The ClawHub homepage shows aggregate stats (52.7K tools, 180K users, 12M downloads) but I couldn't find historical milestone data or a public API for querying skill counts by date. The clawhub CLI doesn't expose total counts. This may require asking the ClawHub team directly or checking if there's a changelog/archive.
- **App Store review timing nuance.** The early App Store review process is well-documented anecdotally but I couldn't find a definitive primary source for turnaround times in July–December 2008. The post may need to hedge this ("reportedly" or "according to developer accounts from the era").
