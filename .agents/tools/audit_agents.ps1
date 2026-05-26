param(
    [string]$Root = "."
)

$ErrorActionPreference = "Stop"
$repo = Resolve-Path $Root
$agents = Join-Path $repo ".agents"
$manifest = Join-Path $agents "manifest.yaml"
$errors = New-Object System.Collections.Generic.List[string]
$manifestPaths = New-Object System.Collections.Generic.HashSet[string]

function Add-Error([string]$Message) {
    $errors.Add($Message) | Out-Null
}

function Convert-ToManifestPath([string]$Path) {
    $relative = Resolve-Path -LiteralPath $Path -Relative
    return ($relative -replace "^\.\\", "" -replace "\\", "/")
}

function Test-FrontMatterKey([string]$Path, [string[]]$Keys) {
    $lines = Get-Content -LiteralPath $Path -TotalCount 80
    if ($lines.Count -eq 0 -or $lines[0] -ne "---") {
        Add-Error "Missing front matter: $Path"
        return
    }

    foreach ($key in $Keys) {
        $matches = @($lines | Where-Object { $_ -match "^$([regex]::Escape($key)):" })
        if ($matches.Count -eq 0) {
            Add-Error "Missing front matter key '$key': $Path"
        }
        if ($matches.Count -gt 1) {
            Add-Error "Duplicate front matter key '$key': $Path"
        }
    }
}

if (-not (Test-Path -LiteralPath $manifest)) {
    Add-Error "Missing manifest: $manifest"
} else {
    $manifestLines = Get-Content -LiteralPath $manifest
    $pathMatches = $manifestLines | Select-String -Pattern '"(\.agents/[^"]+)"'
    foreach ($match in $pathMatches) {
        $manifestPath = $match.Matches[0].Groups[1].Value
        $manifestPaths.Add($manifestPath) | Out-Null
        $relative = $manifestPath -replace "/", "\"
        $target = Join-Path $repo $relative
        if (-not (Test-Path -LiteralPath $target)) {
            Add-Error "Manifest path does not exist: $relative"
        }
    }
}

$canonicalComponents = @()
$canonicalComponents += Get-ChildItem -LiteralPath (Join-Path $agents "editorial\roles") -Filter "*.md" -File -Recurse
$canonicalComponents += Get-ChildItem -LiteralPath (Join-Path $agents "editorial\rules"), (Join-Path $agents "generos\hard_scifi_contemplativa\rules"), (Join-Path $agents "novelas\bitacora_centauri\rules") -Filter "*.md" -File -Recurse
$canonicalComponents += Get-ChildItem -LiteralPath (Join-Path $agents "editorial\workflows"), (Join-Path $agents "generos\hard_scifi_contemplativa\workflows"), (Join-Path $agents "novelas\bitacora_centauri\workflows") -Filter "*.md" -File -Recurse
$canonicalComponents += Get-ChildItem -LiteralPath (Join-Path $agents "editorial\skills"), (Join-Path $agents "generos\hard_scifi_contemplativa\skills"), (Join-Path $agents "novelas\bitacora_centauri\skills") -Filter "SKILL.md" -File -Recurse

foreach ($component in $canonicalComponents) {
    $manifestPath = Convert-ToManifestPath $component.FullName
    if ($component.Name -eq "SKILL.md") {
        Test-FrontMatterKey $component.FullName @("name", "scope")
    } else {
        Test-FrontMatterKey $component.FullName @("id", "scope")
    }

    if (-not $manifestPaths.Contains($manifestPath)) {
        Add-Error "Canonical component is not declared in manifest: $manifestPath"
    }
}

Get-ChildItem -LiteralPath (Join-Path $agents "rules"), (Join-Path $agents "skills"), (Join-Path $agents "workflows") -File -Recurse |
    ForEach-Object {
        $content = Get-Content -LiteralPath $_.FullName -Raw
        if ($content -match 'canonical:\s*"([^"]+)"') {
            $relative = $Matches[1] -replace "/", "\"
        } elseif ($content -match '`(\.agents/[^`]+)`') {
            $relative = $Matches[1] -replace "/", "\"
        } else {
            Add-Error "Wrapper without canonical target: $($_.FullName)"
            return
        }

        $target = Join-Path $repo $relative
        if (-not (Test-Path -LiteralPath $target)) {
            Add-Error "Wrapper canonical target does not exist: $($_.FullName) -> $relative"
        }
    }

$requiredProjectPaths = @(
    "manuscrito",
    "trama",
    "trama\premisas",
    "trama\escaletas",
    "biblia",
    "biblia\personajes",
    "biblia\mundo",
    "biblia\tecnologia",
    "exportacion",
    "exportacion\es"
)

foreach ($relative in $requiredProjectPaths) {
    $target = Join-Path $repo $relative
    if (-not (Test-Path -LiteralPath $target)) {
        Add-Error "Missing normalized novel structure path: $relative"
    }
}

$requiredIndexFiles = @(
    "trama\README.md",
    "biblia\personajes\README.md",
    "biblia\mundo\README.md",
    "biblia\tecnologia\README.md",
    "exportacion\README.md",
    "exportacion\es\README.md"
)

foreach ($relative in $requiredIndexFiles) {
    $target = Join-Path $repo $relative
    if (-not (Test-Path -LiteralPath $target)) {
        Add-Error "Missing normalized novel structure index: $relative"
    }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Output "ERROR: $_" }
    exit 1
}

Write-Output "OK: .agents structural audit passed."

