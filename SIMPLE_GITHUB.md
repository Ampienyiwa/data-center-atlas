# Push to GitHub - 3 Simple Steps

## Step 1: Create GitHub Repo (5 minutes)

1. Go to: https://github.com/new
2. Name: `data-center-atlas`
3. Visibility: `Public`
4. Click **Create repository**
5. Copy the URL it shows (looks like: `https://github.com/Ampienyiwa/data-center-atlas.git`)

## Step 2: Push Your Code (3 minutes)

**Close PowerShell, open a NEW one, then:**

```powershell
cd "C:\Users\mensa\Data Viz - Mid Term\atlas"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Ampienyiwa/data-center-atlas.git
git branch -M main
git push -u origin main
```

That's it! Just copy & paste those 6 lines.

## Step 3: Enable GitHub Pages (1 minute)

1. Go to: https://github.com/Ampienyiwa/data-center-atlas
2. Click **Settings** → **Pages**
3. Branch: `main` / `(root)`
4. Wait 1-2 minutes

## Done! 🎉

Your site is now live at:
```
https://ampienyiwa.github.io/data-center-atlas/
```

Share that link with your instructor!
