import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    # Locators. Class variable shared by all instances
    _search_box = "course"                                          # id
    _course = "//h4[contains(.,'{0}')]"                             # xpath
    # _all_courses = "dynamic-heading"
    _enroll_button = "//button[contains(.,'Enroll in Course')]"     # xpath
    _cc_num = "cardnumber"     # name
    _cc_exp = "exp-date"       # name
    _cc_cvv = "cvc"            # name
    _sel_country = "//select[@name='country-list']/option[text()='{0}']"    # xpath
    _submit_buy = "(//button[contains(.,'Buy')])[1]"                        # xpath
    _enroll_error_msg = "//span[contains(.,'Your card number is invalid.')]"     # xpath
                        # // span[contains(., 'Your card number is invalid.')]
    # _all_courses = 'ALL COURSES'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Element Interactions
    def enter_course_name(self, name):
        self.send_key(name, 'name', self._search_box)

    def select_course(self, full_name):
        self.element_click('xpath', self._course.format(full_name))

    def click_on_enroll_button(self):
        self.element_click('xpath', self._enroll_button)

    def enter_card_num(self, num):
        # self.switch_to_frame(name="Secure card number input frame")
        self.send_key_card(num, 'name', self._cc_num, title="Secure card number input frame")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        # self.switch_to_frame(name="Secure expiration date input frame")
        self.send_key_card(exp, 'name', self._cc_exp, title="Secure expiration date input frame")
        self.switch_to_default_content()

    def enter_card_cvv(self, cvv):
        # self.switch_to_frame(name="Secure CVC input frame")
        self.send_key_card(cvv, 'name', self._cc_cvv, title="Secure CVC input frame")
        self.switch_to_default_content()

    def sel_country(self, country):
        self.element_click('xpath', self._sel_country.format(country))

    def click_buy_button(self):
        self.element_click('xpath', self._enroll_button)

    def enter_CreditCard_info(self, num, exp, cvv, country):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.sel_country(country)

    def enroll_course(self, num="", exp="", cvv="", country="Netherlands"):
        self.click_on_enroll_button()
        self.web_scroll('down', 700)
        self.enter_CreditCard_info(num, exp, cvv, country)

    def verify_enroll_failed(self):
        result = self.is_enable(locator_type='xpath', locator=self._submit_buy, info="BUY button")
        return not result

    # def click_all_courses_btn(self):
    #     self.element_click('linktext', self._all_courses)
