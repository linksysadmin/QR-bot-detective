#!/bin/bash
if ! command -v python3 &> /dev/null
then
    echo "Python не установлен. Установите Python и запустите скрипт снова."
    exit
fi
if [ -d ".venv" ]
then
    echo "Запуск QR Bot"
else
    echo "Установка QR Bot"
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

python3 main.py
