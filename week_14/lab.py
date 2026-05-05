class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()
    
    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()
    
basketball_court = Rectangle(15, 28)
soccer_field = Rectangle(75, 110)

print(f"{basketball_court} area: {basketball_court.area()}")
print(f"{soccer_field} area: {soccer_field.area()}")

print(f"Are areas equal? {basketball_court == soccer_field}")
print(f"Is basketball court smaller? {basketball_court < soccer_field}")
print(f"Is soccer field larger? {soccer_field > basketball_court}")