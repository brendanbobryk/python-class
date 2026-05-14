# Question 4:
# Write a Python program to find the greatest common divisor (GCD) of two integers using 
#   recursion.

def gcd(a, b):
    if b == 0:              # Base case: when b is 0, a is the GCD
        return a

    return gcd(b, a % b)    # Recursive case: apply Euclid's algorithm (see below)

# Test inputs
num1 = 48
num2 = 18

result = gcd(num1, num2)

# Display results
print("First number:", num1)
print("Second number:", num2)
print("The GCD is:", result)

# Euclid's algorithm:
# Euclid's algorithm is a fast method for finding the Greatest Common Divisor (GCD) of 
#   two integers
# Instead of testing every possible divisor, Euclid's algorithm repeatedly applies
#   gcd(a,b) = gcd(b,a mod b)
#
# a mod b is the remainder when a is divided by b
# The process continues until the second number becomes 0
# At that point, the first number is the GCD