"""
Framework module with tools to test shop page
"""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.pages.shop_product import ShopProduct
from pom.pages.shop_minicart import ShopMinicartProduct
#from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:

    _page_url = "https://rahulshettyacademy.com/seleniumPractise/"
    _browser = None

    # Selector for product in list of products and selector for elements inside that product
    _product_locator = (By.CSS_SELECTOR, ".products .product")

    # Some element at the end of the page
    _page_loaded_element = (By.CSS_SELECTOR, "footer")

    # Selectors for search
    _search_form = (By.CSS_SELECTOR, "header form.search-form")
    _search_input = (By.CSS_SELECTOR, "input[type=\"search\"]")
    _search_button = (By.CSS_SELECTOR, "button[type=\"submit\"]")

    # cart related selectors
    _cart = (By.CSS_SELECTOR, ".cart-preview ul.cart-items")
    _cart_item = (By.CSS_SELECTOR, "li.cart-item")

    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(10)
        self._browser.get(self._page_url)
        WebDriverWait(self._browser, 20).until(EC.presence_of_element_located(self._page_loaded_element))

    def get_products(self):
        """
        Finds and returns a list of ShopProduct elements
        :return: ShopProduct[]
        """

        els = self._browser.find_elements(self._product_locator[0], self._product_locator[1])
        ls = []
        for el in els:
            ls.append(ShopProduct(el))
        return ls if len(ls) > 0 else None

    def get_product(self, index=0):
        """
        Finds and returns a product class from products list
        :param index: element number
        :return: ShopProduct
        """
        if index < 0:
            return None
        els = self.get_products()
        return els[index] if index < len(els) else None

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
        products = self.get_products()
        names_list = []
        for product in products:
            names_list.append(product.get_name())
        return names_list

    def get_minicart(self):
        """
        Finds and returns a list of ShopMinicart elements
        :return: ShopMinicartProduct[]
        """

        el = self._browser.find_element(self._cart[0], self._cart[1])
        if el is None:
            return None
        els = el.find_elements(self._cart_item[0], self._cart_item[1])
        li = []
        for el in els:
            li.append(ShopMinicartProduct(self._browser, el))
        return li if len(li) > 0 else None
