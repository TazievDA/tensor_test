from time import sleep

from driver import Driver
from selenium.webdriver.common.by import By


class ContactsPage:
    tensor_banner_xpath = '//a[contains(@class, "sbisru-Contacts__logo-tensor mb-12")]'

    @staticmethod
    def find_tensor_banner(driver: Driver):
        tensor_banner = driver.find_element(By.XPATH, ContactsPage.tensor_banner_xpath)
        return 'OK'

    @staticmethod
    def click_tensor_banner(driver: Driver):
        tensor_banner = driver.find_element(By.XPATH, ContactsPage.tensor_banner_xpath)
        tensor_banner.click()
        driver.switch_to.window(driver.window_handles[-1])