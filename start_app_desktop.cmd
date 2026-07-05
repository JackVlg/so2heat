@echo off
set WORKDIR=%cd%
set PYTHONPATH=%cd%
cd home
%WORKDIR%\.venv\Scripts\python.exe %WORKDIR%\home\app_desktop.py
cd ..

