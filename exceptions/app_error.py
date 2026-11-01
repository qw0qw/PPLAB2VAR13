class AppError(Exception):
    """Базовое исключение приложения."""

    def __init__(self, message: str = "Ошибка приложения"):
        self.message = message
        super().__init__(self.message)