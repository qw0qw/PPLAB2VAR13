import unittest

from services.input_splitter import extract_candidates
from services.card_finder import find_cards
from models.card_type import CardType
from services.card_masker import mask_card


class TestInputSplitter(unittest.TestCase):

    def test_extract_number(self):
        text = "Номер: 4111111111111111"

        result = extract_candidates(text)

        self.assertEqual(result, ["4111111111111111"])

    def test_extract_multiple_numbers(self):
        text = "4111111111111111 и 5555555555554444"

        result = extract_candidates(text)

        self.assertEqual(len(result), 2)

    def test_extract_number_with_spaces(self):
        text = "4111 1111 1111 1111"

        result = extract_candidates(text)

        self.assertEqual(result, ["4111 1111 1111 1111"])

    def test_extract_number_with_hyphens(self):
        text = "4111-1111-1111-1111"

        result = extract_candidates(text)

        self.assertEqual(result, ["4111-1111-1111-1111"])

    def test_no_numbers(self):
        text = "Здесь нет номеров"

        result = extract_candidates(text)

        self.assertEqual(result, [])



class TestCardFinder(unittest.TestCase):

    def test_find_valid_card(self):
        text = "Карта: 4111111111111111"

        results = find_cards(text)

        self.assertEqual(len(results), 1)
        self.assertTrue(results[0].is_valid)
        self.assertEqual(results[0].card_type, CardType.VISA)

    def test_find_invalid_card(self):
        text = "Карта: 4111111111111112"

        results = find_cards(text)

        self.assertEqual(len(results), 1)
        self.assertFalse(results[0].is_valid)

    def test_find_multiple_cards(self):
        text = "4111111111111111 и 5555555555554444"

        results = find_cards(text)

        self.assertEqual(len(results), 2)

    def test_no_cards(self):
        text = "Обычный текст без номеров"

        results = find_cards(text)

        self.assertEqual(results, [])


class TestCardMasker(unittest.TestCase):

    def test_mask_number(self):
        self.assertEqual(
            mask_card("4111111111111111"),
            "************1111"
        )

    def test_mask_number_with_spaces(self):
        self.assertEqual(
            mask_card("4111 1111 1111 1111"),
            "************1111"
        )

    def test_short_number(self):
        self.assertEqual(mask_card("123"), "***")

    def test_empty_number(self):
        self.assertEqual(mask_card(""), "")



if __name__ == "__main__":
    unittest.main()