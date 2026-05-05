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