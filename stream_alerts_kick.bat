@echo off
REM Uruchom FastAPI serwer
start "" python server.py

REM Uruchom ngrok
start "" ngrok http 8000

echo Serwer audio i ngrok uruchomione.
echo Otworz przegladarke lub telefon i wpisz link ngrok, ktory pojawi sie w nowym oknie terminala.
pause
