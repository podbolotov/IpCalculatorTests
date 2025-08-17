import allure
import pytest

from lib.data.calculatuon_cases import get_target_networks_cases
from lib.tools.ip_tools import generate_valid_ip
from lib.ui.screens.calc_screen import CalcScreenLocators
from tests.calculation_tests.addon_reusable_calculation_tests import reusable_calculation_tests


@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты вычислений")
@allure.tag("Slow", "Stable")
class TestMainCalculationTests:
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @pytest.mark.parametrize('iterations', range(1, 21))
    @allure.sub_suite("Вычисление случайных подсетей")
    def test_random_ip_calculations(self, appium_driver, iterations, calc_screen):
        # Генерируем случайный валидный IP
        generated_ip = generate_valid_ip()

        allure.dynamic.title(f"Вычисление случайной подсети ({generated_ip})")
        allure.dynamic.description(
            f"Данный тест проводит тестирование вычисления случайной подсети в 20 итераций.\n\n"
            f"Номер итерации: {iterations}.\n"
            f"Тестируемая подсеть: {generated_ip}.\n\n"
            f"Данный тест проверяет только корректность вычислений, тестирование локализации или темы оформления в его "
            f"пределах не производится.\n"
            f"Тестирование корректности вычислений производится следующим способом: \n"
            f"1. На стороне тестового фреймворка генерируется случайный (корректный) IP-адрес.\n"
            f"2. На стороне тестового фреймворка вычисляются все данные подсети, вычисление которых ожидается от "
            f"приложения.\n"
            f"3. Сгенерированный IP-адрес вводится на устройство.\n"
            f"4. На устройстве инициализируется вычисление данных подсети.\n"
            f"5. Тест производит сверку всех рассчитанных на устройстве данных подсети с данными, ранее рассчитанными "
            f"на стороне тестового фреймворка.\n\n"
            f"При возникновении ошибки к отчёту будет приложен скриншот экрана на момент регистрации ошибки."
        )

        # Вводим сгенерированный IP в приложение
        calc_screen.enter_ip_address(address=generated_ip)

        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        reusable_calculation_tests(
            ip=generated_ip,
            calc_screen_operations=calc_screen,
            calc_screen_locators=CalcScreenLocators,
            appium_driver=appium_driver
        )

    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.sub_suite("Вычисление предопределённых сетей")
    @pytest.mark.parametrize('case', get_target_networks_cases())
    def test_pattern_calculations(self, appium_driver, case, calc_screen):
        # Получаем тестируемый IP из кейса
        case_ip = case.ip_with_cidr

        allure.dynamic.title(f"{case.title} ({case.ip_with_cidr})")
        allure.dynamic.description(case.description)

        # Вводим сгенерированный IP в приложение
        calc_screen.enter_ip_address(address=case_ip)

        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        reusable_calculation_tests(
            ip=case_ip,
            calc_screen_operations=calc_screen,
            calc_screen_locators=CalcScreenLocators,
            appium_driver=appium_driver
        )
