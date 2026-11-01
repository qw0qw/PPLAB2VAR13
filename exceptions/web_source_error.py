from exceptions.app_error import AppError


class WebSourceError(AppError):
    """Ошибка получения данных из веб-источника."""

    def __init__(
        self,
        message: str = "Ошибка получения веб-страницы"
    ):
        super().__init__(message)