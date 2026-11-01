from exceptions.app_error import AppError


class HistoryError(AppError):
    """Ошибка при работе с историей проверок."""

    def __init__(
        self,
        message: str = "Ошибка работы с историей"
    ):
        super().__init__(message)