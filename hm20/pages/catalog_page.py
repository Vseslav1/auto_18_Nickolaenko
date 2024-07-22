import time
from selenium.webdriver.common.by import By
from hm20.pages.base_page import BasePage
from hm20.locators.locators import MarketYandexLocators


class CatalogPage(BasePage, MarketYandexLocators):

    def __init__(self, driver):
        super().__init__(driver)


    def open_catalog(self):
        self.click(self.BUTTON_CATALOG)
        self.assertions.assert_that_element_is_visible(self.CATALOG)
        time.sleep(5)

        self.save_screenshot('assert_catalog_visible.png')

    def assert_search(self):
        self.click(self.BUTTON_CATALOG)
        self.fill(self.INPUT_SEARCH, 'Холодильник')
        self.click(self.BUTTON_SEARCH)
        self.assertions.assert_that_element_is_visible(self.PAGE_SEARCH)

        self.save_screenshot('assert_search.png')
