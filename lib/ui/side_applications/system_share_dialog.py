from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from lib.tools.element_finders import find_by_locator
from lib.tools.screenshotter import make_and_attach_screenshot


class SystemShareLocators:
    class ShareDialogDrag:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("android:id/drag")'

    class ShareDialogContentPreview:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("android:id/content_preview_text")'

    class ShareDialogCopyButton:
        type = AppiumBy.XPATH
        value = ('//android.widget.Button[@resource-id="android:id/chooser_copy_button"]|' # Android 11
                 '//android.widget.FrameLayout[@resource-id="com.android.intentresolver:id/copy"]') # Android 16



class SystemShareOperations:

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

    def get_share_preview_content(self):
        self.find(SystemShareLocators.ShareDialogCopyButton).click()
        share_preview_content = self.driver.get_clipboard_text()
        return share_preview_content

    def swipe_to_close_share(self):
        drag = self.find(SystemShareLocators.ShareDialogDrag)
        ActionChains(self.driver).click_and_hold(drag).move_by_offset(xoffset=10, yoffset=50).release().perform()
