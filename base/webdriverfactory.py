import os

from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_inst(self):
        """
        Get Driver Instance based on the browser configuration
        :return:
        """
        base_url = "https://courses.letskodeit.com"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            # driver = webdriver.Firefox()
            driver = webdriver.Firefox(executable_path="D:\\Selenium\\geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "D:\\Selenium\\chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            # driver.set_window_size(,)
        else:
            driver = webdriver.Firefox()
 
        # Setting Driver Implicit Time Out for an element
        driver.implicitly_wait(2)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver
