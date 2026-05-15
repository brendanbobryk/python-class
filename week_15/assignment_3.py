# Question 3:
# Write a Python program to generate and print a list of the first and last 5 elements 
#   where the values are square numbers between 1 and 30 (both included).

squares = [x ** 2 for x in range(1, 31) if 1 <= x ** 2 <= 30]