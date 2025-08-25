import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.info_screen import InfoScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Дополнительные пользовательские сценарии")
@allure.sub_suite("Тесты функционала «Поделиться»")
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.tag("Fast", "Unstable")
@pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                         indirect=True)
class TestShareApp:


    def test_app_share(self, appium_driver, open_info_screen, info_screen, system_share_dialog, localized_strings):
        allure.dynamic.title(
            f"Функционал «Поделиться приложением» (с контентом для локализации {localized_strings.LANG})")
        allure.dynamic.description(
            "Данный тест проверяет корректность работы функционала «Поделиться приложением» "
            f"(с контентом для локализации {localized_strings.LANG}).\n"
            "При исполнении теста производится:\n"
            "- Инициализация функционала посредством нажатия на кнопку «Поделиться приложением» на экране «Инфо»\n"
            "- Копирование результата из поля предпросмотра системного окна «Поделиться»\n"
            "- Сверка имеющегося в буфере обмена текста с ожидаемым (подготовленным локально)\n\n"
            "При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки.\n\n"
            "**Обратите внимание: данному тесту присвоен тег \"Unstable\": ввиду зависимости теста от локаторов системных "
            "компонентов, ввиду чего данный тест может перестать работать в любой момент.**\n\n"
            "**При трудностях с сопровождением данного теста он может быть снят с "
            "поддержки, с переводом соответствующего ему тест-кейса в режим \"мануальное исполнение\".**",
        )

        # Нажимаем на кнопку "Поделиться приложением"
        info_screen.find(InfoScreenLocators.ShareTheAppButton).click()

        # Получаем контент
        share_preview_content = system_share_dialog.get_share_preview_content()

        # Подготавливаем ожидаемый контент
        expected_app_share_content = localized_strings.app_share_message

        with allure.step("Локально подготовленный результат соответствует полученному из буфера обмена"):
            allure.attach(share_preview_content, "Полученное значение контента Share")
            allure.attach(expected_app_share_content, 'Результат локальной подготовки контента')

            assert share_preview_content == expected_app_share_content, make_and_attach_screenshot(
                appium_driver)
