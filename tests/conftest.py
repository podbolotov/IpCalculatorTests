from typing import Any, Generator

import pytest
import allure

from lib.ui.components.bottom_navigation_bar import BottomNavbarOperations
from lib.ui.screens.calc_screen import CalcScreenOperations
from lib.ui.screens.info_screen import InfoScreenOperations
from lib.ui.screens.settings_screen import SettingsScreenOperations
from lib.ui.side_applications.google_chrome import GoogleChromeOperations


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов экрана «Калькулятор»")
def calc_screen(appium_driver) -> Generator[CalcScreenOperations, Any, None]:
    """
    Данная фикстура инициализирует класс операций экрана "Калькулятор"
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций экрана "Калькулятор".
    """
    _calc_screen = CalcScreenOperations(appium_driver)
    yield _calc_screen


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов экрана «Инфо»")
def info_screen(appium_driver) -> Generator[InfoScreenOperations, Any, None]:
    """
    Данная фикстура инициализирует класс операций экрана "Инфо"
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций экрана "Инфо".
    """
    _info_screen = InfoScreenOperations(appium_driver)
    yield _info_screen


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов экрана «Настройки»")
def settings_screen(appium_driver) -> Generator[SettingsScreenOperations, Any, None]:
    """
    Данная фикстура инициализирует класс операций экрана "Настройки"
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций экрана "Настройки".
    """
    _settings_screen = SettingsScreenOperations(appium_driver)
    yield _settings_screen


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов нижней навигационной панели")
def bottom_navigation_bar(appium_driver) -> Generator[BottomNavbarOperations, Any, None]:
    """
    Данная фикстура инициализирует класс операций нижней навигационной панели
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций нижней навигационной панели.
    """
    _bottom_navigation_bar = BottomNavbarOperations(appium_driver)
    yield _bottom_navigation_bar


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов браузера Google Chrome")
def google_chrome(appium_driver) -> Generator[GoogleChromeOperations, Any, None]:
    """
    Данная фикстура инициализирует класс операций браузера Google Chrome.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций браузера Google Chrome.
    """
    _google_chrome = GoogleChromeOperations(appium_driver)
    yield _google_chrome
