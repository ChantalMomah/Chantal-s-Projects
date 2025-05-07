import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Creating an instance of the Circle class
my_circle = Circle(5)

# Computing the area and perimeter (circumference) of the circle
print("Area of the circle:", my_circle.area())
print("Perimeter (Circumference) of the circle:", my_circle.perimeter())