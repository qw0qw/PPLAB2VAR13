import re

from models.card_type import CardType

"""Словарь с шаблонами структур разных карт"""
CARD_PATTERNS = {
    CardType.VISA: re.compile(r"^4\d{15}$"),# Начинается с 4 и содержит ровно 16 цифр

    CardType.MASTERCARD: re.compile(
        r"^(5[1-5]\d{14}|(222[1-9]|22[3-9]\d|2[3-6]\d{2}|27[01]\d|2720)\d{12})$"
    ), # Начинается с 51-55 или 2221-2720, ровно 16 цифр

    CardType.MIR: re.compile(r"^220[0-4]\d{12}$"), # Начинается с 2200-2204, ровно 16 цифр

    CardType.AMERICAN_EXPRESS: re.compile(r"^3[47]\d{13}$"), # Начинается с 34 или 37, ровно 15 цифр

    CardType.UNIONPAY: re.compile(r"^62\d{14}$") # Начинается с 62, ровно 16 цифр
}