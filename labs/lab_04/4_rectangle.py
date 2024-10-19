class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle1 = Rectangle(width=2, height=4)

print(rectangle1.area())
