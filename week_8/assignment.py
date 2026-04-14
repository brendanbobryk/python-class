print("Excercise 1:\n---------------") # Check for leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

print("\nExcercise 2:\n---------------") # H.C.F.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Replaces a with b, reassigns (a % b) to b
# Loops until no remainder, leaving value in a as HCF
while b != 0:
    a, b = b, a % b

print("HCF is:", a)

print("\nExcercise 3:\n---------------") # Check if string s is a palidrome
s = input("Enter a string: ")

if s == s[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

print("\nExcercise 4:\n---------------") # Combine lists to a dictionary using zip
list1 = [1, 5, 7, 8, 11]
list2 = ['Canada', 'Germany', 'Holland', 'Italy']

result = dict(zip(list1, list2))

print(result)