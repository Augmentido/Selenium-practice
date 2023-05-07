"""
Framework module with tools to test shop page
"""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:

    _page_url = "https://rahulshettyacademy.com/seleniumPractise/"
    _browser = None

    # Selector for product in list of products and selector for elements inside that product
    _product_locator = (By.CSS_SELECTOR, ".products .product")
    _product_increment_button = (By.CSS_SELECTOR, ".stepper-input .increment")
    _product_decrement_button = (By.CSS_SELECTOR, ".stepper-input .decrement")
    _product_count_tocart_input = (By.CSS_SELECTOR, ".stepper-input input.quantity")
    _page_loaded_element = (By.CSS_SELECTOR, "footer")

    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(10)
        self._browser.get(self._page_url)
        WebDriverWait(self._browser, 20).until(EC.presence_of_element_located(self._page_loaded_element))

    def get_product_dom_element(self, index=0):
        """
        Finds and returns a DOM element containing the product (from products list)
        :param index: element number
        :return: DOM Element
        """
        if index < 0:
            return None
        els = self._browser.find_elements(self._product_locator[0], self._product_locator[1])
        return els[index] if index < len(els) else None

    def get_product_tocart_quantity(self, product_object):
        """
        Returns count of products to be added to cart on product block
        :param product_object: product DOM element
        :return: None
        """
        el = product_object.find_element(self._product_count_tocart_input[0], self._product_count_tocart_input[1])
        return int(el.get_attribute("value"))

    def click_product_increment_button(self, product_object):
        """
        Clicks on increment button on product block
        :param product_object: product DOM element
        :return: None
        """
        inc_button = product_object.find_element(self._product_increment_button[0], self._product_increment_button[1])
        inc_button.click()

    def click_product_decrement_button(self, product_object):
        """
        Clicks on increment button on product block
        :param product_object: product DOM element
        :return: None
        """
        dec_button = product_object.find_element(self._product_decrement_button[0], self._product_decrement_button[1])
        dec_button.click()

