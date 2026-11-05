from urllib.parse import urlparse

import requests

from sources.base import BaseSource
from exceptions.web_source_error import WebSourceError


class WebSource(BaseSource):
    """Источник текста из веб-страницы."""

    def __init__(self, url: str):
        self.url = url

    def read(self) -> str:
        """Получает содержимое веб-страницы."""

        parsed_url = urlparse(self.url)

        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            raise WebSourceError("Некорректный URL")

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            return response.text

        except requests.RequestException as error:
            raise WebSourceError(
                f"Не удалось получить страницу: {error}"
            ) from error