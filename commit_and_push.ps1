# Helper script to commit local changes and push to your GitHub remote.
# Run this from the repository root in PowerShell.

$remoteUrl = 'https://github.com/Pranavkrishna136/travel-guide-assistant.git'

Write-Host "Staging all changes..."
git add .

Write-Host "Creating a commit (if there are staged changes)..."
git commit -m "docs: add MkDocs documentation and deploy workflow" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "No commit created (probably nothing to commit). Proceeding to push if remote/branch exist." -ForegroundColor Yellow
} else {
    Write-Host "Commit created." -ForegroundColor Green
}

# Ensure origin remote points to your repo
git remote get-url origin 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Adding remote origin -> $remoteUrl"
    git remote add origin $remoteUrl
} else {
    Write-Host "Setting remote origin URL -> $remoteUrl"
    git remote set-url origin $remoteUrl
}

# Ensure branch is main
git branch -M main

Write-Host "Pushing to origin/main (you may be prompted for credentials)..."
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "Push succeeded." -ForegroundColor Green
} else {
    Write-Host "Push failed. Check your network, credentials, or remote settings." -ForegroundColor Red
}

Write-Host "Done. If you want, run 'mkdocs gh-deploy' locally to preview/publish docs as well." -ForegroundColor Cyan
