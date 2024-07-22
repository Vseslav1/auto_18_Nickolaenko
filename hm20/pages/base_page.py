from selenium.webdriver.common.by import By
from hm20.helpers.assertion import Assertions


class BasePage(Assertions):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.assertions = Assertions(driver)

    def click(self, selector):
        element = self.driver.find_element(By.XPATH, selector)
        element.click()


    def fill(self, selector, text):
        element = self.driver.find_element(By.XPATH, selector)
        element.send_keys(text)


    def save_screenshot(self, name):
        self.driver.save_screenshot(name)