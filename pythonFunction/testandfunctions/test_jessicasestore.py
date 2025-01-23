from unittest import TestCase
from jessicasestore import *

class TestRemoveFromCartFunction(TestCase):
    def test_that_remove_from_cart_exist(self):
        remove_from_cart(cart = [])

class TestRemoveFromCartFunction(TestCase):
    def test_that_add_to_cart_exist(self):
        add_to_cart(cart = [], products = [])

class TestViewProductsFunction(TestCase):
    def test_that_view_products_exist(self):
        view_products(products = [])

class TestViewCartFunction(TestCase):
    def test_that_view_cart_exist(self):
        view_cart(cart = [])


