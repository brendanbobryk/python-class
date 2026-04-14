print("Excercise 1:\n---------------")
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("John", "Doe"))  # using example name John Doe

print("\nExcercise 2:\n---------------")
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)
    
print("Please enter a non-negative integer: ")
number = int(input()) # retrieving an integer from the user
print(f"{number}! =", factorial(number)) 