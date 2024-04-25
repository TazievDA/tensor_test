from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ContactsPage:
    tensor_banner_xpath = '//a[contains(@class, "sbisru-Contacts__logo-tensor mb-12")]'
    region_block_xpath = '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]'
    partners_list_xpath = '//div[@class="controls-BaseControl controls_list_theme-sbisru controls_toggle_theme-sbisru"]'
    concrete_region_xpath = '//span[@title="Камчатский край"]'

    @staticmethod
    def find_tensor_banner(driver: Driver):
        tensor_banner = driver.find_element(By.XPATH, ContactsPage.tensor_banner_xpath)
        return 'OK'

    @staticmethod
    def click_tensor_banner(driver: Driver):
        tensor_banner = driver.find_element(By.XPATH, ContactsPage.tensor_banner_xpath)
        tensor_banner.click()
        driver.switch_to.window(driver.window_handles[-1])

    @staticmethod
    def find_region_block(driver: Driver):
        region_block = driver.find_element(By.XPATH, ContactsPage.region_block_xpath)

    @staticmethod
    def find_partners_list(driver: Driver):
        partners_list = driver.find_element(By.XPATH, ContactsPage.partners_list_xpath)
        return partners_list

    @staticmethod
    def click_region_block(driver: Driver):
        region_block = driver.find_element(By.XPATH, ContactsPage.region_block_xpath)
        region_block.click()

    @staticmethod
    def click_concrete_region(driver: Driver):
        concrete_region = driver.find_element(By.XPATH, ContactsPage.concrete_region_xpath)
        ActionChains(driver).move_to_element(concrete_region).click(concrete_region).perform()

    @staticmethod
    def get_region_info(driver: Driver):
        region_block = driver.find_element(By.XPATH, ContactsPage.region_block_xpath)
        region_name = region_block.text
        actual_url = driver.current_url
        title = driver.title
        return region_name, actual_url, title


