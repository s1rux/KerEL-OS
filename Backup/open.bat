@echo off
start /wait loader.exe
if %errorlevel% neq 0 (
    exit /b 1
)

start /wait main.exe
if %errorlevel% neq 0 (
    exit /b 1
)
