from driver import Driver
from selenium.webdriver.common.by import By

class TensorMainPage:
    text_block_xpath = '//p[@class="tensor_ru-Index__card-title tensor_ru-pb-16" and text()="Сила в людях"]'
    more_button = '//a[@href="/about"]'
    @staticmethod
    def tensor_find_text(driver: Driver):
        text_block = driver.find_element(By.XPATH, TensorMainPage.text_block_xpath)

    @staticmethod
    def tensor_click_more_button(driver: Driver):
        more_button = driver.find_element(By.XPATH, TensorMainPage.more_button)
        more_button.click()
        return driver.current_url