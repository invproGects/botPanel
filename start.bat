@echo off
call .venv\Scripts\activate

start cmd /k "python main.py"
start cmd /k "python server.py"