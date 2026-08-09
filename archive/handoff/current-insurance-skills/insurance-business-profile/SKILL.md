---
name: insurance-business-profile
description: Builds a "what does this company actually do" business-profile writeup (HTML artifact) for Indian insurance companies — business model, revenue sources, product mix breakdown (with segment bars), distribution channels (bancassurance/agency/digital %), and key operational metrics. Use this whenever the user asks how an insurer "makes money", wants to understand its "business model", "products", "distribution", "product mix", or asks a general "tell me about" a named insurer for LIC, ICICI Prudential Life, HDFC Life, SBI Life, Axis Max Life, Star Health, Niva Bupa, ICICI Lombard, Medi Assist, or any other Indian insurer.
---

# Insurance Business Profile

Explains how a company actually operates and earns money — the qualitative complement to the
financial-metric skills. Read `references/design-system.md` for the `.seg-row`/`.seg-bar-wrap` segment
bar pattern and card layout; read `references/metrics-glossary.md` so the revenue-model explanation
uses consistent terminology with the rest of the skill family (e.g. always call TPA "not an insurer,
earns a service fee" rather than reinventing the phrasing). When pulling any qualitative or numeric
fact from the web, follow that file's **Source Hierarchy & Attribution** section: prefer the
company's own filings over aggregator sites, and flag any conflicting figures rather than silently
picking one.

## Step 1 — Gather qualitative + structural facts

Look for (web search if not supplied): promoter/JV structure, founding year, market position/rank,
MD & CEO name, distribution network size (branches/agents/bank partnerships), and product mix %
breakdown by APE or GWP. If a precise product-mix % isn't disclosed, say so rather than estimating a
false-precision number — an approximate range ("~40–45%") sourced from the company's own disclosure is
fine; an invented one is not.

## Step 2 — Structure the profile by category

**Life insurer profile covers**: promoter/JV, revenue pillars (new business premium, renewal premium,
group business, investment income), distribution mix (bancassurance vs agency vs digital, with %),
product mix by APE (ULIP / Non-Par savings / Protection / Annuity / PAR — as a segment-bar breakdown),
and any strategic pivot underway (e.g. shifting from ULIP-heavy to protection-led).

**Health (SAHI) profile covers**: business model (SAHI = health + personal accident only, cannot write
other lines), distribution mix (agents/brokers/bancassurance/digital %), product mix (retail vs group
vs personal accident), network hospital count, differentiators (claim settlement speed, NPS, etc.).

**General insurer profile covers**: lines of business (Motor/Health/Property/Crop/Liability), how
profit is generated (underwriting result + investment income — explain explicitly that Combined Ratio
>100% doesn't necessarily mean the company is unprofitable), distribution, investment portfolio mix.

**TPA profile covers**: explicitly state it is NOT an insurance company; explain the claims-processing
service-fee model, its client base (insurers/self-insured employers), any differentiating tech (AI
fraud detection, platform models), and market share of claims/premiums administered.

## Step 3 — Build the HTML

1. A `.grp-hdr` banner per company: name, promoter/ownership, founding year, one-line positioning.
2. `.g2` grid: left card = "Business Model" prose (1 paragraph, 4–6 sentences, dense with real numbers);
   right card = "Product Mix" or "Key Metrics" — segment bars (`.seg-row`) for product/distribution mix,
   or an `.m-row` list of operational metrics (persistency, network hospitals, agent counts, etc.) if a
   mix breakdown isn't the most relevant framing (e.g. for TPA, use Key Metrics not product mix).
3. For multiple companies, repeat the block per company, grouped under category section titles.

## Step 4 — Save and present

Save to `/mnt/user-data/outputs/<Company_or_Sector>_BusinessProfile.html`, call `present_files`. For a
single quick "how does X make money" question with no request for a saved artifact, a short prose
answer in chat (2–4 sentences) is often enough — don't force a full HTML file for a simple question.
