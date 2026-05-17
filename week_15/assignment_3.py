# Question 3:
# Write a Python program to generate and print a list of the first and last 5 elements 
#   where the values are square numbers between 1 and 30 (both included).

# Create a list of square numbers from 1 to 30
squares = [x ** 2 for x in range(1, 31) if 1 <= x ** 2 <= 30]

# Combine the first 5 and last 5 elements
result = squares[:5] + squares[-5:]

# Display results
print("Square numbers between 1 and 30:")
print(squares)

print("\nFirst and last 5 elements:")
print(result)

# Added an additioanl test case to demonstrate functionality on a larger domain,
#   instead of 30, I use 500
squares = [x ** 2 for x in range(1, 501) if 1 <= x ** 2 <= 500]
result = squares[:5] + squares[-5:]
print ("\nAdditional test case:")
print("Square numbers between 1 and 500:")
print(squares)                              # This will print 22 unqiue elements
print("\nFirst and last 5 elements:")
print(result)