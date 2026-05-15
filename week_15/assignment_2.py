# Question 2:
# Define a ShoppingCart class representing a shopping cart. It has an attribute called 
#   items, which is initially an empty list.
# The "add_item()" method takes an item name and quantity as arguments and adds them as 
#   a tuple to the items list. This adds the item to the cart.
# The "remove_item()" method removes the first occurrence of an item with the specified 
#   name from the items list. It iterates over the list and checks if the current item's 
#   name matches the specified name. If a match is found, it removes the item from the 
#   list and breaks out of the loop.
# The "calculate_total()" method calculates and returns the total quantity of all items 
#   in the cart. It iterates over the items list and accumulates the quantity of each 
#   item.
# Calculate and display the total quantity of items using the calculate_total() method.

class ShoppingCart:
    def __init__(self):
        self.items = []                 # Start with an empty list of items

    def add_item(self, item_name, quantity):
        self.items.append((item_name, quantity))    # Add the item as a tuple

    def remove_item(self, item_name):
        for item in self.items:         # Remove the first item with the matching name
            if item[0] == item_name:
                self.items.remove(item)
                break
    
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total