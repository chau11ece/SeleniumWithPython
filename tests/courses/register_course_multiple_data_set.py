import unittest
import pytest
from pages.courses.register_course_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.courses = RegisterCoursesPage(self.driver)
        self.tstt = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1221", "1234", "United States"),
          ("Rest API Automation With Rest Assured", "1234 5678 9012 3456", "1221", "1234", "United States")
          )
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv, cc_country):
        self.courses.enter_course_name(course_name)
        self.courses.select_course(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, cc_country)
        buy_result = self.courses.verify_enroll_failed()
        self.tstt.mark_final("test_invalid_enrollment", buy_result, "Enrollment Failed Verification")
        self.courses.click_all_courses_btn()
