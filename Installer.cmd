@echo off
setlocal enabledelayedexpansion

echo.
echo --- Francesco Optimizer Installer ---
echo Developed by: Zeroo
echo.

echo.
echo Initializing Francesco Optimizer installation...
echo.

REM Locate the Roblox installation folder in %localappdata%
for /d %%i in ("%localappdata%\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

REM If not found, search in Program Files (x86)
for /d %%i in ("%cd:~0,2%\Program Files (x86)\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

REM If still not found, search in Program Files
for /d %%i in ("%cd:~0,2%\Program Files\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

:NextStep
REM Create the ClientSettings folder if it doesn't exist
if not exist "%folder%\ClientSettings" (
    mkdir "%folder%\ClientSettings"
)

echo Downloading the essential configuration file...

REM Utilizing PowerShell to fetch the necessary file
powershell.exe -Command "& { (New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/FrancescoTheToad/F.Optimizer/main/client settings/ClientAppSettings.json', '%folder%\ClientSettings\ClientAppSettings.json') }"

REM Verify the download's success using the exit code
if !errorlevel! EQU 0 (
    echo.
    echo Configuration file downloaded successfully!
    echo.
    echo INSTALLATION SUCCESSFUL: Francesco Optimizer is ready to enhance your Roblox experience!
) else (
    echo.
    echo Unable to download the configuration file.
    echo.
    echo INSTALLATION ERROR: Francesco Optimizer setup has encountered a problem.
)

echo.
echo Press any key to exit... & pause >nul
