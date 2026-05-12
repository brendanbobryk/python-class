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

list1 = [1, 2, [3]]
print("Input:", list1)
print("Output:", recursive_sum(list1))

list2 = [[4, 5], [7, 8, [20]], 100]
print("\nInput:", list2)
print("Output:", recursive_sum(list2))

list3 = [[1, 2, 3], [4, [5, 6]], 7]
print("\nInput:", list3)
print("Output:", recursive_sum(list3))