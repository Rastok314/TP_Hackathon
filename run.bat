@echo off
cd /d %~dp0

echo === Installing dependencies ===
py -m pip install -r requirements.txt

if "%1"=="start" goto start
if "%1"=="test" goto test

echo Unknown command. Use:
echo   run.bat start
echo   run.bat test
goto end

:start
echo === STARTING APP ===
py src/main.py
goto end

:test
echo === RUNNING TESTS ===
py -m pytest
goto end

:end
pause