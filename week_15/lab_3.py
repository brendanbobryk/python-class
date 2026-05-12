# Question 3:
# Write a Python program to sum all the items in a list.

def sum_list(numbers):
    total = 0

    for number in numbers:  # Loop through each number in the list and add it to total
        total += number

    return total

my_list = [10, 20, 30, 40, 50]

result = sum_list(my_list)

print("The list is:", my_list)
print("The sum of all items in the list is:", result)