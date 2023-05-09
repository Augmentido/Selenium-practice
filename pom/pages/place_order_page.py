"""
Framework module with tools to test PlaceOrder page
"""
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.pages.shop_page import ShopPage
from pom.pages.shop_product import ShopProduct
from pom.pages.shop_minicart import ShopMinicartProduct


# from selenium.webdriver.support.wait import WebDriverWait


class PlaceOrderPage:
    _browser = None

    _agree_checkbox = (By.CSS_SELECTOR, "#root input.chkAgree")
    _country_select = (By.CSS_SELECTOR, "#root select")
    _proceed_btn = (By.CSS_SELECTOR, "#root button")

    def __init__(self, browser):
        self._browser = browser

    def select_country(self, country):
        sl = Select(self._browser.find_element(self._country_select[0], self._country_select[1]))
        sl.select_by_visible_text(country)

    def click_agree_checkbox(self):
        chk = self._browser.find_element(self._agree_checkbox[0], self._agree_checkbox[1])
        chk.click()

    def click_proceed_button(self):
        """
        Clicks on "Proceed" button
        :return: None
        """
        po_button = self._browser.find_element(self._proceed_btn[0], self._proceed_btn[1])
        po_button.click()
