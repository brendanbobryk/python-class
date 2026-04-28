from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, c):
        self.colour = c
    
    def get_colour(self):
        return self.colour
    
    @abstractmethod
    def get_area(self):
        pass

# Derived class
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    
    def get_area(self):
        return self.side * self.side
    
colour = "blue"
side = 7.0

s = Square(colour, side)
print(s.get_colour(), s.get_area())