from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage


# class SignInPage(SeleniumDriver):
class SignInPage(BasePage):

    # Locators. Class variable shared by all instances
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _submit_button = "//input[@value='Login']"

    # Class variable shared by all instances
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # def get_login_link(self):
    #     return self.driver.find_element_by_link_text(self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element_by_id(self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element_by_id(self._password_field)
    #
    # def get_submit_button(self):
    #     return self.driver.find_element_by_xpath(self._login_button)

    def click_login_lnk(self):
        self.element_click('linktext', self._login_link)

    def enter_email(self, email):
        self.send_key(email, 'id', self._email_field)

    def enter_password(self, password):
        self.send_key(password, 'id', self._password_field)

    def click_submit_btn(self):
        self.element_click('xpath', self._submit_button)

    def sign_in(self, email, password):
        self.click_login_lnk()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_btn()

    def verify_login_successful(self):
        result = self.is_element_present('xpath', "//img[@src='/images/default-user-profile-pic.png']")
        return result

    def verify_login_failed(self):
        result = self.is_element_present('xpath', "//span[contains(.,'Your username or password is invalid. Please "
                                                  "try again.')]")
        return result

    def verify_title(self):
        return self.verify_page_title("Google")

    def logout(self):
        self.nav.navigate_to_user_setting()
        self.element_click('xpath', "//div[@class='dropdown open']//a[@href='/logout']")

