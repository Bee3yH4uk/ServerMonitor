from datetime import datetime

from .csv_parser import check_csv
from .utils.domain import Domain
from .utils.network import check_net_connection


class Checker():
    """
        Этот класс предназначен для проверки состояния доменов и ip адресов.

        Аргументы:
            domains_to_check (list): список с доменами.

        Атрибуты:
            data (list): список с элементами [домен, ip-адреса, порты].
            active (bool): активность класса.
    """

    def __init__(self, domains_to_check):
        self.data = domains_to_check
        self.active = True

    def check_ip(self, CurrentDomain: Domain):
        """
            Функция проверяет доступность IP-адресов и портов

            Аргументы:
                CurrentDomain (utils.Domain): Класс описывающий домен

            Возвращает:
                статус доступности IP-адресов и портов
        """
        if not check_net_connection():
            print('[ERROR] Соединение с интернетом потеряно')
            return 0
        print([CurrentDomain.domain, CurrentDomain.ip_addresses, CurrentDomain.ports])
        result_check = CurrentDomain.check_all_ips()
        if result_check:
            print(result_check)

    def cycle_check(self):
        """
            Функция для периодической проверки доступности сайтов
        """
        for CurrentDomain in self.data:
            self.check_ip(CurrentDomain)

    def start(self):
        """
            Функция для запуска проверки доступности сайтов
        """
        print("[INFO] Запущена проверка IP адресов\n")
        while True:
            print('#'* 60)
            self.cycle_check()


    def stop(self):
        """
            Функция для остановки проверки доступности сайтов
        """
        self.active = False
