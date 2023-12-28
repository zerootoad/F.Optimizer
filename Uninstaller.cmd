@echo off
setlocal enabledelayedexpansion

echo.
echo --- Francesco Optimizer Uninstaller ---
echo Developed by: Zeroo
echo.

for /d %%i in ("%localappdata%\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

for /d %%i in ("%cd:~0,2%\Program Files (x86)\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

for /d %%i in ("%cd:~0,2%\Program Files\Roblox\Versions\*") do (
    if exist "%%i\RobloxPlayerBeta.exe" (
        set folder=%%i
        goto :NextStep
    )
)

:NextStep
if exist "%folder%\ClientSettings" (
    echo Uninstalling Francesco Optimizer...
    del "%folder%\ClientSettings\ClientAppSettings.json" /q
    echo.
    echo Uninstallation completed successfully!
) else (
    echo Francesco Optimizer is not currently installed.
)

echo.
echo Press any key to exit... & pause >nul