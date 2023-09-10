FastAPI Framework
py -3 -m venv venv
CTRL+Shift+P Select Python Interpreter -> Choose venv (.\venv\Scripts\Python.exe)
CMS -> .\venv\Scripts\activate.bat
FastAPI Tutorial - User Guide - Intro
pip install fastapi[all]

starting server (--reload is only during dev):
uvicorn posts_controller:app --reload 

# https://www.youtube.com/watch?v=0sOvCWFmrtA&list=WL&index=1