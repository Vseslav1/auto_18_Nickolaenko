from selenium.webdriver.common.by import By


class Assertions:


    def __init__(self, driver):
        self.driver = driver


    def assert_that_element_is_visible(self, selector, by=By.XPATH):
        assert self.driver.find_element(by, selector)