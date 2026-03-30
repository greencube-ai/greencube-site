$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "   GREENCUBE" -ForegroundColor Green
Write-Host "   your agent stops repeating mistakes" -ForegroundColor DarkGray
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

# Create gc.bat shortcut
$gcPath = "$env:USERPROFILE\gc.bat"
'@echo off' | Out-File -FilePath $gcPath -Encoding ascii
'curl -s localhost:9000/b' | Out-File -FilePath $gcPath -Encoding ascii -Append

# Add user profile to PATH if not already there
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$env:USERPROFILE*") {
    [Environment]::SetEnvironmentVariable("PATH", "$userPath;$env:USERPROFILE", "User")
}

Write-Host ""
Write-Host "done." -ForegroundColor Green -NoNewline
Write-Host " open GreenCube from your Start menu."
Write-Host ""
Write-Host "  type " -NoNewline
Write-Host "gc" -ForegroundColor Green -NoNewline
Write-Host " anytime to see what your agent learned."
Write-Host ""
Write-Host "  (open a new terminal for the gc command to work)" -ForegroundColor DarkGray
Write-Host ""
