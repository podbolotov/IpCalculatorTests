from enum import Enum, auto


class AvailableLocales(Enum):
    EN = auto()
    RU = auto()
    KK = auto()
    DEFAULT = auto()


class LocalizedStrings:
    class EN:
        LANG = "EN"

        calculator_empty_state_text = "Waiting for data entry"
        calculate_button_label = "Calculate"
        share_button_label = "Share"

        bottom_navigation_bar_calculator = "Calculator"
        bottom_navigation_bar_info = "Info"
        bottom_navigation_bar_settings = "Settings"

        calculator_subnet_mask_dialog_title = "Choose subnet mask"

        calculator_subnet_mask = "Subnet mask"
        calculator_wildcard_mask = "Wildcard mask"
        calculator_network_ip_address = "Network address"
        calculator_broadcast_ip_address = "Broadcast address"
        calculator_max_possible_hosts = "Total number of addresses"
        calculator_usable_hosts = "Usable number of hosts"
        calculator_first_host = "First host address"
        calculator_last_host = "Last host address"
        calculator_ip_address = "IP address"
        calculator_cidr_prefix = "CIDR notation"
        calculator_no_data = "No data"

    class RU:
        LANG = "RU"

        calculator_empty_state_text = "Ожидание ввода данных"
        calculate_button_label = "Вычислить"
        share_button_label = "Поделиться"

        bottom_navigation_bar_calculator = "Калькулятор"
        bottom_navigation_bar_info = "Инфо"
        bottom_navigation_bar_settings = "Настройки"

        calculator_subnet_mask_dialog_title = "Выберите маску подсети"

        calculator_subnet_mask = "Маска подсети"
        calculator_wildcard_mask = "Обратная маска подсети (wildcard mask)"
        calculator_network_ip_address = "IP адрес сети"
        calculator_broadcast_ip_address = "Широковещательный адрес"
        calculator_max_possible_hosts = "Количество доступных адресов в порции хоста"
        calculator_usable_hosts = "Количество рабочих адресов для хостов"
        calculator_first_host = "IP адрес первого хоста"
        calculator_last_host = "IP адрес последнего хоста"
        calculator_ip_address = "IP адрес"
        calculator_cidr_prefix = "CIDR нотация"
        calculator_no_data = "Нет данных"

    class KK:
        LANG = "KK"

        calculator_empty_state_text = "Деректер енгізіңіз"
        calculate_button_label = "Есептеу"
        share_button_label = "Бөлісу"

        bottom_navigation_bar_calculator = "Калькулятор"
        bottom_navigation_bar_info = "Ақпарат"
        bottom_navigation_bar_settings = "Баптаулар"

        calculator_subnet_mask_dialog_title = "Желі маскасын таңдаңыз"

        calculator_subnet_mask = "Желі маскасы"
        calculator_wildcard_mask = "Кері маска (wildcard mask)"
        calculator_network_ip_address = "Желінің IP мекенжайы"
        calculator_broadcast_ip_address = "Кең ауқымды желінің мекенжайы"
        calculator_max_possible_hosts = "Барлық хосттар саны"
        calculator_usable_hosts = "Қолжетімді хосттар саны"
        calculator_first_host = "Бірінші хосттың IP мекенжайы"
        calculator_last_host = "Соңғы хосттың IP мекенжайы"
        calculator_ip_address = "IP мекенжай"
        calculator_cidr_prefix = "CIDR жазылымы"
        calculator_no_data = "Деректер жоқ"

    def return_localized_resources(self, locale: AvailableLocales):
        match locale:
            case AvailableLocales.EN:
                return self.EN

            case AvailableLocales.RU:
                return self.RU

            case AvailableLocales.KK:
                return self.KK

            case AvailableLocales.DEFAULT:
                return self.EN

            case _:
                raise ValueError("Недопустимая локализация")
