from item import Item
from shopping_list import ShoppingList


def main():
    item_list = [Item(price=100)]
    email_list = ['user1@example.com', 'user2@example.com', 'user3@example.com']
    shopping_list = ShoppingList(item_list, email_list)
    print(shopping_list.calculate_payment_per_email())


if __name__ == '__main__':
    main()
