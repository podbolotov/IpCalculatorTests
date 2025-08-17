from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from lib.tools.element_finders import find_by_locator
from lib.tools.screenshotter import make_and_attach_screenshot


class GoogleChromeLocators:
    class UrlBar:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/url_bar")'

    class TabsListButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/tab_switcher_button")'

    class TabsContextMenuButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/menu_button")'

    class TabsContextMenuCloseAllButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/close_all_tabs_menu_id")'

    class CloseAllTabsConfirmButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/positive_button")'

    class NewTabButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("com.android.chrome:id/toolbar_action_button")'


class GoogleChromeOperations:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = find_by_locator(self.driver, locator)
            element.screenshot = element.screenshot_as_base64
            return element
        except NoSuchElementException as error:
            make_and_attach_screenshot(self.driver)
            raise error

    def close_all_tabs(self):
        self.find(GoogleChromeLocators.TabsListButton).click()
        self.find(GoogleChromeLocators.TabsContextMenuButton).click()
        self.find(GoogleChromeLocators.TabsContextMenuCloseAllButton).click()
        self.find(GoogleChromeLocators.CloseAllTabsConfirmButton).click()
        self.find(GoogleChromeLocators.NewTabButton).click()

    def close_application(self):
        self.driver.terminate_app('com.android.chrome')
