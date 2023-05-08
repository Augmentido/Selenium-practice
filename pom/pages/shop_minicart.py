from selenium.webdriver.common.by import By


class ShopMinicartProduct:
    _dom_element = None

    # cart related selectors
    _name = (By.CSS_SELECTOR, ".product-info .product-name")
    _price = (By.CSS_SELECTOR, ".product-info .product-price")
    _count = (By.CSS_SELECTOR, ".product-total .quantity")

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

