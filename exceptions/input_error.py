from exceptions.app_error import AppError


class InputError(AppError):
    """Ошибка пользовательского ввода."""

    def __init__(
        self,
        message: str = "Некорректные входные данные"
    ):
        super().__init__(message)