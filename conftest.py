import allure
import pytest
from conf.capabilities import ApplicationCapabilities
from lib.data.localized_strings import AvailableLocales, LocalizedStrings
from appium import webdriver
import os

from lib.ui.components.bottom_navigation_bar import BottomNavbarOperations
from lib.ui.screens.settings_screen import SettingsScreenOperations


@pytest.fixture(scope="class")
@allure.title("Запуск драйвера Appium")
def appium_driver():
    """
    Данная фикстура предоставляет драйвер для взаимодействия с мобильным приложением
    """
    driver_options = ApplicationCapabilities.get()
    appium_server_url = os.environ.get("APPIUM_SERVER") or 'http://localhost:4723'
    driver = webdriver.Remote(
        command_executor=appium_server_url, options=driver_options, )
    driver.implicitly_wait(60)
    yield driver

    driver.quit()


@pytest.fixture(scope="class")
@allure.title("Загрузка локализаций")
def localized_strings(appium_driver, request):
    current_locale = AvailableLocales.DEFAULT
    try:
        current_locale = request.param
    except Exception as e:
        print(f"Locale fixture wasn't parametrized! DEFAULT locale will be used ({e})")

    bnb = BottomNavbarOperations(appium_driver)
    bnb.open_settings_screen()

    ss = SettingsScreenOperations(appium_driver)
    ss.set_locale(current_locale)

    appium_driver.terminate_app(appium_driver.capabilities['appPackage'])
    appium_driver.activate_app(appium_driver.capabilities['appPackage'])

    ls = LocalizedStrings()

    localized_strings = ls.return_localized_resources(locale=current_locale)

    return localized_strings


@pytest.fixture(scope="function")
@allure.title("Перезапуск приложения перед тестом")
def restart_before(appium_driver, request):
    appium_driver.terminate_app(appium_driver.capabilities['appPackage'])
    appium_driver.activate_app(appium_driver.capabilities['appPackage'])
    allure.attach("Приложение перезапускается перед началом этого теста.")
    yield


@pytest.fixture(scope="function")
@allure.title("Перезапуск приложения после теста")
def restart_after(appium_driver, request):
    yield
    appium_driver.terminate_app(appium_driver.capabilities['appPackage'])
    appium_driver.activate_app(appium_driver.capabilities['appPackage'])
    allure.attach("Приложение перезапускается после окончания этого теста.")
