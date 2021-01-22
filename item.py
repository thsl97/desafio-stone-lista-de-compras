class Item:
    """
    A class that represents a shopping list item

    """

    def __init__(self, quantity: int, price: int):
        """
        Creates an item with specified quantity and price per unit
        :param quantity: how many units of an item
        :param price: the price per unit of the item
        """
        self.quantity = quantity
        self.price = price

    @property
    def total_price(self) -> int:
        """
        Calculates total value of each item
        :return: the total value of the item
        :rtype: int
        """
        return self.quantity * self.price
