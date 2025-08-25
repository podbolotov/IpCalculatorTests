import allure

from lib.tools.ip_tools import ip_calculator
from lib.tools.screenshotter import make_and_attach_screenshot
from lib.ui.screens.calc_screen import ScrollDirections


def reusable_calculation_tests(ip, calc_screen_operations, calc_screen_locators, appium_driver):
    """
    Данный метод группирует переиспользуемый набор тестов, который вызывается из разных сценариев, связанных
    с проверкой корректности вычислений.

    :param ip: Тестируемый IP (в формате xxx.xxx.xxx.xxx/xx)
    :param calc_screen_operations: Объект фикстуры с инициализированным экраном "Калькулятор"
    :param calc_screen_locators: Локаторы экрана "Калькулятор"
    :param appium_driver: Объект фикстуры с инициализированным драйвером.
    """
    with allure.step("Проверка корректности вычисления"):
        # Производим локальное вычисление для данного IP
        local_calculation_result = ip_calculator(ip)

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
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultIPAddressValue, calc_screen_locators.ResultListContainer,
                initial_direction=ScrollDirections.UP)
            ip_address = calc_screen_operations.find(calc_screen_locators.ResultIPAddressValue).text
            allure.attach(ip_address, "Полученное значение")
            assert ip_address == local_calculation_result.ip_address, make_and_attach_screenshot(appium_driver)

        with allure.step("CIDR нотация соответствует вычисленной локально"):
            cidr = calc_screen_operations.find(calc_screen_locators.ResultCIDRPrefixValue).text
            allure.attach(cidr, "Полученное значение")
            assert cidr == local_calculation_result.cidr, make_and_attach_screenshot(appium_driver)

        with allure.step("Маска подсети соответствует вычисленной локально"):
            network_mask = calc_screen_operations.find(calc_screen_locators.ResultSubnetMaskValue).text
            allure.attach(network_mask, "Полученное значение")
            assert network_mask == local_calculation_result.network_mask, make_and_attach_screenshot(appium_driver)

        with allure.step("Обратная маска соответствует вычисленной локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultWildcardMaskValue, calc_screen_locators.ResultListContainer)
            wildcard_mask = calc_screen_operations.find(calc_screen_locators.ResultWildcardMaskValue).text
            allure.attach(wildcard_mask, "Полученное значение")
            assert wildcard_mask == local_calculation_result.wildcard_mask, make_and_attach_screenshot(
                appium_driver)

        with allure.step("Адрес сети соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultNetworkIPAddressValue, calc_screen_locators.ResultListContainer)
            network_address = calc_screen_operations.find(calc_screen_locators.ResultNetworkIPAddressValue).text
            allure.attach(network_address, "Полученное значение")
            assert network_address == local_calculation_result.network_address, make_and_attach_screenshot(
                appium_driver)

        with allure.step("Широковещательный адрес соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultBroadcastIPAddressValue, calc_screen_locators.ResultListContainer)
            broadcast_address = calc_screen_operations.find(calc_screen_locators.ResultBroadcastIPAddressValue).text
            allure.attach(broadcast_address, "Полученное значение")
            assert broadcast_address == local_calculation_result.broadcast_address, make_and_attach_screenshot(
                appium_driver)

        with allure.step("Общее количество адресов соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultMaxPossibleHostsValue, calc_screen_locators.ResultListContainer)
            total_addresses = calc_screen_operations.find(calc_screen_locators.ResultMaxPossibleHostsValue).text
            total_addresses = total_addresses.replace(" ", "")
            allure.attach(total_addresses, "Полученное значение")
            assert total_addresses == local_calculation_result.total_addresses, make_and_attach_screenshot(
                appium_driver)

        with allure.step("Количество рабочих хостов соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultUsableHostsValue, calc_screen_locators.ResultListContainer)
            total_hosts = calc_screen_operations.find(calc_screen_locators.ResultUsableHostsValue).text
            total_hosts = total_hosts.replace(" ", "")
            allure.attach(total_hosts, "Полученное значение")
            assert total_hosts == local_calculation_result.total_hosts, make_and_attach_screenshot(appium_driver)

        with allure.step("Первый хост соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultFirstHostValue, calc_screen_locators.ResultListContainer)
            first_host = calc_screen_operations.find(calc_screen_locators.ResultFirstHostValue).text
            allure.attach(first_host, "Полученное значение")
            assert first_host == local_calculation_result.first_host, make_and_attach_screenshot(appium_driver)

        with allure.step("Последний хост соответствует вычисленному локально"):
            calc_screen_operations.scroll_to_list_item(
                calc_screen_locators.ResultLastHostValue, calc_screen_locators.ResultListContainer)
            last_host = calc_screen_operations.find(calc_screen_locators.ResultLastHostValue).text
            allure.attach(last_host, "Полученное значение")
            assert last_host == local_calculation_result.last_host, make_and_attach_screenshot(appium_driver)
