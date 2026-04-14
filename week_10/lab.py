print("Excercise 1 & 2:\n---------------")
with open("lab_file.txt", "w") as file:
    file.write("Hello, world!")

with open("lab_file.txt", "r") as file:
    print(file.read())