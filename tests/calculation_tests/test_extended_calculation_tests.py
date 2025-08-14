import allure
import pytest

from lib.data.calculatuon_cases import get_partial_filled_ips_cases
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.calc_screen import CalcScreenLocators
from tests.calculation_tests.addon_reusable_calculation_tests import reusable_calculation_tests


@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты вычислений")
@allure.sub_suite("Расширенные сценарии вычислений")
@allure.severity(severity_level=allure.severity_level.CRITICAL)
class TestExtendedCalculationTests:

    @allure.title("Вычисление с предзаполненным IP")
    @allure.description(
        f"Данный тест проводит тестирование вычисление подсети 192.168.1.1/24 без непосредственного ввода IP-адреса ("
        f"в таком случае должно быть использовано предзаполненное в полях ввода значение).\n\n"

        f"Данный тест проверяет только корректность вычислений, тестирование локализации или темы оформления в его "
        f"пределах не производится.\n"
        f"Тестирование корректности вычислений производится следующим способом: \n"

        f"1. На стороне тестового фреймворка вычисляются все данные подсети, вычисление которых ожидается от "
        f"приложения.\n"
        f"2. На устройстве инициализируется вычисление данных подсети.\n"
        f"3. Тест производит сверку всех рассчитанных на устройстве данных подсети с данными, ранее рассчитанными "
        f"на стороне тестового фреймворка.\n\n"
        f"При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки."
    )
    @allure.tag("Fast")
    def test_calculation_with_prefilled_ip(self, appium_driver, calc_screen):
        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        reusable_calculation_tests(
            ip="192.168.1.1/24",
            calc_screen_operations=calc_screen,
            calc_screen_locators=CalcScreenLocators,
            appium_driver=appium_driver
        )

    @allure.tag("Slow")
    @pytest.mark.parametrize('case', get_partial_filled_ips_cases())
    def test_calculation_with_partial_filled_ip(self, appium_driver, restart_before, case, calc_screen):
        case_title = case.case_title
        case_description_part = case.case_description_part
        ip_as_text = case.ip_as_text
        ip_as_list = case.ip_as_list

        allure.dynamic.title(case_title)

        allure.dynamic.description(
            f"Данный кейс проверяет корректность выполнения вычислений в случае, если ввод данных был осуществлён частично.\n"
            f"В данном кейсе {case_description_part}, а ожидаемый рассчётный IP равен значению \"{ip_as_text}\".\n\n"
            f"Данный тест проверяет только корректность вычислений, тестирование локализации или темы оформления в его "
            f"пределах не производится.\n"
            f"Тестирование корректности вычислений производится следующим способом: \n"
            f"1. На стороне тестового фреймворка генерируется случайный (корректный) IP-адреса "
            f"(без одного из октетов или без маски сети).\n"
            f"2. На стороне тестового фреймворка вычисляются все данные подсети, вычисление которых ожидается от "
            f"приложения.\n"
            f"3. Сгенерированный IP-адрес вводится на устройство (с пропуском соответствующего октета либо без выбора "
            f"маски сети).\n"
            f"4. На устройстве инициализируется вычисление данных подсети.\n"
            f"5. Тест производит сверку всех рассчитанных на устройстве данных подсети с данными, ранее рассчитанными "
            f"на стороне тестового фреймворка.\n\n"
            f"При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки."
        )

        calc_screen.partial_fill_ip_address(
            driver=appium_driver,
            oc1=ip_as_list[0],
            oc2=ip_as_list[1],
            oc3=ip_as_list[2],
            oc4=ip_as_list[3],
            cidr=ip_as_list[4]
        )

        make_and_attach_screenshot(driver=appium_driver, title="Скриншот экрана с введёнными данными перед "
                                                               "вычислением")

        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        reusable_calculation_tests(
            ip=ip_as_text,
            calc_screen_operations=calc_screen,
            calc_screen_locators=CalcScreenLocators,
            appium_driver=appium_driver
        )
