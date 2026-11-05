from abc import ABC, abstractmethod


class BaseSource(ABC):
    """Базовый интерфейс источника текста."""

    @abstractmethod
    def read(self) -> str:
        """Возвращает текст из источника."""
        pass