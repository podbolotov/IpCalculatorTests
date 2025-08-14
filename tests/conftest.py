import pytest
import allure

from lib.ui.components.bottom_navigation_bar import BottomNavbarOperations
from lib.ui.screens.calc_screen import CalcScreenOperations
from lib.ui.screens.settings_screen import SettingsScreenOperations


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов экрана «Калькулятор»")
def calc_screen(appium_driver) -> CalcScreenOperations:
    """
    Данная фикстура инициализирует класс операций экрана "Калькулятор"
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций экрана "Калькулятор".
    """
    _calc_screen = CalcScreenOperations(appium_driver)
    yield _calc_screen


@pytest.fixture(scope="function")
@allure.title("Загрузка локаторов и методов экрана «Настройки»")
def settings_screen(appium_driver) -> SettingsScreenOperations:
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
def bottom_navigation_bar(appium_driver) -> BottomNavbarOperations:
    """
    Данная фикстура инициализирует класс операций нижней навигационной панели
    и предоставляет доступ к его методам.

    :param appium_driver: Фикстура, предоставляющая драйвер.
    :return: Класс операций нижней навигационной панели.
    """
    _bottom_navigation_bar = BottomNavbarOperations(appium_driver)
    yield _bottom_navigation_bar
