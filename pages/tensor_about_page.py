from time import sleep

from driver import Driver, wait_element
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class TensorAboutPage:
    working_header_xpath = '//p[@class="tensor_ru-header-h2 tensor_ru-pb-16" and text()="Учим и учимся"]'
    working_images_xpath = '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]'

    @staticmethod
    def working_image_sizes(driver: Driver):
        next_header = driver.find_element(By.XPATH, TensorAboutPage.working_header_xpath)
        ActionChains(driver).scroll_to_element(next_header).perform()
        working_images = wait_element(driver, 10, By.XPATH,
                                      '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]')
        sizes = []
        for image in working_images:
            width = image.get_attribute('width')
            height = image.get_attribute('height')
            image_size = f'{width} {height}'
            sizes.append(image_size)
        return set(sizes)



