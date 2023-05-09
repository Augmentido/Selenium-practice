""" tests for checkout page """
import random
from pytest import mark
from selenium.webdriver import ActionChains
from selenium import webdriver
from pom.pages.checkout_page import CheckoutPage
import time

from pom.pages.place_order_page import PlaceOrderPage


@mark.functional
@mark.checkout
class TestCheckoutPage:
    """ tests for checkout page """
    def test_totals(self, browser):
        page = CheckoutPage(browser)
        products = page.get_products()
        total = 0.0
        for product in products:
            assert product["count"] * product["price"] == product["total"]
            total = total + product["total"]

        totals = page.get_totals()
        assert totals["amount"] == total

    def test_place_order(self, browser):
        page = CheckoutPage(browser)
        page.click_place_order_button()
        po_page = PlaceOrderPage(browser)
        po_page.select_country('Malta')
        po_page.click_agree_checkbox()
