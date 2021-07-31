import unittest
from tests.home.signin_test import SignInTest
from tests.courses.register_course_csv_data import RegisterCoursesCSVTests

# Get all tests from the test classes
login_testcases = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
register_testcases = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([login_testcases, register_testcases])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
