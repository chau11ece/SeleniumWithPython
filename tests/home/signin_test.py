from pages.home.signin_page import SignInPage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("one_time_setup", "setup")
class SignInTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.sigi = SignInPage(self.driver)
        self.tstt = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_signin(self):
        tit_result = self.sigi.verify_title()
        self.tstt.mark(tit_result, "Matching Title")
        self.sigi.sign_in("test@email.com", "abcabc")
        lg_result = self.sigi.verify_login_successful()
        self.tstt.mark_final("test_valid_login", lg_result, "Successful Sign In")

    @pytest.mark.run(order=1)
    def test_invalid_signin(self):
        self.sigi.logout()
        self.sigi.sign_in("test@email.com", "123456")
        lg_result = self.sigi.verify_login_failed()
        assert lg_result == True
