# Question 2:
# Write a Python program to calculate the sum of a list of numbers using recursion.

def recursive_sum(data):
    total = 0

    for item in data:                       # Go through each item in the list
        if isinstance(item, list):  # If the item is itself a list, recursively sum it
            total += recursive_sum(item)
        else:                               # Otherwise, add the number directly
            total += item

    return total

# Test input 1
list1 = [1, 2, [3]]
print("Input:", list1)  # Display both original and result
print("Output:", recursive_sum(list1))

# Test input 2
list2 = [[4, 5], [7, 8, [20]], 100]
print("\nInput:", list2)    # Display both original and result
print("Output:", recursive_sum(list2))

# Test input 3
list3 = [[1, 2, 3], [4, [5, 6]], 7]
print("\nInput:", list3)    # Display both original and result
print("Output:", recursive_sum(list3))