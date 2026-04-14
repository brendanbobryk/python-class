print("Excercise 1:\n---------------")
A = [[6, 8, -4],
     [5, 0, 11],
     [3, 2, -2]]

B = [[3, 4, 8],
     [4, 6, -9],
     [5, 11, 1]]

R = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        R[i][j] = A[i][j] + B[i][j]

print(R)

print("\nExcercise 2:\n---------------")
square_dict = {}

for i in range(11, 21):
    square_dict[i] = i**2

print(square_dict)

print("\nExcercise 3:\n---------------")
A = {3,5,6,8}
B = {3,4,6,9,10}

print("Difference: ", A - B)
print("Symmetric Difference: ", A ^ B)
print("Intersection: ", A & B)
print("Union: ", A | B)

print("\nExcercise 4:\n---------------")
fruits = ("strawberries", "oranges", "apples")

print("Tuples cannot be changed after creation.")
print("So I created a new tuple containing 'bananas'.")
print("I then concatenate it to the original tuple using +.")
print("The result is assigned back to fruits.")

fruits = fruits + ("bananas",)

print(fruits)