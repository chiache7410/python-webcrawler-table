@echo off
if "%1%"=="" (
echo �ХN�J�ɮ׸��|
goto end
)
dir htmltemp1 >nul
if %ERRORLEVEL%==0 python webGetTabel2csv.py %1% N
if %ERRORLEVEL%==1 python webGetTabel2csv.py %1% Y
:end
pause