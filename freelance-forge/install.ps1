# Freelance Forge — install script (Windows PowerShell)
# Copies skills to the agent's skills directory and shared scripts/references to ~/.freelance-forge/

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# --- Detect target skills directory ---
function Get-SkillsDir {
    $candidates = @(
        "$env:USERPROFILE\.openclaw\skills",
        "$env:USERPROFILE\.claude\skills"
    )
    foreach ($dir in $candidates) {
        if (Test-Path $dir) {
            return $dir
        }
    }
    $userDir = Read-Host "Could not auto-detect skills directory. Enter the path"
    return $userDir
}

$SkillsDir = Get-SkillsDir
$DataDir = if ($env:FREELANCE_FORGE_CONFIG_DIR) { $env:FREELANCE_FORGE_CONFIG_DIR } else { "$env:USERPROFILE\.freelance-forge" }

Write-Host "=== Freelance Forge Installer ==="
Write-Host "Skills directory: $SkillsDir"
Write-Host "Data directory:   $DataDir"
Write-Host ""

# --- Create data directory tree ---
@("reports\qualifications", "reports\proposals", "reports\projects", "exports") | ForEach-Object {
    New-Item -ItemType Directory -Path "$DataDir\$_" -Force | Out-Null
}

# --- Copy shared scripts ---
$SharedDest = "$DataDir\shared"
New-Item -ItemType Directory -Path $SharedDest -Force | Out-Null
Copy-Item "$ScriptDir\shared\__init__.py" "$SharedDest\" -Force
Copy-Item "$ScriptDir\shared\db_helper.py" "$SharedDest\" -Force
Copy-Item "$ScriptDir\shared\web_research.py" "$SharedDest\" -Force
Copy-Item "$ScriptDir\shared\templates.py" "$SharedDest\" -Force
Write-Host "✓ Shared scripts installed to $SharedDest"

# --- Copy references ---
$RefsDest = "$DataDir\references"
New-Item -ItemType Directory -Path $RefsDest -Force | Out-Null
Copy-Item "$ScriptDir\references\*" "$RefsDest\" -Recurse -Force
Write-Host "✓ Reference templates installed to $RefsDest"

# --- Copy skills ---
$skillNames = @("lead-qualifier", "proposal-builder", "project-onboarder", "pipeline-tracker")
foreach ($skill in $skillNames) {
    $src = "$ScriptDir\skills\$skill"
    if (Test-Path $src) {
        $dest = "$SkillsDir\$skill"
        New-Item -ItemType Directory -Path $dest -Force | Out-Null
        Copy-Item "$src\SKILL.md" "$dest\" -Force
        Write-Host "✓ $skill installed to $dest\"
    } else {
        Write-Host "⚠ $skill not found in source — skipping"
    }
}

# --- Verify ---
Write-Host ""
Write-Host "=== Verifying installation ==="
$env:PYTHONPATH = $SharedDest
try {
    python3 -c "import db_helper" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Python modules import successfully"
    } else {
        Write-Host "  ⚠ Could not import db_helper — check Python 3 is installed"
    }
} catch {
    Write-Host "  ⚠ Python 3 not found — install from python.org"
}

try {
    python3 -c "import requests" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ⚠ 'requests' not installed — run: pip install requests beautifulsoup4"
    }
} catch {}

Write-Host ""
Write-Host "=== Installation complete ==="
Write-Host ""
Write-Host '  "qualify this lead: https://example.com"'
Write-Host '  "build a proposal for Acme"'
Write-Host '  "set up project for Acme"'
Write-Host '  "show my pipeline"'
Write-Host ""
Write-Host "All data lives in: $DataDir"
Write-Host "Re-run this script anytime to upgrade in place (your data is never touched)."
