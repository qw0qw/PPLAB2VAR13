from enum import Enum


class CardType(Enum):
    """Поддерживаемые платёжные системы."""

    VISA = "Visa"
    MASTERCARD = "MasterCard"
    MIR = "Мир"
    AMERICAN_EXPRESS = "American Express"
    UNIONPAY = "UnionPay" #iskl lun