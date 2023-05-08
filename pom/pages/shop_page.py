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
    _product_name = (By.CSS_SELECTOR, ".product-name")

    # Some element at the end of the page
    _page_loaded_element = (By.CSS_SELECTOR, "footer")

    # Selectors for search
    _search_form = (By.CSS_SELECTOR, "header form.search-form")
    _search_input = (By.CSS_SELECTOR, "input[type=\"search\"]")
    _search_button = (By.CSS_SELECTOR, "button[type=\"submit\"]")


    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(10)
        self._browser.get(self._page_url)
        WebDriverWait(self._browser, 20).until(EC.presence_of_element_located(self._page_loaded_element))

    def get_product_dom_element(self, index=0):
        """
        Finds and returns a DOM element containing the product (from products list)
        :param index: element number OR -1 to get list of all elements
        :return: DOM Element
        """
        if index < -1:
            return None
        els = self._browser.find_elements(self._product_locator[0], self._product_locator[1])
        if index == -1:
            return els
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

    def get_search_form_dom_element(self):
        """
        Finds and returns a DOM element of search form
        :return: DOM Element
        """
        return self._browser.find_element(self._search_form[0], self._search_form[1])

    def send_keyword_to_search_bar(self, search_form, keyword):
        """
        Inputs some text to search bar
        :param search_form: search FORM DOM element
        :param keyword: text to send
        :return: None
        """
        input_el = search_form.find_element(self._search_input[0], self._search_input[1])
        input_el.clear()
        input_el.send_keys(keyword)

    def click_search_go_button(self, search_form):
        """
        Clicks on "GO" button on search bar
        :param search_form: search FORM DOM element
        :return: None
        """
        go_button = search_form.find_element(self._search_button[0], self._search_button[1])
        go_button.click()

    def get_product_names(self):
        """
        Retrives the list of product names on page.
        :return: list of product names on page
        """
        product_doms = self.get_product_dom_element(-1)
        names_list = []
        for product_dom in product_doms:
            el = product_dom.find_element(self._product_name[0], self._product_name[1])
            names_list.append(el.text)
        return names_list
