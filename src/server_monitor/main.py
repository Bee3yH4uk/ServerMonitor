from src.server_monitor.checker import Checker
from src.server_monitor.csv_parser import check_csv


def start_parse(file_path, ignore_errors=False):
    """
        Эта функция предназначена для запуска проверки доменов и ip адресов.

        Аргументы:
            file_path (str): путь к файлу csv.
            ignore_errors (bool): игнорировать ошибки при запуске.

        Возвращает:
            0, если файл не прошел проверку.
    """
    input_data = check_csv(file_path, ignore_errors=ignore_errors)
    if not input_data:
        input('[INPUT] Нажмите Enter, чтобы закрыть программу.')
        return 0
    CurrentChecker = Checker(input_data)
    CurrentChecker.start()
