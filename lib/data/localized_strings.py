from enum import Enum, auto


class AvailableLocales(Enum):
    EN = auto()
    RU = auto()
    KK = auto()


class LocalizedStrings:
    class EN:
        LANG = "EN"

        calculator_empty_state_text = "Waiting for data entry"
        calculate_button_label = "Calculate"
        share_button_label = "Share"

        bottom_navigation_bar_calculator = "Calculator"
        bottom_navigation_bar_info = "Info"
        bottom_navigation_bar_settings = "Settings"

        calculator_no_data = "No data"

    class RU:
        LANG = "RU"

        calculator_empty_state_text = "Ожидание ввода данных"
        calculate_button_label = "Вычислить"
        share_button_label = "Поделиться"

        bottom_navigation_bar_calculator = "Калькулятор"
        bottom_navigation_bar_info = "Инфо"
        bottom_navigation_bar_settings = "Настройки"

        calculator_no_data = "Нет данных"

    class KK:
        LANG = "KK"

        calculator_empty_state_text = "Деректер енгізіңіз"
        calculate_button_label = "Есептеу"
        share_button_label = "Бөлісу"

        bottom_navigation_bar_calculator = "Калькулятор"
        bottom_navigation_bar_info = "Ақпарат"
        bottom_navigation_bar_settings = "Баптаулар"

        calculator_no_data = "Деректер жоқ"

    def return_localized_resources(self, locale: AvailableLocales):
        match locale:
            case AvailableLocales.EN:
                return self.EN

            case AvailableLocales.RU:
                return self.RU

            case AvailableLocales.KK:
                return self.KK

            case _:
                raise ValueError("Недопустимая локализация")
