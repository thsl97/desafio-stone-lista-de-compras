import unittest

from item import Item


class TestItem(unittest.TestCase):

    def test_item_returns_total_price(self):
        item = Item(quantity=2, price=100)
        self.assertEqual(200, item.total_price)
