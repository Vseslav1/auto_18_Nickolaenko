import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


URL = 'https://jut.su/'


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_login(driver):
    driver.get(URL)

    login_site = driver.find_element(By.CSS_SELECTOR, '[class="login_btn circle"]')
    name = driver.find_element(By.CSS_SELECTOR, '[id="login_input1"]')
    password = driver.find_element(By.CSS_SELECTOR, '[id="login_input2"]')
    enter = driver.find_element(By.CSS_SELECTOR, '[id="login_submit"]')

    login_site.click()
    assert login_site.is_displayed()
    name.send_keys('vseslav12345')
    assert name.is_displayed()
    password.send_keys('qwerty1234')
    assert password.is_displayed()
    enter.click()


def test_registration(driver):
    driver.get(URL)

    login_site = driver.find_element(By.CSS_SELECTOR, '[class="login_btn circle"]')
    login_site.click()
    registration = driver.find_element(By.XPATH, '//*[@id="login_panel"]/form/div[4]/a[2]')
    registration.click()
    new_user_registration = driver.find_element(By.XPATH, '//*[@id="registration"]/div[1]/div[1]')
    assert new_user_registration.is_displayed()
    login = driver.find_element(By.XPATH, '//*[@id="name"]')
    login.send_keys('TeachMySkill')
    assert login.is_displayed()
    pasword = driver.find_element(By.XPATH, '//*[@id="registration"]/div[2]/table/tbody/tr[3]/td[2]/input')
    pasword.send_keys('TeachMySkill12345')
    assert pasword.is_displayed()
    question = driver.find_element(By.XPATH,
                                   '/html/body/div[5]/div[1]/div/form/div[2]/table/tbody/tr[6]/td[2]/div/input')
    question.send_keys('Наруто')
    assert question.is_displayed()



def test_search(driver):
    driver.get(URL)

    search = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[2]')
    search.send_keys('Наруто')
    find = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[3]')
    find.click()
    first_season = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div[2]/div[1]/a/div')
    first_season.click()
    last_ep = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div/div[2]/div[2]/a[220]')
    assert last_ep.is_displayed()


def test_continue_watching(driver):
    driver.get(URL)

    search = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[2]')
    search.send_keys('Наруто')
    find = driver.find_element (By.XPATH, '//*[@id="search_b"]/form/input[3]')
    find.click()
    first_season = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div[2]/div[1]/a/div')
    first_season.click()
    first_series = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div/div[2]/div[2]/a[1]')
    first_series.click()
    play_video = driver.find_element(By.XPATH, '//*[@id="my-player"]/button')
    play_video.click()
    time.sleep(60)
    go_to_home_page = driver.find_element(By.XPATH, '/html/body/div[3]/a/img')
    go_to_home_page.click()
    continue_wathing = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div[2]/div/a/div/div[2]')
    assert continue_wathing.is_displayed()
    time.sleep(3)


def test_series_selection(driver):
    driver.get(URL)

    search = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[2]')
    search.send_keys('Ван Пис')
    find = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[3]')
    find.click()
    episode = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div/div[2]/a[1112]')
    episode.click()
    play_video = driver.find_element(By.XPATH, '//*[@id="my-player"]')
    play_video.click()
    assert play_video.is_displayed()


def test_choose_quality(driver):
    driver.get(URL)
    search = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[2]')
    search.send_keys('Ван Пис')
    find = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[3]')
    find.click ()
    episode = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div/div[2]/a[1112]')
    episode.click()
    play_video = driver.find_element(By.XPATH, '//*[@id="my-player"]')
    play_video.click()
    time.sleep(20)
    choose_quality = driver.find_element(By.XPATH, '//*[@id="my-player"]/div[9]/div[7]')
    choose_quality.click()
    quality = driver.find_element(By.XPATH, '//*[@id="my-player"]/div[9]/div[7]')
    quality.click()
    time.sleep(1)
    quality_menu = driver.find_element(By.XPATH,'//*[@id="my-player"]/div[9]/div[7]/div')
    assert quality_menu.is_displayed()


def test_full_screen_video(driver):
    driver.get(URL)
    driver.get(URL)
    search = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[2]')
    search.send_keys ('Ван Пис')
    find = driver.find_element(By.XPATH, '//*[@id="search_b"]/form/input[3]')
    find.click()
    episode = driver.find_element(By.XPATH, '//*[@id="dle-content"]/div/div[2]/a[1112]')
    episode.click()
    play_video = driver.find_element(By.XPATH, '//*[@id="my-player"]')
    play_video.click()
    time.sleep(20)
    full_screen = driver.find_element(By.XPATH,'//*[@id="my-player"]/div[9]/button[5]')
    full_screen.click()
    full_screen_open = driver.find_element(By.XPATH,'//*[@id="my-player_html5_api"]')
    assert full_screen_open.is_displayed()

