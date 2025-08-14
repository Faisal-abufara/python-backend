import math

class Shape:
    def __init__(self, color="black"):
        self.color = color

    def area(self):
        raise NotImplementedError("All Shapes must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("All Shapes must implement abstract method")

    def __str__(self):
        return f"Shape(color={self.color})"

class Circle(Shape):
    def __init__(self, radius, color="black"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"

class Rectangle(Shape):
    def __init__(self, width, height, color="black"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"

shapes = [
    Circle(5, "red"),
    Rectangle(4, 6, "blue")
]

for shape in shapes:
    print(shape)
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 30)
