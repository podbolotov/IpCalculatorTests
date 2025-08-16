from appium.webdriver.common.appiumby import AppiumBy

from lib.data.localized_strings import AvailableLocales
from lib.tools.element_finders import find_by_locator


class SettingsScreenLocators:
    """ Данный класс содержит локаторы компонентов экрана "Настройки". """

    # Title
    class ThemeSettingsSectionTitle:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ThemeHeadlineItem")'

    class LanguageSettingsSectionTitle:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("LanguageHeadlineItem")'

    # Theme Radio Buttons
    class ThemeSystemRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ThemeRadioGroupSystemRadioOption")'

    class ThemeSystemRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ThemeRadioGroupSystemRadioOption"]/android.widget.TextView'

    class ThemeDarkRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ThemeRadioGroupDarkRadioOption")'

    class ThemeDarkRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ThemeRadioGroupDarkRadioOption"]/android.widget.TextView'

    class ThemeLightRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ThemeRadioGroupLightRadioOption")'

    class ThemeLightRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ThemeRadioGroupLightRadioOption"]/android.widget.TextView'

    # Locale Radio Buttons
    class LocaleEnRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("LocaleRadioGroupEnglishRadioOption")'

    class LocaleEnRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="LocaleRadioGroupEnglishRadioOption"]/android.widget.TextView'

    class LocaleRuRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("LocaleRadioGroupRussianRadioOption")'

    class LocaleRuRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="LocaleRadioGroupRussianRadioOption"]/android.widget.TextView'

    class LocaleKkRadioButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("LocaleRadioGroupKazakhRadioOption")'

    class LocaleKkRadioButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="LocaleRadioGroupKazakhRadioOption"]/android.widget.TextView'


class SettingsScreenOperations:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = find_by_locator(self.driver, locator)
        element.screenshot = element.screenshot_as_base64
        return element

    def set_locale(self, locale: AvailableLocales):
        match locale:

            case AvailableLocales.EN:
                locale_button = self.find(SettingsScreenLocators.LocaleEnRadioButton)
                locale_button.click()

            case AvailableLocales.RU:
                locale_button = self.find(SettingsScreenLocators.LocaleRuRadioButton)
                locale_button.click()

            case AvailableLocales.KK:
                locale_button = self.find(SettingsScreenLocators.LocaleKkRadioButton)
                locale_button.click()

            case AvailableLocales.DEFAULT:
                print("\nЛокализация не будет изменена, запрошено использование локализации по умолчанию.")

            case _:
                raise ValueError("Недопустимая локализация")
