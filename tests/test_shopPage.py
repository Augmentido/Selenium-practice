""" tests for home page """
import random
from pytest import mark
from selenium.webdriver import ActionChains
from selenium import webdriver
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
        time.sleep(1)
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
        time.sleep(1)
        cnt = product.get_tocart_quantity()
        product.click_decrement_button()
        time.sleep(1)
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

    def add_to_cart_script(self, page: ShopPage, browser: webdriver):
        """
        Script for use in tests. Finds two random products,
        adds to cart one item of first one and two items of second one.
        Returns added products
        :param page: ShopPage
        :param browser: webdriver
        :return: (product1, product2)
        """
        products = page.get_products() # getting all products
        assert len(products) > 1

        # get 2 random different products to work with
        product1 = random.randint(0, len(products)-1)
        product2 = random.randint(0, len(products)-1)
        # we need two different products. If we got the same product - let`s try one more time
        if product1 == product2:
            return self.add_to_cart_script(page, browser)
        product1 = products[product1]
        product2 = products[product2]

        # first one just add to cart
        ActionChains(browser).move_to_element(product1.get_dom_element()).perform()
        time.sleep(1)
        product1.click_addtocart_button()
        time.sleep(1)

        # second - increment and add to cart
        ActionChains(browser).move_to_element(product2.get_dom_element()).perform()
        time.sleep(1)
        product2.click_increment_button()
        product2.click_addtocart_button()
        time.sleep(1)

        return product1, product2

    def test_add_to_cart(self, browser):
        """
        Check if add to cart in product block works properly
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)
        selected_products = self.add_to_cart_script(page, browser)
        cart = page.get_minicart()
        assert selected_products[0].is_in_cart(cart, 1)
        assert selected_products[1].is_in_cart(cart, 2)

    def test_remove_from_cart(self, browser):
        """
        Check if remove from cart works properly
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)

        # add something to cart
        selected_products = self.add_to_cart_script(page, browser)
        cart = page.get_minicart()
        assert selected_products[0].is_in_cart(cart, 1)
        assert selected_products[1].is_in_cart(cart, 2)
        time.sleep(1)

        # remove all items from cart
        cart = page.get_minicart()
        for cart_item in cart:
            cart_item.remove()
        time.sleep(1)
        cart = page.get_minicart()
        assert cart is None





# to checkout
# check totals in checkout
# place order
# select country and checkbox
# get "order placed" message
