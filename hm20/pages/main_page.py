from selenium.webdriver.common.by import By
from hm20.pages.base_page import BasePage
from hm20.helpers.url import BASE_URL
from hm20.locators.locators import MarketYandexLocators


class MainPage(BasePage, MarketYandexLocators):


    def __init__(self, driver):
        super().__init__(driver)



    def open(self):
        self.driver.get(BASE_URL)


    def assert_basic_element_visible(self):
        self.assertions.assert_that_element_is_visible(self.LOGIN)
        self.assertions.assert_that_element_is_visible(self.LOGO)
        self.assertions.assert_that_element_is_visible(self.SEARCH)
        self.assertions.assert_that_element_is_visible(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.FAVORITES)
        self.assertions.assert_that_element_is_visible(self.ORDERS)


    def assert_basic_element_click(self):
        self.click(self.BASKET)
        self.assertions.assert_that_element_is_visible(self.BASKET_PAGE)

        self.click(self.START_PAGE)

        self.click(self.FAVORITES)
        self.assertions.assert_that_element_is_visible(self.FAVORITES_PAGE)

        self.click(self.START_PAGE)


        self.click(self.ORDERS)
        self.assertions.assert_that_element_is_visible(self.ORDERS_PAGE)



