# Question 4:
# Write a Python class Restaurant with attributes like menu_items, book_table, and 
#   customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
#   Now add items to the menu.
#   Make table reservations.
#   Take customer orders.
#   Print the menu.
#   Print table reservations.
#   Print customer orders.

class Restaurant:
    def __init__(self):
        # Dictionary to store menu items and their prices
        self.menu_items = {}

        # List to store table reservations
        self.book_table = []

        # List to store customer orders
        self.customer_orders = []

    # Add an item (and its price) to the menu
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    # Reserve a table (for a customer)
    def book_tables(self, customer_name, table_number):
        reservation = {
            "customer": customer_name,
            "table": table_number
        }
        self.book_table.append(reservation)
    
    # Take a customer's order
    def customer_order(self, customer_name, items):
        order = {
            "customer": customer_name,
            "items": items
        }
        self.customer_orders.append(order)

    # Print the menu
    def print_menu(self):
        print("MENU")
        print("-" * 30)
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")
        print()
