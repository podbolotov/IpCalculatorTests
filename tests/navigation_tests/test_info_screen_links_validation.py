import allure
import pytest

from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.info_screen import InfoScreenLocators
from lib.ui.side_applications.google_chrome import GoogleChromeLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты навигации")
@allure.sub_suite("Ссылки на экране «Инфо»")
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.tag("Fast", "Unstable")
class TestInfoScreenLinksValidation:

    @allure.title("Валидация ссылки «Открыть страницу на GitHub»")
    @allure.description(
        "Данный тест проверяет корректность ссылки на открытие страницы приложения на GitHub.\n"
        "При исполнении теста производится:\n"
        "- Переход на экран «Инфо»\n"
        "- Тап по кнопке, ведущей на страницу приложения на GitHub\n"
        "- Проверка содержимого строки ввода адреса в Google Chrome\n\n"
        "При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки.\n\n"
        "**Обратите внимание: данному тесту присвоен тег \"Unstable\": ввиду зависимости теста от локаторов стороннего "
        "приложения (Google Chrome), а также от конфигурации устройства, на котором исполняется данный тест "
        "(наличие установленного Google Chrome, установка Google Chrome в качестве браузера по умолчанию) данный тест "
        "может перестать работать в любой момент.**\n\n"
        "**При трудностях с сопровождением данного теста он может быть снят с "
        "поддержки, с переводом соответствующего ему тест-кейса в режим \"мануальное исполнение\".**",
    )
    def test_info_screen_github_page_link_validation(self, appium_driver, open_info_screen, info_screen, google_chrome,
                                                     non_translatable_strings):
        # Ищем кнопку "Открыть страницу на GitHub"
        info_screen.find(InfoScreenLocators.GitHubPageButton).click()
        google_chrome_url_bar_value = google_chrome.find(GoogleChromeLocators.UrlBar).text
        with allure.step("Ссылка «Открыть страницу на GitHub» ведёт на ожидаемую страницу"):
            assert google_chrome_url_bar_value == non_translatable_strings.github_page_url, \
                make_and_attach_screenshot(appium_driver)
            allure.attach(google_chrome_url_bar_value, "Полученное значение URL")
        google_chrome.close_all_tabs()
        google_chrome.close_application()

    @pytest.mark.parametrize('localized_strings', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK],
                             indirect=True)
    def test_info_screen_privacy_policy_link_validation(self, appium_driver, open_info_screen, info_screen,
                                                        google_chrome, localized_strings):
        allure.dynamic.title(f"Валидация ссылки «Прочитать политику конфиденциальности» для локализации "
                             f"{localized_strings.LANG}")

        allure.dynamic.description(
            f"Данный тест проверяет корректность ссылки на Политику конфиденциальности для локализации "
            f"{localized_strings.LANG}.\n"
            "При исполнении теста производится:\n"
            "- Переход на экран «Инфо»\n"
            "- Тап по кнопке, ведущей на Политику конфиденциальности\n"
            "- Проверка содержимого строки ввода адреса в Google Chrome\n\n"
            "При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки.\n\n"
            "**Обратите внимание: данному тесту присвоен тег \"Unstable\": ввиду зависимости теста от локаторов стороннего "
            "приложения (Google Chrome), а также от конфигурации устройства, на котором исполняется данный тест "
            "(наличие установленного Google Chrome, установка Google Chrome в качестве браузера по умолчанию) данный тест "
            "может перестать работать в любой момент.**\n\n"
            "**При трудностях с сопровождением данного теста он может быть снят с "
            "поддержки, с переводом соответствующего ему тест-кейса в режим \"мануальное исполнение\".**",
        )
        # Ищем кнопку "Прочитать политику конфиденциальности"
        info_screen.find(InfoScreenLocators.PrivacyPolicyButton).click()
        google_chrome_url_bar_value = google_chrome.find(GoogleChromeLocators.UrlBar).text
        with allure.step(f"Ссылка на политику конфиденциальности ведёт на ожидаемую для локализации "
                         f"{localized_strings.LANG} страницу"):
            assert google_chrome_url_bar_value == localized_strings.privacy_policy_url, \
                make_and_attach_screenshot(appium_driver)
            allure.attach(google_chrome_url_bar_value, "Полученное значение URL")
        google_chrome.close_all_tabs()
        google_chrome.close_application()
