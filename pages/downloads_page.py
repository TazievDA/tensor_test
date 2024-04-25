import re
from driver import Driver
from selenium.webdriver.common.by import By


class DownloadPage:

    plugin_button_xpath = ('//div[@class="controls-TabButton controls-TabButton__right-align controls-ListView__item '
                           'undefined ws-enabled ws-control-inactive ws-component"]')
    download_button_xpath = '//a[contains(@href, "setup-web")]'

    @staticmethod
    def go_to_plugin(driver: Driver):
        plugin_button = driver.find_element(By.XPATH, DownloadPage.plugin_button_xpath)
        plugin_button.click()

    @staticmethod
    def download_plugin(driver: Driver):
        download_button = driver.find_element(By.XPATH, DownloadPage.download_button_xpath)
        download_button.click()

    @staticmethod
    def expected_file_size(driver: Driver):
        size_info = driver.find_element(By.XPATH, DownloadPage.download_button_xpath).text # 'Скачать (Exe 7.12 МБ)'
        pattern = r"\d+\.\d+\s+\w{2}"
        expected_size = re.findall(pattern=pattern, string=size_info)
        return expected_size[0]




