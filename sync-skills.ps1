# ==============================================================================
# Gentleman Ecosystem - Antigravity & AI Agent Skills Sync
# ==============================================================================
[CmdletBinding()]
param(
    [switch]$Symlink = $false
)

$targetDir = Join-Path $env:USERPROFILE ".gemini\config\skills"
$sourceDir = Join-Path $PSScriptRoot "skills"
$mcpExample = Join-Path $PSScriptRoot "antigravity\mcp_config.example.json"
$mcpTarget = Join-Path $env:USERPROFILE ".gemini\config\mcp_config.json"

Write-Host "=== Sincronizando Skills de Gentleman Ecosystem ===" -ForegroundColor Cyan
Write-Host "Origen: $sourceDir" -ForegroundColor Gray
Write-Host "Destino: $targetDir" -ForegroundColor Gray

if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    Write-Host "[+] Directorio destino creado." -ForegroundColor Green
}

$skills = Get-ChildItem -Path $sourceDir -Directory
$count = 0

foreach ($skill in $skills) {
    $destPath = Join-Path $targetDir $skill.Name
    if ($Symlink) {
        if (Test-Path $destPath) { Remove-Item $destPath -Recurse -Force }
        New-Item -ItemType Junction -Path $destPath -Target $skill.FullName | Out-Null
    } else {
        Copy-Item -Path $skill.FullName -Destination $targetDir -Recurse -Force
    }
    $count++
}

Write-Host "[OK] Se sincronizaron $count skills correctamente." -ForegroundColor Green

# MCP Config Template check
if (!(Test-Path $mcpTarget)) {
    if (Test-Path $mcpExample) {
        $mcpTargetDir = Split-Path $mcpTarget -Parent
        if (!(Test-Path $mcpTargetDir)) { New-Item -ItemType Directory -Path $mcpTargetDir -Force | Out-Null }
        Copy-Item -Path $mcpExample -Destination $mcpTarget
        Write-Host "[!] Se creo mcp_config.json con valores de ejemplo en $mcpTarget." -ForegroundColor Yellow
        Write-Host "    Recorda configurar tus API keys (GitHub, Google, etc.)." -ForegroundColor Yellow
    }
} else {
    Write-Host "[OK] mcp_config.json ya existe en el destino." -ForegroundColor Gray
}

Write-Host "=== Sincronizacion completada con exito ===" -ForegroundColor Cyan
