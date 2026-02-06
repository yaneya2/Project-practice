#!/bin/bash
# Скрипт для запуска тестов системы на основе LLM

echo "Запуск тестов для системы на основе LLM..."

# Переход в директорию с тестами
cd /workspace/tests

# Запуск всех тестов в папке
python3 -m unittest discover -s . -p "test_*.py" -v

echo "Тесты завершены."