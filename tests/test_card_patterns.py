import unittest

from models.card_type import CardType
from services.card_patterns import CARD_PATTERNS


class TestCardPatterns(unittest.TestCase):

    def test_visa(self):
        self.assertIsNotNone(CARD_PATTERNS[CardType.VISA].match("4111111111111111"))
        self.assertIsNone(CARD_PATTERNS[CardType.VISA].match("5111111111111111"))
        self.assertIsNone(CARD_PATTERNS[CardType.VISA].match("411111111111111"))

    def test_mastercard(self):
        pattern = CARD_PATTERNS[CardType.MASTERCARD]

        self.assertIsNotNone(pattern.match("5111111111111111"))
        self.assertIsNotNone(pattern.match("2221000000000000"))
        self.assertIsNotNone(pattern.match("2720000000000000"))
        self.assertIsNone(pattern.match("5011111111111111"))
        self.assertIsNone(pattern.match("2721000000000000"))

    def test_mir(self):
        pattern = CARD_PATTERNS[CardType.MIR]

        self.assertIsNotNone(pattern.match("2200000000000000"))
        self.assertIsNotNone(pattern.match("2204000000000000"))
        self.assertIsNone(pattern.match("2205000000000000"))

    def test_american_express(self):
        pattern = CARD_PATTERNS[CardType.AMERICAN_EXPRESS]

        self.assertIsNotNone(pattern.match("340000000000000"))
        self.assertIsNotNone(pattern.match("370000000000000"))
        self.assertIsNone(pattern.match("360000000000000"))

    def test_unionpay(self):
        pattern = CARD_PATTERNS[CardType.UNIONPAY]

        self.assertIsNotNone(pattern.match("6200000000000000"))
        self.assertIsNone(pattern.match("6100000000000000"))
        self.assertIsNone(pattern.match("620000000000000"))


if __name__ == "__main__":
    unittest.main()