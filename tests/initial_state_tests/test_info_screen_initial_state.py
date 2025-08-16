import allure

from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.screens.info_screen import InfoScreenLocators


@allure.parent_suite("Тесты пользовательского интерфейса")
@allure.suite("Тесты изначального состояния приложения")
@allure.sub_suite("Состояние экрана «Инфо»")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.tag("Fast")
class TestInfoScreenInitialState:

    @allure.title("Изначальное состояние экрана")
    @allure.description(
        "Данный тест проверяет изначальное состояние экрана «Инфо»\n"
        "При исполнении теста производятся следующие проверки:\n"
        "- На экране отображается кнопка перехода на GitHub-страницу проекта\n"
        "- На экране отображается кнопка открытия политики конфиденциальности приложения\n"
        "- На экране отображается кнопка перехода в email-клиент для составления письма разработчику\n"
        "- На экране отображается кнопка перехода в Google Play для оценки приложения\n"
        "- На экране отображается кнопка вызова системного модального окна \"поделиться\" с сообщением о приложении\n\n"
        "При проверке наличия на экране каждого из перечисленных элементов к отчёту прикрепляется скриншот "
        "проверяемого элемента.\n"
        "При возникновении ошибки к отчёту будет приложен скриншот всего экрана."
    )
    def test_info_screen_initial_state(self, appium_driver, open_info_screen, info_screen):
        # Ищем кнопку "Открыть страницу на GitHub"
        open_github_button = info_screen.find(InfoScreenLocators.GitHubPageButton)
        with allure.step("Кнопка «Открыть страницу на GitHub» отображается на экране"):
            assert open_github_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(open_github_button)

        # Ищем кнопку "Прочитать политику конфиденциальности"
        read_privacy_policy_button = info_screen.find(InfoScreenLocators.PrivacyPolicyButton)
        with allure.step("Кнопка «Прочитать политику конфиденциальности» отображается на экране"):
            assert read_privacy_policy_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(read_privacy_policy_button)

        # Ищем кнопку "Связаться с разработчиком"
        contact_the_developer_button = info_screen.find(InfoScreenLocators.ContactTheDeveloperButton)
        with allure.step("Кнопка «Связаться с разработчиком» отображается на экране"):
            assert contact_the_developer_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(contact_the_developer_button)

        # Ищем кнопку "Оценить приложение"
        rate_the_app_button = info_screen.find(InfoScreenLocators.RateTheAppButton)
        with allure.step("Кнопка «Оценить приложение» отображается на экране"):
            assert rate_the_app_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(rate_the_app_button)

        # Ищем кнопку "Поделиться приложением"
        share_the_app_button = info_screen.find(InfoScreenLocators.ShareTheAppButton)
        with allure.step("Кнопка «Поделиться приложением» отображается на экране"):
            assert share_the_app_button.is_displayed() == True, make_and_attach_screenshot(appium_driver)
            attach_element_screenshot(share_the_app_button)
