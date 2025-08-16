import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.settings_screen import SettingsScreenLocators


@allure.parent_suite("Тесты локализации")
@allure.suite("Тесты локализованных значений")
@allure.sub_suite("Локализация экрана «Настройки»")
@pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                         indirect=True)
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast")
class TestSettingsScreenLocalization:

    def test_settings_screen_localization(self, appium_driver, localized_strings, non_translatable_strings,
                                          settings_screen, open_settings_screen):
        allure.dynamic.title(f"Локализованные значения элементов экрана для локализации {localized_strings.LANG}")

        with allure.step(f"Заголовок секции «Выбор темы оформления» соответствует локализации "
                         f"({localized_strings.LANG})"):
            theme_section_label = settings_screen.find(SettingsScreenLocators.ThemeSettingsSectionTitle).text
            allure.attach(theme_section_label, "Локализованное значение заголовка секции «Выбор темы оформления»")
            assert theme_section_label == localized_strings.settings_theme, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение текста кнопки выбора темы «Системная» соответствует локализации"
                         f"({localized_strings.LANG})"):
            theme_setting_system_radiobutton_text = \
                settings_screen.find(SettingsScreenLocators.ThemeSystemRadioButtonLabel).text
            allure.attach(theme_setting_system_radiobutton_text,
                          "Локализованное значение текста кнопки выбора темы «Системная»")
            assert theme_setting_system_radiobutton_text == \
                   localized_strings.settings_theme_system, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение текста кнопки выбора темы «Тёмная» соответствует локализации"
                         f"({localized_strings.LANG})"):
            theme_setting_dark_radiobutton_text = \
                settings_screen.find(SettingsScreenLocators.ThemeDarkRadioButtonLabel).text
            allure.attach(theme_setting_dark_radiobutton_text,
                          "Локализованное значение текста кнопки выбора темы «Тёмная»")
            assert theme_setting_dark_radiobutton_text == \
                   localized_strings.settings_theme_dark, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение текста кнопки выбора темы «Светлая» соответствует локализации"
                         f"({localized_strings.LANG})"):
            theme_setting_light_radiobutton_text = \
                settings_screen.find(SettingsScreenLocators.ThemeLightRadioButtonLabel).text
            allure.attach(theme_setting_light_radiobutton_text,
                          "Локализованное значение текста кнопки выбора темы «Светлая»")
            assert theme_setting_light_radiobutton_text == \
                   localized_strings.settings_theme_light, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Заголовок секции «Выбор языка» соответствует локализации "
                         f"({localized_strings.LANG})"):
            language_section_label = settings_screen.find(SettingsScreenLocators.LanguageSettingsSectionTitle).text
            allure.attach(language_section_label, "Локализованное значение заголовка секции «Выбор языка»")
            assert language_section_label == localized_strings.settings_language, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Значение текста кнопки выбора языка «English» соответствует ожидаемому"):
            language_setting_english_radiobutton_text = settings_screen.find(
                SettingsScreenLocators.LocaleEnRadioButtonLabel).text
            allure.attach(language_setting_english_radiobutton_text,
                          "Значение кнопки выбора языка «English» (не подвергается переводу)")
            assert language_setting_english_radiobutton_text == \
                   non_translatable_strings.settings_en_language_radio_button, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение текста кнопки выбора языка «Русский» соответствует ожидаемому"):
            language_setting_russian_radiobutton_text = settings_screen.find(
                SettingsScreenLocators.LocaleRuRadioButtonLabel).text
            allure.attach(language_setting_russian_radiobutton_text,
                          "Значение кнопки выбора языка «Русский» (не подвергается переводу)")
            assert language_setting_russian_radiobutton_text == \
                   non_translatable_strings.settings_ru_language_radio_button, make_and_attach_screenshot(appium_driver)

        with allure.step(f"Значение текста кнопки выбора языка «Қазақша» соответствует ожидаемому"):
            language_setting_kazakh_radiobutton_text = settings_screen.find(
                SettingsScreenLocators.LocaleKkRadioButtonLabel).text
            allure.attach(language_setting_kazakh_radiobutton_text,
                          "Значение кнопки выбора языка «Қазақша» (не подвергается переводу)")
            assert language_setting_kazakh_radiobutton_text == \
                   non_translatable_strings.settings_kk_language_radio_button, make_and_attach_screenshot(appium_driver)
