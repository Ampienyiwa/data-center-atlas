# Push to GitHub - Step-by-Step Guide

Your U.S. Data Center Atlas is ready to push to GitHub. Follow these steps:

## Step 1: Install Git

1. Download Git from: **https://git-scm.com/**
2. Run the installer
3. Use default settings (click Next/Install)
4. **Important**: When asked about line endings, select "Checkout as-is, commit as-is"
5. Restart your computer (or restart PowerShell)

## Step 2: Create GitHub Repository

1. Go to: **https://github.com/new**
2. Fill in:
   - **Repository name**: `data-center-atlas`
   - **Description**: "Interactive atlas showing operating data centers and local restrictions across the US"
   - **Visibility**: Public (so your instructor can view)
3. ✅ Check "Add a README file" (optional - we have one)
4. Click **Create repository**
5. **Copy the repository URL** (looks like: `https://github.com/YOUR_USERNAME/data-center-atlas.git`)

## Step 3: Push Your Code

Open **PowerShell** in your `atlas` folder and run these commands:

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

- 4-page interactive data visualization
- Operating data centers with filtering
- 469 local policies from Data Center Policy Database
- Geographic analysis of proposal-restriction correlation
- Complete documentation and methods"

# Add remote (replace URL with your repository)
git remote add origin https://github.com/YOUR_USERNAME/data-center-atlas.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository: `https://github.com/YOUR_USERNAME/data-center-atlas`
2. Click **Settings** (top right)
3. Click **Pages** in the left sidebar
4. Under "Build and deployment":
   - **Source**: Deploy from a branch
   - **Branch**: `main` / `(root)`
5. Click **Save**
6. Wait 1-2 minutes
7. GitHub will show your site URL at: `https://YOUR_USERNAME.github.io/data-center-atlas/`

## Step 5: Verify It Works

1. Visit: `https://YOUR_USERNAME.github.io/data-center-atlas/`
2. Click through all 4 pages
3. Test the filters
4. Share the link with your instructor

## Troubleshooting

### "git: command not found" or "not recognized"
- Git is not installed or not in PATH
- Install from https://git-scm.com/
- Restart PowerShell after installing

### "fatal: could not read Username"
1. Run: `git credential reject https://github.com`
2. Try push again
3. Enter GitHub username and personal access token (see below)

### Generate Personal Access Token

If you get authentication errors:

1. Go to: https://github.com/settings/tokens/new
2. Create token with:
   - ✅ repo (full access)
   - ✅ workflow (if needed)
3. Copy the token (long string)
4. Use as password when git asks
5. Store it safely (GitHub won't show it again)

### "fatal: 'origin' does not appear to be a 'git' repository"
- You didn't run: `git remote add origin https://...`
- Run that command with your repository URL

### Site shows 404

1. Wait 2-3 minutes (GitHub needs to build)
2. Check Settings → Pages to see build status
3. Make sure `site.html` is in root folder
4. Refresh browser cache (Ctrl+Shift+Delete)

### Want to Update Your Site Later?

```powershell
# Check what changed
git status

# See changes
git diff

# Stage and commit
git add .
git commit -m "Update: describe what changed"

# Push to GitHub (site auto-updates)
git push
```

## Your Links

After pushing:

- **Live Site**: `https://YOUR_USERNAME.github.io/data-center-atlas/`
- **Repository**: `https://github.com/YOUR_USERNAME/data-center-atlas`
- **Claude Artifact**: `https://claude.ai/artifact/CXmTcHVRCAENGh2XFcUTb9`

## Git Cheat Sheet

```powershell
# Check status
git status

# View commits
git log --oneline

# View what changed
git diff

# Stage specific file
git add filename.html

# Unstage
git reset filename.html

# Undo last commit (before push)
git reset --soft HEAD~1

# View remote
git remote -v

# Change remote URL
git remote set-url origin https://github.com/NEW_URL.git
```

## Questions?

- Git help: https://git-scm.com/doc
- GitHub help: https://docs.github.com/en
- See: GITHUB_SETUP.md in your atlas folder for more details

---

Good luck! Your site will be live at GitHub Pages within minutes. 🚀
