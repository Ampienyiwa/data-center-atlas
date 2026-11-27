# Data Update Guide

This document explains how to refresh your U.S. Data Center Atlas with the latest data.

## Overview

Your site reads two JSON files:
- `facilities.json` - Operating data centers (from FracTracker Alliance)
- `policies.json` - Local restrictions (from Data Center Policy Database)

Both are updated independently. The site automatically reads and displays them without code changes.

## Update Schedule

Recommended update frequency:
- **FracTracker Data**: Monthly (operates on rolling basis)
- **Policy Database**: Weekly (new policies pass frequently)

## Getting FracTracker Operating Data

### Option A: Download CSV → Convert to JSON (Best)

1. **Get the data:**
   - Visit: https://www.fractracker.org/data-centers/
   - Click "Data Centers Identified by FracTracker Alliance"
   - Opens Google Sheet: "FracTracker Data Centers"
   - Tab: "FracTracker Data Centers"

2. **Export to CSV:**
   - Click top-left menu (hamburger icon)
   - Select "Download" → "Comma-separated values (.csv)"
   - Save as `fractracker_data.csv`

3. **Convert to JSON format:**
   ```python
   import csv
   import json
   
   facilities = []
   with open('fractracker_data.csv', 'r', encoding='utf-8') as f:
       reader = csv.DictReader(f)
       for row in reader:
           # Only keep Operating status
           if row.get('status', '').strip() != 'Operating':
               continue
           
           facilities.append({
               'id': int(row.get('id', 0)),
               'name': row.get('name', ''),
               'operator': row.get('operator', ''),
               'state': row.get('state', ''),
               'locality': row.get('locality', ''),
               'coordinates': [
                   float(row.get('longitude', 0)),
                   float(row.get('latitude', 0))
               ],
               'size_class': row.get('size_class', ''),
               'mw': float(row.get('mw', 0)) if row.get('mw', '').isdigit() else None,
               'mw_range': row.get('mw_range', ''),
               'community_pushback': row.get('community_pushback', '').lower() == 'yes',
               'location_confidence': row.get('location_confidence', ''),
           })
   
   with open('facilities.json', 'w', encoding='utf-8') as f:
       json.dump(facilities, f, indent=2)
   
   print(f'Converted {len(facilities)} operating facilities')
   ```

4. **Replace `facilities.json`** in your atlas folder

### Option B: Use Claude Code (Easiest)

1. Upload the CSV file to Claude Code
2. Ask: "Convert this FracTracker CSV to JSON format with this structure: {id, name, operator, state, locality, coordinates, size_class, mw, mw_range, community_pushback, location_confidence}"
3. Claude will generate the JSON
4. Download and replace `facilities.json`

## Getting Local Policy Data

### Step 1: Download from Policy Database

1. Visit: https://www.datacenterpolicy.com/
2. Click: **"Download full dataset (CSV)"**
3. Browser downloads `policies.csv` (or similar)

### Step 2: Filter for Local Policies

The CSV includes federal bills. We only want local actions:

```python
import csv
import json

policies = []
with open('policies.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Only keep local level and Passed/Signed status
        if row.get('level_of_government', '').strip() != 'Local':
            continue
        if row.get('status', '').strip() not in ['Passed', 'Signed/Enacted']:
            continue
        
        # Determine policy type
        policy_type = 'Zoning & siting rules'
        if 'moratorium' in row.get('name', '').lower():
            policy_type = 'Moratorium'
        elif 'ban' in row.get('name', '').lower():
            policy_type = 'Ban'
        
        policies.append({
            'id': int(row.get('id', 0)),
            'locality': row.get('locality', ''),
            'state': row.get('state', ''),
            'name': row.get('name', ''),
            'type': policy_type,
            'date': row.get('last_action_date', ''),
            'end': row.get('end_date_moratorium', '') if policy_type == 'Moratorium' else None,
            'description': row.get('description', '')[:300],
            'url': row.get('url', ''),
            'status': row.get('status', ''),
            'fips': [],
        })

with open('policies.json', 'w', encoding='utf-8') as f:
    json.dump(policies, f, indent=2)

print(f'Converted {len(policies)} local policies')
```

### Step 3: Replace `policies.json` in your atlas folder

## Verifying Updates

After updating either JSON file:

1. **Local Testing:**
   ```powershell
   # Start a local server
   python -m http.server 8000
   
   # Open browser
   start http://localhost:8000/site.html
   
   # Check the page loads and shows new data
   ```

2. **Publish Updated Site:**
   - Option A: Push to GitHub (auto-updates at GitHub Pages URL)
   - Option B: Republish Claude Artifact with new JSON files

## Checking Data Quality

After updating, verify:

```
✓ All rows have required fields (name, state, locality, etc.)
✓ No duplicate IDs
✓ Dates are in YYYY-MM-DD format
✓ Coordinates are valid (longitude -180 to 180, latitude -90 to 90)
✓ Capacity numbers are positive
✓ State abbreviations are 2 letters
```

## Creating an Update Log

Create a file `UPDATES.md` to track changes:

```markdown
# Update Log

## 2026-11-26
- Updated FracTracker facilities: 536 operating data centers
- Updated Policy Database: 469 local policies
- **New moratoria**: 12 (highest in October)
- **New bans**: 2
- **New zoning rules**: 15
- States with most activity: NC (5), OH (4), TX (3)

## 2026-11-15
- Policy database update: 440 policies → 457 policies
- FracTracker: stable at 536 facilities

## 2026-11-01
- Initial dataset creation
- 469 local policies from Policy Database
- 536 operating facilities from FracTracker
```

## Automation (Optional)

You can automate updates with a scheduled script:

```python
# daily_update.py
import subprocess
import json
from datetime import datetime

# Step 1: Download latest data
print(f"[{datetime.now()}] Downloading latest data...")
subprocess.run(['wget', 'https://...', '-O', 'fractracker.csv'])

# Step 2: Convert to JSON
# (use conversion code from above)

# Step 3: Commit and push if changed
subprocess.run(['git', 'add', 'facilities.json', 'policies.json'])
subprocess.run(['git', 'commit', '-m', f'Auto-update: {datetime.now().date()}'])
subprocess.run(['git', 'push'])

print("✓ Update complete")
```

Then schedule with Windows Task Scheduler, cron, or GitHub Actions.

## GitHub Actions (CI/CD)

Create `.github/workflows/update.yml` to auto-update weekly:

```yaml
name: Weekly Data Update

on:
  schedule:
    - cron: '0 9 * * 0'  # Every Sunday at 9 AM UTC

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Download and convert data
        run: |
          python download_data.py
      - name: Commit and push
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
          git add facilities.json policies.json
          git commit -m "Auto-update: $(date)"
          git push
```

## Troubleshooting

**"Columns don't match"**
- FracTracker sheet changes columns sometimes
- Check the actual columns in the sheet
- Adjust the conversion script

**"Site shows old data"**
- Clear browser cache (Ctrl+Shift+Delete)
- If GitHub Pages: wait 5 minutes for cache to clear
- For Claude Artifact: refresh the page

**"JSON is invalid"**
- Use https://jsonlint.com/ to validate
- Check for unescaped quotes in descriptions
- Ensure all numeric fields are actual numbers, not strings

**"Data looks wrong"**
- Verify source data at FracTracker or Policy Database
- Check for data entry errors in the source
- Contact the source maintainers if issues persist

## Data Sources & Credits

**FracTracker Alliance**
- https://www.fractracker.org/data-centers/
- Regularly updated, maintains Operating/Proposed/Cancelled status

**Data Center Policy Database**
- https://www.datacenterpolicy.com/
- Maintained by: Bridges, Sundstrom, Hahn, & Wigginton (UVA Environmental Institute)
- Citation: Bridges, et al. (2026). Data Center Policy Database. doi:10.17613/PVSTG-4A775

**US Atlas**
- https://github.com/topojson/us-atlas
- County & state boundaries (TopoJSON format)

---

Questions? Check README.md for more information.
