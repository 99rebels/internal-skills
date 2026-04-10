# Research Brief: Local Business Web Agency

## Topic & Angle

**Working title:** "I Charged €800 for a Website I Built in an Afternoon. Here's How."
**Format:** Skill Stack to Outcome (guide)
**Why now:** Local businesses are desperately underserved online. Every town has dozens of businesses with no website or a terrible one. AI agent skills make it possible to build professional sites fast enough to make it a viable service business.
**The story:** A step-by-step guide showing how three free AI skills combine into a workflow: audit the client's current site (free sales tool), build them a new one (the product), set up their local SEO (the upsell). The skills handle the heavy lifting — you handle the client relationship and customization.
**Target audience:** Freelancers, devs, and entrepreneurs looking for a service business with real revenue potential

---

## Skills Tested

| # | Skill | Slug | Downloads | Stars | Installs | Code or Instructions? |
|---|-------|------|-----------|-------|----------|----------------------|
| 1 | Homepage Audit | brw-homepage-audit | — | — | — | Instruction-only (framework/checklist) |
| 2 | React Local Business Website | react-local-biz | — | — | — | Code + templates (real React project) |
| 3 | Local SEO | local-seo | — | — | — | Instruction-only (framework/checklist) |

---

## Skill 1: Homepage Audit (brw-homepage-audit)

**Install:** `clawhub install brw-homepage-audit`

### What It Claims
Quick conversion audit for any homepage or landing page. Reviews above-the-fold clarity, value proposition, social proof, copy, CTAs, and trust signals.

### What It Actually Does
It's an instruction-only skill — a structured framework/checklist for evaluating landing pages. No code, no scripts, no automation. The agent follows the checklist when you ask it to "audit my homepage" or "review my landing page."

The checklist covers:
- 5-Second Test (what's this / who's it for / why care / what next)
- Above the Fold (performance, mobile, headline, CTA, visual, navigation)
- Value Proposition (benefit clarity, audience, differentiation)
- Social Proof (testimonials, logos, numbers)
- Clarity & Copy (scannable, concise, benefits > features)
- CTA & Conversion (primary CTA obvious, repeated, low-friction)
- Trust & Risk Reduction (pricing, guarantee, FAQ, support)

It outputs a **scored report** (X/5 weighted across categories) with:
- 5-Second Test results
- Top 3 issues prioritized
- Quick wins (<1 hour changes)
- Bigger opportunities (longer term)

### Test Methodology
Used the framework to mentally audit a hypothetical local plumber's site (single-page, no mobile optimization, company name as headline, "Contact Us" CTA).

### Test Results
**What worked:**
- The framework is comprehensive and structured — covers all the right conversion factors
- The scoring system (1-5 weighted) gives you a concrete number to show clients
- "Quick wins" section is immediately actionable
- The "5-Second Test" is a great opening — clients instantly understand "your site fails this"

**What didn't:**
- No automation — you have to manually walk through each section
- Requires you to be able to view the site (screenshot, URL, or paste copy)
- Some overlap between categories (trust and social proof, clarity and value prop)

**Overall experience:** This is a sales tool, not a technical tool. You use it to diagnose problems and show clients why they need a new site. The scored output is the deliverable — "your site scored 1.8/5, here are the top 3 problems." That's your foot in the door.

### Security Assessment
- **Code review findings:** No code — instruction-only skill. No external calls, no credential access, no file system access beyond reading the SKILL.md.
- **Safety verdict:** ✅ Safe

### Pros
- Structured, professional audit framework
- Scored output creates urgency for clients
- Easy to follow, covers all key conversion factors

### Cons
- No automation — manual process
- Requires the agent to have access to view the site
- Instruction-only — quality depends entirely on the LLM following it well

---

## Skill 2: React Local Business Website (react-local-biz)

**Install:** `clawhub install react-local-biz`

### What It Claims
Build complete, modern multi-page React websites for local businesses. Handles project scaffolding, full design system, all 5 standard pages, image strategy, responsive layout, animations, and production build.

### What It Actually Does
This is a **real code skill** with templates and a design system. It generates a complete 5-page React site using:
- Vite + React (project scaffold)
- Tailwind CSS v3 (styling)
- React Router v6 (page routing)
- Framer Motion (scroll animations)
- Lucide React (icons)

**Stack:**
| Tool | Purpose |
|---|---|
| Vite + React | Project scaffold |
| Tailwind CSS v3 | Styling |
| React Router v6 | Page routing |
| Framer Motion | Scroll animations |
| Lucide React | Icons |

**5 pages generated:**
1. **Home** — Hero (full viewport), stats bar, services preview, why-choose-us, portfolio grid, testimonials, CTA banner
2. **Services** — Page hero, 6-card service grid with features, how-it-works (4 steps), CTA
3. **Portfolio** — Page hero, filterable gallery with lightbox, featured project block, CTA
4. **About** — Page hero, story section, core values, timeline, team cards, awards grid
5. **Contact** — Page hero, validated form + contact info panel, business hours, social proof strip

**Design system includes:**
- Per-industry color palettes (landscaping, restaurant, salon, plumbing, gym, real estate, vet, generic)
- Curated Unsplash image packs per industry
- Reusable component classes (buttons, cards, inputs)
- Section layout patterns (hero, sub-hero, alternating bg, CTA)
- Animation tokens (fade-up, fade-left/right, scale-in, stagger)
- Responsive grid patterns
- Google Fonts pairings by vibe

**Reference files:**
- `references/business-types.md` — 8 industry palettes + Unsplash image URLs
- `references/design-system.md` — Tailwind config, fonts, CSS components, layout patterns
- `references/page-templates.md` — Section-by-section structure for all 5 pages with copy formulas

**Assets included:**
- Full landscaping template site (HTML, CSS, JSX) as a working example

### Test Methodology
Built a complete plumber website ("O'Connor Plumbing — Dublin's Trusted Plumbers") following the skill's workflow:
1. Created Vite + React project
2. Installed dependencies (tailwindcss, react-router-dom, framer-motion, lucide-react)
3. Configured tailwind with plumber palette (navy blue + orange accent)
4. Wrote index.html with Google Fonts
5. Wrote index.css with Tailwind directives + component classes
6. Wrote App.jsx with router + navbar/footer wrap
7. Wrote 3 components (Navbar, Footer, ScrollToTop)
8. Wrote all 5 pages with full content
9. Ran `npm run build` — **passed clean in 1.07s**

**Environment:** Raspberry Pi 5 (arm64, Linux 6.12), Node v24.14.1

### Test Results
**What worked:**
- Build passes clean — no errors, no warnings
- Output is 464KB total (122KB gzipped JS + 4.7KB gzipped CSS)
- Design system is genuinely good — responsive, animated, professional-looking
- Per-industry palettes and Unsplash image packs make it easy to customize
- Page templates are comprehensive with real copy formulas
- Framer Motion animations add polish without being over the top
- Contact form has proper validation
- Mobile responsive (Tailwind responsive classes throughout)

**What didn't:**
- Had a JSX closing tag bug (`</p>` instead of `</motion.p>`) — easy to fix but shows you need to verify the build
- The Unsplash images are stock photos — real client work would need their own photos
- No backend — the contact form doesn't actually send anywhere (would need Formspree/Netlify Forms/etc.)
- No SEO setup (meta tags, sitemap, robots.txt) — that's a separate step
- No dark mode
- Total lines written: ~836 lines of JSX/CSS across 11 files — this is a LOT of code for an agent to generate correctly in one go

**Overall experience:** This skill genuinely produces a professional-looking local business website. The design system is well-thought-out. But it requires careful execution — 836 lines of code with specific patterns, and any JSX typo will break the build. The agent needs to be methodical and verify the build at the end. For a freelancer, this is the production tool — it makes you fast, not unnecessary.

### Setup Time Estimate
- npm install + dependencies: ~30-60 seconds (depends on connection)
- Writing all config + component + page files: ~10-15 minutes with an agent
- Build verification: ~1 second
- **Total: ~15-20 minutes** for the full site generation (assuming agent does it correctly first time)

### Security Assessment
- **Code review findings:** Template files only — no executable scripts, no external API calls, no credential access. All images come from Unsplash (public CDN). No obfuscated code.
- **Safety verdict:** ✅ Safe

### Pros
- Real, production-ready code
- Comprehensive design system with industry-specific palettes
- All 5 pages with full content templates
- Responsive + animated out of the box
- Build passes clean

### Cons
- 836 lines of code — agent needs to be careful, any typo breaks build
- No backend for contact form (needs separate solution)
- No SEO setup included (meta tags, sitemap)
- Stock photos only — real clients need their own
- Requires Node.js + npm on the machine

---

## Skill 3: Local SEO (local-seo)

**Install:** `clawhub install local-seo`

### What It Claims
Guides local SEO: Google Business Profile, NAP consistency, and citation building. Businesses with accurate NAP across 40+ authoritative sites see ~19% higher visibility in Google Maps.

### What It Actually Does
Instruction-only skill — a structured framework for optimizing a local business's search presence. No code, no automation, no scripts.

Covers three areas:

**1. NAP Consistency (Name, Address, Phone)**
- Exact match requirements ("Street" vs "St." inconsistency = Google treats as different entities)
- Fix-first approach: audit inconsistencies before adding new citations
- References external tools (BrightLocal, Whitespark, Moz Local) for auditing

**2. Google Business Profile (GBP)**
- Physical address (no P.O. boxes)
- Description (750 chars, primary keywords in first 100)
- Hours (accurate, seasonal availability)
- Category (must match business type)
- Service-area (hide address if no storefront)

**3. Citation Building**
Priority order: GBP → Apple Maps → Yelp/Bing/Facebook → BBB/Foursquare/Nextdoor → Niche directories
- Emphasis on "targeted precision over submitting to every directory"
- Citation audit checklist (incorrect data, duplicates, missing listings)

**Output format:**
- NAP format for consistency
- GBP optimization checklist
- Citation priority list
- Audit findings

### Test Methodology
Mentally applied the framework to the hypothetical plumber (O'Connor Plumbing, Dublin 2).

### Test Results
**What worked:**
- Clear, actionable framework — covers all the important local SEO factors
- Priority order for citations is smart (not just "submit everywhere")
- NAP consistency emphasis is correct — this is genuinely the #1 local SEO mistake
- GBP optimization checklist is practical
- The "19% higher visibility" stat adds credibility (referenced in the skill)

**What didn't:**
- No automation — purely instructional
- References paid tools (BrightLocal, Whitespark, Moz Local) for auditing
- Doesn't cover schema markup or local structured data
- Doesn't cover review management strategy
- Relatively short — could be more comprehensive

**Overall experience:** This is the **upsell** skill. After building the site, you offer to set up their GBP, fix their NAP, and build citations. The framework gives you a checklist to follow and a deliverable to present. It's simple but effective — most local businesses have zero local SEO, so even basic GBP optimization is a massive improvement.

### Security Assessment
- **Code review findings:** No code — instruction-only. No external calls, no credentials.
- **Safety verdict:** ✅ Safe

### Pros
- Covers the essential local SEO factors
- Clear priority order for citations
- NAP consistency is genuinely the most impactful local SEO fix
- Creates a clear deliverable (checklist + audit report)

### Cons
- Instruction-only — no automation
- References paid tools without free alternatives
- Doesn't cover schema markup or review strategy
- Relatively thin — could be more comprehensive

---

## The Workflow (How They Combine)

**Step 1: Get the client (brw-homepage-audit)**
- Find a local business with a bad website
- Run the audit framework
- Present the scored report: "Your site scored 1.8/5. Here are the top 3 problems."
- Offer to fix it

**Step 2: Build the site (react-local-biz)**
- Gather client info: business name, type, location, services, contact details
- Pick the matching industry palette from business-types.md
- Generate the full 5-page React site following the skill's workflow
- Customize with client-specific content (services, testimonials, team)
- Build and deploy

**Step 3: Upsell local SEO (local-seo)**
- Offer GBP optimization, NAP fix, and citation building
- Follow the framework checklist
- Present as an add-on package

**Realistic pricing:**
| Service | Typical Range |
|---------|--------------|
| Site audit (free or €50-100) | Lead generation — often free to win the client |
| Website build | €500-1,500 (solo freelancer, template-based) |
| Local SEO setup | €200-500 (GBP + citations + NAP) |
| **Total per client** | **€700-2,000** |

---

## Deployment Note

The skill doesn't include a deployment skill in the final stack. For a real workflow, you'd deploy to Netlify (free tier) or Vercel (free tier). We tested `netlify` from ClawHub — it's a solid skill for CI/CD setup. Deployment adds ~5 minutes to the workflow.

---

## Quotable Moments

- "After running `npm run build`, the entire site compiled clean in 1.07 seconds. 464KB total. 836 lines of code across 11 files. All generated from a skill's design system and templates."
- "The hardest part wasn't the code — it was the closing tag typo. `</p>` instead of `</motion.p>` broke the entire build. One character. That's the kind of thing you learn to check."
- "The design system includes 8 pre-built industry palettes with curated Unsplash image packs. Plumbers get navy blue + orange. Salons get dusty rose + gold. It's thoughtful — the kind of thing that makes the difference between 'template' and 'custom.'"
- "The contact form validates properly, has a success state with a personalized thank you, and even includes a 'Your info is never shared' trust signal. For a plumber's website. The client will think you spent days on this."

---

## Suggested Narrative Elements

- **Hook angle:** "Every town has dozens of businesses with no website or a terrible one. Most freelancers charge €500 minimum. Here's how AI skills let you build professional sites in an afternoon."
- **Contrast point:** "The plumber in my town had a single-page site from 2012 with a company name as the headline and a 'Contact Us' button that didn't work. His competitor had a 5-page React site with animations and mobile responsive design. Guess who gets the call."
- **Compounding story:** Walk through the full workflow — audit → build → SEO setup → deploy. Show how each skill feeds into the next. The audit gets you in the door, the build is the product, the SEO is the upsell.
- **Closing idea:** "The skills don't make you a web designer. They make you fast. The client relationship, the customization, the attention to their specific business — that's still you. The skills just mean you can do it in an afternoon instead of two weeks."

---

## Caveats

- **This is a template workflow, not magic.** The skills give you a starting point — you still need to customize for each client, handle revisions, and manage the relationship.
- **No backend.** The contact form is frontend-only. You'll need to add Formspree, Netlify Forms, or similar for it to actually send emails.
- **No SEO baked into the site.** Meta tags, sitemap, robots.txt, schema markup — all separate steps the skill doesn't cover.
- **Stock photos.** Unsplash images are great for demos but real clients need their own photos. Budget time for this.
- **Local SEO skill is thin.** It covers the basics (GBP, NAP, citations) but doesn't touch schema markup, review management, or content strategy. You'll need to supplement with your own knowledge.
- **Build verification is critical.** We caught a JSX typo that broke the build. Always run `npm run build` before delivering.
- **836 lines of code is a lot.** An agent generating this much code needs to be methodical. If it rushes, it will produce bugs. Budget 15-20 minutes minimum for generation, plus verification time.
- **The €700-2,000 range is realistic but depends on your market and skill.** In Dublin, a freelancer could charge €500-800 for a template-based site. In London or New York, double that. In a smaller market, half that.

---

## Research Notes

- The `google-my-business` skill was initially in the stack but was dropped — it requires a third-party tool (Membrane CLI) with auth, and was flagged as suspicious by VirusTotal. The local-seo skill covers GBP optimization conceptually without needing the API integration.
- The `netlify` skill was tested and works well for deployment, but isn't needed in the 3-skill stack since deployment is commodity knowledge (anyone can `netlify deploy`).
- The react-local-biz skill is by far the strongest in the stack — genuine code, comprehensive design system, industry-specific templates. This is the one that does the real work.
- The audit skill is the sales tool — it's not technically impressive but it's the one that wins clients. "Your site scored 1.8/5" is a powerful opening line.
- The local-seo skill is the upsell — thin but effective for the basics. Most local businesses have zero SEO, so even basic optimization is valuable.
