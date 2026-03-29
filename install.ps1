Write-Host ""
Write-Host "   GREENCUBE" -ForegroundColor Green
Write-Host "   your agent learns from every task" -ForegroundColor DarkGray
Write-Host ""
$repo = "greencube-ai/greencube"
$version = "v1.0.0"
$url = "https://github.com/$repo/releases/download/$version/GreenCube_1.0.0_x64-setup.exe"
Write-Host "downloading GreenCube for Windows..."
$installer = "$env:TEMP\GreenCube-setup.exe"
Invoke-WebRequest -Uri $url -OutFile $installer
Write-Host "running installer..."
Start-Process -Wait $installer
Write-Host ""
Write-Host "GreenCube installed. open it from your Start menu."
Write-Host "then add this before running your agent:" -ForegroundColor DarkGray
Write-Host ""
Write-Host "  set OPENAI_API_BASE=http://localhost:9000/v1" -ForegroundColor Green
Write-Host ""
Write-Host "thats it. your agent now learns from every task."
