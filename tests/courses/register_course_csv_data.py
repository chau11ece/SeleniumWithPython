import unittest
import pytest
from pages.courses.register_course_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class RegisterCoursesCSVTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.courses = RegisterCoursesPage(self.driver)
        self.tstt = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self) -> None:
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    # @data(("JavaScript for beginners", "1234 5678 9012 3456", "1221", "1234", "United States"),
    #       ("Rest API Automation With Rest Assured", "1234 5678 9012 3456", "1221", "1234", "United States")
    #       )
    @data(*get_csv_data("C:\\Users\\Administrator\\PycharmProjects\\pythonProject1\\testdata.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, cc_country):
        self.courses.enter_course_name(course_name)
        self.courses.select_course(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, cc_country)
        buy_result = self.courses.verify_enroll_failed()
        self.tstt.mark_final("test_invalid_enrollment", buy_result, "Enrollment Failed Verification")
        # self.courses.click_all_courses_btn()
