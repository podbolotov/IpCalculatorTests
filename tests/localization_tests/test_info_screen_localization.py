import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.info_screen import InfoScreenLocators


@allure.parent_suite("Тесты локализации")
@allure.suite("Тесты локализованных значений")
@allure.sub_suite("Локализация экрана «Инфо»")
@pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                         indirect=True)
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast")
class TestInfoScreenLocalization:

    def test_info_screen_localization(self, appium_driver, localized_strings, info_screen, open_info_screen):
        allure.dynamic.title(f"Локализованные значения элементов экрана для локализации {localized_strings.LANG}")
        allure.dynamic.description(
            f"Данный тест проверяет локализацию всех текстовых строк, отображаемых на экране «Инфо» для "
            f"локализации {localized_strings.LANG}.\n\n"
            "При проверке локализации каждого элемента к отчёту прикрепляется его локализованное значение.\n"
            "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
        )
        with allure.step(f"Текст кнопки «Открыть страницу на GitHub» соответствует локализации "
                         f"({localized_strings.LANG})"):
            open_github_button_label = info_screen.find(InfoScreenLocators.GitHubPageButton).text
            allure.attach(open_github_button_label, "Локализованное значение кнопки «Открыть страницу на GitHub»")
            assert open_github_button_label == localized_strings.info_go_to_github, make_and_attach_screenshot(
                appium_driver)

        with allure.step(f"Текст кнопки «Прочитать политику конфиденциальности» соответствует локализации "
                         f"({localized_strings.LANG})"):
            read_privacy_policy_button_label = info_screen.find(InfoScreenLocators.PrivacyPolicyButton).text
            allure.attach(read_privacy_policy_button_label,
                          "Локализованное значение кнопки «Прочитать политику конфиденциальности»")
            assert read_privacy_policy_button_label == localized_strings.info_privacy_policy, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Текст кнопки «Связаться с разработчиком» соответствует локализации "
                         f"({localized_strings.LANG})"):
            contact_the_developer_button_label = info_screen.find(InfoScreenLocators.ContactTheDeveloperButton).text
            allure.attach(contact_the_developer_button_label,
                          "Локализованное значение кнопки «Связаться с разработчиком»")
            assert contact_the_developer_button_label == localized_strings.info_send_email, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Текст кнопки «Оценить приложение» соответствует локализации "
                         f"({localized_strings.LANG})"):
            rate_the_app_button_label = info_screen.find(InfoScreenLocators.RateTheAppButton).text
            allure.attach(rate_the_app_button_label,
                          "Локализованное значение кнопки «Оценить приложение»")
            assert rate_the_app_button_label == localized_strings.info_app_rate, \
                make_and_attach_screenshot(appium_driver)

        with allure.step(f"Текст кнопки «Поделиться приложением» соответствует локализации "
                         f"({localized_strings.LANG})"):
            share_the_app_button_label = info_screen.find(InfoScreenLocators.ShareTheAppButton).text
            allure.attach(share_the_app_button_label,
                          "Локализованное значение кнопки «Поделиться приложением»")
            assert share_the_app_button_label == localized_strings.info_share_app, \
                make_and_attach_screenshot(appium_driver)
