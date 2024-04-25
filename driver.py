import os
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver(Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(10)

def wait_element(browser, delay_seconds, by, value):
    return WebDriverWait(browser, delay_seconds).until(EC.presence_of_all_elements_located((by, value)))
