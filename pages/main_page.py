from driver import Driver
from selenium.webdriver.common.by import By


class MainPage:
    contacts_button_xpath = ('//li[contains(@class, "sbisru-Header__menu-item '
                             'sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm")]')

    @staticmethod
    def go_to_contacs(driver: Driver):
        contacts_button = driver.find_element(By.XPATH, MainPage.contacts_button_xpath)
        contacts_button.click()

