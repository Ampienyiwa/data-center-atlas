#!/usr/bin/env python3
"""Process policies.csv and generate JSON data for the site."""

import csv
import json
from datetime import datetime
from collections import defaultdict
import re

# Read and process policies
policies = []
county_map = {}  # maps FIPS to list of policies

# FIPS to state code mapping (simplified)
state_to_fips_prefix = {
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08',
    'CT': '09', 'DE': '10', 'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16',
    'IL': '17', 'IN': '18', 'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22',
    'ME': '23', 'MD': '24', 'MA': '25', 'MI': '26', 'MN': '27', 'MS': '28',
    'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 'NH': '33', 'NJ': '34',
    'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 'OK': '40',
    'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47',
    'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54',
    'WI': '55', 'WY': '56', 'DC': '11'
}

# Read policies from CSV
with open('C:\\Users\\mensa\\Downloads\\policies.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Only keep local policies with passed/enacted status
        if row['level_of_government'] != 'Local':
            continue
        if row['status'] not in ['Passed', 'Signed/Enacted']:
            continue

        state = row['state'].strip()
        locality = row['locality'].strip()

        # Determine policy type
        policy_type = 'Zoning & siting rules'
        if 'moratorium' in row['name'].lower() or 'moratorium' in row['key_mechanism'].lower():
            policy_type = 'Moratorium'
        elif 'ban' in row['name'].lower() or 'ban' in row['key_mechanism'].lower():
            policy_type = 'Ban'

        # Parse dates
        date_passed = row.get('last_action_date', '').strip() or None
        end_date = row.get('end_date_moratorium', '').strip() or None

        policy = {
            'id': int(row['id']),
            'locality': locality,
            'state': state,
            'name': row.get('name', '').strip(),
            'type': policy_type,
            'date': date_passed,
            'end': end_date if policy_type == 'Moratorium' else None,
            'description': row.get('description', '').strip()[:200],
            'url': row.get('url', '').strip(),
            'fips': []  # Placeholder - would need county FIPS lookup
        }

        policies.append(policy)

# Sort by date descending
policies.sort(key=lambda x: x['date'] or '2000-01-01', reverse=True)

print(f"Loaded {len(policies)} local policies")

# Count by state and type
state_counts = defaultdict(lambda: {'Total': 0, 'Moratorium': 0, 'Ban': 0, 'Zoning & siting rules': 0})
for policy in policies:
    state = policy['state']
    state_counts[state]['Total'] += 1
    state_counts[state][policy['type']] += 1

print(f"\nPolicies by state (top 10):")
for state, counts in sorted(state_counts.items(), key=lambda x: x[1]['Total'], reverse=True)[:10]:
    print(f"  {state}: {counts['Total']} (Mor: {counts['Moratorium']}, Ban: {counts['Ban']}, Zone: {counts['Zoning & siting rules']})")

# Save policies JSON
with open('policies.json', 'w') as f:
    json.dump(policies, f, indent=2)

print(f"\nSaved policies to policies.json")

# Create sample FracTracker facilities data (since we can't access Google Sheets directly)
# This is based on the original site's data
facilities_sample = [
    {"id": 1, "name": "Northern Virginia Data Center", "operator": "Amazon", "state": "VA", "coordinates": [-77.5, 38.8], "size": "mega", "mw": 400, "pushback": True},
    {"id": 2, "name": "Atlanta Hub", "operator": "Microsoft", "state": "GA", "coordinates": [-84.4, 33.7], "size": "hyperscale", "mw": 350, "pushback": False},
    {"id": 3, "name": "Texas Complex", "operator": "Meta", "state": "TX", "coordinates": [-97.5, 32.0], "size": "mega", "mw": 500, "pushback": False},
]

print(f"\nCreated sample FracTracker data with {len(facilities_sample)} facilities")
print("NOTE: Replace this with real FracTracker data from Google Sheets")

with open('facilities.json', 'w') as f:
    json.dump(facilities_sample, f, indent=2)

print("Saved sample facilities to facilities.json")
print("\nData processing complete!")
