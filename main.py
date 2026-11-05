from history_storage import HistoryStorage
from services.card_validator import validate_card
from services.card_finder import find_cards
from sources.file_source import FileSource
from sources.web_source import WebSource

from exceptions.file_source_error import FileSourceError
from exceptions.web_source_error import WebSourceError
from exceptions.history_error import HistoryError


history = HistoryStorage()


def show_results(results):
    """Выводит результаты проверки."""

    if not results:
        print("Номера не найдены.")
        return

    for result in results:
        card_type = (
            result.card_type.value
            if result.card_type
            else "Неизвестно"
        )

        print(
            f"{result} | "
            f"Тип: {card_type} | "
            f"{result.reason}"
        )

        try:
            history.save_result(result)
        except HistoryError as error:
            print(error)


def check_one_card():
    """Проверяет один номер."""

    number = input("Введите номер карты: ").strip()

    if not number:
        print("Пустой ввод.")
        return

    result = validate_card(number)
    show_results([result])


def search_in_text():
    """Ищет номера в пользовательском тексте."""

    text = input("Введите текст: ")

    if not text.strip():
        print("Пустой ввод.")
        return

    results = find_cards(text)
    show_results(results)


def search_in_file():
    """Ищет номера в локальном файле."""

    path = input("Введите путь к файлу: ").strip()

    try:
        source = FileSource(path)
        text = source.read()

        results = find_cards(text)
        show_results(results)

    except FileSourceError as error:
        print(error)


def search_on_web():
    """Ищет номера на веб-странице."""

    url = input("Введите URL страницы: ").strip()

    try:
        source = WebSource(url)
        text = source.read()

        results = find_cards(text)
        show_results(results)

    except WebSourceError as error:
        print(error)


def show_history():
    """Показывает историю проверок."""

    try:
        records = history.get_history()

        if not records:
            print("История пуста.")
            return

        print("\nИстория проверок:")

        for record in records:
            print(record)

    except HistoryError as error:
        print(error)


def main():
    """Запускает главное меню."""

    while True:
        print("\n===== Проверка банковских карт =====")
        print("1. Проверить один номер")
        print("2. Найти номера в тексте")
        print("3. Найти номера в файле")
        print("4. Найти номера на веб-странице")
        print("5. Показать историю")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            check_one_card()
        elif choice == "2":
            search_in_text()
        elif choice == "3":
            search_in_file()
        elif choice == "4":
            search_on_web()
        elif choice == "5":
            show_history()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Некорректный пункт меню.")


if __name__ == "__main__":
    main()
