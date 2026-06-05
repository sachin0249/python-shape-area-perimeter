# Python program to calculate area and perimeter/circumference
# of Triangle, Rectangle, Circle, and Square

class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Creating objects

triangle = Triangle(10, 8, 5, 6, 7)
rectangle = Rectangle(10, 5)
circle = Circle(7)
square = Square(4)

# Triangle
print("Triangle")
print("Area =", triangle.area())
print("Perimeter =", triangle.perimeter())

# Rectangle
print("\nRectangle")
print("Area =", rectangle.area())
print("Perimeter =", rectangle.perimeter())

# Circle
print("\nCircle")
print("Area =", circle.area())
print("Circumference =", circle.circumference())

# Square
print("\nSquare")
print("Area =", square.area())
print("Perimeter =", square.perimeter())
