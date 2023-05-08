
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from pom.pages.shop_page import ShopPage


class ShopProduct:
    _page = None
    _browser = None
    _dom_element = None

    _increment_button = (By.CSS_SELECTOR, ".stepper-input .increment")
    _decrement_button = (By.CSS_SELECTOR, ".stepper-input .decrement")
    _count_tocart_input = (By.CSS_SELECTOR, ".stepper-input input.quantity")
    _name = (By.CSS_SELECTOR, ".product-name")

    def __init__(self, page, browser, element):
        self._page = page
        self._browser = browser
        self._dom_element = element

    def get_name(self):
        el = self._dom_element.find_element(self._name[0], self._name[1])
        return el.text

    def click_increment_button(self):
        """
        Clicks on increment button on product block
        :return: None
        """
        inc_button = self._dom_element.find_element(self._increment_button[0], self._increment_button[1])
        inc_button.click()

    def click_decrement_button(self):
        """
        Clicks on increment button on product block
        :return: None
        """
        dec_button = self._dom_element.find_element(self._decrement_button[0], self._decrement_button[1])
        dec_button.click()

    def get_tocart_quantity(self):
        """
        Returns count of products to be added to cart on product block
        :return: None
        """
        el = self._dom_element.find_element(self._count_tocart_input[0], self._count_tocart_input[1])
        return int(el.get_attribute("value"))
