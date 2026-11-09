@echo off
setlocal
pushd "%~dp0"
py -3 main.py
set "drill_exit=%errorlevel%"
popd
exit /b %drill_exit%
