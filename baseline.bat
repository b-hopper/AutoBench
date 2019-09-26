@echo off

net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Failed; Run as administrator
    pause
    EXIT
)

if not {%1} == {} (
    SET /A n = %1
) else (
    SET /A n = 3
)

cd /d %~dp0
reg query "hkcu\software\Python"
if %errorLevel% == 0 (
    cd baseline

    rem One of these installers will work... Don't need both.
    rem Attempting to install both because I want to cover all bases.
    rem If the install fails, script will continue, so all good there
    rem If pywin32 is already installed, it will let us know, and continue anyway
    
    py -m pip install installers/pywin32-224-cp37-cp37m-win_amd64.whl
    py -m pip install installers/pywin32-224-cp37-cp37m-win32.whl
        
    baseline.py %n%
    if exist \\readyshare\USB_Storage\ xcopy /s results \\readyshare\USB_Storage\benchmarks\baseline\
) else (
    rem Install python and try again

    %~dp0/baseline/installers/python-3.7.4.exe /quiet
    echo Python 3.7.4 installed - restarting .bat file
    baseline.bat
)    
pause