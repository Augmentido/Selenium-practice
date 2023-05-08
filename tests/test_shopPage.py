""" tests for home page """
import random

from pytest import mark
from pom.pages.shop_page import ShopPage
import time


@mark.functional
@mark.shop
class TestShopPage:
    """ tests for shop page """

    def test_product_count_increment_btn(self, browser):
        """
        Check if the "plus" button increments the count inside the product block
        :param browser: webdriver
        :return: None
        """

        page = ShopPage(browser)
        product = page.get_product(0)
        assert product is not None
        cnt = product.get_tocart_quantity()
        product.click_increment_button()
        assert product.get_tocart_quantity() == cnt + 1

    def test_product_count_decrement_btn(self, browser):
        """
        Check if the "minus" button decrements count inside the product block
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)
        product = page.get_product(0)
        assert product is not None
        product.click_increment_button()
        cnt = product.get_tocart_quantity()
        product.click_decrement_button()
        assert product.get_tocart_quantity() == cnt - 1

    def test_product_search(self, browser):
        """
        Check if the searchbar works properly
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)
        search_form = page.get_search_form_dom_element()

        # check search by writing some keyword and pressing "Enter"
        page.send_keyword_to_search_bar(search_form, "be\x0D")
        time.sleep(3)
        names = page.get_product_names()
        for name in names:
            assert "be" in name.lower()

        # check search by writing some keyword and clicking on "GO" button
        page.send_keyword_to_search_bar(search_form, "ca")
        page.click_search_go_button(search_form)
        time.sleep(3)
        names = page.get_product_names()
        for name in names:
            assert "ca" in name.lower()

    def test_add_to_cart(self, browser):
        """
        Check if add to cart in product block works properly
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)
        products = page.get_products() # getting all products DOM elements
        assert len(products) > 0
        product1 = random.randint(0, len(products)-1)
        product2 = random.randint(0, len(products)-1)
        if product1 == product2:
            return self.test_add_to_cart(browser)
        pass #TODO

    def test_remove_from_cart(self, browser):
        """
        Check if remove from cart works properly
        :param browser: webdriver
        :return: None
        """
        # remove from cart
        #TODO
        pass



# to checkout

# check totals in checkout
# place order
# select country and checkbox
# get "order placed" message
