@echo off
REM Setup and Run Flask IP Resolver

echo.
echo === Checking virtual environment ===
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

echo.
echo === Activating virtual environment ===
call venv\Scripts\activate

echo.
echo === Installing required packages ===
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo === Starting Flask App ===
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

echo.
pause
