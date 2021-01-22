import unittest

from item import Item
from shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):

    def setUp(self):
        self.item_list = [Item(price=100), Item(price=100)]
        self.email_list = ['user1@example.com', 'user2@example.com']

    def test_shopping_list_calculates_item_list_total_price(self):
        shopping_list = ShoppingList(self.item_list, self.email_list)
        self.assertEqual(shopping_list.item_list_total_price, 200)

    def test_shopping_list_returns_price_per_email(self):
        shopping_list = ShoppingList(self.item_list, self.email_list)
        self.assertEqual(shopping_list.calculate_payment_per_email(),
                         {'user1@example.com': 100, 'user2@example.com': 100})

    def test_shopping_list_returns_price_per_email_without_remainder(self):
        item_list = [Item(price=100)]
        email_list = self.email_list + ['user3@example.com']
        shopping_list = ShoppingList(item_list, email_list)
        self.assertEqual({'user1@example.com': 33, 'user2@example.com': 33, 'user3@example.com': 34},
                         shopping_list.calculate_payment_per_email())

    def test_shopping_list_returns_error_message_if_item_list_is_empty(self):
        item_list = []
        shopping_list = ShoppingList(item_list, self.email_list)
        self.assertEqual('There are no items in the shopping list. Please insert at least one item and try again',
                         shopping_list.calculate_payment_per_email())

    def test_shopping_list_returns_error_message_if_email_list_is_empty(self):
        email_list = []
        shopping_list = ShoppingList(self.item_list, email_list)
        self.assertEqual('There are no emails in the shopping list. Please insert at least one email and try again',
                         shopping_list.calculate_payment_per_email())
