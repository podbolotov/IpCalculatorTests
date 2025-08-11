from appium.webdriver.common.appiumby import AppiumBy
from lib.tools.element_finders import find_by_locator


class CalcScreenLocators:
    """ Данный класс содержит локаторы компонентов экрана "Калькулятор". """

    # Placeholders
    class PlaceholderWidget:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("EmptyStateWidget")'

    class PlaceholderImage:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("EmptyStateWidgetImage")'

    class PlaceholderText:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("EmptyStateWidgetLargeText")'

    # Containers
    class ResultListContainer:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidget")'

    class CidrListContainer:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListContainer")'

    class IPInputContainer:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("OctetTextFieldsWidget")'

    # Inputs
    class IPInputFirstOctet:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("OctetTextField+0")'

    class IPInputFirstOctetPlaceholderValue:
        type = AppiumBy.XPATH
        value = '//android.widget.EditText[@resource-id="OctetTextField+0"]/android.widget.TextView'

    class IPInputSecondOctet:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("OctetTextField+1")'

    class IPInputSecondOctetPlaceholderValue:
        type = AppiumBy.XPATH
        value = '//android.widget.EditText[@resource-id="OctetTextField+1"]/android.widget.TextView'

    class IPInputThirdOctet:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("OctetTextField+2")'

    class IPInputThirdOctetPlaceholderValue:
        type = AppiumBy.XPATH
        value = '//android.widget.EditText[@resource-id="OctetTextField+2"]/android.widget.TextView'

    class IPInputFourthOctet:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("OctetTextField+3")'

    class IPInputFourthOctetPlaceholderValue:
        type = AppiumBy.XPATH
        value = '//android.widget.EditText[@resource-id="OctetTextField+3"]/android.widget.TextView'

    # Result Items

    class ResultIPAddress:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+IPAddress")'

    class ResultIPAddressLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+IPAddress"]/android.widget.TextView[1]'

    class ResultIPAddressValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+IPAddress"]/android.widget.TextView[2]'

    class ResultCIDRPrefix:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+CIDRPrefix")'

    class ResultCIDRPrefixLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+CIDRPrefix"]/android.widget.TextView[1]'

    class ResultCIDRPrefixValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+CIDRPrefix"]/android.widget.TextView[2]'

    class ResultSubnetMask:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+SubnetMask")'

    class ResultSubnetMaskLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+SubnetMask"]/android.widget.TextView[1]'

    class ResultSubnetMaskValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+SubnetMask"]/android.widget.TextView[2]'

    class ResultWildcardMask:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+WildcardMask")'

    class ResultWildcardMaskLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+WildcardMask"]/android.widget.TextView[1]'

    class ResultWildcardMaskValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+WildcardMask"]/android.widget.TextView[2]'

    class ResultNetworkIPAddress:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+NetworkIPAddress")'

    class ResultNetworkIPAddressLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+NetworkIPAddress"]/android.widget.TextView[1]'

    class ResultNetworkIPAddressValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+NetworkIPAddress"]/android.widget.TextView[2]'

    class ResultBroadcastIPAddress:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+BroadcastIPAddress")'

    class ResultBroadcastIPAddressLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+BroadcastIPAddress"]/android.widget.TextView[1]'

    class ResultBroadcastIPAddressValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+BroadcastIPAddress"]/android.widget.TextView[2]'

    class ResultMaxPossibleHosts:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+MaxPossibleHosts")'

    class ResultMaxPossibleHostsLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+MaxPossibleHosts"]/android.widget.TextView[1]'

    class ResultMaxPossibleHostsValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+MaxPossibleHosts"]/android.widget.TextView[2]'

    class ResultUsableHosts:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+UsableHosts")'

    class ResultUsableHostsLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+UsableHosts"]/android.widget.TextView[1]'

    class ResultUsableHostsValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+UsableHosts"]/android.widget.TextView[2]'

    class ResultFirstHost:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+FirstHost")'

    class ResultFirstHostLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+FirstHost"]/android.widget.TextView[1]'

    class ResultFirstHostValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+FirstHost"]/android.widget.TextView[2]'

    class ResultLastHost:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ContentStateWidgetListItem+LastHost")'

    class ResultLastHostLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+LastHost"]/android.widget.TextView[1]'

    class ResultLastHostValue:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ContentStateWidgetListItem+LastHost"]/android.widget.TextView[2]'

    # CIDR List Items
    class Subnet0:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+0")'

    class Subnet1:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+1")'

    class Subnet2:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+2")'

    class Subnet3:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+3")'

    class Subnet4:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+4")'

    class Subnet5:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+5")'

    class Subnet6:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+6")'

    class Subnet7:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+7")'

    class Subnet8:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+8")'

    class Subnet9:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+9")'

    class Subnet10:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+10")'

    class Subnet11:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+11")'

    class Subnet12:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+12")'

    class Subnet13:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+13")'

    class Subnet14:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+14")'

    class Subnet15:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+15")'

    class Subnet16:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+16")'

    class Subnet17:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+17")'

    class Subnet18:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+18")'

    class Subnet19:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+19")'

    class Subnet20:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+20")'

    class Subnet21:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+21")'

    class Subnet22:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+22")'

    class Subnet23:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+23")'

    class Subnet24:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+24")'

    class Subnet25:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+25")'

    class Subnet26:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+26")'

    class Subnet27:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+27")'

    class Subnet28:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+28")'

    class Subnet29:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+29")'

    class Subnet30:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+30")'

    class Subnet31:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+31")'

    class Subnet32:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("SubnetMaskListWidgetItem+32")'

    # Buttons
    class CIDRButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("CIDRWidget")'

    class CIDRButtonPlaceholderText:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("CIDRWidgetPlaceholderText")'

    class CIDRButtonValueText:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("CIDRWidgetValueText")'

    class CalculateButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("CalculateButton")'

    class CalculateButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="CalculateButton"]/android.widget.TextView'

    class ShareButton:
        type = AppiumBy.ANDROID_UIAUTOMATOR
        value = 'new UiSelector().resourceId("ShareButton")'

    class ShareButtonLabel:
        type = AppiumBy.XPATH
        value = '//android.view.View[@resource-id="ShareButton"]/android.widget.TextView'


class CalcScreenOperations:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = find_by_locator(self.driver, locator)
        element.screenshot = element.screenshot_as_base64
        return element

    def scroll_to_list_item(
            self,
            looked_object_locator,
            container_locator,
            initial_direction = 'down'
    ):

        self.driver.implicitly_wait(1)

        scroll_container_locator = container_locator

        scroll_down = f"new UiScrollable({scroll_container_locator.value}).scrollForward()"
        scroll_up = f"new UiScrollable({scroll_container_locator.value}).scrollBackward()"

        print(f"\nНачинаем поиск элемента с id {looked_object_locator.value}.")

        def is_element_displayed(looked_object):
            state = False
            try:
                state = (self.driver.find_element(looked_object.type, looked_object.value).is_displayed())
                return state
            except Exception as e:
                ex = e
                print("При запуске поиска элемент не отображается. ")
                return state

        scroll_locator = scroll_down

        if initial_direction == 'up':
            scroll_locator = scroll_up

        tries = 1
        while not is_element_displayed(looked_object_locator):
            print(f"Делаем свайп (попытка {tries})...")
            self.driver.find_element(
                by=AppiumBy.ANDROID_UIAUTOMATOR,
                value=scroll_locator
            )
            tries = tries + 1
            if tries == 4:
                scroll_locator = scroll_up
                if initial_direction == 'up':
                    scroll_locator = scroll_down
                print(f"Пробуем поменять направление на обратное...")
            if tries == 7:
                break

        if not is_element_displayed(looked_object_locator):
            self.driver.implicitly_wait(60)
            raise RuntimeError(f"Элемент с id {looked_object_locator.value} найти не удалось.")
        else:
            self.driver.implicitly_wait(60)
            print(f"Элемент с id {looked_object_locator.value} найден.")

    def enter_ip_address(self, address: str = "192.168.0.1", cidr: str = "24"):

        ip, *cidr = address.split("/")

        oc1, oc2, oc3, oc4 = ip.split(".")

        subnet = '24'
        if len(cidr) == 1:
            subnet = cidr[0]

        oc1_input = self.find(CalcScreenLocators.IPInputFirstOctet)
        oc1_input.click()
        oc1_input.send_keys(oc1)

        oc2_input = self.find(CalcScreenLocators.IPInputSecondOctet)
        oc2_input.click()
        oc2_input.send_keys(oc2)

        oc3_input = self.find(CalcScreenLocators.IPInputThirdOctet)
        oc3_input.click()
        oc3_input.send_keys(oc3)

        oc4_input = self.find(CalcScreenLocators.IPInputFourthOctet)
        oc4_input.click()
        oc4_input.send_keys(oc4)

        cidr_locator = CalcScreenLocators.__getattribute__(CalcScreenLocators, f'Subnet{subnet}')

        cidr_button = self.find(CalcScreenLocators.CIDRButton)
        cidr_button.click()

        self.scroll_to_list_item(cidr_locator, CalcScreenLocators.CidrListContainer)

        subnet_list_item = self.find(cidr_locator)
        subnet_list_item.click()
