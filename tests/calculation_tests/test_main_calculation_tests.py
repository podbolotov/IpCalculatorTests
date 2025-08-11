import allure
import pytest

from lib.data.calculatuon_cases import get_calculation_case
from lib.data.localized_strings import AvailableLocales
from lib.tools.screenshotter import attach_element_screenshot, make_and_attach_screenshot
from lib.ui.screens.calc_screen import CalcScreenLocators
from lib.tools.ip_tools import ip_calculator, generate_valid_ip_with_cidr


@allure.parent_suite("Тесты вычислений")
@allure.suite("Основные сценарии вычисления")
# @pytest.mark.parametrize('locales', [AvailableLocales.EN, AvailableLocales.RU, AvailableLocales.KK], indirect=True)
# @pytest.mark.parametrize('locales', [AvailableLocales.RU], indirect=True)

class TestMainCalculationTests:
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('iterations', range(1, 4))
    @allure.sub_suite("Вычисление случайных подсетей")
    def test_random_ip_calculations(self, appium_driver, iterations, calc_screen):
        # Генерируем случайный валидный IP
        generated_ip = generate_valid_ip_with_cidr()

        allure.dynamic.title(f"Вычисление случайной подсети ({generated_ip})")
        allure.dynamic.description(
            f"Данный тест проводит тестирование вычисления случайной подсети в 3 итерации.\n\n"
            f"Номер итерации: {iterations}.\n"
            f"Тестируемая подсеть: {generated_ip}.\n\n"
            f"Данный проверяет только корректность вычислений, тестирование локализации или темы оформления в его "
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
        calc_screen.enter_ip_address(generated_ip)

        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        with allure.step("Проверка корректности вычисления"):
            # Производим локальное вычисление для данного IP
            local_calculation_result = ip_calculator(generated_ip)

            allure.attach(str(f'''
IP адрес: {local_calculation_result.ip_address}
CIDR нотация: {local_calculation_result.cidr}
Маска подсети: {local_calculation_result.network_mask}
Обратная маска: {local_calculation_result.wildcard_mask}
Адрес сети: {local_calculation_result.network_address}
Широковещательный адрес: {local_calculation_result.broadcast_address}
Всего адресов: {local_calculation_result.total_addresses}
Рабочих узлов: {local_calculation_result.total_hosts}
Первый хост: {local_calculation_result.first_host}
Последний хост: {local_calculation_result.last_host}'''), 'Результат локального вычисления')

            with allure.step("IP адрес соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultIPAddressValue, CalcScreenLocators.ResultListContainer,
                    initial_direction='up')
                ip_address = calc_screen.find(CalcScreenLocators.ResultIPAddressValue).text
                allure.attach(ip_address, "Полученное значение")
                assert ip_address == local_calculation_result.ip_address, make_and_attach_screenshot(appium_driver)

            with allure.step("CIDR нотация соответствует вычисленной локально"):
                cidr = calc_screen.find(CalcScreenLocators.ResultCIDRPrefixValue).text
                allure.attach(cidr, "Полученное значение")
                assert cidr == local_calculation_result.cidr, make_and_attach_screenshot(appium_driver)

            with allure.step("Маска подсети соответствует вычисленной локально"):
                network_mask = calc_screen.find(CalcScreenLocators.ResultSubnetMaskValue).text
                allure.attach(network_mask, "Полученное значение")
                assert network_mask == local_calculation_result.network_mask, make_and_attach_screenshot(appium_driver)

            with allure.step("Обратная маска соответствует вычисленной локально"):
                wildcard_mask = calc_screen.find(CalcScreenLocators.ResultWildcardMaskValue).text
                allure.attach(wildcard_mask, "Полученное значение")
                assert wildcard_mask == local_calculation_result.wildcard_mask, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Адрес сети соответствует вычисленному локально"):
                network_address = calc_screen.find(CalcScreenLocators.ResultNetworkIPAddressValue).text
                allure.attach(network_address, "Полученное значение")
                assert network_address == local_calculation_result.network_address, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Широковещательный адрес соответствует вычисленному локально"):
                broadcast_address = calc_screen.find(CalcScreenLocators.ResultBroadcastIPAddressValue).text
                allure.attach(broadcast_address, "Полученное значение")
                assert broadcast_address == local_calculation_result.broadcast_address, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Общее количество адресов соответствует вычисленному локально"):
                total_addresses = calc_screen.find(CalcScreenLocators.ResultMaxPossibleHostsValue).text
                total_addresses = total_addresses.replace(" ", "")
                allure.attach(total_addresses, "Полученное значение")
                assert total_addresses == local_calculation_result.total_addresses, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Количество рабочих хостов соответствует вычисленному локально"):
                total_hosts = calc_screen.find(CalcScreenLocators.ResultUsableHostsValue).text
                total_hosts = total_hosts.replace(" ", "")
                allure.attach(total_hosts, "Полученное значение")
                assert total_hosts == local_calculation_result.total_hosts, make_and_attach_screenshot(appium_driver)

            with allure.step("Первый хост соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultFirstHostValue, CalcScreenLocators.ResultListContainer)
                first_host = calc_screen.find(CalcScreenLocators.ResultFirstHostValue).text
                allure.attach(first_host, "Полученное значение")
                assert first_host == local_calculation_result.first_host, make_and_attach_screenshot(appium_driver)

            with allure.step("Последний хост соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultLastHostValue, CalcScreenLocators.ResultListContainer)
                last_host = calc_screen.find(CalcScreenLocators.ResultLastHostValue).text
                allure.attach(last_host, "Полученное значение")
                assert last_host == local_calculation_result.last_host, make_and_attach_screenshot(appium_driver)

    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.sub_suite("Вычисление предопределённых сетей")
    @pytest.mark.parametrize('case', get_calculation_case())
    def test_pattern_calculations(self, appium_driver, case, calc_screen):

        case_ip = case.ip_with_cidr

        allure.dynamic.title(f"{case.title} ({case.ip_with_cidr})")
        allure.dynamic.description(case.description)

        # Вводим сгенерированный IP в приложение
        calc_screen.enter_ip_address(case_ip)

        # Нажимаем на кнопку "Вычислить"
        calc_screen.find(CalcScreenLocators.CalculateButtonLabel).click()

        with allure.step("Проверка корректности вычисления"):
            # Производим локальное вычисление для данного IP
            local_calculation_result = ip_calculator(case_ip)

            allure.attach(str(f'''
IP адрес: {local_calculation_result.ip_address}
CIDR нотация: {local_calculation_result.cidr}
Маска подсети: {local_calculation_result.network_mask}
Обратная маска: {local_calculation_result.wildcard_mask}
Адрес сети: {local_calculation_result.network_address}
Широковещательный адрес: {local_calculation_result.broadcast_address}
Всего адресов: {local_calculation_result.total_addresses}
Рабочих узлов: {local_calculation_result.total_hosts}
Первый хост: {local_calculation_result.first_host}
Последний хост: {local_calculation_result.last_host}'''), 'Результат локального вычисления')

            with allure.step("IP адрес соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultIPAddressValue, CalcScreenLocators.ResultListContainer,
                    initial_direction='up')
                ip_address = calc_screen.find(CalcScreenLocators.ResultIPAddressValue).text
                allure.attach(ip_address, "Полученное значение")
                assert ip_address == local_calculation_result.ip_address, make_and_attach_screenshot(appium_driver)

            with allure.step("CIDR нотация соответствует вычисленной локально"):
                cidr = calc_screen.find(CalcScreenLocators.ResultCIDRPrefixValue).text
                allure.attach(cidr, "Полученное значение")
                assert cidr == local_calculation_result.cidr, make_and_attach_screenshot(appium_driver)

            with allure.step("Маска подсети соответствует вычисленной локально"):
                network_mask = calc_screen.find(CalcScreenLocators.ResultSubnetMaskValue).text
                allure.attach(network_mask, "Полученное значение")
                assert network_mask == local_calculation_result.network_mask, make_and_attach_screenshot(appium_driver)

            with allure.step("Обратная маска соответствует вычисленной локально"):
                wildcard_mask = calc_screen.find(CalcScreenLocators.ResultWildcardMaskValue).text
                allure.attach(wildcard_mask, "Полученное значение")
                assert wildcard_mask == local_calculation_result.wildcard_mask, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Адрес сети соответствует вычисленному локально"):
                network_address = calc_screen.find(CalcScreenLocators.ResultNetworkIPAddressValue).text
                allure.attach(network_address, "Полученное значение")
                assert network_address == local_calculation_result.network_address, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Широковещательный адрес соответствует вычисленному локально"):
                broadcast_address = calc_screen.find(CalcScreenLocators.ResultBroadcastIPAddressValue).text
                allure.attach(broadcast_address, "Полученное значение")
                assert broadcast_address == local_calculation_result.broadcast_address, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Общее количество адресов соответствует вычисленному локально"):
                total_addresses = calc_screen.find(CalcScreenLocators.ResultMaxPossibleHostsValue).text
                total_addresses = total_addresses.replace(" ", "")
                allure.attach(total_addresses, "Полученное значение")
                assert total_addresses == local_calculation_result.total_addresses, make_and_attach_screenshot(
                    appium_driver)

            with allure.step("Количество рабочих хостов соответствует вычисленному локально"):
                total_hosts = calc_screen.find(CalcScreenLocators.ResultUsableHostsValue).text
                total_hosts = total_hosts.replace(" ", "")
                allure.attach(total_hosts, "Полученное значение")
                assert total_hosts == local_calculation_result.total_hosts, make_and_attach_screenshot(appium_driver)

            with allure.step("Первый хост соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultFirstHostValue, CalcScreenLocators.ResultListContainer)
                first_host = calc_screen.find(CalcScreenLocators.ResultFirstHostValue).text
                allure.attach(first_host, "Полученное значение")
                assert first_host == local_calculation_result.first_host, make_and_attach_screenshot(appium_driver)

            with allure.step("Последний хост соответствует вычисленному локально"):
                calc_screen.scroll_to_list_item(
                    CalcScreenLocators.ResultLastHostValue, CalcScreenLocators.ResultListContainer)
                last_host = calc_screen.find(CalcScreenLocators.ResultLastHostValue).text
                allure.attach(last_host, "Полученное значение")
                assert last_host == local_calculation_result.last_host, make_and_attach_screenshot(appium_driver)
