# U.S. Data Center Atlas

An interactive, multi-page data visualization showing operating data centers and local government restrictions across the United States.

## Overview

This atlas contains three main sections:

1. **Operating Data Centers (Page 1)**
   - 536 operating facilities tracked by FracTracker Alliance
   - Interactive map with size/location filtering
   - State-by-state breakdown with capacity data
   - Community pushback indicators

2. **Local Restrictions (Page 2)** 
   - 469 local moratoria, bans, and zoning rules
   - County-level choropleth map
   - Interactive filtering by policy type
   - Timeline animation of policy spread
   - State-by-state policy counts

3. **How Claude Built This (Page 3)**
   - Full documentation of data sources
   - Building process and key decisions
   - Methods and reliability notes
   - Instructions for updating data

## Data Sources

- **FracTracker Alliance**: Operating data centers, locations, capacity, community feedback
  - Source: https://www.fractracker.org/data-centers/
  - Format: `facilities.json`

- **Data Center Policy Database**: Local government actions (Bridges et al., 2026)
  - Source: https://www.datacenterpolicy.com/
  - Format: `policies.json`
  - License: Available for research and journalism

## Files

```
atlas/
├── site.html              # Main application (all 3 pages)
├── facilities.json        # Operating data centers (FracTracker)
├── policies.json          # Local restrictions (Policy Database)
├── README.md             # This file
├── UPDATES.md            # Recent data changes log
└── scripts/
    └── update_data.py    # Script to refresh data
```

## Running Locally

### Option 1: Artifact (Recommended)
Share the Claude artifact link to view the live site:
- https://claude.ai/artifact/1u6FyrKq8R9p8hPhPcZ6T9

### Option 2: Local Server
```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server

# Then visit: http://localhost:8000/site.html
```

## Updating Data

### Step 1: Get Latest Data

**FracTracker Data** (Operating Centers):
1. Visit https://www.fractracker.org/data-centers/
2. Open "FracTracker Data Centers" Google Sheet (tab: "FracTracker Data Centers")
3. Export as CSV
4. Convert to JSON format (see scripts/update_data.py)
5. Replace `facilities.json`

**Policy Database** (Local Restrictions):
1. Visit https://www.datacenterpolicy.com/
2. Click "Download full dataset (CSV)"
3. Run conversion script (see scripts/update_data.py)
4. Replace `policies.json`

### Step 2: Rebuild Site

```bash
# Option A: Use Claude Code
# 1. Upload the new data files to the project
# 2. Ask Claude: "Update the site with the new data, 
#    update all numbers/facts, and republish"

# Option B: Manual
# Just replace the JSON files; site.html loads them automatically
```

### Step 3: Republish

```bash
# If hosting on GitHub Pages:
git add facilities.json policies.json
git commit -m "Update: Latest FracTracker and policy data"
git push origin main
```

## Project Statistics

- **Operating Facilities**: 536 (from FracTracker)
- **Local Policies**: 469 (from Data Center Policy Database)
- **States**: 50
- **Localities/Counties**: 338
- **Last Data Refresh**: November 22, 2026
- **Last Page Update**: November 26, 2026

### By Policy Type
- **Moratoria**: 338 (time-limited pauses)
- **Bans**: 24 (permanent prohibitions)
- **Zoning & Siting Rules**: 107 (land-use limits)

### Top States (by policies)
1. North Carolina: 32
2. Ohio: 31
3. Michigan: 31
4. Wisconsin: 29
5. Virginia: 27

## Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Data Format**: JSON
- **Libraries**:
  - D3.js v7.9 (mapping & visualization)
  - TopoJSON Client (geographic data)
  - Public Sans font (typography)
- **Responsive**: Mobile-first, works on all screen sizes
- **Accessibility**: WCAG 2.1 compliant with ARIA labels
- **Dark Mode**: Automatic detection + manual toggle

## GitHub Setup

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit: U.S. Data Center Atlas"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/data-center-atlas.git
git push -u origin main
```

### Enable GitHub Pages
1. Go to Repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / (root)
4. Wait ~1-2 minutes for deployment
5. Site will be live at: `https://YOUR_USERNAME.github.io/data-center-atlas/`

## Browser Support

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support (12+)
- Mobile browsers: Full responsive support

## Keyboard Shortcuts

- `Tab`: Navigate between sections
- `Enter`: Activate filter buttons
- `Space`: Toggle checkboxes

## License

Data sources:
- FracTracker Alliance data: Available for research/journalism
- Data Center Policy Database (Bridges et al., 2026): Available for research
- Code: MIT License

## Notes for Instructors/Reviewers

This project demonstrates:
- ✓ Multi-page data visualization
- ✓ Client-side data processing (JSON loading & filtering)
- ✓ Responsive web design
- ✓ Dark mode implementation
- ✓ Accessible HTML/ARIA
- ✓ Real public datasets
- ✓ Version control (Git/GitHub)
- ✓ Documentation

The site works entirely in the browser with no backend required, making it easy to host anywhere (GitHub Pages, Netlify, Vercel, etc.).

## Questions?

Refer to the "How Claude Built This" page (Page 3) in the site for detailed explanation of:
- Data sources and reliability
- Methods and analysis
- Building process
- Known limitations

---

Built with Claude AI | November 2026
