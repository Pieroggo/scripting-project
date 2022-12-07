@echo off
setlocal enabledelayedexpansion
set year=%date:~6,4%
set month=%date:~3,2%
set day=%date:~0,2%
set hours=%time:~0,2%
if %hours% lss 10 (set hours=0%time:~1,1%)
set minute=%time:~3,2%
set second=%time:~6,2%
set msecond=%time:~9,2%
set name=%day%%month%%year%_%hours%%minute%%second%
echo %name%
copy backup.txt backup
copy report.html backup 
copy style.css backup
pushd backup
ren backup.txt %name%.txt
ren report.html %name%.html
popd 