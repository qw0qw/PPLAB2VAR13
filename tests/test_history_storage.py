import tempfile
import unittest
from pathlib import Path

from history_storage import HistoryStorage
from models.card_type import CardType
from models.check_result import CheckResult


class TestHistoryStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "history.txt"
        self.storage = HistoryStorage(self.path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_result(self):
        result = CheckResult(
            last_four="1234",
            card_type=CardType.VISA,
            is_valid=True,
            reason="Проверка пройдена"
        )

        self.storage.save_result(result)

        history = self.storage.get_history()

        self.assertEqual(len(history), 1)
        self.assertIn("*1234", history[0])

    def test_empty_history(self):
        self.assertEqual(self.storage.get_history(), [])

    def test_multiple_results(self):
        for number in ["1234", "5678"]:
            result = CheckResult(
                last_four=number,
                card_type=CardType.VISA,
                is_valid=True,
                reason="Проверка пройдена"
            )
            self.storage.save_result(result)

        self.assertEqual(len(self.storage.get_history()), 2)


if __name__ == "__main__":
    unittest.main()