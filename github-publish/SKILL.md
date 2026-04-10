---
name: github-publish
description: Create a GitHub repo from a local project and push initial code. Use when asked to "push to GitHub", "create a GitHub repo", "publish to GitHub", or "make a GitHub repo" for a project.
---

# GitHub Publish 🚀

Create a GitHub repository from a local project directory and push the initial commit.

## Token

GitHub PAT stored at `~/.config/github-growth-tracker/github.json` under key `github_token`. The token may lack `gh auth login` scopes, so use the `GH_TOKEN` env var for all `gh` commands:

```bash
export GH_TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.config/github-growth-tracker/github.json'))['github_token'])")
```

Set this at the start of every operation.

## Steps

1. **Check for existing git repo** in the target directory
   - If `.git` exists: skip init, just add remote and push
   - If no `.git`: initialize with `git init`

2. **Ensure a `.gitignore` exists**
   - Check for common files that shouldn't be committed: `__pycache__/`, `*.pyc`, `node_modules/`, `.env`, `*.csv.bak.*`, any user-specific data files
   - Create `.gitignore` if missing

3. **Commit all files**
   ```bash
   git add -A
   git commit -m "<descriptive initial commit message>"
   ```

4. **Create GitHub repo and push**
   ```bash
   export GH_TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.config/github-growth-tracker/github.json'))['github_token'])")
   gh repo create <repo-name> --public --description "<description>" --source <path> --push
   ```

   - `--source <path>` sets the local path and pushes
   - Use `--private` instead of `--public` if requested
   - The repo name defaults to the directory name if not specified

5. **Report the result** — share the repo URL

## Rules

- Always check the directory contents before committing — don't push secrets, credentials, or user data
- Write a meaningful commit message that describes the project
- If the repo already has a remote set up, ask the user if they want to force push or skip
- The GitHub username is `99rebels`
