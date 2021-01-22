class Item:
    """
    A class that represents a shopping list item

    """

    def __init__(self, price: int):
        """
        Creates an item with a specific value in cents
        :param price: item value in cents
        """
        self.price = price
