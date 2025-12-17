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

    def update(self, dt):
        """
        Velocity Verlet integrace:
        r(t+dt) = r(t) + v(t)*dt + 0.5*a(t)*dt^2
        v(t+dt) = v(t) + 0.5*(a(t) + a(t+dt))*dt
        """
        # předpokládáme, že self.force je již spočítána
        new_acceleration = self.force / self.mass
        # aktualizace pozice
        self.position += self.velocity * dt + self.acceleration * (0.5 * dt**2)
        # dočasná proměnná pro starou akceleraci
        old_acceleration = self.acceleration
        # nová akcelerace se uloží po výpočtu sil znovu v simulaci
        self.acceleration = new_acceleration
        # aktualizace rychlosti (budeme potřebovat novou sílu po compute_forces)
        self.velocity += old_acceleration * (0.5 * dt)  # částečný update, dokončeno po recompute_forces

    def reset_force(self):
        self.force = Vector(0.0, 0.0)
    