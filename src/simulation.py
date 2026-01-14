from vector import Vector

class Simulation:
    def __init__(self, dt: float):
        self.bodies = []
        self.dt = float(dt)

    def add_body(self, body):
        self.bodies.append(body)

    def compute_forces(self):
        #resetuji sily pro vsechna telesa aby nedochazelo k akumulaci sil z jednotlivych kroku
        for body in self.bodies:
            body.reset_force()
        #pro kazde teleso
        for body in self.bodies:
            #se podivam na ostatni telesa
            for other in self.bodies:
                #pokud to neni to same teleso, vektorove sectu gravitacni silu pomoci add_force
                if body != other:
                    body.add_force(other)

    def step(self): #vyuziva Velocity verlet
        dt = self.dt
        # 1) Update pozic podle staré rychlosti a akcelerace
        for body in self.bodies:
            body.position += body.velocity * dt + body.acceleration * (0.5 * dt**2)

        # 2) Přepočítej síly pro novou pozici
        self.compute_forces()

        # 3) Aktualizuj rychlosti podle nové akcelerace
        for body in self.bodies:
            new_acceleration = body.force / body.mass
            body.velocity += 0.5 * (body.acceleration + new_acceleration) * dt # prumer stare a nove akcelerace
            body.acceleration = new_acceleration
