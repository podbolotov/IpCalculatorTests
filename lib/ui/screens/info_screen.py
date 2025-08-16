from appium.webdriver.common.appiumby import AppiumBy

from lib.tools.element_finders import find_by_locator


class InfoScreenLocators:
    """ Данный класс содержит локаторы компонентов экрана "Инфо". """

    # Buttons
    class GitHubPageButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("GithubLargeText")'

    class PrivacyPolicyButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("PrivacyPolicyLargeText")'

    class ContactTheDeveloperButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContactLargeText")'

    class RateTheAppButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("RateTheAppLargeText")'

    class ShareTheAppButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ShareTheAppLargeText")'


class InfoScreenOperations:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = find_by_locator(self.driver, locator)
        element.screenshot = element.screenshot_as_base64
        return element
