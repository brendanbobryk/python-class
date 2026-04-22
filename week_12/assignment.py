import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

# First derived class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Method overriding
    def area(self):
        return math.pi * self.radius ** 2

# Second derived class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method overriding
    def area(self):
        return self.length * self.width

# Polymorphism
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(2.5),
    Rectangle(10, 3)
]

# Different behaviours within the same method call
for shape in shapes:
    print(f"Area: {shape.area():.2f}")