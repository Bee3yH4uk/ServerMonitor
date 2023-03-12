from datetime import datetime

from src.server_monitor.utils.network import get_id_addresses_from_domain, check_ports_ip, check_ip_by_ping, \
    server_availability_check


class Domain():
    """
        Класс Domain предоставляет пользователю инструмент для проверки доступности сервера,
        используя доменное имя или IP-адрес.
        Он предоставляет данные о статусе портов и скорости пинга для каждого IP-адреса и
        анализирует статусы подключения к серверу.

         Аргументы:
            domain (str): доменное имя.
            ip_addresses (list): список IP адресов.
            ports (list): список портов

    """
    def __init__(self, domain=None, ip_addresses=None, ports=None):
        self.domain = domain
        self.ip_addresses = ip_addresses
        self.ports = ports
        self.valid = True
        self.check_domain()

    def check_domain(self):
        """
            Функция проверяет доменное имя и получает IP-адреса связанные с доменным именем.
        """
        if not self.domain and not self.ip_addresses:
            self.valid = False
            return 0
        if self.domain:
            if not self.get_ips():
                return 0

    def get_ips(self):
        """
            Функция получает IP-адреса связанные с доменным именем.
        """
        ip_address = get_id_addresses_from_domain(self.domain)
        self.ip_addresses = ip_address
        if not ip_address:
            print('[ERROR] DNS сервер не возвращает IP-адрес по доменному имени', self.domain)
            return 0

    def check_ip_connection(self, ports_status):
        """
            Функция проверяет состояние портов и соединение с сервером.

            Аргументы:
                ports_status (dict) Словарь со статусом портов.
        """
        errors = ""
        if ports_status[443]['status'] != 'Opened':
            errors += 'Порт 433 закрыт;'
        if ports_status[80]['status'] != 'Opened':
            errors += 'Порт 80 закрыт;'
            errors += 'IP-адрес сервера недоступен;'
        if self.domain:
            status = server_availability_check(self.domain)
            if status != 1:
                errors += status
        if errors:
            print(errors)

    def check_all_ips(self):
        """
            Функция проверяет все IP-адреса для домена и порты.

            Возвращаемое значение:
                output (str) Строка с данными о проверке.
        """
        if not self.valid:
            return 0

        output = ""
        for ip_address in self.ip_addresses:
            ports_status = check_ports_ip(ip_address, self.ports)
            for port in self.ports if self.ports else [-1]:
                if port == -1:
                    rtt = check_ip_by_ping(ip_address)
                else:
                    rtt = ports_status[port]['rtt']
                output += f"{datetime.now()} | {self.domain} | {ip_address} | " \
                          f"{rtt:0.2f} ms | {port} | " \
                          f"{ports_status[port]['status'] if port in ports_status else '???'}\n"
                self.check_ip_connection(ports_status)
        return output
