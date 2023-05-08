""" tests for home page """
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
        product_obj = page.get_product_dom_element(0)
        assert product_obj is not None
        cnt = page.get_product_tocart_quantity(product_obj)
        page.click_product_increment_button(product_obj)
        assert page.get_product_tocart_quantity(product_obj) == cnt + 1

    def test_product_count_decrement_btn(self, browser):
        """
        Check if the "minus" button decrements count inside the product block
        :param browser: webdriver
        :return: None
        """
        page = ShopPage(browser)
        product_obj = page.get_product_dom_element(0)
        assert product_obj is not None
        page.click_product_increment_button(product_obj)
        cnt = page.get_product_tocart_quantity(product_obj)
        page.click_product_decrement_button(product_obj)
        assert page.get_product_tocart_quantity(product_obj) == cnt - 1

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
        # add to cart
        #TODO
        pass

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
