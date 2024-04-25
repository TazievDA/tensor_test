from time import sleep

from driver import Driver
from selenium.webdriver import ChromeOptions, Remote
from pages.downloads_page import DownloadPage
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage

def test_first_scenario(browser: Driver):
    MainPage.go_to_contacs(browser)
    ContactsPage.find_tensor_banner(browser)
    ContactsPage.click_tensor_banner(browser)
    TensorMainPage.tensor_find_text(browser)
    actual = TensorMainPage.tensor_click_more_button(browser)
    expected = 'https://tensor.ru/about'
    assert actual == expected
    actual_set_images_size = TensorAboutPage.working_image_sizes(browser)
    expected = 1
    assert len(actual_set_images_size) == expected

def test_second_scenario(browser: Driver):
    MainPage.go_to_contacs(browser)
    ContactsPage.find_region_block(browser)
    ContactsPage.find_partners_list(browser)
    starter_partners_list = ContactsPage.find_partners_list(browser).text
    ContactsPage.click_region_block(browser)
    ContactsPage.click_concrete_region(browser)
    sleep(1)
    actual_region_name, actual_url, actual_title =  ContactsPage.get_region_info(browser)
    changed_partners_list = ContactsPage.find_partners_list(browser).text
    expected_region_name = 'Камчатский край'
    expected_text_in_url = '41-kamchatskij-kraj'
    expected_text_in_title = 'Камчатский край'
    assert actual_region_name == expected_region_name
    assert changed_partners_list != starter_partners_list
    assert expected_text_in_url in actual_url
    assert expected_text_in_title in actual_title

def test_third_scenario(browser: Driver):
    MainPage.find_download_local_version(browser)
    MainPage.click_download_local_version(browser)
    DownloadPage.go_to_plugin(browser)
    DownloadPage.download_plugin(browser)