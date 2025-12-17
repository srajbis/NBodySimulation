import math
from vector import Vector

G = 6.67430e-11  # gravitační konstanta

class Body:
    def __init__(self, name, mass, position: Vector, velocity: Vector, sim_color):
        self.name = name
        self.mass = float(mass)
        self.position = position
        self.velocity = velocity
        self.force = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.sim_color = sim_color

    def add_force(self, other):
        """Přidá gravitační sílu působící od 'other'"""
        distance = other.position - self.position
        r = distance.mag()
        if r == 0:
            return
        force_magnitude = G * self.mass * other.mass / r**2
        force = distance.normalize() * force_magnitude
        self.force += force

    def reset_force(self):
        self.force = Vector(0.0, 0.0)
    