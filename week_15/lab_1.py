# Question 1:
# Write a Python function to find the maximum of three numbers.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = 15
num2 = 25
num3 = 10

largest = maximum(num1, num2, num3)

print("The three numbers are:", num1, num2, num3)
print("The maximum of the three numbers is:", largest)