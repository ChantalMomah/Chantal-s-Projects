class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating an instance of the Rectangle class
my_rectangle = Rectangle(7, 4)

# Computing the area and perimeter of the rectangle
print("Area of the rectangle:", my_rectangle.area())
print("Perimeter of the rectangle:", my_rectangle.perimeter())