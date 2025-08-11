import ipaddress
import random
from collections import namedtuple

from lib.data.localized_strings import LocalizedStrings


def generate_valid_ip_without_cidr() -> str:
    oc1 = random.randint(0, 255)
    oc2 = random.randint(0, 255)
    oc3 = random.randint(0, 255)
    oc4 = random.randint(0, 255)

    generated_ip_without_cidr = f"{oc1}.{oc2}.{oc3}.{oc4}"
    print("\nСгенерирован адрес:", generated_ip_without_cidr)

    return generated_ip_without_cidr


def generate_valid_ip_with_cidr() -> str:
    oc1 = random.randint(0, 255)
    oc2 = random.randint(0, 255)
    oc3 = random.randint(0, 255)
    oc4 = random.randint(0, 255)

    cidr = random.randint(0, 32)

    generated_ip_with_cidr = f"{oc1}.{oc2}.{oc3}.{oc4}/{cidr}"
    print("\nСгенерирован адрес:", generated_ip_with_cidr)

    return generated_ip_with_cidr


def ip_calculator(ip, locale=LocalizedStrings.EN):
    net = ipaddress.ip_network(ip, False)

    ip_address, cidr = ip.split("/")
    network_address = net.network_address

    broadcast_address = net.broadcast_address
    network_mask = net.netmask
    wildcard_mask = net.hostmask
    total_addresses = net.num_addresses

    total_hosts = total_addresses - 2
    if total_hosts <= 1:
        total_hosts = 0

    match locale.LANG:
        case 'EN':
            first_host = LocalizedStrings.EN.calculator_no_data
            last_host = LocalizedStrings.EN.calculator_no_data
        case 'RU':
            first_host = LocalizedStrings.RU.calculator_no_data
            last_host = LocalizedStrings.RU.calculator_no_data
        case 'KK':
            first_host = LocalizedStrings.KK.calculator_no_data
            last_host = LocalizedStrings.KK.calculator_no_data

        case _:
            raise ValueError("Недопустимая локализация")

    if total_addresses >= 3:
        first_host = net[1]

    if total_addresses >= 3:
        last_host = net[-2]

    print('IP адрес:', ip_address)
    print('CIDR нотация:', cidr)
    print('Маска подсети:', network_mask)
    print('Обратная маска:', wildcard_mask)
    print('Адрес сети:', network_address)
    print('Широковещательный адрес:', broadcast_address)
    print('Всего адресов:', total_addresses)
    print('Рабочих узлов:', total_hosts)
    print('Первый хост:', first_host)
    print('Последний хост:', last_host)

    calculated_network = namedtuple(
        'Network', ['ip_address', 'cidr', 'network_mask', 'wildcard_mask', 'network_address',
                    'broadcast_address', 'total_addresses', 'total_hosts', 'first_host', 'last_host'])

    return calculated_network(
        str(ip_address),
        str(cidr),
        str(network_mask),
        str(wildcard_mask),
        str(network_address),
        str(broadcast_address),
        str(total_addresses),
        str(total_hosts),
        str(first_host),
        str(last_host)
    )
