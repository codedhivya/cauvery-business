# Insurance Dashboard — Shared Design System

Use this design system for ALL insurance-sector HTML artifacts so that outputs from different
skills look like one consistent product family (same look CB Research / Cauvery Business dashboards use).

## 1. Page Skeleton

Every HTML output is a single self-contained file: `<style>` in `<head>`, all JS in one `<script>`
before `</body>`. No external JS framework — vanilla JS + Chart.js CDN only when charts are needed:
`<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>`

Fonts (Google Fonts CDN):
`Playfair Display` (700/900) for headings, `IBM Plex Mono` (400/500) for numbers, `Inter` (300–700) for body text.

## 2. CSS Root Variables (always define these; extend the company color list as needed)

```css
:root{
  --bg:#f7f6f2;--surface:#fff;--surface2:#f2f0eb;--border:#e2ddd5;
  --text:#181511;--muted:#6e6860;
  --pos:#166534;--neg:#dc2626;--warn:#ea580c;
  --gold:#b8911e;--gold-soft:#fdf5e0;
  --star:#7c3aed;--star-soft:#f5f3ff; /* used as the "AI assist / accent" color */
  --shadow:0 1px 8px rgba(24,21,17,.07);--shadow-md:0 4px 20px rgba(24,21,17,.10);
  --radius:10px;
}
```

## 3. Company Color Palette (assign a distinct pair `--code` / `--code-soft` per company)

Reuse these when the company reappears across dashboards so a reader learns to recognize a company
by its color. If a new company isn't listed, pick an unused, visually distinct hue and soft tint.

| Company | Main | Soft (10% tint bg) |
|---|---|---|
| LIC | #1d4ed8 | #eff6ff |
| ICICI Prudential Life | #c84b2f | #fef3f0 |
| Axis Max Life | #166534 | #f0fdf4 |
| HDFC Life | #be123c | #fff1f2 |
| SBI Life | #1e3a5f | #eff6ff |
| Star Health | #7c3aed | #f5f3ff |
| Niva Bupa | #d97706 | #fffbeb |
| ICICI Lombard (General) | #7f1d1d | #fef2f2 |
| Medi Assist (TPA) | #0e7490 | #ecfeff |

Category accent bands (for section headers that group companies by type):
- Life Insurance: bg `#eff6ff`, border-left `#1d4ed8`, text `#1d4ed8`, tag `.cat-life`
- Health Insurance (SAHI): bg `#f0fdf4`, border-left `#15803d`, text `#15803d`, tag `.cat-health`
- General Insurance: bg `#fef2f2`, border-left `#7f1d1d`, text `#7f1d1d`, tag `.cat-general`
- TPA: bg `#fdf2f8`, border-left `#9d174d`, text `#9d174d`, tag `.cat-tpa`

## 4. Core Reusable CSS Classes

Always include these class definitions (trim ones not needed for the specific output):

```css
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);font-size:13.5px;line-height:1.55;}
.hdr{background:#181511;color:#fff;padding:0 40px;display:flex;align-items:stretch;justify-content:space-between;min-height:72px;flex-wrap:wrap;}
.hdr-left h1{font-family:'Playfair Display',serif;font-size:1.5rem;color:#fff;}
.hdr-left .sub{font-size:11px;font-weight:500;color:rgba(255,255,255,.45);letter-spacing:.12em;text-transform:uppercase;margin-top:4px;}
.chip{padding:4px 11px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;}
.tab-nav{background:var(--surface);border-bottom:2px solid var(--border);display:flex;padding:0 40px;overflow-x:auto;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(24,21,17,.06);}
.tab-btn{padding:14px 15px 12px;font-size:12px;font-weight:600;color:var(--muted);background:none;border:none;border-bottom:3px solid transparent;cursor:pointer;white-space:nowrap;}
.tab-btn.active{color:var(--text);border-bottom-color:var(--star);font-weight:700;}
.main{padding:26px 40px 48px;max-width:1460px;margin:0 auto;}
.panel{display:none;}.panel.active{display:block;}
.sec-hdr{font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;margin-bottom:18px;padding-bottom:10px;border-bottom:2px solid var(--border);display:flex;align-items:center;gap:12px;flex-wrap:wrap;}
.sec-note{font-size:11px;color:var(--muted);font-weight:400;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px 22px;box-shadow:var(--shadow);}
.card-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:14px;}
.co-card{background:var(--surface);border:1.5px solid var(--border);border-radius:var(--radius);padding:18px 20px;box-shadow:var(--shadow-md);position:relative;overflow:hidden;}
.co-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--co-color,#181511);}
.co-name{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;}
.co-seg{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-weight:600;margin-bottom:10px;}
.m-row{display:flex;justify-content:space-between;margin-bottom:6px;}
.m-lbl{font-size:11.5px;color:var(--muted);}
.m-val{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;}
.badge{font-size:10px;padding:2px 8px;border-radius:4px;font-weight:700;font-family:'IBM Plex Mono',monospace;}
.b-buy,.b-pos{background:#dcfce7;color:#15803d;}.b-hold{background:#fef9c3;color:#a16207;}
.b-sell,.b-neg{background:#fee2e2;color:#b91c1c;}.b-watch{background:#fff7ed;color:#c2410c;}.b-info{background:#dbeafe;color:#1d4ed8;}
.kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-bottom:22px;}
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:14px 16px;box-shadow:var(--shadow);border-left:4px solid var(--co-color,#181511);}
.kpi .kl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);margin-bottom:5px;}
.kpi .kv{font-size:1rem;font-weight:800;font-family:'IBM Plex Mono',monospace;}
.kpi .kc{font-size:10px;font-weight:700;margin-top:2px;}
.pos{color:var(--pos);}.neg{color:var(--neg);}.warn{color:var(--warn);}
table{width:100%;border-collapse:collapse;background:var(--surface);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);}
th{background:#181511;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:10.5px;font-weight:500;padding:11px 13px;text-align:left;letter-spacing:.05em;text-transform:uppercase;white-space:nowrap;}
td{padding:10px 13px;border-bottom:1px solid var(--border);font-size:12.5px;white-space:nowrap;}
tr:last-child td{border-bottom:none;}tr:nth-child(even) td{background:#fafaf8;}
td.num{font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tpos{color:var(--pos);font-weight:700;font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tneg{color:var(--neg);font-weight:700;font-family:'IBM Plex Mono',monospace;text-align:right;}
td.tb{font-weight:700;}
.swot-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1.5px solid var(--border);border-radius:var(--radius);overflow:hidden;}
.swot-cell{padding:13px 15px;}
.swot-s{background:#e8f5ee;}.swot-w{background:#fbeee8;}.swot-o{background:#f0edf8;}.swot-t{background:var(--gold-soft);}
.swot-lbl{font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.12em;margin-bottom:5px;}
.sl{color:#166534;}.wl{color:#dc2626;}.ol{color:#7c3aed;}.tl{color:var(--gold);}
.swot-ul{list-style:none;font-size:11px;line-height:1.65;}
.swot-ul li::before{content:"• ";color:var(--muted);}
.moat-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow);}
.moat-title{font-size:12.5px;font-weight:700;margin-bottom:5px;}
.moat-body{font-size:11px;color:var(--muted);line-height:1.55;}
.moat-tag{display:inline-block;margin-top:8px;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:700;text-transform:uppercase;}
.cat-tag{display:inline-block;padding:2px 10px;border-radius:12px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.08em;}
.cat-life{background:#dbeafe;color:#1d4ed8;}.cat-health{background:#dcfce7;color:#15803d;}
.cat-tpa{background:#fce7f3;color:#9d174d;}.cat-general{background:#fee2e2;color:#7f1d1d;}
.cat-section-title{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;padding:10px 16px;border-radius:8px;margin:20px 0 14px;display:flex;align-items:center;gap:10px;}
.fnote{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:16px 18px;margin-top:20px;font-size:11px;color:var(--muted);line-height:1.7;}
.footer{text-align:center;font-size:11px;color:var(--muted);padding:20px 40px;border-top:1px solid var(--border);margin-top:20px;background:var(--surface);}
```

Set `--co-color` inline per card/kpi (`style="--co-color:#be123c"`) using the company's main color from §3.

## 5. Tab Navigation Pattern (for multi-section dashboards)

```html
<nav class="tab-nav">
  <button class="tab-btn active" onclick="showTab('dashboard',this)">📊 Dashboard</button>
  <button class="tab-btn" onclick="showTab('financials',this)">💰 Financials</button>
  ...
</nav>
<script>
function showTab(id, btn){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById('tab-'+id).classList.add('active');
  btn.classList.add('active');
}
</script>
```

## 6. Chart.js Patterns

- **Bar comparison across companies**: `type:'bar'`, one dataset, `backgroundColor` = array of each
  company's main color, `borderRadius:6`, value labels drawn via an `afterDatasetsDraw` plugin.
- **Combined/CISR Ratio chart**: bar chart + a horizontal dashed red "100% Breakeven" reference line
  drawn with an `afterDraw` plugin (`ctx.setLineDash([6,4])`, stroke `#dc2626`).
- **Solvency Ratio chart**: horizontal bar (`indexAxis:'y'`) + dashed reference line at IRDAI minimum 150%.
- Always disable the legend for single-dataset bar charts (`plugins:{legend:{display:false}}`) and label
  bars with actual values so the chart is readable without hovering (this renders inside a Claude
  artifact where users may not get JS tooltips reliably — value labels are safer than relying on tooltips alone).

## 7. Footer & Disclaimer

Every output should end with a compact footer stating: data as-of date, "For research/educational
purposes only — not investment advice", and that figures come from company exchange filings /
investor presentations / earnings calls (do not fabricate a specific source if you don't have one —
say "publicly available company disclosures").

## 8. Output & Delivery

- Save the HTML file under `/mnt/user-data/outputs/` with a clear filename, e.g.
  `HDFCLife_Dashboard_Q1FY27.html`.
- Call `present_files` so the person can open it — HTML renders as an interactive artifact.
- If the person asks for something short/conversational instead of a saved artifact, just answer in
  chat using the same numbers — don't force an HTML file for a one-line question.
