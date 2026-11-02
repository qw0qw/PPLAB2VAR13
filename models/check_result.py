from dataclasses import dataclass

from typing import Optional

from models.card_type import CardType



@dataclass
class CheckResult:
    """Результат проверки банковской карты."""

    last_four: str
    card_type: Optional[CardType]
    is_valid: bool
    reason: str
    position: Optional[int] = None

    def __str__(self) -> str:
        """Возвращает краткое представление результата."""
        verdict = "Может существовать" if self.is_valid else "Не может существовать"
        return f"*{self.last_four} — {verdict}"