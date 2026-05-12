# Question 1:
# Write a Python function to find the maximum of three numbers.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
