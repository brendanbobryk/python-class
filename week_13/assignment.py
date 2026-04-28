from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, c):
        self.colour = c