# Shared Design System — CB Research Artifacts

Every HTML artifact this skill produces should look like it came from the same product family, whatever
the sector. That consistency is the point: a reader who has seen one dashboard should recognise the
second one instantly, and should be able to trust that a green number means the same thing everywhere.

This file is **sector-agnostic**. Company colours, category tags, and metric-specific chart reference
lines live in the loaded sector file, because those genuinely differ by domain. Everything here applies
to all of them.

---

## 1. Page skeleton

One self-contained HTML file: `<style>` in `<head>`, all JS in a single `<script>` before `</body>`.
No framework — vanilla JS, plus Chart.js from CDN only when charts are needed:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

Fonts (Google Fonts CDN): `Playfair Display` (700/900) headings, `IBM Plex Mono` (400/500) numbers,
`Inter` (300–700) body.

Numbers are set in mono deliberately — figures line up across rows and become scannable in a way
proportional type prevents.

## 2. CSS root variables

Always define these. Extend per-company colours from the sector file's palette.

```css
:root{
  --bg:#f7f6f2;--surface:#fff;--surface2:#f2f0eb;--border:#e2ddd5;
  --text:#181511;--muted:#6e6860;
  --pos:#166534;--neg:#dc2626;--warn:#ea580c;
  --gold:#b8911e;--gold-soft:#fdf5e0;
  --star:#7c3aed;--star-soft:#f5f3ff; /* "AI assist / accent" colour */
  --shadow:0 1px 8px rgba(24,21,17,.07);--shadow-md:0 4px 20px rgba(24,21,17,.10);
  --radius:10px;
}
```

## 3. Company colour assignment

The sector file owns the actual palette table. The rule that applies everywhere: **a company keeps the
same colour across every artifact**, so a reader learns to recognise it by hue. If a company isn't in the
sector file's table, pick an unused, visually distinct hue plus a ~10% soft tint, and add it to that
sector file so the next report reuses it rather than re-rolling.

Set `--co-color` inline per card (`style="--co-color:#be123c"`).

Category accent bands — grouping companies by sub-type within a sector (e.g. Life vs Health vs General) —
are also sector-owned, since the categories themselves are sector concepts. The *pattern* is constant:
soft background, 4px left border in the category's main colour, matching text colour, and a small
uppercase tag pill.

## 4. Core reusable classes

Include the ones the artifact actually uses; trim the rest.

```css
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);font-size:13.5px;line-height:1.55;}

/* header */
.hdr{background:#181511;color:#fff;padding:0 40px;display:flex;align-items:stretch;justify-content:space-between;min-height:72px;flex-wrap:wrap;}
.hdr-left h1{font-family:'Playfair Display',serif;font-size:1.5rem;color:#fff;}
.hdr-left .sub{font-size:11px;font-weight:500;color:rgba(255,255,255,.45);letter-spacing:.12em;text-transform:uppercase;margin-top:4px;}
.hdr-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:14px 0;}
.chip{padding:4px 11px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;}

/* tabbed layout */
.tab-nav{background:var(--surface);border-bottom:2px solid var(--border);display:flex;padding:0 40px;overflow-x:auto;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(24,21,17,.06);}
.tab-btn{padding:14px 15px 12px;font-size:12px;font-weight:600;color:var(--muted);background:none;border:none;border-bottom:3px solid transparent;cursor:pointer;white-space:nowrap;}
.tab-btn.active{color:var(--text);border-bottom-color:var(--star);font-weight:700;}
.panel{display:none;}.panel.active{display:block;}

/* layout */
.main{padding:26px 40px 48px;max-width:1460px;margin:0 auto;}
.sec-hdr{font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid var(--border);display:flex;align-items:center;gap:12px;flex-wrap:wrap;}
.sec-note{font-size:11px;color:var(--muted);font-weight:400;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;}

/* group header band — one company or sub-group's banner within a section */
.grp-hdr{background:var(--surface2);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:12px 16px;margin:18px 0 14px;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;}
.grp-hdr h3{font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;}
.grp-hdr .grp-meta{font-size:11px;color:var(--muted);}

/* cards */
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px 22px;box-shadow:var(--shadow);}
.card-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:14px;}
.co-card{background:var(--surface);border:1.5px solid var(--border);border-radius:var(--radius);padding:18px 20px;box-shadow:var(--shadow-md);position:relative;overflow:hidden;}
.co-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--co-color,#181511);}
.co-name{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;}
.co-seg{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-weight:600;margin-bottom:10px;}

/* metric rows */
.m-row{display:flex;justify-content:space-between;margin-bottom:6px;}
.m-lbl{font-size:11.5px;color:var(--muted);}
.m-val{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;}

/* badges */
.badge{font-size:10px;padding:2px 8px;border-radius:4px;font-weight:700;font-family:'IBM Plex Mono',monospace;}
.badge-row{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;}
.b-buy,.b-pos{background:#dcfce7;color:#15803d;}.b-hold{background:#fef9c3;color:#a16207;}
.b-sell,.b-neg{background:#fee2e2;color:#b91c1c;}.b-watch{background:#fff7ed;color:#c2410c;}.b-info{background:#dbeafe;color:#1d4ed8;}

/* KPI strip */
.kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:22px;}
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:14px 16px;box-shadow:var(--shadow);border-left:4px solid var(--co-color,#181511);}
.kpi .kl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);margin-bottom:5px;}
.kpi .kv{font-size:1rem;font-weight:800;font-family:'IBM Plex Mono',monospace;}
.kpi .kc{font-size:10px;font-weight:700;margin-top:2px;}
.pos{color:var(--pos);}.neg{color:var(--neg);}.warn{color:var(--warn);}

/* tables */
table{width:100%;border-collapse:collapse;background:var(--surface);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);}
th{background:#181511;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:10.5px;font-weight:500;padding:11px 13px;text-align:left;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;}
td{padding:10px 13px;border-bottom:1px solid var(--border);font-size:12.5px;white-space:nowrap;}
tr:last-child td{border-bottom:none;}tr:nth-child(even) td{background:#fafaf8;}
td.num{font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tpos{color:var(--pos);font-weight:700;font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tneg{color:var(--neg);font-weight:700;font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tb{font-weight:700;}
.tbl-wrap{overflow-x:auto;} /* wrap every table so wide ones scroll instead of breaking the page */

/* SWOT */
.co-hdr-swot{display:flex;align-items:center;gap:10px;margin:16px 0 8px;padding-bottom:6px;border-bottom:2px solid var(--co-color,var(--border));}
.co-hdr-swot .co-badge{background:var(--co-color,#181511);color:#fff;font-size:10px;font-weight:800;padding:3px 9px;border-radius:4px;letter-spacing:.06em;text-transform:uppercase;}
.swot-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1.5px solid var(--border);border-radius:var(--radius);overflow:hidden;}
.swot-cell{padding:13px 15px;}
.swot-s{background:#e8f5ee;}.swot-w{background:#fbeee8;}.swot-o{background:#f0edf8;}.swot-t{background:var(--gold-soft);}
.swot-lbl{font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.12em;margin-bottom:5px;}
.sl{color:#166534;}.wl{color:#dc2626;}.ol{color:#7c3aed;}.tl{color:var(--gold);}
.swot-ul{list-style:none;font-size:11px;line-height:1.65;}
.swot-ul li::before{content:"• ";color:var(--muted);}

/* moats */
.moat-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.moat-title{font-size:12.5px;font-weight:700;margin-bottom:5px;}
.moat-body{font-size:11px;color:var(--muted);line-height:1.55;}
.moat-tag{display:inline-block;margin-top:8px;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;text-transform:uppercase;}

/* segment / mix bars */
.seg-row{display:grid;grid-template-columns:112px 1fr 52px;align-items:center;gap:10px;margin-bottom:7px;font-size:11.5px;}
.seg-lbl{color:var(--muted);}
.seg-bar-wrap{background:var(--surface2);border-radius:4px;height:14px;overflow:hidden;}
.seg-bar{height:100%;border-radius:4px;background:var(--co-color,#181511);}
.seg-val{font-family:'IBM Plex Mono',monospace;font-weight:600;text-align:right;}

/* scorecard */
.score-row{display:grid;grid-template-columns:1fr repeat(auto-fit,minmax(70px,1fr));align-items:center;gap:8px;padding:9px 0;border-bottom:1px solid var(--border);font-size:11.5px;}
.score-row:last-child{border-bottom:none;}
.score-pill{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:700;text-align:center;padding:3px 0;border-radius:4px;background:var(--surface2);}

/* chart metric switcher */
.metric-sel{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px;}
.metric-sel button{font-size:11px;font-weight:600;padding:5px 12px;border-radius:16px;border:1px solid var(--border);background:var(--surface);color:var(--muted);cursor:pointer;}
.metric-sel button.on{background:var(--star);border-color:var(--star);color:#fff;}

/* analyst-ratings component — recurs across the corpus */
.analyst-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;}
.analyst-card{background:var(--surface);border:1px solid var(--border);border-left:4px solid var(--co-color,#181511);border-radius:var(--radius);padding:13px 15px;box-shadow:var(--shadow);}
.analyst-firm{font-size:11.5px;font-weight:700;margin-bottom:3px;}
.analyst-rating{font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px;text-transform:uppercase;}
.analyst-tp{font-family:'IBM Plex Mono',monospace;font-size:12.5px;font-weight:700;margin-top:5px;}
.analyst-date{font-size:10px;color:var(--muted);margin-top:3px;}

/* chart containers */
.chart-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.chart-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);margin-bottom:10px;}
.chart-wrap{position:relative;height:300px;}

/* callout boxes */
.info-box{background:#eff6ff;border:1px solid #bfdbfe;border-left:4px solid #1d4ed8;border-radius:8px;padding:13px 15px;font-size:11.5px;line-height:1.7;}
.warn-box{background:#fff7ed;border:1px solid #fdba74;border-left:4px solid var(--warn);border-radius:8px;padding:13px 15px;font-size:11.5px;line-height:1.7;}

/* small inline labels */
.pill{display:inline-block;padding:2px 10px;border-radius:14px;font-size:10px;font-weight:700;background:var(--surface2);border:1px solid var(--border);}
.tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;background:var(--surface2);color:var(--muted);}

/* embedded Q&A panel */
.qa-q{font-size:11.5px;font-weight:700;padding:8px 0 4px;}
.qa-a{font-size:11.5px;color:var(--muted);line-height:1.65;padding-bottom:8px;border-bottom:1px dashed var(--border);}

/* watermark / attribution */
.wm{font-size:10px;color:var(--muted);letter-spacing:.08em;text-transform:uppercase;}

/* notes & footer */
.fnote{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:16px 18px;margin-top:20px;font-size:11px;color:var(--muted);line-height:1.7;}
.footer{text-align:center;font-size:11px;color:var(--muted);padding:20px 40px;border-top:1px solid var(--border);margin-top:20px;background:var(--surface);}
```

## 5. Two layouts — pick deliberately

Both are first-class. The choice follows the shape of the content, not habit.

**Tabbed** — use when there are 6+ sections, or several companies each needing the same section set.
Sticky `.tab-nav`, one `.panel` per tab with `id="tab-<name>"`, first one `active`.

```html
<nav class="tab-nav">
  <button class="tab-btn active" onclick="showTab('dashboard',this)">📊 Dashboard</button>
  <button class="tab-btn" onclick="showTab('financials',this)">💰 Financials</button>
</nav>
<script>
function showTab(id, btn){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById('tab-'+id).classList.add('active');
  btn.classList.add('active');
  if(id==='charts') initCharts();   // lazy-init: canvases size wrongly while hidden
}
</script>
```

**Single-page scroll** — use for a focused single-company read or a narrative argument, where forcing a
reader to hunt through tabs costs more than it saves. Sections run in sequence under `.sec-hdr` headings.
A short jump-link row at the top is a good substitute for tabs.

Emoji-prefix section labels lightly (📊 💰 📈 🏢 🔍 🎯 🛡️ 🏆 🎓) — a readability aid for scanning, not a
requirement.

## 6. Chart.js patterns

- **Cross-entity comparison** → vertical bar, one bar per company, coloured from the sector palette,
  value labels drawn above each bar via an `afterDatasetsDraw` plugin. Label the bars rather than relying
  on hover tooltips — these render inside artifacts where hover may not be available, and an unreadable
  chart defeats the purpose.
- **Trend over time** → grouped bar or line, x-axis = periods, one dataset per company. Keep the legend.
- **Single-dataset bar** → disable the legend (`plugins:{legend:{display:false}}`); it says nothing.
- **Reference lines** — the pattern is shared, the *values* are sector-specific and come from the sector
  file's "chart reference lines" table. Draw with an `afterDraw` plugin, dashed
  (`ctx.setLineDash([6,4])`), labelled with what the line means. A threshold line without a label is
  just a mystery stripe. Where a metric has a natural "good/bad" side, tint bars accordingly.
- **Metric switcher** — keep a small `DATA` object keyed by metric name; the handler swaps
  `chart.data.datasets[0].data` and calls `chart.update()` rather than rebuilding the chart.
- Wrap canvases in `.card` with a `.card-lbl` title, and put **one sentence of plain-English takeaway**
  under each chart. A chart with no stated takeaway pushes the analysis back onto the reader.

## 7. AI assist panel

An embedded Q&A panel is the house default on full multi-section reports — it appears in the large
majority of published reports, so treat its absence as the exception rather than its presence as a
special request. Omit it for narrow single-slice outputs where it would be noise.

Render it as a clearly-labelled optional panel using the `--star` accent. Anything embedded in its
prompt as "known facts" obeys exactly the same no-fabrication discipline as the rest of the artifact: if
a figure isn't sourced, it doesn't go in. Do not wire up external API calls unless explicitly asked for
a live interactive feature.

## 8. Footnotes and caveats — do not skip these

Whenever a figure carries a caveat the company itself flagged — a one-off tax credit, an MTM swing,
consolidated vs standalone basis, an exceptional item, a change in reporting standard — put it in a
`.fnote` under the table. This is the single most-skipped element in past reports and the one most
likely to mislead a reader who trusts the number at face value. A table with an honest footnote is worth
more than a clean-looking table that quietly misleads.

## 9. Footer

Every artifact ends with a compact footer carrying: the data as-of date, an explicit `Source:` line (see
the source-hierarchy reference for the required format — source **plus date**), and the
research/educational disclaimer stating this is not investment advice.

## Table row emphasis and small components

These recur across generated reports and were previously improvised per file, which is how two reports
end up with the same class doing different things. `.hl` in particular was applied to the Revenue,
EBITDA and PAT rows of a P&L and left undefined, so the rows meant to stand out rendered identically to
every other row.

```css
/* highlight row — the subtotal lines of a financial table (Revenue, EBITDA, PAT) */
.hl{background:var(--surface2);}
.hl td{font-weight:700;}

/* section sub-heading, below a tab title */
.sub-hdr{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;margin:26px 0 12px;}
.hdr-em{font-size:1.7rem;}

/* the "what to take away" note under a table or chart */
.take{font-size:11px;color:var(--muted);line-height:1.6;margin-top:10px;padding-top:9px;
      border-top:1px dashed var(--border);}

/* callout boxes */
.ok-box{background:#f0fdf4;border:1px solid #bbf7d0;border-left:4px solid var(--pos);
        border-radius:var(--radius);padding:14px 16px;font-size:12px;}
.chip-warn{background:rgba(255,255,255,.08);color:#fbbf24;border:1px solid rgba(251,191,36,.35);
           border-radius:999px;padding:3px 10px;font-size:10px;font-weight:700;}

/* horizontal score bar — CB Rating components and any 0-100 scale */
.score-bar-wrap{background:var(--surface2);border-radius:4px;height:12px;overflow:hidden;}
.score-bar{height:100%;border-radius:4px;background:var(--accent);}

/* masthead strip above the report header */
.topbar{background:#0b0a08;color:rgba(255,255,255,.5);font-size:10px;letter-spacing:.14em;
        text-transform:uppercase;padding:6px 0;text-align:center;}
```

**`.score-bar` takes the sector's accent colour**, not a company colour — it measures a component score,
not a company. Where a report compares companies on the same bar, colour by company from the sector
palette instead.
