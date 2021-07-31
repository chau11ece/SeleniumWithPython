import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.signin_page import SignInPage
from utilities.teststatus import TestStatus


TestStatus.__test__ = False


@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    print("Running ONE TIME setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_inst()
    si = SignInPage(driver)
    si.sign_in("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # driver.quit()
    print("Running ONE TIME tearDown")


@pytest.fixture()
def setup():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
