from enum import Enum, auto

from appium.webdriver.common.appiumby import AppiumBy

from lib.tools.element_finders import find_by_locator


class NavigationButtons(Enum):
    Calculator = auto()
    Info = auto()
    Settings = auto()


class BottomNavbarLocators:
    class CalculatorNavigationButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("RootNavigationItem+calculator")'

    class CalculatorNavigationButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="RootNavigationItem+calculator"]/android.widget.TextView'

    class InfoNavigationButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("RootNavigationItem+info")'

    class InfoNavigationButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="RootNavigationItem+info"]/android.widget.TextView'

    class SettingsNavigationButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("RootNavigationItem+settings")'

    class SettingsNavigationButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="RootNavigationItem+settings"]/android.widget.TextView'


class BottomNavbarOperations:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = find_by_locator(self.driver, locator)
        element.screenshot = element.screenshot_as_base64
        return element

    def _navigation_click(self, button: NavigationButtons):
        match button:
            case NavigationButtons.Calculator:
                calculator_button = self.find(BottomNavbarLocators.CalculatorNavigationButton)
                calculator_button.click()

            case NavigationButtons.Info:
                info_button = self.find(BottomNavbarLocators.InfoNavigationButton)
                info_button.click()

            case NavigationButtons.Settings:
                settings_button = self.find(BottomNavbarLocators.SettingsNavigationButton)
                settings_button.click()

            case _:
                raise ValueError("Недопустимая кнопка")

    def open_calculator_screen(self):
        self._navigation_click(NavigationButtons.Calculator)

    def open_info_screen(self):
        self._navigation_click(NavigationButtons.Info)

    def open_settings_screen(self):
        self._navigation_click(NavigationButtons.Settings)
