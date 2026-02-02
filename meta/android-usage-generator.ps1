# SPDX-License-Identifier: Unlicense

<#
.SYNOPSIS
    Generates cumulative usage for Android versions from statcounter
.DESCRIPTION
    This script produces cumulative usage for Android versions beginning from 4.0 ICS.

    It can update the index.md homepage for apilevels or just print the cumulative usage
    against API level.
.EXAMPLE
    ./android-usage.generator.ps1

    Updates index.md with cumulative usages for Android API levels up to the previous month
.EXAMPLE
    ./android-usage.generator.ps1 -JustPrint

    Prints a list of cumulative usages for Android API levels up to the previous month
.EXAMPLE
    ./android-usage.generator.ps1 -Month 2026-01

    Updates index.md with cumulative usages for Android API levels up to January 2026
.PARAMETER Month
    A year and month in the format YYYY-MM (e.g. 2026-01) to generate cumulative usage up to
.PARAMETER JustPrint
    Don't update the apilevels index.md file, and print cumulative usage to console
.OUTPUTS
    None
.NOTES
    Statcounter often holds incomplete data for the current month, so you shouldn't use the current month
    with -Month YYYY-MM when updating the homepage.
.LINK
    https://github.com/ebelinski/apilevels
.LINK
    https://gs.statcounter.com/android-version-market-share/mobile-tablet
#>

[CmdletBinding()]
param (
    [ValidatePattern('20\d{2}-(?:0[1-9]|1[012])')]
    [string]$Month = '',
    [switch]$JustPrint
)

begin {
    $Target = Join-Path $PSScriptRoot "../index.md"
    $ValidVersions = @{
        '4.0' = 15; '4.1' = 16; '4.2' = 17; '4.3' = 18; '4.4' = 20; '5.0' = 21; '5.1' = 22; '6.0' = 23; '7.0' = 24;
        '7.1' = 25; '8.0' = 26; '8.1' = 27; '9.0' = 28; '10.0' = 29; '11.0' = 30; '12.0' = 32; '13.0' = 33;
        '14.0' = 34; '15.0' = 35; '16.0' = 36
    }
    $DataUrlTemplate = 'https://gs.statcounter.com/android-version-market-share/mobile-tablet/chart.php?' +
    'device=Mobile%20%26%20Tablet&device_hidden=mobile%2Btablet&multi-device=true&statType_hidden=' +
    'android_version&region_hidden=ww&granularity=monthly&statType=Android%20Version&region=Worldwide&' +
    'fromInt=201706&toInt={0}&fromMonthYear=2017-06&toMonthYear={1}&csv=1'
}

process {
    if (-not (Test-Path $Target -PathType Leaf)) {
        throw "Target file '$Target' not found!"
    }

    if ([string]::IsNullOrEmpty($Month)) {
        $TargetMonth = [datetime]::Now.AddMonths(-1).ToString('yyyy-MM')
    } else {
        $TargetMonth = $Month
    }
    $TargetMonthInt = $TargetMonth -ireplace '-'
    $DataUrl = $DataUrlTemplate -f $TargetMonthInt, $TargetMonth

    Write-Host "Retrieving monthly usage stats from URL '$DataUrl'..."
    $Data = Invoke-RestMethod -Uri $DataUrl | ConvertFrom-Csv
    $Latest = $Data | Sort-Object -Property { [datetime]::Parse($_.Date) } -Descending | Select-Object -First 1

    Write-Host "Getting usage stats for month: $($Latest.Date)..."
    $Versions = $Latest.PSObject.Properties |
        Select-Object @{Name = 'Version'; Expression = {
                $_.Name -ireplace '^([\d.]+).*', '$1'
            }
        }, @{Name = 'Share'; Expression = { $_.Value -as [Double] } } |
        Where-Object Version -In $ValidVersions.Keys |
        Sort-Object -Property { $_.Version -as [Single] } -Descending

    Write-Host 'Summing cumulative usages...'
    $Cumulative = 0
    $LevelPcs = @{}
    foreach ($Field in $Versions) {
        $Share = $Field.Share
        $Cumulative += $Share
        $LevelPcs[$ValidVersions[$Field.Version]] = '{0:F1}' -f [Double]::Min($Cumulative, 100)
    }

    if ($JustPrint) {
        Write-Host "Printing cumulative usage for each API Level..."
        return [pscustomobject]$LevelPcs
    }

    Write-Host "Replacing cumulative usage stats in file '$Target'..."
    $PageContent = Get-Content -Path $Target -Raw
    foreach ($Level in $LevelPcs.Keys) {
        $Pattern = ('(?s)((?><td>\s*Level\s+{0}.*?</td>)\s*(?><td>.+?</td>)\s*(?><td.+?</td>)?\s*' +
            '\{{% include progress-cell.html rowspan=\d+ percentage=)([\d\.]+)(\s*%\}})') -f [regex]::Escape($Level)
        if ($PageContent -inotmatch $Pattern) {
            Write-Host -ForegroundColor Red "Couldn't find replacement region for API level $Level!"
            continue
        }
        Write-Host "    API Level ${Level}: Replacing $($Matches[2])% with $($LevelPcs[$Level])%."
        $PageContent = $PageContent -ireplace $Pattern, ('${{1}}{0}$3' -f $LevelPcs[$Level])
    }

    Write-Host "Replacing last updated footnote in file '$Target'..."
    $TodayPretty = Get-Date -Format 'MMMM dd, yyyy'
    $PageContent = $PageContent -ireplace
    '(Cumulative usage distribution figures were last updated on)[\w, ]+(using <b>)[\w ]+(</b> data from)',
    ('$1 {0} $2{1}$3' -f $TodayPretty, [datetime]::Parse($TargetMonth).ToString('MMMM yyyy'))

    Write-Host "Writing changes to '$Target'..."
    Set-Content -Path $Target -Value $PageContent -NoNewline
}
