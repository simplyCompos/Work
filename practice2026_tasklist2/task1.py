import math

def rectangle_area(a, b):
    return a * b

def circle_area(r):
    return math.pi * r * r

print(rectangle_area(4, 5))
print(circle_area(3))

class Rectangle:
    def init(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle:
    def init(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r
