@echo off
setlocal

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run tests
echo Running tests...
pytest tests

if %ERRORLEVEL% NEQ 0 (
    echo Tests failed. Exiting...
    exit /b %ERRORLEVEL%
)

REM Run the main script
echo Running main script...
python src/main.py

endlocal