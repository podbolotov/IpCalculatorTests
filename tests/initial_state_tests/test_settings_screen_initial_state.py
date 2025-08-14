import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.screens.calc_screen import CalcScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние экрана «Настройки»")
# @pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK], indirect=True)
class TestSettingsScreenInitialState:

    @allure.title("Изначальное состояние экрана")
    @allure.severity(severity_level="NORMAL")
    def test_settings_screen_initial_state(self, appium_driver, localized_strings, calc_screen):
        pytest.skip("Ожидает реализации")
