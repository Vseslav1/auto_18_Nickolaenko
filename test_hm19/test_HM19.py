import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()

URL = 'https://www.bbc.com/'


class TestBBS:

    def test_news(self, driver):
        driver.get(URL)
        news = driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/section/nav/ul/li[2]/div/a')
        assert news.is_displayed()


    def test_logo(self, driver):
        driver.get(URL)
        logo = driver.find_element(By.CSS_SELECTOR, '[class="sc-1097f7fe-0 jbvZzi"]')
        assert logo.is_displayed()


    def test_home(self, driver):
        driver.get(URL)
        home = driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-4 yKcKi"]')
        assert home.is_displayed()


    def test_sports(self, driver):
        driver.get(URL)
        sports = driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/section/nav/ul/li[3]/div/a')
        assert sports.is_displayed()


    def test_innovation(self, driver):
        driver.get(URL)
        innovation = driver.find_element(By.CSS_SELECTOR, '[class="sc-f116bf72-4 eqTiTw"]')
        assert innovation.is_displayed()


    def test_travel(self, driver):
        driver.get(URL)
        travel = driver.find_element(By.XPATH, '//*[@id="__next"]/div/nav/section/nav/ul/li[7]/div/a')
        assert travel.is_displayed()


    def test_menu(self, driver):
        driver.get(URL)
        menu = driver.find_element(By.CSS_SELECTOR, '[class="sc-2c06e71a-0 fsMljb"]')
        assert menu.is_displayed()


    def test_banner_name(self, driver):
        driver.get(URL)
        banner_name = driver.find_element(By.XPATH,
                '//*[@id="main-content"]/article/section[1]/div/div[2]/div[2]/div[3]/div/a/div/div/div[1]/div/h2')
        assert banner_name.is_displayed()


    def test_banner_pictures(self, driver):
        driver.get(URL)
        banner_pictures = driver.find_element(By.CSS_SELECTOR, '[class="sc-13b8515c-0 hbOWRP"]')
        assert banner_pictures.is_displayed()


    def test_publication_time(self, driver):
        driver.get(URL)
        publication_time = driver.find_element(By.CSS_SELECTOR, '[class="sc-4e537b1-1 dsUUMv"]')
        assert publication_time.is_displayed()


    def test_only_from_the_bbc(self, driver):
        driver.get(URL)
        only = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[2]/div/div[1]/div/h2')
        assert only.is_displayed()