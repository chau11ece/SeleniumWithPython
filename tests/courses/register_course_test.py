import unittest
import pytest
from pages.courses.register_course_page import RegisterCoursesPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("one_time_setup", "setup")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.courses = RegisterCoursesPage(self.driver)
        self.tstt = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.courses.enter_course_name("Java")
        self.courses.select_course("JavaScript for beginners")
        self.courses.enroll_course("1234 5678 9012 3456", "1221", "1234", "United States")
        buy_result = self.courses.verify_enroll_failed()
        self.tstt.mark_final("test_invalid_enrollment", buy_result, "Enrollment Failed Verification")
