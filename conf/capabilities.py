import os
from appium.options.android import UiAutomator2Options

from conf.variables import Variables


class ApplicationCapabilities:
    @staticmethod
    def get():
        application_path = Variables.APP_PATH
        application_capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName=Variables.DEVICE_NAME,
            appPackage='io.github.kaczmarek.ipcalculator',
            app=application_path,
            fullReset='true'
        )
        capabilities = UiAutomator2Options().load_capabilities(application_capabilities)
        return capabilities
