$ThemesDir = Join-Path $env:USERPROFILE "AppData\Roaming\Zed\themes"
New-Item -ItemType Directory -Force -Path $ThemesDir | Out-Null

Copy-Item -Force ".\themes\*.json" $ThemesDir
if (Test-Path ".\themes\experimental") {
  Copy-Item -Force ".\themes\experimental\*.json" $ThemesDir -ErrorAction SilentlyContinue
}

Write-Host "Installed themes into: $ThemesDir"
Write-Host "Restart Zed and open the Theme Selector."
