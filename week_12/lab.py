# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# First derived class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Second derived class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Third derived class
class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

# Fourth derived class
class Trapezoid(Shape):
    def __init__(self, a, b, height):
        self.a = a  # parallel side 1
        self.b = b  # parallel side 2
        self.height = height

    def area(self):
        return 0.5 * (self.a + self.b) * self.height

# Polymorphic function
def print_area(shape):
    print(f"{shape.__class__.__name__} Area: {shape.area()}")

shapes = [
    Triangle(10, 5),
    Square(4),
    Parallelogram(6, 3),
    Trapezoid(4, 6, 5)
]

for s in shapes:
    print_area(s)