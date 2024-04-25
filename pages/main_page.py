from selenium.webdriver.common.action_chains import ActionChains

from driver import Driver
from selenium.webdriver.common.by import By


class MainPage:
    contacts_button_xpath = ('//li[contains(@class, "sbisru-Header__menu-item '
                             'sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm")]')
    download_local_version_xpath = '//a[@href="/download"]'
    close_cookie_xpath = '//div[@class="sbis_ru-CookieAgreement__close"]'

    @staticmethod
    def go_to_contacs(driver: Driver):
        contacts_button = driver.find_element(By.XPATH, MainPage.contacts_button_xpath)
        contacts_button.click()

    @staticmethod
    def find_download_local_version(driver: Driver):
        download_local_version = driver.find_element(By.XPATH, MainPage.download_local_version_xpath)

    @staticmethod
    def click_download_local_version(driver: Driver):
        download_local_version = driver.find_element(By.XPATH, MainPage.download_local_version_xpath)
        close_cookie = driver.find_element(By.XPATH, MainPage.close_cookie_xpath).click()
        ActionChains(driver).move_to_element(download_local_version).click(download_local_version).perform()