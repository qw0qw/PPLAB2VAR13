from models.card_type import CardType
from models.check_result import CheckResult
from services.card_patterns import CARD_PATTERNS
from services.luhn_checker import check_luhn


def validate_card(number: str) -> CheckResult:
    """Определяет платёжную систему и проверяет номер карты."""

    number = number.replace(" ", "").replace("-", "")

    for card_type, pattern in CARD_PATTERNS.items():
        if pattern.fullmatch(number):
            last_four = number[-4:]

            if card_type != CardType.UNIONPAY and not check_luhn(number):
                return CheckResult(
                    last_four=last_four,
                    card_type=card_type,
                    is_valid=False,
                    reason="Неверная контрольная сумма"
                )

            return CheckResult(
                last_four=last_four,
                card_type=card_type,
                is_valid=True,
                reason="Проверка пройдена"
            )

    return CheckResult(
        last_four=number[-4:] if len(number) >= 4 else number,
        card_type=None,
        is_valid=False,
        reason="Неизвестная платёжная система или неверный формат"
    )