print("Excercise 4.1:\n---------------")
a = True
b = True
print(a)
print(b)
print(a != b)
print(a == b)
print(a < b)
print(a > b)

print("\nExcercise 4.2:\n---------------")
x = 6
y = 10
print(x)
print(y)
print(x % 3 == 0 and y % 2 == 0)
print(x % 5 == 0 or y % 3 == 0)
print(x % 2 == 0 and not(y % 3 == 0))

print("\nExcercise 4.3:\n---------------")
num = 30
print("Checking divisibility for num =", num)
# Check num
if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("num is divisible by 2, 3, and 5")

elif num % 2 == 0 and num % 3 == 0:
    print("num is divisible by 2 and 3 (but not 5)")

elif num % 2 == 0 and num % 5 == 0:
    print("num is divisible by 2 and 5 (but not 3)")

elif num % 3 == 0 and num % 5 == 0:
    print("num is divisible by 3 and 5 (but not 2)")

elif num % 2 == 0:
    print("num is divisible by 2")

elif num % 3 == 0:
    print("num is divisible by 3")

elif num % 5 == 0:
    print("num is divisible by 5")

else:
    print("num is not divisible by 2, 3, or 5")

# Now check num/2
half = num / 2
print("\nChecking divisibility for num/2 =", half)

if half % 2 == 0 and half % 3 == 0 and half % 5 == 0:
    print("num/2 is divisible by 2, 3, and 5")

elif half % 2 == 0 and half % 3 == 0:
    print("num/2 is divisible by 2 and 3 (but not 5)")

elif half % 2 == 0 and half % 5 == 0:
    print("num/2 is divisible by 2 and 5 (but not 3)")

elif half % 3 == 0 and half % 5 == 0:
    print("num/2 is divisible by 3 and 5 (but not 2)")

elif half % 2 == 0:
    print("num/2 is divisible by 2")

elif half % 3 == 0:
    print("num/2 is divisible by 3")

elif half % 5 == 0:
    print("num/2 is divisible by 5")

else:
    print("num/2 is not divisible by 2, 3, or 5")