from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def test_validLogin():
    base_url = "https://courses.letskodeit.com/courses/javascript-for-beginners/buy"
    driver = webdriver.Firefox(executable_path="D:\\Selenium\\geckodriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)

    driver.execute_script("window.scrollBy(0, 750);")

    frames = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//iframe[contains(@name, '__privateStripeFrame')]")))
    print(len(frames))
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='Secure card number input frame']"))
    card_num = driver.find_element_by_xpath("//input[@name='cardnumber']")
    card_num.send_keys("10")
    #
    #
    # emailField = driver.find_element(By.NAME, "exp-date")
    # emailField.send_keys("1220")
    #
    # passwordField = driver.find_element(By.NAME, "cvc")
    # passwordField.send_keys("10")

    # loginButton = driver.find_element(By.NAME, "commit")
    # loginButton.click()

    # userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
    # if userIcon is not None:
    #     print("Login Successful")
    # else:
    #     print("Login Failed")


if __name__ == "__main__":
    test_validLogin()
