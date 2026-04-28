from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, c):
        self.colour = c     # assigns value of c to colour attribute
    
    def get_colour(self):
        return self.colour  # returns value of colour
    
    @abstractmethod
    def get_area(self):     # abstract method
        pass

# Derived class
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)         # calls super(c) to initialize the color
        self.side = side            # assigns the value to side.
    
    def get_area(self):
        return self.side * self.side    # returns the area of the square
    
# example inputs
colour = "blue"
side = 7.0

s = Square(colour, side)                # creates object
print(s.get_colour(), s.get_area())     # prints colour and area of object