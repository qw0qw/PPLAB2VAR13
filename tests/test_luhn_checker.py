import unittest

from services.luhn_checker import check_luhn


class TestLuhnChecker(unittest.TestCase):
    """Тесты алгоритма Луна."""

    def test_valid_number(self):
        """Проверяет номер с правильной контрольной суммой."""
        self.assertTrue(check_luhn("4111111111111111"))

    def test_invalid_number(self):
        """Проверяет номер с неправильной контрольной суммой."""
        self.assertFalse(check_luhn("4111111111111112"))

    def test_another_valid_number(self):
        """Проверяет ещё один номер с правильной контрольной суммой."""
        self.assertTrue(check_luhn("5555555555554444"))

    def test_empty_number(self):
        """Проверяет обработку пустой строки."""
        self.assertTrue(check_luhn(""))


if __name__ == "__main__":
    unittest.main()