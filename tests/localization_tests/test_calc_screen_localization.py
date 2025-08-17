import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.components.bottom_navigation_bar import BottomNavbarLocators
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты локализации")
@allure.suite("Тесты локализованных значений")
@allure.sub_suite("Локализация экрана «Калькулятор» и нижней навигационной панели")
@pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                         indirect=True)
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast", "Stable")
class TestCalcAndBottomNavigationBarLocalization:

    def test_calc_screen_and_navbar_empty_state_localization(self, appium_driver, restart_before, localized_strings,
                                                             calc_screen, bottom_navigation_bar):
        allure.dynamic.title(f"Локализованные значения изначального состояния для локализации {localized_strings.LANG}")
        allure.dynamic.description(
            f"Данный тест проверяет локализацию всех текстовых строк, отображаемых на экране «Калькулятор» и на нижней "
            f"навигационной панели для локализации {localized_strings.LANG} до осуществления вычислений.\n\n"
            "При проверке локализации каждого элемента к отчёту прикрепляется его локализованное значение.\n"
            "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
        )

        with allure.step("Локализованные значения экрана «Калькулятор»"):
            # Ищем на экране текст пустого состояния
            empty_state_title = calc_screen.find(CalcScreenLocators.PlaceholderText)
            with allure.step(
                    f"Значение текста пустого состояния соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(empty_state_title.text, "Локализованное значение текста пустого состояния")
                assert empty_state_title.text == localized_strings.calculator_empty_state_text, make_and_attach_screenshot(
                    appium_driver)

            # Ищем на экране текст кнопки "Вычислить"
            calculate_button_label = calc_screen.find(CalcScreenLocators.CalculateButtonLabel)
            with allure.step(
                    f"Значение текста кнопки «Вычислить» соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(calculate_button_label.text, "Локализованное значение текста кнопки «Вычислить»")
                assert calculate_button_label.text == localized_strings.calculate_button_label, make_and_attach_screenshot(
                    appium_driver)

            # Ищем на экране текст кнопки "Поделиться"
            share_button_label = calc_screen.find(CalcScreenLocators.ShareButtonLabel)
            with allure.step(
                    f"Значение текста кнопки «Поделиться» соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(share_button_label.text, "Локализованное значение текста кнопки «Поделиться»")
                assert share_button_label.text == localized_strings.share_button_label, make_and_attach_screenshot(
                    appium_driver)

        with allure.step("Локализованные значения навигационной панели"):
            # Ищем на навигационной панели текст кнопки "Калькулятор"
            calc_navbar_button_label = bottom_navigation_bar.find(BottomNavbarLocators.CalculatorNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Калькулятор» соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(calc_navbar_button_label.text, "Локализованное значение текста кнопки «Калькулятор»")
                assert calc_navbar_button_label.text == localized_strings.bottom_navigation_bar_calculator, make_and_attach_screenshot(
                    appium_driver)

            # Ищем на навигационной панели текст кнопки "Инфо"
            info_navbar_button_label = bottom_navigation_bar.find(BottomNavbarLocators.InfoNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Инфо» соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(info_navbar_button_label.text, "Локализованное значение текста кнопки «Инфо»")
                assert info_navbar_button_label.text == localized_strings.bottom_navigation_bar_info, make_and_attach_screenshot(
                    appium_driver)

            # Ищем на навигационной панели текст кнопки "Настройки"
            settings_navbar_button_label = bottom_navigation_bar.find(
                BottomNavbarLocators.SettingsNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Настройки» соответствует выбранной локализации ({localized_strings.LANG})"):
                allure.attach(settings_navbar_button_label.text, "Локализованное значение текста кнопки «Настройки»")
                assert settings_navbar_button_label.text == localized_strings.bottom_navigation_bar_settings, make_and_attach_screenshot(
                    appium_driver)

    def test_calc_screen_cidr_list_title_localization(self, appium_driver, restart_before, localized_strings,
                                                      calc_screen):
        allure.dynamic.title(
            f"Локализованное значение заголовка окна выбора CIDR для локализации {localized_strings.LANG}")
        allure.dynamic.description(
            f"Данный тест проверяет локализацию заголовка модального окна выбора маски подсети (CIDR) "
            f"для локализации {localized_strings.LANG}.\n\n"
            "При проверке локализации элемента к отчёту прикрепляется его локализованное значение.\n"
            "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
        )

        calc_screen.find(CalcScreenLocators.CIDRButton).click()

        cidr_window_title = calc_screen.find(CalcScreenLocators.CidrWindowTitle)
        with allure.step(
                f"Значение заголовка окна выбора Маски подсети соответствует локализации ({localized_strings.LANG})"):
            allure.attach(cidr_window_title.text, "Локализованное значение заголовка окна выбора Маски подсети")
            assert cidr_window_title.text == localized_strings.calculator_subnet_mask_dialog_title, \
                make_and_attach_screenshot(appium_driver)

    def test_calc_screen_result_localization(self, appium_driver, restart_before, localized_strings,
                                             calc_screen):
        allure.dynamic.title(f"Локализованные значения результатов вычисления для локализации {localized_strings.LANG}")
        allure.dynamic.description(
            f"Данный тест проверяет локализацию всех текстовых строк, отображаемых в результатах вычисления для "
            f"локализации {localized_strings.LANG}.\n\n"
            "При проверке локализации каждого элемента к отчёту прикрепляется его локализованное значение.\n"
            "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
        )
        # Тапаем по кнопке "Вычислить" для появления результатов вычисления
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        with allure.step(f"Значение заголовка IP адреса в результатах соответствует выбранной локализации "
                         f"({localized_strings.LANG})"):
            ip_address_label = calc_screen.find(CalcScreenLocators.ResultIPAddressLabel).text
            allure.attach(ip_address_label, "Локализованное значение текста заголовка «IP адрес»")
            assert ip_address_label == localized_strings.calculator_ip_address, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение заголовка CIDR нотации в результатах соответствует выбранной локализации "
                         f"({localized_strings.LANG})"):
            cidr_label = calc_screen.find(CalcScreenLocators.ResultCIDRPrefixLabel).text
            allure.attach(cidr_label, "Локализованное значение текста заголовка «CIDR нотация»")
            assert cidr_label == localized_strings.calculator_cidr_prefix, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение заголовка Маски подсети в результатах соответствует выбранной локализации "
                         f"({localized_strings.LANG})"):
            network_mask_label = calc_screen.find(CalcScreenLocators.ResultSubnetMaskLabel).text
            allure.attach(network_mask_label, "Локализованное значение текста заголовка «Маска подсети»")
            assert network_mask_label == localized_strings.calculator_subnet_mask, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение заголовка Обратной маски в результатах соответствует выбранной локализации "
                         f"({localized_strings.LANG})"):
            wildcard_mask_label = calc_screen.find(CalcScreenLocators.ResultWildcardMaskLabel).text
            allure.attach(wildcard_mask_label, "Локализованное значение текста заголовка «Обратная маска»")
            assert wildcard_mask_label == localized_strings.calculator_wildcard_mask, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение заголовка Адреса сети в результатах соответствует выбранной локализации "
                         f"({localized_strings.LANG})"):
            network_address_label = calc_screen.find(CalcScreenLocators.ResultNetworkIPAddressLabel).text
            allure.attach(network_address_label, "Локализованное значение текста заголовка «Обратная маска»")
            assert network_address_label == localized_strings.calculator_network_ip_address, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение заголовка Широковещательного адреса в результатах соответствует выбранной "
                         f"локализации ({localized_strings.LANG})"):
            broadcast_address_label = calc_screen.find(CalcScreenLocators.ResultBroadcastIPAddressLabel).text
            allure.attach(broadcast_address_label, "Локализованное значение текста заголовка «Широковещательный адрес»")
            assert broadcast_address_label == localized_strings.calculator_broadcast_ip_address, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение заголовка Общего количества адресов в результатах соответствует выбранной "
                         f"локализации ({localized_strings.LANG})"):
            calc_screen.scroll_to_list_item(
                CalcScreenLocators.ResultMaxPossibleHostsLabel, CalcScreenLocators.ResultListContainer)
            total_addresses_label = calc_screen.find(CalcScreenLocators.ResultMaxPossibleHostsLabel).text
            allure.attach(total_addresses_label, "Локализованное значение текста заголовка «Общее количество "
                                                 "адресов»")
            assert total_addresses_label == localized_strings.calculator_max_possible_hosts, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение заголовка Количества рабочих хостов в результатах соответствует выбранной "
                         f"локализации ({localized_strings.LANG})"):
            calc_screen.scroll_to_list_item(
                CalcScreenLocators.ResultUsableHostsLabel, CalcScreenLocators.ResultListContainer)
            working_hosts_label = calc_screen.find(CalcScreenLocators.ResultUsableHostsLabel).text
            allure.attach(working_hosts_label, "Локализованное значение текста заголовка «Количество рабочих хостов»")
            assert working_hosts_label == localized_strings.calculator_usable_hosts, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение заголовка Первого хоста в результатах соответствует выбранной "
                         f"локализации ({localized_strings.LANG})"):
            calc_screen.scroll_to_list_item(
                CalcScreenLocators.ResultFirstHostLabel, CalcScreenLocators.ResultListContainer)
            first_host_label = calc_screen.find(CalcScreenLocators.ResultFirstHostLabel).text
            allure.attach(first_host_label, "Локализованное значение текста заголовка «Первый хост»")
            assert first_host_label == localized_strings.calculator_first_host, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение заголовка Последнего хоста в результатах соответствует выбранной "
                         f"локализации ({localized_strings.LANG})"):
            calc_screen.scroll_to_list_item(
                CalcScreenLocators.ResultLastHostLabel, CalcScreenLocators.ResultListContainer)
            last_host_label = calc_screen.find(CalcScreenLocators.ResultLastHostLabel).text
            allure.attach(last_host_label, "Локализованное значение текста заголовка «Последний хост»")
            assert last_host_label == localized_strings.calculator_last_host, \
                make_and_attach_screenshot(appium_driver)
