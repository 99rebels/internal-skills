# Exploratory Findings: B2B Product PDF Conversion Stack Play

**Date:** 11 April 2026
**Format (tentative):** Stack Play
**Working direction:** 3-4 skill stack converting legacy product PDFs into structured, schema-marked-up product page content

---

## 1. Candidate Stack Table

### Stage 1: PDF Parsing and Text Extraction

| # | Skill | Slug | Author | Downloads | Installs | D:L Ratio | Last Updated | Code/Instructions | One-line description |
|---|-------|------|--------|-----------|----------|-----------|-------------|-------------------|---------------------|
| 1 | **PDF Extract** | `pdf-extract` | Xejrax | 13,991 | 198 | 71:1 | ~3 Mar 2026 | Code (instruction-only — no scripts, just a SKILL.md wrapper around `pdftotext`) | Thin wrapper around `pdftotext` (poppler-utils) for extracting text from PDFs. Has no actual code — just tells the agent to run `pdftotext`. |
| 2 | **PDF Processing** | `pdf-processing` | 银河诗人 (rainshow) | 2,608 | 18 | 145:1 | ~12 Mar 2026 | Instruction-only | Claims text extraction, table extraction, form filling, and merge. No actual scripts shipped — just a SKILL.md saying "put scripts in scripts/". Empty shell. |
| 3 | **PDF Toolkit Pro** | `pdf-toolkit-pro` | gdp6539 | 2,452 | 23 | 107:1 | ~11 Apr 2026 | Code (Node.js) | Merge, split, compress, convert PDFs. Uses pdf-lib, sharp, pdf2pic. **No text extraction capability** — this is a manipulation toolkit, not a parser. Flagged suspicious by VirusTotal (false positive on crypto/pdf libs, but noted). |

**Assessment:** PDF Extract is the strongest by download count and install count, but it's literally just `pdftotext` with a skill wrapper. PDF Processing is an empty shell. PDF Toolkit Pro doesn't extract text at all. **None of these skills do what the pipeline actually needs for stage 1**, which is structured table extraction from engineering PDFs.

**The real tool for this stage is `pdfplumber`** (Python library, not a ClawHub skill). It extracts text, tables, and layout from PDFs with significantly better table handling than `pdftotext`. It's what the pdf-processing skill *claims* to use but doesn't actually ship.

**Also relevant but not tested:** `document-parser` (ankylala) — sends PDFs to an external API at `http://47.111.146.164:8088` for layout analysis, table recognition, and OCR. Suspicious flagged. External API dependency. Chinese-language skill. The external API endpoint is an opaque Chinese server — I did not test this against production data. The code reads files and sends them to the remote server. **Security concern: unclear data handling at the remote endpoint.**

**Also relevant:** `mineru-extract` (easerene) — sends URLs/PDFs to the MinerU API (mineru.net) for conversion to structured Markdown with layout analysis. Requires a paid API token. Suspicious flagged. I did not test this because it requires a MinerU account/token.

### Stage 2: Structured Data Extraction (from unstructured text)

**No dedicated skill exists for this stage on ClawHub.**

I searched for: "data extraction", "structured data", "extract", "parser", "document parser". The closest candidates are:

| # | Skill | Slug | Why it's close | Why it's not right |
|---|-------|------|---------------|-------------------|
| 1 | `document-summary` | kelevis | Takes text input, produces structured markdown summary | Summarises documents — doesn't extract structured fields (dimensions, materials, ratings, etc.) |
| 2 | `document-parser` | ankylala | Claims structured data extraction from PDFs | Sends to external Chinese API — not a local skill. Security concerns. |
| 3 | `mineru-extract` | easerene | Converts PDFs to structured Markdown via MinerU API | External API dependency, requires token. Not local extraction. |

**This is the critical gap.** The pipeline needs a skill that takes raw PDF text (from stage 1) and extracts structured product fields: dimensions, weight, power rating, voltage, materials, operating temperature range, flow rate, head, efficiency, protection class, etc. No ClawHub skill does this locally.

**In practice, this stage would be performed by the LLM agent itself** — reading the extracted text and using its own reasoning to identify and extract structured fields. This is actually the most reliable approach for the heterogeneous PDF formats encountered in B2B catalogues, because the field names, layouts, and units vary enormously across manufacturers. A deterministic extraction script would need a different template for every manufacturer. An LLM can generalise.

### Stage 3: Data Normalisation

**No skill exists for this stage.**

Searched: "normalize", "normalise", "transform", "convert". Found `data-format-converter` (CSV↔JSON↔XML↔YAML↔TOML) and `convert-units` (unit conversion), neither of which does field name normalisation or cross-document schema alignment.

**This stage is also best performed by the LLM agent.** Normalising "1.5 HP (1.1 kW)" to a standard power field, "AISI 304" to a material field, "IP55" to a protection class, "1745 rpm" to a speed field — this requires domain understanding that a deterministic skill can't provide without extensive configuration per manufacturer.

### Stage 4: Schema Markup Generation / HTML Output

| # | Skill | Slug | Author | Downloads | Installs | Code/Instructions | One-line description |
|---|-------|------|--------|-----------|----------|-------------------|---------------------|
| 1 | **Schema Markup** | `schema-markup` | wpank | 1,281 | 18 | Instruction-only | Comprehensive reference guide for implementing schema.org structured data (JSON-LD). Covers Product schema with examples, required/recommended fields, validation tools. This is an instruction-only skill — it tells the agent *how* to write schema markup, but doesn't generate it programmatically. |
| 2 | `schema-markup-seo` | kostja94 | 42 | 0 | Instruction-only | Similar to above, same author's earlier version. Zero installs. |
| 3 | `product-page-seo` | nexscope-ai | 116 | 0 | Instruction-only | E-commerce product page SEO audit framework. Mentions Product schema but focuses on auditing, not generating. Zero installs. |
| 4 | `products-page-generator` | kostja94 | 104 | 0 | Instruction-only | Category/listing page guidance. Not relevant to individual product page generation. Zero installs. |
| 5 | `html-coder` | jhauga | 763 | 6 | Instruction-only | HTML development reference. Could help an agent write HTML product pages, but it's a general HTML reference, not product-page-specific. |

**Assessment:** Schema Markup (wpank) is the strongest candidate — it has actual downloads, installs, and a solid Product schema template with all required and recommended fields. However, it's instruction-only: it teaches the agent how to write schema markup, it doesn't generate it. **The LLM agent would use this skill's reference material to generate the schema markup itself.** This is actually the right model for this use case — the schema output depends on the structured data from stage 2/3, so it has to be dynamically generated per product, not templated.

---

## 2. PDF Run Results

### Test PDFs Used

| # | File | Source | Layout | Pages |
|---|------|--------|--------|-------|
| 1 | `motor-spec.pdf` | wolfautomation.com (WEG motor datasheet) | **Table-heavy**: dense spec table with key-value pairs in two columns | 1 |
| 2 | `pump-spec.pdf` | dabpumps.com (DAB KI centrifugal pump) | **Mixed**: performance curves (graphs), tables (materials, dimensions, power), prose (application description) | 3 |
| 3 | `submersible-pump.pdf` | mwipumps.com (MWI submersible pump) | **Prose-heavy**: engineering specification document with structured fields embedded in prose paragraphs | 4 |
| 4 | `valve-spec.pdf` | sandpiperpump.com (Sandpiper diaphragm pump) | **Mixed**: data submittal pack with forms, tables, engineering drawings, material compatibility charts | 9 |
| 5 | `bearing-spec.pdf` | rbcbearings.com (RBC Nice bearings catalog) | **Catalog**: table of contents, product overview, dimension tables across 60 pages | 60 |

### Stage 1 Results: PDF Text Extraction

**Tool used:** `pdftotext` (poppler-utils, the tool wrapped by pdf-extract) and `pdfplumber` (Python library)

**motor-spec.pdf (1 page, table-heavy):**
- `pdftotext`: Extracted all text cleanly. Key-value pairs like "Frame : 143/5T", "Output : 1.5 HP (1.1 kW)" came through perfectly. The two-column layout was interleaved correctly. **Quality: usable as-is.**
- `pdfplumber`: Detected 1 table (14 rows × 7 cols), but the table structure was messy — key-value pairs were packed into cells with newlines, not aligned as clean rows/columns. The raw text extraction was better than the table extraction for this PDF. **Quality: text usable, tables need cleanup.**

**pump-spec.pdf (3 pages, mixed layout):**
- `pdftotext`: Page 1 (graphs) produced garbled coordinate data — performance curves are inherently graphical and don't extract as text. Pages 2-3 extracted cleanly: materials table, dimensions table, power table, packing dimensions all readable. **Quality: graphs fail (expected), tables usable with light cleanup.**
- `pdfplumber`: Page 1: 0 tables (correct — it's graphs). Page 2: 8 tables detected, of which 3-4 were meaningful (materials, power ratings, packing dimensions). Some tables had merged cells and multi-line values that needed cleanup. Performance curve data was partially captured in tables but in a confusing format. **Quality: mixed. Some tables clean, some garbled. Would need human review per table.**

**submersible-pump.pdf (4 pages, prose-heavy):**
- `pdftotext`: All text extracted cleanly. Structured fields like "Pumping Capacity: ______ GPM each" came through, but the values were blank (this is a specification template, not a filled-in data sheet). The prose sections about construction requirements, bearing specifications, seal specifications, and weldment standards extracted perfectly. **Quality: usable as-is.**
- `pdfplumber`: 0 tables detected across all 4 pages. The document is prose with structured fields embedded in paragraphs — pdfplumber's table detection correctly identified no tabular data. **Quality: text usable, no table extraction needed.**

**valve-spec.pdf (9 pages, mixed layout):**
- `pdftotext`: Pages 1-2 (data sheet forms) extracted reasonably — field labels came through but some alignment was lost. Pages 3-4 (engineering drawings) produced coordinate garbage. Page 5 (material compatibility table) extracted well. Pages 6-7 (dimension drawings) produced coordinate garbage. Page 8 (certification) extracted cleanly. Page 9 (ATEX certification table) was partially garbled. **Quality: mixed. Forms and text pages usable, drawing pages fail.**
- `pdfplumber`: 12 tables detected across 9 pages. The data sheet form on page 2 was detected as a 74-row × 16-col table, which is technically correct but the form fields (blank fill-in fields) came through as empty cells. The material compatibility table on page 5 was extracted cleanly. Dimension drawing pages produced tables with garbled coordinate data. **Quality: mixed. Forms partially usable, drawings fail, material tables clean.**

**bearing-spec.pdf (60 pages, catalog):**
- Did not run full extraction — this is a product catalog, not a single product spec. The first 5 pages show a table of contents, product overview, and industrial markets served. **Not a good test for single-product extraction.** Would need to target specific pages for specific bearing product specs.

### Stage 2 Results: Structured Data Extraction

**No ClawHub skill was run for this stage** because no suitable skill exists (see gap analysis above).

**Simulated using LLM reasoning on the extracted text:**

For motor-spec.pdf, an LLM can reliably extract:
- Product name: "Single Phase Induction Motor - Squirrel Cage"
- Manufacturer: WEG
- Catalog number: 00158ES1B145T-S
- Power output: 1.5 HP (1.1 kW)
- Voltage: 115/208-230 V
- Speed: 1745 rpm
- Insulation class: F
- Protection degree: IP55
- Weight: 48.0 lb
- Efficiency: 77.0% at full load

**Quality assessment: highly reliable for this PDF type.** The key-value pair format maps cleanly to structured fields.

For pump-spec.pdf, an LLM can extract from the materials and power tables but would struggle with the performance curve data (graphical). The materials table (AISI 304 stainless steel, NBR, carbon/ceramic) extracts cleanly. The power ratings (kW, Hp, current, capacitor) extract cleanly. The packing dimensions (mm measurements) extract cleanly. **Quality: good for tabular data, poor for graphical performance data.**

For submersible-pump.pdf, an LLM can extract construction specifications (bearing types, seal types, materials, weldment standards) from the prose but many values are blanks in the template. **Quality: extracts what's there, but this is a template, not a filled spec.**

For valve-spec.pdf, the data sheet form fields are mostly blank (this is a customizable template). The material compatibility data (temperature ranges for FKM, Nitrile, PTFE) extracts well from the table on page 5. **Quality: limited by the template format.**

### Stage 3 Results: Normalisation

**No skill tested.** In practice, the LLM agent would handle this during stage 2 — extracting fields into a normalised schema in a single pass rather than extracting raw and then normalising separately. There's no practical reason to separate these two stages when an LLM is doing both.

### Stage 4 Results: Schema Markup

**Schema Markup (wpank) was read but not "run"** — it's instruction-only. Using its Product schema template, the output for the motor spec would look like:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Single Phase Induction Motor - Squirrel Cage",
  "description": "1.5 HP (1.1 kW) single phase induction motor, 4-pole, 60 Hz, IP55 protection",
  "sku": "00158ES1B145T-S",
  "brand": { "@type": "Brand", "name": "WEG" },
  "offers": {
    "@type": "Offer",
    "availability": "https://schema.org/InStock"
  }
}
```

Note: the schema.org Product type doesn't have native fields for most B2B engineering specs (insulation class, protection degree, locked rotor torque, etc.). These would need to be captured either as `additionalProperty` key-value pairs or as custom structured data beyond the standard Product schema. **This is a real limitation of the schema.org vocabulary for B2B industrial products.** The standard Product schema is designed for consumer e-commerce (price, availability, ratings), not engineering specifications.

---

## 3. Observations (~400 words)

### What the exploratory pass reveals

The working hypothesis was partially right and partially wrong.

**Right:** The parsing stage is well-covered at the tooling level — `pdftotext` and `pdfplumber` are mature, reliable, and handle the common PDF layouts well. The structured data extraction stage is indeed the variable one. The normalisation stage is the weakest as a standalone step.

**Wrong:** The hypothesis assumed the weakness would be in deterministic tools failing on prose-heavy PDFs. The actual finding is more interesting: **the weakness isn't in the tools, it's in the skill ecosystem.** No ClawHub skill exists for the extraction or normalisation stages. The pipeline doesn't fail because the tools are bad — it fails because the skills don't exist, and the agent would need to do stages 2-3 entirely from its own reasoning, using no skill at all.

**What this means for the stack:** The pipeline would be a 2-skill stack at most, not 3-4. Stage 1 uses `pdf-extract` (or just `pdftotext`/`pdfplumber` directly — the skill adds minimal value over the raw CLI tool). Stage 4 uses `schema-markup` as a reference. Stages 2-3 have no skill and are done by the agent. Calling this a "4-skill stack" would be dishonest — it's a 1-2 skill stack with 2 stages of raw LLM reasoning.

**Output quality:** For table-heavy spec sheets (motor specs, pump performance tables, material tables), the pipeline produces usable output with light cleanup. For prose-heavy specs (engineering specifications), the text extraction works but the structured field extraction depends entirely on how well the LLM parses the prose, which varies. For graphical content (performance curves, engineering drawings), the pipeline fails entirely — this data is lost. For template-style PDFs (blank data sheets), the pipeline extracts the field labels but not the values (because there are no values).

**Schema.org limitation:** The Product schema is designed for consumer e-commerce. B2B engineering specs need fields that don't exist in schema.org (insulation class, protection degree, NPSH, flow rate, head, operating temperature range). These would need custom `additionalProperty` entries or a custom schema extension. This isn't a blocker, but it means the "schema-marked-up" output won't trigger standard Google Product rich results — it would need custom search engine handling.

**The working direction holds with modification.** The opportunity is real — B2B manufacturers do publish specs as PDFs, and converting them to structured web content would improve their search visibility. But the "skill stack does most of the work" framing needs adjustment. The skill stack does the parsing (stage 1) and provides schema reference (stage 4). The LLM agent does the heavy lifting in the middle (stages 2-3), and that heavy lifting is where most of the per-product time and effort lives.

---

## 4. What Would Need More Research

### Full security review needed for:
- `pdf-toolkit-pro` — flagged suspicious by VirusTotal. Code review needed.
- `document-parser` — sends files to external Chinese API. Security review needed.
- `mineru-extract` — sends files to external MinerU API. Suspicious flagged.

### Deeper testing needed for:
- `pdfplumber` on a wider variety of B2B PDF layouts (chemical datasheets, electrical schematics, hydraulic specs)
- The LLM extraction quality on a larger sample (20-30 products) to estimate the human cleanup rate
- Whether the cleanup rate varies by industry vertical (pumps vs motors vs bearings vs valves)

### Pricing and market data the directed brief should request:
- **SaaS alternatives:** What do PIM systems (Akeneo, Salsify, Plytix) charge for structured data import? What do agencies charge for product page creation?
- **Manual effort baseline:** How long does it take a human to manually convert a product PDF to a structured web page? (This is the "time saved" number.)
- **Target vertical pricing:** What do mid-market B2B manufacturers typically pay for web development services? What's the per-product-page market rate?
- **Schema.org extensions:** Research whether Google supports any B2B-specific schema extensions (Manufacturing, IndustrialProduct, etc.) or whether custom additionalProperty is the only option.

### The "how much human cleanup" question:
This is the load-bearing number for the whole Stack Play. The exploratory pass suggests it varies by PDF type: ~2-5 minutes per product for clean table-heavy specs, ~10-15 minutes for prose-heavy or mixed-layout specs, ~20+ minutes for PDFs with heavy graphical content that can't be extracted. The directed brief should include a plan to test this systematically.

---

## 5. Blockers

- **No ClawHub skills for stages 2-3.** This is the biggest finding. The pipeline has a gap in the middle that no skill fills. The agent does it from raw reasoning.
- **`document-parser` requires an external API key** for a Chinese server (47.111.146.164:8088). I did not have credentials and did not test against production data. This skill could potentially fill stages 1-2 if the API works, but the security review is a prerequisite.
- **`mineru-extract` requires a MinerU API token.** I did not have credentials and did not test. This could potentially improve stage 1 (better layout/table extraction) but is an external dependency.
- **Graphical content in PDFs is a hard wall.** Performance curves, engineering drawings, and dimensioned diagrams cannot be extracted by text-based tools. The pipeline loses this data. For some B2B products (like pumps, where performance curves are critical specs), this is a significant loss.
- **The "4-skill stack" framing doesn't hold.** It's 1-2 skills + raw LLM reasoning. The post would need to reframe around "how much can the agent do with minimal tooling" rather than "here's a complete skill stack."
