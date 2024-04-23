from driver import Driver
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

def test_first_scenario(browser: Driver):
    MainPage.go_to_contacs(browser)
    banner = ContactsPage.find_tensor_banner(browser)
    assert banner == 'OK'
    MainPage.go_to_contacs(browser)
    ContactsPage.click_tensor_banner(browser)
    TensorMainPage.tensor_find_text(browser)
    actual = TensorMainPage.tensor_click_more_button(browser)
    assert actual == 'https://tensor.ru/about'
    actual_set_images_size = TensorAboutPage.working_image_sizes(browser)
    expected = 1
    assert len(actual_set_images_size) == expected

def test_second_scenario(browser: Driver):
    MainPage.go_to_contacs(browser)
