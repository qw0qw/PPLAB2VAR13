import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

from sources.file_source import FileSource
from sources.web_source import WebSource
from exceptions.file_source_error import FileSourceError
from exceptions.web_source_error import WebSourceError


class TestFileSource(unittest.TestCase):

    def test_read_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.txt"
            path.write_text("Тестовый текст", encoding="utf-8")

            source = FileSource(path)

            self.assertEqual(source.read(), "Тестовый текст")

    def test_missing_file(self):
        source = FileSource("missing_file.txt")

        with self.assertRaises(FileSourceError):
            source.read()


class TestWebSource(unittest.TestCase):

    @patch("sources.web_source.requests.get")
    def test_read_page(self, mock_get):
        response = Mock()
        response.text = "Тестовая веб-страница"
        response.raise_for_status.return_value = None

        mock_get.return_value = response

        source = WebSource("https://example.com")

        self.assertEqual(source.read(), "Тестовая веб-страница")

    @patch("sources.web_source.requests.get")
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.RequestException(
            "Ошибка соединения"
        )

        source = WebSource("https://example.com")

        with self.assertRaises(WebSourceError):
            source.read()

    def test_invalid_url(self):
        source = WebSource("incorrect-url")

        with self.assertRaises(WebSourceError):
            source.read()


if __name__ == "__main__":
    unittest.main()