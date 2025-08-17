import allure

from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.screens.settings_screen import SettingsScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние экрана «Настройки»")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast", "Stable")
class TestSettingsScreenInitialState:

    @allure.title("Изначальное состояние экрана")
    @allure.description(
        "Данный тест проверяет изначальное состояние экрана «Настройки»\n"
        "При исполнении теста производятся следующие проверки:\n"
        "- На экране отображается заголовок секции выбора темы оформления\n"
        "- На экране отображается кнопка выбора системной темы\n"
        "   - Системная тема выбрана по умолчанию\n"
        "- На экране отображается кнопка выбора тёмной темы\n"
        "   - Тёмная тема не выбрана по умолчанию\n"
        "- На экране отображается кнопка выбора светлой темы\n"
        "   - Светлая тема не выбрана по умолчанию\n"
        "- На экране отображается заголовок секции выбора языка приложения\n"
        "- На экране отображается кнопка выбора английского языка\n"
        "   - Английский язык выбран по умолчанию\n"
        "- На экране отображается кнопка выбора русского языка\n"
        "   - Английский язык не выбран по умолчанию\n"
        "- На экране отображается кнопка выбора казахского языка\n"
        "   - Казахский язык не выбран по умолчанию\n\n"
        "При проверке наличия на экране каждого из перечисленных элементов к отчёту прикрепляется скриншот "
        "проверяемого элемента.\n"
        "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
    )
    def test_settings_screen_initial_state(self, appium_driver, open_settings_screen, settings_screen):
        # Ищем на заголовок секции "Выбор темы оформления"
        theme_setting_title = settings_screen.find(SettingsScreenLocators.ThemeSettingsSectionTitle)
        with allure.step("Заголовок секции «Выбор темы оформления» отображается на экране"):
            assert theme_setting_title.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(theme_setting_title)

        # Ищем на кнопку выбора системной темы
        theme_setting_system_radiobutton = settings_screen.find(SettingsScreenLocators.ThemeSystemRadioButton)
        with allure.step("Радио-кнопка выбора темы «Системная» отображается на экране"):
            assert theme_setting_system_radiobutton.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(theme_setting_system_radiobutton)

            with allure.step("Радио-кнопка выбора темы «Системная» выбрана по умолчанию"):
                assert theme_setting_system_radiobutton.get_attribute("checked") == 'true', make_and_attach_screenshot(
                    appium_driver)

        # Ищем на кнопку выбора тёмной темы
        theme_setting_dark_radiobutton = settings_screen.find(SettingsScreenLocators.ThemeDarkRadioButton)
        with allure.step("Радио-кнопка выбора темы «Тёмная» отображается на экране"):
            assert theme_setting_dark_radiobutton.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(theme_setting_dark_radiobutton)

            with allure.step("Радио-кнопка выбора темы «Тёмная» не выбрана по умолчанию"):
                assert theme_setting_dark_radiobutton.get_attribute("checked") == 'false', make_and_attach_screenshot(
                    appium_driver)

        # Ищем на кнопку выбора светлой темы
        theme_setting_light_radiobutton = settings_screen.find(SettingsScreenLocators.ThemeLightRadioButton)
        with allure.step("Радио-кнопка выбора темы «Светлая» отображается на экране"):
            assert theme_setting_light_radiobutton.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(theme_setting_light_radiobutton)

            with allure.step("Радио-кнопка выбора темы «Светлая» не выбрана по умолчанию"):
                assert theme_setting_light_radiobutton.get_attribute("checked") == 'false', make_and_attach_screenshot(
                    appium_driver)

        # Ищем на заголовок секции "Выбор языка"
        language_setting_title = settings_screen.find(SettingsScreenLocators.LanguageSettingsSectionTitle)
        with allure.step("Заголовок секции «Выбор языка» отображается на экране"):
            assert language_setting_title.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(language_setting_title)

        # Ищем на кнопку выбора языка English
        language_setting_english_radiobutton = settings_screen.find(SettingsScreenLocators.LocaleEnRadioButton)
        with allure.step("Радио-кнопка выбора языка «English» отображается на экране"):
            assert language_setting_english_radiobutton.is_displayed() == True, make_and_attach_screenshot(
                appium_driver)
            attach_element_screenshot(language_setting_english_radiobutton)

            with allure.step("Радио-кнопка выбора темы «English» выбрана по умолчанию"):
                assert language_setting_english_radiobutton.get_attribute(
                    "checked") == 'true', make_and_attach_screenshot(
                    appium_driver)

        # Ищем на кнопку выбора языка Русский
        language_setting_russian_radiobutton = settings_screen.find(SettingsScreenLocators.LocaleRuRadioButton)
        with allure.step("Радио-кнопка выбора языка «Русский» отображается на экране"):
            assert language_setting_russian_radiobutton.is_displayed() == True, make_and_attach_screenshot(
                appium_driver)
            attach_element_screenshot(language_setting_russian_radiobutton)

            with allure.step("Радио-кнопка выбора темы «Русский» не выбрана по умолчанию"):
                assert language_setting_russian_radiobutton.get_attribute(
                    "checked") == 'false', make_and_attach_screenshot(
                    appium_driver)

        # Ищем на кнопку выбора языка Қазақша
        language_setting_kazakh_radiobutton = settings_screen.find(SettingsScreenLocators.LocaleKkRadioButton)
        with allure.step("Радио-кнопка выбора языка «Қазақша» отображается на экране"):
            assert language_setting_kazakh_radiobutton.is_displayed() == True, make_and_attach_screenshot(
                appium_driver)
            attach_element_screenshot(language_setting_kazakh_radiobutton)

            with allure.step("Радио-кнопка выбора темы «Қазақша» не выбрана по умолчанию"):
                assert language_setting_kazakh_radiobutton.get_attribute(
                    "checked") == 'false', make_and_attach_screenshot(
                    appium_driver)
