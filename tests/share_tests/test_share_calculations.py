import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.ip_tools import generate_valid_ip, ip_calculator
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Дополнительные пользовательские сценарии")
@allure.sub_suite("Тесты функционала «Поделиться»")
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.tag("Fast", "Unstable")
@pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                         indirect=True)
class TestShareCalculations:

    def test_calculations_share(self, appium_driver, calc_screen, system_share_dialog, localized_strings):
        allure.dynamic.title(
            f"Функционал «Поделиться результатами вычисления» (с контентом для локализации {localized_strings.LANG})")
        allure.dynamic.description(
            "Данный тест проверяет корректность работы функционала «Поделиться результатами вычисления» "
            f"(с контентом для локализации {localized_strings.LANG}).\n"
            "При исполнении теста производится:\n"
            "- Инициализация функционала посредством нажатия на кнопку «Поделиться» на экране «Калькулятор»\n"
            "- Копирование результата из поля предпросмотра системного окна «Поделиться»\n"
            "- Сверка имеющегося в буфере обмена текста с ожидаемым (рассчитанным и подготовленным локально)\n\n"
            "При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки.\n\n"
            "**Обратите внимание: данному тесту присвоен тег \"Unstable\": ввиду зависимости теста от локаторов системных "
            "компонентов, ввиду чего данный тест может перестать работать в любой момент.**\n\n"
            "**При трудностях с сопровождением данного теста он может быть снят с "
            "поддержки, с переводом соответствующего ему тест-кейса в режим \"мануальное исполнение\".**",
        )

        # Генерируем случайный корректный IP
        generated_ip = generate_valid_ip()

        # Вводим сгенерированный IP в приложение
        calc_screen.enter_ip_address(address=generated_ip)

        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        # Нажимаем на кнопку "Поделиться"
        calc_screen.find(CalcScreenLocators.ShareButton).click()

        # Получаем контент
        share_preview_content = system_share_dialog.get_share_preview_content()

        with allure.step("Локально подготовленный результат соответствует полученному из буфера обмена"):

            local_calculation_result = ip_calculator(generated_ip, locale=localized_strings)

            allure.attach(share_preview_content, "Полученное значение контента Share")

            def add_spaces_after_every_third_symbol_from_end(string: str) -> str:
                counter, result = 0, ""
                for symbol in reversed(string):
                    result, counter = result + symbol, counter + 1
                    if counter == 3: result, counter = result + " ", 0

                return ''.join(reversed(result)).strip()

            expected_calculations_share_content = \
                f"{localized_strings.calculator_ip_address}: {local_calculation_result.ip_address}\n" \
                f"{localized_strings.calculator_cidr_prefix}: {local_calculation_result.cidr}\n" \
                f"{localized_strings.calculator_subnet_mask}: {local_calculation_result.network_mask}\n" \
                f"{localized_strings.calculator_wildcard_mask}: {local_calculation_result.wildcard_mask}\n" \
                f"{localized_strings.calculator_network_ip_address}: {local_calculation_result.network_address}\n" \
                f"{localized_strings.calculator_broadcast_ip_address}: {local_calculation_result.broadcast_address}\n" \
                f"{localized_strings.calculator_max_possible_hosts}: {add_spaces_after_every_third_symbol_from_end(local_calculation_result.total_addresses)}\n" \
                f"{localized_strings.calculator_usable_hosts}: {add_spaces_after_every_third_symbol_from_end(local_calculation_result.total_hosts)}\n" \
                f"{localized_strings.calculator_first_host}: {local_calculation_result.first_host}\n" \
                f"{localized_strings.calculator_last_host}: {local_calculation_result.last_host}\n"

            allure.attach(str(expected_calculations_share_content), 'Результат локальной подготовки контента')

            assert share_preview_content == expected_calculations_share_content, make_and_attach_screenshot(
                appium_driver)
