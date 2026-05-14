# Question 4:
# Write a Python program to find the greatest common divisor (GCD) of two integers using 
#   recursion.

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)