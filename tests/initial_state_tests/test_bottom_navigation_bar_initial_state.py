import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.components.bottom_navigation_bar import BottomNavbarLocators
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние нижней навигационной панели")
class TestBottomNavigationBarInitialState:

    @pytest.mark.parametrize('locales', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK], indirect=True)
    @allure.title("Изначальное состояние навигационной панели")
    @allure.severity(severity_level="NORMAL")
    def test_bottom_navigation_bar_initial_state(self, appium_driver, locales, bottom_navigation_bar):
        # Ищем на навигационной панели кнопку "Калькулятор"
        calc_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.CalculatorNavigationButton)

        with allure.step("Кнопка «Калькулятор» отображается на навигационной панели"):
            assert calc_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(calc_navbar_button)

            with allure.step("Кнопка «Калькулятор» активна"):
                assert calc_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Калькулятор» выбрана"):
                assert calc_navbar_button.is_selected() == True, make_and_attach_screenshot(appium_driver)

            # Ищем на навигационной панели текст кнопки "Калькулятор"
            calc_navbar_button_label = bottom_navigation_bar.find(BottomNavbarLocators.CalculatorNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Калькулятор» соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(calc_navbar_button_label.text, "Локализованное значение текста кнопки «Калькулятор»")
                assert calc_navbar_button_label.text == locales.bottom_navigation_bar_calculator, make_and_attach_screenshot(
                    appium_driver)

        # Ищем на навигационной панели кнопку "Инфо"
        info_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.InfoNavigationButton)

        with allure.step("Кнопка «Инфо» отображается на навигационной панели"):
            assert info_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(info_navbar_button)

            with allure.step("Кнопка «Инфо» активна"):
                assert info_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Инфо» не выбрана"):
                assert info_navbar_button.is_selected() == False, make_and_attach_screenshot(appium_driver)

            # Ищем на навигационной панели текст кнопки "Инфо"
            info_navbar_button_label = bottom_navigation_bar.find(BottomNavbarLocators.InfoNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Инфо» соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(info_navbar_button_label.text, "Локализованное значение текста кнопки «Инфо»")
                assert info_navbar_button_label.text == locales.bottom_navigation_bar_info, make_and_attach_screenshot(
                    appium_driver)

        # Ищем на навигационной панели кнопку "Настройки"
        settings_navbar_button = bottom_navigation_bar.find(BottomNavbarLocators.SettingsNavigationButton)

        with allure.step("Кнопка «Настройки» отображается на навигационной панели"):
            assert settings_navbar_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(settings_navbar_button)

            with allure.step("Кнопка «Настройки» активна"):
                assert settings_navbar_button.is_enabled() == True, make_and_attach_screenshot(appium_driver)

            with allure.step("Кнопка «Настройки» не выбрана"):
                assert settings_navbar_button.is_selected() == False, make_and_attach_screenshot(appium_driver)

            # Ищем на навигационной панели текст кнопки "Настройки"
            settings_navbar_button_label = bottom_navigation_bar.find(
                BottomNavbarLocators.SettingsNavigationButtonLabel)

            with allure.step(
                    f"Значение текста кнопки «Настройки» соответствует выбранной локализации ({locales.LANG})"):
                allure.attach(settings_navbar_button_label.text, "Локализованное значение текста кнопки «Настройки»")
                assert settings_navbar_button_label.text == locales.bottom_navigation_bar_settings, make_and_attach_screenshot(
                    appium_driver)
