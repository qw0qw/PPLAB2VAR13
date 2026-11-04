import re


CARD_CANDIDATE_PATTERN = re.compile(
    r"(?<!\d)(?:\d[ -]?){12,18}\d(?!\d)"
)


def extract_candidates(text: str) -> list[str]:
    """Извлекает из текста возможные номера карт."""

    matches = CARD_CANDIDATE_PATTERN.findall(text)

    return [
        match.strip()
        for match in matches
    ]