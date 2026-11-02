import unittest

from models.card_type import CardType
from models.check_result import CheckResult


class TestCardType(unittest.TestCase):
    """Проверяет, правильно ли записаны названия карт."""

    def test_card_types(self):
        self.assertEqual(CardType.VISA.value, "Visa")
        self.assertEqual(CardType.MASTERCARD.value, "MasterCard")
        self.assertEqual(CardType.MIR.value, "Мир")
        self.assertEqual(CardType.AMERICAN_EXPRESS.value, "American Express")
        self.assertEqual(CardType.UNIONPAY.value, "UnionPay")


class TestCheckResult(unittest.TestCase):

    def test_valid_result(self):
        result = CheckResult(
            last_four="1234",
            card_type=CardType.VISA,
            is_valid=True,
            reason="Проверка пройдена"
        )

        self.assertEqual(result.last_four, "1234")
        self.assertEqual(result.card_type, CardType.VISA)
        self.assertTrue(result.is_valid)

    def test_invalid_result(self):
        result = CheckResult(
            last_four="5678",
            card_type=None,
            is_valid=False,
            reason="Неверный формат"
        )

        self.assertFalse(result.is_valid)
        self.assertIsNone(result.card_type)

    def test_string_representation(self):
        result = CheckResult(
            last_four="1234",
            card_type=CardType.VISA,
            is_valid=True,
            reason="Проверка пройдена"
        )

        self.assertEqual(str(result), "*1234 — Может существовать")


if __name__ == "__main__":
    unittest.main()