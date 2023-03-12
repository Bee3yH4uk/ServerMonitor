import re


def is_valid_domain(domain):
    """
        Функция проверяет корректность доменного имени.

        Аргумент:
            domain (str): доменное имя
        Возвращаемое значение:
            bool: True, если доменное имя корректно, иначе False.
    """
    if domain == 'localhost':
        return True
    domain_regex = r'[a-z0-9]+(?:-[a-z0-9]+)*\.[a-z]{2,}$'
    if re.fullmatch(domain_regex, domain):
        return True
    else:
        return False


def is_valid_ip(ip):
    """
        Функция проверяет корректность IP-адреса.

        Аргумент:
            ip (str): IP-адрес
        Возвращаемое значение:
            bool: True, если IP-адрес корректный, иначе False.
    """
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True


def check_ports(ports):
    """
        Функция проверяет корректность указанных портов.

        Аргумент:
            ports (str): порты, разделённые запятыми
        Возвращаемое значение:
            list: список корректных портов, или 0, если порт указан неверно.
    """
    result = []
    if not ports:
        return []
    ports = ports.split(',')
    for port in ports:
        if not port.isdigit():
            print(f'Порт {port} указан неверно')
            continue
            # return 0
        port = int(port)
        if 0 < port < 65536:
            result.append(port)
        else:
            print(f'Порт {port} указан неверно')
            # return 0
    return result
