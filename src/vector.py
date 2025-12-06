#class for calculating 2D vector operations - addition, subtraction, multiplication, division, magnitude, normalization and other needed functions

import math

class Vector:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)   

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float) -> "Vector":
        """Násobení skalárem zleva: a * v."""
        return self.__mul__(scalar)
    
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        m = self.mag()
        if m == 0:
            return Vector(0,0)
        return self / m
    
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
