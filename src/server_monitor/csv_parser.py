import csv
from pprint import pprint

from .utils.domain import Domain
from .utils.validation import check_ports, is_valid_ip, is_valid_domain


def check_row(row: list):
    """
        Функция проверяет входные данные строки из CSV файла на корректность.
        Для проверки используются следующие условия:
            - Количество элементов должно быть равно двум
            - Первый элемент должен быть непустым
            - Если первый элемент является IP адресом, он должен быть корректным
            - Если первый элемент является доменным именем, он должен быть корректным
            - Второй элемент должен быть корректным списком портов

        Аргументы:
        row (list) - строка из CSV файла

        Возвращаемое значение:
        output (list) - список с проверенными данными
    """
    if len(row) != 2:
        print('Некорректный формат данных', row)
        return 0
    if not row[0]:
        print('Некорректный формат данных', row)
        return 0
    if row[0] == 'Host' and row[1] == 'Ports':
        return 1
    port_list = check_ports(row[1])
    if port_list == 0:
        return 0
    domain_name, ip_address = None, None
    if is_valid_ip(row[0]):
        ip_address = [row[0]]
    else:
        domain_name = row[0]
        if not is_valid_domain(domain_name):
            print('Домен указан неверно', row)
            return 0

    return Domain(domain_name, ip_address, port_list)


def check_csv(file_path: str, ignore_errors: bool = False):
    """
        Функция производит проверку входных данных из CSV файла и возвращает список с проверенными данными.
        Для проверки используется функция check_row.

        Аргумент:
        file_path (str) - путь до файла
        ignore_errors (bool) - игнорирование ошибок

        Возвращаемое значение:
        output (list) - список с проверенными данными
    """
    output = []
    try:
        with open(file_path) as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                checked_row = check_row(row)
                if checked_row == 1:
                    continue
                if checked_row:
                    output.append(checked_row)
                else:
                    if not ignore_errors:
                        print('Входные данные указаны неверно!')
                        return 0
    except Exception as E:
        print('Ошибка чтения csv файла', E)
        return 0
    return output
