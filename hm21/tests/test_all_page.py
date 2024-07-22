from hm21.pages.main_page import MainPage
from hm21.pages.catalog_page import CatalogPage
from hm21.pages.login_page import LoginPage



def test_open_main_page_website(driver):
    page = MainPage(driver)
    page.open()
    page.assert_basic_element_visible()


def test_open_menu_page(driver):
    page = MainPage(driver)
    page.open()

    pages = MainPage(driver)
    pages.assert_basic_element_click()


def test_catalog_is_visible(driver):
    page = MainPage(driver)
    page.open()

    catalog = CatalogPage(driver)
    catalog.open_catalog()


def test_form_login(driver):
    page = MainPage(driver)
    page.open()

    login_form = LoginPage(driver)
    login_form.assert_form_visible()


def test_input_login(driver):
    page = MainPage(driver)
    page.open()

    login = LoginPage(driver)
    login.assert_login_input()


def test_search(driver):
    page = MainPage(driver)
    page.open()

    search = CatalogPage(driver)
    search.assert_search()