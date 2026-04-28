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

