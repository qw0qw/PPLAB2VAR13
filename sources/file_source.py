from pathlib import Path

from sources.base import BaseSource
from exceptions.file_source_error import FileSourceError


class FileSource(BaseSource):
    """Источник текста из локального файла."""

    def __init__(self, path: str):
        self.path = Path(path)

    def read(self) -> str:
        """Читает содержимое файла."""

        try:
            with self.path.open("r", encoding="utf-8") as file:
                return file.read()

        except (OSError, UnicodeError) as error:
            raise FileSourceError(
                f"Не удалось прочитать файл: {error}"
            ) from error