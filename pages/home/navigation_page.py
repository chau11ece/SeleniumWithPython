from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from base.basepage import BasePage


# class SignInPage(SeleniumDriver):
class NavigationPage(BasePage):
    # Locators. Class variable shared by all instances
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _my_courses = "MY COURSES"
    _user_icon = "//img[@src='/images/default-user-profile-pic.png']"

    # Class variable shared by all instances
    def navigate_to_all_courses(self):
        self.element_click('linktext', self._all_courses)

    def navigate_to_support(self):
        self.element_click('linktext', self._support)

    def navigate_to_my_courses(self):
        self.element_click('linktext', self._my_courses)

    def navigate_to_user_setting(self):
        user_setting_element = self.wait_for_element(locator_type="xpath", locator=self._user_icon, timeout=10, poll_frequency=1)
        self.element_click(user_setting_element)
        # self.element_click('xpath', self._user_icon)
