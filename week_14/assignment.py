class Number:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an int or float")
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return Number(self.value + other)
    
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        return Number(self.value - other)
    
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        return Number(self.value * other)
    
    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Number(self.value / other.value)
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Number(self.value / other)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Number({self.value})"