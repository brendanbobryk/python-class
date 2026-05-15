# Question 3:
# Write a Python program to generate and print a list of the first and last 5 elements 
#   where the values are square numbers between 1 and 30 (both included).

# Create a list of square numbers from 1 to 30
squares = [x ** 2 for x in range(1, 31) if 1 <= x ** 2 <= 30]

# Combine the first 5 and last 5 elements
result = squares[:5] + squares[-5:]

# Display the lists
print("Square numbers between 1 and 30:")
print(squares)

print("\nFirst and last 5 elements:")
print(result)