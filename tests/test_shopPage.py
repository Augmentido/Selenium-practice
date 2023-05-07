""" tests for home page """
from pytest import mark
from pom.pages.shop_page import ShopPage


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
