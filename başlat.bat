@echo off

rem Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python yüklü değil! Python'un yüklü olduğundan emin olun.
    pause
    exit
)

rem Python yüklü ise, koda devam et
pip install cryptography
pip install fernet
python deneme.py