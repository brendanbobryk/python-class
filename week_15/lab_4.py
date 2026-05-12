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

    # Print table reservations
    def print_table_reservations(self):
        print("TABLE RESERVATIONS")
        print("-" * 30)
        for reservation in self.book_table:
            print(
                f"Customer: {reservation['customer']}, "
                f"Table Number: {reservation['table']}"
            )
        print()

    # Print customer orders
    def print_customer_orders(self):
        print("CUSTOMER ORDERS")
        print("-" * 30)
        for order in self.customer_orders:
            items_string = ", ".join(order["items"])
            print(
                f"Customer: {order['customer']}, "
                f"Ordered: {items_string}"
            )
        print()

# Create a Restaurant object
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Burger", 12.99)
restaurant.add_item_to_menu("Pizza", 15.50)
restaurant.add_item_to_menu("Pasta", 13.75)
restaurant.add_item_to_menu("Salad", 9.25)
restaurant.add_item_to_menu("Soda", 2.50)

# Make table reservations
restaurant.book_tables("Alice", 1)
restaurant.book_tables("Bob", 2)
restaurant.book_tables("Charlie", 3)

# Take customer orders
restaurant.customer_order("Alice", ["Burger", "Soda"])
restaurant.customer_order("Bob", ["Pizza", "Salad"])
restaurant.customer_order("Charlie", ["Pasta", "Soda"])

# Print all information
restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()