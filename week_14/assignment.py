class Number:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an int or float")
        self.value = value

    def __add__(self, other):   # Addition
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return Number(self.value + other)
    
    def __sub__(self, other):   # Subtraction
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return Number(self.value - other)
    
    def __mul__(self, other):   # Multiplication
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return Number(self.value * other)
    
    def __truediv__(self, other):   # Division
        if isinstance(other, Number):
            if other.value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Number(self.value / other.value)
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Number(self.value / other)
    
    def __str__(self):  # User-friendly string
        return str(self.value)
    
    def __repr__(self): # Developer representation
        return f"Number({self.value})"

# Example objects
a = Number(10)
b = Number(5)

# Examples using two objects
print(a + b)   # 15
print(a - b)   # 5
print(a * b)   # 50
print(a / b)   # 2.0

# Examples with raw numbers
print(a + 3)   # 13
print(a * 2.5) # 25.0