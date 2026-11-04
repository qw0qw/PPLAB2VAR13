from services.input_splitter import extract_candidates
from services.card_validator import validate_card


def find_cards(text: str):
    """Находит и проверяет номера карт в тексте."""

    candidates = extract_candidates(text)

    results = []

    for candidate in candidates:
        result = validate_card(candidate)
        results.append(result)

    return results