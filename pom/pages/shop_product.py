from selenium.webdriver.common.by import By


class ShopProduct:
    _dom_element = None

    # product related selectors
    _increment_button = (By.CSS_SELECTOR, ".stepper-input .increment")
    _decrement_button = (By.CSS_SELECTOR, ".stepper-input .decrement")
    _addtocart_button = (By.CSS_SELECTOR, ".product-action button")
    _count_tocart_input = (By.CSS_SELECTOR, ".stepper-input input.quantity")
    _name = (By.CSS_SELECTOR, ".product-name")
    _price = (By.CSS_SELECTOR, ".product-price")

    def __init__(self, element):
        self._dom_element = element

    def get_dom_element(self):
        return self._dom_element

    def get_name(self):
        el = self._dom_element.find_element(self._name[0], self._name[1])
        return el.text

    def get_price(self):
        el = self._dom_element.find_element(self._price[0], self._price[1])
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

    def click_addtocart_button(self):
        """
        Clicks on ADD TO CART button on product block
        :return: None
        """
        atc_button = self._dom_element.find_element(self._addtocart_button[0], self._addtocart_button[1])
        atc_button.click()

    def get_tocart_quantity(self):
        """
        Returns count of products to be added to cart on product block
        :return: None
        """
        el = self._dom_element.find_element(self._count_tocart_input[0], self._count_tocart_input[1])
        return int(el.get_attribute("value"))

    def is_in_cart(self, cart, quantity):
        """
        Checks if this product is in cart
        :return: True or False
        """
        name = self.get_name()
        price = self.get_price()
        for cart_item in cart:
            if name == cart_item.get_name() and price == cart_item.get_price() and quantity == cart_item.get_quantity():
                return True
        return False

