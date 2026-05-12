# Question 2:
# Write a Python program to calculate the sum of a list of numbers using recursion.

def recursive_sum(data):
    total = 0

    # Go through each item in the list
    for item in data:
        # If the item is itself a list, recursively sum it
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            # Otherwise, add the number directly
            total += item

    return total