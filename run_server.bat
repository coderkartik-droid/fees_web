@echo off
REM Script to run the Django development server

echo Starting Django development server...
echo.
echo The application will be available at: http://127.0.0.1:8000
echo.
echo Upload page: http://127.0.0.1:8000/upload/
echo Display page: http://127.0.0.1:8000/
echo.
echo Press Ctrl+C to stop the server
echo.

py manage.py runserver