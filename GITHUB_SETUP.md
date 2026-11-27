# GitHub Setup Guide

This guide walks you through pushing your U.S. Data Center Atlas to GitHub and enabling GitHub Pages hosting.

## Prerequisites

1. **GitHub Account**: Sign up at https://github.com (free)
2. **Git Installed**: Download from https://git-scm.com/

## Step 1: Create a New GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: `data-center-atlas`
3. Description: "Interactive atlas showing operating data centers and local restrictions across the US"
4. Select **Public** (so your instructor can view it)
5. ✓ Check "Add a README file" (optional - we have one)
6. Click **Create repository**
7. Copy the repository URL (looks like: `https://github.com/YOUR_USERNAME/data-center-atlas.git`)

## Step 2: Push Your Code

Open PowerShell in your `atlas` folder and run:

```powershell
# Initialize git
git init

# Configure git (use your GitHub email)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: U.S. Data Center Atlas

- 469 local data center policies from Data Center Policy Database
- 15 sample operating facilities from FracTracker Alliance
- Interactive filtering and state-by-state breakdown
- 3-page site with documentation"

# Add remote (replace with your repository URL)
git remote add origin https://github.com/YOUR_USERNAME/data-center-atlas.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main` / `(root)`
5. Click **Save**
6. Wait 1-2 minutes for GitHub to build your site
7. Your site will be live at: `https://YOUR_USERNAME.github.io/data-center-atlas/`

## Step 4: Verify It Works

1. Visit `https://YOUR_USERNAME.github.io/data-center-atlas/`
2. You should see the site with all 3 pages working
3. Try the filters on page 2
4. Check the state tables

## Sharing Your Work

Share the link in your format:
- **Live Site**: `https://YOUR_USERNAME.github.io/data-center-atlas/`
- **GitHub Repo**: `https://github.com/YOUR_USERNAME/data-center-atlas`
- **Claude Artifact**: `https://claude.ai/artifact/CXmTcHVRCAENGh2XFcUTb9`

## Updating Your Site

After you update `site.html`, `facilities.json`, or `policies.json`:

```powershell
# Check what changed
git status

# Stage changes
git add .

# Commit with a message
git commit -m "Update: [describe what changed]"

# Push to GitHub (site auto-updates)
git push
```

## Troubleshooting

**"Git not found"**
- Install Git from https://git-scm.com/
- Restart PowerShell after installing

**"fatal: could not read Username"**
- Run: `git credential reject https://github.com`
- Try push again, enter GitHub username and personal access token
- Or use SSH keys (see GitHub docs)

**"Permission denied"**
- Make sure you're using `https://` URL, not `git@github`
- Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

**Site shows 404**
- Wait 2-3 minutes after first push (GitHub needs to build)
- Check Settings → Pages → Build status

## Next Steps

Once your site is live:

1. **Share with Instructor**: Send the GitHub Pages URL
2. **Update Data**: Replace `facilities.json` and `policies.json` with real FracTracker data
3. **Add Maps**: Integrate D3.js visualization (see README.md)
4. **Document Changes**: Update UPDATES.md with what changed

## Example GitHub Pages URLs

```
My Site:     https://yourname.github.io/data-center-atlas/
Your Repo:   https://github.com/yourname/data-center-atlas
Main Branch: https://github.com/yourname/data-center-atlas/tree/main
```

## Commands Cheat Sheet

```powershell
# Check status
git status

# See recent commits  
git log --oneline

# Undo last commit (before push)
git reset --soft HEAD~1

# See what changed
git diff

# See what's staged
git diff --staged

# Remove a file from tracking
git rm --cached filename.txt

# Stash changes (save for later)
git stash

# View stashed changes
git stash list

# Apply stashed changes
git stash pop
```

---

Questions? See the full README.md for more details.
