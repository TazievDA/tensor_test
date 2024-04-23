import pytest
from driver import Driver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def browser():
    path = ChromeDriverManager().install()
    driver_service = Service(executable_path=path)
    driver = Driver(service=driver_service)
    driver.maximize_window()
    driver.get("https://sbis.ru")

    yield driver

    driver.quit()