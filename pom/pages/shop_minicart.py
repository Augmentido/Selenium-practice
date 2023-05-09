from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ShopMinicartProduct:
    _dom_element = None

    # cart product related selectors
    _name = (By.CSS_SELECTOR, ".product-info .product-name")
    _price = (By.CSS_SELECTOR, ".product-info .product-price")
    _count = (By.CSS_SELECTOR, ".product-total .quantity")
    _remove = (By.CSS_SELECTOR, ".product-remove")
    _minicart_show_btn = (By.CSS_SELECTOR, "header .cart-icon")

    def __init__(self, webdriver, element):
        self._dom_element = element
        self._browser = webdriver

    def get_dom_element(self):
        return self._dom_element

    def get_name(self):
        """
        Returns name of product added to cart
        :return: text
        """
        return self._browser.execute_script(
            "return arguments[0].innerText",
            self._dom_element.find_element(self._name[0], self._name[1])
        )

    def get_price(self):
        """
        Returns price of product added to cart
        :return: text
        """
        return self._browser.execute_script(
            "return arguments[0].innerText",
            self._dom_element.find_element(self._price[0], self._price[1])
        )

    def get_quantity(self):
        """
        Returns count of product added to cart
        :return: int
        """
        return self._browser.execute_script(
            "return parseInt(arguments[0].childNodes[0].data)",
            self._dom_element.find_element(self._count[0], self._count[1])
        )

    def remove(self):
        """
        Remove this item from minicart
        :return: None
        """
        if not self._dom_element.is_displayed():
            self._browser.find_element(self._minicart_show_btn[0], self._minicart_show_btn[1]).click()
        WebDriverWait(self._browser, 3).until(EC.visibility_of(self._dom_element))
        self._dom_element.find_element(self._remove[0], self._remove[1]).click()
