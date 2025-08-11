import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние экрана «Настройки»")
# @pytest.mark.parametrize('locales', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK], indirect=True)
@pytest.mark.parametrize('locales', [AvailableLocales.RU], indirect=True)
class TestSettingsScreenInitialState:

    @allure.title("Изначальное состояние экрана")
    @allure.severity(severity_level="NORMAL")
    def test_calc_screen_initial_state(self, appium_driver, locales, calc_screen):
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

            with allure.step(f"Значение текста пустого состояния соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(empty_state_title.text, "Локализованное значение текста пустого состояния")
                assert empty_state_title.text == locales.calculator_empty_state_text, make_and_attach_screenshot(
                    appium_driver)

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

            # Ищем на экране текст кнопки "Вычислить"
            calculate_button_label = calc_screen.find(CalcScreenLocators.CalculateButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Вычислить» соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(calculate_button_label.text, "Локализованное значение текста кнопки «Вычислить»")
                assert calculate_button_label.text == locales.calculate_button_label, make_and_attach_screenshot(
                    appium_driver)

        # Ищем на экране кнопку "Поделиться"
        share_button = calc_screen.find(CalcScreenLocators.ShareButton)

        with allure.step("Кнопка «Поделиться» отображается на экране"):
            attach_element_screenshot(share_button)
            assert share_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Поделиться» неактивна"):
                assert share_button.is_enabled() == False, make_and_attach_screenshot(appium_driver)

            # Ищем на экране текст кнопки "Поделиться"
            share_button_label = calc_screen.find(CalcScreenLocators.ShareButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Поделиться» соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(share_button_label.text, "Локализованное значение текста кнопки «Поделиться»")
                assert share_button_label.text == locales.share_button_label, make_and_attach_screenshot(appium_driver)
