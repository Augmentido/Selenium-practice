""" tests for checkout page """
import random
from pytest import mark
from selenium.webdriver import ActionChains
from selenium import webdriver
from pom.pages.checkout_page import CheckoutPage
import time


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


# place order
# select country and checkbox
# get "order placed" message