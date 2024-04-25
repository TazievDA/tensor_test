import pytest
import os
from driver import Driver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": f"{os.getcwd()}",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False
    })
    chrome_options.enable_downloads = True
    path = ChromeDriverManager().install()
    driver_service = Service(executable_path=path)
    driver = Driver(service=driver_service, options=chrome_options)
    driver.maximize_window()
    driver.get("https://sbis.ru")

    yield driver

    driver.quit()