$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "   GREENCUBE" -ForegroundColor Green
Write-Host "   your agent learns from every task" -ForegroundColor DarkGray
Write-Host ""

$repo = "greencube-ai/greencube"

# Get latest release
Write-Host "detecting latest release..."
try {
    $release = Invoke-RestMethod "https://api.github.com/repos/$repo/releases/latest"
    $version = $release.tag_name
} catch {
    Write-Host "error: could not reach GitHub. check your internet connection." -ForegroundColor Red
    exit 1
}

# Find the right asset
$arch = if ([Environment]::Is64BitOperatingSystem) { "x64" } else { "x86" }
$asset = $release.assets | Where-Object { $_.name -match "setup" -and $_.name -match $arch -and $_.name -match "\.exe$" } | Select-Object -First 1

if (-not $asset) {
    # Fallback: try any .exe
    $asset = $release.assets | Where-Object { $_.name -match "\.exe$" } | Select-Object -First 1
}

if (-not $asset) {
    Write-Host "error: no Windows installer found in $version. check github.com/$repo/releases" -ForegroundColor Red
    exit 1
}

$url = $asset.browser_download_url
$installer = "$env:TEMP\GreenCube-setup.exe"

Write-Host "downloading GreenCube $version for Windows ($arch)..."
Invoke-WebRequest -Uri $url -OutFile $installer -UseBasicParsing

Write-Host "running installer..."
Start-Process -Wait $installer
Remove-Item $installer -Force -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "done." -ForegroundColor Green -NoNewline
Write-Host " open GreenCube from your Start menu."
Write-Host ""
Write-Host "then add this before running your agent:" -ForegroundColor DarkGray
Write-Host ""
Write-Host '  $env:OPENAI_API_BASE = "http://localhost:9000/v1"' -ForegroundColor Green
Write-Host ""
Write-Host "  or in cmd:" -ForegroundColor DarkGray
Write-Host '  set OPENAI_API_BASE=http://localhost:9000/v1' -ForegroundColor Green
Write-Host ""
Write-Host "that's it. your agent now learns from every task."
