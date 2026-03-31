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

# Create gc.bat in WindowsApps (always in PATH on Windows 10/11)
$gcCreated = $false
$gcLocations = @(
    "$env:LOCALAPPDATA\Microsoft\WindowsApps",
    "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps",
    "$env:USERPROFILE"
)

foreach ($loc in $gcLocations) {
    if (Test-Path $loc) {
        try {
            $gcPath = Join-Path $loc "gc.bat"
            $gcScript = "@echo off`r`nfor /L %%p in (9000,1,9010) do (`r`n  curl -s http://localhost:%%p/health >nul 2>&1 && curl -s http://localhost:%%p/b && exit /b`r`n)`r`necho GreenCube is not running. Open the app first."
            Set-Content -Path $gcPath -Value $gcScript -Encoding ASCII -Force
            $gcCreated = $true
            break
        } catch {
            continue
        }
    }
}

# Fallback: also try creating in the GreenCube install directory and adding to PATH
if (-not $gcCreated) {
    try {
        $gcDir = "$env:LOCALAPPDATA\GreenCube"
        if (Test-Path $gcDir) {
            $gcPath = Join-Path $gcDir "gc.bat"
            $gcScript = "@echo off`r`nfor /L %%p in (9000,1,9010) do (`r`n  curl -s http://localhost:%%p/health >nul 2>&1 && curl -s http://localhost:%%p/b && exit /b`r`n)`r`necho GreenCube is not running. Open the app first."
            Set-Content -Path $gcPath -Value $gcScript -Encoding ASCII -Force
            $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
            if ($userPath -notlike "*$gcDir*") {
                [Environment]::SetEnvironmentVariable("PATH", "$userPath;$gcDir", "User")
            }
            $gcCreated = $true
        }
    } catch {}
}

Write-Host ""
Write-Host "  installed." -ForegroundColor Green
Write-Host ""
if ($gcCreated) {
    Write-Host "  next steps:" -ForegroundColor White
    Write-Host "  1. open a " -ForegroundColor DarkGray -NoNewline
    Write-Host "new terminal" -ForegroundColor White
    Write-Host "  2. run " -ForegroundColor DarkGray -NoNewline
    Write-Host "greencube" -ForegroundColor Green -NoNewline
    Write-Host " to set up your provider" -ForegroundColor DarkGray
    Write-Host "  3. type " -ForegroundColor DarkGray -NoNewline
    Write-Host "gc" -ForegroundColor Green -NoNewline
    Write-Host " to see what your agent learned" -ForegroundColor DarkGray
} else {
    Write-Host "  next steps:" -ForegroundColor White
    Write-Host "  1. open a new terminal" -ForegroundColor DarkGray
    Write-Host "  2. run " -ForegroundColor DarkGray -NoNewline
    Write-Host "greencube" -ForegroundColor Green -NoNewline
    Write-Host " to set up your provider" -ForegroundColor DarkGray
    Write-Host "  3. type " -ForegroundColor DarkGray -NoNewline
    Write-Host "curl -s localhost:9000/brain" -ForegroundColor Green -NoNewline
    Write-Host " to check your agent" -ForegroundColor DarkGray
}
Write-Host ""
