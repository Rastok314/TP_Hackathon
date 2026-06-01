@echo off
setlocal

cd /d "%~dp0"

echo === CHECK VENV ===

if not exist venv\Scripts\python.exe (
    echo === Creating virtual environment ===
    rmdir /s /q venv
    py -m venv venv
)

echo === Installing dependencies ===
venv\Scripts\python.exe -m pip install -r requirements.txt

if "%1"=="start" goto start
if "%1"=="test" goto test

echo Usage:
echo   run.bat start
echo   run.bat test
goto end

:start
echo === STARTING APP ===
venv\Scripts\python.exe -m src.main
goto end

:test
echo === RUNNING TESTS ===
venv\Scripts\python.exe -m pytest -q
goto end

:end
endlocal
pause