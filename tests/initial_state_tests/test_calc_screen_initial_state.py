import allure

from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.components.bottom_navigation_bar import BottomNavbarLocators
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние экрана «Калькулятор»")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast")
class TestCalcScreenInitialState:

    @allure.title("Изначальное состояние экрана")
    def test_calc_screen_initial_state(self, appium_driver, restart_before, calc_screen,
                                       bottom_navigation_bar):
        # Ищем на экране изображение пустого состояния
        empty_state_image = calc_screen.find(CalcScreenLocators.PlaceholderImage)
        with allure.step("Изображение пустого состояния отображается на экране"):
            assert empty_state_image.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(empty_state_image)

        # Ищем на экране текст пустого состояния
        empty_state_title = calc_screen.find(CalcScreenLocators.PlaceholderText)
        with allure.step("Текст пустого состояния отображается на экране"):
            assert empty_state_title.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(empty_state_title)

        # Ищем на экране контейнер с полями ввода IP адреса
        ip_address_inputs_container = calc_screen.find(CalcScreenLocators.IPInputContainer)
        with allure.step("Контейнер с полями ввода IP-адреса отображается на экране"):
            assert ip_address_inputs_container.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(ip_address_inputs_container)

            # Ищем на экране стандартные значения группы полей ввода IP-адреса
            ip_input_first_octet_placeholder_value, ip_input_second_octet_placeholder_value, \
                ip_input_third_octet_placeholder_value, ip_input_fourth_octet_placeholder_value = (
                calc_screen.find(CalcScreenLocators.IPInputFirstOctetPlaceholderValue),
                calc_screen.find(CalcScreenLocators.IPInputSecondOctetPlaceholderValue),
                calc_screen.find(CalcScreenLocators.IPInputThirdOctetPlaceholderValue),
                calc_screen.find(CalcScreenLocators.IPInputFourthOctetPlaceholderValue)
            )
            with allure.step("Стандартное значение IP-адреса соответствует 192.168.1.1"):
                ip_placeholder = (f"{ip_input_first_octet_placeholder_value.text}."
                                  f"{ip_input_second_octet_placeholder_value.text}."
                                  f"{ip_input_third_octet_placeholder_value.text}."
                                  f"{ip_input_fourth_octet_placeholder_value.text}")
                assert ip_placeholder == "192.168.1.1", make_and_attach_screenshot(appium_driver)

        # Ищем на экране кнопку выбора маски подсети
        cidr_button = calc_screen.find(CalcScreenLocators.CIDRButton)
        with allure.step("Кнопка выбора маски подсети отображается на экране"):
            assert cidr_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(cidr_button)

            # Ищем на экране стандартное значение маски подсети
            cidr_button_value = calc_screen.find(CalcScreenLocators.CIDRButtonPlaceholderText)
            with allure.step("Стандартное значение маски подсети соответствует 24"):
                cidr_placeholder = cidr_button_value.text
                assert cidr_placeholder == "24", make_and_attach_screenshot(appium_driver)

        # Ищем на экране кнопку "Вычислить"
        calculate_button = calc_screen.find(CalcScreenLocators.CalculateButton)

        with allure.step("Кнопка «Вычислить» отображается на экране"):
            assert calculate_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(calculate_button)

            with allure.step("Кнопка «Вычислить» активна"):
                assert calculate_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

        # Ищем на экране кнопку "Поделиться"
        share_button = calc_screen.find(CalcScreenLocators.ShareButton)

        with allure.step("Кнопка «Поделиться» отображается на экране"):
            attach_element_screenshot(share_button)
            assert share_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Поделиться» неактивна"):
                assert share_button.is_enabled() == False, make_and_attach_screenshot(appium_driver)

        ###
        calc_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.CalculatorNavigationButton)

        with allure.step("Кнопка «Калькулятор» отображается на навигационной панели"):
            assert calc_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(calc_navbar_button)

            with allure.step("Кнопка «Калькулятор» активна"):
                assert calc_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Калькулятор» выбрана"):
                assert calc_navbar_button.is_selected() == True, make_and_attach_screenshot(appium_driver)

        # Ищем на навигационной панели кнопку "Инфо"
        info_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.InfoNavigationButton)

        with allure.step("Кнопка «Инфо» отображается на навигационной панели"):
            assert info_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(info_navbar_button)

            with allure.step("Кнопка «Инфо» активна"):
                assert info_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Инфо» не выбрана"):
                assert info_navbar_button.is_selected() == False, make_and_attach_screenshot(appium_driver)

        # Ищем на навигационной панели кнопку "Настройки"
        settings_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.SettingsNavigationButton)

        with allure.step("Кнопка «Настройки» отображается на навигационной панели"):
            assert settings_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(settings_navbar_button)

            with allure.step("Кнопка «Настройки» активна"):
                assert settings_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Настройки» не выбрана"):
                assert settings_navbar_button.is_selected() == False, make_and_attach_screenshot(appium_driver)
