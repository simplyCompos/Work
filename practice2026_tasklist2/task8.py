from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def init(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class Rectangle(Shape):
    def init(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
