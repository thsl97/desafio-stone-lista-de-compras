import math
from typing import Union

from main.item import Item


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
            total += item.total_price
        return total

    def calculate_payment_per_email(self) -> Union[str, dict]:
        """
        Calculates the value which every email will pay. Every email pays the same price rounded down, and the remainder
        accumulates. Finally, the remainder is distributed to the n last items of the email list, where n is the total
        accumulated remainder.
        :returns: dictionary where the key is the email and the value is the price that email will áy
        :rtype: Union[str, dict]
        """
        if len(self.item_list) == 0:
            return 'There are no items in the shopping list. Please insert at least one item and try again'
        if len(self.email_list) == 0:
            return 'There are no emails in the shopping list. Please insert at least one email and try again'
        total_per_email = self.item_list_total_price // len(self.email_list)
        remainder_value = self.item_list_total_price % len(self.email_list)
        emails_to_add_remainder = self.email_list[-remainder_value:]
        price_per_email = {}
        for email in self.email_list:
            price_per_email[email] = math.floor(total_per_email)
            remainder_value += self.item_list_total_price % len(self.email_list)
            if remainder_value > 0 and email in emails_to_add_remainder:
                price_per_email[email] += 1
        return price_per_email
