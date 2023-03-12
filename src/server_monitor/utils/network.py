import socket
import time

import pythonping
import requests


def check_port(ip, port):
    """
        Функция проверяет доступность порта на IP-адресе.

        Аргументы:
            ip (str): IP-адрес для проверки.
            port (int): Номер порта для проверки.

        Возвращаемое значение:
            dict: Словарь с ключами 'status' и 'rtt', где 'status' указывает на статус порта
            (открыт/закрыт) и 'rtt' - время ответа в миллисекундах.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        _start_time = time.time()
        s.settimeout(2)
        result = s.connect_ex((ip, int(port)))
        _finish_time = time.time()
        if result == 0:
            return {"status": "Opened", "rtt": (_finish_time - _start_time) * 1000}
        else:
            return {"status": "Not opened", "rtt": (_finish_time - _start_time) * 1000}


def get_id_addresses_from_domain(hostname):
    """
        Функция возвращает список IP-адресов, связанных с доменным именем.

        Аргумент:
            hostname (str): доменное имя
        Возвращаемое значение:
            list: список IP-адресов, связанных с доменным именем, или 0, если произошла ошибка.
    """
    try:
        addresses = []
        for address in socket.getaddrinfo(hostname, 0):
            addresses.append(address[4][0])
        if '::1' in addresses:
            addresses.remove('::1')
        return addresses
    except Exception as E:
        print(E)
        return 0


def check_ports_ip(ip, port_list):
    """
        Функция проверяет доступность портов на IP-адресе.

        Аргументы:
            ip (str): IP-адрес для проверки.
            port_list (list): Список портов для проверки.

        Возвращаемое значение:
            dict: Словарь с ключами, равными портам из списка 'port_list', а значениями словари с
            ключами 'status' и 'rtt', где 'status' указывает на статус порта
            (открыт/закрыт) и 'rtt' - время ответа в миллисекундах.
    """
    ports = {443: {}, 80: {}}
    for port in port_list:
        if port not in ports:
            ports[port] = {}
    for port in ports.keys():
        ports[port] = check_port(ip, port)
    return ports


def check_ip_by_ping(ip):
    """
        Функция проверяет доступность IP-адреса по пингу.

        Аргументы:
            ip (str): IP-адрес для проверки.

        Возвращаемое значение:
            float: Время ответа в миллисекундах.
    """
    ping_info = pythonping.ping(ip)
    return ping_info.rtt_avg_ms


def check_net_connection():
    """
        Функция проверяет доступность Интернета.

        Аргументы:
            Отсутствуют.

        Возвращаемое значение:
            bool: True - если Интернет доступен, False - в противном случае.
    """
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def server_availability_check(domain_name):
    """
        Функция проверяет доступность сервера по имени домена.

        Аргументы:
            domain_name (str): имя домена, например, 'google.com'

        Возвращает:
            int: 1, если запрос прошел успешно
            str: сообщение об ошибке, если произошла ошибка
    """
    try:
        r = requests.get(f'https://{domain_name}')
        if r.ok:
            return 1
        else:
            return f"Ошибка сервера: {r}"
    except TimeoutError:
        return 'TimeOut ошибка сервера'
    except Exception as E:
        return f'Ошибка запроса к серверу {E}'
