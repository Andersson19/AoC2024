$daysPath = ".\days"
Get-ChildItem -Path $daysPath -Directory | ForEach-Object {
    $part1Path = Join-Path $_.FullName "part1.py"
    $part2Path = Join-Path $_.FullName "part2.py"

    if (-not (Test-Path $part1Path)) {
        New-Item -ItemType File -Path $part1Path
    }
    if (-not (Test-Path $part2Path)) {
        New-Item -ItemType File -Path $part2Path
    }
}
