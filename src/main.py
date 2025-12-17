import math
from simulation import Simulation
from body import Body
from vector import Vector
from visualize import animate_trajectories

sim = Simulation(dt=3600)  # 1 hod timestep

# parametry dvou slunci
d = 2e11
G = 6.67430e-11
M_sun = 1.989e31

# circular speed of each sun
v_sun = math.sqrt(G*M_sun / (d/2)) / 10
Sun1 = Body("Sun1", M_sun, Vector(-d/2, 0), Vector(0,  v_sun), sim_color="orange")
Sun2 = Body("Sun2", M_sun, Vector(d/2,  0), Vector(0, -v_sun), sim_color="red")

#smaller planet orbiting both suns
r_planet = 2 * d
v_planet = math.sqrt(G * (2*M_sun) / r_planet)
Planet = Body("Planet", 5.972e27, Vector(r_planet, 0), Vector(0, v_planet), sim_color="blue")

sim.add_body(Sun1) #pridani objektu do simulace
sim.add_body(Sun2)
sim.add_body(Planet)

positions = {b.name: [] for b in sim.bodies}

n_steps = 24 * 365 *1  # 1 year of one hour steps

for step in range(n_steps):
    sim.step()                   
    for b in sim.bodies:
        positions[b.name].append(Vector(b.position.x, b.position.y))

colors = {b.name: b.sim_color for b in sim.bodies} #z objektu Body vezme jmeno a barvu pro vizualizaci

animate_trajectories(positions, interval=1, colors = colors) #volani fce ze souboru visualize.py
print("Simulation complete.")
