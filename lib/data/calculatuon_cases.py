from lib.tools.ip_tools import generate_valid_ip_without_cidr


class CaseBundle:
    def __init__(self, title, description, ip_with_cidr):
        self.title: str = title
        self.description: str = description
        self.ip_with_cidr: str = ip_with_cidr


def get_calculation_case():
    return [
        CaseBundle(
            title="Проверка наибольшей сети",
            description="Данный кейс проверяет вычисление наибольшей из возможных подсетей.",
            ip_with_cidr="0.0.0.0/0"
        ),
        CaseBundle(
            title="Проверка случайной сети с маской /32",
            description="Данный кейс проверяет вычисление случайной подсети с наименьшей из возможных масок.",
            ip_with_cidr=f"{generate_valid_ip_without_cidr()}/32"
        ),
    ]
