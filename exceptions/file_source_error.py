from exceptions.app_error import AppError


class FileSourceError(AppError):
    """Ошибка при чтении или обработке файла."""

    def __init__(
        self,
        message: str = "Ошибка работы с файлом"
    ):
        super().__init__(message)