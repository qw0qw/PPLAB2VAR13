import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):

    @patch("builtins.input", side_effect=["0"])
    def test_exit(self, _):
        main.main()

    @patch("builtins.input", side_effect=["9", "0"])
    def test_invalid_choice(self, _):
        main.main()

    @patch("builtins.input", side_effect=["   "])
    def test_empty_card(self, _):
        main.check_one_card()

    @patch("builtins.input", side_effect=["   "])
    def test_empty_text(self, _):
        main.search_in_text()

    @patch("builtins.input", side_effect=["missing_file.txt"])
    def test_missing_file(self, _):
        main.search_in_file()

    @patch("builtins.input", side_effect=["bad-url"])
    def test_bad_url(self, _):
        main.search_on_web()


if __name__ == "__main__":
    unittest.main()
