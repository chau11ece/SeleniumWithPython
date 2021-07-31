from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

os.remove("automation.log")


class SeleniumDriver:
    # Class variable shared by all instances
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def screen_shot(self, result_message):
        """
        Takes screenshot of the current open web page
        :param result_message:
        :return:
        """
        output_filename = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "..\screenshots\\"
        relative_filename = screenshot_dir + output_filename
        current_dir = os.path.dirname(__file__)
        dest_file = os.path.join(current_dir, relative_filename)
        dest_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            self.driver.save_screenshot(dest_file)
            self.log.info("Screenshot saved to directory: " + dest_file)
        except NameError:
            self.log.error("### Exception Occurred")
            print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            # print("Locator type: " + locator_type + " is not correct/ supported")
            self.log.info("Locator type: " + locator_type + " is not correct/ supported")
        return False

    def get_element(self, locator_type, locator):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            # print("Element found with locator_type: " + locator_type + " and locator: " + locator)
            self.log.info("Element found with locator_type: " + locator_type + " and locator: " + locator)
        except NameError:
            self.log.info("Element not found with locator_type: " + locator_type + " and locator: " + locator)
        return element

    def element_click(self, locator_type, locator):
        try:
            element = self.get_element(locator_type, locator)
            element.click()
            self.log.info("Clicked on element with locator_type: " + locator_type + " locator: " + locator)
        except NameError:
            print("Cannot click on element with locator_type: " + locator_type + " locator: " + locator)
            print_stack()

    # def drop_list_element(self, locator_type, locator):
    #     try:
    #         element = self.get_element(locator_type, locator)
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(element).perform()
    #         self.log.info("Clicked on element with locator_type: " + locator_type + " locator: " + locator)
    #     except NameError:
    #         print("Cannot click on element with locator_type: " + locator_type + " locator: " + locator)
    #         print_stack()

    def send_key(self, data, locator_type, locator):
        try:
            # self.log.info("Input data: " + data)
            element = self.get_element(locator_type, locator)
            # self.log.info("Element is visible? " + str(self.is_element_display(locator_type, locator, element)))
            element.send_keys(data)
            self.log.info("Sent data on element with locator_type: " + locator_type + " locator: " + locator)
        except NameError:
            self.log.info("Cannot send data on element with locator_type: " + locator_type + " locator: " + locator)
            print_stack()

    def send_key_card(self, data, locator_type, locator, title):
        try:
            # self.log.info("Input data: " + data)
            self.driver.switch_to.frame(
                self.driver.find_element_by_css_selector("iframe[title='{0}']".format(title)))
            element = self.get_element(locator_type, locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator_type: " + locator_type + " locator: " + locator)
        except NameError:
            self.log.info("Cannot send data on element with locator_type: " + locator_type + " locator: " + locator)
            print_stack()

    def is_element_present(self, by_type, locator):
        try:
            element = self.get_element(by_type, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except ValueError:
            print("Element not found")
            return False

    def elements_presence_check(self, by_type, locator):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except NameError:
            print("Element not found")
            return False

    def wait_for_element(self, locator_type, locator, timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element =
            print("Element appeared on the web page")
        except NameError:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def is_element_display(self, locator_type, locator, element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator_type and locator
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator_type, locator)

            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator_type: " + locator_type +
                              " locator: " + locator)
            else:
                self.log.info("Element not displayed with locator_type: " + locator_type +
                              " locator: " + locator)
            return is_displayed
        except NameError:
            print("Element not found")
            return False

    def get_element_list(self, locator_type, locator):
        """
        :param locator_type:
        :param locator:
        :return:
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(locator_type, locator)
            self.log.info("Element list found with locator_type: " + locator_type +
                          " and  locator: " + locator)
        except NameError:
            self.log.info("Element list not found with locator_type: " + locator_type +
                          " and  locator: " + locator)
        return element

    def get_text(self, locator_type, locator, element, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator_type, locator)

            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except NameError:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def web_scroll(self, direction="up", range=1000):
        """
        :param range:
        :param direction:
        :param self:
        :return:
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -{});".format(range))

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, {});".format(range))

    def switch_to_frame(self, id="", name="", index=None):
        """
        Switch to frame using element locator inside iframe
        :param id: id of the iframe
        :param name: name of the iframe
        :param index: index of the iframe
        :return:
        """

        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_to_default_content(self):
        """
        Switch to default content
        :return:
        """
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator_type="xpath", locator=""):
        """

        :param attribute: attribute whose values to find
        :param element: element whose attribute need to find
        :param locator_type: locator_type to find the element
        :param locator: locator of the element
        :return:
        """
        if locator:
            element = self.get_element(locator_type, locator)
        value = element.get_attribute(attribute)
        return value

    def is_enable(self, locator_type, locator, info=""):
        """
        Check if element is enabled
        :return:
        """
        element = self.get_element(locator_type, locator)
        disabled = False
        try:
            # is_enable() method is used to check if element is enabled or not. True/ False
            attribute_value = self.get_element_attribute_value(attribute="disabled", element=element)
            if attribute_value is not None:
                disabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(attribute="class", element=element)
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                disabled = not ("disabled" in value)
            if disabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except ValueError:
            self.log.error("Element :: '" + info + "' state could not be found")
        return disabled



