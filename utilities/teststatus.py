from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        :param driver:
        """
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            # result = True | False | None
            if result is not None:  # result = True | False
                if result:  # True
                    self.result_list.append("PASSED")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + result_message)
                else:   # False
                    self.result_list.append("FAILED")
                    self.log.error("### VERIFICATION FAILED :: " + result_message)
                    self.screen_shot(result_message)
            else:   # result = None
                self.result_list.append("FAILED")
                self.log.error("### VERIFICATION FAILED :: " + result_message)
                self.screen_shot(result_message)
        except ValueError:
            self.result_list.append("FAILED")
            self.log.error("### Exception Occurred !!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        :param test_name:
        :param result:
        :param result_message:
        :return:
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a tes case
        This needs to be called at least once in a test case
        This should be final test status of the test data
        :param test_name:
        :param result:
        :param result_message:
        :return:
        """
        self.set_result(result, result_message)
        self.log.info(self.result_list)

        if "FAILED" in self.result_list:
            self.log.error(test_name + "### TEST FAILED")
            self.result_list.clear()
            assert True == False
        else:
            self.log.error(test_name + "### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True == True
