import unittest

from models.card_type import CardType
from services.card_validator import validate_card


class TestCardValidator(unittest.TestCase):

    def test_valid_visa(self):
        result = validate_card("4111111111111111")

        self.assertTrue(result.is_valid)
        self.assertEqual(result.card_type, CardType.VISA)

    def test_valid_mastercard(self):
        result = validate_card("5555555555554444")

        self.assertTrue(result.is_valid)
        self.assertEqual(result.card_type, CardType.MASTERCARD)

    def test_valid_unionpay(self):
        result = validate_card("6200000000000000")

        self.assertTrue(result.is_valid)
        self.assertEqual(result.card_type, CardType.UNIONPAY)

    def test_invalid_luhn(self):
        result = validate_card("4111111111111112")

        self.assertFalse(result.is_valid)
        self.assertEqual(result.reason, "Неверная контрольная сумма")

    def test_invalid_format(self):
        result = validate_card("1234567890123456")

        self.assertFalse(result.is_valid)
        self.assertIsNone(result.card_type)

    def test_spaces_and_hyphens(self):
        result = validate_card("4111 1111-1111 1111")

        self.assertTrue(result.is_valid)
        self.assertEqual(result.card_type, CardType.VISA)


if __name__ == "__main__":
    unittest.main()