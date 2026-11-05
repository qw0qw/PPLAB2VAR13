from pathlib import Path

from exceptions.history_error import HistoryError


class HistoryStorage:
    """Хранит историю проверок банковских карт."""

    def __init__(self, path="data/history.txt"):
        self.path = Path(path)

    def save_result(self, result):
        """Сохраняет результат проверки."""

        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)

            with self.path.open("a", encoding="utf-8") as file:
                file.write(str(result) + "\n")

        except OSError as error:
            raise HistoryError(
                f"Не удалось сохранить историю: {error}"
            ) from error

    def get_history(self):
        """Возвращает историю проверок."""

        if not self.path.exists():
            return []

        try:
            with self.path.open("r", encoding="utf-8") as file:
                return [
                    line.strip()
                    for line in file
                    if line.strip()
                ]

        except OSError as error:
            raise HistoryError(
                f"Не удалось прочитать историю: {error}"
            ) from error