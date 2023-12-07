@echo off
setlocal enabledelayedexpansion

echo.
echo --- Francesco Optimizer Uninstaller ---
echo Developed by: Zeroo
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
REM Check if the ClientSettings folder exists
if exist "%folder%\ClientSettings" (
    echo Uninstalling Francesco Optimizer...
    REM Remove the ClientAppSettings.json file
    del "%folder%\ClientSettings\ClientAppSettings.json" /q
    echo.
    echo Uninstallation completed successfully!
) else (
    echo Francesco Optimizer is not currently installed.
)

echo.
echo Press any key to exit... & pause >nul