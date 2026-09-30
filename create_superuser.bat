@echo off
REM Script to create a Django superuser for admin access

echo ========================================
echo Create Django Superuser
echo ========================================
echo.
echo You will be prompted to enter:
echo - Username
echo - Email (optional)
echo - Password
echo.
py manage.py createsuperuser
echo.
echo ========================================
echo Superuser created successfully!
echo ========================================
echo.
echo You can now login at: http://127.0.0.1:8000/admin/login/
echo.
pause