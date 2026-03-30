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
try {
    Invoke-WebRequest -Uri $url -OutFile $installer -UseBasicParsing
} catch {
    Write-Host "error: download failed." -ForegroundColor Red
    exit 1
}

Write-Host "installing..."
$proc = Start-Process -FilePath $installer -PassThru -Wait
$proc.WaitForExit()
Remove-Item $installer -Force -ErrorAction SilentlyContinue

# Create gc.bat
try {
    $gcPath = "$env:USERPROFILE\gc.bat"
    Set-Content -Path $gcPath -Value "@echo off`r`ncurl -s http://localhost:9000/b" -Encoding ASCII

    # Add to PATH if needed
    $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    if ($userPath -and ($userPath -notlike "*$env:USERPROFILE*")) {
        [Environment]::SetEnvironmentVariable("PATH", "$userPath;$env:USERPROFILE", "User")
    } elseif (-not $userPath) {
        [Environment]::SetEnvironmentVariable("PATH", "$env:USERPROFILE", "User")
    }
} catch {
    Write-Host "  (could not create gc shortcut — you can still use: curl localhost:9000/brain)" -ForegroundColor DarkGray
}

Write-Host ""
Write-Host "  installed." -ForegroundColor Green
Write-Host ""
Write-Host "  next steps:" -ForegroundColor White
Write-Host "  1. open a new terminal" -ForegroundColor DarkGray
Write-Host "  2. run " -ForegroundColor DarkGray -NoNewline
Write-Host "greencube" -ForegroundColor Green
Write-Host "  3. pick your provider, enter your key" -ForegroundColor DarkGray
Write-Host "  4. type " -ForegroundColor DarkGray -NoNewline
Write-Host "gc" -ForegroundColor Green -NoNewline
Write-Host " to see what your agent learned" -ForegroundColor DarkGray
Write-Host ""
