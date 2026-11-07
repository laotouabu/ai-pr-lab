# 本地版 CI：ruff + pytest
# 用法：powershell -ExecutionPolicy Bypass -File scripts\check.ps1

$ErrorActionPreference = "Stop"
Set-Location (Split-Path $PSScriptRoot -Parent)

Write-Host "==> uv sync" -ForegroundColor Cyan
uv sync

Write-Host "==> ruff check" -ForegroundColor Cyan
uv run ruff check .
if ($LASTEXITCODE -ne 0) {
    Write-Host "ruff 未通过" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "==> pytest" -ForegroundColor Cyan
uv run pytest
if ($LASTEXITCODE -ne 0) {
    Write-Host "pytest 未通过" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "本地检查全部通过" -ForegroundColor Green
