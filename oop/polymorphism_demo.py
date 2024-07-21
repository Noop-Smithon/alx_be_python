import math

class Shape:
    def area(self):
        # Calculate the area of the shape.
        raise NotImplementedError("Subclasses must override area() method")

class Rectangle(Shape):
    def __init__(self, length, width):
        # Initializes a Rectangle instance with the given length and width.
        self.length = length
        self.width = width

    def area(self):
        # Calculate the area of the rectangle.
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        # Initializes a Circle instance with the given radius.
        self.radius = radius

    def area(self):
        # Calculate the area of the circle.
        return math.pi * (self.radius ** 2)