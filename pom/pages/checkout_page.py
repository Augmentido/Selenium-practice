"""
Framework module with tools to test checkout page
"""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pom.pages.shop_page import ShopPage
from pom.pages.shop_product import ShopProduct
from pom.pages.shop_minicart import ShopMinicartProduct


# from selenium.webdriver.support.wait import WebDriverWait


class CheckoutPage:
    _page_url = "https://rahulshettyacademy.com/seleniumPractise/"
    _browser = None

    # Some element at the end of the page
    _page_loaded_element = (By.CSS_SELECTOR, "footer")

    # checkout products table
    _product_rows = (By.CSS_SELECTOR, "#productCartTables tbody tr")
    _name = (By.CSS_SELECTOR, ".product-name")
    _quantity = (By.CSS_SELECTOR, ".quantity")
    _price = (By.CSS_SELECTOR, "td:nth-child(4) .amount")
    _total = (By.CSS_SELECTOR, "td:nth-child(5) .amount")

    # checkout totals
    _totals = (By.CSS_SELECTOR, ".products>div")
    _total_amount = (By.CSS_SELECTOR, ".totAmt")
    _total_discount = (By.CSS_SELECTOR, ".discountPerc")
    _total_amount_after_discount = (By.CSS_SELECTOR, ".discountAmt")

    _place_order_button = (By.CSS_SELECTOR, ".products>div button:not(.promoBtn)")
    _country_select_page_indicator = (By.CSS_SELECTOR, "#root input.chkAgree")

    def __init__(self, browser):
        self._browser = browser
        self._browser.implicitly_wait(8)
        self._browser.get(self._page_url)
        WebDriverWait(self._browser, 20).until(EC.presence_of_element_located(self._page_loaded_element))

        # go to checkout page
        sp = ShopPage(self._browser, False)
        products_in_cart = sp.add_to_cart_script()
        cart = sp.get_minicart()
        cart[0].go_to_checkout()

    def get_products(self):
        """
        Returns parsed products list from products table
        :return: list of products
        """
        rows = self._browser.find_elements(self._product_rows[0], self._product_rows[1])
        products = []
        for row in rows:
            products.append({
                "name": row.find_element(self._name[0], self._name[1]).text,
                "price": float(row.find_element(self._price[0], self._price[1]).text),
                "count": int(row.find_element(self._quantity[0], self._quantity[1]).text),
                "total": float(row.find_element(self._total[0], self._total[1]).text)
            })
        return products

    def get_totals(self):
        """
        Returns data from totals section
        :return:
        """
        totals_block = self._browser.find_element(self._totals[0], self._totals[1])
        return {
            "amount": float(totals_block.find_element(self._total_amount[0], self._total_amount[1]).text),
            "discount": totals_block.find_element(self._total_discount[0], self._total_discount[1]).text,
            "amount_after_discount": float(totals_block.find_element(self._total_amount_after_discount[0], self._total_amount_after_discount[1]).text),
        }

    def click_place_order_button(self):
        """
        Clicks on "Place order" button
        :return: None
        """
        po_button = self._browser.find_element(self._place_order_button[0], self._place_order_button[1])
        po_button.click()
        WebDriverWait(self._browser, 10).until(EC.presence_of_element_located(
           self._country_select_page_indicator
        ))
