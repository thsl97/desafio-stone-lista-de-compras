import math
from typing import Union

from item import Item


class ShoppingList:
    """
    Class used for representing a shopping list

    """

    def __init__(self, item_list: list[Item], email_list: list[str]):
        """
        :param item_list: Item list
        :param email_list: Emails list
        """
        self.item_list = item_list
        self.email_list = email_list

    @property
    def item_list_total_price(self) -> int:
        """
        Calculates total item list price
        :returns: total item list price
        :rtype: int
        """
        total = 0
        for item in self.item_list:
            total += item.price
        return total

    def calculate_payment_per_email(self) -> Union[str, dict]:
        """
        Calculates the value which every email will pay. Every email pays the same price, and in case of a remainder
        value, the last email on the list pays. Returns error message if either item list of email list is empty
        :returns: dictionary where the key is the email and the value is the price that email will áy
        :rtype: Union[str, dict]
        """
        if len(self.item_list) == 0:
            return 'There are no items in the shopping list. Please insert at least one item and try again'
        if len(self.email_list) == 0:
            return 'There are no emails in the shopping list. Please insert at least one email and try again'
        total_per_email = math.floor(self.item_list_total_price // len(self.email_list))
        remainder_value = self.item_list_total_price % len(self.email_list)
        price_per_email = {}
        for counter, email in enumerate(self.email_list):
            price_per_email[email] = total_per_email
            # if there is a remainder value and it's the last loop, add the remainder to the price of the email
            if remainder_value > 0 and counter == len(self.email_list) - 1:
                price_per_email[email] = math.ceil(total_per_email + remainder_value)
        return price_per_email
