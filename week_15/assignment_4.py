# Question 4:
# Write a Python program to find the greatest common divisor (GCD) of two integers using 
#   recursion.

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

# Test inputs
num1 = 48
num2 = 18

result = gcd(num1, num2)

# Display results
print("First number:", num1)
print("Second number:", num2)
print("The GCD is:", result)