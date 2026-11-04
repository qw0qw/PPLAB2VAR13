def mask_card(number: str) -> str:
    """Маскирует номер карты, оставляя последние четыре цифры."""

    digits = "".join(
        char for char in number
        if char.isdigit()
    )

    if len(digits) < 4:
        return "*" * len(digits)

    return "*" * (len(digits) - 4) + digits[-4:]