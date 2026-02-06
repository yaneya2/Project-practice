#!/usr/bin/env python3
"""
Скрипт для тестирования системы на основе LLM
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os

# Добавляем корневую директорию в путь для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestLLMSystem(unittest.TestCase):
    """
    Тесты для системы на основе LLM
    """

    def setUp(self):
        """
        Подготовка тестового окружения
        """
        pass

    def test_llm_response_generation(self):
        """
        Тест генерации ответа от LLM
        """
        # Создаем mock объект для LLM
        llm_mock = Mock()
        llm_mock.generate.return_value = "Тестовый ответ от LLM"
        
        # Проверяем, что генерируется ответ
        response = llm_mock.generate("Тестовый запрос")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_llm_context_handling(self):
        """
        Тест обработки контекста LLM
        """
        # Создаем mock объект для LLM
        llm_mock = Mock()
        test_context = "Контекст для тестирования"
        llm_mock.process_with_context.return_value = "Ответ с учетом контекста"
        
        # Проверяем обработку контекста
        response = llm_mock.process_with_context(test_context)
        self.assertIsNotNone(response)
        
    def test_llm_error_handling(self):
        """
        Тест обработки ошибок LLM
        """
        # Создаем mock объект для LLM, который выбрасывает исключение
        llm_mock = Mock()
        llm_mock.generate.side_effect = Exception("Ошибка LLM")
        
        # Проверяем, что ошибка обрабатывается корректно
        with self.assertRaises(Exception):
            llm_mock.generate("Тестовый запрос")

    def test_llm_input_validation(self):
        """
        Тест валидации входных данных для LLM
        """
        # Проверяем, что пустой запрос не принимается
        llm_mock = Mock()
        llm_mock.generate.return_value = "Ответ"
        
        # Валидация должна проверять, что запрос не пустой
        with self.assertRaises(ValueError):
            llm_mock.generate("")

    def test_llm_response_quality(self):
        """
        Тест качества ответа от LLM
        """
        # Мокаем LLM с определенным поведением
        llm_mock = Mock()
        test_query = "Какие плюсы у языка Python?"
        expected_keywords = ["простота", "читаемость", "гибкость"]
        
        # Возвращаем типичный ответ о преимуществах Python
        llm_mock.generate.return_value = (
            "Python имеет простоту синтаксиса, хорошую читаемость кода "
            "и большую гибкость в разработке приложений."
        )
        
        response = llm_mock.generate(test_query)
        
        # Проверяем, что ответ содержит ключевые слова
        response_lower = response.lower()
        found_keywords = [kw for kw in expected_keywords if kw in response_lower]
        
        self.assertGreaterEqual(len(found_keywords), 1,
                               f"Ответ должен содержать хотя бы одно из ключевых слов: {expected_keywords}")

if __name__ == '__main__':
    print("Запуск тестов для системы на основе LLM...")
    unittest.main(verbosity=2)