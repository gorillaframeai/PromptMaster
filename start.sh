#!/bin/bash

# Установка UTF-8
export LANG=en_US.UTF-8

echo "╔═══════════════════════════════════════╗"
echo "║      PromptMaster by GorillaFrame     ║"
echo "║              Version 1.0.0            ║"
echo "╚═══════════════════════════════════════╝"

# Пробуем запустить через python3
if command -v python3 &> /dev/null; then
    python3 process_prompts.py
    if [ $? -eq 0 ]; then
        echo "Нажмите Enter для выхода..."
        read
        exit 0
    fi
fi

# Пробуем запустить через python
if command -v python &> /dev/null; then
    python process_prompts.py
    if [ $? -eq 0 ]; then
        echo "Нажмите Enter для выхода..."
        read
        exit 0
    fi
fi

# Если Python не найден
echo "╔═══════════════════════════════════════╗"
echo "║           ОШИБКА: Python не найден    ║"
echo "║     Установите Python с python.org    ║"
echo "╚═══════════════════════════════════════╝"
echo "Нажмите Enter для выхода..."
read
exit 1