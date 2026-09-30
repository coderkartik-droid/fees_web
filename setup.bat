@echo off
REM Setup script for Student Fees Management System
REM Run this script to set up the Django project

echo ========================================
echo Student Fees Management System Setup
echo ========================================
echo.

echo Step 1: Creating migrations...
py manage.py makemigrations fees_app
if %errorlevel% neq 0 (
    echo Error creating migrations
    pause
    exit /b 1
)

echo.
echo Step 2: Applying migrations...
py manage.py migrate
if %errorlevel% neq 0 (
    echo Error applying migrations
    echo.
    echo If you get migration errors due to model changes,
    echo delete db.sqlite3 and run this script again.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To run the server, execute: run_server.bat
echo Or manually run: py manage.py runserver
echo.
pause