import unittest

from services.input_splitter import extract_candidates


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


if __name__ == "__main__":
    unittest.main()