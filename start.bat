@echo off
chcp 65001 > nul

:: Пробуем запустить через python
python process_prompts.py
if %ERRORLEVEL% EQU 0 goto end

:: Если не получилось, пробуем через py
py process_prompts.py
if %ERRORLEVEL% EQU 0 goto end

:: Пробуем запустить напрямую через путь к Python
c:\python311\python.exe process_prompts.py
if %ERRORLEVEL% EQU 0 goto end

:: Если Python не найден
echo ╔═══════════════════════════════════════╗
echo ║           ОШИБКА: Python не найден    ║
echo ║     Установите Python с python.org    ║
echo ╚═══════════════════════════════════════╝
pause
exit /b 1

:end
pause